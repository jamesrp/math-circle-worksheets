# Week 61 fresh adversarial student-packet review

Reviewed October 4, 2026. Reviewer stage only: the draft, source and writer evidence are unchanged. This report is not the independent mathematical review, a facilitator guide, a physical rehearsal or a classroom pilot.

## Verdict

**Revise the upper covering work before release.** The route/corner entry is substantial and preserves children's construction choices. Pages 1–4 give three useful kinds of concrete work before area bookkeeping. The principal problems are on pages 5–6: the projected region map is harder to recover than its eight-entry table suggests, the first covering count lacks a worked recording convention, and the general area task leaps from one highly symmetric coverage example to three numerical records without a checkable non-octant coverage investigation.

Keep the lune argument and universal area explanation. These findings support a clearer concrete bridge and honest readiness gates, not deleting the upper mathematics or manufacturing K–1 coverage. None is evidence of a failed sphere lesson: the packet is unpiloted, and age-fit concerns below are operational hypotheses.

## Evidence actually inspected

- Read `AGENTS.md`, root `README.md`, `REPUBLISHING.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, this run's `PROMPT.md` and `CRITIC.md`.
- Read the actual six-page `draft/students.pdf`, `draft/src/students.tex`, `geometry.py`, `verify_math.py`, `README.md`, `source-notes.md`, the research notes, research checks and writer-stage evidence.
- Independently rendered all six pages from the actual combined PDF at 108 dpi into `critic-qa/page-01.png` through `page-06.png`, and inspected every page. Text extraction is in `critic-qa/student-text.txt`. All six headers, their actual bands, the consistent footer, sequential problem numbers and Letter dimensions are present. No text overlap or clipping was found. The circular silhouettes use equal axis scaling.
- Consulted the actual local primary reference: Petrunin and Zamora Barrera, *What Is Differential Geometry? Curves and Surfaces*, v7, Observation 2.22 (pp. 24–25), §14B (p. 119) and Lemma A.17 (p. 178). The lune theorem and antipodal exception are established mathematics with the intended limits.
- Checked the cited teaching passages directly: *Math Circle by the Bay*, printed pp. viii–x; Rozhkovskaya, Lessons 3, 7 and 8, “At the lesson”; and the year-one *Pattern Block Exercises – Google Docs*, PDF p. 1. They support handling materials, independent attempts, flexible depth and light records. They do not establish age fit for this sphere adaptation. The atlas octant/lune precedent is correctly credited as prior library mathematics.
- `critic-qa/checks.json` records the scalar fraction checks and a separate octant visibility/count check described below. This is a critic check, not a substitute for the assigned independent math stage.

## High-priority revisions

### 1. Page 5: make the eight-region map recoverable in both views

**Evidence:** The front picture labels 1, 2, 3 and 5; the back labels 4, 6, 7 and 8. Both views use an oblique camera looking toward the center of the target octant. Each visible hemisphere actually intersects seven of the eight spherical cells, rather than four. Thus the front also contains small, unlabelled visible portions of regions 4, 6 and 7; the back contains unlabelled visible portions of 2, 3 and 5. The dashed hidden arcs add further projected subdivisions that are not boundaries on the visible surface. `geometry.py` labels only cells whose chosen centers face the camera, not every cell with a visible part. This is confirmed for the octant independently in `critic-qa/checks.json`.

**Consequence:** A child shading or marking the supplied pictures must mentally join the unlabelled pieces to regions on the other view, while distinguishing hidden arcs from visible boundaries. The single eight-entry tally is a good intended record, but this map currently makes the state harder to externalize. An adult can reconstruct it; that is not evidence that the child retains the covering decisions.

**Expected revision:** Either choose a view whose visible hemisphere has four complete octants, or identify every visible part with the same region ID across both views, using close labels/callouts where needed. State briefly that both pictures show the same ball. Retain one record row rather than requiring two separate tallies. Check actual rendered views after changing the camera; a coordinate check alone does not settle legibility.

### 2. Page 5: demonstrate one pair-to-count record before asking for the three-pair tally

**Evidence:** The worked example shows the finished pair at A on an 80° triangle, with the same blue shading on front and back. All three full circles use the same line style. It does not explicitly identify the two side circles that determine the pair at A, or show a meaningful intermediate between selecting those circles and shading the opposite lunes. The table “Pairs covering it” first appears in Problem 5 with no example of what a count entry means.

**Consequence:** The new representation combines several unfamiliar choices: arbitrary corner-poles replacing the fixed N/S lune, selecting the two circles at that corner, selecting opposite lunes, and treating coverage as a multiplicity rather than shaded area. A student can mistake “pair” for two contributions in the same region, or count coloured boundaries instead of pair memberships. These are plausible interpretation failures, not observed classroom errors.

**Expected revision:** Use the existing non-task 80° example to show input triangle/corner, the two relevant full circles as a meaningful intermediate, and the selected pair. Include one marked sample region/patch and its matching single-pair count entry; leave the main eight-region, three-pair enumeration unsolved. A short essential rule identifying the two sides meeting at the chosen corner is appropriate. The result should still leave children choosing the remaining pairs and counting their overlaps.

**Acceptance check:** After a normal launch, a child should be able to point to a region, name the pairs currently marking it, and recover its single count from the model or page without an adult performing the whole investigation. This does not require printing a complete counting procedure.

### 3. Page 6: supply concrete non-octant coverage work before the universal explanation

**Evidence:** Problem 5 supplies one coverage investigation, on eight equal octants. Page 6 then asks children to use the six lunes for the 60°/60°/90°, 80°/80°/80° and 100°/100°/100° records, find a rule and explain it for every allowed triangle. Its three diagrams show only the triangle boundaries; none shows the extended circles, antipodal triangle or cells to mark. The material notes specify calibrated meridians and the octant model, but do not supply physical exact models for those three non-meridian triangles. The 80° full-circle example on page 5 is presently only a finished single-pair example, not a second coverage investigation.

**Consequence:** Equal octants can make the count and area seem to follow from “eight equal pieces.” The three later angle records are purposeful arithmetic contrasts, but do not by themselves let children test whether the one/three coverage pattern survives unequal cells. Children would need to reconstruct a new sphere model from the records, mentally extend the sketches, or receive the general invariant from the adult. That is a larger prerequisite than the current source table's angle sums and fraction work suggest. Fitting a rule to these records is also not an explanation for every triangle.

**Expected revision:** Reuse the existing 80° full-circle geometry as a genuine second covering investigation with a recoverable pair record, or supply a similarly usable non-octant layer board/physical model. Let children check the coverage on unequal regions before the universal explanation. Keep the three exact records as applications and contrasts; they need not all become exact physical construction exercises. Retain the general argument as a readiness-dependent continuation or second visit, with concrete coverage work available alongside it. Update the source prerequisites to include understanding overlapping counted area and the distinction between checking several cases and explaining the invariant.

**Acceptance check:** The route to the formula must have a checkable reason that the target triangle and its antipodal copy receive three coverings, the other six regions one, and the two target regions have equal area. The guide may hold discretionary proof prompts and algebra. The student representation must support the required actions without giving the finished theorem as a procedure.

## Smaller precision and operational points

1. **Page 3, meridian convention:** “A meridian goes from N to the opposite pole” describes endpoints but does not explicitly state that it is a great-circle semicircle. Its claimed right angle with the equator depends on that fact, not merely on its endpoints. Tighten this definition in place; no additional problem is needed. Page 4 already uses the precise great-circle wording for a lune.

2. **Page 2, nondegeneracy:** The student rules correctly require distinct corners, no antipodal pair, shorter great-circle sides, the smaller convex region and strict containment in some hemisphere. They do not explicitly say that the triangle encloses positive surface area. An ordinary collinear triple is effectively excluded by the less-than-180° corner requirement, so this is not a demonstrated counterexample to the current rules. Still, a short concrete positive-area condition would make the intended nondegenerate scope explicit and agree with the source notes. Do not add a long formal definition block.

3. **Physical preparation remains a real gate:** The ordinary launch must demonstrate surface contact with fixed endpoints, three retained sides of one triangle, and comparing tangent directions with the narrow paper corner. With only two strings, the third side needs a recoverable washable mark or another retained arc; the later guide should make that kit operation explicit. Exact opposite markers, marked 45°/72°/120° meridians and region/pair handling require the already-disclosed physical pretest. This report did not perform it. The supplied source honestly marks the pretest and pilot unperformed; preserve that status.

4. **Entry reading:** Pages 1–3 require no arithmetic sums, but page 2 has adult-read technical words and hemisphere constraints. Grades 2–5 is an honest approximate supported band if the launch shows legal shapes and the adult checks the scope while children choose their vertices/routes. Do not equate an adult reading or steadying the ball with an adult doing the mathematics. Confirm this distinction during the first pilot rather than treating the grade header as validated.

## What is already sufficient and should be preserved

| Page | Actual student evidence | Review result |
| --- | --- | --- |
| 1, Grades 2–5 | Fixed surface endpoints, non-task points → great circle → shorter arc visual; chosen close/far/opposite pairs; three route records. | Clear concrete action and meaningful antipodal contrast. Do not require a formal uniqueness proof at entry. Physical shortest-route experiments need the adult distinction between an ideal theorem and measurements. |
| 2, Grades 2–5 | Local surface corner → matching directions → 135° record; open search for a three-right-angle triangle; large drawing area. | Meaningful corner convention precedes use. The maximal-right-corners question leaves a substantial construction choice. A narrow paper corner supplies an experimental check, not exact universal proof. |
| 3, Grades 2–5 | Fixed pole, variable equator endpoints, smaller/equal/larger-than-right corner cases and surface-coverage comparison. | Three contrasting constructions give enough work before fractions. Keep the independently chosen endpoint positions; clarify only the meridian definition. |
| 4, Grades 3–5 | Non-task 40° lune → nine equal angular sectors → 1/9 surface record; three new physical meridian-gap triangles. | The unfamiliar degrees-to-surface-fraction convention has a real input/intermediate/output example. Inferring the triangular northern half can remain the mathematical task; do not print all its answers or turn it into tiny steps. |
| 5, Grades 4–5 | Full great circles, opposite points and eight-region tally. | Worth keeping as substantial work, possibly on a separate visit. Repair the map and first-use count convention. |
| 6, Grades 4–5 | Three exact non-octant angle records, fraction blanks, substantial explanation space. | Serious destination and useful contrasts. Needs a recoverable non-octant coverage bridge and honest continuation gates. |

## Mathematical spot-check and scope result

The credited lune relation gives whole-sphere fraction θ/360; the fixed-pole/equator triangle is half that lune. The 40° example is 1/9. Problem 4's fractions are 1/16, 1/10 and 1/6. For the ideal triangles in Problem 6, excess/720 gives 1/24, 1/12 and 1/6. For the octant arrangement the pair memberships are `[3,1,1,1,1,1,1,3]`; the corresponding counted area is 3/2 spheres and the target octant is 1/8. These values are consistent with the text and research.

No numerical answer error was found in this critic pass. The separate mathematical reviewer should still independently check the realizability and precise coordinates of every displayed triangle, all hidden/visible arc and shading boundaries, and the six-lune argument under the stated minor-arc, positive-area, convex/open-hemisphere assumptions. The antipodal exception on page 1 is intentional; antipodal *triangle* side endpoints remain excluded. Complete meridian semicircles and lune pole pairs are a different construction. The complementary region and latitude-edged shapes must remain outside the triangle formula's scope.

The source's prior-library and source-adaptation limits are appropriately explicit. Digital geometry checks, portable writer rebuild checks and these rendered-page observations do not establish physical readiness, successful classroom use or independent child control.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
