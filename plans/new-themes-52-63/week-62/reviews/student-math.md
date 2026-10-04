# Week 62 independent mathematics review

Reviewed October 4, 2026. Scope: every problem and every diagram in the actual nine-page `draft/students.pdf`, under `plans/new-themes-52-63/STAGE-ROUTING.md`. All nine pages were independently rendered and visually inspected; all 18 full-size graphs were extracted from the actual PDF vectors and independently enumerated. No draft files were edited. Complete solutions, universal arguments, alternate counting conventions and check data are in `math-audit.md`, `math-assets/independent_check.py` and `math-assets/independent-results.json`. The writer's verification/data were not used as evidence. The adversarial report was read only after the independent computations.

## Located issues

### 1. Grades 4–5 / PDF page 4 / shared definition before Problem 4

**Quoted text:** “A cycle follows conflict lines back to its start, without repeating any other circle.”

**Evidence:** W–X–W along the single edge WX returns to the start and repeats no *other* circle. The literal definition therefore admits an out-and-back walk as a cycle of a simple graph. It also does not explicitly prevent the starting circle being revisited midway. The worked square is a proper cycle but does not exclude those readings. The odd-cycle criterion in Problem 5 should use simple cycles of at least three distinct vertices.

**Smallest fix:** “A cycle follows conflict lines through at least three different circles and back to its start. Only the start repeats, at the end.” Retain the square input/intermediate/output visual. No task graph or numerical answer changes.

### 2. Grades 4–5 / PDF page 6 / Problem 6, both diagrams

**Quoted task/diagram:** “Add the fewest conflict lines you can so each network can no longer fit in two slots. Join only different circles that have no line yet.” Both layouts place A, B, C at (−4,2), (0,2), (4,2), and D, E, F at (−4,−2), (0,−2), (4,−2) cm.

**Evidence:** On the upper tree, independently enumerated one-edge answers are AC, AE, CE, BD, BF and DF. A straight AC segment passes exactly through B and retraces the printed AB/BC conflict lines; a straight DF segment passes exactly through E. These legal new endpoint pairs cannot be drawn as clear ordinary straight edges on that layout. On the lower empty graph the minimum is three edges forming a triangle; 8 of the 20 possible triangles use AC or DF and have the same obstruction. The “line crossings add none” rule concerns unmarked crossings and does not resolve a line going through an existing marked activity. Other legal solutions are drawable, so the numerical minima 1 and 3 are still correct.

**Smallest fix:** stagger or relayout the six sites in both diagrams while preserving labels, 20 mm diameter and the existing five edges. Check every possible added segment against every nonendpoint **disk**, not just collinearity of center triples. Explicitly allowing curves that avoid other circles is an alternative small fix. Do not direct children to one particular answer.

### 3. Grades 4–5 / PDF page 7 / Problem 7 and shared first-fit rule

**Quoted text:** shared rule “Do not move a placed card”; Problem 7 “Find orders that make the rule use as few slots and as many slots as possible on this network. Could moving placed cards improve either result?”

**Evidence:** Exhausting all 24 path orders gives a first-fit minimum of 2 and maximum of 3. Order A,D,B,C gives A1,D1,B2,C3. If “improve” means reduce used slots, legal moves D:1→2 then C:3→1 reduce this to two; the minimum cannot improve because AB requires two. But if “improve” refers to the explicitly stated maximum objective, moving A:1→4 gives a valid four-slot assignment and increases the maximum. Thus different readings give different objectives/answers. In addition, the shared no-moving restriction is not explicitly released for the repair phase.

**Smallest fix:** replace the final question with “After an order is finished, you may move cards. Can you use fewer slots?” Keep first-fit mandatory and forbid moves only while performing the ordered trial. Keep the two blank path records and leave orders/repair methods for children to discover.

## Band coverage

**Grades 2–5 / pages 1–3 / Problems 1–3:** every problem and diagram checks out mathematically. Minimum slots: 2,2; 3,4,2; 3,2. The page 3 maximum clique sizes are 2 and 2; the odd five-cycle correctly shows that the clique bound can be strict. Legal constructions and matching lower bounds were independently verified. No located mathematical issue in this band.

**Grades 4–5 / pages 4–9 / Problems 4–9:** all graphs, minimum schedules, odd-cycle certificates, component/isolate edge cases, universal two-colorability explanation, added-edge minima, first-fit extrema and named counts check out except for the three localized wording/geometry issues above. The eight-vertex first-fit tree has 12,810 two-slot, 26,880 three-slot and 630 four-slot orders among all 40,320; no order uses five. Named counts on page 9 are 24/108 for the path and 6/48 for the diamond. Empty slots and different slot names are correctly specified. The worked schedule/count examples are mathematically correct.

**K–1:** no separate packet exists or is required under the authorized routing; no K–1 coverage claim is made. Physical rehearsal, classroom piloting and final revised-output checks remain unperformed by this draft mathematics review.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
