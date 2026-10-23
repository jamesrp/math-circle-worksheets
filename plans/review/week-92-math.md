# Week 92 (Fold-and-stretch predictions): math check

Scope:
- `lowell-math-circle-year-2/week-92/week-92-students.pdf`, 7 pages, one packet with two bands:
  - pp. 1–3 (header "Grades 2–3"): the move rule with the 13 → 6 map example and Problem 1 (p. 1), the band rule with the [5,10] map example and Problem 2 (p. 2), Problem 3 (p. 3).
  - pp. 4–7 (header "Grades 4–5"): Problems 4–5 (p. 4), 6–7 with the enlarged 0–1 lines (p. 5), 8 with pieces A–N and 14 result tracks (p. 6), 9 (p. 7).
  - There is no K–1 packet; the README and guide say so on purpose.
- `week-92-facilitator.pdf`, 5 pages.
- Both PDFs are byte-identical to `source/week-92/reference-pdfs/`.

Sources read: `source/week-92/student/students.tex`, `guide/facilitator.tex`, `README.md`, `QA.md`, `SOURCES.md`, `PROVENANCE.md`. I opened the package's `check_math.py` and earlier reviews only to see what they claim. I did not run or import them. My scripts and their outputs are in this run folder, for `plans/review/checks/week-92/`. Checked October 23, 2026.

**Result: every printed start, diagram, worked example and intended answer is correct, and so is every fact, proof and solution in the guide. I found 1 problem, a minor wording slip in the guide's Problem 1 solution.**

## How it was checked

The move is the tent map on the continuous track [0,16], T(x) = 2·min(x, 16 − x). A band is the set of possible positions of one marker.

- **`check_math.py`** (output `check_math.py.out`, all pass). Exact fractions throughout. It computes band images in two independent ways and requires them to agree:
  - (A) iterate the one-move image, taking the two ends and, when it lies inside, the turn at 8;
  - (B) treat T^n as piecewise linear with possible turns only at the points 16k/2^n, and take the min and max over the band's ends and those points.

  What it covers:
  - **Problem 1:** all 136 pairs of whole-number starts. It also covers how long each whole-number start takes to reach 0, and the fixed point 32/3.
  - **Problems 2–4:** every printed band. For Problem 4 it also checks all half-unit bands for when endpoint-only shading misses places.
  - **Problem 5:** the width claims, on all eighth-unit bands.
  - **Problems 6–7:** the widest [0,q], found by a grid search on 1/4096 steps and then confirmed exactly, under both readings of "through the first n moves".
  - **Problem 8 and the overview's cell claim:** every dyadic cell for n = 1–10.
  - **Problem 9:** 4,000 random rational bands with ends between ticks. It checks the guide's proof bound, the guide's whole-piece-fits step, and the zero-width exceptions.
- **`check_diagrams.py`** (output `check_diagrams.py.out`). It uses PyMuPDF on the delivered student PDF, not the TeX:
  - Every 0–16 track is 160.0 mm with 17 evenly spaced ticks, and the Problem 8 result tracks are 70.0 mm.
  - The shaded bands and their end dots are read in track units.
  - On pp. 1–2, the sloping line, the dots, the dashed readings and the thick axis highlights are converted to (input, output) values using the printed side labels.
  - On p. 5, the enlarged-scale dots are located.
  - On p. 6, the piece labels and the result-track labels are read.

The general statements are proved, not just sampled:
- **Image of a crossing band** a ≤ 8 ≤ b: [min(2a, 32 − 2b), 16]. Its width is 2·max(8 − a, b − 8), which is at least (8 − a) + (b − 8) = b − a, with equality exactly when 8 − a = b − 8. A band on one half has its width doubled.
- **Cells:** one move sends each cell of width 16/2^(n+1) affinely, with slope ±2, onto a cell of width 16/2^n. Induction then gives that each cell of the 2^n-subdivision fills [0,16] after n moves, and not after n − 1.
- **Prediction horizon:** T^k([0,q]) = [0, 2^k·q] while 2^(k−1)·q ≤ 8. So [0,q] stays in [0,2] through n moves if and only if q ≤ 2/2^n. Any q > 2/2^n already leaves [0,2] by move n, so the "only after move n" reading gives the same answer.

## Student packet, Grades 2–3 (pp. 1–3): checks out

- **Rule and map (p. 1).** The sloping line reads T(0) = 0, T(4) = 8, T(8) = 16, T(13) = 6 and T(16) = 0 against the left output labels 0–16. The right labels 0–8 are half the output at each height, so they are the nearer-end distance. The worked example's dots sit at (13, 0) and (13, 6), and distance 3 reads correctly.
- **P1 (p. 1).**
  - Pairs that meet after one move: exactly the 8 mirror pairs (0,16), (1,15), …, (7,9). The guide lists the same 8.
  - Moving farther apart on moves 1, 2 and 3: 24 of the 136 pairs do this. The guide's (0,1) has gaps 1, 2, 4, 8, then 16, then 0.
  - Every whole-number start reaches 0 within 5 moves; the odd starts take exactly 5.
