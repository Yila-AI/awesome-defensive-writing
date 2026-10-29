# Technical guidance

**English** | [简体中文](../zh/technical.md)

[All categories](index.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

- [DW-043 Beginner tutorial](#dw-043)
- [DW-044 Installation instructions](#dw-044)
- [DW-045 Troubleshooting](#dw-045)
- [DW-046 SOP prerequisites](#dw-046)
- [DW-047 Code-review feedback](#dw-047)
- [DW-048 Technical choice](#dw-048)

<a id="dw-043"></a>

## DW-043 · Beginner tutorial

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Give the shortest complete path supported by the material. Keep
prerequisites, expected observations and recovery steps; concision must not
remove required actions.

Output: A tutorial with prerequisites, steps, completion checks and recovery
actions.

Input material:
Task: [fill in]
Environment: [fill in]
Steps: [fill in]
Failure cases: [fill in]
```

<details>
<summary>See a related case · EX-15 · A complete tutorial path</summary>

**Facts**

Fictional offline-tool instructions: on a tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill. Copying only SKILL.md loses references. If it is missing, first check folder nesting. No install command or other tested operating system is supplied.

**Before**

Installation may carry various risks; proceed cautiously. Copy a file and it will work on every system.

**After**

On the tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill; if missing, check whether the folder is nested one level too deep.

**Reason**

Keep the environment, full-folder requirement and observable check; remove generic caution and universal compatibility claims.

[Full case and conditions to preserve](examples.md#ex-15)

</details>

<a id="dw-044"></a>

## DW-044 · Installation instructions

**Mode**: Revise

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Preserve verified commands, versions, scope and order. Explain required
actions without generic warning piles; do not simplify commands by changing
their effects, and label untested environments.

Output: Installation instructions with environment and scope, supplied commands and
completion checks.

Input material:
Verified steps: [fill in]
Versions: [fill in]
Environment: [fill in]
Scope: [fill in]
```

<details>
<summary>See a related case · EX-15 · A complete tutorial path</summary>

**Facts**

Fictional offline-tool instructions: on a tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill. Copying only SKILL.md loses references. If it is missing, first check folder nesting. No install command or other tested operating system is supplied.

**Before**

Installation may carry various risks; proceed cautiously. Copy a file and it will work on every system.

**After**

On the tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill; if missing, check whether the folder is nested one level too deep.

**Reason**

Keep the environment, full-folder requirement and observable check; remove generic caution and universal compatibility claims.

[Full case and conditions to preserve](examples.md#ex-15)

</details>

<a id="dw-045"></a>

## DW-045 · Troubleshooting

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Organize symptoms, observations, diagnosis and next action. Separate causes
from hypotheses; avoid blaming the user or defaulting to reinstalling, and
retain data-protection conditions.

Output: A troubleshooting table of symptoms, observations, current hypotheses and
next checks.

Input material:
Symptoms: [fill in]
Logs: [fill in]
Environment: [fill in]
Attempts: [fill in]
```

<details>
<summary>See a related case · EX-15 · A complete tutorial path</summary>

**Facts**

Fictional offline-tool instructions: on a tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill. Copying only SKILL.md loses references. If it is missing, first check folder nesting. No install command or other tested operating system is supplied.

**Before**

Installation may carry various risks; proceed cautiously. Copy a file and it will work on every system.

**After**

On the tested Windows setup, copy the whole sample-skill folder into the client's configured skills directory, retaining references. Reload the client and check for sample-skill; if missing, check whether the folder is nested one level too deep.

**Reason**

Keep the environment, full-folder requirement and observable check; remove generic caution and universal compatibility claims.

[Full case and conditions to preserve](examples.md#ex-15)

</details>

<a id="dw-046"></a>

## DW-046 · SOP prerequisites

**Mode**: Revise

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Preserve order, units, parameters, prohibitions and applicability. Remove
only nonoperational repetition; do not replace a prohibition with a
nonequivalent positive suggestion.

Output: A numbered SOP retaining parameters, prerequisites, sequence and
prohibitions.

Input material:
Original SOP: [fill in]
Scope: [fill in]
Confirmed parameters: [fill in]
```

<details>
<summary>See a related case · EX-16 · A prohibition and a real trade-off</summary>

**Facts**

Fictional maintenance task: power must be disconnected before opening the service cover; opening it while powered is prohibited. Records need equipment ID and date. Route A organizes records without opening the cover. Route B checks internal wiring and requires opening the cover only after disconnection. These prerequisites are supplied; no other procedure is requested.

**Before**

Always remember safety and try to disconnect power before opening. For simplicity, both routes can be described as directly checking the device.

**After**

Route A: organize maintenance records with equipment ID and date; no cover opening is needed. Route B: disconnect power before opening the service cover to check internal wiring. Opening while powered is prohibited.

**Reason**

Replace admonition with operational language while retaining the prohibition and route distinction.

[Full case and conditions to preserve](examples.md#ex-16)

</details>

<a id="dw-047"></a>

## DW-047 · Code-review feedback

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: State the trigger, observable consequence and minimal fix, separating
defects from preferences. Do not invent execution results or obscure a real
issue with vague politeness.

Output: Review feedback with trigger, consequence, suggested fix and actual
verification status.

Input material:
Diff: [fill in]
Relevant context: [fill in]
Actual test results: [fill in]
```

<details>
<summary>See a related case · EX-21 · A code-review comment with a trigger</summary>

**Facts**

Fictional code: def first(items): return items[0]. Empty lists are possible. The reviewer has not run tests. The interface specifies None for empty input.

**Before**

This implementation might not be very elegant; consider some edge cases carefully. I tested it and everything passed.

**After**

When items is empty, items[0] raises IndexError rather than returning None as the interface specifies. Add an empty-list check returning None. Tests have not been run.

**Reason**

State a verifiable trigger and consequence; remove vague aesthetic criticism and a fabricated test claim.

[Full case and conditions to preserve](examples.md#ex-21)

</details>

<a id="dw-048"></a>

## DW-048 · Technical choice

**Mode**: Draft

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Compare options against constraints and comparable evidence. Recommend when
justified and state switching conditions; otherwise identify a useful
verification step.

Output: An option comparison, recommended choice and conditions that would change
it.

Input material:
Constraints: [fill in]
Options: [fill in]
Measurements or docs: [fill in]
Maintenance: [fill in]
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
