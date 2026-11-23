# Shared agent instructions

1. On every run, read the current issue, status, assignee, trigger, approved scope and revision, latest handoff, and any linked candidate, tests, or deployment records. On a parent, read the current child list and stages. Reconcile those facts before acting.
2. Follow the authority of your role. The current step owner advances the issue. An invited reviewer posts findings. If the current step or assignee changed, stop writes and leave a concise note where useful.
3. Before handing off, record the outcome, exact revision or durable artifact, verification evidence, unresolved items, and next action. Save everything the next run needs in Git or an accessible issue artifact. A model session or local worktree may speed up work but carries no required state.
4. Before repeating an external action, check whether it already happened. Resume matching child issues, pull requests, and release records. Never claim that a run, test, deployment, or approval succeeded without evidence for the relevant revision.
5. Obey human approval and cancellation. A changed spec or release candidate invalidates the corresponding earlier approval. Material scope changes return to Shape.
6. Use the documented tools and permissions for your role. Escalate a missing tool, permission, or decision with the last durable checkpoint and a concrete next action.
7. Use the issue-label vocabulary in [the delivery workflow](../workflows/README.md#labels). Use `discovery` for research and prototypes. If an approved label is unavailable, leave the issue unlabelled.
