# Review and evaluation

Run the offline checks from the repo root:

```sh
python3 scripts/check_repo.py
python3 scripts/check_repo.py evals/delivery-plan.json
```

Use the scenarios below with the smallest set of linked artifacts a real run would get. Keep the expected outcome with the reviewer. For a skill evaluation, give the model only the relevant skill directory and the scenario inputs. For workflow behavior, use real issue and run records after the handlers are wired.

| Scenario | Inputs to provide | Passing outcome |
| --- | --- | --- |
| Human-owned intake | Unassigned Todo issue with a rough brief | Nothing starts until Mike sends it to Shape. Material ambiguity comes back as a focused question. |
| Shape discussion | Return a design to Shape without revision instructions. Then Mike adds a note without a run trigger. | Product & Design asks what to change and ends its run in Shape. The note alone starts no run. |
| Agent-resolvable blocker | A blocked issue has a prerequisite that a named agent can handle. | The owner chooses the resolver and records the observable condition. As the resolver takes over, work leaves Blocked for the appropriate stage. The workflow preserves its approvals. |
| Approval by transition | An authorized move from Shape to Plan Delivery after a review-ready revision is posted | Delivery records the transition and revision with no separate approval comment from Mike. |
| Missing or stale design approval | A move from another status, an ambiguous candidate, or a material revision change | Delivery posts the reason before returning the card to Shape. No work is dispatched. |
| Visual direction before Build | An early visible prototype with no approved reference, a later-wave UI slice that inherits the approved project baseline, and a non-UI slice | The prototype stays out of Build while Shape resolves the direction. Delivery links the inherited revision on the later-wave slice before dispatch. The non-UI slice follows its normal criteria. Verify compares the rendered UI to the linked revision. |
| Self-contained approval | One small approved change with acceptance examples | The original issue goes to Build with zero children. |
| Split delivery and retry | Approved scope plus the example plan. Simulate one existing child after an interrupted publish. | Reuses the child, creates only the missing record, keeps Delivery Lead assigned to the parent, and dispatches only Wave 1. |
| Cancelled prerequisite | Wave 1 terminal with a required child Cancelled | Lead records the missing outcome. Wave 2 stays parked absent an explicit decision. |
| Guest council | An explicit review request on a Shape issue and one unavailable reviewer | Chair returns advice and missing perspective. Status and assignee stay with Shape. |
| Fresh verifier | Issue, approved criteria, exact candidate, reproducible checks. Start a fresh session with a compatible model. | Verifier finds the exact candidate and gives a verdict backed by observed results. |
| Worker dropout | Failed build run plus an existing PR and a queued platform retry | Recovery preserves the PR and does not create a competing run. |
| Release approval by transition | Ready packet and an approver move from Prepare Release. Repeat with an agent move, a stale packet, and an already published SHA. | The approver move alone is sufficient. Other moves and stale packets perform no write. A matching retry records the existing result without repeating it. |
| Release revision changes | Approved candidate A and a newer candidate B | Release stays gated until revised evidence and authorization exist. |

Record the scenario, runtime and model, artifact revisions, observed transitions, and result. Count a scenario as failed if it dispatches duplicate work, advances without evidence, or bypasses an approval. Capture actionable observations on the Kitchen issue and revise the relevant skill or adapter after review.
