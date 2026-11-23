# Release

In Prepare Release, record the exact candidate, required CI results, target environment, smoke checks, and rollback procedure. When needed, use one durable wait for linked CI and recheck the head when resumed. Move to Approve Release after recording the evidence.

Mike authorizes and initiates release through the deployment controls. In Verify Release, check the actual deployed revision and run smoke checks against the agreed target. Record the deployment link and results. Mark Done when the release criteria pass. On failure, record the evidence and rollback path. Route agent-resolvable work to the responsible role. Mark Blocked only if a specific human action is required.
