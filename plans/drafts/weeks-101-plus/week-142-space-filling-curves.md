# Week 142 (draft plan): A path through every point

**Strand:** analysis, with shape (app region "Shapes and spaces"). **Deep-math field:** analysis and topology (continuity, limits of curves), recursion. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Hilbert (Mathematische Annalen, 1891), following Peano's 1890 curve, described a continuous map from a time interval [0, 1] onto the whole unit square: a path whose limit passes through every point of the square. Stage n is a path through a grid of 4^n cells, visiting each cell exactly once with unit steps from the bottom-left cell to the bottom-right cell. Stage n + 1 is four copies of stage n, one per quarter of the square, with the two bottom copies reflected in a diagonal so the ends meet, joined by three short bridges; equivalently, an L-system turning rule draws it. The key property is nesting: the cell visited at step i of stage n + 1 lies inside the cell visited at step ⌊i/4⌋ of stage n. So writing a time t in base 4 picks a quarter of the square, then a quarter of that quarter, and so on, and these nested squares shrink to one point H(t); every point of the square arises this way, so the limit curve is onto. Nearby times stay nearby: times within 4^(−n) lie in the same or neighbouring stage-n cells, which gives continuity (in fact distance at most a constant times the square root of the time difference). The converse fails: neighbouring places can be visited at very different times, and the limit curve is not one-to-one. For example, the midpoint of the bottom edge lies in both the first quarter (times 0 to 1/4) and the last quarter (times 3/4 to 1), and the curve covers each quarter completely in its quarter of time, so it passes through that point at two different times. This is forced: Netto's theorem (1878, with later corrections) says no continuous one-to-one map takes an interval onto a square. Stage n has 4^n − 1 steps of length 2^(−n), so the drawn paths grow without bound in length (3/2, 15/4, 63/8, …) while the limit is one well-defined curve. The ordering by Hilbert curve is used to store spatial data so that nearby points tend to be near each other in the list. Children can discover the copy-and-join rule, that every stage visits every cell once, that cell numbers that are close are close in the square but not the other way round, and in grades 4–5 why the stages settle down to a curve.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Ueber die stetige Abbildung einer Line auf ein Flächenstück](https://link.springer.com/doi/10.1007/BF01199431). David Hilbert, Mathematische Annalen 38 (1891), 459–460. Bibliographic record of the original paper (read November 3, 2026).
- [Area-filling curves](https://pdf.arxiv.org/pdf/2112.00691). Maria Chiara Nasso and Aljoša Volčič, arXiv 2112.00691, December 2021. Peano's 1890 analytic curve and Hilbert's pictures, both continuous maps of [0, 1] onto [0, 1]², and that such curves cannot be injective by Netto's result (read November 3, 2026).
- [Analysis of the Clustering Properties of Hilbert Space-filling Curve](https://drum.lib.umd.edu/handle/1903/804). Bongki Moon, H. V. Jagadish, Christos Faloutsos, Joel Saltz, University of Maryland technical report, 1998. Hilbert ordering for mapping multidimensional data to one dimension so that nearby objects stay near in the list (read November 3, 2026).
- [Netto's theorem](https://en.wikipedia.org/wiki/Netto%27s_theorem). Wikipedia, used only as a secondary pointer for the statement that no continuous bijection joins an interval and a square, and the 1878–1879 history (read November 3, 2026).
- Prior use with children: [Worksheet 7: Space-filling curves](https://www.cs.ox.ac.uk/geomlab/sheet7.html). GeomLab, Oxford Computer Science, a school programming resource: build Hilbert stages 1 to 3 from bend and straight tiles and ask whether stage 10 deserves the name space-filling (read November 3, 2026). No K–5 math-circle handout was found (searched math circle and classroom pages for Hilbert curve drawing).

## A kid-friendly way in

Materials: a floor grid of 4 × 4 squares in masking tape (about 40 cm squares), grid paper with 2 × 2, 4 × 4 and 8 × 8 boards, tracing paper or printed stage-1 and stage-2 cut-outs, coloured pencils, and numbered sticky dots 0–15. Prep: tape the floor grid and print boards, about 20 minutes. Launch (3 minutes): on a 2 × 2 board, draw the "cup" path through the four squares from bottom-left to bottom-right; then one child walks the stage-2 path on the floor grid while others call out the step numbers, and the group checks every square was stepped on exactly once.

Suggested hour: 0–5 launch; 5–25 floor walks and drawing stage 2 from four cups; 25–45 band questions, stage 3 on the 8 × 8 board for older children; 45–60 numbered-cell detective work.

## By band

- **K–1:** Walk the floor path, putting a sticky dot on each square as you step on it; then invent your own path that steps on every square once with no diagonal steps. Sort paths that end at a corner from those that do not.
- **2–3:** Make stage 2 from four stage-1 cups: place four cut-out cups in the four quarters of a 4 × 4 board, turn them so that three short bridges join them into one path from bottom-left to bottom-right, and draw it. Then do the same with four stage-2 drawings on the 8 × 8 board. How many steps does each stage take?
- **4–5:** Number the 8 × 8 cells along stage 3. Find two cells whose numbers differ by 1 (always side by side) and two side-by-side cells whose numbers are far apart (5 and 58 at the bottom middle). Where does the first quarter of the numbers lie, and the first sixteenth? Use this to explain why the drawings, as the grids get finer, settle down to one curve that reaches every point, and why the bottom-middle point is reached twice.

## Checked facts

- `check_week_142()`: for stages 1 to 6, the standard Hilbert map visits all 4^n cells exactly once in unit steps from (0, 0) to (2^n − 1, 0); four copies plus three bridges and the L-system turning rule (A → +BF−AFA−FB+, B → −AF+BFB+FA−) both reproduce it (the turtle drawing up to a symmetry of the square).
- `check_week_142()`: nesting: the cell at step i of stage n lies in the cell at step ⌊i/4⌋ of stage n − 1, for stages 2 to 6.
- `check_week_142()`: stages 1, 2, 3 have 3, 15, 63 steps; path lengths in a unit square are 3/2, 15/4, 63/8.
- `check_week_142()`: on the 32 × 32 grid, cells k steps apart are at squared distance at most 225/43 · k (under 6k), a discrete form of the square-root continuity estimate.
- `check_week_142()`: on the 8 × 8 grid the bottom cells either side of the middle are steps 5 and 58, and steps 0–15, 16–31, 32–47, 48–63 fill the bottom-left, top-left, top-right and bottom-right quarters.
- Surjectivity, continuity of the limit and non-injectivity are proved in the paragraph above by the nesting argument; Netto's theorem is cited.

## Nearest existing themes

Atlas GA-29 (Cantor set) gives each point an endless L/R address; here an endless base-4 address of a time picks nested squares, the same addressing idea used to build a point instead of remove length. Week 76 (Substitution strips) rewrites letters by a rule, as the L-system does, but for a one-dimensional word. Week 50 (Staircases and lengths) shows close curves with different lengths; here the lengths blow up while the curves converge. Week 80 (Midnight laboratory) is about limits of infinite processes. New here: a curve as a function of time, continuity versus one-to-one, and a recursive drawing rule whose limit fills a square.

## App connection

Region "Shapes and spaces", possible family "Snake through the grid": a child lays copies of a smaller path in the four quarters of a board, rotating them until three bridge tiles connect them into one path through every cell. Puzzle 1: "Turn the four cups so one path visits all 16 cells, starting and ending on the bottom row." Puzzle 2: "Here are two neighbouring cells on the 8 × 8 path; how many steps apart are they?" A tile-rotation or path-drawing family, if one exists, could carry it.

## Open questions

- Is the copy-and-turn step with cut-outs manageable for 2–3, or do they need pre-rotated cut-outs and only the bridges to find?
- Floor grid size: 4 × 4 is walkable; is a stage-3 walk (64 squares) worth a hallway session?
- How much of the limit argument can 4–5 children hold; a reviewer should test whether "first quarter of the numbers stays in one quarter of the board" lands as the key idea.
- Peano's 1890 date is cited only from the reference list of Nasso and Volčič; add a primary record if the guide uses it.
