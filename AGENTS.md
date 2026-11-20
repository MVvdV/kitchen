# Kitchen Brigade repository

Read README.md for the repository layout. For delivery behavior, read workflows/README.md, workflows/runbook.md, and the relevant role instructions in agents/.

Keep workflows, skills, and templates independent of integration mechanics. Put platform setup and platform-specific procedures under integrations/. Keep the workflow blueprint, handbook, and relevant scenario aligned when changing a transition.

Run `python3 scripts/check_repo.py` for offline validation. The scenarios in evals/README.md require a separate observation of actual behavior. Mike starts the first issue and owns design and release approval.
