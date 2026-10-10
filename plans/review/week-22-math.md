# Week 22 (meeting regions, four-point convex partitions): math check

Scope: `lowell-math-circle-year-2/week-22/week-22-k-1.pdf` (F22-K-v3, 8 pp., Problems 1–6), `week-22-grades-2-3.pdf` (F22-23-v3, 8 pp., Problems 1–6), `week-22-grades-4-5.pdf` (F22-45-v3, 11 pp., Problems 1–7) and `week-22-facilitator.pdf` (an unnumbered overview, printed pages 1–21, then a route-note page printed 23). I also checked the companion `week-22-bonus.pdf` (W22-BON-v1, 5 pp., Problems 1–6) and `week-22-bonus-facilitator.pdf`. Sources: `lowell-math-circle-year-2/source/week-22/editable/src/` and `source/week-22-bonus/student-src/bonus.tex`. I opened no use logs or session records. My scripts and their outputs are in [checks/week-22/](checks/week-22/). Checked October 10, 2026.

**Result: I found no mathematical errors. Every student answer and every guide answer, table, proof and extension is correct. I found 4 located problems, none of them a wrong answer:**

1. In the bonus Problem 1, the target T is printed 1.3 mm from segment BE.
2. The K–1 Problem 2 record page gives three boards per D position, but each position has two answers.
3. On page 1 of every band, the region key has a stray "×" on the same page as "Put D on each cross".
4. A route-note page reference in the adult guide is wrong.

## How it was checked

- **PDFs match the sources.** The three student PDFs and the guide are byte-identical (MD5) to `source/week-22/editable/reference-pdfs/`. I did not recompile them, because no pdflatex is available.
- **`extract.py` reads the diagrams back.** It uses pdfminer to read every work board back out of the delivered student PDFs: the board rectangle, the dots with their nearest labels, and the crosses. Its output is in `out_extract.txt` and `extracted.json`.
  - All 55 boards match their TeX source boards exactly, to 0.001 board units. That covers labels, dot positions and cross positions.
  - The full boards are 12.60 cm and the record boards are 5.35 cm (K–1 P2) or 5.70 cm. Every record board is a uniform scale of its full board, so collinearities and on-edge contacts survive.
- **Run order:** run `extract.py` before `check_students.py`, which reads its `extracted.json`; the other scripts are independent. The `render/` folder holds page images and text used for reading only and is not part of the checks.
- **`geom.py` is my own exact geometry.** It uses `Fraction` arithmetic for hulls, containment, segment clipping, shared sets and partition enumeration. It imports nothing from the packet's checkers.
- **`check_students.py`** (output in `out_check_students.txt`) recomputes every fixed board from the printed coordinates. For each board it gives every successful split with its exact shared point or segment. It also gives how far the nearest failing split misses at print size, and the nearest non-collinear point-to-line distance.
  - No near-misses exist. Every failing split on a full board misses by at least 14.9 mm. Every non-collinear triple is at least 14.9 mm from collinear.
- **`check_theorem.py`** (output in `out_check_theorem.txt`) runs exhaustive grid checks of the general facts.
  - **Four labels:** all 390,625 placements on a 5×5 grid, coincidences included. Every placement has a success. General position gives exactly 1, exactly one collinear triple gives exactly 2, and four distinct collinear points give exactly 4. Any coincidence gives 4–6, and all four coincident gives 7. Seven occurs only when all four coincide.
  - **Shared sets:** no shared set ever has area. A shared segment of positive length occurs only when all locations are collinear.
  - **Three labels** succeed exactly when their locations are collinear (coincident included). **Two labels** succeed exactly when they coincide. On a line, three labels always succeed.
  - **Random placements:** 30,000 random placements on a thirds lattice, all successful.
- **`check_guide.py`** (output in `out_check_guide.txt`) checks the guide. Every answer set, shared point or segment, construction and table in it is transcribed and recomputed, and its page cross-references are checked against the printed page numbers.
- **`check_bonus.py`** (output in `out_check_bonus.txt`) does the same for the bonus packet and its guide. It reads the dots back from the PDF, which matches the source to 0.0001 units, and the P5 hexagon is regular with equal axis scaling.

## K–1: no mathematical error (one count cue, one key glyph: findings 2–3)

- **P1:**
  - D = (9, 9) has only AD | BC, meeting at (88/13, 88/13).
  - D = (4.3, 4.7) is strictly inside ABC and has only ABC | D.
  - D = (0.8, 7.2) has only AC | BD, meeting at (624/205, 1266/205).
  - Both outside placements have four hull corners.
