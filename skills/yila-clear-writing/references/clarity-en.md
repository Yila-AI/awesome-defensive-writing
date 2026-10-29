# Clear expression

**English** | [简体中文](clarity-zh.md)

Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.

## DW-001 · Sentence-level diagnosis

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

Related case: EX-01 in examples-en.md

## DW-002 · Minimal editing

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

Related case: EX-01 in examples-en.md

## DW-003 · Claim and grounds

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

Related case: EX-01 in examples-en.md

## DW-004 · Remove repeated caveats

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

Related case: EX-02 in examples-en.md

## DW-005 · Make advice actionable

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

Related case: EX-06 in examples-en.md

## DW-006 · Evaluate a qualification

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

Related case: EX-02 in examples-en.md
