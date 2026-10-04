# Week 55 fresh student revision

Completed October 4, 2026. Scope: only the revision stage, one combined ten-page Grades 3–5 packet, following `plans/new-themes-52-63/STAGE-ROUTING.md`. The generic three-band defaults do not apply. No facilitator guide, other stage, released collection output, global index, publication, or remote copy was authored or changed.

Current review output: [students.pdf](../../../../tmp/worksheet-runs/week-55-new-v1/final/students.pdf), W55-S-v2, US Letter landscape. PDF SHA256: `dcf7a9d6fbce6845baf61a8b5dab51ef9af63c90b7b7ffc1ffd935beca7ce511`.

## Located revisions

* **R1 / M1, page 6:** before Problem 6, the essential convention now states, “An input is equally spaced when neighboring numbers in increasing order have the same difference. That difference is its gap.” Numerical differences are thus defined before use; equal printed card separations do not define the property. All four contrasts and the open question remain. The common-gap inverse conclusion has not been printed as a solving procedure.
* **R2, page 9:** before Problem 9, an original compact visual shows A cards {1,4} and B cards {0,2,5,8}, then m=2 and n=4 card counts, then the substitutions m+n−1=2+4−1=5 and m×n=2×4=8. “Card counts” and “Substitute counts” label the bridge. These evaluate expressions without enumerating the example's totals or resolving the child's general question. Problem 9 expresses nonemptiness as at least one card in each input.
* **R2, page 10:** “Each input has at least two cards” replaces m≥2, n≥2. Both directions of the common-gap equality theorem and the open explanation/counterexample choice remain.
* **Optional page 5 brevity edit:** removed the pooling instruction. A later independently authored guide may consider pooling the catalog; the student task still requests every two-card B. Eight catalog records remain for the seven solutions.
* All footers identify the revision as W55-S-v2. Problems 1–10 remain consecutive; all fixed card trials, chosen-input sizes, result lanes, singleton contrasts, grids, sharp bound and inverse theorem remain.

The source README retains the original provenance distinctions, exact prerequisites, scope of source precedents, and unperformed physical/classroom checks. `MATH-NOTES.md` retains the complete arbitrary-size theorem proof and adds only revision convention notes. Source verifiers recognize the new footer and count example. `REPUBLISHING.md` and the draft are preserved.

## Final mathematical and digital evidence

The reviser independently recalculated the actual final tasks in [qa/independent_final_check.py](../../../../tmp/worksheet-runs/week-55-new-v1/final/qa/independent_final_check.py), importing none of the writer/critic verifiers or their outputs. [qa/independent-final-checks.json](../../../../tmp/worksheet-runs/week-55-new-v1/final/qa/independent-final-checks.json) records the results, final page/grid geometry, final source hashes, and fresh copied/ZIP-extracted rebuilds. The inherited author checks were also rerun and passed; they are supplemental evidence, not the basis for this fresh calculation.

| Final page | Actual task, values and rendering inspected |
|---|---|
| 1 | Shared rules and incomplete placement demonstration are accurate: tries 1+3=4, 4+0=4, 1+0=1, with positions-so-far {1,4}. Problem 1 counts 3 and 4. All visible inputs and both full 0–18 lanes checked. |
| 2 | Contrasting counts 5,6,9; all eighteen input values and three full lanes checked. Physical separation of the 0,1,3 cards is uniform, as intended for pictorial cards. |
| 3 | All 14,400 legal 3+3 kit designs independently checked; minimum 5 and maximum 9. Four records remain, each with correct three-card input sizes and full lane. |
| 4 | All 5,400 2+3, 9,450 2+4 and 25,200 3+4 designs checked; minima 4,5,6 and attainable upper counts 6,8,12. Slot counts and all three lanes checked. |
| 5 | All 45 B choices checked. Exactly seven solutions, {t,t+3} for t=0,…,6. Fixed A, eight B record spaces, total lines and full reusable lane remain legible. |
| 6 | Counts 4,6,4,4. The new value-difference definition appears before the unchanged four trials. Definition, task, cards and lanes have clear separation. |
| 7 | Counts 3,3,4; irregular B cases and A={0} preserve the singleton exception. All thirteen input values and three lanes checked. |
| 8 | Every row/column label, all 27 sum nodes and all 36 grid edges checked. Demonstration has 3 routes of 4 values; task grids have 6 routes of 5 values and 10 routes of 6 values. Each route increases strictly. Bold demonstrated route is right/up/right, 1,3,7,11. |
| 9 | New visual inputs/counts/substitutions checked in the actual PDF. Nonempty arbitrary whole-number input domain, both sharp bounds, and general explanation task remain. Four widely spaced writing lines remain. |
| 10 | Ordinary at-least-two restriction, inverse necessity question and common-gap sufficiency question checked in the actual PDF. Open work area remains. |

