# Delivery and recovery

## Ownership and waves

The parent owns the application outcome. Keep the Delivery Lead assigned through In Delivery. Each delivery slice has acceptance criteria, explicit dependencies, and a durable handoff.

Group work into numbered stages. Work in the same stage can start independently. Record all children unassigned in Todo before dispatching eligible first-wave work to Build. When a stage closes, check the actual outcomes and dependencies before promoting the next wave. A cancelled required child needs a recorded scope decision before advancing.

## Checkouts and handoffs

Use the project's managed checkout for work. Keep disposable files scoped to the run. Save versioned work as local commits and share evidence as accessible issue artifacts. Record the exact candidate before any external publication. Record the exact commit SHA or pull request and candidate SHA on the issue so Verification can reproduce the result.

Run independent slices in isolated checkouts. Keep dependent slices parked until the predecessor's required revision and evidence are available. Use the recorded revision as input when picking up dependent work.

## Visual direction before Build

Before dispatching work that will render or change a user-facing UI, require a link to the exact approved visual direction. This includes visible prototypes, spikes, and temporary screens. A ticket can inherit the approved project baseline when it covers the work. An exploratory visual variant belongs in Shape until the direction is ready for delivery.

For a blank slate, Product & Design supplies a representative screen and short style notes covering typography, spacing and density, color, surface hierarchy, and the treatment of common controls. An existing visual reference can guide that direction. Choosing dependencies is a separate decision. Include the direction in the revision presented for approval through the normal Shape handoff.

Delivery records the reference and relevant states on each applicable issue before Build, including at later wave promotions. If the direction is missing, stale, or leaves a material visual decision open, keep the affected work out of Build and route that decision to Shape with the reason. Engineering checks the reference before UI implementation, follows it, and reuses shared tokens and components where available. Verification compares the rendered result in the relevant states to the reference and checks reuse. Product & Design owns new visual decisions.

## Publication and release approval

Keep prototypes, product changes, and verification candidates local before release approval. Share review evidence in the issue. Use the configured Git author identity and omit automated co-author trailers, provider bylines, and session links.

Prepare Release records the exact candidate SHA, checks, destination, and rollback. Approve Release asks Mike to explicitly approve that SHA and destination. An approval statement is required before publication. Obtain fresh approval if the candidate or destination changes. Mike performs the approved publication and records the published revision for Verify Release.

## Recovery

The Delivery Lead coordinates recovery. Use a notification or check that can run independently of the worker. Check for an existing attempt before dispatching another. Reconcile issues, candidate revisions, and release records with the latest durable checkpoint. A successful run with missing evidence leaves the step incomplete.

Allow one recovery dispatch after scheduler retries when the cause is fixed and repetition is safe. If an agent can resolve the issue, the current owner selects that agent and records the condition that will prove recovery. Work can wait at its current stage with a wakeup for that condition, or move to the stage that owns the fix. If an agent takes over an already Blocked issue, the current owner moves it out of Blocked as part of the handoff. If a specific human action is required, mark it Blocked and record the person, action, last checkpoint, and resume stage. Respect cancellations and human approvals. Resume Engineering through Build. If someone changed the workflow step, review the current state before starting another attempt.
