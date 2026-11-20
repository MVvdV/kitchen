# Multica stage wakeups and recovery

Use the [delivery and recovery policy](../../workflows/runbook.md) and the [Multica wiring guide](README.md).

- In Delivery has no handler. Entering it retains the Delivery Lead as assignee and queues no run. Number child stages on creation and record dependency issue IDs in the dependent child's description.
- Use the native sub-issue wakeup to bring back the parent assignee when a stage closes. Multica treats Done and Cancelled as closed for the event. Apply the delivery policy before promoting the next stage. One native wakeup is sufficient.
- To handle failed runs after native retries, use a separate wakeup or periodic check on a runtime that can act independently of the worker. Verify the active and queued runs before dispatching. A stale step rejection requires reading the current issue state and using the current owner to proceed.
- Use the [evaluation scenarios](../../evals/README.md) to verify guest squad mentions, stage completion, fresh-session recovery, and duplicate prevention after wiring.