The independent full-kit finite computation checked all **1,046,529** ordered pairs of nonempty subsets of 0–9. Both bounds hold; the 20,360 singleton pairs all attain the lower bound; all 2,688 nonsingleton lower-equality pairs are precisely the pairs with a common positive numerical gap. These experiments verify the finite examples; they do not replace the arbitrary-size argument.

The general proof was independently reasoned through again: in a sorted addition array every right/up path visits m+n−1 strictly increasing sums, proving the lower bound. There are mn pairs, proving the upper bound. Consecutive inputs attain the lower bound; A={0,…,m−1}, B={0,m,…,(n−1)m} attains the upper bound by quotient/remainder uniqueness. If m,n≥2 and lower equality holds, every full path gives the entire sumset. Full paths sharing a prefix/suffix and choosing opposite intermediate corners of any adjacent square share m+n−2 distinct values; their remaining values must agree. Hence aᵢ₊₁−aᵢ=bⱼ₊₁−bⱼ for every adjacent i,j, forcing both inputs to have a common positive gap. Conversely, common-gap inputs produce precisely a+b+kd for 0≤k≤m+n−2. A singleton translates arbitrary B and therefore needs no equal-spacing assumption. Distinct values and nonempty ordinary whole-number inputs are essential; repeated cards are not extra set members, and modular wrapping is outside the task.

All **ten latest PNG pages** in `qa/render/` were individually viewed at 108 dpi after the revised PDF build. Every header, footer, card value, result lane and grid was inspected; no clipping, collision or broken symbol was found. The full actual-PDF vector audit found 380 result cells, each 12×18 mm; twenty full lanes, each 228 mm wide; 13×14 mm pictorial cards; and 9 mm grid nodes with equal horizontal/vertical spacing (20 mm in the example, 17 mm in both tasks). Edge counts are 7,12,17, with every required nearest-neighbor edge present. There is no polygon fit claim. Poppler is not installed here; PyMuPDF supplies the rendering under the direct routing's permitted runtime.

[qa/draft-preservation.json](../../../../tmp/worksheet-runs/week-55-new-v1/final/qa/draft-preservation.json) confirms that page bodies 1,2,3,4,7,8 are pixel-identical to the draft at 108 dpi; only their footer version changes. Student content edits are confined to pages 5,6,9,10. The original draft SHA256 still matches the independent review record.

## Portable source and boundaries

The final `src/` remains exactly **seven authored files**: `students.tex`, `build.py`, `verify_math.py`, `verify_pdf.py`, `verify_rebuild.py`, `README.md`, and `MATH-NOTES.md`. No exemplar, prompt, borrowed reference/PDF, generated PDF, raster asset, output JSON or TeX intermediate is inside it.

Fresh copied and seven-member ZIP-extracted sources were each built into separate clean output directories. All ten rebuilt pages match the delivered PDF exactly in text, page dimensions and rendered pixels at **120 dpi**. The independent test archive and rebuild outputs are QA intermediates; root owns release source packaging and indexing. The existing portable verifier also passed its 108 dpi comparison before the final note/verifier updates; the independent 120 dpi comparison covers the final seven-file source state.

No execution blocker remains. A separately authored and independently reviewed facilitator guide, organizer review, physical material handling/kit-fit checks, launch rehearsal, and classroom piloting remain later work. Digital dimensions and finite/general mathematical checks do not establish those outcomes. No remote copy is represented as current.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