- **Band visual (p. 2).**
  - The input band is shaded 5–10, with dots at 5, 8 and 10.
  - The thick path runs through (5,10), (8,16) and (10,12).
  - The distance axis is highlighted 5–8 and the output axis 10–16.
  - All of this matches "Input band 5–10 → distance band 5–8 → output band 10–16".
- **P2 (p. 2).** The bands [1,4], [10,15], [6,11] and [2,14] map to [2,8], [2,12], [10,16] and [4,16], as in the guide.
- **P3 (p. 3).**
  - [1,2] → [2,4] → [4,8] → [8,16] → [0,16].
  - [7,9] → [14,16] → [0,4] → [0,8] → [0,16].
  - Both first fill the track on move 4, and the page gives exactly 4 "after" tracks for each.

## Student packet, Grades 4–5 (pp. 4–7): checks out

- **P4 (p. 4).**
  - [6,10]: both ends go to 12, but 8 goes to 16. The full output is [12,16].
  - Over all half-unit bands, shading only between the endpoint outputs misses places exactly when 8 is strictly inside the band. So "two more starting bands" always has answers, such as [7,9] → [14,16] and [3,11] → [6,16]. The page gives two spare Start/After pairs.
- **P5 (p. 4).**
  - Getting wider: any band on one half, which doubles its width.
  - Keeping the same width: a band symmetric about 8, or the whole track.
  - Narrower: never, by the proof above.
- **P6 (p. 5).**
  - The widest bands are [0, 1/4], [0, 1/8] and [0, 1/32] for 3, 4 and 6 moves. They lie 40, 20 and 5 mm from 0 on the 160 mm enlarged lines.
  - The enlarged-scale figure is correct: the whole-track segment covers 0–1, its dot is at 0.500 units, and the enlarged dot is at 0.500 of the 0–1 line.
- **P7 (p. 5).**
  - Yes: [0, 2/2^n] works for n moves and leaves [0,2] on move n + 1. Checked for n = 0–29, and proved above.
  - No single positive band works forever.
- **P8 (p. 6).**
  - The pieces read from the PDF are A = [0,8], B = [8,16]; C–F the quarters; G–N the eighths.
  - Each fills [0,16] after 1, 2 and 3 moves respectively. The full histories are in the output.
  - There are 14 result tracks labelled A–N, each with 17 ticks.
  - The pattern continues, by the cell induction above.
- **P9 (p. 7).** Yes for every band of positive width, including bands whose ends lie between ticks; the cell argument proves it.
  - In the sample, every random band filled the track no later than the guide's bound: the first m with 16/2^m ≤ width/2.
  - Zero-width bands are genuine exceptions: 0 and 32/3 stay put.

## Facilitator guide: one minor problem

**Guide, p. 3, solution to Problem 1, first paragraph.** It says: "On each half, no two different starts have the same output, because doubling distinct distances preserves their difference."
- **Evidence:** doubling does not preserve the difference between two distances; it doubles it. Starts 1 and 3 have distances 1 and 3, a difference of 2, and outputs 2 and 6, a difference of 4.
- **Why it matters:** the guide's own overview says "On one half, a pair's distance doubles", and the 0–1 example two sentences later has gaps 1, 2, 4, 8. Read literally, "preserves their difference" contradicts both. The sentence is only correct if "difference" means "the fact that they differ".
- **Smallest fix:** change "preserves their difference" to "keeps them different (it doubles the gap)".

Optional, not an error: the next paragraph says the (0,1) separation "grows for three successive moves". It actually grows for four, with gaps 1, 2, 4, 8, 16, and then both markers are at 0. "for at least three successive moves (here four)" would match what children will see.

Everything else in the guide checks out:
- The overview's image and width formula, with the equality case.
- The dyadic cell statement with n ≥ 1.
- The exclusion of singletons, "within five moves" and the fixed point 32/3.
- The 2/2^n horizon.
- The launch arithmetic: 13 → 3 → 6, and [5,10] → [5,8] → [10,16] with 16 coming from 8.
- The Problem 2 hint: the maximum comes from the point nearest 8 and the minimum from the point nearest an end of the track.
- Solutions 2–9, including the Problem 6 maximality argument, the Problem 8 induction and the Problem 9 whole-piece step (a piece width below half the band width always fits a whole piece).
- The connections section's integer argument: after 4 moves every whole number is at 0 or 16.
- The 160 mm and 70 mm track lengths, and the page 5 and pages 1–2 references.
