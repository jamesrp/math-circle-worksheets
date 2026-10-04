# Independent review: Week 26 draft

## Verdict

A strong, mathematically substantial draft that largely follows the organizer's unusually strict page standard. All three PDFs have six US Letter pages. I independently rendered and looked at every page, read the generated sources and builder, and independently checked the finite mathematics. I found no clipped/overlapping text, incorrect supplied tile counts, or impossible construction that is mistakenly stated to be possible.

I recommend one targeted revision before finalizing: make K–1 Problem 6's exhaustive-search request precise and give it enough recording space. There is also an important hole-convention trap in Grades 4–5 Problem 2 that the author should explicitly verify, plus a minor print-margin risk.

The review did not edit any draft file or rerun the authoring workflow.

## Findings, in priority order

### 1. K–1, page 6 / Problem 6: “Find every move that works” is ambiguous and badly mismatched to the space

The task reads: “Move one tile in each shape to make its boundary as short as you can. Find every move that works.” There is one blank grid for each starting shape.

The three starts have genuinely contrasting outcomes, which is good. Their original boundaries are all 14, and their best one-move boundaries are respectively **14, 10, and 12**. In particular, the straight six-tile row cannot be shortened at all by relocating one tile. That is a worthwhile impossibility result, not a mathematical error.

The problem is the combination of that case with “every move.” For the row, every legal relocation is optimal. With the starting cells fixed at coordinates (0,0) through (5,0), excluding putting a tile straight back where it came from, there are **22** legal optimal relocations. These give **four** resulting shapes up to turns, flips, and translation, including a translated straight row; there are still three genuinely changed resulting shapes if the original shape is excluded. The middle start has one optimal relocation; the bottom start has two, producing two different shapes.

Consequently:

- It is unclear whether children should find distinct source/destination moves or distinct resulting shapes. The packet's turns/flips convention defines sameness of shapes, not sameness of moves.
- “Works” may be heard as “makes it shorter,” leading to “none” for the first case, while the stated optimization goal permits all 22 moves.
- One recording grid per case does not support the requested exhaustive result even when equivalent resulting shapes are combined.

**Revision needed:** Decide whether this is an optimization/impossibility task or an exhaustive classification task. If keeping the first, ask for one best result from each start and ask which starts can actually be shortened; the current space then suffices. If keeping the second, ask for different resulting shapes rather than every move, clarify whether a result congruent to the starting shape counts, and provide multiple recording copies. Keep the straight-row case: it carries real mathematics.

### 2. Grades 4–5, page 2 / Problem 2: the maximum-boundary hole question has the subtle answer **yes** under the stated rules

“Can it have a hole?” must not be answered “no” on the assumption that every hole forces a cycle in the edge-adjacency graph. Incidental corner contacts are permitted for an otherwise edge-connected polyomino. They can seal a hole without adding a shared edge.

A concrete maximum-boundary twelve-tile counterexample is:

```text
.##.....
#.#.....
########
```

Each `#` is a tile. The center empty cell is surrounded on all four sides. The other empty cell diagonally above-left is exterior; the two enclosing tiles meet at a point between the two empty cells. The shape is edge-connected, has 12 tiles and 11 shared edges, and therefore has boundary **26**, the maximum. Four of those boundary edges surround the hole. The edge-adjacency graph is a tree.

This does **not** make the printed question wrong. It is a valuable, unexpectedly rich question if intentional. But it is a high-risk interpretation point in an unpiloted session, especially with no separate facilitator guide. The correct answer to the preceding 2-by-2-block question is **no**: a 2-by-2 block really does force an adjacency cycle.

**Author check:** Preserve the hole question only with the intended “yes” answer understood. Do not revise it into an asserted impossibility. If “hole” is intended to exclude a point-sealed opening, the current rules do not say that; this would need an additional convention. Regardless of the name given to that empty cell, incidental corner contacts remain allowed and are important in Grades 2–3 Problem 6.

A related positive check: Grades 2–3 Problem 6 requires only **7**, not 8, starting tiles to reduce the boundary by 4. The author's checked value of 7 is correct for exactly this reason: a 3-by-3 frame missing its center and one corner is connected and touches the center position on all four sides.

### 3. All pages: footer is close to the physical print boundary

The footer text box ends approximately **5.3 mm above the bottom edge** of the Letter page; the page-number box ends about 5.7 mm above it. Nothing is cut off in the PDF, but this is inside a conservative quarter-inch/6.35 mm printer margin. Since printing is expressly at 100%, “fit to page” should not be relied on to rescue it.

**Low-priority fix:** Raise the footer and page number a few millimeters, or test the actual printer at 100%. This is a physical printing risk, not observed clipping in the rendered files.

## Page-by-page checks

