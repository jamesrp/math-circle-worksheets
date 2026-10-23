# Week 94 (Calibration lab): math check

Scope:
- `lowell-math-circle-year-2/week-94/week-94-k-1.pdf`: 2 pages, Problems 1–3.
- `week-94-grades-2-3.pdf`: 4 pages, Problems 1–7.
- `week-94-grades-4-5.pdf`: 5 pages, Problems 1–7.
- `week-94-facilitator.pdf`: 5 pages.

Sources read: `source/week-94/student/common.tex`, `k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`, `guide/facilitator.tex`, plus `README.md`, `QA.md`, `SOURCES.md`, `revision-response.md` and both `build.py` files. I rendered every student and guide page at 80 dpi (`render/`) and read them all. I did not import or rely on the package's `check_math.py` files; the package build runs one of them as a side effect of the rebuild below, and I ignored its result. Scripts and outputs are in this run folder, for `plans/review/checks/week-94/`. Checked October 23, 2026.

**Result: every student problem, diagram and answer in all three bands is mathematically correct, and every solution in the guide is correct. I found 1 problem, minor and guide-only: one example sentence in the guide's Problem 7 entry is false at separation 1 ("a true stretch of 2 with exact displays avoids truncation for every allowed separation at least 1"). It does not change any answer.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`: all checks pass, 1 NOTE, which is the finding below). Exact fractions throughout. Data are parsed from the `.tex` sources: strip lengths, the unit row, ruler labels, the extras, the Problem 4 rows, the Problem 6 boxes and the 4–5 Problem 4 reports.
  - K–1: the length of each strip in every placement on the 2–14 ruler. Every placement with one end at 7 and both ends on printed labels. Every pair of supplied pieces covered by a third, and also with duplicates and with the 12-square row as a possible cover.
  - 2–3: all worlds for reports 7 and 10, found by search rather than by formula. The difference invariant. The three standard rows. The partner game for every extra and every supplied standard. Every single-report repair of each box, found by searching report values 0–39. An exhaustive check of Problem 7: all 933,120 puzzles with three lengths from 1 to 12, any extra, and one wrong report from 0 to 30 have exactly one repair, and it is the intended one.
  - 4–5:
    - The 21-machine game: which single lengths always identify the machine, ambiguous reports for each supplied strip, lucky single reports, every pair of supplied strips, and end-to-end combinations of strips.
    - Problem 2: candidates and separating second lengths.
    - Problems 3 and 4: rules, uniqueness, and every one-report repair, with positivity checked.
    - Problem 5: the tables.
    - Problem 6: an exact feasibility test for each stretch, checked against a 1/8-grid brute force over the true reports, with the witnesses checked.
    - Problem 7: the worst-case width after positivity truncation, for every integer pair from 1 to 10, maximised over a grid of displays consistent with a positive-stretch machine. Also one reference repeated.
  - Guide: every number in every solution, plus the Problem 7 remark.
  - Geometry, read from the delivered PDFs with PyMuPDF:
    - Every ruler tick gap is 12.000 mm: 1 ruler on K–1 p. 1, 5 on p. 2, and the example rulers.
    - The cut strips are 2, 3, 4 and 6 units by 1 unit on all three first pages.
    - The unit row is 12 squares of 12 mm.
    - In the K–1 example, the placed 1-unit strip spans exactly one tick gap (8–9).
    - The 2–3 example blocks are 1 + (1 + 1). The 4–5 p. 1 example is 1 → 1 + 1 + 1 + 1.
    - The 4–5 p. 3 example is three 1-unit squares, three 1½-unit pieces (4½), and a 3½-unit report bar.
- **`rebuild_compare.py`** (output `rebuild_compare.py.out`): rebuilds all four PDFs from the sources into a temporary folder. Every page's text and every vector drawing (to 0.1 pt) is identical to the delivered PDFs, so the sources I parsed are what is printed. The bytes differ from the delivered files on this TeX Live, so the README's "byte-identical clean rebuilds" depends on the TeX installation. That is not a math issue.

## Grades K–1 (2 pages): checks out

- **Opening example:** a 1-unit strip placed at ticks 8–9, marked at 8 and 9, length 1. Geometry exact.
- **P1:** A = 2, B = 3, C = 4, D = 6 units in every placement. The ruler starts at 2, so reading the right-end label is visibly wrong, which is the point.
- **P2 (one end at 7, both ends on printed marks):** A at 5–7 or 7–9; B at 4–7 or 7–10; C at 3–7 or 7–11; D at 7–13 only, because 1–7 runs off the 2–14 ruler. There are four rulers, one per strip, so a child draws both placements on one ruler. That is workable.
- **P3:** only A + C = D. The other sums of two distinct pieces (5, 7, 8, 9, 10) match no strip, and the 12-square row matches no pair. With duplicate pieces, A + A = C and B + B = D would also work. The guide correctly says each kit has one of each.

## Grades 2–3 (4 pages): checks out

- **Opening / P1:** report = length + extra, with the extra from 1 to 6. One known strip always identifies the extra. Reports from the supplied strips are at most 12, so they fit the 12-square row.
- **P2:** exactly six pairs: (6, 9), (5, 8), (4, 7), (3, 6), (2, 5), (1, 4) for extras 1–6. The page gives seven rows, so it does not reveal the count. Every length can be built with 12 cubes.
- **P3:** P is never longer than Q. Q is always exactly 3 longer.
- **P4:** the extras are 4, 2 and 6, all allowed. The hidden lengths are (5, 8), (7, 10) and (3, 6).
- **P5:** for every extra, the hidden lengths 7 − e and 10 − e are positive, and any one supplied standard reveals e.
- **P6:** I has extras 3, 3, 4, and the only repair is 6 → 10 changed to 9. II has extra 6 throughout and is possible. III has extras 1, 2, 1, and the only repair is 4 → 6 changed to 5. The search over all report values found no other single-report repair.
- **P7:** every one-wrong-report puzzle has a unique repair (exhaustive, above). The guide's extension, that two bad reports can leave the answer ambiguous, is also right.

