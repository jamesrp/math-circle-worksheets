# Week 170 (draft plan): Shapes that build bigger copies of themselves

**Strand:** shape (Shapes and spaces). **Deep-math field:** tilings, self-similarity, substitution tilings. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A rep-tile is a shape that can be cut into k identical pieces, each a smaller copy of the whole (rep-k); equivalently, k copies fit together into an enlarged copy. Solomon Golomb named them (in 1962, according to Nitica) and studied them in "Replicating figures in the plane" (Mathematical Gazette, 1964), answering C. D. Langford's question about which figures split into four replicas; Martin Gardner popularised them in Scientific American. Every triangle and every parallelogram is rep-4 (cut through the midpoints). Some shapes are rep-tiles in less obvious ways: the L-tromino (three squares in an L) is rep-4 with exactly one arrangement and rep-9 in 4 ways; the L-tetromino is rep-4, while the T- and S-tetrominoes cannot make a double of themselves; the sphinx (a pentagon made of six equilateral triangles) makes its double from four sphinxes in exactly one way, and three of the four must be flipped over, and it makes its triple from nine sphinxes in 4 ways. Among the pattern blocks, the triangle, rhombi, square and trapezoid double themselves; the hexagon cannot. A rectangle with sides 1 and √2 is rep-2: cut in half it gives two copies of itself, which is why A4 paper keeps its shape when folded, and US letter (8.5 by 11, ratio 1.294) does not (its half has ratio 1.545). A right isosceles triangle is rep-2 as well. Repeating the split forever gives a tiling of the whole plane that is self-similar. For the L-tromino this is the chair tiling, listed in the Bielefeld Tilings Encyclopedia as a substitution tiling with one prototile that is nonperiodic. The L-tromino itself also tiles the plane periodically, so this is a property of the tiling made by repeated splitting, not of the tile; the hat (draft 125) is a tile all of whose tilings are nonperiodic. Counting is immediate: after n splits there are 4ⁿ small pieces (4, 16, 64), each with area 1/4ⁿ of the whole. Proved: the classical constructions; the chair tiling's nonperiodicity is cited. Checked here: every count above by exhaustive search. Open questions remain about which shapes are rep-tiles: Nitica's page lists conjectures, for example about a skewed hexagon. What children can discover: which shapes double themselves, how to build the 4, 16 and 64 copies, that some need flips, and that A4 paper is a rep-tile.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Replicating figures in the plane](https://www.cambridge.org/core/journals/mathematical-gazette/article/replicating-figures-in-the-plane/8AB25F7F11C3462D296A10B68C0E2CDE), Solomon W. Golomb, Mathematical Gazette 48 (366), December 1964, 403–412, bibliographic page and extract (read November 4, 2026). Langford's question about four replicas, triangles and parallelograms always rep-4, his trapezoid and hexagon examples.
- [Rep-tiles revisited](https://www.wcupa.edu/sciences-mathematics/mathematics/vNitica/webRepTiles.aspx), Viorel Nitica, West Chester University (read November 4, 2026). Golomb's 1962 coinage and rep-k definition, Gardner's popularisation, rep-4 trapezoids, hexagons and the sphinx, open conjectures.
- [Chair](https://tilings.math.uni-bielefeld.de/substitution/chair/), Tilings Encyclopedia, Bielefeld University (read November 4, 2026). The chair substitution: one prototile, every tile substituted the same way, nonperiodic.
- Prior use with children: [Tetromino Reptiles](https://static.mathigon.org/lessons/tetromino-reptiles.pdf), Mathigon (Polypad lesson plan, about grade 7) (read November 4, 2026). Enlarge the L-tetromino by 2 to 5 and tile each enlargement; 4 pieces at scale 2, 16 at scale 4; only some enlargements of the T work.
- Prior use with children: [Sphinx Album](https://mathematicscentre.com/taskcentre/sphinx.htm), Mathematics Task Centre, Task 166 (read November 4, 2026). Year 6 classes fold paper sphinxes and build large sphinxes; one class worked on it for many weeks.

## A kid-friendly way in

Pattern blocks; card-stock L-trominoes (three 3 cm squares, about 70 per table, cut from a printed sheet), card-stock sphinxes coloured differently on each side (about 15 per table), one sheet of A4 paper and one of US letter, scissors. Prep about 30 minutes, mostly printing and cutting (a paper cutter helps). Launch (2–3 minutes): put four green triangles together into a big green triangle in front of everyone, then hold up an orange square and a yellow hexagon and ask: which other blocks can make a bigger copy of themselves using only copies of themselves?

Suggested hour: 0–5 pattern-block launch; 5–20 pattern-block doubles; 20–40 L-trominoes to 16 (and 64 with pre-built blocks); 40–55 tetromino doubles or the sphinx (4–5); 55–60 share which shapes could not double.

## By band

- **K–1:** Pattern-block doubles: triangle, square, blue rhombus, red trapezoid. Try the yellow hexagon and talk about what goes wrong. Then build a big L from four card Ls.
- **2–3:** Build an L of side 4 from four L's of side 2 (16 small Ls), then an L of side 8 (64). How many small Ls each time, and how do you know before building? Which of the five tetrominoes make a double of themselves? Can nine Ls make an L three times as long?
- **4–5:** The sphinx: find how four sphinxes make a double (only one way, with flips; the two-colour card shows the flips). Then the triple with nine. Fold A4 and letter paper in half and compare shapes; explain why √2 is the ratio that works. Look at a large printed chair tiling and find copies at three sizes; story of the hat (draft 125), which never repeats whatever you do.

## Checked facts

In `check_shape_2.py`, `check_week_170()`: exact-cover search finds 1 tiling of the doubled L-tromino and 4 of the tripled; repeated chair splitting gives 4, 16 and 64 unit L-trominoes filling Ls of side 2, 4 and 8; the doubled L-tetromino has 4 tilings, the doubled T- and S-tetrominoes none; the sphinx has 6 unit triangles, its double (24) has exactly 1 tiling, with one piece the same way round as the big sphinx and three flipped, and its triple (54) has 4 tilings; the doubled red trapezoid, green triangle and blue rhombus have 1 tiling each, the doubled hexagon none; 11/8.5 ≈ 1.294 and 8.5/5.5 ≈ 1.545. The history and the chair tiling's nonperiodicity are cited.

## Nearest existing themes

Week 1 (Tiling lab) fills outlines with rhombi and counts colour obstructions; this week fills an enlarged copy of the tile itself. Draft 125 (One tile that never repeats) uses the hat's hierarchy, and Week 76 (Substitution strips) the one-dimensional version of "replace each piece by a pattern of pieces"; the chair tiling is the two-dimensional substitution children can build by hand. Draft 127 (coastlines) and draft 142 (space-filling curves) are other self-similar constructions. Week 26 (Same area, different boundaries) works with tetrominoes; the Week 1 notes (`plans/week-01-undergraduate-notes.md`) suggest the deficient-board L-tromino problem, a close cousin of the rep-4 split. New here: self-replication as the question, flips in the sphinx, and A-paper.

## App connection

Shapes and spaces, next to Rhombus gardens (Week 1). Board: an enlarged outline of a tile and a tray of copies; the child drags, turns and flips tiles to fill it, and a "zoom" button turns each placed tile into its own outline to fill one level down. Puzzles: "Fill the big L with four Ls"; "Fill the big sphinx (you will need to flip)"; "Which of these shapes can fill its own double?" Rhombus gardens' fill engine could carry the square-grid and triangle-grid boards.

## Open questions

- Card-stock sphinx pieces are fiddly; test size (side 4 cm) and whether 2–3 children can do the double before 4–5 material.
- 64 small Ls is a lot of cutting; pre-built 16-blocks taped together may be needed for the third level.
- A printed chair tiling picture is needed for the 4–5 story; check the Bielefeld image licence before printing.
