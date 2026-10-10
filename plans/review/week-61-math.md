# Week 61 (triangles on a ball): math check

Scope: `lowell-math-circle-year-2/week-61/week-61-students.pdf` (W61-S-v2, 7 pp., Problems 1–7) and `week-61-facilitator.pdf` (W61-F-v1, 9 pp.). The student PDF is one combined packet:
- pp. 1–3 (Problems 1–3) are headed Grades 2–5;
- p. 4 (Problem 4) is headed Grades 3–5;
- pp. 5–7 (Problems 5–7) are headed Grades 4–5.

I also read the editable source in `lowell-math-circle-year-2/source/week-61/` (`student/students.tex`, `student/geometry.py`, `student/source-notes.md`, `guide/facilitator.tex`, the READMEs). Checked October 10, 2026. My scripts and outputs are in [checks/week-61/](checks/week-61/).

**Result: every answer, key, diagram and theorem in the packet is correct. I found 5 minor problems, none of which changes an answer:**
- the p. 1 rules answer most of Problem 1 in advance;
- a label box hides the corner on the p. 5 "Corner A" panel;
- the guide calls the p. 5 example a "non-task" triangle, but it is the Problem 6 triangle and it shows P6's whole pair-A column;
- the guide lists cases where the rule still holds as "counterexamples";
- a guide hint compares projected sizes of cells.

## How it was checked

- `extract.py` reads the delivered student PDF, not the source. It uses poppler's `pdftocairo -svg` for the vector paths and `pdftotext -bbox` for the words, and writes every path (stroke, fill, dash, sampled Bézier points) and every word box to `extracted.json`.
- `check_diagrams.py` (`out_check_diagrams.txt`, 75 ok lines, no FAIL) treats each drawn ball as an orthographic disc. It lifts every visible point to the front of the unit sphere and every dashed point to the back. From the actual printed dots, arcs, fills and number labels it recomputes:
  - surface angles from tangent vectors, and arc lengths;
  - the best-fit centre plane of every curve, to confirm it is a great circle;
  - the lune angle;
  - the sign cell of every shaded region and region number;
  - an orthogonal (Kabsch) fit of each back view to its front view, to confirm the back is a rotation of the same ball and not a mirror image.
- `check_math.py` (`out_check_math.txt`, 71 ok lines, no FAIL) uses only the standard library and numpy. Areas come from the Van Oosterom–Strackee solid angle and Monte Carlo sampling (400,000 points), never from Girard's formula. Lune membership is tested from longitudes about the lune's own pole, never from the guide's sign rule. The script:
  - runs the covering count on the P5 and P6 triangles lifted from the PDF and on 40 random triangles in scope;
  - checks Girard's formula against solid angles on 300 random triangles and on three near-hemisphere triangles;
  - checks every number in the guide, including the out-of-scope examples, the 60-60-90 coordinates, the equal-angle Gram construction and the kit and printing arithmetic.
- `w61lib.py` holds the shared geometry and PDF-figure helpers.
- I did not run the packet's own `verify_math.py` or `compare_pdfs.py`. No `pdflatex` is installed here, so I could not rebuild the PDF. I matched source to PDF through the figure parameters instead: the 95° route, the 110° triangle, the 40° lune, the 80-80-80 side views and the three records all match `geometry.py`.

## Grades 2–5 (pp. 1–3, Problems 1–3): correct; item 4 below

- **Page 1 convention figure:** P and Q are 95.00° apart. The drawn circle is one centre plane through P and Q (front solid, back dashed), and "center" is the projected centre. The thick blue route is the 95° minor arc, entirely on the front. The guide's "95° minor arc; the other 265° arc" is right.
- **P1:**
  - Close and far non-opposite pairs each have a unique shortest route, the minor great-circle arc.
  - Opposite points have infinitely many: routes through different equator points all have length π.
  - So "two different routes of the same shortest length" happens only for the opposite pair.
