# Week 59 (constant width): math check

Scope: `lowell-math-circle-year-2/week-59/week-59-students.pdf` (W59-S-v2, 6 pp., Problems 1–6), `week-59-materials.pdf` (W59-M-v1, 3 pp.) and `week-59-facilitator.pdf` (W59-F-v1, 8 pp.). The student PDF is one combined packet: pp. 1–2 (Problems 1–2) are headed Grades 2–5, pp. 3–5 (Problems 3–5) Grades 3–5, and p. 6 (Problem 6) Grades 4–5. There is no K–1 page. I also read the editable source in `lowell-math-circle-year-2/source/week-59/` (`student/students.tex`, `materials.tex`, `make_assets.py`, `geometry.py`, `mathematical-notes.md`, `guide/facilitator.tex` and the READMEs) for the nominal coordinates. Checked October 10, 2026. My scripts and outputs are in [checks/week-59/](checks/week-59/).

**Result: every answer, table entry, formula and proof in the packet is correct, and every diagram matches its text. I found 2 minor problems on the student pages, neither of which changes an answer: millimetre labels on drawings printed smaller than the labels say, with no note that they are reduced (pp. 1, 3–6), and a Problem 4 sentence that can be read two ways (p. 4). The materials and the adult guide check out completely.**

## How it was checked

- `w59common.py` reads the delivered PDFs themselves: every vector path (converted with `pdftocairo -svg` and parsed, in millimetres) and every word position (`pdftotext -bbox`). It computes the exact support function of line and cubic Bézier segments, so widths of the printed curves are found from the actual curves, not from control-point boxes. Nothing from the packet's `make_assets.py`, `geometry.py` or `verify_math.py` is used.
- `check_math.py` (`out_check_math.txt`, 98 ok, no FAIL) recomputes the mathematics from exact ideal geometry:
  - the smallest and largest width of all five pieces in 36,000 directions, the nearest-mm readings, and the guide's width formulas for the ellipse, square and triangle;
  - the fixed-gap answers to Problem 2 (a piece fits in an orientation if and only if its width is at most 60, and touches both edges if and only if its width equals 60), including that the square cannot start to turn;
  - the constant-width theorem for exact Reuleaux triangles of sides 60, 40, 7.3 and 123 (rotated and shifted), and each step of the guide's p. 2 proof: the minor arc BC is exactly the part of the circle about A inside both other disks; P = A + wu lies in K for u in the closed A-sector; x·B ≥ |x|²/2 and x·C ≥ |x|²/2 on 20,903 points of K; 0 ≤ x·u ≤ w on K, with both values attained; the sectors and their reversals cover every direction; both contacts are corners at a sector endpoint;
  - three "rounded triangle" variants (outward arcs of radius 45 or 90, and arcs centred on side midpoints), which all have changing width, as the guide's limit statements say;
  - Problem 5's distances from the centroid mark to a supporting line over 36,000 directions, the opposite-sum rule, and the guide's formula d_O(u) = w − R cos(θ − 30°);
  - Problem 6's boundary lengths (exactly and by a 60,000-segment polyline);
  - the convention examples' numbers, and the guide's kit, print and group arithmetic.

  It then reads the guide and student text and checks that each verified number, table row and answer is the one printed.
- `check_diagrams.py` (`out_check_diagrams.txt`, 145 ok, no FAIL) checks every diagram in the delivered PDFs:
  - p. 1: the parallelogram is (0,0), (38,0), (46,32), (8,32) at scale 0.55 in all three panels; both vertical supports touch its extreme corners, so the whole piece lies between them; the perpendicular gap is 25.30 mm on the page, which is 46 at scale 0.55.
  - pp. 1–2: the ten row icons are the right shapes at scale 0.22 in the order disk, oval, square, straight triangle, curved triangle.
  - p. 3: in all three panels DE = DF = 17.5 mm (25 at 0.7) and DE ⟂ DF. The compass legs end at D and E, and arc EF is centred at D with radius DE.
  - p. 4: the tangent line is at distance 12.35 mm from X, which is the radius; the radius to P is perpendicular to the line. Each of the three curved triangles has three 60° arcs, each centred at a labelled corner, with radius equal to the side (33 mm = 0.55 × 60) and joining the other two corners. Each has a compiled width of 33.000 ± 0.002 mm in 3,600 directions. Their AB directions are 7°, 37° and 83°, and A, B, C run counterclockwise in all three, so they are rotations, not reflections.
  - p. 5: the rectangle is 44 × 28 with O at (12, 9) at scale 0.6. The support lies along the right side, and the perpendicular is 19.2 mm on the page (32 at scale 0.6). In the icons, O is the disk's centre and the curved triangle's centroid.
  - p. 6: the disk's radius is 18.9 mm and the generating circle's 37.8 mm (30 and 60 at the same scale, 0.63). The curved triangle has a width of 37.8 mm, and its arcs are centred at its corners. The six dots sit at 0°, 60°, …, 300°. The bold arc on the triangle is centred at A and joins B and C. The bold arc on the circle runs from the 0° dot (B) to the 60° dot (C), in the same orientation. The compiled boundary lengths are equal (188.50 vs 188.52 at full scale; 60π = 188.496).
  - Materials p. 1: the disk has a width of 59.9998–60.0175 mm with O at its centre. The oval is 40.000–60.000 mm wide. The square has sides of 60.000 mm and is 60.000–84.853 mm wide. The triangle has sides of 60.000 mm and is 51.962–60.000 mm wide. Both curved triangles are within 0.0015 mm of 60 in 3,600 directions, with arcs centred at the corners, and the marked one has O at the centroid. The bar is 100.000 mm, and the captions sit under the right pieces.
  - Materials pp. 2–3: the grid has 21 × 21 lines 10 mm apart, spanning 200 × 200 mm, and both bars are 100.000 mm. The templates are equilateral, two with 60.000 mm sides and two with 40.000 mm, with corners labelled A, B, C. The finished curved triangles drawn on the four templates overlap neither each other nor the captions.
  - The guide's two sketches: on p. 2, the curved triangle is exact; P is on arc BC at 30° and AP equals the side; both blue lines are perpendicular to AP and are the extreme lines in that direction. On p. 7, O is the centroid; the supports through C and at the bottom of the lower arc are 60/√3 and 60 − 60/√3 from O, in 60 mm units.

