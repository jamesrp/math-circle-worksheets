# Week 106 (Coloring maps), mathematical review of draft/

Reviewer: independent math critic. Sources read: PROMPT.md, draft/k-1.pdf (8 pages), draft/grades-2-5.pdf (12 pages), draft/src/*. Both PDFs were rendered and every page was inspected.

## How it was checked

- **Maps.** I reran the author's raster check (`figs.py check`) on a copy and compared it with the rendered pages by eye. I also re-derived each map's country graph from its construction: where the lines end, which lines are full and which stop, and whether a dangling line separates anything. Every country count and fewest-colors number below matches.
- **Games.** I wrote my own minimax solver for the Painter/Spoiler game, separate from the author's `game.py`. The game ends with a Spoiler win as soon as an uncolored country has all k colors among its neighbors. A move colors any uncolored country with a color that no neighbor has. Results:
  - 4-square strip, 2 colors: the Spoiler wins if the Painter goes first, and the Painter wins if the Spoiler goes first.
  - Ring of 4 around a pond, 2 colors: the same as the strip.
  - 3×3 grid, 3 colors: the Spoiler wins whoever goes first.
  - 3×3 grid, 4 colors: the Painter wins whoever goes first.
- **Seven-country donut.** I wrote my own parser for `figs/d_seven.tex`. It reads the 14 polygons and 14 number labels and checks that each polygon holds exactly one label. The pieces tile the whole 12.5 cm square, with total area 156.25 cm². I rasterized the board with the printed wrap rule (left↔right at the same height, top↔bottom at the same place; the arrows match a torus, not a Klein bottle). Results:
  - Each of the 7 numbers forms one connected country on the donut, so every cut piece is labeled consistently with its partners across the edges.
  - All 21 pairs share a border of about 3 to 5 cm, never just a corner.

## Answers verified (no error found)

**K–1**

| Problem | Maps | Fewest colors / answer |
|---|---|---|
| P1 | two scribble maps | 2 each (7 and 7 countries) |
| P2 | three-circle Venn; self-crossing loop | 2 each (8 and 7 countries) |
| P3 | open drawing | (see note 3) |
| P4 | T, plus, Y, line + loop | 3, 2, 3, 2 |
| P5 | pond rings of 4, 5, 6, 7 | 2, 3, 2, 3 |
| P6 | flowers in printed order 4, 5, 6, 3 petals | 3, 4, 3, 4 |
| P7 | 4-strip, 2 colors, Painter first | **Spoiler** |
| P8 | pond ring of 4, 2 colors, Spoiler first | **Painter** |

**Grades 2–5**

| Problem | Maps | Fewest colors / answer |
|---|---|---|
| P1 | 4 crossing lines (10 countries); 2 circles + line (8); Venn + line (9); self-crossing loop (7) | 2 each |
| P2 | open | No such map exists; parity argument |
| P3 | T, 6-ray star, Y, dangling line, ladder (two stubs on opposite sides), 5-ray star | 3, 2, 3, 2, 3, 3 |
| P4 | lake rings of 4, 5, 6, 7 | 2, 3, 2, 3; ring of 20 → 2; ring of 25 → 3 |
| P5 | middle + ring of 4, 5, 6, 7 | 3, 4, 3, 4; ring of 100 → 3; ring of 101 → 4 |
| P6 | open | 4 all-touching countries are possible; 5 are impossible |
| P7 | labeled wheel of 5 | Needs 4 colors; there are no four mutually touching countries (see below) |
| P8 | open | Every attempt fails (four color theorem) |
| P9 | 3×3, 3 colors | **Spoiler**, both orders |
| P10 | 3×3, 4 colors | **Painter**, both orders |
| P11 | donut stripes of 4, stripes of 3, 4×4 grid, 3×3 grid | 2, 3, 2, 3 |
| P12 | seven-country donut | 7 |
| P13 | open | At most 7 |

- **P7 detail.** Any four countries of the labeled wheel include either F plus three ring countries, or four ring countries. Neither group can be mutually touching in a ring of 5. The answer stays "none" even if a child counts the white outside as a country, because the outside does not touch F.
- **P10 detail.** With 4 colors only the center square has 4 neighbors, so only the center can ever be stuck. The Painter colors it at the first chance.

## Located problems

None of the following changes a printed answer. They are wording and diagram edge cases where a reasonable reading or a freehand drawing could make a task behave differently from what the page assumes.

### 1. Grades 2–5, page 1, Problem 1, bottom-left map (Venn + line, `u_venn_line`): near-tangent line

- **Diagram.** The line passes under the bottom circle with a computed gap of 0.16 cm (1.6 mm) between the curves. The drawn lines are about 0.4 mm thick, so on paper the line looks as if it touches the circle.
- **Effect.**
  - A child may read the two as touching. That splits the region above the line into a left and a right country meeting at a point.
  - A child may read the line as crossing the circle, which creates a sliver country.
  - Either way the map is still made of whole lines and closed loops, so 2 colors still work. The problem stays correct.
  - However, the ambiguous pinch is the only place on this page where a child cannot tell what the countries are, and it falls on the page meant to show that two colors "always work".
- **Smallest fix.** Give at least about 5 mm of clearance. For example, lower the line's middle control points from y≈1.1 to about 0.5. Alternatively, make the line clearly cross the bottom circle twice.

### 2. K–1, page 7, Problem 7 (and page 8, Problem 8): the move rule is not restated

- **Text.** "Take turns coloring one square. … A square that touches both colors is stuck."
- **The issue.** The game's analysis assumes that a square may only get a color its neighbors do not already have. The packet rule at the top of page 1 says so, but Problem 7 does not, and it is read aloud as a separate game. If children play without that rule:
  - a square can be colored to match its neighbor;
  - "stuck" then no longer prevents coloring, and the verified answer (Spoiler wins with the Painter first) no longer applies.
- **Problem 8 wording.** Problem 8 says "Play the same game on these pond maps", but the countries there are not squares.
- **Smallest fix.**
  - Problem 7: "Take turns coloring one square with a color that is not next to it."
  - Problem 8: add "A country next to both colors is stuck." Alternatively, word Problem 7's stuck rule as "a country".

### 3. K–1, page 3, Problem 3: the free drawing can make a map that needs 3 pencils

- **Text.** "In the top box, draw lines that go from one side of the box to another side. … Then color each map with your two thick pencils."
- **Edge case.** With freehand drawing, a five-year-old's line can easily stop where it meets another line instead of at the box side. That makes a "T", the same shape the packet later uses on page 4 as a 3-pencil map. The page asserts two pencils will work, which is false for such a drawing.
- **Smallest fix.** Write "lines that go all the way across the box, from one side to another side". The adult can then check that each line reaches the frame. This is a facilitator point more than a page error.
- **Grades 2–5 Problem 2** carries the same risk, but there it is part of the investigation, so no change is needed.

## Band verdicts

- **K–1.** All maps, counts, fewest-color answers and both game outcomes are correct. Only items 2 and 3 above need attention.
- **Grades 2–5.** All maps, fewest-color answers, the ring and wheel generalizations, the game outcomes, and the seven-country donut are correct. Specifically, the donut has 21 of 21 pairs adjacent, consistent edge labels, and a torus wrap matching the arrows. Only item 1 above needs a diagram adjustment.
