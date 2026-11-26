---
name: prototype-question
description: Design a small disposable prototype when a specific interaction, state model, or feasibility question needs evidence.
---

# Prototype Question

Name the question, the design decision it could change, and the evidence that would let you stop. Choose the smallest test that can supply that evidence. Use side-by-side frames for a visual choice, a clickable sequence for an interaction or navigation choice, and runnable code when real behavior or technical feasibility needs testing. Use realistic inputs when they affect the answer.

Record the outcome, what remains uncertain, and which decision the evidence informed. Put a quick experiment in the owning issue. Use a linked follow-up if the test needs its own owner, time, or review.

Put editable working files in the owning issue's `artifacts/<issue-id>/design/` folder. If a prototype spans several issues, link the owner and exact base revision from each contributor. Keep variants and review evidence under their own issues and let the owner integrate accepted changes.

During live exploration, report what the prototype demonstrated and what remains uncertain. Use the working prototype during routine discussion and follow the Shape rule for focused visuals. When handing off the result for approval, formal review, or transfer to another owner who needs a pinned revision, provide an accessible snapshot or runnable bundle and how to exercise it. Include the dependency lockfile for a runnable code prototype when available. Pair native design files with a preview that another tool can open. Treat production implementation as a separate decision.
