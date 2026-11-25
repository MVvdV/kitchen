---
name: build-change
description: Implement an approved software change and produce a reproducible candidate for independent verification.
---

# Build Change

Read the approved scope and baseline. Reuse isolation supplied by the host, or create a separate checkout if needed. Preserve unrelated changes. Add or update behavior-level checks where they materially improve proof.

Reuse the issue branch and checkout for routine iteration. Keep one current checkpoint with the exact commit, checks completed, and next step when work may resume elsewhere. Run focused checks while iterating and give the requester only relevant changes, blockers, and results. Link existing logs or show the relevant failure excerpt. Share a focused screenshot when it helps resolve a visual question.

When the candidate meets its Build criteria, prepare one Verify handoff with the exact commit, required checks and results, reproduction steps, and known gaps. Refresh the handoff if the candidate changes and reuse matching evidence. Keep GitHub publication under the release workflow. If the work needs a material scope decision, report the choice before implementing it.
