# Week 15 (nearest-site regions): math check

Scope: `lowell-math-circle-year-2/week-15/week-15-k-1.pdf`, `week-15-grades-2-3.pdf`, `week-15-grades-4-5.pdf` (8 problems each) and `week-15-facilitator.pdf` (15 pages). The return visit was not checked. No use logs or session records were opened. My scripts and outputs are in [checks/week-15/](checks/week-15/). Checked October 5, 2026, before the guide was marked piloted; that change touched only the guide's status wording.

**Result: no errors in any student band. The adult guide has 2 minor problems: a missing hypothesis and an incomplete argument. No stated answer is wrong.**

## How it was checked

- The delivered PDFs are byte-identical to `source/week-15/editable/reference-pdfs/`. Re-running `build_packets.py` and `build_guide.py` in a scratch folder reproduced the shipped `.tex` files exactly.
- `extract_pdf_geometry.py` and `extract_crosses.py` read the site circles, labels, probe crosses and shaded targets back out of the student PDFs. All 24 maps match the source data. Each frame is 5.8 in square, and the scale is 69.6 pt per unit on both axes, so scaling is equal. The shaded targets are exact: strip −1 ≤ x ≤ 1; corner x ≤ 1, y ≤ 1; triangle (−2,−1), (2,−1), (0,2).
- `voronoi_exact.py` and `check_all.py` (output in `check_all.out`) are my own exact rational code for closed cells. They cover every site set and every guide construction: each cell (clipped to the frame, plus whether the full cell is bounded), the shared set for every pair (an edge, a single point or nothing), every point with three or more nearest sites, and the nearest-site label and margin for all 46 probe crosses.
- `search_placements.py` (output in `search_placements.out`) brute-forces the placement tasks:
  - K–1 P8 and 2–3 P8 each have exactly one solution on a ½-grid, up to swapping the two names.
  - 2–3 P7: 198 D positions on a ¼-grid in the frame work, and on x = 0 exactly t ∈ {9/4, 5/2, 11/4, 3} works.
  - 4–5 P6: no single new dot (¼-grid on [−6,6]²) bounds B's region.
  - 4–5 P8: 60,000 random placements of 1–3 new dots never take R while keeping P and Q. Many take S.

## K–1: checks out completely

- **P1:** 7 A, 6 B, 3 AB. Every non-tie cross is at least 0.67 in from a tie.
- **P2:** boundary 3x + 2y = 0.
- **P3:** boundaries x = ±1, with no AC tie.
- **P4:** 3 A, 3 B, 1 C, 2 AB, 1 AC, 1 BC, 1 ABC. The cross at (0,1) is C only.
- **P5:** the centre is a four-way tie.
- **P6:** E's region is the diamond |x| + |y| ≤ 2, with three-way vertices ABE, BCE, CDE, ADE.
- **P7:** placing the new dot at the midpoint works, giving C the strip |3x − 2y| ≤ 39/10.
- **P8:** the unique answer is B and C at (∓2, 0).

## Grades 2–3: checks out completely

- **P1:** 4 A, 6 B, 4 AB, all on x + y = 0.
- **P2:** three rays meeting at the ABC point (0,0).
- **P3:** boundaries x = −5/4 and x = 3/4. No three-way tie exists.
- **P4:** both axes are shared, and the centre is ABCD.
- **P5:** the pairs that share a boundary are AB, AD, BC, BD and CD. AC shares nothing. The BD edge runs from (0,−1/2) to (3/8,0) and has length 5/8.
- **P6:** the open axis segments inside the diamond disappear.
- **P7:** D at (0,−5/2) works. D at (0,−2) fails because of the four-way tie at the origin. The guide's range 2 < t ≤ 3 is correct.
- **P8:** the unique answer is B and C at (2,0) and (0,2).

## Grades 4–5: checks out completely

- **P1:** boundary 3x + 2y = 0. The triangle-inequality argument is valid and strict off the crease.
- **P2:** same as 2–3 P2.
- **P3:** D's whole cell is the triangle (±7/4, 1), (0,−5/2), which lies inside the frame.
- **P4:** only the origin has three or more nearest sites.
- **P5:** the diamond vertices are ABE, BCE, CDE, ADE, clockwise from the top.
- **P6:** the minimum is 2 new dots, for example (0,±2), giving B the square [−1,1]². One new dot cannot bound B.
- **P7:** the unique answer is (0,−2) and (±24/13, 16/13). All three dots are in the frame.
- **P8:** R cannot be taken, by convexity. S can be taken by B at (0,−5/2): the bisector is y = −1/4, and the squared distances 8 < 41/4 and 1/4 < 16 are correct.

## Adult guide

The guide's coordinates, counts, inequalities, captions and answer diagrams match the computations above. This covers all 24 solutions, hints and extensions; I checked each diagram visually against the computed cells. The two problems below are minor and change no answer.

### 1. Overview and page 3: the inverse construction is missing a hypothesis (guide p. 1 and p. 3)

- **Quoted text, p. 1:** "To realize a convex polygon as the full cell of a site strictly inside it, reflect that site across each supporting edge line and place a competitor at each image. Intersecting the corresponding half-planes gives exactly the polygon."
- **Quoted text, p. 3:** "This works for a convex polygon with A strictly inside it."
- **Evidence:** the cell is the intersection over *all* other sites. Any site already present adds its own half-plane. Example: with B = (0,0) and the existing sites A = (−2,0) and C = (2,0) (4–5 P6), target the square [−2,2]². Adding the four reflections (±4,0) and (0,±4) still leaves B with only [−1,1] × [−2,2]. The packet's own inverse tasks (K–1 P8, 2–3 P8, 4–5 P7) start with A alone, so their answers are unaffected. But the overview states the fact in general, and the 4–5 P6 extension ("Find another pair that makes B a bounded quadrilateral") is exactly a case with other sites already present.
- **Smallest fix:** after "place a competitor at each image", add: "(with no other sites present; any existing site adds its own half-plane and can cut the polygon further)". Make the same addition on p. 3: "…with A strictly inside it and no other sites cutting into it."

### 2. Grades 4–5 Problem 4: the reasoning covers only one of the four triples (guide p. 13)

- **Quoted text:** "An AB equality requires x = 0, and a tie with D also requires y = 0, fixing the point. The same point also ties C."
- **Evidence:** the claim is that the origin is the only place shared by three or more sites. The quoted sentence handles a tie among A, B and D. It does not handle a tie among B, C and D, which contains no A. The conclusion is true, because every three of the four corners include one horizontally adjacent pair and one vertically adjacent pair, but the argument as written is incomplete.
- **Smallest fix:** replace the second and third sentences with: "Any three of the four corners include one horizontally adjacent pair (tie on x = 0) and one vertically adjacent pair (tie on y = 0), so every three-way tie is at the origin, where all four tie."

### Not checked

The guide's description of the Mount CMSC 754 lecture (open cells; the no-four-cocircular assumption) could not be checked because the source is not available locally.
