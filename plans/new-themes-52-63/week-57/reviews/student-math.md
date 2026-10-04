# Week 57 independent mathematics review

October 4, 2026. Fresh math-review stage only; no draft, research, prior packet, guide or workflow prompt was edited. Reviewed the actual ten-page `draft/students.pdf`, every authored source file, the research notes and `review.md`, under the combined-packet routing. Pages 1–6 are Grades 3–5; pages 7–10 are Grades 4–5. There is no separate K–1 or 2–3 packet to certify.

**The supplied student polygons, counts, geometric areas, construction tasks, seam identities and hole formula are correct. A genuine gap in the adult general-triangle proof needs correction before release.** Preserve the theorem and upper investigations. The critic's three targeted student corrections are independently supported below.

Full problem-by-problem outcomes, exact constructions, a corrected noncircular general proof, and measured PDF geometry are in [math-qa/review-evidence.md](../../../../tmp/worksheet-runs/week-57-new-v1/math-qa/review-evidence.md). The fresh executable [math-qa/independent_check.py](../../../../tmp/worksheet-runs/week-57-new-v1/math-qa/independent_check.py) produced [math-qa/independent-evidence.json](../../../../tmp/worksheet-runs/week-57-new-v1/math-qa/independent-evidence.json). It imports no author checker or classifier. Areas come from exact horizontal-strip integration and independent triangle base/height areas; point membership comes from ear-triangle unions. All ten pages were freshly rendered and visually inspected, with delivered-vector measurements of every outline, seam and dot board.

## 1. Necessary mathematical correction: the general bounding-rectangle shortcut does not cover every triangle

**Band/page/problem:** Grades 4–5, p. 8/P8, supporting general proof rather than an incorrect student test figure. P8 asks: “Find an explanation that Pick's rule works for every allowed polygon.”

**Exact affected passages:**

- `plans/new-themes-52-63/week-57/research-notes.md`, line 17: “Any lattice triangle fits in its minimal axis-parallel bounding rectangle; the complementary pieces are axis-parallel right triangles (at most three), so subtract their known Q values to prove it for the triangle.”
- `draft/src/README.md`, mathematical-facts paragraph, line 35: “An arbitrary lattice triangle lies inside an axis-aligned rectangle, with axis-aligned right triangles outside it; subtraction proves its rule.” This abbreviated account inherits the unsupported general step and does not supply an order of legal one-side joins for the missing case.
- The current outline, kernel 2, and its historical copy in `PROMPT.md` say: “Enclose a general lattice triangle in its axis-parallel bounding rectangle and subtract the right triangles outside it.” They identify the same proof route; the review is the correction record, not a reason to regenerate or edit the workflow prompts.

**Counterexample/evidence:** take `A=(0,0), B=(2,1), C=(6,6)`. It is a simple nondegenerate lattice triangle of area 3, with `I=0, B=8`, but its vertex `(2,1)` is strictly inside its minimal 6-by-6 rectangle. The complement has an upper-left right triangle and a lower-right quadrilateral, rather than the claimed three right-triangle pieces. The natural axis-right pieces have areas 18, 1 and 10 and leave the rectangle `(2,0),(6,0),(6,1),(2,1)` of area 4. Subtracting only those three areas from 36 gives 7 instead of 3. Filling this missing rectangle with more pieces also requires a careful count argument at the now-interior vertex; the stated one-full-side additivity proof cannot simply be invoked for an arbitrary cyclic decomposition.

The supplied P8 triangle happens to have all three vertices on its bounding rectangle, so its `12−2−3−3/2=11/2` certificate passes. Checking that example does not establish the universal claim.

**Smallest complete fix:** replace the general-triangle step in current research/source notes and the later guide with the two-diagonal argument recorded in `math-qa/review-evidence.md`: first establish triangles having a horizontal or vertical side by rectangle subtraction; then complete a general triangle to a lattice quadrilateral using a horizontal/vertical projection on the opposite side of its longest x-span edge. Its two legal diagonal cuts compare the target triangle with three already established axis-side triangles. No off-lattice cut, empty-triangle theorem, or unstated extension of seam additivity is needed. Exact tests cover all 2,148 noncollinear triples on a 5-by-5-dot board, including 548 instances needing this bridge. P8 remains a sound open investigation.

## 2. Supported critic correction: allow copies in the independent P2 area check

**Band/page/problem:** Grades 3–5, p. 2/P2.

