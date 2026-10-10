# Week 38 (Seams and cuts): math check

Scope: the current student packets in `lowell-math-circle-year-2/week-38/`:
- `week-38-k-1.pdf` (6 pp., Problems 1–7, footer F38-K-v3);
- `week-38-grades-2-3.pdf` (6 pp., Problems 1–7, F38-23-v3);
- `week-38-grades-4-5.pdf` (6 pp., Problems 1–7, F38-45-v3);
- the adult guide `week-38-facilitator.pdf` (7 pp.: six guide pages plus the appended route update).

The companion bonus packet (`week-38-bonus.pdf`, W38-BONUS-v1, 3 pp.) and its guide (`week-38-bonus-facilitator.pdf`, 2 pp.) were also checked in full. The two `archive-*` folders were ignored. The six delivered PDFs are byte-identical to the `reference-pdfs/` copies in `source/week-38/editable/` and `source/week-38-bonus/`. I read the generators (`src/make_packets.py`, `src/examples.py`, `week-38-bonus/student/build.py`), but every check reads the delivered PDFs. Checked October 10, 2026.

**Result: every answer, count and theorem in the base packet and its guide is correct, and every base diagram matches its text. I found 3 problems:**
1. **Bonus, page 2 (the joining visual for Problem 2), and the bonus guide's launch.** The R row says to "align the same marks". With the marks as printed, that join is M, not R. This is the only substantive problem.
2. Minor: the base guide never says that on B the slid arrow comes back on the other face of the paper.
3. Minor, not mathematics: the bonus guide garbles the band names in its kit counts.

## How it was checked

All scripts are in this folder. Each finds the repository from its own location, four folders up from `plans/review/checks/week-38/`, and otherwise searches upward. They use Python 3, pypdf and Poppler's `pdftotext`. I also ran them from a mock `plans/review/checks/week-38/` tree.

- **`common.py`** extracts the drawing from each delivered PDF with pypdf. It tracks the content stream's transformation matrix and records every filled or stroked path, with its colour, dash pattern and clip box, in millimetres from the top-left corner. Word boxes come from `pdftotext -bbox`.
- **`surfaces.py`** is my own cell-complex model of paper bands. A band is a cycle of strips cut into square cells, with each seam given by how it pairs the corner heights of the two ends. Cuts and removed cells are allowed. Union-find then computes:
  - the pieces;
  - the boundary circles, after checking that every boundary vertex has degree 2;
  - the Euler characteristic and orientability of each piece, which name it as an annulus or a Möbius band;
  - which circles are old edges and which are cut edges;
  - how a transverse arrow is carried along a row of cells.

  It uses no packet or guide answer.
- **`check_math.py`** → `out_check_math.txt`: 41 checks, all pass. It builds A and B uncut and with the centre cut. It brute-forces every placement of 2 or 4 dots on distinct boundary sides, for Problems 2, 3, 5, 6 and 7. It compares the results with every answer and table in the guide, transcribed by hand.
- **`check_diagrams.py`** → `out_check_diagrams.txt`: 144 checks, all pass. For every band and page it reads, from the PDF:
  - every recipe's corner marks, end arrows, dashed middle line and U/L labels, and builds the band each recipe encodes;
  - the worked example's cylinder;
  - the washer (circle radii, which dot is on which circle) and its rings;
  - the five four-dot pictures, by counting the dots inside each ellipse;
  - the Grades 4–5 arrow picture;
  - the guide's A/B seam diagram on p. 2;
  - footers and problem numbering.
- **`check_bonus.py`** → `out_check_bonus.txt`: 56 checks pass and 1 fails. The failure is finding 1. The script rebuilds each printed bonus band from the PDF:
  - P1: seam, lane lines and end labels;
  - P2: the local visual's alignment lines and the four seam words;
  - P3: holes and notches, rasterised at 0.5 mm with the clip boxes respected.

  It also checks the guide's general claims for every lane count n ≤ 8, and every M/R word of length up to 6.

## Diagrams, all bands: correct

- **Recipes.** Every recipe has one dot and one square at each end. The worked-example input and every A have the dot at both top corners: under "Join • to • and □ to □" that is the matching seam, so the band is an annulus. Every B has the dot top-left and bottom-right: the reversing seam, a Möbius band.
- **Arrows, middle line and labels.** Both end arrows run from the square to the dot. The dashed middle line is exactly at mid-height. U is above it and L below.
- **Same in every band.** The recipes on pp. 1, 4 and 5 are identical in all three bands.
- **Worked example.** The cylinder's seam carries the dot on its top rim and the square on its bottom rim, as the input recipe requires.
- **Washer (p. 2).** The circles are concentric, R = 29 mm and r = 13 mm, with equal x and y scale. P and Q lie on the outer circle and R on the inner one. The rings group {P, Q} and {R}, which matches.
- **Four-dot pictures (p. 3; p. 6 in K–1 and 2–3).** Top to bottom they are 4, 3+1, 2+2, 2+1+1, 1+1+1+1, the order the guide's p. 3 key gives. Each picture has four dots, each inside exactly one ring, and the rings are disjoint.
- **Grades 4–5 p. 6.** Both arrows point from the upper long edge to the lower one, matching "pointing from U toward L".
- **Guide p. 2.** The A diagram is the matching seam and the B diagram the reversing one. The cell model confirms the captions "U → U, L → L" and "U → L, L → U" for the centre cut.

