# Week 51 (Honest measurement ranges): math check

Scope:

- Base packet in `lowell-math-circle-year-2/week-51/`:
  - `week-51-k-1.pdf` (6 pp., Problems 1–7, footer F51-K-v2);
  - `week-51-grades-2-3.pdf` (6 pp., Problems 1–8, F51-23-v2);
  - `week-51-grades-4-5.pdf` (6 pp., Problems 1–9, F51-45-v2);
  - `week-51-facilitator.pdf` (4 pp.: three guide pages and the route update).
- Bonus companion in the same folder: `week-51-bonus.pdf` (3 pp., Problems 1–3, F51B-S) and `week-51-bonus-facilitator.pdf` (2 pp.).

Sources read: `source/week-51/editable/src/make.py` and `draw.py` (the student builder), `facilitator-src/content.json` and `route-note.json`, and `source/week-51-bonus/student/build.py`, `support.py` and `guide.md`. I ignored the archive folders. I did not run or import any writer or guide checker (`verify*.py`, `checks.txt`). My scripts and their outputs are in this folder. Checked October 10, 2026.

**Result: every range, count, witness and answer on the student pages and in both guides is correct. I found 3 problems, all minor and all on the base student pages:**

1. K-1 Problem 3 depends on "fits within 9" including 9, and no K-1 page says so.
2. K-1 Problem 4's "keep A unchanged within each comparison" can be read as freezing A in the bottom picture. Under that reading the key's 1 and 5 can't both be reached.
3. On page 1 of all three bands, the launch joins are drawn 2 mm to the right of the A + B ruler, so their ends overshoot the band's 3 and 5.

The bonus pages, the adult guide and the bonus guide check out completely.

## How it was checked

- `pdfgeom.py` is a standard-library reader for the delivered PDFs. It unpacks pdfTeX object streams and ReportLab ASCII85 streams, tracks `q/Q/cm` and colours, and records every painted path, stroked segment and text run in page coordinates.
- `check_diagrams.py` (output `out_check_diagrams.txt`) finds every ruler (ticks and numerals), every range band (light and gray rectangles), the shared-A comparison pictures, the launch joins and every answer box, all in the delivered PDFs. It compares them with my transcription of the rendered pages:
  - All 74 base-packet rulers have exactly 10.000 mm units, with numerals 0..n in order. Every 0–16 ruler is 160 mm.
  - All 57 base bands start at their ruler's 0 and are drawn exactly at the printed "L to U units".
  - The white add-ons are exactly 40 mm and 10 mm, as labelled. The repeated A is drawn at one length (5).
  - The P3 target box is 0–9 with 7–9 shaded. The K-1 P7 and Grades 2–3 P8 boxes are 9 units and the 4–5 P8 box is 12 units.
  - Problem numbers run consecutively in each packet.
  - Bonus: the working grid is 5 × 5 squares of exactly 20.00 mm, the launch grid is 3 × 2 equal squares, and the answer table is 3 × 5. The p. 2 cards are as transcribed and its ruler unit is 45 pt. The p. 3 bands on 39 pt rulers are A 3–7/B 5–9, A 2–4/B 6–8 and A 3–5/B 5–7.
  - The six print PDFs are byte-identical to the reference copies in the source packages.
- `check_math.py` (output `out_check_math.txt`) recomputes every answer:
  - It uses exact endpoints with Fractions, plus brute force over an exact 1/8-unit grid that contains every endpoint.
  - It enumerates whole-unit cases directly.
  - It searches all B cards on a 1/4-unit grid for P3.
  - It enumerates the bonus rectangles, the card logic and the gap extremes.
  - It runs random tests of both guides' general formulas: 300 cases for the interval sum and difference formulas, and 400 for the |A − B| extremes, the longer and tie conditions, and the area range. All pass.

## K-1 (6 pp.): all answers correct. See Problems 1–3 below.

