---
name: peer-review
description: Independently review a pinned design revision or implementation candidate against stated criteria. Use for a peer or Council review of work owned by someone else.
---

# Peer review

Confirm the review question, exact revision, acceptance criteria, and accessible evidence. Ask the owner for missing inputs. Inspect the candidate independently before reading other reviewers’ conclusions when practical. If you own or materially edited the candidate, disclose that and provide context so another qualified reviewer can give the independent assessment.

- **Design** Check hierarchy, typography, spacing, alignment, contrast, component and state consistency, and responsive behavior. Reference the affected screen, frame, state, or viewport and the approved direction.
- **Product** Check the intended outcome, assumptions, user trade-offs, and unresolved choices against the approved brief or review question.
- **Engineering** Inspect the exact diff and relevant tests. Check acceptance criteria, regressions, failure paths, interfaces, migrations, dependencies, and evidence gaps. Reference the affected code or behavior and report any checks actually run.

For each finding give its impact, evidence, and expected correction. Note unresolved questions and checks you could not complete. Leave the report with the issue owner. During review, keep the candidate, issue assignment, and stage intact. If asked to take ownership, get an explicit handoff before editing. Review the next pinned revision when findings remain open or the change affects the agreed criteria.
