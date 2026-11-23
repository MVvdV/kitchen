# Kitchen Brigade

Kitchen maintains the shared delivery blueprint. Product projects use Kitchen Brigade for real delivery and provide the evidence Kitchen evaluates. Kitchen records and rolls out improvements that apply beyond the source project. The workflow defines who decides and what evidence is needed. Integrations describe how to apply those rules in individual tools.

| Path | What belongs here |
| --- | --- |
| `governance/` | [How Kitchen evaluates product runs and improves the blueprint](governance/blueprint-improvement.md) |
| `workflows/` | [Workflow](workflows/README.md), board blueprint, and [delivery and recovery rules](workflows/runbook.md) |
| `agents/` | [Shared agent instructions](agents/shared.md) and role instructions |
| `skills/` | Standalone skill directories using the Agent Skills format |
| `templates/` | Spec, delivery plan, handoff, council, and release records |
| `scripts/` | Offline repository and delivery-plan checks |
| `evals/` | [Evaluation scenarios](evals/README.md) and a worked delivery-plan fixture |
| `integrations/` | Tool-specific documentation for [Multica](integrations/multica/README.md) and [FigCraft](integrations/figcraft/README.md) |

The workflow, role instructions, templates, and core skills can be reused with another orchestrator. Map its statuses, role assignments, human approval events, and artifact links to the same workflow. Install skills and register MCP connections through that orchestrator's tooling. Tooling skills apply only when a ticket uses the corresponding tool.

A fresh run must be able to resume from the issue record and linked artifacts. Product specifications, source, and product-specific checks belong in the relevant application repository. Choose a model with the tools and permissions required for its role.

Run `python3 scripts/check_repo.py` for offline repository checks. Pass a delivery-plan JSON path to validate that plan. Observe live agent behavior through real product runs and record broadly applicable findings in Kitchen.
