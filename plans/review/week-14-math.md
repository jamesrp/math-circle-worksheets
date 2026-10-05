# Week 14 (polygon triangulations and flips): math check

Scope: `lowell-math-circle-year-2/week-14/week-14-k-1.pdf` (6 pp., Problems 1–6), `week-14-grades-2-3.pdf` (8 pp., Problems 1–7; p. 8 is "Problem 7 (continued)") and `week-14-grades-4-5.pdf` (7 pp., Problems 1–7), with `week-14-facilitator.pdf` (14 pp.; p. 14 is the 4 October route update). I also checked the return-visit companion in the same folder: `week-14-return-visit.pdf` (6 pp., Problems 1–3) and `week-14-return-visit-facilitator.pdf` (5 pp.). Archive folders were ignored. My scripts and outputs are in [checks/week-14/](checks/week-14/). Checked October 5, 2026.

**Result: no mathematical errors in any student band of the base packet or in any stated answer, proof or extension of either guide. I found 4 problems, all about how pages present a task. In the base packet, one K–1 page prints twice as many pre-lined copies as there are answers. One planning note in the base guide cites the wrong problems. In the return visit, Problem 2 asks children to circle corners that are already printed as circles, and the second required drawing of Problems 1 and 2 sits under an "Extra workspace" heading.**

## How it was checked

- All six delivered PDFs are byte-identical (MD5) to the reference copies in `source/week-14/editable/reference-pdfs/` and `source/week-14-return-visit/reference-pdfs/` (`check_text.out`).
- `pdfgeom.py` is my own standard-library PDF reader. `extract_figures.py` uses it to read every polygon straight out of the PDFs. A closed stroked polyline is an outline, a stroked segment between two of its corners is a diagonal, and a one-character word just outside a corner, on the outward ray from the centre, is that corner's label. It covers 255 drawings: 175 on base student pages, 24 in the return visit and 56 guide figures. Each page is compared with my own transcription, `expected.py`, which I typed from the rendered pages; for guide figures I typed the caption or table beside each picture. All pages match (`extract_figures.out`). Every student board and every guide polygon is regular, with equal circumradii and equal sides to within 4·10⁻⁴ (relative). Labels run clockwise from the top corner (A or 1). The only non-regular shapes are intentional: the rhombus flip example (2–3 P4, 4–5 P3), the return visit's peeled "After" quadrilateral A-C-D-E, and the guide's local quadrilateral on p. 11, which is convex. `check_guide_map.py` reads the guide's drawn pentagon map (p. 6) and finds it equals the computed flip graph.
- `tri.py` and `solve.py` are my own enumeration code. Triangulations come from two independent generators, noncrossing (n−3)-subsets and root-side recursion, which agree for n ≤ 8; the counts are 1, 2, 5, 14, 42, 132, 429 for n = 3…9. For n ≤ 9 I computed flips from the actual triangles, built the flip graphs and ran BFS. The scripts check the following:
  - Every noncrossing chord set that cuts the polygon into triangles only has exactly n−3 chords, for n ≤ 8, so 3 triangles in a hexagon is impossible.
  - Every filling has exactly n−3 distinct flip neighbours, and two fillings are neighbours exactly when they share n−4 diagonals.
  - The flip graphs are connected.
  - The distance to the fan at any corner v is n−3−d_v for all fillings and all v, for n ≤ 9.
  - Every non-fan filling has a flip that adds a diagonal at A.

  Every starting filling the solver uses is read from the PDFs, not typed. All 95 checks pass (`solve.out`).
- `rv_check.py` enumerates every peeling word, every three-colouring, every minimum corner cover and every rotation-fixed hexagon filling. It also checks the general claims for n up to 10. On the printed Problem 3 board it rotates the PDF's own corner coordinates about the printed centre mark. The mark is at the centre to 10⁻⁴ pt, and 60°, 120° and 180° turns carry corners to corners. All 42 checks pass (`rv_check.out`).

## K–1