## Grades 2–5 (pp. 1–2, Problems 1–2): correct; item 1 below

- **Convention example (p. 1):** for the parallelogram (0,0), (38,0), (46,32), (8,32), the vertical supports are x = 0 and x = 46, which touch at (0,0) and (46,32). The gap is 46 mm as recorded.
- **P1:** smallest/largest width (nearest mm):
  - disk: 60/60;
  - oval: 40/60 (short and long axes);
  - square: 60/60√2 ≈ 84.85, read as 85 (sides, then diagonal);
  - straight triangle: 30√3 ≈ 51.96, read as 52 (a side and the opposite corner touching)/60 (a side across the gap);
  - curved triangle: 60/60.

  The largest reading is 85, within the 150 mm ruler.
- **P2:** can each piece turn all the way round inside the fixed 60 mm gap, and keep touching both edges throughout?
  - disk: yes, yes;
  - oval: yes, no;
  - square: no, no (every orientation except side-aligned is wider than 60, so it cannot even start to turn);
  - straight triangle: yes, no;
  - curved triangle: yes, yes.

  With translation allowed, centring the piece between the edges gives a continuous full turn for the oval and the triangle. The table has all five pieces, so the page asks for exactly the set it implies.
- Note, not a mathematical error: the disk, oval, triangle and curved triangle all reach width exactly 60, so their "yes" for turning inside holds only with zero clearance. The guide already flags the fixed-gap setup as an untested physical procedure (p. 3, "Do not silently widen the gap").

## Grades 3–5 (pp. 3–5, Problems 3–5): correct; items 1 and 2 below

- **P3:** the predicted widths are 60 and 40. The 40 mm piece is the 60 mm piece scaled by 2/3, and both have constant width.
- **P4:** the intended outcome is the all-direction argument:
  - for directions in each 60° sector, one support passes through a corner and the other touches the opposite arc;
  - both supports are perpendicular to the radius from that corner, so the gap is the radius, 60;
  - the three sectors and their reversals cover every direction.

  This is true, and the three drawings are exact positions of one labelled piece.
- **P5:**
  - disk: 30/30;
  - curved triangle (O at the centroid): smallest 60 − 60/√3 ≈ 25.36 (the middle of an arc touching; reads 25), largest 60/√3 ≈ 34.64 (a corner touching, with the line perpendicular to O-to-corner; reads 35). Opposite distances always sum to 60.

  The answer to "Can a piece have constant width while those distances change?" is yes. The p. 5 example is correct: the support is x = 44, the foot (44, 9), the distance 32; this is not the 44 mm width.

## Grades 4–5 (p. 6, Problem 6): checks out completely

- **P6:** the two boundaries are equal. Each arc is one sixth of the radius-60 circle, so the three arcs make half of it, 60π. The radius-30 disk is that circle scaled by 1/2, so its boundary is also 60π ≈ 188.5 mm.

## Materials: check out completely

All six pieces, the grid mat, the four templates and the three bars have the stated dimensions; see "How it was checked".

## Adult guide: checks out completely

