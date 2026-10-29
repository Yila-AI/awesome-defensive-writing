# Clear expression

**English** | [简体中文](../zh/clarity.md)

[All categories](index.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

- [DW-001 Sentence-level diagnosis](#dw-001)
- [DW-002 Minimal editing](#dw-002)
- [DW-003 Claim and grounds](#dw-003)
- [DW-004 Remove repeated caveats](#dw-004)
- [DW-005 Make advice actionable](#dw-005)
- [DW-006 Evaluate a qualification](#dw-006)

<a id="dw-001"></a>

## DW-001 · Sentence-level diagnosis

**Mode**: Diagnose

```text
Inspect the passage and explain the function of each suspect qualification.
Use the supplied evidence and conditions to distinguish useful information
from repetition. Return the requested diagnosis.

Task: Identify each suspect sentence's function and what information would be lost
by removing it. Flag only relevant passages; mark uncertain judgments for
verification rather than inferring author motives.

Output: A sentence table: original, information function, action and grounds; then a
minimally revised passage.

Input material:
Text: [fill in]
Audience and purpose: [fill in]
Supporting facts: [fill in]
```

<details>
<summary>See a related case · EX-01 · Say the same thing clearly</summary>

**Facts**

The meeting confirmed prototype delivery on Thursday, followed by testing. Delivery refers to the prototype, not completed testing.

**Before**

Given the project's complexity, we may try to aim for prototype delivery on Thursday. Of course, this does not mean that all work is finished.

**After**

The prototype will be delivered on Thursday, followed by testing.

**Reason**

The source contains a firm delivery agreement. Remove wording that weakens it and use the testing step to state scope.

[Full case and conditions to preserve](examples.md#ex-01)

</details>

<a id="dw-002"></a>

## DW-002 · Minimal editing

**Mode**: Revise

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Keep the author's voice and sentence structure where they work. Separate
grammar and organization edits from changes in claim strength; do not
mechanically make mild phrasing forceful.

Output: Replacement copy followed by the most important language or structural
edits.

Input material:
Draft: [fill in]
Tone to preserve: [fill in]
```

<details>
<summary>See a related case · EX-01 · Say the same thing clearly</summary>

**Facts**

The meeting confirmed prototype delivery on Thursday, followed by testing. Delivery refers to the prototype, not completed testing.

**Before**

Given the project's complexity, we may try to aim for prototype delivery on Thursday. Of course, this does not mean that all work is finished.

**After**

The prototype will be delivered on Thursday, followed by testing.

**Reason**

The source contains a firm delivery agreement. Remove wording that weakens it and use the testing step to state scope.

[Full case and conditions to preserve](examples.md#ex-01)

</details>

<a id="dw-003"></a>

## DW-003 · Claim and grounds

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Find the question the paragraph answers. Lead with the supported answer,
then its grounds and conditions. If no conclusion is available, state the
open question instead of inventing a position.

Output: A direct answer followed by grounds and necessary conditions.

Input material:
Passage: [fill in]
Question: [fill in]
Evidence: [fill in]
```

<details>
<summary>See a related case · EX-01 · Say the same thing clearly</summary>

**Facts**

The meeting confirmed prototype delivery on Thursday, followed by testing. Delivery refers to the prototype, not completed testing.

**Before**

Given the project's complexity, we may try to aim for prototype delivery on Thursday. Of course, this does not mean that all work is finished.

**After**

The prototype will be delivered on Thursday, followed by testing.

**Reason**

The source contains a firm delivery agreement. Remove wording that weakens it and use the testing step to state scope.

[Full case and conditions to preserve](examples.md#ex-01)

</details>

<a id="dw-004"></a>

## DW-004 · Remove repeated caveats

**Mode**: Revise

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Merge caveats only when they qualify the same claim in the same way. Similar
wording can serve different purposes. Keep conditions next to claims when
needed for interpretation.

Output: Revised copy and the repeated qualifications merged, with retained
conditions located.

Input material:
Text: [fill in]
Surrounding context: [fill in]
```

<details>
<summary>See a related case · EX-02 · A forecast is not a promise</summary>

**Facts**

At the current workload, completion is estimated for Thursday. New data arriving Wednesday would move the estimate to Friday. No fixed date has been promised to the client.

**Before**

Completion might possibly be around Thursday, although the situation is complex and uncertainty remains.

**After**

At the current workload, completion is estimated for Thursday, or Friday if new data arrives Wednesday.

**Reason**

Replace stacked hedges with an explicit estimate and the supplied condition that changes timing.

[Full case and conditions to preserve](examples.md#ex-02)

</details>

<a id="dw-005"></a>

## DW-005 · Make advice actionable

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Extract actions, sequence, resources and decision criteria already supported
by the material. Identify missing owners or deadlines separately without
creating commitments or arbitrary numbers.

Output: Ordered actions, completion checks and known dependencies; missing facts
separately.

Input material:
Advice draft: [fill in]
Resources: [fill in]
Goal: [fill in]
```

<details>
<summary>See a related case · EX-06 · A real dependency and fallback</summary>

**Facts**

Fictional project: authorized data precede cleaning and a trial run. Compute is available but data approval is pending. Friday is the team's decision point: without approval, use public samples next week to check the pipeline. Public samples cannot substitute for project data in the final evaluation.

**Before**

The project has many complex risks, and data issues could prevent any progress, making feasibility difficult to assess.

**After**

Compute is ready; data approval is pending. If approval has not arrived by Friday, use public samples next week to check the pipeline. Final evaluation still requires authorized project data.

**Reason**

Replace blanket pessimism with available resources, a decision trigger and a feasible fallback.

[Full case and conditions to preserve](examples.md#ex-06)

</details>

<a id="dw-006"></a>

## DW-006 · Evaluate a qualification

**Mode**: Diagnose

```text
Inspect the passage and explain the function of each suspect qualification.
Use the supplied evidence and conditions to distinguish useful information
from repetition. Return the requested diagnosis.

Task: For each suspect qualification, explain what it changes and which supplied
facts justify it. Remove stacked hedges while preserving forecasts, targets,
estimates and conditions as such.

Output: The function, grounds and keep-or-revise recommendation for each
qualification.

Input material:
Sentence: [fill in]
Factual context: [fill in]
Uncertainty sources: [fill in]
```

<details>
<summary>See a related case · EX-02 · A forecast is not a promise</summary>

**Facts**

At the current workload, completion is estimated for Thursday. New data arriving Wednesday would move the estimate to Friday. No fixed date has been promised to the client.

**Before**

Completion might possibly be around Thursday, although the situation is complex and uncertainty remains.

**After**

At the current workload, completion is estimated for Thursday, or Friday if new data arrives Wednesday.

**Reason**

Replace stacked hedges with an explicit estimate and the supplied condition that changes timing.

[Full case and conditions to preserve](examples.md#ex-02)

</details>