- **Launch:** A 2–3 with B 1–2 joins 3 to 5.
- **P1:** the shortest join is 7 and the longest 10. The join can end exactly at 8, by whole units only 4+4 or 5+3.
- **P2:** A+B gives [7,10], C+D [8,10] and E+F [8,12]. C with D and E with F always reach 8.
- **P3:** only card B 4–5 works (joins [7,9]). B 3–4 fails at 3+3=6 and B 5–6 at 4+6=10.
- **P4:** the top gap is always 3. The bottom gap is [1,5], from 8−7 and 10−5. A+4 always ends to the right of B+1.
- **P5:** the biggest gap is 9−5=4 and the smallest 7−6=1.
- **P6:** the whole-unit ways are 8−5 and 9−6. Others exist between ticks, for example 8.5−5.5.
- **P7:** the whole-unit pairs are (4,5), (5,4) and (6,3). Three boards are printed.

## Grades 2–3 (6 pp.): all answers correct. The page-1 launch diagram has Problem 3.

- **P1:** the tight range is [7,10]. 4+3=7 and 6+4=10 defeat the claim "between 8 and 9".
- **P2:** C+D is the only pair meeting both promises, and it is also the only pairing of any two cards that does. A+B fails only "reaches 8" (7). E+F fails only "fits within 10" (12).
- **P3:** B ≥ 4 because A may be 3, and B ≤ 5 because A may be 4. Every valid card lies inside [4,5], so [4,5] is the unique widest card.
- **P4:** uncover A. The join range left has width 1 for every value of A, against width 2 for every value of B.
- **P5:** the top gap is 3 and the bottom gap [1,5].
- **P6:** the gap is [1,5] (13−12 and 15−10), always positive.
- **P7:** the middle values give 14−11=3. It is possible but not forced, because 1 and 5 also occur.
- **P8:** the pairs are (4,5), (5,4) and (6,3).

## Grades 4–5 (6 pp.): all answers correct. The page-1 launch diagram has Problem 3.

- **P1–P7:** as for Grades 2–3.
- **P8:** B = 12 − A in [3,7] forces A into [5,9]. With A's card, A is in [7,9] and B in [3,5]. A is always longer, and the gap 2A − 12 runs from 2 to 6, at (7,5) and (9,3). A = 10 would need B = 2. With whole units the gaps are 2, 4 and 6, so the answer is the same.
- **P9:** the remainder is exactly B, so the tight range is [3,4]. The claimed [1,6] is a valid but loose enclosure. A total of 7 forces A = 4 and a total of 10 forces A = 6, so remainders 1 and 6 never occur.

## Located problems

### 1. K-1, page 3, Problem 3: "fits within 9" is never said to include 9

- **Quoted text:** "Pick a card for B so the join always reaches 7 and fits within 9."
  - The only K-1 convention is on page 2: "Reaching 8 includes ending at 8."
  - The older packets add "Fitting within 10 includes ending at 10." on their page 2. K-1 has no such sentence.
- **Evidence (`out_check_math.txt`, Problem 3):**
  - The intended card, B 4–5, gives joins from 7 to 9, so it relies on both conventions. Its longest join, 4+5, ends exactly at 9.
  - If "fits within 9" means ending before 9, no printed card works: B 3–4 fails to reach 7, and B 4–5 and B 5–6 both pass 9.
  - A child who reads it that way can correctly answer "none", which the key would mark wrong. The guide's overview says equality is allowed, but nothing on the K-1 page tells the child or the reading adult.
- **Smallest fix:** add one line under the K-1 Problem 3 cards, matching the older page-2 note: "Fitting within 9 includes ending at 9." In `make.py` this is a `text(...)` line in the `if k:` branch for page 3.

### 2. K-1, page 4, Problem 4: "keep A unchanged within each comparison" can freeze A in the bottom picture

- **Quoted text:** "Find how small and how big each end gap can be. Start at 0 and keep A unchanged within each comparison; B may vary separately."
  - The bottom picture shows A at 5 next to B at 4.
  - The older bands say instead "Repeated A means the same unchanged length; B may vary separately", which ties "unchanged" to the repeated A.
- **Evidence (`out_check_math.txt`, K-1 Problem 4):**
  - The key's bottom answer [1,5] needs A to change between the two extremes: A=4, B=6 gives 1, and A=6, B=4 gives 5.
  - Read literally, "keep A unchanged within each comparison" contrasted with "B may vary" holds A fixed for the whole bottom comparison. Then the gap is A + 3 − B, which ranges only over [A−3, A−1]. That is [2,4] at the drawn A = 5, and the answer depends on which A was chosen.
  - The intro's "Each trial may use new lengths" points the other way, but the problem's own sentence is the nearer instruction. An adult following the key may then correct a child who answers 2 and 4 by leaving A where it is.
