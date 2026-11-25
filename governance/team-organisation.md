# Team organisation

Staff Shape with two peer designers and Build with two peer engineers. Either peer can own a ticket from the start and carries the full responsibilities of the role. Select the owner based on continuity, availability, and the work at hand. Give the peers different model providers when compatible runtimes are available.

| Role | Responsibility |
| --- | --- |
| Product & Design | The two designers shape briefs, set visual direction, collaborate with the product approver, and own editable designs. Either designer can review the other’s work or own a new issue. |
| Engineering | The two engineers implement approved scope and deliver reproducible candidates. Either engineer can review the other’s work or own a new issue. |
| Council Chair | Choose reviewers for the question, collect independent findings before synthesis, and record evidence, dissent, and a recommendation. Formal verification remains independent of implementation. |
| Product, Architecture, and Visual Critics | Give advice within their disciplines. Visual Critic is an additional Council duty held by one designer. When that designer owns the design, invite the other designer to review it. |
| Analysis Assistant | Compare supplied artifacts, map evidence to the question, and flag gaps. |
| Operations Assistant | Collect CI, deployment, smoke-check, and rollback evidence for an exact candidate. |

## Ownership and handoffs

The product approver chooses the initial Shape owner. Delivery chooses the Build owner once approved scope and dependencies are ready. When returning work for revision, use the previous stage owner if available and select their peer when recovery needs it. Keep one issue owner and one writer for an editable design or implementation. Before transferring ownership, confirm the prior run has stopped and record the exact artifact or commit, completed checks, unfinished work, and next owner. If neither peer is available, leave the recorded checkpoint and use the workflow recovery process.

## Review and authority

Use one on-demand Council during the current stage. For consequential design or engineering decisions, ask an independent peer from the other provider to review the same pinned revision and criteria. Give each invited reviewer the same question and collect independent findings before synthesis. Reviewers leave findings for the issue owner. Reviewers who contributed edits to the candidate defer independent review to another eligible reviewer. If a perspective is unavailable, record it in the synthesis. The product approver resolves material scope and design choices.

Use [peer-review](../skills/peer-review/SKILL.md) for focused design or engineering review. Ask for another pass when a finding remains unresolved or a material revision needs it. The assistants are independently assignable and use the same [evidence report](../templates/evidence-report.md). They gather evidence. The stage owner makes the decision.