- **P2:**
  - D = (5, 3) on AB: AB | CD and ABC | D, both at D.
  - D = (11, 3) beyond B: AD | BC and ACD | B, both at B.
  - D = (3.5, 6.5) is the exact midpoint of AC: AC | BD and ABC | D, both at D.
  - That is exactly two per position.
- **P3:** the order is A, D, C, B. There are exactly four successes:
  - AB | CD and AC | BD share segment DC, which is 3 cm.
  - ABC | D shares D, and ABD | C shares C.
- **P4:** with A, B, C fixed and D at all 4,096 points of a 0.2 cm lattice in the box, every position has at least one success.
- **P5:**
  - The middle cross gives AB | C, the right cross gives AC | B, and the upper cross gives none.
  - On a 0.1 cm lattice, the successful positions are exactly y = 5.6. At C = A and C = B there are two successes each.
- **P6:** yes, always (see `check_theorem.py`).

## Grades 2–3: no mathematical error (one key glyph: finding 3)

- **P1:**
  - (9, 9) gives AD | BC.
  - (4, 5) gives ABC | D.
  - (6, 2.5) is the exact midpoint of AB and gives AB | CD and ABC | D, both at D.
  - (6, 1) gives AB | CD at (126/23, 59/23), not at D.
- **P2:** the order is A, D, B, C. There are exactly four successes:
  - AB | CD and AC | BD share DB, which is 3.2 cm.
  - ABC | D and ACD | B.
- **P3:**
  - A positive-length shared segment needs all four labels collinear.
  - A shared filled triangle is impossible, because one group always has at most two labels.
- **P4:** possible. The guide's witnesses have disjoint success sets.
- **P5:**
  - The printed triangle has no success.
  - The locus is the line y = 11/4 + x/8 across the box, which I confirmed on a 0.1 cm lattice.
- **P6:** yes, always.

## Grades 4–5: no mathematical error (one key glyph: finding 3)

- **P1:**
  - (9.8, 9) gives AD | BC.
  - (5, 5) gives ABC | D.
  - (6.25, 2.5) is the exact midpoint of AB and gives AB | CD and ABC | D.
  - (1, 6) gives AC | BD.
  - The counts are 1, 1, 2, 1.
- **P2:** the four points are exactly collinear on y = x + 1, in the order A, C, B, D. There are exactly four successes:
  - AB | CD and AD | BC share CB, from (5, 6) to (8, 9).
  - ABD | C and ACD | B.
- **P3:** the opponent can always find one.
- **P4:** with A = D, there are exactly the four splits that separate A from D. A coincident pair always gives at least those four successes, and all-coincident gives all seven.
- **P5:**
  - "Exactly one success" holds exactly for general position.
  - All seven split types occur as a unique success, so two different unique splits are achievable.
  - Any degenerate placement gives at least two successes.
- **P6:** yes, always.
- **P7:**
  - The printed triangle has no success, and (B − A) × (C − A) = 5613/100.
  - Four is the sharp threshold.

## Bonus (W22-BON-v1): answers correct (finding 1 concerns the printed precision of P1)

- **P1:**
  - T = (4, 16/5) is inside the hexagon. It is on no joining segment and on no infinite joining line.
  - Exactly 8 triples contain it: ABE, ACE, ADE, ADF, BDF, BEF, CDF and CEF. So three dots are necessary and sufficient.
- **P2:**
  - A needs 1 dot, (3, 0) needs 2 and T needs 3.
  - No lattice target in the hexagon needs 4: 6 targets need 1, 262 need 2 and 3,828 need 3.
- **P3:** AC/BD meet at (4, 4), so they cannot be separated. y = 4 separates AB from CD.
- **P4:**
  - Of the 25 partitions of A–E into three groups, exactly AD/BE/C and AE/BD/C succeed.
  - None of the 6 partitions of P–S succeeds.
  - The sharp threshold on a line is 2r − 1 labels for r = 2 and 3.
- **P5:** I mapped the regular hexagon affinely to rational coordinates, which keeps every hull incidence. Of the 90 partitions, only AD/BE/CF succeeds.
- **P6:**
  - The hexagon is strictly convex, and none of its 90 partitions succeeds.
  - AD × BE = (37/9, 28/9), and CF at that x has y = 179/72.
  - The three pairwise crossings are up to 12.8 mm apart, so the failure is visible.

## Adult guides

The main guide's overview is true as stated, with the right hypotheses:

- the planar Radon statement, allowing coincident and collinear labels;
- seven splits, four of type 1+3 and three of type 2+2;
- sharpness at three noncollinear points;
- exactly one success in general position;
- no filled-triangle overlap.

