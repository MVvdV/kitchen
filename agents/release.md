# Release

Use the prepare-release skill and release record. In Prepare Release, post one ready packet for the exact candidate with checks, target state, planned GitHub actions, publication text, smoke checks and rollback. Keep the card here. Mike moves it to Approve Release when ready.

In Approve Release, verify the latest move came directly from Prepare Release and was made by Mike after the ready packet was posted. Record the transition and packet reference. Reconcile any prior attempts. Execute only the listed actions for the exact candidate and target. Check the outgoing history and text for automated attribution and unrelated prototype work before publishing. Return to Prepare Release with the reason if approval, checks, or inputs are incomplete or stale.

In Verify Release, compare the actual published revision to the approved one and run the agreed smoke checks. Record the release reference and results. Mark Done when the criteria pass. Record failures and the rollback path. Route agent-resolvable work to the responsible role. Mark Blocked only when a specific human action is required.
