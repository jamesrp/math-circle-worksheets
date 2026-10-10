# Week 56 (Corners of a solid: Euler's formula and angular defect): math check

Scope:
- `lowell-math-circle-year-2/week-56/week-56-students.pdf`: 9 pages, US Letter, footer N56-S-v2. Two bands:
  - pp.1–6 are headed Grades 2–5 (Problems 1–6).
  - pp.7–9 are headed Grades 4–5 (Problems 7–9).
  - There is no separate K–1 packet; the guide offers p.3 orally to younger children.
- `week-56-materials.pdf`: 4 preparation pages (N56-M-v1). They hold five nets with 30 mm edges, eight fan triangles, eight fan squares and two 80 mm circles. I checked them because every problem depends on the models being the stated solids.
- `week-56-facilitator.pdf`: 10 pages (N56-FAC-v1).

Sources read:
- `source/week-56/student/students.tex`, `materials.tex`, the five `*-net.tex` files and the student README.
- `source/week-56/guide/facilitator.tex` and the guide README.

I did not run or import `make_assets.py`, `verify.py`, `audit_math.py` or `guide/check_answers.py`. pdfLaTeX is not installed here, so I could not rebuild. I read every printed value from the delivered PDFs (with `pdftotext`, from renders at 100–300 dpi, and from pixel measurements at 254 dpi) and cross-checked it against the source coordinates. My scripts and their outputs are in this folder. Checked October 10, 2026.

**Result: every answer, count, angle, table entry and proof step in the student packet and the guide is correct, and the five nets fold to the stated solids. I found 3 problems, all minor:**
- **two model icons on p.1 that no real view of the solid could produce;**
- **a Problem 6 wording whose cumulative reading changes two table rows but not the conclusions.**

**The guide has no errors.**

## How it was checked

- **`check_nets.py`** (output `out_check_nets.txt`, 0 failures). It parses each net's TikZ source: faces, tabs, dashed folds, solid cuts, seam letters, face numbers and blue corner labels. For every net it checks that:
  - every face is a regular polygon with 30 mm sides;
  - the folds form a spanning tree of the faces, and no faces or tabs overlap;
  - every corner carries one blue label, and both sides of each fold carry the same labels;
  - each of the 24 seam letters (7+3+5+5+4) marks exactly two cut edges with the same corner-label pair and exactly one tab.

  It then glues the labelled faces. The result is a closed, consistently oriented surface, with each edge in two faces and each vertex star a single cycle. It is isomorphic face by face to the convex hull of the cube, tetrahedron, octahedron, right equilateral prism and equilateral square pyramid. Finally, it confirms that all 170 labels appear at their source positions in the delivered materials PDF.