- **Page 2 convention figure:** the two sides at P are great-circle arcs whose tangent directions are 135.01° apart. The flat "Directions close to P" panel is 135.00°.
- **P2:** yes, three right angles. The octant N, (1,0,0), (0,1,0) has corners 90°, 90°, 90° and area 1/8. It lies strictly inside the open hemisphere about (1,1,1), so it obeys the p. 2 rules although A and B are on the equator.
- **P3:**
  - The printed triangle measures corners N 110.00°, A 90.00°, B 90.00°. Its sides are 90°, 90° and 110°, all great-circle arcs, and the shading is the triangle itself.
  - For gaps 30° to 179°, the corners are (gap, 90, 90), the area is gap/720 (strictly increasing), and the triangle is inside an open hemisphere.
  - All three requested cases exist: gap < 90, = 90, and between 90 and 180. Gap 180 is excluded by "No two corners are opposite."

## Grades 3–5 (p. 4, Problem 4): checks out completely

- **Lune figure:** the open dot "S (back)" is the back point opposite N, to within 0.01°. Both lune edges are meridians, each with solid front pieces and a dashed back piece. The lune angle measures 39.95°, the thin circle is N's equator, and the shading lies inside the lune. The top view has 9 spokes at exactly 40° gaps, and 40 is not one of the task gaps.
- **P4:** 45° → 8 lunes, 1/8, triangle **1/16**; 72° → 5, 1/5, **1/10**; 120° → 3, 1/3, **1/6**. These are confirmed by solid angle, and the 40° lune samples to 0.1111.

## Grades 4–5 (pp. 5–7, Problems 5–7): correct; item 5 below

- **P5 convention panels (80-80-80 triangle):**
  - "Corner A" shades the triangle, cell +++.
  - The two blue circles are exactly ABB* and ACC*.
  - "Pair at A: front" shades cells +++ and +−−, and "Same pair: back" (a true rotation, det +1) shades −++ and −−−. That is exactly the cells whose B and C signs agree.
  - Patch X is in cell +−−, covered by the A pair only, so the table's count 1 is right.
- **P5 (octant N, A, B):**
  - The printed N, A and B are mutually perpendicular.
  - The back view is a rotation of the front (residual 0.0004).
  - Each region label k sits in the k-th sign cell (+++, ++−, +−+, +−−, −++, −+−, −−+, −−−).
  - Sampled with independent lune tests: every region ≈ 1/8, and each pair ≈ 1/2. Pairs: region 1 N, A, B; 2 B; 3 A; 4 N; 5 N; 6 A; 7 B; 8 N, A, B. So the counts are **3,1,1,1,1,1,1,3**.
  - 3/2 = 1 + 4f, so f = 1/8.
- **P6:**
  - The printed triangle measures 80.00°, 80.00°, 80.00°, with equal sides of 77.87°.
  - The back view is a rotation (residual 0.0000), and labels 1–8 sit in the eight sign cells in order.
  - Sampled: regions 1 and 8 ≈ 0.083 (1/12), regions 2–7 ≈ 0.139 (5/36), each pair ≈ 0.444 (4/9).
  - Letters: ABC, C, B, A, A, B, C, ABC, so the counts are **3,1,1,1,1,1,1,3**, the same as P5 although the regions are unequal.
  - 4/3 = 1 + 4f, so f = **1/12**.
- **P7:**
  - Rule f = (sum − 180)/720.
  - All three records exist inside an open hemisphere: (60, 60, 90) → **1/24**; (80, 80, 80) → **1/12**; (100, 100, 100) → **1/6**. Solid angles agree to 1e-12.
  - The printed sketches measure exactly the captioned corners, with minor sides of 70.5°, 54.7° and 54.7°; 77.9° ×3; and 98.5° ×3.
- **General theorem:**
  - Girard matches solid angle on 300 random triangles in scope, with worst error 3e-15.
  - Sums stay in (180, 540). Near-hemisphere triangles reach 534° with area < 1/2.
  - On 40 random triangles all eight cells are nonempty and the counts are always 3,1,1,1,1,1,1,3.