- **P1:** the pentagon has 5 fillings and the hexagon 14, so two different ways exist for each; every pentagon filling has 3 triangles and every hexagon filling 4.
- **P2:** exactly 5 fillings, the five fans. The page has 8 small copies.
- **P3:** 4 triangles yes, 3 no. Every noncrossing chord set whose pieces are all triangles has 3 chords and 4 triangles.
- **P4:** with 1–3 the pentagon has 2 completions ({13,14}, {13,35}); with 1–4 the hexagon has 4. See problem 1 below.
- **P5:** each start has exactly 3 one-change results: {13,14,15} → {14,15,24}, {13,15,35}, {13,14,46}; {13,15,35} → {15,25,35}, {13,35,36}, {13,14,15}.
- **P6:** yes. From the 1-fan there are exactly 2 loops through all five fillings, one each way round the five-cycle.

## Grades 2–3: checks out completely

- **P1:** two fillings always exist and the counts cannot differ: 4 triangles in a hexagon, 5 in a heptagon.
- **P2:** 5 fillings.
- **P3:** the same 3 + 3 results as K–1 P5, in letters.
- **P4:** the five printed pentagons are the five fillings, and there are exactly 5 joins, FA–FC–FE–FB–FD–FA. The page places the drawings in that cycle order, so no join needs to cross another. The example (AC, then BD on the rhombus) is one flip.
- **P5:** the shortest odd return is 5 flips; returns of length 1 or 3 do not exist.
- **P6:** start {BD,BE,BF}, target {AC,AD,AE}, distance 3. Repeat-free routes exist with every length from 3 to 13, so "a different number" can always be found.
- **P7:** 14 fillings; pp. 7–8 give 17 small outlines.

## Grades 4–5: checks out completely

- **P1:** 5 fillings.
- **P2:** as 2–3 P3.
- **P3:** the five-cycle again. It is not bipartite, so an odd return exists (5 flips).
- **P4:** the starts {BD,BE,BF}, {AC,AE,CE} and {AD,BD,DF} are 3, 1 and 2 flips from the A-fan, the fourth drawing. Each equals the number of missing A-fan diagonals, so "no shorter" follows from that bound.
- **P5:** start {AC,AD,DF,DG,DH}: 3 flips to the A-fan (d_A = 2) and 5 to the E-fan (d_E = 0); 8 copies hold the 3 + 5 new pictures.
- **P6:** the rule n−3−d_A holds for every filling with n ≤ 9.
- **P7:** S and T share no diagonal and are 5 apart, so a 5-flip route is shortest. All flip graphs with n ≤ 9 are connected.

## Adult guide

The overview is true with the hypotheses it states: strictly convex, labelled, no new vertices. That covers n−2 triangles and n−3 diagonals, C_{n−2} fillings, exactly n−3 flip neighbours, connectivity, the exact fan distance n−3−d_v, and the remark that missing-diagonal counts are only a lower bound for non-fan targets; in the hexagon, 8 ordered pairs exceed that bound by one. The proofs are sound: the pentagon shared-corner argument, the triangle-count induction, the quadrilateral argument for one-flip completeness, the fan-growing construction on p. 11 (whose figure is convex) and the reverse-the-second-route connectivity proof.

Every list, route and count in the keys matches my computations: the K–1 P4 and P5 catalogs, the 2–3 P3 neighbour lists, the five joins, "no shorter odd return", the 3-flip and 4-flip 2–3 P6 routes (legal, no repeats), the 5 + 2 + 2 + 5 catalog of all 14 grouped by the triangle on AF, the distances 3/1/2 and 3/5, both P5 routes and the P7 route, and "A gives 3 + 4 = 7". (Through the D-fan the same construction gives 5, which is also correct and consistent with the guide.) The extensions are also right: 14 + 5 + 4 + 5 + 14 = 42, the Catalan recursion, and the non-fan example, where the first flip can add only AC, BE or DF and the distance is 4 by the route given. All 56 guide figures match their captions. One planning note cites the wrong problems (problem 2 below).

### 1. K–1 Problem 4: the pentagon has four pre-lined copies but only two answers (student p. 4)

