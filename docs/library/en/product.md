# Product writing

**English** | [简体中文](../zh/product.md)

[All categories](index.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

- [DW-031 Feature description](#dw-031)
- [DW-032 Release notes](#dw-032)
- [DW-033 Product comparison](#dw-033)
- [DW-034 Direct FAQ answer](#dw-034)
- [DW-035 Landing-page value](#dw-035)
- [DW-036 Customer case study](#dw-036)

<a id="dw-031"></a>

## DW-031 · Feature description

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: State what eligible users can do, then steps and conditions. Use verified
capabilities and retain access, pricing, formats and beta scope without unverified
quality promises.

Output: One sentence describing the user capability, followed by actions and
necessary conditions.

Input material:
Verified feature: [fill in]
eligible users: [fill in]
conditions: [fill in]
placement: [fill in]
```

<details>
<summary>See a related case · EX-11 · A feature and its beta scope</summary>

**Facts**

Fictional product P: users on the current beta list can upload a PDF and choose a template to generate an editable figure draft. Public registration is not open. No efficiency study, free-use policy or submission-quality guarantee has been supplied. Release notes may announce only this beta capability.

**Before**

We might provide some assistance to some extent. Everyone can use it free and get submission-ready figures in one click.

**After**

Users in the current beta can upload a PDF and choose a template to generate an editable figure draft. Public registration is not yet open.

**Reason**

State the task clearly while retaining eligibility and draft status; remove redundant retreat and unsupported promotion.

[Full case and conditions to preserve](examples.md#ex-11)

</details>

<a id="dw-032"></a>

## DW-032 · Release notes

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Separate released, beta and planned changes. Describe user-visible behavior,
retaining breaking changes and migration steps instead of vague upgrade claims.

Output: Release notes grouped by availability, with required migration actions.

Input material:
Changes: [fill in]
release status: [fill in]
impact: [fill in]
migration steps: [fill in]
```

<details>
<summary>See a related case · EX-11 · A feature and its beta scope</summary>

**Facts**

Fictional product P: users on the current beta list can upload a PDF and choose a template to generate an editable figure draft. Public registration is not open. No efficiency study, free-use policy or submission-quality guarantee has been supplied. Release notes may announce only this beta capability.

**Before**

We might provide some assistance to some extent. Everyone can use it free and get submission-ready figures in one click.

**After**

Users in the current beta can upload a PDF and choose a template to generate an editable figure draft. Public registration is not yet open.

**Reason**

State the task clearly while retaining eligibility and draft status; remove redundant retreat and unsupported promotion.

[Full case and conditions to preserve](examples.md#ex-11)

</details>

<a id="dw-033"></a>

## DW-033 · Product comparison

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Compare the same task under consistent conditions and dates. Report verifiable
differences and unknowns; avoid fabricated competitor claims or unfair setups.

Output: A like-for-like comparison, a use-case choice and missing information.

Input material:
Products: [fill in]
task: [fill in]
comparable facts: [fill in]
date: [fill in]
```

<details>
<summary>See a related case · EX-22 · Choose against the goal and report the trade-off</summary>

**Facts**

Constructed selection task: offline operation is required, lower latency is the priority, and an accuracy decrease of up to 1 percentage point is acceptable. A and B both support the required offline format. On the same machine and test set, A has 90% accuracy and 100 ms latency; B has 89% accuracy and 60 ms latency. Pricing is not supplied.

**Before**

Both tools have pros and cons, and there are many uncertainties, so it is difficult to judge. B also loses accuracy and can only be considered cautiously; it depends on the user.

**After**

Choose B for the stated goal. Both meet the offline requirement; B reduces latency from 100 to 60 ms while accuracy falls from 90% to 89%, meeting the allowed 1-percentage-point decrease.

**Reason**

Turn empty balance into a comparable assessment and conditional choice, stating both gain and cost.

[Full case and conditions to preserve](examples.md#ex-22)

</details>

<a id="dw-034"></a>

## DW-034 · Direct FAQ answer

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Answer the specific question first, then conditions and actions. Identify
unknowns rather than evading with generic disclaimers; retain material costs and
deletion consequences.

Output: The direct answer first, followed by conditions and next steps.

Input material:
Question: [fill in]
confirmed rules: [fill in]
instructions: [fill in]
```

<details>
<summary>See a related case · EX-24 · Answer a pricing question directly</summary>

**Facts**

Fictional product rules: visitors can view public examples; exporting requires a paid plan, with no free export allowance. The user asks whether export is available without payment. No other capabilities need describing.

**Before**

We value different user needs, and circumstances may vary; we suggest exploring for yourself.

**After**

No. Export requires a paid plan and has no free allowance. You can view the public examples first.

**Reason**

Answer the known rule directly and offer a real available option instead of evasive filler.

[Full case and conditions to preserve](examples.md#ex-24)

</details>

<a id="dw-035"></a>

## DW-035 · Landing-page value

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Connect features to users and concrete tasks with verifiable value. Remove
empty value language without inventing efficiency gains, guarantees or endorsements.

Output: A headline, subheadline and three supported value points.

Input material:
Audience: [fill in]
task: [fill in]
feature: [fill in]
evidence: [fill in]
```

<details>
<summary>See a related case · EX-12 · A case is not a performance guarantee</summary>

**Facts**

Fictional case: user A permits anonymous use of 'I turned scattered notes into an outline.' Records show notes imported and the generated outline manually revised. No timing, comparison group or quality score exists. The team confirms it cannot guarantee freedom from manual editing.

**Before**

This is merely a small preliminary attempt that may help some people; it has proven tenfold efficiency for everyone with no editing needed.

**After**

User A shared: 'I turned scattered notes into an outline.' The workflow included importing notes and manually revising the result. The case illustrates one way to organize notes; it does not guarantee editing-free results for every task.

**Reason**

Use the authorized quote and observed workflow while directly answering the guarantee question.

[Full case and conditions to preserve](examples.md#ex-12)

</details>

<a id="dw-036"></a>

## DW-036 · Customer case study

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Distinguish quotes, verified process and outcome data. Avoid unsupported
attribution and universal results; use approved anonymization for identities without
permission.

Output: A case narrative with the authorized quote, actual workflow, recorded result
and measurement definition.

Input material:
Permission: [fill in]
quotes: [fill in]
process: [fill in]
measurement definition: [fill in]
```

<details>
<summary>See a related case · EX-12 · A case is not a performance guarantee</summary>

**Facts**

Fictional case: user A permits anonymous use of 'I turned scattered notes into an outline.' Records show notes imported and the generated outline manually revised. No timing, comparison group or quality score exists. The team confirms it cannot guarantee freedom from manual editing.

**Before**

This is merely a small preliminary attempt that may help some people; it has proven tenfold efficiency for everyone with no editing needed.

**After**

User A shared: 'I turned scattered notes into an outline.' The workflow included importing notes and manually revising the result. The case illustrates one way to organize notes; it does not guarantee editing-free results for every task.

**Reason**

Use the authorized quote and observed workflow while directly answering the guarantee question.

[Full case and conditions to preserve](examples.md#ex-12)

</details>
