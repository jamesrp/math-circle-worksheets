# Week 126 (draft plan): Cut and rearrange

**Strand:** shape (app region "Shapes and spaces"). **Deep-math field:** geometry, scissors congruence, invariants. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Wallace–Bolyai–Gerwien theorem: any two polygons with the same area can each be cut into the same finite list of polygonal pieces, so one can be cut up and rearranged into the other. Wallace had a proof around 1807 and Bolyai (1832) and Gerwien (1833) proved it independently; accounts of the dates differ slightly. The proof is a chain of moves children can perform: triangulate; turn each triangle into a rectangle (cut off the top at half height and swing it down); turn any rectangle into any other rectangle of the same area (a staircase or "P-slide" cut); and merge two squares into one (a dissection proof of Pythagoras such as Perigal's). Equal area is therefore the only invariant for polygons in the plane under cutting along straight lines. In three dimensions this fails. Hilbert's third problem (1900) asked whether two polyhedra of equal volume are always scissors congruent; Dehn (1901, published around 1901–02) showed that a cube and a regular tetrahedron of equal volume are not. His invariant adds up, over the edges, edge length paired with the dihedral angle modulo rational multiples of π; it is unchanged by cutting and regluing. The cube's angles are all π/2 (contributing nothing), while the tetrahedron's angle arccos(1/3) is not a rational multiple of π, so the invariants differ. Sydler (1965) proved the converse: equal volume and equal Dehn invariant are enough. Limits: the plane theorem needs polygonal pieces moved rigidly (flips allowed); minimal piece counts are mostly unknown in general and are a craft. What children can discover: any shape they make from the same pieces has the same area (counted in grid squares), a rectangle can be reshaped into a different rectangle by a staircase cut, and two squares can be cut and rebuilt as one.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Wallace-Bolyai-Gerwien Theorem](https://www.cut-the-knot.org/do_you_know/Bolyai.shtml) — Cut-the-Knot. Statement, the dating disagreements among Frederickson, Stewart, and Andreescu–Gelca, and the four-step proof outline (triangulate, triangle to rectangle, rectangle to square, two squares to one) (read November 3, 2026).
- [Scissors Congruence](https://math.uchicago.edu/~may/REU2016/REUPapers/Welsh.pdf) — Maeve Coates Welsh, University of Chicago REU paper, 2016. Dehn invariant definition; a unit cube and a regular unit tetrahedron are not scissors congruent; Sydler's converse (read November 3, 2026).
- Prior use with children: [UW Math Circle, Week 14: Dissections](https://sites.math.washington.edu/~mathcircle/circle/archive/2024-25/files/25wi-week14.pdf) — University of Washington Math Circle handout, winter 2025 (level not stated). Rectangle, parallelogram and two squares into one square; 5 × 8 into 4 × 10 with fewest pieces; P-slides (read November 3, 2026).
- Prior use with children: [Dissections and Decompositions](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2015/lecture/BMC%20Handout%202_16_16-2.pdf) — Laura Pierson, Berkeley Math Circle handout, February 2016. Pythagoras by dissection, Bolyai–Gerwien (Problem 8), Dehn and Hilbert's third problem (Problem 9) (read November 3, 2026).
- [Turn an Equilateral Triangle into a Square](https://cutoutfoldup.com/109-turn-an-equilateral-triangle-into-a-square) — Laszlo C. Bardos, cutoutfoldup.com. Printable letter and A4 pattern for the classical triangle-to-square dissection, with hinges (read November 3, 2026).

## A kid-friendly way in

Materials: squared paper (1 cm), scissors, glue sticks, pre-printed squares and triangles with cut lines for the youngest, a printed triangle-to-square pattern on card for the 4–5 table, and a few paper tetrahedra for a closing demonstration. Prep: about 20 minutes of printing and pre-cutting. Launch (2 minutes): cut a paper square along one diagonal in front of everyone, rearrange the two pieces into a big triangle, and ask "Did the paper get bigger or smaller?"

Suggested hour: 0–5 launch; 5–20 free rearranging of pre-cut squares; 20–45 band challenges on squared paper; 45–55 compare piece counts and show the best solutions; 55–60 tetrahedra-around-an-edge demonstration.

## By band

- **K–1:** Each child gets a square cut into 2, 3 or 4 printed pieces and makes as many different shapes as they can (triangle, rectangle, "house"). Counting grid squares under each shape shows the same total.
- **2–3:** On squared paper: turn a 5 × 8 rectangle into a 4 × 10 rectangle with as few cuts as possible (a two-piece staircase works). Then two equal squares into one square (four triangles). Who can make a 3 × 3 and a 4 × 4 square into one 5 × 5 square?
- **4–5:** The 3 + 4 → 5 challenge with fewest pieces, then a general recipe: any triangle into a rectangle, any rectangle into a square. Closing contrast: five paper tetrahedra around one edge leave a gap while four cubes close up; a facilitator tells the Dehn story as an example of an invariant (no proof expected).

## Checked facts

- `check_week_126()`: the staircase cut (steps 2 across and 1 up) turns 5 × 8 into 4 × 10 with two pieces, checked cell by cell.
- `check_week_126()`: keeping the 4 × 4 whole, the 3 × 3 square can fill the 9-cell L border of the 5 × 5 with 3 grid pieces (an L of five cells and two dominoes), and no cut of the 3 × 3 into two connected grid pieces works (exhaustive search with turns and flips). So 4 pieces in all, among grid-line cuts.
- `check_week_126()`: two unit squares make four half-square triangles, which form a square of side √2; a square cut on its diagonal makes a right isosceles triangle with the same area.
- `check_week_126()`: the regular tetrahedron's dihedral angle is about 70.53°, so five around an edge leave a gap of about 7.36°; four cubes close exactly. Irrationality of arccos(1/3)/π is cited (Welsh), and the script only confirms that no fraction with denominator up to 1000 is within 10⁻⁹.

## Nearest existing themes

Week 93 (Squaring a rectangle) keeps area while reshaping by averaging sides, numerically; Week 32 (Squares inside rectangles) dissects into squares for Euclid's algorithm; Week 57 (Area from dots) uses a cut-and-join additivity lemma; Week 85 (Drawing machines) and atlas AD-18 scale or shear area. New here: equal area as a complete invariant for cut-and-rearrange in the plane, the fewest-pieces craft, and an obstruction in three dimensions (Dehn). Overlap with Week 93 is in theme (rectangle to square) but not in method.

## App connection

"Shapes and spaces". A grid board with a scissors tool that cuts along grid lines and pieces that can be dragged, turned and flipped; puzzles: "make this 5 × 8 into a 4 × 10 with one cut" or "turn these two squares into one square using at most four pieces". Star levels could reward fewer pieces. A polyomino-placement family, if one exists in the app, could carry the rebuild half.

## Open questions

- Is free cutting with scissors too imprecise for 2–3? Grid-line cuts on squared paper may be the honest default; printed cut lines for the triangle-to-square pattern.
- Is the 3 + 4 → 5 challenge reachable in a single session for 2–3, or a 4–5 item only?
- Tetrahedron gap demonstration: is a 7° gap visible with paper models of edge 8 cm? Needs a home trial.
- Decide whether to include the non-grid Perigal dissection as a printed puzzle for 4–5.
