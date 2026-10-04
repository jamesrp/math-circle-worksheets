# Week 58 adversarial student/material review

Reviewed 4 October 2026. Critic stage only; the draft was not edited. Read `PROMPT.md`, `CRITIC.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, root `README.md` and `REPUBLISHING.md`, and the draft source/README. Direct routing correctly overrides the generic three-band/file target.

**Recommendation: revise the small operational issues below before release; retain this mathematical sequence and its upper depth.** The packet contains serious fair-division mathematics rather than equal-count sharing. I found no visibly clipped or overlapping student/material content, no changed preference values within a stated trial, and no comparison of different people's scores as a fairness test. This is an independent page/usability review, not the separately assigned exhaustive mathematical audit or classroom validation.

## Actual coverage and evidence

Independently opened `draft/students.pdf` (7 pages) and `draft/materials.pdf` (10 pages) with PyMuPDF, rendered all pages at 108 dpi, and visually inspected **each of the 17 full-page images**, not only extracted text or an author's contact sheet. Evidence is in `review-assets/students-01.png` through `students-07.png`, `materials-01.png` through `materials-10.png`, extracted text, and `geometry-and-spotcheck.json`. No final/revised packet was inspected.

| Student page | Actual task and review finding |
| --- | --- |
| 1, Grades 2–5 | Shared additive/whole-card/tie rules; original three-token input → division → choice/remainder visual before first use; R1,R2,R3,B1 physical division/choice with fixed A/B scales. Children decide the division and choice. Four compact A/B records are ample when actual cards are used in separate trays. A real substantial entry, with scope for role reversal and different successful labelled allocations. |
| 2, Grades 2–5 | All envy-free labelled allocations of R1,R2,B1,B2, followed by proportional checks. Six catalog slots can contain the five successful allocations. Independent critic enumeration also found exactly five: both reds to A/both blues to B, and the four labelled mixed splits. The final unkeyed score table needs clarification (issue 4). |
| 3, Grades 2–5 | Non-task panel worth 2 → equal 75 mm lengths → value 1 each visual correctly precedes density use. Both A-cutter and B-cutter trials are supplied. Sketches are intentionally smaller than the physical strips and explicitly called sketches. The required exact alternative-observer score table introduces thirds (issue 1). |
| 4, Grades 3–5 | Central cut-and-choose explanation, then an equal-length/unequal-value counterexample with both observers using the explicitly stipulated A scale. Universal explanation is the mathematical problem, so it belongs on the student page. Exact equality is stated as the assumption; generous writing space. |
| 5, Grades 2–5 | Three identical positive-value whole cards versus a declared splittable paper replacement. An object/count argument works without fraction notation. Two 86×56 mm record trays and explanation space suffice. The paper-copy replacement should be explicit (issue 2). |
| 6, Grades 3–5 | Fixed cyclic value rows (4,8,0), (0,4,8), (8,0,4); unchanged printed initial allocation A:X/B:Y/C:Z; both fairness checks before rearranging. This is a meaningful three-person counterexample followed by a child-owned repair, not sequential preference updating. The unkeyed score table can be tightened (issue 4). |
| 7, Grades 3–5 | General two-/three-person implication questions, complete allocation and additive values stated, one-observer tray pictures, substantial explanation space. Preserves the upper destination without giving an algorithm or importing trimming. Do not replace this with more routine trials. |

| Material page(s) | Actual contents inspected |
| --- | --- |
| 1 | Twelve labelled 25×25 mm reusable goods plus a separate 25×25 mm paper R3; 100 mm bar. Seven reusable goods have no task use (issue 3). |
| 2 | Two 100×150 mm A/B cards. Red/blue values match student pages 1–3 exactly; numeral/dot scales and shapes are legible. The unused green row adds inventory with no problem. |
| 3 | Two 100×150 mm U/V cards. Each red value is 1; unused types are zero. Correct for Problem 5; two observer cards are useful even though their values agree. |
| 4 | Two 100×150 mm upper A/B observer cards, X/Y/Z rows and readable 4/8/0 dot groups. Match page 6 exactly. |
| 5 | One 100×150 mm C card plus one X, Y and Z panel, each 50×40 mm. Match page 6 exactly. |
| 6 | Strip 1 red/blue halves and strip 2 red/blue halves; all four 150×40 mm, correctly paired labels, assembly instruction and 100 mm bar. |
| 7 | Same verified geometry and usable labels for strips 3 and 4. |
| 8 | Same verified geometry and usable labels for strips 5 and 6. |
| 9 | Same verified geometry and usable labels for strips 7 and 8. |
| 10 | Same verified geometry and usable labels for strips 9 and 10. |

Vector spot-checks confirm US Letter dimensions, landscape material pages 2–5, all 13 current small-card borders at 25 mm, all seven large preference borders at 100×150 mm, three panels at 50×40 mm, and twenty strip halves at 150×40 mm. Each of the ten material pages has a digitally 100 mm check line (TeX/PDF rounding under 0.001 mm). Matching halves make **ten** 300×40 mm strips only after the prescribed edge-to-edge, no-overlap join. There is no attempt to shrink a 300 mm strip onto Letter. Digital dimensions do not establish printer scale or a successful taped seam.

## Located issues and minimum fixes

### 1. Required exact thirds conflict with the declared concrete entry prerequisite

**Priority: high; students p. 3, Problem 3 and its four-row score table; `draft/src/README.md`, page-3 prerequisites.** A cutter's correct red-region cut is 100 mm from the left. The other observer values those pieces 2/3 and 10/3. The role-reversed case also requires thirds. The student problem requires finding how *each* person values *both* pieces, and the table makes those exact scores look mandatory. Yet the README says exact fractional scoring is not a younger entry prerequisite and may be adult-recorded. This differs materially from merely reading the text aloud: the adult could end up doing the required new arithmetic while the children wait.

Minimum fix: keep the physical cut/choice investigation and its differing-value mathematical substance. Make the main printed result the cut location and chosen piece, with exact alternative-observer fraction calculation reserved for the adult/readiness-dependent continuation; alternatively explicitly gate this page's complete numerical task on fractions/thirds in the prerequisites and supply a child-owned concrete route for those who do not meet that gate. Do not print the 100 mm answer or a procedure for discovering it. The first-use half-panel visual is good and should stay.

This is a documented mismatch in the required task versus prerequisites. How strongly it affects the actual third graders is an unpiloted hypothesis, not a reason to ban fractional or upper work.

### 2. Say that paper R3 replaces the whole R3

**Priority: medium; students p. 5, second trial; materials p. 1.** The kit contains both a reusable R3 and a visually identical separate paper R3. “You may cut the paper copy of R3” does not explicitly say to remove the original R3. A literal material-handling interpretation could create four cards' total value and a different problem.

Minimum fix: change the essential second-trial wording to make replacement explicit, for example “Replace R3 with its paper copy; you may cut that copy.” Retain the stated whole-square value 1 and equal-area convention. In adult preparation, remove the reusable R3 from that trial. No new example or longer scaffold is needed.

### 3. Trim unused inventory and state a whole-group print recipe

**Priority: medium; materials pp. 1–3; `draft/src/README.md`, material dimensions/scope.** Every actual card task uses only R1,R2,R3,B1,B2. R4,B3,B4,G1,G2,G3,G4 are unused, as the README partly acknowledges. The third-type preference rows are also unused. The outline's dozen was a material limit, not a demand for unused cutouts. Keeping these adds cutting, sorting and preference-card reading without adding a mathematical contrast.

Minimum fix: supply the five reusable goods actually needed plus the one separate paper R3; remove unused type rows from the A/B and U/V cards while retaining the required large usable card sizes. Do not pad the kit by inventing an extra green task solely to justify inventory.

Also add an exact page/copy recipe in source/adult preparation: five pair kits, one additional three-person kit, separately supplied trays/rulers, and which material pages are repeated. Calling the entire ten-page PDF a “pair kit” can cause all upper cards/panels to be printed five times although the outline requests one additional upper kit. The full-group counts should distinguish sturdy reusable R3s from paper replacements.

The twenty strip halves really do produce ten full strips. Ten strips per pair are explicitly authorized in the outline and are defensible consumable stock for repeated physical attempts; their five labelled assembly pages are not an accidental duplicated output. State whether ten are the recommended stock or whether a shorter first-route print subset suffices, without falsely calling twenty halves twenty strips. Keep the matching-number and no-overlap assembly instructions.

### 4. Bind a score table to one recoverable reference allocation

**Priority: low-to-medium; students p. 2 bottom table and p. 6 bottom table.** Page 2 catalogs several allocations but has one two-row score table with no allocation identifier. Page 6 asks for initial checks and then a rearrangement but its table does not distinguish the two states; both alternative columns say “Other tray.” The printed initial diagram is unchanged and the prose orders the checks correctly, so I am not claiming the packet currently prescribes sequential updating. The unresolved bookkeeping question is what state a completed numerical row records.

Minimum fix: either remove these supplementary numerical tables and retain the allocation records, or briefly tie each table to one saved allocation. For page 6, label tray-owner columns A/B/C and explicitly make the record refer to the initial allocation. For page 2, a tiny matching record number suffices if the table is kept. Give discretionary repeated scoring to the adult rather than requiring a second ledger for every catalog entry. These should remain checks the child can perform on visible trays; do not make the adult operate the investigation.

## Preserve, prerequisites, and adult-only boundaries

* Keep the non-task input/intermediate/output visuals. They demonstrate the unfamiliar turn convention and partial-panel valuation without revealing the target cut or full catalog.
* Keep fixed personal values, complete allocation, ties, whole-versus-splittable distinction, and the same observer evaluating each candidate tray. The current score rows never compare A's own score with B's own score.
* The supplied contrasting instances are purposeful: unequal color counts, the complete four-card catalog, role-reversed density cuts, equal-length failure, indivisibility, and a three-person proportional-but-envious allocation. Seven pages need not become four pages for every band. The two-/three-person implication proof is central upper work, not an automatic explanation appended to every small action.
* The optional oral younger entry is honest. A younger child can divide and choose, with an adult reading; no printed K–1 label or arithmetic guarantee should be manufactured. The present written catalog/general arguments are not an independent K–1 route.
* Source notes accurately distinguish nonnegative additive preferences, exact mathematical equality from approximate physical cuts, and nonatomic divisibility. The future adult overview must explicitly map those assumptions and destinations to the tasks before solutions. It must also state that the two-person guarantee does not automatically extend to three sequential choosers, and that whole-card impossibility is not impossibility for divisible cake. The current student packet establishes the three-person fairness distinction; it does **not** itself demonstrate a three-person cut-three/choose failure or teach the full trimming procedure. Keep that boundary honest; no full algorithm is required here.

For teaching evidence, independently reread Rozhkovskaya's *Math Circles for Elementary School Students*, Lesson 1 “At the lesson” (`OEBPS/part0011.xhtml`) and Lesson 6 “At the lesson” (`part0016.xhtml`) in the downloaded EPUB. Those accounts actually report slower/harder crossing work than planned and additional concrete cutting examples needed before the one-extra-piece argument convinced children. Lesson 6 also describes a useful table for a logic problem. My inference is to preserve substantial physical trials and use one clear recoverable record; those accounts do not justify banning all tables or certify this adaptation.

## Unperformed physical/classroom pretests

No printing, scissors rehearsal, taped assembly or classroom trial was performed in this review. Before calling the kit physically ready, rehearse:

1. Actual-size printing of both portrait and landscape material pages; measure the 100 mm bars, 25 mm card edges and 150 mm half lengths. Check printer orientation/scaling does not alter them.
2. Assemble at least one labelled 300×40 mm strip with a true butt seam and tape only on the back. Confirm no overlap/gap, red/blue order, flat handling, and a 100 mm/200 mm cut crossing only the intended panel.
3. Child chooses/marks the cut while the adult handles scissors; test the 25 mm paper R3 replacement and retention of small halves. Remove the original R3 so only total value 3 remains.
4. Rehearse with the non-mathematician adult that a fixed A or B card evaluates both unchanged trays, children control division and choice, role reversal does not silently change a person's preferences, and the upper referee is not a third recipient in two-person trials.
5. Test the large preference-card/two-tray table footprint, setup/reset of five pairs and one upper kit, cutting delays, and a manageable 35–40 minute route. Keep exact fraction records and universal explanation readiness-dependent. Verify children retain the decisions after a normal short launch rather than needing adults to carry the investigation.

Until these and actual use occur, material fit, fixed-observer understanding, timing, age fit and piloting remain untested. The rendered packet supports a promising concrete route; that is a design judgment, not observed classroom evidence.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