## Adult guide

Every answer and proof is correct. I checked:
- the overview (shortest routes, lune fraction θ/360, pole triangle θ/720, Girard with the stated hypotheses, 180 < sum < 540 and 0 < f < 1/2, and the eight-cell covering summary);
- the P1 key and the ds² proof, the P2 octant and its hemisphere witness, and the P3 key including the gap-0 and gap-180 endpoints;
- the P4 table and its rotation/reflection proof;
- the P5 key table and the 3/2 tally;
- the P6 key, the opposite-region partners, 4/3 = 1 + 4f, and the independent cell key (cells 2–7 have corners 80, 100, 100 and solid angle 5/36; 2(1/12) + 6(5/36) = 1; one pair = 4/9);
- the sign-cell proof on pp. 7–8 (independence, existence of all eight cells, the agreement rule, the antipodal area argument and the area deduction);
- the P7 table, the explicit 60-60-90 coordinates (corners exactly 60, 60, 90), and the equal-angle construction: d = cos q/(1 − cos q), eigenvalues 1 − d, 1 − d, 1 + 2d > 0, tangent cosine d/(1 + d) = cos q, for both 80° and 100°;
- the latitude counterexample (corners 90, 90, 90 at latitude 30°, area 1/16, not 1/8);
- the radius-scaling remarks;
- the preparation and printing arithmetic: 15 strings = 12 m, 30 dots, 11 tabs, 5 balls, a 62.8 cm circumference under 80 cm, and 21 + 7 + 9 = 37 student and 27 adult sheets.

The cross-references (guide "pages 7–8", "page 3" for K–1) point to the right pages. The guide's problems are items 1–3 below.

## Located problems (5, all minor; no incorrect answers)

### 1. Guide pp. 3 and 5: the "non-task 80° example" is the Problem 6 triangle and shows P6's whole pair-A column
- **Quoted text:** p. 3: "Before P5, reuse its non-task 80° example: corner A → circles AB, AC → containing/opposite pair → X counted once." p. 5: "The P5 convention example uses A, B, C on a non-task 80° triangle."
- **Evidence:** every labelled point of the p. 5 panels "Pair at A: front" and "Same pair: back" coincides with the P6 "Front" and "Back" views, to 0.0000 ball radii after scaling (`check_diagrams.py`, last section). So the example is the P6 triangle, drawn in the P6 views. Its shaded cells are +++ and +−− in front and −++ and −−− behind. These are P6 regions 1, 4, 5 and 8, which is exactly where the guide's P6 key puts the letter A. A child can copy one of the three pair columns of P6 straight from the example. An adult told that the example is "non-task" will not expect this. Nothing printed is false.
- **Smallest fix:** in both guide sentences, replace "non-task 80° example/triangle" with "the P6 triangle, which already shows P6's pair at A (regions 1, 4, 5, 8); children still find the B and C pairs". If the example should be non-task, draw the four panels on a different triangle.

### 2. Guide p. 8 (and p. 1): "Counterexamples to overextension" lists cases where the rule still holds
- **Quoted text:** p. 8: "Counterexamples to overextension. … Taking the octant's complementary region gives fraction 7/8 and reflex inside corners 270°; it violates our convex/open-hemisphere/less-than-180° conditions. A long equatorial side changes the selected region and is not a minor side. A small latitude circle cannot replace the equator…" p. 1: "The formula here does not cover long sides, latitude sides, degenerate triples, or the complementary region."
- **Evidence (`check_math.py`, "Outside the stated scope"):**
  - For the octant's complement, (3·270 − 180)/720 = 630/720 = 7/8, which is exactly its area.
  - For the pole triangle closed by the long equator arc with gap g, the corners are 360 − g, 90, 90 and the rule gives (360 − g)/720. That is 0.4167 at g = 60 and 0.3472 at g = 110, against sampled areas 0.4167 and 0.3467.
  - Only the latitude case in that paragraph is a real counterexample (rule 1/8, area 1/16).
  - What needs the stated conditions is the bound 180 < sum < 540 and the six-lune proof as written, not the formula.
  
  Testing the rule on the outside of the octant is a natural P7 move. An adult reading "counterexamples" may tell a child the rule fails there, when it gives the right 7/8.