- **Smallest fix:** reuse the older wording in K-1, for example: "Start at 0. Both A's in the top picture are the same length. Each try may use new lengths for A and B."

### 3. Page 1, all three bands: the launch joins start 2 mm to the right of the A + B ruler

- **Diagram:** the two joins under "A + B: 3 to 5 units" (A|B labelled 3, and A|B labelled 5).
  - `make.py` draws the band and its ruler from x = 104 mm, but the joins from x = 106 mm (`joins(106,80,2,1)`, `joins(106,97,3,2)`).
- **Evidence (`out_check_diagrams.txt`, page 1 of each packet):**
  - The joins have the right lengths: 20 + 10 mm and 30 + 20 mm.
  - Each starts 2.00 mm right of the ruler's 0, so their right ends sit at 3.2 and 5.2 on the A + B ruler. They are visibly past the band's light/gray boundary at 3 and its end at 5 directly above.
  - The guide's launch uses this visual to show "the shortest join is 3, longest 5" by matching ends to the band.
- **Smallest fix:** draw the joins from x = 104 and move their total labels with them: `joins(104,80,2,1)+label(147,84.5,'3',10)` and `joins(104,97,3,2)+label(167,101.5,'5',10)`.

## Bonus (3 pp.): checks out completely

- **P1:** the labelled pairs (1,5), (2,4), (3,3), (4,2), (5,1) have areas 5, 8, 9, 8, 5. The minimum is 5 and the maximum 9 (3 × 3). Area 1 needs 1 × 1 (sum 2) and area 25 needs 5 × 5 (sum 10), so neither end of the promised 1 to 25 occurs. The tight range is [5,9], and it is [5,9] for real sides too. The 5-row table and the 5 × 5 grid of 20 mm squares hold every case.
- **P2:**
  - Row 1 meets in 5 to 6.
  - Row 2: card 1 (1–4) can be the false one, with witnesses 5 to 8. Card 3 (5–9) can too, with witnesses 3 to 4. Card 2 cannot, because 1–4 and 5–9 are disjoint.
  - Row 3: only card 1 can be false, with witnesses 7 to 8.
  - In every viable case the other cards' common range is disjoint from the false card, as the guide says.
- **P3:**
  - A 3–7, B 5–9: gap 0 to 6. Either strip can be longer, and they can match.
  - A 2–4, B 6–8: gap 2 to 6. B is always longer, and they never match.
  - A 3–5, B 5–7: gap 0 to 4. A is never strictly longer, and they match only at 5.
  - The design task is possible, for example A 4–6 and B 4–6. The two cards' widths can total at most 4.

## Adult guide (4 pp.): checks out completely

- **Overview:** the sum and difference formulas, their tightness for independent closed intervals, and the meaning of "reaches" and "fits within" with equality are correct, as are the cancellation of a repeated A and the loss of tightness under linked variables.
- **Material claims:** the 10 mm unit, the 160 mm rulers and the 40 mm and 10 mm add-ons match the PDFs. "Negative numbers are unnecessary" holds: the smallest gaps are 3, 1, 1, 1 and 2.
- **Keys:** every key matches my enumeration. These are the P2 table, the K-1 and older P2 answers, the P3 bounds and uniqueness, the P4 widths, the shared and separate gaps, K-1 P5 and P6, older P6 and P7, the three total-9 pairs, 4–5 P8 (including the discarded A = 10) and 4–5 P9 (including why 1 and 6 cannot occur).
- **Route update:** its problem numbers match the packets.

## Bonus guide (2 pp.): checks out completely

- **Overview:** these formulas are correct, confirmed on random intervals:
  - the area range [ac, bd] for nonnegative independent sides;
  - minimum |A − B| = max(0, a − d, c − b) and maximum = max(|a − d|, |b − c|);
  - A can be longer exactly when b > c, and B exactly when d > a;
  - a tie is possible exactly when the ranges intersect.
- **Answers:** all three answer paragraphs, their witnesses and the designed cards are correct.
- **Material claims:** the 20 mm squares, the 45 pt and 39 pt ruler units, the 2 × 3 launch example with side sum 5, the 2.5 launch length, and the 125 tiles for five kits all match.
