# Blueprint improvement

Kitchen maintains the shared delivery blueprint by evaluating work done in product projects. Product projects run Kitchen Brigade on real work and provide the evidence. Kitchen issues are for learning, evaluating, proposing improvements, and tracking their rollout. Product implementation and product-specific fixes stay with the product project.

## Capture and evaluate

Open a linked improvement issue in Kitchen when a product run exposes a potential weakness in the shared workflow, agent instructions, skills, or templates. Record:

- the source issue or run and any relevant artifact or candidate revision
- the blueprint revision or live configuration used
- what was expected, what happened, and the effect on delivery
- which shared rule might need to change, and where else the problem could recur

Use accessible links and a brief summary. Keep sensitive product material in the source project.

Evaluate whether the cause is in the shared blueprint, tool integration, or product-specific context. Evidence from multiple projects helps establish a pattern. A single well-documented case can support a shared change if its mechanism applies wherever the same rule is used. If the fix belongs to one product, record that decision and keep implementation in that project.

## Approve and roll out

Propose the smallest generally applicable change in this repository. Link the proposal from the Kitchen issue and state what the next applicable run should do differently. Update an eval when it helps reviewers judge that outcome.

Before approving a blueprint change, record whether it affects instructions agents receive at runtime. For Multica changes, complete the [runtime compatibility check](../integrations/multica/README.md#runtime-compatibility-check) and record the result on the Kitchen issue. Resolve any conflict that would change what an agent does before rolling out the affected change.

Record approval and the Git revision before updating live shared workflow, agent, or skill settings. A change to shared settings reaches every project using them. If the change warrants a limited rollout, first apply it to one real project using separate configuration where needed. Record the affected projects and the revision applied, then use subsequent product runs to check the result. Record whether the evidence supports keeping, revising, or rolling back the change.

## Proposed Kitchen board

Learning Inbox → Evaluate → Propose Change → Approve → Roll Out → Follow Up.

This is a proposed maintenance board. Kitchen Brigade remains the delivery blueprint for product projects.
