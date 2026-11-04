# Week 198 (draft plan): Nibble a tile

**Strand:** symmetry and shape (Patterns and symmetry). **Deep-math field:** tilings and combinatorics on words (tiling by translation, boundary factorizations, the Conway criterion). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The "Escher method" starts with a square, cuts a nibble from one side and glues it to the opposite side moved straight across (no turning, no flipping). The new tile still covers the floor by sliding copies, because opposite sides still match. The same works for a hexagon with three pairs of opposite sides. Beauquier and Nivat (Discrete & Computational Geometry, 1991) proved this is the whole story for polyominoes (shapes made of grid squares, with no holes): such a shape tiles the plane by translations alone exactly when its boundary, read as a word of steps right, up, left and down, splits into A B C Â B̂ Ĉ, where Â is the piece A walked backwards (the matching opposite side) and at most one of A, B, C is empty. With one empty piece the shape is a pseudo-square (two pairs of matching opposite sides), otherwise a pseudo-hexagon (three pairs). Blondin Massé, Brlek and Labbé (2010) note that the factorization need not be unique and trace the question to Wijshoff and van Leeuwen (1984), who named such tiles exact polyominoes. Turning copies gives more tiles. The Conway criterion (made public by Martin Gardner in 1975; treated by Doris Schattschneider in 1980) says a disk tiles the plane if its boundary has six points A to F with the part AB matched to ED by a slide and the four other parts each centrally symmetric (unchanged by a half-turn about its own midpoint). The tiling uses slides and half-turns. It is sufficient, not necessary. In nibble language: nibble half of one side and spin the nibble about that side's midpoint onto the other half. Checked here by two methods (the boundary factorization, and a direct search for a tiling by the copies of a lattice; they agree on every polyomino up to 6 squares): all 5 tetrominoes tile by translation alone, 9 of the 12 pentominoes do (not F, T or U), and 24 of the 35 hexominoes. On a 4-by-4 square, a one-square nibble from the top edge stuck anywhere along the bottom edge still tiles by sliding (if it is not directly below, the rows slide sideways), but stuck on a side it never does; an L-shaped nibble slid across tiles, while the same nibble flipped over does not. Proved: Beauquier–Nivat and the Conway criterion (cited). Checked: the counts and examples. Limits: Beauquier–Nivat is stated for polyominoes; tiling with turns and flips allowed is a different, harder question (compare draft 125's hat). Children can discover that a nibble must move straight across, that a bump may slide along the opposite side, and which pentominoes need turning.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [On Translating One Polyomino To Tile the Plane](https://eudml.org/doc/131174). D. Beauquier and M. Nivat, Discrete & Computational Geometry 6, 1991, 575–592. Record page (title, authors, journal, pages); the theorem's statement is taken from the next source (read November 4, 2026).
- [Combinatorial aspects of Escher tilings](https://dmtcs.episciences.org/2868/pdf). A. Blondin Massé, S. Brlek and S. Labbé, FPSAC 2010, DMTCS proc. AN, 533–544. The Beauquier–Nivat factorization A·B·C·Ā·B̄·C̄ with at most one empty factor, pseudo-squares and pseudo-hexagons, non-uniqueness, Wijshoff and van Leeuwen (1984), recognition algorithms (read November 4, 2026).
- [Conway criterion](https://en.wikipedia.org/wiki/Conway_criterion). Wikipedia, as a secondary pointer. The six-point statement, sufficient but not necessary, tilings by half-turns, Gardner's 1975 column and Schattschneider's 1980 article (read November 4, 2026).
- [A Mathematica GUI for Generating Conway Tiles](https://archive.bridgesmathart.org/2012/bridges2012-397.pdf). Bruce Torrence, Bridges 2012. The criterion with one translated pair and four centro-symmetric parts; Escher-like tiles; cites Schattschneider, "Will It Tile? Try the Conway Criterion!" (Mathematics Magazine, 1980) (read November 4, 2026).
- Prior use with children: [Tessellations 2](https://everydaymath.uchicago.edu/parents/5th-grade/student-gallery/tessellations-2.html). Everyday Mathematics student gallery, grade 5, Normandale Hills Elementary. Students cut a shape from one side of a square and slide it to the opposite side to make Escher-like tessellations (read November 4, 2026).

## A kid-friendly way in

Cut, slide, tape, trace. Each child gets a few card squares (2 inches) and later squared paper; a nibble is cut from one side, slid straight across and taped to the opposite side; the tile is traced, slid and traced again until a patch of floor appears. For the grid version, tiles are cut from 1 cm squared card, so nibbles are whole squares and "does it fit?" is checkable by tracing on squared paper. Prep: cut card squares and print grid sheets and a pentomino sheet, about 20 minutes (a pentomino set saves time). Launch (2 to 3 minutes): the facilitator nibbles one square, slides the nibble across, tapes it, and traces three copies in a row; then flips a second nibble before taping and shows that the row will not close up.

## By band

- **K–1:** make a nibble tile, trace a row and then a row above it, and decorate the tile as a creature. Then try a nibble that was turned or flipped before taping: does the floor still work? Scissors, tape and tracing; no reading.
- **2–3:** on a 4-by-4 grid square, take one square from the top edge. Where can you stick it so the new shape still covers the floor by sliding only (no turning)? Try every spot on the bottom and on the sides. Then: which of the 12 pentominoes cover a floor by sliding alone? The table pools its answers on one sheet.
- **4–5:** write a tile's boundary as an arrow word (right, up, left, down) starting from a corner, and look for opposite pieces that match when walked backwards; does every sliding tile have two or three matching pairs? Then the Conway twist: nibble half of one side and spin the nibble about the side's midpoint onto the other half; why does the floor now need half-turned copies? Extension: can the F, T and U pentominoes cover a floor if turning is allowed? (They can; that every pentomino tiles the plane is a classical fact, not taken from a source read here.)

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_198()`:

- there are 1, 1, 2, 5, 12 and 35 polyominoes of 1 to 6 squares (no holes at these sizes); of these 1, 1, 2, 5, 9 and 24 tile by translation alone;
- for every one of them, the Beauquier–Nivat boundary test and a direct search for a lattice tiling agree;
- the translation pentominoes are I, L, N, P, V, W, X, Y and Z;
- 4-by-4 square: a top nibble at column 2 stuck under any of the four bottom positions tiles; stuck on either side at any height, it does not; an L-shaped three-square nibble slid across tiles, flipped over it does not; two nibbles (top to bottom and left to right) still tile.

Cited, not computed: the theorems of Beauquier and Nivat and of Conway; the history of the criterion.

## Nearest existing themes

Week 1 (Tiling lab) asks whether given blocks fill an outline and uses colour counts as obstructions; Week 26 (Same area, different boundaries) shows a nibble keeps the area and changes the boundary. Draft 115 (wallpaper) is where the symmetry of the finished floor would be named (a sliding tile gives the slides-only type, a Conway tile adds half-turn centres); draft 125 (the hat) is a tile with no periodic floor at all, the extreme contrast; draft 170 (rep-tiles) builds bigger copies from small ones. New here: designing a tile rather than testing given ones, the matching-opposite-sides theorem, and the boundary word as a tool. The Escher-nibble craft is common in schools, so the art activity is familiar; the mathematics (which nibbles work, and why exactly these) is what is new.

## App connection

Shapes and spaces, or Patterns and symmetry. A "Nibble tile" family on a square grid: drag a square off one side and drop it elsewhere; the board tries to fill the floor by sliding copies and shows the first clash. Puzzles: "Put the nibble where the floor still works without turning"; "This tile needs turning: change one square so it slides"; "Which of these four tiles slides?". A new family; it would need a sliding-copies checker.

## Open questions

- Card squares versus grid tiles: does K–1 cutting give clean enough edges for tracing to show a fit or a clash?
- Is the arrow-word boundary (4–5) readable at that age, or should matching opposite pieces be found by tracing and sliding a cut-out side?
- Decide whether the Conway criterion is a student task or a guide-only extension.
