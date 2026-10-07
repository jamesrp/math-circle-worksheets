# Adversarial review: Week 73, The gentlest stretch

## Verdict

**Mathematics passes; retain this four-page Grades 4–5 prototype, with small revisions to the experimental wording and explicit adult handling of measurement.** No release-blocking diagram or arithmetic error was found. The substantive progression is sound: a finite set of pins fails to reveal a bad map, midpoint probes expose it, then a whole-sheet rule and a universal lower bound address the actual question. Do not replace that progression with a lecture or publish an empirical ruler result as an exact certificate.

This is an independent critic-stage review, not classroom validation. Read `AGENTS.md`, this run's full `PROMPT.md` and scope addendum, the exact LaTeX and source README, the local checker, and the independent kernel review. Rendered the delivered PDF afresh with Poppler and inspected **all four pages**, not merely extracted text. Ran `draft/src/check_math.py` successfully. No draft file was edited.

Reviewed PDF SHA-256: `3caa6045d880d6d93713a7298a8680a9270d8a68a6284021b2e2bbfb49a22839`.
Reviewed LaTeX SHA-256: `a626256a71b1aa9d61d0dccaa2c1aeeb6e7a15a3cdc83ded314f7d59ef1ea83e`.

## Revisions and risks, in priority order

1. **Page 2, Problem 2: distinguish surviving measurements from surviving every exact test.** “Which positions for O survive every test?” is too absolute immediately after a ruler-and-dot experiment. The centered position is uniquely correct in the specified affine-fan family, but nearby wrong positions can survive every practicable measurement. The printed grid has quarter-unit spacing. At O = (1.25, 1), even the clean vertical midpoint witness exceeds a factor of 2 by only about **0.735 mm** in new length on this printout. Smaller displacements make the discrepancy arbitrarily smaller. Prefer “Which positions for O survive your tests?” or equivalent experimental wording. Keep the exact universal question on page 3. In the later adult guide, separate an observed candidate, the exact midpoint argument for this family, and the all-pairs proof for a whole-sheet rule. Do not require a calculator or an exact answer from ruler noise.

2. **Page 1, Problem 1: make the checking partner's adversarial goal explicit.** “Your partner chooses pairs” does not say that the partner is trying to expose a large stretch. A low score from three conveniently chosen pairs says very little even about the five pins. A short change such as “Your partner tries to find the pair with the largest stretch” makes the roles enforce the intended game. Keep “found” or other finite-test language in the definition of the observed score.

3. **The opening optimization is deliberately flat. Preserve its purpose but do not overrun it.** Every legal O position has five-pin maximum exactly 2: AD and BC already attain 2, and no corner–O pair exceeds it. The child controls O, but that choice cannot improve this true score. This is a useful counterexample to trusting sparse measurements, not a rich optimization by itself. The later adult guide should recognize the discovery of this tie as a natural transition to Problem 2 rather than asking for many more unproductive placements. This is a pacing risk, not a demand to discard Problem 1 or add the answer to the student page.

4. **Prerequisite boundary: page 3 needs more than measuring several pairs.** An exact all-pairs explanation must handle diagonal displacements, not just horizontal and vertical test segments. Ruler use, halves, and the multiplier convention suffice to enter pages 1–2. For pages 3–4, an adult may need a geometric argument that horizontal compression cannot increase straight-line distance, or a squared-distance argument for children ready for it. Keep this optional scaffolding with adults. The README appropriately marks whole-sheet explanations as later work; retain that distinction in the eventual guide.

## Mathematical checks

- **Problem 1:** the source O is (2, 1/2), and its distance from every corner is sqrt(17)/2. A point inside the target square is less than sqrt(8) from every target corner, giving a corner–O ratio below sqrt(32/17), hence below 2. The side pairs AD and BC have ratio 2. Consequently every true five-pin score is 2. The local finite checker agrees; the argument, not sampling, establishes the general claim.
- **Problem 2:** the boundary midpoints (2,0), (2,1) map to (1,0), (1,2). For target O = (a,b), the two relevant ratios are 2 sqrt((a−1)^2+b^2) and 2 sqrt((a−1)^2+(2−b)^2). Both are at most 2 only at (1,1). Thus the printed halfway-dot rule supplies valid witnesses against every off-center O. The triangle correspondence is continuous and one-to-one for every interior O, and the non-task PQR example correctly demonstrates midpoint transfer.
- **Problems 3–4:** F(x,y) = (x/2, 2y) is a legal whole-sheet map. For a displacement (u,v), u²/4 + 4v² ≤ 4(u²+v²), so no pair stretches more than twice. Any legal named-side map sends the endpoints of a source vertical unit segment to opposite target sides separated by 2; therefore no map can make every pair's ratio less than 2. The side-preserving hypothesis is present. No Teichmüller-metric claim appears.
- **Problem 5:** for a target width w and height h, the optimum is max(w/4,h), achieved by coordinate scaling and forced by the two opposite-side separations. The two printed answers are 2 and 3.
- **Problem 6:** valid distinct examples include 6 by 1 and 4 by 1.5. The open invention task is well posed and retains mathematical choice.

## Page-by-page visual and usability inspection

- **Page 1:** the 2 cm to 3 cm convention example is dimensionally correct and precedes use. Rectangle and square share the same physical unit; their displayed 4:1 and 2:2 proportions are correct. Dots, letters, rules, and four recording rows are legible. No clipping or collisions. The facing rotated “right” and “left” labels are close but readable. No Name/Date field or prohibited decorative heading.
- **Page 2:** midpoint labels and dashed comparison segment are correct. The affine example is visibly a different instance from the target problem. Both fan boards remain usable, with room below for a position and findings. The partner places O although the opening sentence refers to joining it first; this is a minor ordering awkwardness, not an inability to perform the task.
- **Page 3:** grids and side names are clear, and ample writing space separates construction from proof. “No gaps, overlaps or tears” usefully states the whole-sheet requirement in ordinary language. The leap to arbitrary pairs is mathematically substantial; it should remain a readiness-dependent continuation.
- **Page 4:** both target rectangles are drawn at the correct proportions and a consistent scale within their pair. Prompts fit, and answer areas are sufficient for a compact rule and witness, although additional scratch paper will help explanations. The invention problem is a genuine further direction rather than routine extra arithmetic.

## Preserve and verify after revision

Preserve the one shared Grades 4–5 packet, the child-controlled O placement, the finite-sample versus whole-map distinction, the non-task convention examples, and the partner tests. Do not add the theorem or its proof to the student directions. Re-render all four final pages and recheck proportional scaling and labels. Physical dot/strip/ruler rehearsal remains untested; specifically test whether children can make and interpret the intended midpoint comparisons at this print scale.
