# Week 57 K–1 draft: mathematical review

Draft checked: `draft/k-1.pdf` (6 pages, Problems 1–7), built from `draft/src/k-1.tex`. I did not use the author's check scripts. My own scripts are in `review-math-check/`:

- `geo.py` models a piece as a square or half in a unit cell. Inside and outline dots come from the sum of piece-corner angles at each dot (360° means inside; more than 0° and less than 360° means outline). Gaps are found by flood fill. Pick's rule is not assumed.
- `enum_halves.py`, `p23.py`, `enum_pieces.py`, `cornerjoin.py` and `p6_p1.py` hold the enumerations.
- `measure2.py` reads dot positions from the PDF's drawing commands.

## Sizes and diagrams: all correct

- **Dot spacing.** On every working board the dots are exactly 20.000 mm apart, measured from the vector paths.
- **Board sizes, all large enough:**
  - p. 1: six boards (2×2, 2×2, 3×2, 3×2, 3×2 and 4×2 dots).
  - pp. 2–3: six 3×4-dot boards each.
  - p. 4: a 5×5-dot board and a 6×5-dot board.
  - p. 5: nine 3×3-dot boards.
  - p. 6: two 5×5-dot boards.
- **Problem 1 shapes.** The six shapes are at actual size with 45° slants (legs 20 mm, bases 40 and 60 mm). The Problem 7 square is 40 mm.

## Each problem, its intended answer, and my check

**Problem 1** (p. 1): "Cover each shape with halves. Then circle the dots on its outline." The shapes are a half, a square, the triangle (0,0),(2,0),(1,1), the parallelogram (0,0),(1,0),(2,1),(1,1), the 2×1 rectangle and the trapezoid (0,0),(3,0),(2,1),(1,1).
- Intended (halves, outline dots): (1,3), (2,4), (2,4), (2,4), (4,6), (4,6). In every case the outline has two more dots than the halves.
- Check: I computed each from the coordinates with doubled area and gcd edge counts. Each grid shows every vertex and mid-side dot. **Correct.**

**Problem 2** (p. 2): "Make different shapes from three halves, one on each board. Can you make two with different numbers of dots on the outline?"
- Intended answer: no. Every shape has 5.
- Check: there are 4 shapes of three halves if turns and flips count as the same, 6 if mirror images count as different, and 24 if turned copies count too. All have 5 outline dots, none has a gap, and each fits a 2×3-spacing board. **Correct** (see note D on the number of boards).

**Problem 3** (p. 3): "Make different shapes from four halves … Find one with as few dots on its outline as you can."
- Intended answer: the tilted square, with 4 outline dots and 1 inside.
- Check: there are 14 shapes. Thirteen have 6 outline dots and the tilted square has 4. All 14 fit the 3×4-dot board. No four-half shape can have a gap. **Correct.**

**Problem 4** (p. 4): "Can three pieces make a shape with the boxed dot inside? If they can't, explain why."
- Intended answer: no. Each piece fills at most a quarter turn at a dot, and three quarter turns do not go all the way round.
- Check: none of the 16 gap-free shapes made of 1–3 pieces has an inside dot. The angle argument also holds for any arrangement. **Correct** (see note E on the mark).

**Problem 5** (p. 4): "Make a shape with both boxed dots inside, using as few pieces as you can." The two dots are side by side.
- Intended answer: 6 pieces.
- Check: no shape of 5 or fewer pieces has two inside dots. Exactly 7 six-piece shapes enclose two side-by-side dots: the 2×3 rectangle (12 halves of paper) down to the 2-square, 4-half hexagon (8 halves). All fit the 6×5-dot board. By hand: the two cells that touch both dots give each dot at most 180° in total, every other cell gives at most 90°, and 720° are needed, so at least 6 pieces. **Correct.**

**Problem 6** (p. 5): "Make shapes from four pieces with the boxed dot inside, one on each board. How many different shapes can you find?"
- Intended answer: 6, with 4, 5, 6, 6, 7 and 8 halves of paper. Each has as many outline dots as halves.
- Check: exactly 6 four-piece shapes close in a dot, counting turns and flips as the same. Each piece must put a 90° corner on the dot, so every half has its square corner there. **Correct** under that convention (see notes B and C).

**Problem 7** (p. 6): "Make a shape from eight halves with fewer dots on its outline than this square."
- Intended answer: possible. Two shapes give 6 outline dots with 2 inside: the tilted domino and the hexagon (two squares with a roof on each end). Both fit a 5×5-dot board.
- Check: the 1,105 gap-free shapes of eight halves have 10 outline dots (1,038 shapes), 8 (65) or 6 (2). No shape has 7, since outline + 2 × inside = 10 forces an even count. The 11 eight-half shapes with a corner gap have 9 outline dots, so breaking the gap rule gives no false answer. The reference square is drawn correctly: 8 halves, 8 circled dots, centre boxed. **Correct** under the intended reading of the joining rule (see note A).

The half enumeration reproduces the polyabolo counts 1, 3, 4, 14, 30, 107, 318, 1116. The relation outline + 2 × inside = halves + 2 holds for every gap-free shape of one to eight halves.

## Problems found

### A. The joining rule either rules out the intended shapes or allows a false answer to Problem 7 (p. 1 shared rules; p. 6 Problem 7)