| Packet / page | Independent assessment |
|---|---|
| K–1 / 1 | Four-tile classification is concrete and substantial. There are five free shapes: one with boundary 8 and four with boundary 10. The six recording grids do not force an incorrect sixth answer because the task does not require filling all of them. |
| K–1 / 2 | The extrema for 5 tiles are 10 and 12; for 6 tiles, 10 and 14. Good contrast: increasing area need not increase the minimum. Both straight-row maxima fit the recording grids. |
| K–1 / 3 | The extrema for 7 tiles are 12 and 16; for 8 tiles, 12 and 18. Seven tiles correctly admit a nonrectangular minimum. Both long rows fit. |
| K–1 / 4 | Boundary 10 has only one six-tile shape up to turns/flips; boundaries 12 and 14 each have multiple shapes. The “which numbers” wording correctly permits the second 10-side grid to remain unused. |
| K–1 / 5 | With five tiles, exactly 10 and 12 among the displayed lengths 8–13 are possible. This asks for real impossibility reasoning, not merely counting. |
| K–1 / 6 | Correct contrasting starts and optimal boundaries 14, 10, 12. Revise the exhaustive-search language and space as described above. |
| Grades 2–3 / 1 | Eight tiles have two noncongruent minimum-boundary shapes, so the request for a second shortest shape is feasible. The minimum is 12 and the maximum is 18. |
| Grades 2–3 / 2 | The row admits only change +2; the stair admits 0 and +2; the five-tile U admits −2 and +2; the eight-tile frame admits −4 and +2. All starts are edge-connected. The surplus second recording box beside the row is not a mathematical error. |
| Grades 2–3 / 3 | For ten tiles, shared-side counts 9, 10, 11, 12, 13 are all attainable, with boundaries 22, 20, 18, 16, 14. The rule follows concrete addition experiments and is not printed as a hint. |
| Grades 2–3 / 4 | Maximum boundaries are 10, 16, 22, 26 for 4, 7, 10, 12 tiles. The 14-column recording grids accommodate the straight-row witnesses. The explanation is the mathematical point here. |
| Grades 2–3 / 5 | All four supplied shapes have eight tiles. Their boundaries, in reading order, are 18, 18, 12, 16. The first two are maximal. Additional maximal shapes without any four-in-a-row or four-in-a-column are possible. |
| Grades 2–3 / 6 | Minimum starting counts for changes +2, 0, −2, −4 are 1, 3, 5, 7. Good late problem: merely copying the eight-tile frame from page 2 does not solve the minimization. |
| Grades 4–5 / 1 | Correct minimum targets: 12, 14, 16 for 7, 10, 13 tiles. Noncongruent attaining shapes exist in all three cases. The wording permits children to investigate without giving the answers. |
| Grades 4–5 / 2 | Maximum 26 is correct; nonstraight attaining shapes exist. A 2-by-2 block is impossible in a maximum; a hole is possible under the stated rules. See the important distinction above. |
| Grades 4–5 / 3 | Supplied shapes have (rows, columns, boundary) = (2,6,16), (3,4,14), (4,5,18), each with twelve tiles. Two twelve-tile shapes occupying four rows and five columns can have boundaries 18 and 20. The minimum for those spans is 18, attained whether or not “twelve tiles” is carried into the final sentence. |
| Grades 4–5 / 4 | Maximum areas for boundary 12, 14, 16, 18 are 9, 12, 16, 20, all within the 24-tile stock. This gives concrete evidence for balancing dimensions without supplying the method. |
| Grades 4–5 / 5 | Minimum boundaries for 12, 13, 17, 20, 21 tiles are 14, 16, 18, 18, 20. The 17/20/21 progression supports the intended thresholds. All counts fit the stated materials. |
| Grades 4–5 / 6 | Minimum boundaries for 37, 50, 73 squares are 26, 30, 36. Attaining shapes fit the 11-by-10 drawing grids. “Squares” and “draw” appropriately move beyond the physical stock of 24 tiles. The maximum-area rule for an even boundary B is the product of the two integers nearest B/4, equivalently floor(B²/16). |

## Fit to the organizer's standard

- **Format:** All 18 pages have the prescribed one-line header, numbered “Problem N:” label, and packet-specific footer/page number. No extra activity headings, mascots, praise, exclamations, or lesson narration were found.
- **Language and independence:** K–1 problems each remain within two sentences. The oldest band's proof requests concern genuine optimality or impossibility. The middle band's shared-side definition follows the use of shared contacts in concrete experiments. No worked answer or general perimeter formula is given away.
- **Depth:** Six pages per band provide a credible surplus for forty minutes. K–1 receives classification, optimization, multiple solutions, impossibility, and local moves. It is not reduced to a short counting exercise. Pages 2–3 repeat the extremal format, but with meaningful changes of tile count and nonrectangular minima.
- **Concrete support:** Starting positions are supplied whenever a move or addition depends on them. Free-construction tasks specify exact tile counts. The diagrams and grids are clean and readable. The longest-row tasks are not silently truncated by narrow grids.
- **Physical scale:** The worksheet grids are schematic recording grids, roughly 5.5–11 mm per cell; they are not 20 mm tile mats. That is workable with the separate matching work mats and table space required in the brief. They should not be treated as the promised physical tile grid.
- **Layout:** No overlaps, off-page objects, malformed minus signs, or broken grids appeared in the rendered pages. There is ample drawing space for most tasks. The notable exception is the “every move” request in K–1 Problem 6; the footer margin is the only broad print-production concern.

## Verification record

- Rendered the delivered PDFs afresh at 90 dpi into `critic-render/` and visually inspected all six pages of each packet.
- Confirmed 612 × 792 point Letter size and six pages per PDF.
- Read the exact TeX and `build_packets.py` after looking at the pages; checked that supplied positions, grid dimensions, and text matched the PDFs.
- Ran a separate enumeration, without importing the author's checking code, of free polyominoes through ten squares: counts 1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655. Checked perimeter distributions, attainable shared-edge counts, and minimum tile counts for all four addition changes.
- Exhaustively checked the legal one-tile relocations of each K–1 Problem 6 start.
- Independently computed integer row/column lower bounds for all larger minimum-boundary tasks and checked explicit maximum-boundary/hole and no-four-in-a-line witnesses.

The review script is `critic-check.py`. No draft changes were made.
