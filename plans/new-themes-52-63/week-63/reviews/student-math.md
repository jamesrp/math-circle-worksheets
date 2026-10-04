# Week 63 fresh independent mathematical review

Reviewed October 4, 2026. I independently checked the actual combined `draft/students.pdf` (nine pages) and `draft/materials.pdf` (three pages), their authored sources, and the supplied instructions/research notes. I freshly rendered and viewed all twelve pages. No draft, guide, earlier week, workflow prompt, index or remote copy was edited.

All numerical claims, complete printed outcome decks, four/five-card catalogs, inclusive fixed-home intersections, alternating multiplicities, printed arrow examples, and reversible two-family constructions check out. The recurrence is correct for n>=2. The two located issues below confirm the critic's proposed targeted repairs; no upper mathematical content needs removal.

## R1 — first-use outcome/membership convention needs a visual bridge

**Location:** Grades 2-5, students p. 2, Problem 2; materials p. 2. Exact text: “Use the six A–C outcome cards. Make one group with A in home A and another with B in home B. A card may belong to both groups.” Materials p. 2 says “Each outcome card is one complete placement.”

**Evidence:** The first-page visual correctly records one whole row as VUWX and checks it against unchanged homes U,V,W,X, but neither p. 1 nor p. 2 demonstrates one whole-outcome object with two simultaneous group memberships. All six A-C outcome cards are correctly supplied. Their A-home group is {ABC,ACB}; B-home group is {ABC,CBA}; their shared outcome is the single row ABC, not two different rows. The arithmetic task has the correct intended result `6-2-2+1=3`, with BAC,BCA,CAB outside both groups. This is a first-use representation gap with a plausible alternative reading of “card” as an individual letter-card; it is not a false numerical claim or an observed classroom failure.

**Smallest repair preserving the mathematics:** Before Problem 2, add the critic's compact non-task visual that explicitly presents **one outcome card = one whole row**, reusing VUWX in U,V,W,X homes, with both “W in home W” and “X in home X” markers attached to that same outcome. Retain its unchanged reference row and persistent VUWX ID; avoid making two apparent outcomes or moving a card between membership checks. This proposed repair is mathematically verified: VUWX has exactly the home-match set {W,X}, so it belongs to both named groups at once and to neither U-home nor V-home. It neither supplies the A-C solution nor prescribes the add-back method.

## R2 — the two-family counting rule needs its valid domain

**Location:** Grades 4-5, students p. 9, Problem 9. Exact text: “Use the two families to give a counting rule for any number of distinct cards, and explain why each row is counted once.”

**Evidence:** For n>=2 the distinguished card has n-1 different possible homes. Each branch is bijective with a derangement on n-2 original labels in the reciprocal case or n-1 original labels in the longer case, giving `D_n=(n-1)(D_(n-2)+D_(n-1))`. Independent row-based deletion/insertion checks cover every row and inverse for n=2 through 5, retaining labels. At n=1 there is no different destination and no such two-family partition; substituting n=1 would require undefined D_-1. The exceptional counts are D_0=1 (the unique empty bijection) and D_1=0. At n=2 the verified rule uses these and gives one row.

**Smallest repair:** Replace “for any number of distinct cards” by “for two or more distinct cards.” Alternatively explicitly include zero/one-card starting cases as a separate part of a rule for all nonnegative n. The restriction is mathematically sufficient for the requested two-family explanation; the later adult guide must still state D_0=1, D_1=0 and the n>=2 domain. Do not print the recurrence as the student's method.

## Coverage and evidence

The Grades 3-5 pages (Problems 3-5) and all three material pages check out completely. Grades 2-5 pages have R1 only; Grades 4-5 pages have R2 only. No K-1 packet was required by direct routing. Explicit task-by-task outcomes, exact general proofs, all printed non-task examples, every checked permutation/intersection/reduction, PDF geometry and hashes, and a successful twelve-page clean copied-source rebuild are in [evidence/math-qa/README.md](../../../../tmp/worksheet-runs/week-63-new-v1/evidence/math-qa/README.md), with [check.py](../../../../tmp/worksheet-runs/week-63-new-v1/evidence/math-qa/check.py) and [results.json](../../../../tmp/worksheet-runs/week-63-new-v1/evidence/math-qa/results.json). The author's verifier was read for scope but was not run or used as independent proof.

Retain the new four/five-card overlap and reversible-construction investigations across future visits; the already-used three-card Week 43 rows are entry background. Complete finite enumeration and the general bijections/cancellation arguments support the mathematical conclusions. Cut handling, exact material fit, simultaneous-membership sorting, reversal rehearsal and classroom piloting remain unperformed. The reviewed draft sources rebuild consistently; final revised PDFs/ZIPs and any remote copies will need later verification.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