Text (p. 1): "Pieces touch side to side, and no gap is left inside a shape."

- **Strict reading** (any two pieces that touch must share a side). This forbids the shapes the packet depends on:
  - in the tilted square, opposite halves meet only at the centre dot;
  - in the launch's 2×2 square, diagonal squares meet only at the centre;
  - in all six Problem 6 shapes, opposite pieces meet only at the boxed dot.
- **Weak reading** (every piece shares a side with some other piece). This allows two tilted squares placed tip to tip: centres two spacings apart, touching at one dot.
  - That arrangement uses 8 halves and has 7 outline dots, 2 inside dots and no gap (`p6_p1.py`).
  - It is fewer than the square's 8, so it answers Problem 7 without closing in two dots in one connected shape.
  - It also breaks the relation the quick pair is meant to see: 7 + 2·2 = 11, not 8 + 2 = 10.
  - `cornerjoin.py` checks every split of eight halves into two side-connected groups that meet at a dot. This is the only one with fewer than 8 outline dots. The others have at least 9.
- **Problems 2–6 are unaffected under either reading:**
  - Problem 2: three halves cannot split into groups of two or more, so a half meeting the rest only at a corner breaks both readings.
  - Problem 3: groups meeting at a dot give 7 outline dots, which is more than 4.
  - Problems 4–5: the angle bounds do not depend on how the pieces join.
  - Problem 6: all four pieces always join along sides.

Smallest fix: replace the sentence with "Pieces join along sides into one shape, with no gap inside." Two tilted squares meeting at a single dot are then two shapes. The tilted square and the 2×2 square stay legal, because each piece is joined along sides to the rest.

### B. Problem 6's count depends on whether turned shapes count as the same (p. 5)

Text: "How many different shapes can you find?" The page has nine 3×3-dot boards with the centre dot boxed.

- There are 6 shapes if turned shapes count as the same. Flips change nothing here: 6 either way.
- There are 16 placements on the fixed board if a turned copy counts as new. Each of the four cells around the dot can hold a square or a half with its square corner at the dot, and 2^4 = 16 (`p6_p1.py`).
- On a fixed board with a fixed boxed dot, K–1 children will naturally treat a turned copy as different. They then need more than the nine boards, and the answer no longer matches the intended 6.
- The workflow has no facilitator guide, so the adult has no source for the convention.

Smallest fix: add "A turned shape counts as the same." to Problem 6.

### C. Problem 6's halves record is undefined when a shape uses squares (p. 5)

Diagram: under each board, a half icon with a blank, then a circle icon with a blank. In Problem 1 the half count is literal, because every shape is covered with halves. In Problem 6 most shapes use squares, and the page never says how to count them.

- **Square counts as two halves** (intended): halves 4, 5, 6, 6, 7, 8 against outline dots 4, 5, 6, 6, 7, 8. Outline equals halves, which is kernel 2's pattern.
- **Half pieces counted literally:** halves 4, 3, 2, 2, 1, 0 against outline dots 4, 5, 6, 6, 7, 8. This gives outline = 8 − half pieces, which is true but hides the intended pattern.

Smallest fix: state the launch fact once in the shared rules on p. 1, "A square counts as two halves." Alternatively, put the same words in Problem 6, or give its record row a square icon marked "= 2" beside the half icon.

### D. Problem 2's six boards ask for six different shapes, which exist only if mirror images count (p. 2)

Text: "Make different shapes from three halves, one on each board." There are six boards.

- 4 shapes exist if turns and flips are the same. This is the convention used in the outline's own counts.
- 6 exist if mirror images are different, and 24 if turned copies are different too.
- An adult who says "that's the same, just flipped" leaves the child unable to fill the boards with different shapes. Every case has 5 outline dots, so the main question is unaffected.

Smallest fix: no change to the mathematics. Either add "A flipped shape counts as new." or make the sixth board extra workspace (for example, five boards). Low priority.

### E. Problem 4 pre-prints the "inside" mark on a dot that can never be inside (p. 4)

Diagram: the centre dot of the 5×5 board is printed with a box. The shared rules and the launch use the box to mean "this dot is inside." The correct outcome of Problem 4 is that the dot is never inside. After any three-piece attempt around it, it is an outline dot that the rules say to circle, so the child would mark a boxed dot with a circle. Problems 5 and 6 do not have this conflict, because there the boxed dots end up inside.

Smallest fix: mark target dots in Problems 4–6 with a sign of their own, for example a star or a larger hollow ring, and keep the box for the children's own inside marks. Alternatively, change only Problem 4's mark. Low priority.

### F. The two Problem 7 boards sit 12 mm apart, less than one dot spacing (p. 6, physical)

Measured from the PDF: the left board's dot columns are at x = 22–102 mm and the right board's at 114–194 mm. The facing columns are 12 mm apart, so the two boards read as one row of dots with an off-lattice gap. Only the frames, 3.2 mm apart, separate them. No answer depends on this, because both six-dot shapes fit inside one board. Smallest fix: widen the gap. The text width allows about 18 mm between the facing columns.

## Verdict

All seven problems are mathematically sound under their intended readings. Every intended answer is confirmed by enumeration, and every diagram matches its text and is correctly scaled. Before printing, fix A, B and C: each lets a reasonable reading of the page change an answer or hide the intended pattern. D, E and F are minor.
