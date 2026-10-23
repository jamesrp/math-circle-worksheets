# Week 85 (Drawing machines): math check

Scope:
- `lowell-math-circle-year-2/week-85/week-85-shared.pdf`: shared Grades 2–5 packet, 4 pages, Problems 1–4.
- `week-85-upper.pdf`: Grades 4–5 packet, 4 pages, Problems 1–4.
- `week-85-materials.pdf`, 10 pages: bar templates, assembly page, two mat sheets, seam bridge, inserts A–M, area pieces.
- `week-85-facilitator.pdf`: the adult guide, 5 pages.

There is no K–1 packet; the guide says so. Sources read: `source/week-85/student/generate.py` (it produces every coordinate), `shared.tex`, `upper.tex`, `materials.tex`, `guide/facilitator.tex`, both READMEs, `QA.md`, `SOURCES.md` and `build.py`. I did not run or import the package's `check_math.py`, and I did not rely on its `pose()` function. My scripts and their outputs are in this run folder, for `plans/review/checks/week-85/`. Page renders at 80 dpi are in `render/`, for viewing only. Checked October 23, 2026.

**Result: I found 0 problems. Every task is possible as printed and has the answer the guide gives. Every diagram matches the source coordinates and the mechanism. Every statement in the guide is true under the hypotheses it states.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 50 checks, 0 failures). It reads the task coordinates from `generate.py` as literal data, without executing that file. It takes the mat geometry from the materials pages; `check_diagrams.py` confirms that geometry in the PDF.
  - **Linkage from first principles.** For a given anchor O and tracer T, it finds every pose of the six-bar machine by circle intersections: X on both circle(O, 80) and circle(T, 80), then Q = 2X − O, then Y on circle(Q, 80) and circle(T, 80), then P = 2Y − Q. I tried 20,000 random T with 1 < |OT| < 159, giving 40,000 open poses (two mirror images each). Every open pose is a parallelogram with P = 2T − O. The only other poses have Y = X, which puts P on O; O, T and P are then trivially on one line.
  - **Second parameterisation.** Here the two long-bar angles are the free parameters, and T must be Q or X + Y − Q. In 20,000 random poses, the open branch always gives P = 2T − O. The fold branch T = Q breaks collinearity in all 20,000, but it always has |OT| = 160 exactly. The two branches meet only at full extension (|OT| = 160) or with P on O.
  - **Zones and copies.** Every copy and inverse the tasks need, checked against the T zone (110..160 × 115..165) and the output target (180..290 × 90..190). The T zone doubled about O is 180..280 × 90..190. It also checks the segment lengths, orientation, F's inverse rectangle, L's forward rectangle, J and K halved, and the M anchor shift with its unique compensating translation.
  - **Areas.** Exact areas by the shoelace formula. An exact covering by 10 mm squares and half-squares, each grid cell tested as whole, empty or cut on a diagonal. Whether the kit is enough.
  - **Reach.** Every tracer position needed has 71.6 ≤ |OT| ≤ 122.6 mm (the singular values are 0 and 160). The rhombus angle at Q stays between 53° and 100°. With 20 mm bar ends, every joint of both mirror poses stays on the 450 × 400 board centred on the mat.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 150 checks, 0 failures). It reads the delivered PDFs with PyMuPDF in millimetres from the lower-left corner (the TikZ frame).
  - **Every page.** Headers, footer ids, and one numbered problem per page, 1–4 in each packet.
  - **All nine mechanism drawings.** These are the three demo panels on each operation strip, shared p. 3, upper p. 1 and materials p. 2. In each one:
    - the four bars meet the six joints, and X and Y are the long-bar midpoints;
    - the six lengths OX, XQ, QY, YP, XT and TY are equal (spread ≤ 0.001 mm);
    - P − O = 2(T − O);
    - the labels sit on their own joints.
  - **Tick marks.** Upper p. 1 and materials p. 2 each have exactly six ticks, one across the middle of each equal length.
  - **Demo strokes.** In each panel the P stroke is the T stroke doubled about O. The T legs are 6.125 and 6.860 mm. The panel-2 arrow aims at T (forward strip) or P (reverse strip).
  - **Thumbnails.** A, B, C, D, E, G, H, I, J, K, L and the M locator on upper p. 4 each match the source data at their stated scale, up to one translation. The D labels 1–5 sit beside the right dots. The p. 4 locator uses one consistent 0.8 scale for O, O′ (20 mm apart) and M. Shared p. 4 shows F at actual size.
  - **Materials.** Two 182 × 18 and two 102 × 18 strips, with holes 80 mm apart and 11 mm from each end. Both mat sheets: O (40, 140) and O′ (60, 140); the input corners 100..170 × 105..175; the T zone; the output corners split across the seam; all eight placement crosses; the 100 mm bar; the registration circles. The 44 × 145 bridge covers mat x 194..238, y 70..215, which spans the unprinted band 207.9..223.9. Every insert has its border (70 × 70 or 110 × 100), its corner crosses, its letter inside, and its drawing at the mat position the guide uses. F's box is at 220..260 × 125..155 and L's at 125..155 × 130..150. There are 48 squares plus 8 diagonally cut squares (16 half-squares), all 10 mm.
  - **Sources.** The checked-in `.tex` files equal a fresh run of `generate.py` (run on a copy). The delivered PDFs equal `reference-pdfs/`.

## Shared Grades 2–5 packet (pp. 1–4): checks out completely

