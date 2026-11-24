# Kitchen Brigade workflow

Product projects use this delivery board. Mike creates the first issue in Todo and initiates Shape. Council is an optional advisory review during a stage. Kitchen’s [blueprint improvement process](../governance/blueprint-improvement.md) uses evidence from those product projects.

| Column | Intended handler | Exit |
|---|---|---|
| Todo | None | Mike sends intake to Shape. Park delivery slices here unassigned until Delivery moves eligible work to Build. |
| Shape | Product & Design | Entering Shape starts collaboration. Keep the issue here through discussion and revisions. Set or reference the visual direction for UI work. Post one review-ready artifact revision when ready. Mike approves it by moving directly to Plan Delivery. |
| Plan Delivery | Delivery Lead | Verify Mike’s move from Shape and record the approved revision before planning. Explain missing or stale approval and return to Shape before dispatching. Gate UI work on an [approved visual direction](runbook.md#visual-direction-before-build). Send a self-contained issue to Build or publish a split plan and move the parent to In Delivery. |
| In Delivery | None, retain Delivery Lead | Advance eligible waves on native wakeups. Send the final candidate to Prepare Release or close work that needs no release. |
| Build | Engineering | Confirm the approved visual direction before UI implementation. Post evidence and hand off to Verify. Return material scope changes to Shape. |
| Verify | Verification | Compare rendered UI to the approved visual direction. Send defects to Build. Close integrated and verified children, or send a standalone release candidate to Prepare Release. |
| Prepare Release | Release | Post one complete, verified packet, then move the issue to Ready for Release. |
| Ready for Release | None, retain Release | The packet is ready for review. Mike moves the issue to Release & Verify to approve it. |
| Release & Verify | Release, triggered by Mike | Verify the approval, execute the prepared actions, confirm the published revision, and run smoke checks before Done. |
| Blocked | None, retain current owner | Use when a specific human action is required outside normal review or discussion. Record the person, action, and resume stage. If an agent can take over, return the issue to the appropriate stage as that agent picks it up. |
| Done | None | Agreed criteria verified. |
| Cancelled | None | Reason for dropping the work recorded. |

## Project directories

Use the [project directory rules](project-directories.md) for managed checkouts, local artifacts, and prototype ownership across issues.

## Labels

Issue types: `initiative`, `slice`, `discovery`, `bug`, `enhancement`, `factory-improvement`. Flags: `risk:high` for consequential changes, `needs-info` for a missing input, and `council` for an open advisory review. Use `discovery` for research, feasibility work, and prototypes that answer a specific question. This list is the complete issue-label vocabulary for projects using Kitchen Brigade. If an approved label is unavailable, leave the issue unlabelled. Clear temporary flags when resolved. The step owner checks the criteria before moving the issue. A label alone never dispatches work.
