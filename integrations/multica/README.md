# Multica integration

Use this guide to apply the [workflow](../../workflows/README.md) in Multica. Resolve the symbolic handlers in the blueprint to the intended workspace agents or members. The blueprint is a review document and does not apply itself.

## Wiring

Bind the intended agent roles to the corresponding columns after their agents exist. Give each role its instructions and the shared instructions. Keep Backlog, Build, In Delivery, and Blocked without automatic handlers. Set a one-shot retry or periodic recovery check only after choosing a compatible independent runtime and verifying permissions. Test the columns and handoffs with work started by Mike.

Use an on-demand squad mention for the Debate Council. A guest council posts findings while the current assignee owns the transition.

## Column order

Multica puts Backlog and Todo at the front of the board. Todo is required and returns to that position when the workflow is saved. The blueprint lists the logical delivery order, where Plan Delivery sends a self-contained issue or eligible children to Todo. Use the explicit handoff targets to verify that path on both Kitchen Brigade and any project copy.

## Procedures

- [Publish delivery tickets](procedures/publish-delivery-tickets.md)
- [Record a handoff](procedures/record-handoff.md)
- [Resume on CI](procedures/resume-on-ci.md)
- [Stage wakeups and recovery](runbook.md)
