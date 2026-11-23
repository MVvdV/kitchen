# Multica integration

Use this guide to apply the [workflow](../../workflows/README.md) in Multica. Resolve the symbolic handlers in the blueprint to the intended workspace agents or members. The blueprint is a review document and does not apply itself.

## Wiring

Bind the intended agent roles to the corresponding columns after their agents exist. Give each role its instructions and the shared instructions. Keep Todo, In Delivery, and Blocked without automatic handlers. Bind Engineering to Build. Set a one-shot retry or periodic recovery check only after choosing a compatible independent runtime and verifying permissions. Test the columns and handoffs with work started by Mike.

Use an on-demand squad mention for the Debate Council. A guest council posts findings while the current assignee owns the transition.

## Column order

The workflow omits Backlog and uses the built-in Todo column for intake and parked work. Leave those issues unassigned. Move intake to Shape when Mike is ready, and move eligible approved work to Build to start Engineering.

## Issue labels

Apply only the labels in the [Kitchen Brigade workflow](../../workflows/README.md#labels). Generated runtime briefs may include workspace label examples. Follow the workflow vocabulary when creating or updating Kitchen Brigade issues.

## Runtime compatibility check

1. Use a recent run from an affected product project. Read the generated runtime instructions and the project, workflow step, agent, and skill instructions supplied to that run. If there is no representative run, record what could be checked from the live configuration and inspect the first applicable product run before broader rollout.
2. Compare the proposed revision with those instructions for the actions it changes. Check labels, status commands and handoffs, who can advance or approve work, and required artifacts. Distinguish generic examples from platform behavior the workflow must respect.
3. Resolve a conflicting example in the project or agent instructions. If the runtime enforces different behavior, adjust the integration or hold rollout of the affected change. Leave generated runtime files under Multica's control.
4. On the Kitchen issue, record the run or configuration checked, the blueprint revision, any conflict and its resolution, and what to verify on the next real product run.

## Procedures

- [Publish delivery tickets](procedures/publish-delivery-tickets.md)
- [Record a handoff](procedures/record-handoff.md)
- [Resume on CI](procedures/resume-on-ci.md)
- [Stage wakeups and recovery](runbook.md)
