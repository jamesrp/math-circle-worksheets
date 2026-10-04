# Week 58 revision record

Completed 4 October 2026 as the fresh revision stage only. Read AGENTS.md, root README.md and REPUBLISHING.md, direct STAGE-ROUTING.md, PROMPT.md and REVISE.md, both independent reviews, all actual draft student/material pages, and the original editable source. Revised only this run's final student/material packet, sources and evidence. No facilitator guide, global index, other week, workflow prompt, remote copy or publication was changed. No subagents were used.

Current local review candidate: **students.pdf, 7 pages**, and **materials.pdf, 10 pages**, footer version **v2**. The final source directory has exactly seven files: `common.tex`, `students.tex`, `materials.tex`, `build.sh`, `verify_math.py`, `verify_pdf.py`, and `README.md`. There are no generated prompts, borrowed exemplars, books/reference PDFs, copied student PDFs, render images or build intermediates in `src/`. Root handles release indexing and final source packaging later. Separate guide authorship/review is still outstanding by stage design.

## Review issue trace

| Located issue in review.md / review-math.md | Actual final change | Delivered-page and source evidence |
| --- | --- | --- |
| Required exact thirds versus page-3 entry prerequisite | Kept the full-size physical differing-preference cut-and-choose trials and role reversal. Removed the four-row exact score table and the mandatory instruction to find each observer's piece values. The child marks a cut on the sketch, writes its distance from the left end, and circles the chooser's piece. Exact thirds moved to an adult/readiness continuation in source notes, with its fraction prerequisites and exact answers. | Student p. 3 / Problem 3; `students.tex`; `README.md` prerequisites and readiness continuation. The non-task value-2 panel → two equal 75 mm lengths → value 1 each visual remains before use. The target 100/200 mm cut answers are absent from the student task. |
| Paper R3 could be read as an added fourth card | Problem 5 now explicitly says to **replace R3 with its paper copy**. The material page and U/V cards repeat the essential replacement rule. Preparation puts the sturdy R3 away before the paper copy enters, preserving total value 3. | Student p. 5 / Problem 5; material pp. 1,3; `students.tex`, `materials.tex`; `README.md` print recipe and exact problem subsets. Whole-square value 1 and equal-area valuation remain. |
| Seven unused reusable cutouts and unused preference rows; unclear kit copies | Removed R4, B3, B4, G1–G4 and the green geometry/color code. Material p. 1 now supplies R1,R2,R3,B1,B2 plus one separate paper R3. A/B cards show red/blue only; U/V show red only. Kept 100×150 mm usable card dimensions. Added exact five-pair/one-upper-kit recipes and stock versus first-route counts without inventing tasks to justify inventory. | Material pp. 1–3; all actual upper/strip pages retained; `common.tex`, `materials.tex`; `README.md` exact material page/copy table. See geometry/copy checks below. |
| Unkeyed page-2 and page-6 score tables | Page 2 labels its six allocation records and binds the single table to a selected saved record number. Page 6 labels the table **Initial allocation only: A has X, B has Y, C has Z**, with A's/B's/C's tray columns. No supplementary ledger for every catalog allocation or repaired state was added; existing lines remain for the repair. | Student pp. 2,6; `students.tex`; actual PDF text and renders. One observer row evaluates one recoverable unchanged allocation before any rearrangement. |

## Mathematics preserved and independently checked

The revised task instances retain the whole-card investigation/impossibility, the differing-value physical cuts, the exact two-person guarantee and equal-length counterexample, the three-person fairness distinction and repair, and the general two-/three-person implication questions. The early input → division → choice/remainder visual conserves three tokens and does not reveal the four-card catalog. Student headers remain honest approximate Grades 2–5 on pp. 1,2,3,5 and Grades 3–5 on pp. 4,6,7. There is no manufactured K–1 worksheet; an optional oral younger divide/choose action is documented separately from the numerical catalog/proof route.

