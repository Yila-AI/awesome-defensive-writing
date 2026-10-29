# Technical guidance

**English** | [简体中文](technical-zh.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

## DW-043 · Beginner tutorial

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Give the shortest complete path supported by the material. Keep prerequisites,
expected observations and recovery steps; concision must not remove required
actions.

Output: A tutorial with prerequisites, steps, completion checks and recovery
actions.

Input material:
Task: [fill in]
environment: [fill in]
steps: [fill in]
failure cases: [fill in]

Related case: EX-15 in examples-en.md

## DW-044 · Installation instructions

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Preserve verified commands, versions, scope and order. Explain required
actions without generic warning piles; do not simplify commands by changing their
effects, and label untested environments.

Output: Installation instructions with environment and scope, supplied commands and
completion checks.

Input material:
Verified steps: [fill in]
versions: [fill in]
environment: [fill in]
scope: [fill in]

Related case: EX-15 in examples-en.md

## DW-045 · Troubleshooting

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Organize symptoms, observations, diagnosis and next action. Separate causes
from hypotheses; avoid blaming the user or defaulting to reinstalling, and retain
data-protection conditions.

Output: A troubleshooting table of symptoms, observations, current hypotheses and
next checks.

Input material:
Symptoms: [fill in]
logs: [fill in]
environment: [fill in]
attempts: [fill in]

Related case: EX-15 in examples-en.md

## DW-046 · SOP prerequisites

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Preserve order, units, parameters, prohibitions and applicability. Remove only
nonoperational repetition; do not replace a prohibition with a nonequivalent
positive suggestion.

Output: A numbered SOP retaining parameters, prerequisites, sequence and
prohibitions.

Input material:
Original SOP: [fill in]
scope: [fill in]
confirmed parameters: [fill in]

Related case: EX-16 in examples-en.md

## DW-047 · Code-review feedback

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: State the trigger, observable consequence and minimal fix, separating defects
from preferences. Do not invent execution results or obscure a real issue with vague
politeness.

Output: Review feedback with trigger, consequence, suggested fix and actual
verification status.

Input material:
Diff: [fill in]
relevant context: [fill in]
actual test results: [fill in]

Related case: EX-21 in examples-en.md

## DW-048 · Technical choice

Make the supplied material clear, direct and informative. Organize it around the
judgment or action the reader needs. Remove repetitive retreat and empty preambles.
Ground facts, numbers, scope, responsibility and commitments in the material; keep
meaningful conditions next to the claims they qualify. List missing facts
separately.

Task: Compare options against constraints and comparable evidence. Recommend when
justified and state switching conditions; otherwise identify a useful verification
step.

Output: An option comparison, recommended choice and conditions that would change
it.

Input material:
Constraints: [fill in]
options: [fill in]
measurements or docs: [fill in]
maintenance: [fill in]

Related case: EX-22 in examples-en.md
