# Week 21 (shortest routes that touch a line): math check

Scope:

- **Student bands:** `lowell-math-circle-year-2/week-21/week-21-k-1.pdf` (W21-K-v2), `week-21-grades-2-3.pdf` (W21-23-v2) and `week-21-grades-4-5.pdf` (W21-45-v2). Each has 7 pp. and Problems 1–7.
- **Adult guide:** `week-21-facilitator.pdf`. It has 19 PDF pages: an unnumbered overview, printed pages 1/17 to 17/17, and a route update printed "19".
- **Bonus companion:** `week-21-bonus.pdf` (W21-BON-v1, 5 pp., Problems 1–5) and `week-21-bonus-facilitator.pdf` (W21-BON-FAC-v1, 5 pp.).
- **Sources read for coordinates and drawing logic only:**
  - `source/week-21/editable/src/` (`k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`, `build_packets.py`);
  - `facilitator-src/board-data.json` and `build_guide.py`;
  - `source/week-21-bonus/student-src/bonus.tex`.
- **Not used:** the packages' own checkers and audit files (`check_geometry.py`, `geometry-audit.json`, `geometry-checks.json`, `math/independent-check.py`, `guide-independent-check.py`, review notes).
- **Not opened:** archive folders, use logs and session records.

My scripts and their outputs are in [checks/week-21/](checks/week-21/). Checked October 10, 2026.

**Result: I found no mathematical errors in any student band or in the bonus companion. Every stated answer, number, proof, hint and extension in both adult guides is correct. The base guide has 1 minor diagram problem: on p. 12, two labels sit nearer another dot than their own. It changes no answer.**

## How it was checked

- **Delivered files:** all six delivered PDFs are byte-identical (same MD5) to the reference copies in `source/week-21/editable/reference-pdfs/` and `source/week-21-bonus/reference-pdfs/`.
- **`extract_geometry.py`** (output in `extract_geometry.out` and `geometry.json`) reads every page of the three base PDFs with pdfplumber. It extracts each dot, letter label, boundary line, end mark and pre-drawn route, and converts them to board centimetres.
  - All 21 boards match the TeX and the guide's `board-data.json` exactly.
  - Each label sits 0.36–0.40 cm from its own dot.
  - Every horizontal marked segment prints 15.6 cm long and every vertical one 17.0 cm. The pages are true scale with equal axes, as the guide says.
- **`check_base.py`** (output in `check_base.out`) works in exact fractions from those extracted coordinates.
  - For every assigned pair it compares the reflection answer with a brute-force scan of 400,001 contacts along the marked segment. The scan never uses the reflection formula.
  - All 35 same-side pairs on the 21 pages have their optimum strictly inside the end marks, and every reflected finish lies on the working region.
  - The inverse task is checked by exhaustive search. For 64,030 starts on a 0.05 cm grid above the line, it computes the best allowed contact exactly. The starts whose best contact is P are exactly those on the ray from P away from B′.
- **`check_guide_diagrams.py`** (output in `check_guide_diagrams.out`) reads all 12 solution diagrams in the guide back out of the PDF, counting the three vertical-board views separately. It maps them to board centimetres using the drawn end marks.
  - The scale is 9.121 pt per cm on both axes.
  - Every dot, contact, reflected point, trial point and drawn path is at its computed position.
  - The two label mismatches it reports are finding 1.
- **`check_bonus.py`** (output in `check_bonus.out`) does the following for the bonus companion:
  - It reads the bonus boards from the PDF: a 20.00 mm grid on a 160 mm board, the walls, windows, rectangle, dots and the three-panel practice visual.
  - P1–P2: it brute-forces both contacts for each contact order.
  - P3: it scans both windows.
  - P4–P5: it enumerates all 65 corner sequences per board, with an exact test for whether a segment meets the open interior of the rectangle.
  - It checks the guide's height formula and its mid-height tie rule.

Coordinates below are board centimetres from the lower-left corner of the 16.8 × 18.2 cm working region. The boundary is y = 8.7 or x = 8.4, and the end marks are at 0.6 and 16.2 (or 0.6 and 17.6 on the vertical board).