Every other solution, answer gallery, table, proof and extension matches my computations, except one page reference (finding 4).

- **Galleries and tables:** the answer galleries for every fixed board, the 4–5 P5 seven-row table, and the shared points and segments with their lengths.
- **Coordinates:** the K–1 P5 and 2–3 P5 loci, and the 5613/100 determinant.
- **Proofs:** the proof cases on printed p. 18 (coincidence, a collinear triple, three or four hull corners) and the uniqueness argument on p. 4.
- **Extensions on p. 20:** five labels give a triangle–segment shared segment, six give an area overlap, the line threshold is 3, the maximum of 7 is attained when all four coincide, four distinct collinear points give 4, and no prescribed split works universally.

The bonus guide's facts are also all correct:

- Carathéodory's at-most-three bound and the triangulation proof;
- the closest-point separation certificate;
- the line threshold of 2r − 1 with its counting proof;
- the regular-hexagon uniqueness;
- the irregular-hexagon impossibility argument with its exact coordinates.

## Located problems

### 1. Bonus, page 1, Problem 1 (and bonus guide page 2): T almost lies on segment BE

**Printed text:** "Keep as few of these dots as possible while keeping T in their region." The guide's key says "P1 exactly three dots are necessary and sufficient … None of the fifteen joining lines contains T."

**Evidence** (`check_bonus.py`):

- T = (4, 3.2) is 0.082 units from segment BE, which is **1.34 mm at print size**, and 2.30 mm from segment AD.
- AD and BE cross at (37/9, 28/9), only 2.3 mm from T.
- T is printed as a ring of radius 3 pt with a 1.2 pt stroke, so its outer edge is 1.27 mm from its centre.
- A ruled line from B to E therefore grazes the printed T mark. A child who keeps only B and E will see the line touch T and claim two dots suffice.

The key's "exactly three" is mathematically right, but the deciding fact is a 1.3 mm offset on hand-drawn work, which a child cannot reliably check.

**Smallest fix:** move T to a point well clear of all 15 joining segments, and update the guide's coordinates and weights. For example, T = (3.2, 3.4) is at least 12.9 mm from every joining segment and is contained in the same eight triples, ABE, ACE, ADE, ADF, BDF, BEF, CDF and CEF. A simple certificate for the guide is T = 2/5 B + 2/5 E + 1/5 F.

### 2. K–1, page 3, Problem 2 (record page): three boards per D position, two answers each

**Printed:** nine record boards under "Find every split whose regions meet." Each row of three is one D position: D on AB, D beyond B and D on AC.

**Evidence** (`check_students.py`): each position has exactly two successful splits, (AB | CD, ABC | D), (AD | BC, ACD | B) and (AC | BD, ABC | D). Three identical boards per position read as "three answers each". A K–1 child may keep searching for a third that does not exist. The guide warns only the adult (p. 2: "Three copies in a row on K-1 P2 are available spaces, not a promised answer count"; p. 6).

Other record pages give six boards plus the work board, which is seven, the number of candidate splits. They do not tie a count to a single placement.

**Smallest fix:** make the per-position count not read as an answer count. Either label the record boards as extra workspace, as AGENTS.md asks for additional boards, or print one board per D position plus a row of unassigned spare boards.

### 3. All bands, page 1, region key: a "×" inside triangle HIJ on the page that says "Put D on each cross"

**Printed:** the key's "H, I, J → edge and inside" triangle contains a "×" in the same style as the D-position crosses on the work board below. Problem 1 on the same page says "Put D on each cross" (K–1) or "Put D on each cross. For each position, …" (2–3, 4–5).

**Evidence:** the key mark is drawn as two 0.8 pt diagonal strokes, the same style as the board crosses: 4.5 pt across, against 5.1 pt for the board crosses. `extract.py` lists it on page 1 of each band as a cross outside every board. Read literally, "each cross" includes it. The guide (p. 2) has to tell the adult that "The interior cross marks a location, not another group label."

**Smallest fix:** replace the key's interior "×" with a different mark, such as a small open ring, or delete it, since the shading already shows "inside".

### 4. Adult guide, route-note page (printed 23): wrong page reference and page number

**Printed:** "The middle return route P5-6 is already marked on guide p4."

**Evidence** (`check_guide.py`): the guide states that "References in the following guide use its printed page numbers". The middle route ("P5 and P6 can continue another day") is on printed p. 3, and printed p. 4 is "Adult mathematical tools". The route-note page is numbered 23 directly after printed p. 21, so there is no page 22.

**Smallest fix:** change "guide p4" to "guide p. 3" and number the route-note page 22.
