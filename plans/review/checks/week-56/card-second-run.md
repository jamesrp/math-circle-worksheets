# Week 56: Corners of a solid (Euler's formula and total angular gap)

**Verdict: revise.** The mathematics, the problems and the upper proofs are at the bar, and every answer checks. One must: the K–1 entry the outline promised ("handle closed solids, match face corners and compare … fans") is one page, P3, and the guide's fallback repeats it.

Reviewed October 10, 2026 by Claude, with the math check in math.md; I confirm its three findings (fixes 2 and 3). Packets: week-56-students.pdf (N56-S-v2, 9 pp.: pp. 1–6 Grades 2–5, P1–6; pp. 7–9 Grades 4–5, P7–9); week-56-materials.pdf (N56-M-v1, 4 pp.). Adult guide: week-56-facilitator.pdf (N56-FAC-v1, 10 pp.). Companions: none exist. Status: unpiloted; guide p. 2 lists folding, tape, fit, preparation and timing as unrehearsed. Written October 4 under the 52–63 routing, which allowed "genuine shallow younger entries".

## The mathematics

Closed convex polyhedra have V − E + F = 2, and their vertex gaps (360° minus the face corners) total 720°. Children count four solids (P1), find that sides pair into edges while corners don't fix the vertex count (P2), fold corner fans (P3), total the gaps on equal and unequal solids (P4–P5), and see subdivisions change neither count (P6). Grades 4–5 prove both (P7 by reduction to a tree, P8 by summing face angles) and run them backward to the icosahedron's and dodecahedron's counts (P9). A mathematician would enjoy it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Euler and Descartes with hypotheses, subdivision invariance, a reverse deduction. |
| Problems | strong | Contrasts carry it: cube and octahedron both 24 corners (P2); two flat fans among six (P3); prism and octahedron share 120° from different corners (P4); unequal pyramid (P5); three redrawings (P6). |
| Student pages | adequate | Spec header and footer, no slop, worked visuals before first use on pp. 1, 3, 4, 7, 8. Faults: P6's wording; p. 7 prints the proof route. |
| Concreteness | strong | Closed models make vertex and edge physical; paper fans can't stretch an angle; the guide p. 3 launch shows face, edge, vertex and a two-triangle fan before the tables split. 30 mm models unrehearsed. |
| Correctness | strong | Every answer, table and proof step checks (math.md), except two p. 1 thumbnails no solid could produce (fix 2). |
| Adult guide | strong | Theorem-first p. 1 with hypotheses, limits, band map; full keys, ordered hints, a verified tree route, the face-angle argument, return visits. K–1 route thin. |
| Age fit, K–1 | weak | Guide p. 3: "Younger: Problem 3 orally … Fallback: one child builds a fan, the partner predicts flat or pointed closure". Nothing else. |
| Age fit, grades 2–3 | adequate | P1–P3 need counting only; P4–P5 need 8 × 90 and 4 × 150 with support; P6 is dense and starts at 8 − 12. |
| Age fit, grades 4–5 | strong | Real proofs with the organizer at a table of three; P9 needs 540 ÷ 5 and 720 ÷ 36. |

## Keep

- p. 1: the closed-model rules, the sides → edge → vertex visual, P1's four models.
- P2's "Can the separate face-corner count alone tell you the vertex count?" with the cube and octahedron rows.
- P3's six groups, its wording "close into a pointed corner with no inward dents … close flat with no gap", and the non-task two-triangle visual.
- P4's four models, P5's pyramid, P6's three redrawings and "Can a new vertex have a gap while the cube keeps its shape?"
- p. 7's opened-view conversion, P8's pentagon angle sum, P9 "without a model of the whole solid".
- Materials: five lettered nets, checked to fold correctly; the 30 mm bar; 80 mm circles.
- Guide: p. 1 overview, the P6 independence note, the P7 route AB, BC, CD, DA, ab and the P8 explanation.

## Fix

1. **must**, K–1, guide pp. 1–3 and 5. The table gets P3 and a fallback that repeats it: neg.md's K–1 band shorter than the mathematics allows, as on the Week 53 and 63 cards. Fix: head pp. 1 and 3 "Grades K–5" and write a guide route. The launch; P1 for the cube and tetrahedron, faces then vertices, with removable marks, the parent writing numbers; all six P3 groups; then gaps without degrees. Rebuild each corner's fan flat and fill its gap with pattern-block pieces, one pile per model: tetrahedron 4 × 3 = 12 triangles, octahedron and prism 6 × 2 = 12, cube 8 squares, pyramid 6 triangles and 4 squares. Ask how many flat rounds each pile makes: always two. Supply 12 triangles and 8 squares per pair. I checked the counts; that K–1 sustains this is a prediction.
2. **should**, Grades 2–5, p. 1, P1 table. The tetrahedron thumbnail dashes one of the three edges at its inside vertex and draws the other two solid; the octahedron thumbnail lays two hidden edges on the solid vertical edge, so 10 edges show, 2 dashed. By guide p. 4's "dashed lines are hidden edges", a child checking the picture may count 10. Fix (math.md): draw (0,0)–(1.65,1) solid; in `\octa` move the front ring vertex to (1,1.15) and the back to (1.8,2.05).
3. **should**, p. 6, P6: "try these three changes". Kept together they give (9,17,10) and (10,18,10), against the key's (9,16,9) and (9,13,6); conclusions hold, but an adult with the key may correct a right row. Fix: "try each of these three changes on its own, starting from the original cube."
4. **should**, Grades 4–5, p. 7, third panel "three boundary edges erased / a tree remains". With P7's tree question it prints the proof's procedure. Fix: drop the panel; keep the opened-view conversion and the question; guide p. 7 shows the tetrahedron reduction when needed.
5. **could**, p. 7: "opened cube: five bounded faces" gives a count children can find; write "opened cube".
6. **could**, p. 6: three of the "four models in Problem 1" have no V − E + F space; add rows.
7. **could**, guide p. 6: suggest V + F − E for third graders who stop at 8 − 12.
8. **could**, guide p. 2: write "KK11 / 3333 / 445" as K–1, 2–3, 4–5.
9. **could**, Grades 4–5: ask for a rule linking V, E and F before P6 prints the expression.

## Overlaps

Week 53 supplies P7's E = V − 1 for trees; Week 14, P8's n − 2 triangles. Week 61's spherical excess is the smooth cousin of the 720°; Week 65's floor, four octagons at every corner, is the negatively curved side P3 never reaches, a good return visit. Weeks 26 and 37 share objects, not theorems. No other theme owns V − E + F on solids or the total gap. No merge.

## App fit

Change C to B, size M. A fan builder: the child taps triangles (T) and squares (S), later pentagons, into a ring around a dot; the app lays it flat with the gap shaded and, on "close", folds it to a point, leaves it flat, or shows the overlap. Solves: find every ring that closes to a point (10 piece sets, 11 rings up to turning and flipping, by my enumeration) and every flat ring (SSSS, TTTTTT, TTTSS, TTSTS), with a "That's all" claim the app checks; the "can't" certificate is the angle total laid flat. Then "build this solid's corner" (P4, P5) and a fill-the-gaps playground ending in two flat rounds (fix 1). Pitfalls: P9's inventory and "what is V − E + F?" are prediction; a live gap or Euler counter gives the theorem away; counting on a rotating solid is bookkeeping. P7's tree reduction belongs in Week 53's graph editor.

## Classroom evidence

None reported. Unpiloted; no physical rehearsal (guide p. 2, source README).