## K–1: checks out completely

- **P1:** A = (2.8,13.4) and B = (14,13.4) are at the same height.
  - Contacts at 8.4 − d and 8.4 + d give equal totals for every 0 < d ≤ 7.8, and both contacts are always between the end marks.
  - The length is strictly convex and symmetric about 8.4, so these mirror pairs are exactly the equal-length pairs. The unique shortest route touches at 8.4 and has length √213.8 ≈ 14.62.
- **P2:** the answer is yes. The drawn guesses touch at 3.5 and 11.5 and are 16.81 and 17.35 long. The optimum touches at 3473/525 ≈ 6.615 and has length √259.09 ≈ 16.10.
- **P3:** C = (13.5,4.3) is B = (13.5,13.1) mirrored in the line, so at every shared contact the two routes are equal. The answer is no.
- **P4:** the best contact is 6.3, with length √248.04 ≈ 15.75. Both legs and the reflection fit on the sheet.
- **P5:** A to B needs less string, by about 1.0 cm.
  - A to B: contact 658/71 ≈ 9.268, length √175.85 ≈ 13.26.
  - A to C: contact 1646/295 ≈ 5.580, length √203.24 ≈ 14.26.
  - Measured directly, C is nearer A (8.77 against 11.25), so the board separates the two questions as intended.
- **P6** (vertical line x = 8.4): the best contacts are at y = 2788/405, 9977/1150 and 2539/225 (≈ 6.88, 8.68, 11.28). The minima are √110.5, √311.81 and √125.89 (≈ 10.51, 17.66, 11.22). All contacts are inside the marks.
- **P7:** any start on the open ray (7.1 − 6.3t, 8.7 + 5.6t), t > 0, works, and no other start above the line does.
  - The ray runs about 9.5 cm across the board before leaving the frame at (0, 15.0).
  - Infinitely many dots therefore work.

## Grades 2–3: checks out completely

- **P1:** same board as K–1 P5. A to B needs less string.
- **P2:** no. MB = MC exactly at every contact, so the two totals always agree.
- **P3:** same board as K–1 P4. The best contact is 6.3, and the reflection argument excludes every other contact.
- **P4:** same as K–1 P6.
- **P5:** any two distinct starts on the ray from K–1 P7 work.
- **P6:** both minima are √164 = 2√41 ≈ 12.81. The best contacts differ, at 8 and 6.2. They need the same amount.
- **P7:** the unrestricted contact is 6.5, with minimum √288 = 12√2 ≈ 16.97.
  - C–D = [4.5, 8.2]: still allowed.
  - E–F = [10.2, 14.9]: not allowed.
  - C–F = [4.5, 14.9]: still allowed.
  - All three decisions hold whether or not the endpoints count: 6.5 is 2.0 cm and 1.7 cm from C and D, and 3.7 cm from E.

## Grades 4–5: checks out completely

- **P1:** same as K–1 P5.
- **P2:** same as Grades 2–3 P2. The routes are equal for every contact point on the whole line.
- **P3:** same as K–1 P4.
- **P4:** yes, both best routes touch at 6.2.
  - The heights are 3.6 : 7.2 and 4 : 8, so each crossing is a third of the way across, from A and from C.
  - The minima differ: √260.64 ≈ 16.14 for A to B and 15 for C to D.
- **P5:** the locus is the open ray in K–1 P7. Two distinct starts exist.
- **P6:** same decisions as Grades 2–3 P7.
  - In E–F the old route is not allowed. The new best route there, which the page does not ask for, touches at E and is 17.76 long.
  - In C–D and C–F the old route is allowed and still attains the old lower bound.
- **P7:** no. The unique contact is 1157/110 ≈ 10.518, with length √208.26 ≈ 14.43. The length has positive second differences at all 4,001 sample points along the segment.

## Bonus companion (W21-BON-v1): checks out completely

- **P1 (lower wall, then upper):** the walls are y = 1 and y = 7, with A = (1,3) and B = (7,5).
  - B goes to (7,9) and then to (7,−7).
  - The contacts are (11/5, 1) and (29/5, 7), and the length is √136 ≈ 11.66 units (233 mm).
  - A brute-force search over both contacts finds the same optimum.
