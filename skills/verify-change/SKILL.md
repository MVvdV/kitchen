---
name: verify-change
description: Independently verify an exact software candidate against acceptance criteria and produce a revision-specific verdict.
---

# Verify Change

Read the approved criteria, candidate revision, and claimed evidence. Reproduce the relevant checks against that revision. Trace likely behavior outside the changed path when the change affects shared state or interfaces.

Report each criterion as passed, failed, or unverified, with commands, observations, and artifact links. Give a reproducible finding for failures and identify any missing prerequisite. Changes to the candidate require fresh verification.
