"""Check the Kitchen blueprint and delivery-plan fixtures offline."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_blueprint():
    blueprint = json.loads((ROOT / "workflows/kitchen-brigade.json").read_text())
    roles = blueprint["roles"]
    columns = blueprint["columns"]
    by_key = {column["key"]: column for column in columns}
    require(len(by_key) == len(columns), "Duplicate workflow column key")
    for column in columns:
        handler = column["handler"]
        require(handler is None or handler in roles, f"Unknown handler: {handler}")
        missing = set(column["targets"]) - by_key.keys()
        require(not missing, f"Unknown transition targets for {column['key']}: {missing}")
    for key in blueprint["owner_retained"]:
        require(by_key[key]["handler"] is None, f"{key} must retain its owner")
    require("backlog" not in by_key, "Backlog must be omitted")
    require(columns[0]["key"] == "todo" and by_key["todo"]["handler"] is None, "Todo must be first and have no handler")
    require(by_key["build"]["handler"] == "engineering", "Build must dispatch Engineering")
    require("approve_design" not in by_key, "Design approval is the move from Shape to Plan Delivery")
    require(by_key["shape"]["handler"] == "product-and-design" and "plan_delivery" in by_key["shape"]["targets"], "Shape must dispatch Product & Design and support the Plan Delivery handoff")
    require(by_key["plan_delivery"]["handler"] == "delivery-lead" and "shape" in by_key["plan_delivery"]["targets"], "Delivery must be able to return issues to Shape")
    ready = by_key["approve_release"]
    release = by_key["verify_release"]
    require(ready["name"] == "Ready for Release" and ready["handler"] is None, "Ready for Release must wait without a handler")
    require(release["name"] == "Release & Verify" and release["handler"] == "release", "Release & Verify must dispatch Release")
    require(release["approval"] == {"from": "approve_release", "actor": "project-approver"}, "Release approval must be the project approver's move from Ready for Release")
    require("approve_release" in by_key["prepare_release"]["targets"] and "verify_release" in ready["targets"], "The release workflow must pass through Ready for Release")
    require("prepare_release" in release["targets"], "Release must be able to return stale work to preparation")
    for path in [*roles.values(), blueprint["advisory_review"], blueprint["runbook"]]:
        if path is not None:
            require((ROOT / path).is_file(), f"Missing workflow reference: {path}")


def check_skills():
    paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    require(bool(paths), "No skills found")
    names = set()
    for path in paths:
        frontmatter = re.match(r"---\n(.*?)\n---\n", path.read_text(), re.DOTALL)
        require(frontmatter, f"Missing skill frontmatter: {path}")
        name = path.parent.name
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), f"Invalid skill name: {name}")
        header = frontmatter.group(1)
        require(f"name: {name}" in header.splitlines(), f"Skill name mismatch: {path}")
        require(re.search(r"^description: \S", header, re.MULTILINE), f"Missing description: {path}")
        require(name not in names, f"Duplicate skill name: {name}")
        names.add(name)
    return len(paths)


def check_plan(path):
    plan = json.loads(path.read_text())
    require(bool(plan["scope_revision"].strip()), "A plan needs an approved scope revision")
    mode = plan["mode"]
    slices = plan["slices"]
    require(mode in {"single", "split"}, "Mode must be single or split")
    if mode == "single":
        require(not slices, "Single-ticket work must have no slices")
        return
    require(len(slices) >= 2, "A split plan needs at least two slices")
    by_key = {item["key"]: item for item in slices}
    require(len(by_key) == len(slices), "Duplicate slice key")
    for item in slices:
        key = item["key"]
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key), f"Invalid slice key: {key}")
        require(bool(item["title"].strip()), f"{key} needs a title")
        criteria = item["acceptance"]
        require(bool(criteria) and all(criterion.strip() for criterion in criteria), f"{key} needs acceptance evidence")
        require(type(item["wave"]) is int and item["wave"] > 0, f"Invalid wave for {key}")
    for item in slices:
        for dependency in item["depends_on"]:
            require(dependency in by_key, f"Unknown dependency: {dependency}")
            require(by_key[dependency]["wave"] < item["wave"], f"{item['key']} must follow {dependency}")
    waves = sorted({item["wave"] for item in slices})
    require(waves == list(range(1, len(waves) + 1)), "Waves must start at 1 and have no gaps")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", nargs="?", type=Path, help="Validate a delivery plan instead of the repository")
    args = parser.parse_args()
    try:
        if args.plan:
            check_plan(args.plan)
            print(f"Valid delivery plan: {args.plan}")
        else:
            check_blueprint()
            count = check_skills()
            check_plan(ROOT / "evals/delivery-plan.json")
            print(f"Validated workflow references, {count} skills, and delivery-plan fixture.")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
