# Work updates

**English** | [简体中文](../zh/work.md)

[All categories](index.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

- [DW-019 Weekly update](#dw-019)
- [DW-020 Delay notice](#dw-020)
- [DW-021 Decision summary](#dw-021)
- [DW-022 Retrospective](#dw-022)
- [DW-023 Update for a decision-maker](#dw-023)
- [DW-024 Resource request](#dw-024)

<a id="dw-019"></a>

## DW-019 · Weekly update

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Organize completed work, blockers, next steps and requests. Preserve status
and dates; remove empty assurances without hiding important blockers.

Output: Completed work, current blockers, next steps and requests.

Input material:
Progress notes: [fill in]
plan: [fill in]
blockers: [fill in]
requests: [fill in]
```

<details>
<summary>See a related case · EX-07 · A blocker and revised schedule</summary>

**Facts**

Fictional update: page development is complete; API access has not been enabled; integration testing has not started. A testable build was due Tuesday and is now committed for Thursday. The owner asks the project manager to coordinate access today. The meeting confirmed this revision.

**Before**

Overall progress is good and we are working hard. Due to complexity, there might be a slight delay; thank you for understanding.

**After**

Page development is complete, but API access is still unavailable and integration testing has not started. Delivery of a testable build moves from Tuesday to Thursday. Please coordinate API access today.

**Reason**

State completion, blocker, revised commitment and requested action rather than empty assurances.

[Full case and conditions to preserve](examples.md#ex-07)

</details>

<a id="dw-020"></a>

## DW-020 · Delay notice

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: State the original plan, change, known cause and recovery arrangement.
Distinguish committed dates from estimates; acknowledge responsibility and avoid
invented remedies.

Output: A sendable delay notice containing the original plan, change, cause and
revised arrangement.

Input material:
Original schedule: [fill in]
status: [fill in]
cause: [fill in]
revised arrangement: [fill in]
```

<details>
<summary>See a related case · EX-07 · A blocker and revised schedule</summary>

**Facts**

Fictional update: page development is complete; API access has not been enabled; integration testing has not started. A testable build was due Tuesday and is now committed for Thursday. The owner asks the project manager to coordinate access today. The meeting confirmed this revision.

**Before**

Overall progress is good and we are working hard. Due to complexity, there might be a slight delay; thank you for understanding.

**After**

Page development is complete, but API access is still unavailable and integration testing has not started. Delivery of a testable build moves from Tuesday to Thursday. Please coordinate API access today.

**Reason**

State completion, blocker, revised commitment and requested action rather than empty assurances.

[Full case and conditions to preserve](examples.md#ex-07)

</details>

<a id="dw-021"></a>

## DW-021 · Decision summary

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Lead with a recommendation and decisive grounds, then switching conditions and
costs. If evidence does not support a choice, specify the missing test rather than
offering empty balance.

Output: A recommendation followed by decisive evidence, costs and switching
conditions.

Input material:
Options: [fill in]
criteria: [fill in]
evidence: [fill in]
constraints: [fill in]
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

<a id="dw-022"></a>

## DW-022 · Retrospective

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Separate facts, explanations and improvements. Identify supported,
controllable causes; remove vague reflection and self-justification without
assigning unsupported blame.

Output: A retrospective organized around facts, verified causes and improvements.

Input material:
Timeline: [fill in]
outcomes: [fill in]
verified causes: [fill in]
improvements: [fill in]
```

<details>
<summary>See a related case · EX-08 · Retrospective and resource request</summary>

**Facts**

Fictional incident: Wednesday delivery was two hours late. Logs show the build machine's disk was full; clearing the cache restored operation. The team agreed to a pre-delivery space check and requests a spare drive with a budget ceiling of CNY 600; approval is pending. There is no evidence of individual negligence.

**Before**

We have many shortcomings and need comprehensive reflection; some people may not have been careful enough. We hope management might consider offering some support.

**After**

Wednesday delivery was delayed by two hours because the build machine's disk was full; clearing the cache restored operation. The team adds a pre-delivery space check and requests a spare drive costing no more than CNY 600, pending approval.

**Reason**

Use a verified cause and concrete improvement, with an explicit pending resource request.

[Full case and conditions to preserve](examples.md#ex-08)

</details>

<a id="dw-023"></a>

## DW-023 · Update for a decision-maker

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Lead with what the reader needs to know or decide, followed by impact and
evidence. Make the pending decision explicit while preserving relevant protocol and
courtesy.

Output: The information or decision needed first, followed by impact and evidence.

Input material:
Issue: [fill in]
impact: [fill in]
requested decision: [fill in]
protocol: [fill in]
```

<details>
<summary>See a related case · EX-08 · Retrospective and resource request</summary>

**Facts**

Fictional incident: Wednesday delivery was two hours late. Logs show the build machine's disk was full; clearing the cache restored operation. The team agreed to a pre-delivery space check and requests a spare drive with a budget ceiling of CNY 600; approval is pending. There is no evidence of individual negligence.

**Before**

We have many shortcomings and need comprehensive reflection; some people may not have been careful enough. We hope management might consider offering some support.

**After**

Wednesday delivery was delayed by two hours because the build machine's disk was full; clearing the cache restored operation. The team adds a pre-delivery space check and requests a spare drive costing no more than CNY 600, pending approval.

**Reason**

Use a verified cause and concrete improvement, with an explicit pending resource request.

[Full case and conditions to preserve](examples.md#ex-08)

</details>

<a id="dw-024"></a>

## DW-024 · Resource request

```text
Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Specify resources, purpose, rationale and the supported consequence of
nonapproval. Distinguish requests from authorized resources; avoid self-effacement
and invented returns.

Output: A resource request stating supplied quantities or budget, purpose, grounds
and requested approval.

Input material:
Requested resources: [fill in]
purpose: [fill in]
cost: [fill in]
supporting facts: [fill in]
```

<details>
<summary>See a related case · EX-08 · Retrospective and resource request</summary>

**Facts**

Fictional incident: Wednesday delivery was two hours late. Logs show the build machine's disk was full; clearing the cache restored operation. The team agreed to a pre-delivery space check and requests a spare drive with a budget ceiling of CNY 600; approval is pending. There is no evidence of individual negligence.

**Before**

We have many shortcomings and need comprehensive reflection; some people may not have been careful enough. We hope management might consider offering some support.

**After**

Wednesday delivery was delayed by two hours because the build machine's disk was full; clearing the cache restored operation. The team adds a pre-delivery space check and requests a spare drive costing no more than CNY 600, pending approval.

**Reason**

Use a verified cause and concrete improvement, with an explicit pending resource request.

[Full case and conditions to preserve](examples.md#ex-08)

</details>
