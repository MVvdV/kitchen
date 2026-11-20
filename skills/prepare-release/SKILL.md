---
name: prepare-release
description: Prepare an evidence-backed release decision or verify what shipped using a deployment record and smoke checks.
---

# Prepare Release

For preparation, identify the candidate revision, target, required checks, smoke tests, rollback path, and unresolved decisions. Return a release packet tied to that candidate. A changed candidate requires renewed evidence and any required approval.

For verification, compare the deployed revision with the approved candidate and record the smoke results and deployment reference. Respect the authority granted by the caller and the deployment system.