- **Opening.** The rules, plus three genuine poses of one non-task elbow. P's stroke is T's stroke doubled about O.
- **P1 (A, B, C).** Each copy has the same shape and orientation at twice the size, placed by dilation about O. A: 35, 20 → 70, 40 mm. B: sides 30, 31.6, 36.1 → 60, 63.2, 72.1 mm. C: 10, 15, 20, 25, 10 → 20, 30, 40, 50, 20 mm. All three copies fall inside the output target.
- **P2 (D, E).** The inverse is T = (P + O)/2. The D dots need T at (115, 125), (130, 160), (155, 150), (150, 120) and (125, 140). The E house needs T at (120, 125), (150, 125), (150, 145), (135, 157.5), (120, 145). All of these are inside the T zone.
- **P3.** The answer is no: on the open frame, O, T and P are always collinear with OT = TP, so OP = 2·OT. The only pose that breaks collinearity is the fold T = Q. It needs |OT| = 160, which means T over Q's pivot at full extension (or P on O), so the machine cannot reach it in use. See "Not counted".
- **P4 (F).** F's 40 × 30 box pulls back to the 20 × 15 tracer rectangle (130, 132.5)–(150, 147.5). Because the map is a bijection, a T path has its copy inside F exactly when T stays inside this rectangle, so the rectangle is unique.

## Upper Grades 4–5 packet (pp. 1–4): checks out completely

- **P1.** Yes. With u = OX = XQ and v = QY = YP as directed bars, the open frame gives XT = v and TY = u. So OT = u + v and OP = 2(u + v). The page's rule "open and uncrossed" excludes the fold pose, which is the only exception.
- **P2 (areas).**
  - G: 4 units; copy 16.
  - H: 4 units; copy 16.
  - I: 4½ units (3 squares + 3 halves); copy 18 (15 squares + 6 halves).
  - All three coverings are exact with the supplied pieces. The most one original and its copy need is 20 squares (G or H) and 9 triangles (I), within the kit's 48 and 16.
  - The pictured convention is correct: two congruent 10 mm half-squares, the second shown 2 mm from completing the square, and a 10 mm unit square.
- **P3 (reverse).** T = O + ½(P − O).
  - J (60 × 40) gives 30 × 20 at (120, 125)–(150, 145). Every length of K halves, and K's halved copy stays inside the T zone.
  - L's box (125, 130)–(155, 150) needs P on (210, 120)–(270, 160), inside the output target. That rectangle is the same size as J but 10 mm off in both x and y, so tracing J does not answer the question.
- **P4 (anchor change).** With M fixed, the copy moves from (220, 110), (260, 110), (240, 160) to 20 mm left, because P′ = 2T − O′ = P − (20, 0). Moving M 10 mm right puts the second copy exactly on the first. The shift is unique: half the anchor shift, in the same direction. The moved M reaches x = 160, the edge of the T zone, so it is still inside. All tracer distances from O′ are 71.6–101.1 mm.

## Materials (10 pp.): check out completely

- The bars are 0/80/160 mm and 0/80 mm between hole centres, as the guide's hardware paragraph says.
- The anchor, zones and corners on the mat agree with every coordinate the guide uses.
- Each insert lands its drawing at the guide's mat position when its corners sit on the matching crosses.
- The seam bridge restores the 16 mm unprinted band.
- The piece counts are as stated.

## Adult guide (5 pp.): checks out completely

- **Overview.** True with its stated hypotheses (OX = XQ = QY = YP = XT = TY = L, simple open parallelogram branch):
  - P = O + 2(T − O);
  - X = u, Q = 2u, Y = 2u + v, T = u + v, P = 2u + 2v;
  - P₂ − P₁ = 2(T₂ − T₁), so lengths double, angles and orientation are kept, and area is ×4;
  - swapping the tips gives ½ and ¼;
  - moving the anchor by d moves the copy by −d.

  Its warning that equal-length marks alone do not fix the branch is right: the fold pose T = Q exists.
- **Solutions.** Every coordinate, length and area in the shared P1–P4 and upper P1–P4 solutions matches the computations above. That covers the A and C segment lengths, the D and E tracer positions, the F inverse, J's 30 × 20, the L target, the anchor shift and the 10 mm compensation. So do the hint (four unit squares in a doubled square; pair two triangles, use ×4, halve) and the general compensation rule (half the anchor displacement, same direction).
- **Hardware remark.** "A pencil taped beside a bar invalidates the exact scale model" is correct. An offset tip rotates with bar QP, so the copy is no longer a dilation.

## Not counted (correct as printed, or outside the mathematical scope)

- **Shared P3 never states the "open frame" rule.** The upper packet states it; the shared page has only "Keep O fixed … Stop if the bars get stuck". The answer "no" still holds:
  - For any T with 0 < |OT| < 160 and P off O, every pose is the open parallelogram.
  - Breaking collinearity needs the fold T = Q at |OT| = 160, reached only at full extension.
  - In the working zone |OT| ≤ 122.6 mm.
  - The guide tells adults not to count a stuck, crossed or off-axis assembly as a counterexample.
- **Guide p. 3: "OT = TP (equivalently OP = 2OT)".** The two are equivalent only given the collinearity stated in the same sentence. As written, it reads correctly.
- **Shared P2: the D dots are numbered 1–5,** while the guide says any order is fine. This is wording, not mathematics; the task "visit every dot" has no order.
- **The moved M touches the T zone edge** (x = 160). The guide's "within the intended zone" is true with the edge included.
- **Joint Q leaves the paper** in some poses (y up to 298 mm against a 279.4 mm mat), but it stays on the 450 × 400 board. The guide and materials say the board is required for this reason.
- **The dashed frame in the upper p. 4 locator** matches no mat feature (at the 0.8 scale it would span mat x 20..235). The positions of O, O′ and M inside it are exact.
- **Physical fit, coaxial mounts, clearance and print scaling** are untested, as the package says. Digital geometry does not establish them.
