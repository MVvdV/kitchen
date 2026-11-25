# Delivery and recovery

## Ownership and waves

The parent owns the application outcome. Keep the Delivery Lead assigned through In Delivery. Each delivery slice has acceptance criteria, explicit dependencies, and a durable handoff.

Group work into numbered stages. Work in the same stage can start independently. Record all children unassigned in Todo before dispatching eligible first-wave work to Build. When a stage closes, check the actual outcomes and dependencies before promoting the next wave. A cancelled required child needs a recorded scope decision before advancing.

## Select a Shape or Build owner

The product approver selects either designer when initiating Shape. Delivery selects either engineer when dispatching Build. Prefer continuity on returns, and choose the other peer if the previous owner cannot continue. Record the intended owner and checkpoint, then use the project integration to dispatch explicitly. Reread the issue and active attempts before retrying a partial handoff. See [team organisation](../governance/team-organisation.md).

## Split and reconcile work during Shape

Keep decisions in the current Shape issue when they can be resolved in its normal discussion. Create a follow-up when the question has its own outcome and can be shaped and reviewed separately. First check related Shape and Todo issues for overlap, including earlier follow-ups. Reuse an applicable issue. If none fits, create one linked design issue in Todo, unassigned. Link both directions and record the source design, inherited decisions, the follow-up’s boundary, draft acceptance criteria, and whether the source depends on its answer. A design follow-up can be linked independently of the delivery hierarchy.

The product approver selects when the follow-up starts and who owns it. The default is manual start. A project may explicitly authorize the workflow to move and assign eligible follow-ups into Shape later. Starting design carries no authority to approve it or dispatch implementation.

If the follow-up owns a material decision needed for the source approval, hold the affected approval until that decision is resolved. Continue unaffected shaping. When either issue changes a shared assumption, state the impact and link both issues. Update parked Todo drafts for settled decisions within scope. Record proposed changes as proposals. If another owner is actively shaping the affected issue, record the impact for that owner to reconcile instead of editing their design, reassigning it, or starting a run. Preserve traceability if a follow-up is superseded.

Plan Delivery performs the wider reconciliation after approval. It can reuse suitable existing work and creates Build slices when approved scope needs them. A linked Shape issue does not become a staged delivery child by default.

## Reconcile existing work before dispatch

After design approval, Delivery compares the approved revision with the affected existing tickets, dependencies, in-flight work, built changes, and unreleased candidates in the project. Include related work outside the current issue's children when it depends on the same product assumptions. Record each affected ticket and candidate revision with its evidence, disposition, downstream changes, owner, and next step. Record the scope checked if there is no affected work. Finish the reconciliation before creating or dispatching new work.

| Disposition | Delivery action |
| --- | --- |
| Keep | Record evidence that the existing assumptions, acceptance criteria, and candidate still fit. |
| Revise | Reuse the applicable issue, update acceptance criteria and dependencies, and send changed implementation through Build and Verify. Treat its outdated release packet as stale. |
| Supersede | Link the replacement or approved omission, update affected dependencies, and keep the superseded ticket and commit history for traceability. Exclude obsolete changes from the release candidate. |

Record an unresolved reconciliation hold on an affected release issue. A candidate with unresolved impact stays out of Ready for Release and cannot be published. If already ready, coordinate with the release owner to return it to preparation. Release checks current related design revisions and holds before marking a packet ready and before publishing. Reuse a prior verification only when its exact candidate and affected criteria still match. A revised release candidate needs a fresh packet and the existing release approval.

The approved design is enough for Delivery to reconcile and dispatch work within its scope. Ask the product approver about a material scope change or an unresolved product trade-off. Record the reason and return that decision to Shape before dispatching affected work. One design approval can cover several revised tickets.

## Discussion, iteration, and handoff

Use the working artifact during collaboration. Keep replies focused on the answer, relevant change, and next decision. For routine design discussion and canvas edits, default to zero attachments and refer to the live page or frame. Share a single focused visual when a specific question depends on it and pointing to the canvas is insufficient. For engineering updates, link only the log or excerpt needed for the question. Save material decisions or a restart checkpoint in the existing working record.