**Exact text:** “Check area with pieces or a cut.”

**Evidence:** the supplied triangle is `(0,0),(4,0),(1,3)`, with exact area 6. Its left edge has slope 3. A finite union of the supplied uncut unit squares and diagonal half-square triangles has boundary segments only horizontal, vertical, or of slope ±1, so those pieces cannot tile this whole triangle without cutting. A second congruent copy forms a parallelogram of base 4 and height 3, area 12; one copy therefore has area 6. Copies are demonstrated on p. 1 and allowed by P1 and P3. The current P2 restriction is feasible with scissors but unnecessarily excludes the practiced exact method.

**Smallest fix:** “Check area with pieces, cuts or copies.” Preserve a duplicate or the recoverable original when cutting. No polygon redesign is necessary for this correction.

## 3. Supported critic correction: provide an odd-B, half-integer contrast in the concrete core

**Band/page/problem:** Grades 3–5, pp. 1–5/P1–P5, particularly P2 before the conjecture in P4 and formula in P5.

**Exact diagrams/counts:** p. 1's non-task triangle has area 1; the count model on p. 2 has `(I,B,A)=(1,8,4)`. P1 areas are 6 and 6. P2's records are `(0,12,5)` and `(3,8,6)`; P3 forces `(2,6,4)` for both constructions. Every supplied pre-formula B is even. The first fixed odd-B figure is p. 8's triangle `(5,3,11/2)`.

**Evidence:** none of the supplied concrete records shows a nonintegral exact area or tests “half of B” on an odd B. A child could choose such a case in P4, but the packet does not ensure it. This is a contrast/coverage correction, not a false theorem.

**Smallest mathematical addition/replacement:** under an existing core problem, a nonempty triangle such as `(0,0),(3,0),(1,3)` has `I=3, B=5, A=9/2`. The direct inside dots are `(1,1),(1,2),(2,1)`; its boundary comprises four base dots and the top vertex, with no intermediate dot on either primitive sloping edge. Two congruent copies have parallelogram area `3×3=9`. It fits the existing 5-by-5-dot board and retains intermediate side dots. The reviser can choose a different independently checked contrast; do not turn this into a repeated empty-triangle catalog. Render and inspect whichever final figure is used.

## 4. Supported critic correction: give separated-loop conditions before P9's first child-built hole

**Band/page/problem:** Grades 4–5, p. 9/P9; first explicit loop-separation sentence currently appears at p. 10/P10.

**Exact text:** P9 says “Count dots on either outline in B” and “Test your change on another shape with one hole.” P10 then says “Keep every boundary loop separate, with straight sides and corners on dots.”

**Evidence:** the target square ring is legal and has `I=0, B=24, A=12`. The `+1` correction assumes a hole strictly inside the outer polygon, with disjoint simple boundary loops. P9 has already relaxed p. 1's “one closed outline” when it requests a new hole construction; its needed second-loop conditions should not first appear in the following problem. The global no-touch rule and target figure provide substantial protection, so this is a small first-use clarification, not a demonstrated wrong target answer.

**Smallest fix:** at P9's first hole permission, say briefly that the hole stays inside and its outline stays separate from the outer outline, and use “both outlines” in the B convention. P10 may refer to the now-shared hole rules. Keep the `+1` discovery and any-number-of-holes extension.

## Coverage and limits

Grades 3–5 pp. 1–6 and Grades 4–5 pp. 7–10 otherwise check out mathematically. All 17 fixed definitions are simple, nondegenerate lattice polygons with the declared side counts; the one ring has a separate four-sided hole. P3 constructions exist; all six P5 records have actual-board witnesses; both P6 seam endpoint sets and category changes match the formulas; P9's narrow board and P10's full board hold legal one-/two-hole tests. Every fixed outline and blank board in the actual PDF has equal measured x/y spacing within 0.0003 mm of 20 mm, with all 509 dot centers checked and visible in the renders. Convention markers, grades, page/problem numbering and record labels agree with the mathematics.

This stage did not alter or rebuild the draft, nor certify a later revision. Clean-copy and ZIP rebuilds were already checked by the critic; this independent stage did not repeat that unchanged check. Final revised pages still require their own complete geometry/render/rebuild pass. Physical printing, material fit, cutting/handling, classroom timing and piloting remain **unperformed**. No prior Week 31 packet or remote file was edited or certified.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