- **`check_math.py`** (output `out_check_math.txt`, 0 failures). It recomputes every answer from 3D coordinates with its own brute-force convex hull:
  - P1, P2, P4: inventories, incidences, gaps and totals.
  - P3: fan closures, by explicit cone construction.
  - P5: the pyramid.
  - P6: the three redrawings, independently and cumulatively.
  - P7: plane face tracing, the guide's deletion route, all 384 spanning trees of the cube graph and the tetrahedron example.
  - P8: the total defect on 87 convex solids.
  - P9: the reverse inventories, both by the page's deduction and from icosahedron and dodecahedron hulls.
  - The guide's (n,q) restriction and its preparation arithmetic.

  It also compares every table row in the delivered guide (pdftotext) with these computations.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`; its 2 failures are Problems 1 and 2 below).
  - Checks the packet structure: headers, footers and problem numbering.
  - Checks that the five model icons draw the right edge graphs, and whether each is a possible view of a convex solid. It also re-tests the proposed fixes, which pass.
  - Checks equal x/y scaling and equal sides in every worked visual and problem diagram, including the regular pentagon and the 5×60° and 3×108° fans.
  - Checks the Problem 6 and 7 pictures, and the fan pieces against `materials.tex`.
  - Measures the delivered materials PDF at 10 px/mm: circle 80.0 mm across, check bar 30.1 mm.

## Grades 2–5 (pp.1–6): the mathematics checks out (see Problems 1–3 for three minor points)

- **Shared rules and launch picture (p.1):** "two face sides → one shared edge → three face corners, one assembled vertex" is drawn correctly.
- **P1:** the counts are cube (8,12,6), tetrahedron (4,6,4), right triangular prism (6,9,5) and octahedron (6,12,8). They match both the hulls and the glued nets, and V−E+F = 2 in every case.
- **P2:** sides, edges, corners and vertices are cube 24/12/24/8, tetrahedron 12/6/12/4, prism 18/9/18/6, octahedron 24/12/24/6.
  - Edges = sides ÷ 2 in every row, because each edge takes one side from each of its two faces.
  - The corner count alone does not give V: the cube and the octahedron both have 24 corners, but 8 and 6 vertices. "Divide by 3" works for the cube, tetrahedron and prism, and the octahedron row, which is printed, refutes it.
- **P3:** angles used and gaps for the six groups are 180/180, 240/120, 300/60, 360/0 (triangles) and 270/90, 360/0 (squares).
  - Explicit symmetric convex cones exist for the four positive-gap groups. Their edge half-angles are 35.26°, 45°, 58.28° and 54.74°.
  - The two 360° groups degenerate to flat (half-angle 90°). A convex pointed corner needs face angles summing to less than 360°; 835 random convex cones reached at most 358.3°.
  - So 3, 4 and 5 triangles and 3 squares close to a pointed corner with no dents, and 6 triangles and 4 squares close flat.
  - The worked visual is two triangles with a gap arc from 120° to 360°, which is not one of the tasks.
- **P4:** cube 8 vertices × 90°, tetrahedron 4 × 180°, prism 6 × 120° (1 triangle + 2 squares = 240°) and octahedron 6 × 120° (4 triangles). These were measured on the hulls, where each model has one vertex type. Every total is 720°, two full turns. The worked example (60°+60° = 120°, 360°−120° = 240°) matches its drawn arc.
- **P5:** an apex 1/√2 above the centre of a unit square gives all 8 edges length 1.
  - Top: 4 × 60° = 240°, so the gap is 120° (1 vertex).
  - Base corners: 90°+60°+60° = 210°, so the gap is 150° (4 vertices).
  - Total 120° + 600° = 720°, with (V,E,F) = (5,8,5).
  - The "top" and "base corner" labels sit on the right vertices, and the five face pieces have equal sides.
- **P6:** the four P1 models all give V−E+F = 2. The independent redrawings give:

  | Redrawing | (V,E,F) |
  |---|---|
  | Diagonal | (8,13,7) |
  | Centre + 4 lines | (9,16,9) |
  | Edge vertex | (9,13,6) |

  - Each gives V−E+F = 2 and total gap 720°.
  - The old corners keep 90° each. The new centre vertex has four 90° angles and the new edge vertex two 180° angles, so both have gap 0. The answer to "Can a new vertex have a gap?" is no.
  - The pictures are correct: the diagonal runs corner to corner, the centre dot is the square's centre joined to all four corners, and the edge dot is the midpoint of the shared edge.

## Grades 4–5 (pp.7–9): checks out

- **Launch (p.7):** the tetrahedron view has 4 dots, 6 edges and 3 bounded regions. Erasing its three boundary edges leaves a 3-edge star, which is a tree.
- **P7:** the opened cube has 8 dots, 12 edges and 5 bounded regions (by face tracing), as printed, giving the opened count 1.
  - "Yes" to the tree question: the cube graph has 384 spanning trees, and all 384 connected 7-edge subgraphs have no bounded region.
  - Deleting a cycle edge keeps the drawing connected and removes exactly one bounded region. With a tree's E = V−1, this gives opened count 1 and closed count 2 for every convex solid, through a view with no crossed edges through one face.
- **P8:** total gap = 360V − Σ180(n_f−2) = 360V − 360(E−F) = 720°.
  - Checked on 87 convex solids: 7 named, 20 prisms, antiprisms, bipyramids and mixed-face solids, and 60 random hulls. Every one has V−E+F = 2, all vertex gaps positive, and total 720°.
  - The pentagon example (two diagonals from one corner, 3 × 180° = 540°) is correct.
- **P9:**
  - Five equilateral triangles per vertex: gap 60°, V = 12, F = 5·12/3 = 20, E = 3·20/2 = 30.
  - Three regular pentagons per vertex: gap 36°, V = 20, F = 3·20/5 = 12, E = 30.
  - The icosahedron and dodecahedron hulls agree, with every vertex alike. The counts are forced, so "must have" is right.
  - In the fans, the pentagon is regular (sides 0.9, angles 108.000°); its three copies at 0°/108°/216° leave 36°, and the five triangles leave 60°.

## Materials (pp.1–4): check out

- All five nets fold to the stated solids with matching letters and corner numbers (details in `out_check_nets.txt`).
- The tab and face totals match the guide: 24 closing seams per set (72 for three sets) and 28 faces per set (84 for 15 models).
- The fan pieces are 30 mm equilateral triangles and 30 mm squares on non-overlapping grids. The circles have radius 40 mm.

## Problems found

### 1. Page 1, Problem 1 table: the tetrahedron icon is not a possible view of a tetrahedron

- **Diagram (`\tetra` in `students.tex`):**
  - The outline is P(0,0), Q(2.8,0), R(1.3,2.8). The fourth vertex S(1.65,1) lies inside it.
  - Edges QS and SR are drawn solid, and PS is dashed (`\draw[dashed,gray] (0,0)--(1.65,1);`).
- **Evidence (`out_check_diagrams.txt`, "MIXED at (1.65, 1.0)"):**
  - For a convex solid, a vertex inside the outline is either in front, so all its edges are visible, or behind, so all are hidden. S has two visible edges and one hidden, so no viewpoint gives this picture.
  - The counts (4 vertices, 6 edges) are still right. But the icon contradicts the guide's p.4 explanation that "a drawing's dashed lines are hidden edges".
- **Smallest fix:** draw PS solid (`\draw (0,0)--(1.65,1);`). S then becomes the front vertex with three visible faces. The checker passes this version.

### 2. Page 1, Problem 1 table: the octahedron icon draws two hidden edges on top of a visible edge

- **Diagram (`\octa`):** the top (1.4,3.2), the bottom (1.4,0), the front ring vertex (1.4,1.15) and the back ring vertex (1.4,2.1) all lie on the line x = 1.4.
  - The hidden edges top–back and back–bottom (dashed) run exactly along the solid top–front–bottom line.
  - The back vertex sits in the middle of the solid top–front edge.
- **Evidence (`out_check_diagrams.txt`, "vertex-on-edge" and "overlapping"):**
  - The picture shows 10 distinguishable edges, only 2 of them dashed. The octahedron has 12 edges, and 4 of them are hidden in this view.
  - Counting with the guide's rule "dashed lines are hidden edges" (p.4) gives 10. The real models give the right count, and the guide tells children to keep the models beside their records.
- **Smallest fix:** move the front ring vertex to (1,1.15) and the back ring vertex to (1.8,2.05), replacing both occurrences of each in `\octa`. The ring stays a parallelogram, and the four hidden edges become four separate dashed lines. The checker passes this version.

### 3. Page 6, Problem 6: "try these three changes" has a cumulative reading that changes two table rows

- **Text (p.6):** "Keep the cube's shape and try these three changes to its surface drawing." The page never says to start each change from the original cube.
- **Intended:** three independent redrawings, giving (8,13,7), (9,16,9) and (9,13,6). The guide (p.6) says: "Erase the previous change before beginning another. The following rows are independent, not cumulative."
- **Other reading:** a child who keeps all three changes on one cube, on different faces, records (8,13,7), (9,17,10) and (10,18,10) (`out_check_math.txt`, "other reading").
  - V−E+F = 2 and the total gap of 720° still hold, so the answers to the page's questions are unchanged.
  - Rows 3–4 of the table, however, disagree with the guide's key.
- **Mitigation:** the guide's preparation note ("Reset it completely between the three cases") and its Problem 6 instruction tell the adult to reset the cube.
- **Smallest fix:** "…try each of these three changes on its own, starting from the original cube."

## Adult guide (pp.1–10): checks out

**Mathematical overview (p.1).** Every claim is true with its stated hypotheses:
- Euler's formula and the 720° total defect for finite closed convex polygon-faced solids, with the sphere-cellulation and planar-cell conditions;
- defect as a plane-angle sector, positive at genuine convex corners and zero at subdivision points;
- positive local gap is necessary but not sufficient for a whole solid;
- the opened count is 1;
- total signed defect is 360(V−E+F) for closed polygonal surfaces, with a torus giving 0.

**Tables.** All P1–P6 rows, as printed in the PDF, match the computations exactly.

**Arguments.**
- The P2 rule and counterexample are right. "Tetrahedron and prism happen to have three face corners at every vertex" is true; the cube, named in the previous sentence, has three too.
- The P5 realisation at height 1/√2 is right.
- The P6 change accounting and the zero-gap explanation are right.
- The P7 route AB, BC, CD, DA, ab is right: every step stays connected, borders the outside region and removes one bounded region, and the route ends in an 8-dot, 7-edge tree. The leaf-removal proof of E = V−1 is also right.
- The P8 face-angle identity and the P9 deductions are right.

**Adult mathematics (p.9).**
- nF = qV = 2E.
- q·180(n−2)/n < 360 ⇔ (n−2)(q−2) < 4, with exactly the candidates (3,3), (3,4), (3,5), (4,3), (5,3), each realised by a Platonic solid.

**Preparation arithmetic (p.2).** All figures are right:
- 84 faces and 72 closing seams;
- 18 cardstock and 32 student sheets;
- 48 hinge strips;
- 40 triangles, 40 squares and 10 circles;
- a square's far corner at 42.4 mm reaches beyond the 40 mm circle radius.

**Launch figure (p.3).** It matches the student p.3 visual.
