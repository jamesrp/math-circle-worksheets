# Week 12 independent mathematical review

Scope: `draft/return-visit.pdf`, all three pages and all four numbered problems. The explicit shared-layout override was followed: Grades K–3 on page 1, Grades 2–5 on page 2, and Grades 4–5 on page 3. This is the independent mathematician stage only; no draft files were changed.

**No located mathematical errors. All represented bands check out.**

| Page / band | Problem and intended outcome | Independent result |
| --- | --- | --- |
| 1 / K–3 | Problem 1 asks for all unlike-color noncrossing perfect pairings of three fixed six-dot arrangements. | Reading clockwise from the top gives `RBRBRB`, `RRRBBB`, `RRBRBB`; their counts are respectively **5, 1, 2**. All 15 perfect matchings of six fixed vertices were generated, then tested for unlike labels and alternating-endpoint chord crossings. The full pairing lists are saved in `math-audit/results.json`. |
| 2 / 2–5 | Problem 2 asks for all paths with four U and four D steps, height between 0 and 2. | Exactly **8**. Independently generated all 70 balanced eight-step words and rejected those going below 0 or above 2. There are ten supplied grids, so the recording space does not force an incorrect count. Each grid is eight units wide and two units high. |
| 2 / 2–5 | Problem 3 asks for the five-pair count under the same height-2 restriction, with an explanation avoiding a complete drawing list. | Exactly **16** among the 252 balanced ten-step words. Successive excursions correspond bijectively to compositions of 5. This problem changes the path length to ten steps; it does not request drawing a ten-step path on the eight-step grids supplied for Problem 2. |
| 3 / 4–5 | Problem 4 asks for shortest legal adjacent-swap routes from three printed eight-step starts to `UUUUDDDD`, and a way to determine the distance in advance. | Breadth-first search over all legal adjacent unlike swaps gives distances **6, 4, 1**, in the printed order. Explicit shortest routes are saved in `math-audit/results.json`. A shortest route exists from every printed start. |

## Independent mathematical explanations

**Pairing existence and limits.** Equal red and blue counts are necessary since every pair uses one of each. They are sufficient for fixed cyclic positions: any nonempty balanced cyclic word has an adjacent unlike pair. Join that neighboring pair near the boundary, delete it, and recurse on the remaining balanced word. The added boundary-neighbor arc can be kept disjoint from the smaller matching; straight chords also give a noncrossing realization. This proves existence, not equal counts of matchings for different words. All balanced words on 2, 4, 6, 8, and 10 fixed dots were also checked independently. The printed task counts endpoint pairings; neither rotation nor changes in the shape of a connecting line make a new pairing.

**Height restriction.** A height-at-most-two excursion from height 0 must have the form `U(UD)^(k−1)D`, with k up/down pairs. A complete path is a sequence of such excursions, so it corresponds to a composition of n. Conversely, each composition constructs one and only one permitted path. A composition chooses separators among n−1 gaps, hence the count is `2^(n−1)` for n at least 1; the empty n=0 path is a separate case. Independent code checks both directions for n=4 and n=5. As an additional outline check, the four-pair counts under ceilings 1, 2, 3, 4 are 1, 8, 13, 14.

**Shortest swaps.** Count pairs of card positions in which a D lies to the left of a U. The target has zero such pairs. A `DU → UD` swap removes exactly one, raises the affected intermediate path vertex by two, and keeps the path nonnegative. A reverse swap adds one and is legal only when the lowered vertex stays at or above zero. Any word with a remaining D-before-U pair has an adjacent `DU`, so repeated raising swaps reach the target. Therefore this pair count is both a lower bound and an attainable distance. Equivalently, it is half the sum of the target-minus-start vertex heights. The three printed height-difference sums are 12, 8, and 2. Independent breadth-first search agrees with this formula for every Dyck start with one through five up/down pairs.

## Diagrams and worked convention

- All three pages were independently rendered at 120 dpi with PyMuPDF and visually inspected in full. Headers, problem numbering, captions, and footer fit without clipped or overlapping content.
- Page 1 has exactly six places on each large circle; their visible R/B labels match the three words used in the independent computation. Dots occupy matching cyclic positions. The three large rendered circle bounds are square to PDF precision, with diameter about 216 PDF points (3 inches). The six small extra-workspace circles also have square bounds and six dots each.
- Page 2's ten grids have equal horizontal and vertical unit scale; the floor is at 0, the dashed ceiling at 2, and S/E are at the endpoints of the eight-step floor. The two intermediate grid intervals are legible. Problem 3 has a writing area rather than a misleading eight-step working board.
- The page 3 convention visual correctly marks positions 2–3 in `UDUUDD`: its heights are `0,1,0,1,2,1,0`. Swapping that `DU` gives `UUDUDD`, with heights `0,1,2,1,2,1,0`, exactly as the output diagram shows. The card intermediate matches the blue-highlighted step pair.
- Page 3's target and all three start diagrams agree with the printed words. The example grids, target grid, and start grids each use equal x/y scale, although their overall sizes differ. All starts and the worked example remain nonnegative.

Supporting audit: `math-audit/independent_verify.py` and `math-audit/results.json`. The code uses only Python's standard library and does not import the writer's code or check results. Fresh render evidence is in `math-audit/page-1.png` through `page-3.png`.

This is mathematical and digital-layout verification. Physical use and classroom piloting remain untested.