- **Quoted text and diagram:** "Fill each shape with triangles, keeping the printed line. Find every way." The large pentagon and **four** small copies all carry the line 1–3. The large hexagon and four small copies carry 1–4.
- **Evidence:** the pentagon has exactly 2 completions, {13,14} and {13,35}; the hexagon has exactly 4 (`solve.out`). On this page the hexagon's four copies match its answer count, which teaches the reader that the boxes count the answers. A K–1 child who has the two pentagon answers will keep hunting for two that do not exist, or will fill the copies with repeats. The guide's key ("leaves a quadrilateral with two choices") does not tell the adult that two copies stay empty. (K–1 P5 has the same pattern less sharply: 4 copies per start for 3 results, but the key there says "exactly three".)
- **Smallest fix:** print two pre-lined pentagon copies, not four. If the page stays as it is, add to the guide's K–1 P4 key: "Only two pentagon completions exist; two of the four pre-lined copies stay empty."

### 2. Route update: the Grades 2–3 return route cites hexagon problems as pentagon work (guide p. 14)

- **Quoted text:** "Grades 2-3 can use their pentagon gallery for the flip map and routes (P3-6), leaving the hexagon collection (P7) for a separate investigation."
- **Evidence:** only P4 (the map) and P5 (the odd return) use the pentagon gallery. P3 (one-flip results) and P6 (the shortest route from the B-fan to the A-fan) are hexagon problems (2–3 pp. 3 and 6). An adult preparing from this note would bring pentagon material for two hexagon tasks.
- **Smallest fix:** "Grades 2-3 can use their pentagon gallery for the flip map and odd return (P4-5), with the hexagon one-flip and shortest-route problems (P3, P6), leaving the full hexagon collection (P7) for a separate investigation."

## Return visit

The answers and the companion guide check out:

- **P1:** the fan has 8 complete peeling words and the central drawing 12. On both, every triangle can be the last one. The guide's example words leave the stated triangles. Ears run from 2 to ⌊n/2⌋, no two ear corners are adjacent, and a fan has exactly 2 (n ≤ 10).
- **P2:** each drawing has a colouring that is unique up to renaming. The fan needs 1 corner (A only). The central drawing needs 2, and the minimum pairs are exactly AC, AD, AE, BE, CE and CF. R,Y,B,R,Y,B is valid. The smallest colour class is at most ⌊n/3⌋ and touches every triangle (n ≤ 9).
- **P3:** 6 fillings match after a half-turn, 2 after a one-third turn and 0 after a one-sixth turn. No filling is in two of these lists, so there are 8 answers for 9 boxes. Both of the guide's lists are exactly right, and the worked example (AC lands on DF) is drawn correctly.

### 3. Return visit Problem 2: every corner is already printed as a circle (pp. 3–4)

- **Quoted text and diagram:** "Circle as few corners as possible so every triangle touches a circled corner." All six P2 drawings, two large and four small, print an open circle of radius 0.12 in on all six corners. They are meant to hold the colours.
- **Evidence:** `rv_check.out` finds 6 rings on 6 corners in every drawing. As printed, every corner is already circled, so the condition "every triangle touches a circled corner" is already met, and a circle a child draws looks like the printed ones. The intended answers (1 corner, A, for the fan; 2 for the central drawing) cannot be recorded unambiguously. The corner letters A, B, C, E and F also overlap their rings in every P2 drawing (glyph box inside the ring radius; `rv_check.out`), so colouring a ring partly covers its label.
- **Smallest fix:** "Put a star next to as few corners as possible so every triangle touches a starred corner." Optionally move the corner letters about 0.06 in further out.

### 4. Return visit Problems 1 and 2: the second required drawing is headed "Extra workspace" (pp. 2 and 4)

- **Quoted text:** p. 1 says "Peel ears from each large drawing on these two pages", but p. 2 is headed "Extra workspace for Problem 1". The same happens with p. 3, "Color the corners of each large drawing on these two pages", and p. 4, headed "Extra workspace for Problem 2". Pages 2 and 4 hold the only central-triangle (ACE) drawings.
- **Evidence:** the central drawing is the case that carries each problem's mathematics. It has three ears at the start, where the fan has two, which shows the guide's "'exactly two' is false". Its triangle ACE can be peeled last only after it becomes an ear. It is also the only P2 drawing that needs two corners (the fan needs just A). An adult or child who treats the "Extra workspace" pages as optional loses that contrast and meets only the fan.
- **Smallest fix:** head p. 2 "Problem 1 (continued):" and p. 4 "Problem 2 (continued):", as base 2–3 p. 8 does. Keep "Extra workspace" only for the small spare copies.