Ran the revised authored `verify_math.py` and, independently, **reran the critic's `math-review-assets/independent_checks.py::math_audit` without importing the authored verifier**. The independent implementation enumerates allocations by bit masks/listed trays and computes cuts by integrating panel portions. Its new output is `final/independent-math.json`; authored output is `final/math-checks.json`.

| Problem | Complete allocations / cuts checked | Result |
| --- | --- | --- |
| 1: R1,R2,R3,B1 | All 16 labelled complete allocations | Exactly 4 envy-free, also exactly 4 proportional. Both chooser-role assignments can realize each success with ties allowed. |
| 2: R1,R2,B1,B2 | All 16 labelled complete allocations | Exactly 5 envy-free, also exactly 5 proportional: preferred-color split plus four labelled mixed splits. |
| 3: constant-density paper | Every integer-mm cut plus exact density calculation | A's exact equal-value cut is 100 mm from the red/left end: A (2,2), B (2/3,10/3), B chooses right. B's is 200 mm: B (2,2), A (10/3,2/3), A chooses left. Strictly positive panel density makes each cumulative value strictly increasing, so no other real equal-value cut exists. These exact fractional scores are adult continuation, not mandatory page-3 records. |
| 4: both use A scale, cut at color join | Exact midpoint scores | Both observers see (3,1); the chooser takes red, and the cutter's blue is below half and envied. The first task's equal-own-value cut guarantee remains exact and conditional. |
| 5: three whole red cards | All 8 complete allocations | No envy-free or proportional allocation. Equal preferences require equal counts, impossible with total 3. Replacing R3 by a splittable uniform-value square and giving each one whole card plus half the square gives 3/2 each. |
| 6: X,Y,Z / cyclic rows | All 27 complete allocations, including empty trays and multiple panels per tray | Exactly 2 proportional allocations; exactly 1 envy-free allocation. Initial A:X/B:Y/C:Z gives own 4 of total 12 but envy of an 8-valued panel. Unique repair A:Y/B:Z/C:X gives each own 8 against alternatives 4 and 0. |
| 7: general implications | Algebra plus finite sanity checks | Envy-free implies proportional: add all n comparisons to obtain total ≤ n×own. For n=2, proportional gives own ≥ total−own = other, so the converse holds. For n=3, Problem 6 refutes the converse. Completeness/additivity are necessary; finite checks supplement the explanation. |

The independent additional sweep covers 4,096 nonnegative two-person value profiles on three goods and 32,768 complete allocations, including zero values and empty trays; 169 two-bundle and 2,197 three-bundle observer rows; and 308 legal choices after exact halving for two-panel densities 0–3, including zero density and ties. These checks do not prove a universal theorem without the preceding algebra.

## Actual rendered geometry and copy counts

`final/qa-checks.json` records checks against PDF vector outlines and actual extracted text. All student pages are portrait Letter. Material pp. 2–5 are rotated landscape Letter; all others portrait. Every page's media box is 612×792 pt with the expected rotation, header, footer v2 and consecutive Problem 1–7 labels. Text and vectors stay within page bounds.

* Material p. 1: **six** actual 25×25 mm borders: five reusable goods plus the separate paper R3. Only used labels appear.
* Material pp. 2–5: **seven** actual 100×150 mm preference borders, distributed 2,2,2,1. Printed dot counts by page are 8,2,24,12; numerals and panel/color labels match all tasks. The upper A/B set is explicitly X/Y/Z and separate from two-person color preferences.
* Material p. 5: three actual **50×40 mm** panels X,Y,Z, indivisible in Problem 6.
* Material pp. 6–10: exactly **four 150×40 mm halves per page**, matching red/blue strip numbers 1–2,3–4,5–6,7–8,9–10. The twenty halves produce **ten 300×40 mm strips** after a true no-overlap/no-gap butt seam, red on the left and blue on the right, tape on the back. No 300 mm strip is shrunk onto Letter.
* Every material page has exactly one actual **100 mm** check bar; PDF rounding error is less than 0.001 mm. The four remaining blue material icons have four equal sides; no unused green polygons remain. Student blue squares and rectangular/sketch proportions were also inspected visually on all affected pages. Rectangular panels/strips are intentionally not regular polygons.
* Recommended whole-group recipe: five copies each of material pp. **1,2,3,6–10**, and one copy each of pp. **4,5** = **42 printed sheets**. Result: 25 reusable goods, 5 paper R3 replacements, 23 preference cards, 3 upper panels, **100 half-strips / 50 full strips**, plus 13 separately supplied trays and 5 rulers. Page 1 is printed on ordinary paper; mount only the five reusable squares, leaving the separate replacement unmounted.
* Smaller first-route subset: five copies each of material pp. **1,2,3,6,7**, and one copy each of pp. **4,5** = **27 sheets**, same card/upper-kit quantities and **40 halves / 20 full strips** (four strips per pair). The ten strips per pair in full stock support retries/revisits, not ten required trials.