## K–1: checks out completely

- **P1.** A has 2 closed edges (the top closes on itself, as does the bottom). B has 1, made of the top and bottom edges together.
- **P2.** On A, a pair of dots can share a trip or not. On B every pair shares a trip, so "no one trip reaches both" is impossible.
- **P3.** On A: 4, 3+1, 2+2 yes; 2+1+1, 1+1+1+1 no. On B: only 4.
- **P4.** A gives 2 pieces, B gives 1.
- **P5.** Yes for both: each cut piece is an annulus with two edges.
- **P6.** Cut A: all five pictures. Cut B: 4, 3+1, 2+2.
- **P7.** Possible for cut A (one dot on each of 4 circles, which covers both pieces). Impossible for cut B (4 dots, 2 circles).

All of this matches the guide's p. 3 key and table.

## Grades 2–3: checks out completely

- **P1–2.** 2 edges and 1 edge. On B the "cannot" request is the impossible one.
- **P3.** As K–1.
- **P4.** 2 and 1 pieces.
- **P5.** Cut A puts U and L in separate pieces. Cut B makes one piece through both halves. Both answers are yes.
- **P6.** The guide's table is right in every cell.
- **P7.** As K–1.
- **Proof with the materials.** On cut B, one circle is exactly the whole old edge and the other exactly the whole cut edge. On cut A, each piece has one old edge and one cut edge.

## Grades 4–5: checks out completely

- **P1–2.** As above.
- **P3.** The guide's "A: yes, yes, yes, no, no. B: yes, no, no, no, no" is right.
- **P4.** Cut A: 2 pieces with 2 + 2 boundary components. Cut B: 1 piece with 2.
- **P5.** The half-strip cycles are (U)(L) and (UL). The cut-B piece is orientable with χ = 0 and b = 2, so it is an annulus.
- **P6.** Along the middle row, the arrow returns with sign +1 on A. On B it returns with −1 after one trip and +1 after two. Only B's middle row closes after one trip; every other row needs two.
- **P7.** All five pictures for cut A; 4, 3+1, 2+2 for cut B.

## Adult guide (base): correct, with one minor gap (item 2)

**The overview's facts hold.**
- A matching seam gives an annulus with 2 boundary circles; a reversing seam gives a Möbius band with 1.
- The centre cut of A gives 2 annuli with 4 boundary circles in all. The centre cut of B gives 1 annulus with 2.
- The arrow reverses on B and is restored after two trips.
- With b boundary circles, the realizable four-dot pictures are exactly the partitions of 4 into at most b groups. I checked this for b = 1, 2 and 4 by brute force.

**Its stated limits are right.** An off-centre cut is a different experiment: cutting B at 1/3 gives a Möbius band plus an annulus. Seam parity alone fixes the abstract type, as the optional questions say.

**The keys and the proof notes on p. 6 are right.** Every key on pp. 3–5 matches the brute-force results. On p. 6:
- the [0,1] × [−1,1] model and the cycle argument are correct;
- "two reversing seam identifications compose to the identity" holds with the fibre parametrised by t;
- the five partitions of 4 are complete.

I did not check the Hatcher and NRICH page references: those sources are not in this checkout.

## Bonus packet and bonus guide

**P1 (p. 1): correct.**
- The corner marks encode M for "3 lanes / M" and "4 lanes / M", and R for the two R recipes.
- The lane lines are equally spaced, and the end labels sit at the lane centres. Under "join matching corner marks", matching labels agree with the corner marks.
- Results:
  - 3M: 3 annuli, 6 edges.
  - 3R: lanes 1+3 form an annulus and lane 2 a Möbius band, so 2 pieces with 2 + 1 edges.
  - 4M: 4 annuli, 8 edges.
  - 4R: lanes 1+4 and 2+3 form 2 annuli, 4 edges.
- Only 3R has a one-edge piece next to a two-edge piece.
- The overview's lane rule (n annuli for M; ⌊n/2⌋ annuli plus a Möbius band for odd n under R) holds for n = 1 to 8.

**P2 (p. 2): the seam words and answers are right.** The printed words are MMM, MMR, MRR, RRR, giving 2, 1, 2, 1 edges, as the guide says. The parity rule holds for all 126 words of length 1–6, including unequal strip lengths. The guide's four-strip designs are right: RMMM gives 1 edge; RRMM and MMMM give 2. The visual above P2 is item 1.

**P3 (p. 3): correct.**
- Rasterised from the printed shapes: A/M has 3 edges, B/R 2, C/R 1 and D/M 3, each one piece.
- D's two half-disks sit at the same height (0.5 of the width) at both ends, so the M seam closes them into one hole. Offset half-holes would give two openings and 4 edges, as the guide's extension warns.
- The guide's four-edge designs are right: M with 2 disks gives 4 edges and R with 3 gives 4. M with 1 disk and R with 2 give only 3.