- **Smallest fix:** after the complement sentence on p. 8, add: "The rule itself still gives (810 − 180)/720 = 7/8 here, and it works for the long-side triangle too; our conditions are needed for the bound 180 < sum < 540 and for the six-lune proof. The latitude case is a true counterexample." On p. 1, change "The formula here does not cover" to "This proof does not cover".

### 3. Guide p. 6 hint: "compare the sizes of cells 1 and 2 in the same map" judges area from a projection
- **Quoted text:** "Optional hint: If children assume 'eight cells means eighths,' compare the sizes of cells 1 and 2 in the same map."
- **Evidence:**
  - On the printed P6 front view, regions 1, 2, 3 and 4 take up 0.141, 0.272, 0.272 and 0.315 of the disc. Their true fractions are 1/12, 5/36, 5/36 and 5/36 (`check_math.py`, "Guide p.6 hint").
  - Cells 1 and 2 happen to compare the right way. The same method makes region 4 look larger than regions 2 and 3, although all three are congruent.
  - The guide rules this method out elsewhere: p. 5 says "Do not measure the projected shaded shape", and p. 7 says "a camera's apparent sizes are irrelevant".
- **Smallest fix:** "…note that cells 1 and 2 together are the 80° lune at C (between circles CA and CB), 2/9 of the ball, not 2/8, so the cells cannot all be eighths." Check: 1/12 + 5/36 = 2/9.

### 4. Student p. 1, shared rules: the definition answers most of Problem 1
- **Quoted text:** "For two distinct points that are not opposite, its shorter arc is the shortest surface route." Problem 1 then asks: "Which pairs let you find two different routes of the same shortest length?"
- **Evidence:** the rule says the close and far pairs have *the* (one) shortest route. It names opposite points as the exception, so the answer, "only the opposite pair", can be read off before any string is moved. The guide's launch says "Do not solve the opposite-point question", and the page does. The mathematics is right; the discovery is pre-empted.
- **Smallest fix:** "A shortest surface route between two points runs along a great circle through them." The three-panel P → circle → shorter-arc visual can stay.

### 5. Student p. 5, convention panels: the label box over A hides the corner the panel is named for
- **Quoted figure:** the "Corner A" panel, and also "Pair at A: front" and "Same pair: back".
- **Evidence:**
  - A's white label box sits 1.8–11.2 pt above A's dot, on the triangle's side of A. The 33 pt tall shaded triangle and both sides stop at the box, so the corner at A is not visible (600 dpi render; `check_diagrams.py`, "Vertex-label boxes" lists 23/25 probe points of the box over shading).
  - The same happens to A on "Pair at A: front" and to A* on "Same pair: back", where the box covers the tip of a shaded lune.
  - On pp. 3 and 6 the vertex labels sit off the shapes. On the p. 7 100° sketch the B and C boxes cover a little of their corners, but those angles are given in the caption.
- **Smallest fix:** in the four p. 5 panels, put A's label (and A*'s) beside the dot, for example `anchor=west`, instead of above it.

## Not checked

- The Petrunin–Zamora page and observation references (Observation 2.22, §14B, Lemma A.17, Proposition 17.10). The reference PDF is not in this checkout. The statements they are cited for are standard, and I verified them independently above.
- A clean rebuild from source (no `pdflatex` here). Correspondence between source and PDF was checked through the figure geometry and text only.
- Physical behaviour: string contact, friction loops on small circles, a flat paper right angle on a ball, and calibrated meridian gaps. The guide already marks these unperformed.
- The packet's own `verify_math.py` and `compare_pdfs.py`, which I did not run, by design.