Shape publishes one frozen approval candidate when all material choices are resolved and it is ready for approval. Use a pinned revision for a formal peer review or ownership transfer when the recipient needs it. Update the working design between handoffs and reuse the published packet while its revision is current. Mark an outdated packet superseded if a material change invalidates it.

Build uses an isolated checkout and the issue branch. Use local commits and a compact checkpoint for recovery. At Verify, identify the exact candidate, provide the relevant check results and reproduction commands, and link evidence. Routine replies and implementation steps do not create new packets. Release preparation uses the verified revision and the existing release approval process.

## Checkouts and handoffs

Follow the [project directory rules](project-directories.md) for checkouts, local files, prototypes, and cross-tool handoffs. Save versioned work as local commits and share accessible evidence on the issue. Record the exact candidate before external publication. Include the commit SHA or pull request and candidate SHA so Verification can reproduce the result.

Run independent slices in isolated checkouts. Keep dependent slices parked until the predecessor's required revision and evidence are available. Use the recorded revision as input when picking up dependent work.

## Visual direction before Build

Before dispatching work that will render or change a user-facing UI, require a link to the exact approved visual direction. This includes visible prototypes, spikes, and temporary screens. A ticket can inherit the approved project baseline when it covers the work. An exploratory visual variant belongs in Shape until the direction is ready for delivery.

For a blank slate, Product & Design supplies a representative screen and short style notes covering typography, spacing and density, color, surface hierarchy, and the treatment of common controls. An existing visual reference can guide that direction. Choosing dependencies is a separate decision. Include the direction in the revision presented for approval through the normal Shape handoff.

Delivery records the reference and relevant states on each applicable issue before Build, including at later wave promotions. If the direction is missing, stale, or leaves a material visual decision open, keep the affected work out of Build and route that decision to Shape with the reason. Engineering checks the reference before UI implementation, follows it, and reuses shared tokens and components where available. Verification compares the rendered result in the relevant states to the reference and checks reuse. Product & Design owns new visual decisions.

## Publication and release approval

Keep prototypes, product changes, and verification candidates local before release approval. Share review evidence in the issue. Use the configured Git author identity and omit automated co-author trailers, provider bylines, and session links.

Prepare Release posts one ready packet with the full candidate SHA, repository and target, exact GitHub actions, current target state, checks, prepared publication text, and rollback. Review all outgoing commits for the configured human Git identity and automated attribution, including on a first push to an empty branch. Keep prototypes outside the outgoing history and file tree unless the approved release explicitly includes them. Keep drafts and evidence in the issue.

After posting the complete packet, Release moves the issue to Ready for Release. Mike approves by moving it directly from Ready for Release into Release & Verify. That move starts the Release agent. Release checks the actor, transition, packet, candidate, target state, and prior publication before executing the prepared actions. Verify the published revision and run smoke checks in the same stage. Return to Prepare Release if approval is missing or the packet, candidate, or target state has changed. Record the reason and obtain a fresh move. Reconcile any already published result before retrying.

## Recovery

The Delivery Lead coordinates recovery. Use a notification or check that can run independently of the worker. Check for an existing attempt before dispatching another. Reconcile issues, candidate revisions, and release records with the latest durable checkpoint. A successful run with missing evidence leaves the step incomplete.

Allow one recovery dispatch after scheduler retries when the cause is fixed and repetition is safe. If an agent can resolve the issue, the current owner selects that agent and records the condition that will prove recovery. Work can wait at its current stage with a wakeup for that condition, or move to the stage that owns the fix. If an agent takes over an already Blocked issue, the current owner moves it out of Blocked as part of the handoff. If a specific human action is required, mark it Blocked and record the person, action, last checkpoint, and resume stage. Respect cancellations and human approvals. Resume Engineering through Build. If someone changed the workflow step, review the current state before starting another attempt.