Every statement, table entry, proof step and number is correct. I checked:
- the overview: the support-width definition; the exact constant-width theorem with its hypotheses (equilateral corners, radius equal to the side, minor arcs); the extremes table; the fixed-gap rule ("fits … exactly when its width … is at most g; … touch both exactly when its width equals g"); the marked-point range 25.359–34.641 with the opposite-sum rule; and 60π for both boundaries;
- the p. 2 proof (each step, as listed above) and its sketch;
- the p. 5 Problem 1 key, the nearest-mm readings 60/60, 40/60, 60/85, 52/60, 60/60, and the global-extremum formulas. The triangle formula assumes θ is measured from a side-parallel normal, which is the reading that gives 60 at θ = 0;
- the Problem 2 table and its translation argument;
- the p. 6 construction table (centre A joins B to C, and so on), the 2/3 scale, the compass example (17.5 mm at 0.7), and the 7°, 37°, 83° drawings;
- the P4 "concrete path" and its limits;
- the p. 7 table, sketch, d_O formula, its range from w − R to w/2 on each side, "roughly 25 and 35", and the 26.4 × 16.8 mm and 19.2 mm on-page sizes;
- the p. 8 perimeter argument and hints;
- the arithmetic: 10 basic and 3 optional sheets, 30 pieces, 6 templates per size, 10 rails, 5 rulers, 10 guides, 5 mats, eleven children with seven in grades 3–5, and 2 + 2 + 1 = 5 kits.

The p. 8 digital-precision figures ("sampled full-size disk widths are 60.000456–60.016920 mm; largest sampled Reuleaux nominal-width error is 0.001631 mm") are labelled as finite samples. An exact computation on the compiled curves gives 59.9998–60.0175 and 0.0015, which differ only in the fourth decimal, so I do not count this as a problem.

## Located problems (2, both minor; no incorrect answers)

### 1. Student pp. 1, 3, 4, 5, 6: millimetre labels on reduced drawings, with no note that they are reduced
- **Quoted text and diagrams:**
  - p. 1: the "parallel contacts" panel marks the gap arrow "0" at one end and "46 mm" at the other, and the "record" panel says "46 mm". The page asks children to "Measure the perpendicular gap, to the nearest millimeter."
  - p. 5: "32 mm" is written above the O-to-edge segment and again in the record panel.
  - p. 3: "25 mm" under DE.
  - p. 4: "Its arcs have radius 60 mm".
  - p. 6: "radius 30 mm" and "radius 60 mm".
- **Evidence (`out_check_diagrams.txt`):**

  | Page | Label | Drawn length on the page | Scale |
  |---|---|---|---|
  | p. 1 | 46 mm gap | 25.30 mm | 0.55 |
  | p. 3 | 25 mm DE | 17.50 mm | 0.7 |
  | p. 4 | 60 mm arc radius | 33.0 mm | 0.55 |
  | p. 5 | 32 mm segment | 19.20 mm | 0.6 |
  | p. 6 | 30 mm and 60 mm radii | 18.9 and 37.8 mm | 0.63 |

  Nothing on the student pages says the drawings are reduced (no "scale", "size" or "smaller" anywhere in the student text). In this activity every pair holds a 150 mm ruler, and the p. 1 example is laid out like a ruler reading from "0" to "46 mm". A child who checks the worked example with the ruler reads 25 mm where the page says 46, and 19 mm where p. 5 says 32. The guide knows this ("Compact student diagrams are sketches, not cutout patterns", p. 3; "The 32 mm label records the nominal example, not a ruler reading from that compact sketch", p. 7), but the children's page does not say it. The drawings are internally consistent, and p. 6's three figures share one scale, so no answer is affected.
- **Smallest fix:** add "(drawn smaller than real size)" under the p. 1 and p. 5 example figures, and under the figures on pp. 3, 4 and 6, or once in the p. 1 opening guidance: "Drawings on these pages are smaller than the real pieces."

### 2. Student p. 4, Problem 4: "Include the turns between the drawings" has two readings
- **Quoted text:** "Explain why the exact curved triangle has the same width in every direction. Its arcs have radius 60 mm, with centers at A, B and C. Include the turns between the drawings in your explanation."
- **Evidence:** the intended meaning (guide p. 4: P4 "needs … reasoning over intervening turns"; guide p. 6: the three drawings "illustrate positions, not complete angular coverage") is that the explanation must also cover every position between the drawn ones. The sentence can also be read as asking for the amounts the piece turned from one drawing to the next. Those amounts are 30° and 46° (the AB directions are 7°, 37° and 83°, `out_check_diagrams.txt`). On that reading a child measures or reports two angles that play no part in the argument. Neither reading changes the constant-width answer. (The intended reading is coherent: the drawn range from 7° to 83° is 76°, more than the 60° that the symmetry needs, so explaining every turn between the drawings does cover every direction.)
- **Smallest fix:** "Your explanation should also work for every position between the drawings."

## Not checked

- Physical readiness: actual printer scale and margins (the grid mat comes within 7.5 mm of the page edge), stiff-card cutting accuracy, rail parallelism and clearance at the fixed 60 mm gap, compass handling, and timing. The packet itself marks all of these unperformed.
- I did not rebuild the PDFs from source, because `pdflatex` is not installed here. The checks read the delivered PDFs; they match the nominal coordinates in `make_assets.py` and `facilitator.tex`.