- **P2 (upper wall, then lower):** the contacts are (19/7, 7) and (37/7, 1), and the length is √232 ≈ 15.23 units. Lower-then-upper is shorter.
- **P3:**
  - The unrestricted best contact is (3,1), which is in neither window.
  - Left window: its best point is (2,1), with length √5 + √41 ≈ 8.639.
  - Right window: its best point is (5,1), with length 4√5 ≈ 8.944.
  - So (2,1) is the unique optimum, because 41 < 45.
- **P4:** 8 of the 65 corner sequences are legal. The lower chain, 4 + 2√5 ≈ 8.472, is the unique shortest route. The upper chain is 4 + 2√8 ≈ 9.657, and the direct segment crosses the interior.
- **P5:** exactly two shortest routes tie at 9 units (180 mm).
- **Practice visual:** it is exact: B′ = (4, 2.8), N′ = (3, −2) and B″ = (4, −2.8), and leg lengths are preserved. The visual is a bent, non-optimal route, as the bonus guide says.

**Bonus guide:** every fact in it is correct:

- the overview's hypotheses;
- the two-order unfolding;
- the formula for the vertical distance in each contact order: 2H + h_A − h_B and 2H + h_B − h_A, giving 10 and 14;
- the strict-convexity certificate for closed windows;
- the claim that a shortest route bends only at corners;
- the mid-height tie rule, checked over 31 heights;
- the board scale.

## Adult guide

All of the following match the computations above:

- every coordinate, fraction, decimal, squared minimum and inequality on guide pp. 1–17 and on the route update;
- every answer diagram;
- the page finder on p. 2.

The facts checked include:

- **The overview's theorem,** with its hypotheses: strictly the same side, one straight line, and a contact that must be permitted.
- **Its limit for a restricted segment.** The p. 13 caution that "use the nearest endpoint" needs a further argument is accurate. The claim is true by strict convexity, and the bonus guide supplies that argument.
- **The p. 8 claim** that a poor A-to-B route can be longer than the best A-to-C route. The longest legal A-to-B route is 18.39, against 14.26.
- **The p. 10 claim** that S₁ and S₂ have the same contact and different minima: 12.64 against 16.86.
- **The p. 15 extensions:** reflecting the other endpoint, moving both dots outward, and making equal minima deliberately.

### 1. Grades 4–5 Problem 4 diagram: two labels are nearer another dot (guide p. 12)

- **Diagram:** "Two different journeys share the best contact", with the labels "C" and "D′".
- **Evidence:**
  - The builder places C's label up and to the left (dx = −16), but A's dot is the left one of the close pair: A = (2.2,12.3) and C = (3.2,12.7). The "C" sits 11.6 pt from A's dot and 14.8 pt from C's own dot, directly above A. A reader can take the left dot, and with it the black A–B route, for C.
  - "D′" is drawn to the right of D′ = (12.2,0.7), between it and B′ = (14.2,1.5). It is 8.8 pt from B′'s dot and 11.4 pt from its own, touching the B′ dashed leg.
  - These measurements are in `check_guide_diagrams.out`. Every dot and path is drawn in the right place, and both routes meet the same M*, so no answer changes.
- **Smallest fix:** in `facilitator-src/build_guide.py`, drop 'C' from the matching-board `dx=-16` rule, so that C's label goes above right like B's and D's. Put D′'s label below or left of its dot. Each label is then nearest its own dot.

## Not checked

- Physical fit and procedure (string lengths, folding and tracing registration, taping an extra sheet for the bonus's off-page images) have not been rehearsed. I checked only that the stated sizes match the PDFs.
- I did not rebuild the PDFs from source, because no pdflatex is available here. Instead I compared the delivered PDFs' drawn geometry directly with the TeX and with `board-data.json`.
- The cited sources (Petrunin, *Euclidean Plane and Its Relatives*; Rozhkovskaya, *Math Circles for Elementary School Students*; *Math Circle by the Bay*) were not consulted.
- Not mathematical, noted in passing: the route update page is printed "19" although it follows page "17 / 17". The overview is unnumbered.
