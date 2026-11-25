# Kitchen agent setup in Multica

The [team rules](../../governance/team-organisation.md) define portable roles, authority, and review requirements. This roster records their Multica bindings. Keep the workspace agent IDs when changing display names. Resolve role bindings afresh when applying the blueprint in another workspace.

| Multica agent | Runtime | Model | Reasoning | Role |
| --- | --- | --- | --- | --- |
| Engineer I | Codex | `gpt-6.2-sol` | Medium | Build owner and Council reviewer for architecture and implementation |
| Engineer II | Claude Code | `claude-opus-5-5` | Medium | Build owner and Council reviewer for architecture and implementation |
| Product & Design II | Claude Code | `claude-opus-5-5` | Medium | Shape owner and Council reviewer for product and design |
| Product & Design I | Codex | `gpt-6.1-terra` | High | Shape owner, design peer reviewer, and Council visual critic |
| Delivery | Codex | `gpt-6.2-sol` | High | Planning, reconciliation, dispatch, and recovery |
| Release | Codex | `gpt-6.2-sol` | Medium | Prepare, publish, and verify approved releases |
| Chairman | Claude Code | `claude-opus-5-5` | High | Council leader and independent Verification |
| Analysis Assistant | Codex | `gpt-6-luna` | High | Bounded evidence analysis |
| Operations Assistant | Claude Code | `claude-haiku-5-5` | Medium | Bounded operational evidence collection |

## Skills and tools

Give both designers the same Shape, prototype, and FigCraft skills. Give both engineers the same Build and delegation skills. Bind `peer-review` to both pairs and Chairman. Give Chairman `review-options` for convening reviews and synthesizing findings. The assistants use the portable [evidence report](../../templates/evidence-report.md) format.

Assign both designers the workspace-managed FigCraft MCP entry for the project. In SynThesis, the entry is `figcraft-synthesis`. Keep its registration and assignments in Multica. Verify the saved runtime, model, reasoning, visibility, skill bindings, and workspace MCP assignment before the human starts the first real issue. For projects with different design resources, use their own configured entry and check the active project's resource before editing.

Use the existing Council squad with Chairman as leader and both designers and both engineers as members. Give each member the review role listed above. Chairman invites the relevant peers for each question and can mention either assistant separately for evidence. A Council mention reaches Chairman, who chooses reviewers. Record the question and exact revision on the issue. Chairman leaves the ticket with its owner while Council reviews it.

## Dispatch

Multica workflow handoffs select one fixed destination. Set Shape and Build to **No handoff** so their columns can accept either peer. Store the Shape and Build guidance in both peer agents’ instructions because Multica clears the handoff instructions when the handler is removed. Preserve each project’s approval gates. Moving into either column now retains the current assignee and starts no run by itself.

- **Shape** Mike moves the issue to Shape, then assigns either designer and starts the run. For a reviewer on an existing Shape ticket, mention the chosen peer with the review question and exact revision. The assignee continues to own the ticket.
- **Build** Delivery records a chosen engineer and the planned revision before dispatch. Verify the item is eligible, move it to Build, and explicitly assign the selected engineer to start work. Apply this procedure to self-contained tickets and each eligible child in a wave.
- **Returns and recovery** Record the reason and pointer to the prior checkpoint before moving. Select the prior eligible stage owner or their available peer. Stop overlapping writers before a takeover. Check issue status, assignee, and active runs before retrying a partial handoff. If the intended owner is already assigned and there is no active or queued attempt, explicitly request continuation once on the issue instead of repeating the move.

The stable step owners for Plan Delivery, Verify, and release stages keep their normal handoff behavior. Use the [runtime compatibility check](README.md#runtime-compatibility-check) when updating this configuration. Observe the first real SynThesis work before broader rollout and capture reusable findings in Kitchen.