## Grades 4–5 (5 pages): checks out

- **P1 (21 machines):** two different supplied strips always identify the machine.
  - No supplied strip does so in one request on every report. D is ambiguous only at reports 12 and 18.
  - Every length of 7 or more identifies the machine in one request, and no length of 6 or less does.
  - Lucky single reports exist, such as 6 → 24, which forces 3 copies and extra 6.
- **P2:** 2 → 6 leaves (1, 4), (2, 2) and (3, 0).
  - Every second length other than 2 separates them. Length 3 gives 7, 8, 9.
  - "Could a single first request ever identify a machine?" Yes, for example 2 → 2, 2 → 11 or 6 → 24.
- **P3:** A is y = 2x + 4, giving 4, 12, 24. B is y = x + 6, giving 6, 10, 16. Two distinct inputs fix the line, so no other rule gives the same two reports.
- **P4:** not collinear (steps 4 and 5). There are exactly three repairs, all with positive stretch:
  - 2 → 7 changed to 6, with y = 5/2·x + 1;
  - 4 → 11 changed to 11½, with y = 9/4·x + 5/2;
  - 6 → 16 changed to 15, with y = 2x + 3.

  11½ is allowed by the p. 3 rule "Fractions are allowed".
- **P5:** the guide's tables (2x + 3, with the last entry changed from 19 to 20) fit and disagree at 8. No number of tests below 8 can force the report at 8 when no form is promised.
- **P6:** pair A's stretch is in [1, 3], attained by y = x + 7 (true reports 9, 11) and y = 3x + 1 (true reports 7, 13). Pair B's stretch is in [7/4, 9/4], attained by y = 7/4·x + 11/2 (true reports 9, 23) and y = 9/4·x + 5/2 (true reports 7, 25). Both ranges are strictly positive, every value between the ends is feasible, and nothing outside them is.
- **P7:** the worst-case width is exactly 4/D for every pair, after positivity truncation, maximised over all consistent displays. The unique best pair is 1 and 10, with width 4/9. One reference, even repeated, fits every positive stretch. Both answers match the intended outcome.
- **Diagrams:** 1 + 1 + 1 + 1 = 4 (p. 1); 3 × 1½ = 4½, minus 1 = 3½ (p. 3, drawn to scale); 3 × 2 + 1 = 7, plus ½ = 7½ (p. 5).

## Adult guide (5 pages): correct except problem 1 below

- **Overview:** all of it is true with the stated hypotheses:
  - the shared-offset cancellation and the joint shift x ↦ x + t, b ↦ b − t;
  - the two-point formulas, assuming b > 0 and any real a;
  - one known input leaves every positive slope possible;
  - the bounded-error interval [(Δ − 2e)/D, (Δ + 2e)/D] ∩ (0, ∞), whose untruncated width is 4e/D, so the worst case is 4e/D;
  - an infimum at 0 when the interval is truncated;
  - the printed examples avoid that truncation;
  - finite tests cannot force an untested value.
- **Solutions:** every K–1, 2–3 and 4–5 solution, hint and extension listed above matches my computations. That includes "the intervals for copies 1 and 2 overlap for every integer input at most 6", "input 7 gives 7–13, 14–20, 21–27" and the 20 strips for five kits.

## Problems found

### 1. Guide p. 5, Grades 4–5 Problem 7: the example of an untruncated interval fails at separation 1 (minor, guide only)

- **Quoted text:** "Positive stretch can truncate a particular observed interval but cannot improve the largest possible width; for example, a true stretch of 2 with exact displays avoids truncation for every allowed separation at least 1."
- **Evidence** (`check_math.py.out`, NOTE line): with true stretch 2, exact displays and separation D, the displayed difference is Δ = 2D. The untruncated interval is [2 − 2/D, 2 + 2/D].
  - At D = 1, for example references 1 and 2, this is [0, 4]. Requiring a positive stretch removes 0, so the possible stretches are (0, 4]. Truncation does occur, and there is no smallest possible stretch.
  - This is exactly the infimum case that the guide's own overview warns about ("a lower endpoint at zero is an infimum, not an attained smallest positive stretch").
  - The width is still 4 = 4/D, so the conclusion that the worst case is 4/D for every pair, and that the best pair is 1 and 10, stays true. Only the example is wrong.
  - An adult who works the D = 1 case would see the sentence fail.
- **Smallest fix:** change "a true stretch of 2" to "a true stretch of 3". The lower endpoint is then 3 − 2/D ≥ 1 > 0 for every D ≥ 1, which `check_math.py` confirms for D = 1 to 9. Alternatively, keep 2 and say "every allowed separation greater than 1".

## Notes for the card stage (not mathematical errors)

- 4–5 Problem 1, "How few requests can you manage?": with the kit, B and C laid end to end make a known 7, which identifies the machine in one request. So the in-kit answer is 1 if children combine strips and 2 if they do not. The guide covers this under "If arbitrary known lengths can be built" and "State which materials a child chose", but does not name B + C = 7. Naming it would help an adult who sees a child combine strips.
- K–1 Problem 2 gives one ruler per strip, while A, B and C each have two placements. A child draws three marks on one ruler (for A: 5, 7, 9). That is legible, and the guide lists the placements separately.
- Rebuilt PDFs on this TeX Live match the delivered files in text and geometry but not in bytes (see `rebuild_compare.py.out`).
