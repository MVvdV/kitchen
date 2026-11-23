# Delivery and recovery

## Ownership and waves

The parent owns the application outcome. Keep the Delivery Lead assigned through In Delivery. Each delivery slice has acceptance criteria, explicit dependencies, and a durable handoff.

Group work into numbered stages. Work in the same stage can start independently. Record all children unassigned in Todo before dispatching eligible first-wave work to Build. When a stage closes, check the actual outcomes and dependencies before promoting the next wave. A cancelled required child needs a recorded scope decision before advancing.

## Recovery

The Delivery Lead coordinates recovery. Use a notification or check that can run independently of the worker. Check for an existing attempt before dispatching another. Reconcile issues, candidate revisions, and release records with the latest durable checkpoint. A successful run with missing evidence leaves the step incomplete.

Allow one recovery dispatch after scheduler retries when the cause is fixed and repetition is safe. If an agent can resolve the issue, the current owner selects that agent and records the condition that will prove recovery. Work can wait at its current stage with a wakeup for that condition, or move to the stage that owns the fix. If an agent takes over an already Blocked issue, the current owner moves it out of Blocked as part of the handoff. If a specific human action is required, mark it Blocked and record the person, action, last checkpoint, and resume stage. Respect cancellations and human approvals. Resume Engineering through Build. If someone changed the workflow step, review the current state before starting another attempt.
