# Week 197 (draft plan): Star patterns from crossing lines

**Strand:** symmetry (Patterns and symmetry). **Deep-math field:** Euclidean geometry and symmetry groups (star polygons, wallpaper symmetry, the crystallographic restriction). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

E. H. Hankin's "polygons in contact" method, as Craig Kaplan (Graphics Interface 2005) implements it, makes an Islamic-style star pattern from a plain tiling: at the midpoint of every edge draw two rays crossing like an X, each at the same contact angle θ to the edge, extend each ray until it meets another, then erase the tiling. One fact explains what appears inside a regular polygon. In a regular n-gon the line through edge midpoint M_i at contact angle θ = 180°·k/n passes exactly through the midpoint M_{i+k}, so the rays lie on the chords M_i M_{i+k}, and the motif is the outline of the star polygon {n/k} drawn on the edge midpoints. For the octagons of the octagon-and-square tiling (4.8.8), the contact angles 22.5°, 45° and 67.5° that Kaplan's figures use give {8/1} (an octagon), {8/2} (two overlapping squares) and {8/3} (an eight-pointed star); for hexagons, 60° gives {6/2}, the six-pointed star of two triangles. A star {n/k} falls into gcd(n, k) separate pieces, and a regular one has 2n symmetries (n turns and n mirrors). Because every X is mirror-symmetric, every symmetry of the starting tiling carries the line pattern to itself. Here the local and global symmetry differ: an eight-pointed star alone keeps eighth turns, but the whole 4.8.8 pattern keeps only quarter turns about the star's centre, as the crystallographic restriction (draft 115) says it must: no wallpaper pattern has a 5-, 8- or 12-fold turn. On a square grid drawn on dot paper, contact angles come from dot steps: in a 6-by-6 cell, rays "1 across, 2 up" (about 63.4°) meet at dots 2 from each corner, making four-pointed stars inside the cells and equilateral eight-sided shapes (all sides √5) round the grid corners; "2 across, 1 up" (about 26.6°) swaps which shape is the star; "1 across, 1 up" (45°) gives a tilted square grid. Each of these patterns keeps quarter turns and mirrors but no eighth turn (checked on a patch). Status: the midpoint fact is elementary geometry, proved by an angle chase and checked numerically here; the 17 wallpaper groups and the restriction are proved theorems (cited in draft 115). Hankin's method is a construction, not a historical finding: these sources do not settle how medieval designers worked, and Bodner (2008) notes that traditional builders used a compass, straightedge and set square and memorised repeat units. Children can discover that changing one angle turns a grid into stars, that stars swap places at complementary angles, and that a pattern can hold stars with more symmetry than it has itself.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Islamic Star Patterns from Polygons in Contact](https://cs.uwaterloo.ca/~csk/publications/Papers/kaplan_2005.pdf). Craig S. Kaplan, Proceedings of Graphics Interface 2005, 177–185 (venue confirmed on the [GI proceedings page](https://graphicsinterface.org/proceedings/gi2005/gi2005-22)). Hankin's method (an X through each edge midpoint, rays extended until they meet), the contact angle, and figures for 4.8.8 at 22.5°, 45° and 67.5°, 4.6.12 and 3.12.12 (read November 4, 2026).
- [Islamic Star Patterns](https://cs.uwaterloo.ca/~csk/other/starpatterns/). Craig S. Kaplan, project page, University of Waterloo. Hankin's method controlled by the single contact-angle parameter; parquet deformations made by varying it across the plane (read November 4, 2026).
- [Hankin's 'Polygons in Contact' Grid Method for Recreating a Decagonal Star Polygon Design](https://archive.bridgesmathart.org/2008/bridges2008-21.html). B. Lynn Bodner, Bridges Leeuwarden 2008, 21–28. Abstract only: the method applied to one decagonal design; traditional tools and memorised repeat units (read November 4, 2026).
- Prior use with children: [Geometric Design in Islamic Art](https://www.metmuseum.org/learn/educators/lesson-plans/geometric-design-in-islamic-art). The Metropolitan Museum of Art lesson plan, adapted from a lesson by Michael Wilkinson (2012), middle and high school. Students construct regular polygons and stars with compass and straightedge and compare methods (read November 4, 2026). No K–5 source for Hankin's method was found (searched NRICH and lesson sites for Islamic star patterns on grids).

## A kid-friendly way in

Draw an X at the middle of every side of a grid, keep each line going until it bumps into another, then erase the grid. Materials: square dot paper with a 6-by-6-dot cell outlined faintly, a printed octagon-and-square (4.8.8) template, rulers, coloured pencils, tracing paper, two paper squares per child and a small mirror. Prep: print sheets and cut squares, about 15 minutes. Launch (2 to 3 minutes): on a big dot grid, the facilitator draws the "1 across, 2 up" X at one midpoint and extends both rays until they meet their neighbours, so everyone sees one legal stroke and one meeting; then the pattern is theirs to finish.

## By band

- **K–1:** lay one paper square on another and turn it until the corners make an eight-pointed star; glue it. Find every place a mirror can stand so the star looks whole (8). Then finish a dot-grid sheet where every X is already started: extend each line to where it bumps, and colour the stars. Little reading.
- **2–3:** the dot-grid rules. Draw the pattern with "1 across, 2 up", with "2 across, 1 up" and with "1 across, 1 up" in the same size cells. What shapes appear, and where do the stars sit? Can you invent a rule that puts stars at both kinds of place?
- **4–5:** on a large regular octagon with its 8 edge midpoints marked, join each midpoint to the one 1, 2 or 3 steps round; compare with Hankin rays at 22.5°, 45° and 67.5° (supplied as angle strips). Then build the star pattern on the 4.8.8 template and hunt its symmetries with tracing paper: the eight-pointed star turns by an eighth, the whole pattern does not. Why not? (A turn that keeps the pattern must carry one octagon centre to another; draft 115's argument shows no pattern keeps an eighth turn.)

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_197()`:

- in regular 5-, 6-, 8-, 10- and 12-gons, the Hankin line at contact angle 180°·k/n through M_i passes through M_{i+k}; at 50° in the octagon it hits no other midpoint;
- {8/2} and {6/2} have 2 pieces, {8/3} and {5/2} one, and in general gcd(n, k) pieces (n up to 12); {8/3} and {8/2} have 16 symmetries, {6/2} has 12;
- in a 6-by-6 cell, "1 across, 2 up" rays meet at (2, 2), "2 across, 1 up" at (1, 1), and "1 across, 1 up" at (1.5, 1.5) on the line joining the midpoints; every drawn segment of the first two rules has length √5;
- with the steep rule the corner shape is convex and the cell shape a four-pointed star; the shallow rule swaps them;
- both dot-grid patterns are unchanged by quarter turns about a cell centre and a grid corner and by mirrors, and changed by an eighth turn;
- an eighth turn about an octagon centre of 4.8.8 sends the neighbouring centre (1 + √2, 0) off the lattice of centres.

Cited, not computed: the 17 wallpaper groups and the crystallographic restriction (draft 115).

## Nearest existing themes

Week 4 (Stars and wheels) already draws star polygons {n/k} by hopping round dots and finds the gcd(n, k) pieces, so the stars themselves are not new. Draft 115 (wallpaper patterns) classifies the symmetry of repeating patterns and proves the crystallographic restriction; Week 35 (footprint borders) does strips; draft 116 (kaleidoscopes) builds dihedral symmetry from mirrors; Week 1 supplies tilings. New here: a construction that turns any tiling into a star pattern with one parameter, the contact-angle-to-{n/k} fact, stars swapping places at complementary angles, and a concrete clash between a motif's symmetry and the pattern's. Honest overlap: this could run as a return visit for draft 115 or Week 4 rather than a separate theme.

## App connection

Patterns and symmetry. A "Star lattice" family: choose a tiling and drag a contact-angle dial (or pick a dot step); the board draws the X's and extends them. Puzzles: "Make four-pointed stars sit on the grid corners"; "Which angle made this pattern?"; "Tap every turn centre of the whole pattern" (stars' centres count only as quarter-turn centres). It could share draft 115's symmetry-hunting tools.

## Open questions

- Can K–1 children extend lines with a ruler until they bump, or should the K–1 sheet print the full lines lightly to trace?
- Angle strips for 22.5° and 67.5° need testing; the midpoint-joining version may be enough for 4–5.
- Cultural framing: name the tradition accurately and avoid claiming how historical designers worked; ask a reviewer with knowledge of the art history.
