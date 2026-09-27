# Review of the ten-entry worksheet trial

September 25, 2026. This record concerns the ten new worksheet investigations, not a re-review of all 90 atlas cards.

## Scope and independent review

Three authors worked on disjoint groups, then exchanged mathematical/design reviews before final page production:

- Geometry author: GA-26, GA-29, GA-25. Independently reviewed by the systems author in [systems-review-of-geometry.md](systems-review-of-geometry.md).
- Systems author: GA-11, AP-26, AP-07. Independently reviewed by the decisions author in [decisions-review-of-systems.md](decisions-review-of-systems.md).
- Decisions author: AP-23, AP-21, AP-01, AP-29. Independently reviewed by the geometry author in [geometry-review-of-decisions.md](geometry-review-of-decisions.md).

The editor inspected the current Week 1 reference sheets, rechecked the investigation arcs and prerequisite gates, and reviewed the new student and guide layouts. The [design brief](DESIGN-BRIEF.md) records the source-supported teaching lessons and editorial choices separately.

## Mathematical evidence

All four exact check programs pass:

- [Geometry author checks](geometry-checks.py) and [results](geometry-checks-results.json): knot colorings and local moves, Cantor endpoints/addresses/lengths, grid trees, shortest swaps and complementary region graphs.
- [Independent geometry checker](systems-review-geometry-checks.py) and [results](systems-review-geometry-checks-results.json): independently reconstructs all 4,096 grid-edge subsets and 192 spanning trees, and all 162 valid signed R3 coloring cases.
- [Systems checks](systems-checks.py) and [results](systems-checks-results.json): additive-machine examples, exact feedback trajectories and transformation identities, and the cooling accuracy threshold with rational bounds for the exponential comparison.
- [Decisions checks](decisions-checks.py) and [results](decisions-checks-results.json): congestion states and cycles, all 32 battery subsets and suffix states, exact hitting/time equations, and prefix-code costs/classification.

The authors' and reviewers' written general arguments matter as well. Finite tests alone do not prove the general tree theorem, a recurrence identity for arbitrary real starts, uniqueness of harmonic prices, the infinite Cantor claim or knot equivalence. The guide supplies the appropriate arguments and explicitly identifies facts that students are allowed to use.

The data have 45 geometry, 32 systems and 36 decisions prompt IDs, each with a nonempty solution; there are no missing, extra or duplicate solution IDs within a family. IDs are keyed by **family plus prompt**, since GA-29 and AP-29 both use numbers beginning `29.`. Two geometry follow-ups, 25.15 and 29.11, are facilitator-only extensions; a few introductory actions are incorporated into rule cards or combined prompts. These counts describe the planning/key records, not 113 separately numbered printed exercises.

The editor reproduced the exact random draw from the saved seed and confirmed that all three original atlas family-file hashes still match `sample.json`. The trial did not alter or replace the original cards.

## Repairs arising from review

1. **Knot proof scope.** The pictured R3 move checks one representative. The guide now explains the six legitimate height orders, excludes cyclic ones and records the complete local calculation. The student explicitly receives the all-variants and Reidemeister facts. The source URL was repaired. Equal invariant values are not presented as a proof of equivalence.
2. **Random-walk rules.** Fair independent tosses and interior starting positions are explicit; a child cannot select the winning shore as a trivial guaranteed-win answer.
3. **Avoiding answer leaks.** The traffic page title no longer announces that the group gets hurt. The cooling minimum-update question no longer reveals the answer by naming the five-update lower bound in advance.
4. **Actual diagram use.** Maze-copying templates use faint reference roads so children can draw only their kept roads/walls. The water rule distinguishes those walls from reference marks. Knot crossings are drawn from checked strand data, with visible gaps. The worked region tree avoids an accidental visual crossing.
5. **Usable workspace.** The delayed-control period proof has a larger writing panel. The Cantor address argument gained space. The full battery dynamic-programming table stays out of the student sheet. Optional geometry follow-ups moved to the teaching key; some advanced explanations may continue on the back.
6. **Print editing.** Prose spacing was repaired without splitting mathematical strings. Guide headings stay with their first paragraph; systems prompts and their answers stay together. AP-21 distinguishes three take/skip boxes from the fourth box used to trace the chosen plan.

## PDF review

Maker records: [decisions](decisions-maker-review.md), [systems](systems-maker-qa.md), and [geometry](geometry-maker-qa.md). Independent full PDF reviews: [systems sheets](decisions-pdf-review-of-systems.md) and [decisions sheets](systems-pdf-review-of-decisions.md). The editor independently inspected all twelve geometry student pages at full size, all geometry guide contact sheets, and selected full-size worked figures and proof pages. The other two independent reviewers inspected all eleven systems and all twelve decisions student pages at full size, every guide page on contact sheets, and dense guide pages individually. Each checked actual PDF solution text against the keyed data.

A [final targeted cross-review](geometry-final-pdf-spot-review.md) passed the repaired maze templates and knot/region figures. The editor also re-inspected all changed geometry pages. Rebuilt pages were inspected under fresh filenames because the image viewer can retain a same-path earlier rendering. All actionable review findings are closed.

Final assembly is complete: **36 student-book pages and 44 guide pages**, including one contents page in each. All 80 pages were rendered; both books have zero blank pages, out-of-page characters or suspect glyphs. All twenty contents links resolve to the correct family starts. The editor visually inspected both final contents pages and verified that all **78 investigation/key page bodies exactly match the reviewed subset PDFs in character text, position and size**; assembly changed only the page numbers and ordering. This lets the full-size page reviews carry through to the combined files without claiming another redundant visual pass.

The [release manifest](release-manifest.json) records source/output hashes, page ranges, mechanical checks and the reviewed-page comparison. Page ranges are also in the trial README. Page-boundary and glyph checks are mechanical support, not substitutes for visual review.

## What remains unproved by this work

These are reviewed worksheet trials, not classroom-tested lessons. Time estimates, engagement and the amount of facilitation needed remain unmeasured. The sample is genuinely random but small and contains no AD family; it is not a statistical certificate for all of the atlas. The editor's first-pilot choices and conditional fits are in the [trial assessment](README.md). In particular, GA-11 retains algebra/irrational-number prerequisites, and AP-07 retains calculus.