## Complete visual inspection and rebuild evidence

Rendered the **actual final PDFs** at 108 dpi and viewed **every full-page image**, not only text or contact sheets. Images and extracted text stay outside the portable source, under `final/renders/` and `final/*-text.txt`.

| Final pages viewed | Visual result |
| --- | --- |
| Students 1 | Whole-card entry, fixed scales, three-token convention visual, card IDs and four records intact; no overlap. |
| Students 2 | Six legible labelled records and one saved-record score table; adequate writing space, no clipping. |
| Students 3 | Worked partial-value convention, fixed A/B scales, two large cut sketches and distance labels; no exact-score ledger or target cut revealed. |
| Students 4 | Exact cut-and-choose argument and equal-length failure prompt intact; diagram/proof space clear. |
| Students 5 | Explicit R3 replacement and equal-area convention; whole-card graphics, two recording trays and explanation lines clear. |
| Students 6 | Cyclic preference table, unchanged initial tray diagram, initial-only A/B/C table and existing repair lines clear. |
| Students 7 | Two-/three-person implication tasks, one-observer pictures and substantial explanation space retained. |
| Materials 1 | Exactly five reusable cards plus paper replacement, replacement caption and 100 mm bar clear. |
| Materials 2 | Two large A/B red/blue cards, correct dot/numeral scales, no green row. |
| Materials 3 | Two large red-only U/V cards; replacement caption clear, no unused rows. |
| Materials 4 | Upper X/Y/Z A/B observer cards with 4/8/0 and 0/4/8 dots/numerals clear. |
| Materials 5 | Upper C observer 8/0/4 plus all three 50×40 mm panels clear. |
| Materials 6,7,8,9,10 | Each page's four halves separately inspected; matching numbers/colors, 150×40 labels, butt-join directions and 100 mm bar clear. |

Ran `verify_pdf.py` from the final seven-file source directory. A new clean copied source folder rebuilt **both PDFs**, then a new ZIP containing all seven source files was extracted to another clean directory and rebuilt **both PDFs**. For **each of all 17 pages in both paths**, original and rebuilt text, media/visible dimensions, rotation and rendered 108-dpi pixels are identical. Temporary ZIP, extracted copies and build outputs were deleted by the verifier. `qa-checks.json` contains per-page pixel hashes and both rebuild outcomes. Build intermediates are kept out of delivered `src/` by `build.sh`'s temporary directory.

## Remaining limits and next stage

No digital or mathematical blocker remains for this revision. **Unperformed:** physical printing/scale measurement, strip seam assembly and flatness, adult-held scissors and small R3-half handling, fixed-observer rehearsal with the non-mathematician adult, material/tray footprint, five-pair setup/reset, staffing, timing, and classroom piloting. A measured child cut is an approximation; exact mathematical equality is the theorem's hypothesis. The later separate guide must carry these limits, the exact-third readiness continuation and the honest boundary that this packet demonstrates the three-person fairness distinction rather than a naive cut-three/choose failure or full trimming algorithm. Student-page review/approval and independent guide authoring/review precede release. No remote copy is claimed current.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
