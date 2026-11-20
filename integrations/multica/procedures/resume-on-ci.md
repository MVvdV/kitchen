# Resume On Ci

Confirm the PR is linked and inspect the current head and required checks. If they are still pending, reuse an existing matching wait or register a supported one-shot PR check condition, then end the run. Recheck after registering to cover checks that finish during setup.

On resume, inspect the current issue step and PR head again. A completion event may carry a failure, or refer to a different candidate. Record the actual checks and only proceed when the evidence for the current head meets the step criteria. Escalate missing links, inaccessible results, or expired waits with the last checkpoint.
