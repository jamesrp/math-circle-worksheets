# Week 122 (draft plan): Tangram shapes with no dents

**Strand:** shape (Shapes and spaces). **Deep-math field:** dissections, lattice polygons, convexity. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The seven tangram pieces form exactly 13 convex polygons: one triangle, six quadrilaterals, two pentagons and four hexagons (Wang and Hsiung, "A theorem on the tangram", American Mathematical Monthly 49, 1942, pp. 596–599). The proof turns a puzzle with infinitely many placements into a finite count. Every tan is made of the same small half-square triangle (2 large tans of 4, the medium triangle, square and parallelogram of 2 each, 2 small tans of 1: 16 in all), and the proof's lemma (cited, not checked here) places these 16 small triangles of a convex arrangement on one square grid, cut by diagonals. On that grid a convex shape has sides only in the 8 compass directions, so its corners turn by multiples of 45° and it has at most 8 sides. The check script lists every convex grid shape made of 16 half-squares: there are 20, the largest with 6 sides, and a search for tan placements fills exactly 13 of them, matching the theorem's list by side count. The 7 that fail are all thin four-sided shapes, such as the 1-by-8 rectangle and the trapezoid with parallel sides 9 and 7 at height 1. The limit is the grid lemma: without it, a shape off the grid is not ruled out by the count, and the lemma is cited, not checked here. Children can discover that "no dents" shapes are rare, that the corners of such a shape are all 45°, 90° or 135°, and, with an adult, why there can be only a finite list. Current research still extends the theorem: Pohl and Richter (2020) list all 53 simple tangram pentagons, convex or not.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The complete characterization of tangram pentagons](https://arxiv.org/pdf/2006.09698), Sarah Sophie Pohl and Christian Richter, arXiv 2006.09698, 2020 (read November 3, 2026). States Wang and Hsiung's theorem (exactly 13 convex tangrams: one triangle, six quadrangles, two pentagons, four hexagons) with the Monthly citation, and proves there are exactly 53 simple tangram pentagons.
- [A Theorem on the Tangram](https://blogs.canisius.edu/mathblog/?p=371), Canisius College mathematics blog (read November 3, 2026). Citation (Monthly 49, no. 9, 1942, 596–599) and the proof's key fact that every piece is made of unit isosceles right triangles.
- [The Art and Mathematics of Tangrams](https://static1.bridgesmathart.org/2012/cdrom/proceedings/143/index.html), Xiaoxi Tian, Bridges 2012 short paper (read November 3, 2026). Uses the set of thirteen convex polygons as a springboard for teaching.
- Prior use with children: [World of Tan 13: A Storm in a Tea Cup](https://nrich.maths.org/14182), NRICH, ages 7 to 11 (read November 3, 2026). Children fit the tans into the outlines of two convex shapes, with a side discussion of convex and concave.

## A kid-friendly way in

Make tangram shapes with "no dents": a rubber band stretched round the outside touches the shape all the way round. Materials: one tangram set per child or pair (foam or card; a printable sheet on card cut with a paper cutter makes 10 sets in about 20 minutes), rubber bands, outline cards of a few of the 13 shapes at full size, scrap paper for tracing finds. Launch (2–3 minutes): make the big square in front of everyone and stretch a band round it; then make a house shape with a dent and show the band skipping the dent. "Find other shapes that use all seven pieces and pass the band test."

## By band

- **K–1:** Fill full-size outlines of convex shapes (the square, the triangle, a rectangle, the parallelogram); the band test is shown, not read. Then make any band-passing shape and trace it.
- **2–3:** Find as many different band-passing shapes as possible and trace each; the class pools them and decides when two are the same (turned or flipped). How many sides can such a shape have? Which corners appear?
- **4–5:** Cut every tan into small half-square triangles (16) and draw found shapes on half-square grid paper. Why are the corners only 45°, 90° or 135°, and why at most 8 sides? Can you make a pentagon? A hexagon? An adult can reveal that exactly 13 exist and the group checks its pooled list against that number; extension: a thin shape on the grid (1 by 8) that the tans cannot fill, and why.

## Checked facts

In `check_shape_a.py`, `check_week_122()`: the tans total 16 half-squares (32 quarter-cells); there are 20 convex grid shapes of area 8 with sides in 8 directions (longest side 9, so the search bound of 10 does not cut any off); an exact-cover search places all seven tans in exactly 13 of them, with side counts 3, 4 (six times), 5 (twice) and 6 (four times), matching Wang and Hsiung; the other 7 are quadrilaterals. The grid lemma itself is cited to Wang and Hsiung via Pohl and Richter and the Canisius summary.

## Nearest existing themes

The brief asked about Weeks 85, 93 and atlas GA-22: none overlaps. Week 85 is a pantograph (scaling), Week 93 reshapes rectangles toward a square, and GA-22 wraps bands round pegs for Radon's theorem; GA-22 and Week 22 share only the rubber-band picture of a convex hull. Closer are Year 1's pattern-block coverings and Weeks 1 and 1e (filling outlines with blocks, with counting invariants), Week 26 (area fixed, boundary varies) and Week 32 (dissecting rectangles into squares). No catalog week uses tangrams. The sibling draft Week 126 (Cut and rearrange, Bolyai–Gerwien) also cuts and reassembles polygons, but asks whether any two equal areas are related by some dissection, not which shapes one fixed set of pieces can make; schedule them apart or pair them deliberately. New here: a complete, finite classification by a grid argument, and convexity as the property that makes the list finite.

## App connection

Shapes and spaces. The Tile gardens family (covers a garden with tiles) could carry it with a half-square grid and the seven tans, rotating in 45° steps and flipping the parallelogram. Puzzles: "Fill this outline" for each of the 13; "Make a shape with no dents and 5 sides" with a checked "That's all" (2 pentagons); a "Can't" board for the 1-by-8 strip. The app should not show a running count of shapes found.

## Open questions

- Is finding the 13 without outlines too frustrating at 2–3? Silhouettes of the 13 as cards may be needed, held back for later.
- Card or foam sets: do printed sets keep exact angles well enough for the band test?
- The grid lemma is the heart of the proof and the hardest part; decide whether 4–5 get a version of it or only the count on the grid.
- A text search of the Year 1 folder and of `plans/` found no tangram use; the Year A plan's pentomino session is the nearest piece-fitting activity, so space the two apart.
