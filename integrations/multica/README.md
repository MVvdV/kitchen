# Multica integration

Use this guide to apply the [workflow](../../workflows/README.md) in Multica. Resolve the symbolic handlers in the blueprint to the intended workspace agents or members. The blueprint is a review document and does not apply itself.

## Wiring

Bind the intended agent roles to the corresponding columns after their agents exist. Give each role its instructions and the shared instructions. Keep Todo, In Delivery, and Blocked without automatic handlers. Bind Engineering to Build. Set a one-shot retry or periodic recovery check only after choosing a compatible independent runtime and verifying permissions. Test the columns and handoffs with work started by Mike.

Use an on-demand squad mention for the Debate Council. A guest council posts findings while the current assignee owns the transition.

## Managed local checkouts

Use **Worktree** mode for projects with concurrent local agent runs. Attach one clean Git checkout per project as the baseline on the machine running the Multica daemon. Keep the human checkout separate.

| Location | Purpose |
| --- | --- |
| `~/workspace/<project>` | Human checkout for day-to-day work and previews. |
| `~/workspace/.multica-checkouts/<project>` | Default Kitchen path for the project's dedicated baseline checkout. The dot keeps workspace listings tidy. A visible path also works when configured on the project. |
| Multica-allocated worktree | Isolated working directory for an agent run. Multica manages its location and branch. |

In **In place** mode, an agent edits the attached folder directly. Multica serializes runs that use it. In **Worktree** mode, the same one attached folder supplies the baseline for separate Git worktrees. Parallel runs have their own files and index while sharing the repository's Git history. Later turns in the same agent issue conversation resume its work on its branch. Worktree isolation removes the shared-folder lock for independent runs. Runtime concurrency limits and issue dependencies still apply.

Keep the baseline clean. Configure its upstream and the project's GitHub resource to use the same integration branch, normally `main`. After approved changes land, fast-forward the baseline while idle. Existing issue branches may need their own update, and dependent work uses the exact revision recorded in the handoff.

Use the worktree Multica allocates. Keep disposable files in that worktree or a run-specific temporary directory. Publish durable evidence before finishing. During migration, verify two independent runs overlap in different worktrees, then retire idle manual worktrees after preserving any local files and checking their branches.

## GitHub write gate

Keep GitHub branch and tag creation, updates, and deletion blocked across all refs before release approval. Use a human-controlled admin session for the approved publication and restore the rules immediately afterward. Keep publishing and administration credentials out of agent runtimes for an independent permission boundary.

Use the exact approved local commit and issue evidence for the handoff. Verify the published SHA and restore the gate before marking the release ready for verification.

## Column order

The workflow omits Backlog and uses the built-in Todo column for intake and parked work. Leave those issues unassigned. Move intake to Shape when Mike is ready, and move eligible approved work to Build to start Engineering.

## Design handoff

Entering Shape starts Product & Design. Drafts and feedback stay in Shape. Use a note or suppress the comment trigger when you only want to leave feedback for later. The approver moves the card from Shape to Plan Delivery when ready. Delivery records the approval from the issue timeline before publishing tickets. See [Publish delivery tickets](procedures/publish-delivery-tickets.md).

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
