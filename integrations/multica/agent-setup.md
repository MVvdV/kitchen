# Kitchen agent setup in Multica

The [team rules](../../governance/team-organisation.md) define portable roles, authority, and review requirements. This roster records their Multica bindings. Keep the workspace agent IDs when changing display names. Resolve role bindings afresh when applying the blueprint in another workspace.

| Multica agent | Runtime | Model | Reasoning | Role |
| --- | --- | --- | --- | --- |
| Engineer I | Codex | `gpt-6.2-sol` | Medium | Build owner and Council reviewer for architecture and implementation |
| Engineer II | Claude Code | `claude-opus-5-5` | Medium | Build owner and Council reviewer for architecture and implementation |
| Product & Design II | Claude Code | `claude-opus-5-5` | Medium | Shape owner and Council reviewer for product and design |
| Product & Design I | Codex | `gpt-6.1-terra` | High | Shape owner, design peer reviewer, and Council visual critic |
| Chief of Staff | Codex | `gpt-6.2-sol` | Medium | Cross-project setup, blueprint governance, and approved rollout |
| Delivery | Codex | `gpt-6.2-sol` | High | Planning, reconciliation, dispatch, and recovery |
| Release | Codex | `gpt-6.2-sol` | Medium | Prepare, publish, and verify approved releases |
| Chairman | Claude Code | `claude-opus-5-5` | High | Council leader and independent Verification |
| Analysis Assistant | Codex | `gpt-6-luna` | High | Bounded evidence analysis |
| Operations Assistant | Claude Code | `claude-haiku-5-5` | Medium | Bounded operational evidence and configuration checks |

## Skills and tools

Give both designers the same Shape, prototype, and FigCraft skills. Give both engineers the same Build and delegation skills. Bind `peer-review` to both pairs and Chairman. Give Chairman `review-options` for convening reviews and synthesizing findings. The assistants use the portable [evidence report](../../templates/evidence-report.md) format.

Resolve the selected design tool from the project setup. Assign its tool skill and workspace-managed MCP entry to the designers who use it. Keep tool selection, connection mapping, and machine settings in the project setup. Keep server registration and assignments in Multica. Verify the saved runtime, model, reasoning, visibility, skill bindings, and workspace MCP assignment before the human starts the first real issue. For projects with different design resources, use their own configured entry and check the active project's resource before editing. Onboard new FigCraft agents with the [concurrent work rules](../figcraft/README.md#concurrent-agent-work). Assign a distinct open file to each simultaneous writer and require explicit document targeting.

Use the existing Council squad with Chairman as leader and both designers and both engineers as members. Give each member the review role listed above. Chairman invites the relevant peers for each question and can mention either assistant separately for evidence. A Council mention reaches Chairman, who chooses reviewers. Record the question and exact revision on the issue. Chairman leaves the ticket with its owner while Council reviews it.

## Cross-project operations

Bind the [Chief of Staff](../../agents/chief-of-staff.md) role to one workspace agent and use its stable agent ID for integrations that need a binding. Use a Kitchen issue to record shared decisions and rollout evidence. For each affected project, record the effective workflow, relevant role and skill bindings, project variations, and blueprint revision as appropriate to the change. Compare live rules and runtime instructions with the approved blueprint before rollout.

The workspace operator initiates work or explicitly delegates configuration changes through an operations issue. The Operations Assistant can compare saved settings with the approved record and report gaps. Keep established project stage ownership and approvals in place. A schedule or automatic rollout requires a separately approved scope.

## Shape decision record

For a substantial Shape issue, maintain a short decision section in the issue description. Use a targeted description edit to preserve other edits. Record settled choices and evidence, open decisions, linked follow-ups and dependencies, and the live canvas reference. Update the section at meaningful checkpoints. Keep exploratory conversation in replies and use a separate linked Todo issue when a question needs its own shaping.

The frozen handoff identifies what the approval covers separately from the exploratory record. Delivery reconciles affected work and plans implementation from that scope.

## Dispatch

Multica workflow handoffs select one fixed destination. Set Shape and Build to **No handoff** so their columns can accept either peer. Store the Shape and Build guidance in both peer agents’ instructions because Multica clears the handoff instructions when the handler is removed. Preserve each project’s approval gates. Moving into either column now retains the current assignee and starts no run by itself.

- **Shape** The design approver moves the issue to Shape, then assigns either designer and starts the run. For a reviewer on an existing Shape ticket, mention the chosen peer with the review question and exact revision. The assignee continues to own the ticket. Designers may create a linked follow-up in Todo without assigning or starting it. See [Shape follow-up and reconciliation rules](../../workflows/runbook.md#split-and-reconcile-work-during-shape).
- **Build** Delivery records a chosen engineer and the planned revision before dispatch. Verify the item is eligible, move it to Build, and explicitly assign the selected engineer to start work. Apply this procedure to self-contained tickets and each eligible child in a wave.
- **Returns and recovery** Record the reason and pointer to the prior checkpoint before moving. Select the prior eligible stage owner or their available peer. Stop overlapping writers before a takeover. Check issue status, assignee, and active runs before retrying a partial handoff. If the intended owner is already assigned and there is no active or queued attempt, explicitly request continuation once on the issue instead of repeating the move.

The stable step owners for Plan Delivery, Verify, and release stages keep their normal handoff behavior. Use the [runtime compatibility check](README.md#runtime-compatibility-check) when updating this configuration. Observe the first applicable run in a project using the revised configuration before broader rollout and capture reusable findings in Kitchen.
