# Blueprint improvement

Kitchen maintains the shared delivery blueprint by evaluating work done in product projects. Product projects run Kitchen Brigade on real work and provide the evidence. Kitchen issues are for learning, evaluating, proposing improvements, and tracking their rollout. Product implementation and product-specific fixes stay with the product project.

The [Chief of Staff](../agents/chief-of-staff.md) coordinates this work with the blueprint approver. Use Kitchen issues to track shared improvements and product project issues to track project-specific setup or fixes. The Operations Assistant can collect evidence or compare an applied configuration with the intended rollout. Delivery continues to own execution inside each product project.

## Capture and evaluate

Use a Kitchen issue for a reusable evaluation, learning to incorporate, or proposed workflow change. An anticipated improvement can start with a question to answer, such as which operations can safely become more autonomous.

Describe the general problem, the expected and observed behavior, the impact, and the shared rule to evaluate or change. Keep project names, issue and run links, raw evidence, and project-specific actions in the product project. Record the generalized conclusion and the relevant blueprint revision in Kitchen.

Evaluate whether the cause is in the shared blueprint, tool integration, or product-specific context. Evidence from multiple projects helps establish a pattern. A single well-documented case can support a shared change if its mechanism applies wherever the same rule is used. If the fix belongs to one product, record that decision and keep implementation in that project.

## Approve and roll out

Propose the smallest generally applicable change in this repository. Use the Kitchen issue to record the proposed blueprint change and what the next applicable run should do differently. Update an eval when it helps reviewers judge that outcome.

Before approving a blueprint change, record whether it affects instructions agents receive at runtime. For Multica changes, complete the [runtime compatibility check](../integrations/multica/README.md#runtime-compatibility-check) and record the result on the Kitchen issue. Resolve any conflict that would change what an agent does before rolling out the affected change.

Record approval and the Git revision before updating live shared workflow, agent, or skill settings. A change to shared settings reaches every project using them. If the change warrants a limited rollout, first apply it to one real project using separate configuration where needed. Use the [rollout record](../templates/blueprint-rollout.md) to record approval, rollout scope, intended settings, and the revision applied, then use subsequent product runs to check the result. Record whether the evidence supports keeping, revising, or rolling back the change.

## Close records when work is complete

Use Todo for work the Kitchen team still needs to do. When an agreed change has been applied and its saved configuration verified, close its rollout record as Done. If recording work after completion, file it as Done. Note any post-rollout observation in the record. Give a required evaluation of its own or a new proposed improvement a separate open issue with a concrete outcome.

## Proposed Kitchen board

Learning Inbox → Evaluate → Propose Change → Approve → Roll Out → Follow Up.

This is a proposed maintenance board. Kitchen Brigade remains the delivery blueprint for product projects.
