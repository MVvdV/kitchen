# Team organisation

Use one Council for independent review. Bring in reviewers with the right expertise for the question and assign follow-up work to the role that owns it. Keep the person who approves the design able to choose between materially different outcomes.

| Role | Responsibility |
| --- | --- |
| Product & Design | Own the Shape issue and editable design. Define the review criteria with the product approver, apply agreed changes, and publish the exact revised candidate. |
| Visual Critic | Independently review an exact revision for visual hierarchy, typography and spacing, alignment, component and state consistency, contrast, and responsive layout. Point to the affected frame or state and explain the expected correction. |
| Alternate Designer | Take over an explicitly handed-off Shape issue or give an independent design review. When taking over, work from the recorded revision, decisions, and open questions. Keep one agent writer per editable file. |
| Engineering and Alternate Engineer | Use one implementation owner at a time. The alternate can take over from an exact commit and test checkpoint or review a colleague's implementation. Use isolated worktrees and let Verification assess the candidate independently. |
| Council Chair | Select relevant reviewers, reconcile findings, record dissent, and make a recommendation. For a visual review, invite Visual Critic and add product or architecture perspectives where they affect the design. |

For a design review loop, pin the design revision and the visible criteria. Council reports concrete findings against that revision. Product & Design resolves findings within the existing direction and posts the next revision. Ask for another focused review only when an unresolved finding or a changed design needs it. Keep the issue in Shape until the product approver is satisfied. A consequential choice about the product experience goes to the approver with options and trade-offs.

Use an alternate when capacity, continuity, or independence requires one. Before transferring write ownership, confirm the previous run is stopped and record the current revision, completed checks, remaining work, and next owner. Reviewers can work independently from frozen snapshots. The Council advises and the designated owner applies changes.

Start with a Visual Critic in the existing Council and keep the alternate roles available for deliberate handoffs. Consider a separate Design Council only if recurring reviews need a distinct roster or cadence.
