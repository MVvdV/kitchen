# Kitchen Brigade workflow

Product projects use this delivery board. Mike creates the first issue in Todo and initiates Shape. Council is an optional advisory review during a stage. Kitchen’s [blueprint improvement process](../governance/blueprint-improvement.md) uses evidence from those product projects.

| Column | Intended handler | Exit |
|---|---|---|
| Todo | None | Mike sends intake to Shape. Park delivery slices here unassigned until Delivery moves eligible work to Build. |
| Shape | Product & Design | Post the proposed spec and send to Approve Design. Honour any explicit council hold. |
| Approve Design | Mike | Approve the spec and send to Plan Delivery, or return to Shape. |
| Plan Delivery | Delivery Lead | Send a self-contained issue to Build. Publish a split plan and move the parent to In Delivery. |
| In Delivery | None, retain Delivery Lead | Advance eligible waves on native wakeups. Send the final candidate to Prepare Release or close work that needs no release. |
| Build | Engineering | Post evidence and hand off to Verify. Return material scope changes to Shape. |
| Verify | Verification | Send defects to Build. Close integrated and verified children, or send a standalone release candidate to Prepare Release. |
| Prepare Release | Release | Record the release packet and send to Approve Release. |
| Approve Release | Mike | Initiate the authorized release and move to Verify Release, or return to Prepare Release. |
| Verify Release | Release | Confirm the deployed revision and finish, or record the failure in Blocked. |
| Blocked | None, retain current owner | Record the obstacle and resume point. Resume Engineering at Build. |
| Done | None | Agreed criteria verified. |
| Cancelled | None | Reason for dropping the work recorded. |

## Labels

Issue types: `initiative`, `slice`, `discovery`, `bug`, `enhancement`, `factory-improvement`. Flags: `risk:high` for consequential changes, `needs-info` for a missing input, and `council` for an open advisory review. Use `discovery` for research, feasibility work, and prototypes that answer a specific question. This list is the complete issue-label vocabulary for projects using Kitchen Brigade. If an approved label is unavailable, leave the issue unlabelled. Clear temporary flags when resolved. The step owner checks the criteria before moving the issue. A label alone never dispatches work.