**Guide arithmetic: correct.**
- Per pair, 4 + 3 + 4 + 2 = 13 strips.
- For six kits, 78 = 24 + 18 + 24 + 12 strips, and 72 = 6 × 12 dots.
- The lane cuts are at 80/3 and 160/3 mm, and at 20, 40 and 60 mm.

## Problems found

### 1. Bonus p. 2, the R row of the joining visual, contradicts R (and the bonus guide repeats it)

**Where.** Bonus packet W38-BONUS-v1, page 2, the unnumbered visual above Problem 2:
- the instruction "Keep each mark attached to its corner. Join short ends.";
- three columns, "before joining | align the same marks | seam record", with an M row and an R row.

**What is printed.**
- **"Before joining" (both rows the same):** strip 1's right end has the dot at the top corner (33.5, 45.2 mm) and the square at the bottom (33.5, 55.0). Strip 2's left end also has the dot on top (41.0, 45.2) and the square at the bottom (41.0, 55.0). The R row repeats this at y = 64.2 and 74.1.
- **"Align the same marks", M row:** straight grey lines pair dot with dot and square with square.
- **"Align the same marks", R row:** crossing grey lines, from the left dot (91.7, 65.0) to a right dot drawn at the bottom (121.4, 73.4), and from the left square (bottom) to a right square drawn at the top. They pair dot with dot and square with square, exactly as in the M row (`out_check_bonus.txt`, "row R").

**Why it is wrong.** Strip 2's marks are on the same corners in both rows. A join that sends dot to dot and square to square therefore sends top corner to top corner, which is the M identification (t ↦ t), however the strip is turned in space. R needs t ↦ −t: strip 1's top corner meets strip 2's bottom corner. Strip 1's dot must therefore meet strip 2's square.

Physically: give strip 2 a half-turn and its square comes to the top, so taping the ends together puts dot against square. An adult who demonstrates "same-mark alignment with M versus R" as the bonus guide asks (p. 2, "Before P2, demonstrate the student local two-strip visual: unchanged corner marks on two short ends, same-mark alignment with M versus R") cannot produce R.

The P2 strips are reusable and marked the same way at both ends ("mark upper/lower corners with distinct dot/square symbols"). A child who joins same marks at every seam, as the visual and page 1's "join matching corner marks" say, builds only M seams. All four printed circles then have 2 closed edges, not 2, 1, 2, 1 (cell model: `out_check_bonus.txt`, "taken literally"). That hides the parity rule P2 asks children to find.

The R row is consistent only if the grey lines are read as the motion of strip 2's own corners during the half-turn. But the column is titled "align the same marks", and the M row reads as a join.

**Smallest fix.** Two changes are needed.
- **Student page.** In the R row's middle column, keep strip 2's half-turned end drawn as square-over-dot, but join it to strip 1 with straight lines: dot to square at the top, square to dot at the bottom. Retitle the column "align the ends". A caption under the visual can say "M: dot meets dot. R: half-turn, so dot meets square." Alternatively, keep the crossing lines but end them at the opposite mark.
- **Bonus guide p. 2.** Change "same-mark alignment with M versus R" to "M joins dot to dot; R, after a half-turn, joins dot to square".

Page 1's "join matching corner marks" can stay. It is right for the P1 recipes, whose R ends are printed with the marks already reversed.

### 2. Minor, base guide pp. 2 and 5 (Grades 4–5 Problem 6): the arrow returns on the other face of B

**Where.**
- Student page: Grades 4–5 page 6, Problem 6: "Slide it along the middle line for one full trip, keeping it across the strip … Compare the returning arrow with its starting position."
- Guide p. 2: "Check that the arrow can slide without being detached, flipped by hand, or rotated within the strip."
- Guide p. 5: "On B it returns L→U relative to the original location."

**What is missing.** All three statements are true. But a Möbius band is one-sided: an arrow held against one face and slid once along the middle line comes back to its start on the opposite face of the paper. On A it comes back on the same face.

The guide never says this. An adult rehearsing the procedure, which the guide says has not been done, may read the face change as the forbidden "flipped". If U and L are marked on one face only, the child must also read the comparison through the paper.

**Smallest fix.** Add one sentence to guide p. 5, Problem 6: "On B the arrow comes back to its start on the other face of the paper; that is the one-sidedness, not a flip. Mark U and L on both faces, or read the direction from the long edges." Optionally add "on both faces" to the U/L preparation on p. 2.

### 3. Minor, not mathematics: garbled band names in the bonus guide's kit counts

**Where.** Bonus guide p. 1:
- "For six full pair-sized kits across KK11 / 3333 / 445: 78 strips …"
- "two P3 kits at KK11, two P1/P2 kits at 3333 and two full kits at 445".

The same text is in `source/week-38-bonus/guide.md`.

**Problem.** These read as K–1 / 2–3 / 4–5 with doubled characters. The arithmetic is right, but the allocation by band cannot be read as printed.

**Fix.** Replace them with "K–1 / 2–3 / 4–5" and "at K–1 … at 2–3 … at 4–5".
