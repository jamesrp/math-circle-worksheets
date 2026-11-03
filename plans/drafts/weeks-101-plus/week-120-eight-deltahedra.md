# Week 120 (draft plan): Gems made only of triangles

**Strand:** shape (Shapes and spaces). **Deep-math field:** polyhedra, Euler's formula, discrete geometry. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A deltahedron is a polyhedron whose faces are all equilateral triangles of one size. There are exactly eight strictly convex ones, with 4, 6, 8, 10, 12, 14, 16 and 20 faces: the tetrahedron, triangular dipyramid, octahedron, pentagonal dipyramid, snub disphenoid, triaugmented triangular prism, gyroelongated square dipyramid and icosahedron (Freudenthal and van der Waerden, "On an assertion of Euclid", Simon Stevin 25, 1947; Kaufman credits a first enumeration to Rausenberger, 1915). Part of the theorem is elementary counting. Each face has 3 edges and each edge joins 2 faces, so 3F = 2E and F is even; Euler's V − E + F = 2 then gives F = 2V − 4. At a convex corner the face angles must leave a gap, 360° − 60°·k > 0, so 3, 4 or 5 triangles meet at each corner, and the gaps total 720° (Descartes, Week 56), which is the same as saying the numbers 6 − (corner degree) add to 12. So V ≤ 12 and F ≤ 20. Eighteen faces would need 11 corners, and the counting forces exactly one corner of degree 4 and ten of degree 5; an exhaustive search in the check script finds no closed triangle pattern with that degree list, so 18 fails before any geometry. The geometric half is subtler: the search finds 11 closed patterns with every degree at most 5, and three of them (a capped dipyramid, a capped octahedron and an octahedron capped on two opposite faces) cannot be built convex from equilateral triangles, because a tetrahedron cap on an octahedron lies exactly flat (70.53° + 109.47° = 180°) and a cap on the dipyramid makes a dent. Proved: the list of eight. Checked here: the counting, the 11 patterns and the 18-face gap. Children can discover that the counts they build are even, that they never get more than five triangles at a corner, and that some counts (2, 18, anything above 20) never appear. Allowing non-equilateral triangles changes the answer: any even number of faces from 4 up is possible (Lee's notes).

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Deltahedron](https://mathworld.wolfram.com/Deltahedron.html), Eric Weisstein, MathWorld (read November 3, 2026). Eight convex deltahedra with 4 to 20 faces; gives the citation Freudenthal and van der Waerden, Simon Stevin 25, 115–121, 1947.
- [The Convex Deltahedra](https://www.interocitors.com/polyhedra/Deltahedra/Convex), Roger Kaufman, Roger's Polyhedra, 2006–2024 (read November 3, 2026). Corner-degree table for all eight; Rausenberger's 1915 enumeration and the 1947 proof; 18-face forms exist only with coplanar faces.
- [The Deltahedra](https://www.ms.uky.edu/~lee/ma415fa10/delta.pdf), course notes at Carl Lee's MA 415 page, University of Kentucky (no author named on the page) (read November 3, 2026). A class built the eight; evenness by the handshake count on the face network; any even count with non-equilateral triangles.
- [Deltahedral Domes over Equiangular Polygons](https://arxiv.org/html/2408.04687v2), Akitaya, Demaine, Hesterberg, Lubiw, Lynch, O'Rourke, Stock, Tkadlec, arXiv 2408.04687 (read November 3, 2026). Calls the eight convex deltahedra the best-known result in the area and pursues current questions about deltahedral domes.
- Prior use with children: [Getting to grips with geometry](https://www.tes.com/news/getting-grips-geometry), Ian Wilson, Tes, 1995 (read November 3, 2026), reviews a Polydron booklet for ages 11–16 that asks pupils to find the remaining convex deltahedra. No K–5 circle handout found (searched NRICH, JRMF and "deltahedra" with Polydron, Magna-Tiles and Geofix).

## A kid-friendly way in

Build closed "gems" from equilateral triangles only, with every corner poking outward. Materials: magnetic triangle tiles (Magna-Tiles or Polydron; borrow class or family sets, about 20 triangles per pair) or, as a paper fallback, card sheets printed with rows of triangles, cut into strips with a paper cutter, folded on the lines and taped. Prep: sort tiles into bags of 20, or cut strips (under 30 minutes). Launch (2–3 minutes): build a tetrahedron in front of everyone, count its 4 triangles, then push one corner inward to show a dent that does not count; ask "What other numbers of triangles can make a gem?"

## By band

- **K–1:** Build gems and count triangles; put each finished gem on a number line card (4, 6, 8, ...). Notice which numbers the table found. Almost no reading: the rule is shown, not written.
- **2–3:** Find gems with as many different triangle counts as possible. Can anyone make one with an odd count? With 18? With more than 20? Count triangles at each corner and record the largest.
- **4–5:** Explain why every count is even (each triangle has 3 edges, each hinge uses 2), why a corner holds at most 5 triangles (lay them flat, as in Week 56), and why 20 is the most (the corner gaps total 720°, and every corner leaves a gap of at least 60°, so there are at most 12 corners). Try to build an 18: the adult can show that it must have one corner of 4 and ten corners of 5, and the group tests whether that can close.

## Checked facts

In `check_shape_a.py`, `check_week_120()`: 3F = 2E and F = 2V − 4 for V = 4 to 12; corner degrees 3, 4, 5 only; each of Kaufman's eight degree lists sums to 3F and has gap total 720°; 11 corners force degrees (one 4, ten 5); an exhaustive search of closed triangle patterns with degrees at most 5 finds 1, 1, 2, 2, 2, 1, 1, 0, 1 patterns for 4 to 12 corners (11 in all, none with 11 corners), containing all eight deltahedra; the three extras are capped forms; tetrahedron plus octahedron dihedral angles total exactly 180° and three tetrahedron angles total 211.6°. The search was also run without the degree limit and reproduced the known counts 1, 1, 2, 5, 14, 50 of sphere triangulations with 4 to 9 corners. The full classification (which patterns are geometrically convex) is cited to Freudenthal and van der Waerden via MathWorld and Kaufman.

## Nearest existing themes

Week 56 (Corners of a solid) is the closest: its Problem 3 asks which groups of 3 to 6 triangles close into a pointed corner, and its Problem 9 counts the icosahedron from "five triangles at every vertex". This week reuses that gap fact as a tool and asks a new classification question: which whole solids exist. Week 37 (Mirror twins) shares the tetrahedron only. Week 52 (Hinged frames) touches rigidity: a tape-hinged gem holds its shape, which could be an aside, not a claim to prove here. Untangling networks (scouting draft) uses E ≤ 3V − 6, the same counting from the flat side. New here: an existence-and-impossibility census of solids, and the gap between what counting allows and what geometry allows.

## App connection

Shapes and spaces. A 3D builder is a large build (the Week 56 decision kept turning solids on paper). A flat family could carry it: a "gem map" board shows a flat drawing of a gem's triangles (one face stretched to the outside), and the child adds or removes dots and links until every dot meets 3, 4 or 5 triangles; the app then folds the map into the gem. Example puzzles: "Finish a gem with 7 corners" (pentagonal dipyramid); "Make one where every corner has 4" (octahedron). The Week 56 corner-ring builder could share the corner check.

## Open questions

- Material fit: do magnetic tiles hold the 16- and 20-face gems without collapsing, and do the magnets' polarities allow every hinge? Rehearse the snub disphenoid (12) and the icosahedron.
- The three capped extras will appear as near-misses (flat faces); the guide must say how to judge "pokes out" with a ruler or by eye.
- Is the 18-face impossibility explainable to 4–5 beyond the degree count, or should it stay an adult-held fact?
- Age fit of the 12- and 14-face gems for K–1 builders, who may need a photo card.
