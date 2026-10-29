# Data interpretation

**English** | [简体中文](../zh/analysis.md)

[All categories](index.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

- [DW-049 Chart takeaway](#dw-049)
- [DW-050 Association versus causation](#dw-050)
- [DW-051 Sample and generalization](#dw-051)
- [DW-052 Forecast and scenario](#dw-052)
- [DW-053 Negative or inconclusive findings](#dw-053)
- [DW-054 Multiple-metric trade-offs](#dw-054)

<a id="dw-049"></a>

## DW-049 · Chart takeaway

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Check axes, units, denominators, periods and comparability before giving the
main observation. Separate chart facts from causal interpretation and retain
material uncertainty.

Output: A main chart takeaway followed by measurement definitions and necessary
interpretation.

Input material:
Chart data: [fill in]
Axes and units: [fill in]
Comparison definition: [fill in]
```

<details>
<summary>See a related case · EX-17 · Chart denominators and samples</summary>

**Facts**

Fictional chart: activity A has 20 completions among 100 participants; B has 30 among 200. Participants self-selected into different groups, without random assignment, in the same period. The requested comparison is completion rate, not count.

**Before**

B has more people, so it is clearly more effective. Of course, many factors may exist, so nothing can be concluded.

**After**

A's completion rate is 20% (20/100), versus 15% (30/200) for B. The groups self-selected, so the comparison describes completion rates rather than identifying causal effects.

**Reason**

Compute the supported rates, retain denominators and correct the causal overclaim.

[Full case and conditions to preserve](examples.md#ex-17)

</details>

<a id="dw-050"></a>

## DW-050 · Association versus causation

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Calibrate claims to design and evidence. Remove hedge stacking without
upgrading associations, predictions or group differences to causality;
correct overclaims when warranted.

Output: A design-calibrated conclusion and an explanation of claim-strength wording
changes.

Input material:
Claim: [fill in]
Design: [fill in]
Analysis: [fill in]
Results: [fill in]
```

<details>
<summary>See a related case · EX-17 · Chart denominators and samples</summary>

**Facts**

Fictional chart: activity A has 20 completions among 100 participants; B has 30 among 200. Participants self-selected into different groups, without random assignment, in the same period. The requested comparison is completion rate, not count.

**Before**

B has more people, so it is clearly more effective. Of course, many factors may exist, so nothing can be concluded.

**After**

A's completion rate is 20% (20/100), versus 15% (30/200) for B. The groups self-selected, so the comparison describes completion rates rather than identifying causal effects.

**Reason**

Compute the supported rates, retain denominators and correct the causal overclaim.

[Full case and conditions to preserve](examples.md#ex-17)

</details>

<a id="dw-051"></a>

## DW-051 · Sample and generalization

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: State sample, period and measurement scope. Do not hide generalization
limits behind broad wording. Keep an explicit exclusion when positive scope
alone would invite misuse.

Output: A scoped conclusion identifying sample, period, measurement and
generalization conditions.

Input material:
Sample source: [fill in]
Period: [fill in]
Measures: [fill in]
Target population: [fill in]
```

<details>
<summary>See a related case · EX-17 · Chart denominators and samples</summary>

**Facts**

Fictional chart: activity A has 20 completions among 100 participants; B has 30 among 200. Participants self-selected into different groups, without random assignment, in the same period. The requested comparison is completion rate, not count.

**Before**

B has more people, so it is clearly more effective. Of course, many factors may exist, so nothing can be concluded.

**After**

A's completion rate is 20% (20/100), versus 15% (30/200) for B. The groups self-selected, so the comparison describes completion rates rather than identifying causal effects.

**Reason**

Compute the supported rates, retain denominators and correct the causal overclaim.

[Full case and conditions to preserve](examples.md#ex-17)

</details>

<a id="dw-052"></a>

## DW-052 · Forecast and scenario

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Distinguish forecasts, targets, commitments and hypothetical scenarios.
State assumptions, ranges or scenario differences without turning
conditional estimates into certainties.

Output: A forecast stating assumptions, scenarios, ranges or triggering conditions.

Input material:
Forecast: [fill in]
Assumptions: [fill in]
Ranges: [fill in]
Use: [fill in]
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

<a id="dw-053"></a>

## DW-053 · Negative or inconclusive findings

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Report what was not detected and the precision available. Distinguish lack
of significant evidence from evidence of absence; do not hide the result or
invent a positive finding.

Output: A negative-results paragraph reporting estimates, intervals and the
interpretation they support.

Input material:
Design: [fill in]
Estimates: [fill in]
Intervals: [fill in]
Test results: [fill in]
```

<details>
<summary>See a related case · EX-18 · An inconclusive result is not equivalence</summary>

**Facts**

A constructed study reports a difference test: the estimated group difference is 2 points, 95% CI −1 to 5, p=0.18. No equivalence margin was prespecified and no equivalence test was reported. The task is to report the analysis.

**Before**

The result is not significant, which may mean the study has little value. The situation is complex and more research may be needed, so it seems best to draw no conclusion.

**After**

The difference test did not detect a significant difference: the estimate was 2 points, 95% CI −1 to 5, p=0.18. No equivalence margin was prespecified and no equivalence test was reported, so these results do not provide evidence of equivalence.

**Reason**

Replace blanket self-dismissal with the estimate, interval and supported interpretation.

[Full case and conditions to preserve](examples.md#ex-18)

</details>

<a id="dw-054"></a>

## DW-054 · Multiple-metric trade-offs

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Report gains and costs under consistent conditions and units. Relate the
choice to the objective without treating one decline as total failure or
hiding unfavorable metrics.

Output: All relevant metrics and trade-offs, then a choice justified by the task
objective.

Input material:
Metrics: [fill in]
Test conditions: [fill in]
Objective priorities: [fill in]
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
