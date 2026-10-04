# Week 55 independent math review

Reviewed October 4, 2026. Scope: the actual ten-page combined Grades 3–5 `draft/students.pdf`, as required by direct STAGE-ROUTING.md. The generic three-band filenames do not apply; no omitted K–1 or separate 2–3 packet was assumed checked.

**Verdict:** all printed sums, finite catalogs, attainable extrema, grid entries, route claims, bounds and the non-singleton common-gap equality theorem are correct under the intended numerical conventions. One representation ambiguity needs a small definition; it is the same located issue as adversarial critic R1. No other mathematical defect was found. The separate critic R2 convention revision remains required and is not waived by this review.

## Located finding M1: define numerical spacing

**Band / location:** Grades 3–5, page 6, Problem 6; inherited by page 7, Problem 7 and page 10, Problem 10.

**Exact text:** “Each input is equally spaced.” Problem 7 asks “Does B need equal spacing?” Problem 10 asks “Must both inputs be equally spaced, with the same gap in A and B?”

**Evidence:** equal spacing has not been defined as equal *differences between ordered values*. Actual printed card centers are uniformly spaced regardless of the values: on page 2, the A cards 0,1,3 have centers approximately x=92.126,134.646,177.166 points, successive 15 mm separations, although their numerical gaps are 1 and 2. Consequently a literal reading about pictured card separation makes this irregular input “equally spaced” too and removes the meaningful distinction in Problems 6, 7 and 10. Under the intended numerical reading the mathematics is correct: Problem 6's four counts are 4,6,4,4; its second pair has A gap 2 and B gap 3. Problem 7 supplies genuine irregular B examples. Problem 10's inverse theorem holds with common numerical gaps, not a condition on drawing placement.

**Smallest fix:** define at or before first substantive use: “Equally spaced means that neighboring numbers in increasing order have the same difference.” Treat “gap” as that difference. Preserve the four contrasts and both directions of Problem 10; do not print the common-gap conclusion as a solving procedure. This is a mathematical convention clarification, not evidence of classroom failure.

## Coverage and evidence

The combined Grades 3–5 packet checks out mathematically apart from M1. [audit.md](../../../../tmp/worksheet-runs/week-55-new-v1/math-review-evidence/audit.md) states the request and independently verified outcome for **every Problem 1–10 and both worked demonstrations**, and supplies a complete arbitrary-size proof of the bound and both equality implications, including the singleton, empty-input, repeated-value and modular limits. Tao is contextual provenance; no missing equality proof is assumed from the sample.

[independent_check.py](../../../../tmp/worksheet-runs/week-55-new-v1/math-review-evidence/independent_check.py) and [checks.json](../../../../tmp/worksheet-runs/week-55-new-v1/math-review-evidence/checks.json) are fresh evidence, importing and executing no author or critic verifier. They independently check all 1,046,529 nonempty 0–9 input pairs; all 14,400, 5,400, 9,450 and 25,200 designs for the printed sizes; all 45 Problem 5 candidates (exactly seven solutions); and all 3,6,10 routes in the three grids. Actual PDF extraction verifies every input/grid label, all 380 12×18 mm result cells, 228 mm result lanes, 13×14 mm pictorial cards, 9 mm nodes, equal x/y grid spacing and all grid edges. I viewed all ten fresh 120 dpi render images.

[rebuild-checks.json](../../../../tmp/worksheet-runs/week-55-new-v1/math-review-evidence/rebuild-checks.json) records an independently compared fresh ZIP-extracted build: every draft page matches in text, dimensions and 120 dpi pixels. Reviewed PDF SHA256: `4042f6ab9717ae4d4a7ea2b9f6329a608fa97dfbc6099bf27a66f141b7495504`.

The draft and its sources were not edited. No tooling blocker remains for this stage. Physical handling, actual kit fit, launch rehearsal and classroom piloting remain unperformed; revised final PDFs and a later independently authored guide require their own checks.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
