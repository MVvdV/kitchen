---
name: prepare-release
description: Prepare a ready release packet, execute the exact approved GitHub actions, or verify the published result.
---

# Prepare Release

Check relevant design revisions and reconciliation dispositions before preparing a release packet and again before publication. Hold affected candidates with unresolved impact. An outdated attestation or packet goes back to preparation.

**Prepare.** Post one ready packet before requesting approval. Include the full candidate SHA and how to retrieve it, repository and target refs, expected current target SHA or absent state, exact publication actions and final text, required check results for this candidate, smoke checks, rollback, and release access readiness. Identify which checks run before publication and which are post-publication. Inspect the outgoing file changes and every introduced commit, including all reachable commits on the first push, for scope and attribution. Keep unrelated prototypes out of the release. Check author and committer identities, message trailers, provider bylines, and session links. Use the configured human Git identity and omit automated attribution. Hand off the complete packet to Ready for Release. Keep incomplete preparation out of the ready column.

**Publish.** Use the workflow's approval record to match the approver, transition, target, and the one ready packet posted before the approval event. The authorized approver's move from Ready for Release to Release & Verify supplies the approval. Check current status and target state immediately before writing. Reconcile prior publication records and the remote before retrying, so completed actions are never repeated. Execute only the listed actions for the recorded SHA. Stop on missing evidence, drift, or an unauthorized action. Return the work to preparation with the reason. Record the actual published commit, actions, and references before verifying the outcome in the same stage.

**Verify.** Check the published revision against the approved SHA, run the agreed smoke checks, and record the outcome and references. Return problems through the workflow and request a fresh approval for a changed candidate, target, or publication action.
