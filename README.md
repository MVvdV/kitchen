# Kitchen Brigade

Kitchen is the home for the workflow, reusable skills, role instructions, templates, scripts, and evals. The workflow defines who decides and what evidence is needed. Integrations describe how to apply those rules in individual tools.

| Path | What belongs here |
| --- | --- |
| `workflows/` | [Workflow](workflows/README.md), board blueprint, and [delivery and recovery rules](workflows/runbook.md) |
| `agents/` | [Shared agent instructions](agents/shared.md) and role instructions |
| `skills/` | Standalone skill directories using the Agent Skills format |
| `templates/` | Spec, delivery plan, handoff, council, and release records |
| `scripts/` | Offline repository and delivery-plan checks |
| `evals/` | [Evaluation scenarios](evals/README.md) and a worked delivery-plan fixture |
| `integrations/` | Tool-specific documentation, beginning with [Multica](integrations/multica/README.md) |

A fresh run must be able to resume from the issue record and linked artifacts. Product specifications, source, and product-specific checks belong in the relevant application repository. Choose a model with the tools and permissions required for its role.

Run `python3 scripts/check_repo.py` for offline repository checks. Pass a delivery-plan JSON path to validate that plan. Run the evaluation scenarios separately to observe agent behavior.

This checkout is ready for review. Set the remote when the Kitchen repository is available.
