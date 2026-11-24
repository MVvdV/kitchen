# Publish Delivery Tickets

Confirm that you own Plan Delivery. Use `multica issue timeline <issue-id> --output json` to match the latest entry into Plan Delivery to the authorized approver's recorded move from Shape. Identify the review-ready revision presented before that move and check that no later material change superseded it. Record the approver, transition event ID, and immutable artifact revision in the issue before ticket creation or dispatch. Reuse an existing approval record only if it matches the same verified handoff and current revision.

If the move or revision cannot be verified, or the design has changed, post the specific reason first and return the issue to Shape. This starts Product & Design with the reason available on the issue. Leave the move back to Plan Delivery to the approver. Follow the Kitchen workflow and supported Multica CLI operations. A self-contained issue goes to Build without a child.

Before creating or dispatching an issue, inspect the affected project tickets and any in-progress, verified, or unreleased candidates and their current release packets. Post the reconciliation table on the planning issue. Use exact description edits to preserve concurrent changes when updating acceptance criteria and dependency links. On affected release issues, record a hold in the description while disposition or re-verification is pending. Coordinate with the current owner if work is already running. Preserve superseded issues and commits as evidence.

For a split, reconcile existing children using stable plan keys. Create missing children as staged native sub-issues unassigned in Todo with their criteria and dependency IDs. Record the mappings before dispatch. Keep the parent assigned to Delivery Lead in In Delivery. Move eligible first-wave children to Build and leave later waves parked in Todo.

On a native stage wakeup, verify actual success and dependencies before promoting later work. A cancelled required child needs an explicit decision. Skip existing dispatches and stop if ownership or the workflow step changed.
