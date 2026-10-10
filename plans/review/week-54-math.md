# Week 54 (partitions and rebuilding): math check

Scope: `lowell-math-circle-year-2/week-54/week-54-students.pdf` is one combined packet of 9 pages with Problems 1–9. Pages 1–5 are headed Grades 2–5 and pages 6–9 are headed Grades 4–5. The adult guide is `week-54-facilitator.pdf`, 8 pages. I read the sources in `source/week-54/`: `student/students.tex`, `guide/facilitator.tex` and the READMEs. I did not run or import the packet's own `verify_math.py` or `check_answers.py`. My scripts and their outputs are in this folder. Checked October 10, 2026.

**Result: every answer, count, route and theorem in the packet and guide is correct, and every diagram matches its text. I found 2 problems, both minor wording problems in the adult guide's explanations. The student pages check out completely.**

## How it was checked

- **`pdfgeom.py`** reads the content streams of the delivered PDFs using only the standard library. It recovers every unit square, strip, outline, grid line, answer box and text label, in points.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`) rebuilds all 22 strip and row diagrams from the PDF and compares them with my transcription of the rendered pages. It checks:
  - the strip sizes and their printed number labels;
  - that every unit square is square (w/h between 0.9989 and 1.0013);
  - that the rows on p. 7 are left-aligned and touching;
  - the thick column outlines and column labels on p. 7;
  - the six 6×6 answer grids on p. 7;
  - the number of answer cells on pp. 1, 2, 5 and 8.

  There are 0 mismatches.
- **`check_math.py`** (output `out_check_math.txt`) has its own partition generator and its own join and split moves. It explores every legal route by state search and counts routes. It checks:
  - every printed case and every guide key;
  - Euler's bijection and both round trips for n ≤ 40;
  - that every route ends at the same collection, for every only-odd start with total ≤ 24 and for every start with total ≤ 18;
  - that the components of the join/split move graph each hold one only-odd and one all-different collection (n ≤ 30);
  - that conjugation is an involution and that "at most k parts" corresponds to "parts at most k" (n ≤ 20);
  - the guide's powers-of-two uniqueness lemma;
  - the physical bounds the guide states.

  There are 0 failures.
- **`check_guide_text.py`** (output `out_check_guide_text.txt`) confirms with `pdftotext` that the delivered guide PDF, not just its TeX, prints each computed key on the stated page. It also confirms that the student PDF prints the problem wording checked here. Nothing is missing.

## Grades 2–5 (pp. 1–5): the mathematics checks out and the diagrams are correct

- **p. 1 convention and Problem 1:**
  - The demo shows loose strips of 1 and 2, then "Longest first" 2 over 1, then "2 + 1". That is a non-task total of 3.
  - There are 5 collections of 4: (4), (3,1), (2,2), (2,1,1), (1,1,1,1). There are 7 collections of 5. The page prints 6 and 8 cells.
- **p. 2 Problem 2:**
  - Total 6 has 4 only-odd collections: (5,1), (3,3), (3,1,1,1), 1^6. It has 4 all-different ones: (6), (5,1), (4,2), (3,2,1).
  - Total 7 has 5 of each. The only-odd ones are (7), (5,1,1), (3,3,1), (3,1^4), 1^7. The all-different ones are (7), (6,1), (5,2), (4,3), (4,2,1).
  - Each column has 6 cells, which is enough.
- **p. 3 demo and Problem 3:**
  - Demo: (3,3,1,1,1,1) → join 3 and 3 → (6,1,1,1,1) → (6,4). Total 10, a non-task total.
  - Each case ends at one collection, whatever the route: nine 1s → (8,1) (3 routes); (5,5,3,3,3,1,1) → (10,6,3,2) (6 routes); (5,3,1) needs no join.
- **p. 4 demo and Problem 4:**
  - Demo: (4,3,2) → split 4 → (3,2,2,2) → (3,1^6). Total 9.
  - All three inputs have all sizes different, so "different again" fits.
  - Each one returns: (10,7,4,2,1) → (7,5,5,1^7) → back, total 24; (12,6,3) → 3^7 → back, total 21; (7,3,1) needs no move.
- **p. 5 Problem 5:** there are 6 pairs and the page has 8 box pairs:
  - (7,1)↔(7,1)
  - (5,3)↔(5,3)
  - (5,1,1,1)↔(5,2,1)
  - (3,3,1,1)↔(6,2)
  - (3,1^5)↔(4,3,1)
  - 1^8↔(8)

  Every reading of "connected by joining and splitting" gives these same pairs, whether by full joining or by any chain of single joins and splits. Each component of the move graph holds exactly one only-odd and one all-different collection (checked for n ≤ 30).

## Grades 4–5 (pp. 6–9): the mathematics checks out and the diagrams are correct

- **p. 6 Problem 6:** four 3s and six 1s (total 18). There are 24 reachable states, 70 join routes and a single terminal collection, (12,4,2). The answer to "Can the routes end with different collections?" is no, and it is no for every all-odd start. This was checked for every only-odd collection with total ≤ 24, and the general argument holds. The intended answer is reachable, and the question is not trivialized.
- **p. 7 demo and Problem 7:**
  - The demo is (5,3,3,1). The column outlines are 4,3,3,1,1 units high and labelled 4 3 3 1 1, and the new rows are (4,3,3,1,1).
  - Each case returns after the second exchange: (5,2,1) → (3,2,1,1,1) → back; (4,4) → (2,2,2,2) → back; (3,3,1,1) → (4,2,2) → back.
  - Every result fits the printed 6×6 grids.
- **p. 8 Problem 8:**
  - There are 10 collections of 8 with at most 3 strips, and 12 rows are printed.
  - Their exchanges are exactly the 10 collections of 8 with every size at most 3. (3,3,2) is self-conjugate.
- **p. 9 Problem 9:** the answer is yes, by Euler's theorem. Joining and splitting are mutually inverse bijections. This was verified for n ≤ 40, and the general proof holds.
- **Physical bounds:**
  - No printed case needs more than 24 units (P4 case 1).
  - The longest strip that is printed, or formed on any legal route, is 12 units (P4 case 2 and P6).

## Adult guide: the facts, keys and proofs are correct. Two minor wording problems

The overview is correct with the right hypotheses and limits:
- partitions are unordered and positive, and the empty partition is the only partition of 0;
- conjugation needs aligned, sorted rows, and it swaps the number of rows with the longest row;
- partitions with at most k parts correspond to partitions with parts at most k;
- Euler's theorem is the doubling case of Glaisher's map;
- the 2^j·u family argument holds, and both termination arguments hold;
- the limits are stated correctly. For example, (2,2) → (1,1,1,1) → (4) shows that a repeated-size input need not return, and the two catalogs coincide only for n = 0, 1.

Every key matches my enumeration: P1–P5, the two P6 routes (every arrow is one legal join), P7 and P8 (including the 1 + 4 + 5 completeness count). The proofs on p. 6 are valid: both round trips, and uniqueness by the smallest differing size.

The figures I checked are also right:
- "7,338 partitions through total 24" equals the sum of p(0..24).
- The kit and print arithmetic is right: 84 units, 28 sheets, 24 guide sheets.
- The K–1 subset of 12 greens per kit covers each named Week 1 board on greens alone. The boards' areas are sailboat 11, cat 7, hexagon 6 and diamond 8 small triangles.

### 1. Guide p. 4, Problem 3 "First-use bridge": the demo input is said to have one legal join

- **Quoted text:** "(3, 3, 1, 1, 1, 1) has one legal join 3 + 3 → 6, giving (6, 1, 1, 1, 1)."
- **Evidence:** this collection has two different legal first joins: 3+3 → (6,1,1,1,1) and 1+1 → (3,3,2,1,1). See `out_check_math.txt`, "demo legal first joins". Read literally, the sentence tells the adult that 3+3 is the only legal move. That contradicts the routes the guide itself encourages children to vary ("Different legal orders may be tried here", and Problem 6).
- **Smallest fix:** "(3, 3, 1, 1, 1, 1): one legal join is 3 + 3 → 6, giving (6, 1, 1, 1, 1)."

### 2. Guide p. 4, Problem 2 "Answer and explanation": the completeness argument for total 7 skips largest size 3

- **Quoted text:** "the largest sizes for 6 are 6,5,4,3; those for 7 are 7,6,5,4. … A largest size at most 2 cannot supply either total with distinct positive parts, since 2 + 1 = 3. These cases yield exactly the table."
- **Evidence:** the lists are correct, but the stated reason excludes only a largest size of 2 or less. For total 7 the guide also excludes 3 without saying why. The reason is that the most an all-different collection with largest 3 can hold is 3+2+1 = 6 < 7. An adult asked "why not 3 for seven?" finds no answer here. The P5 key does give this reason, for total 8.
- **Smallest fix:** replace the sentence with "A largest size of 2 or less gives at most 2 + 1 = 3, and a largest size of 3 gives at most 3 + 2 + 1 = 6, so 3 is possible for 6 but not for 7."

## Readings considered and not counted as problems

- **P5's same-collection pairs.** (7,1)↔(7,1) and (5,3)↔(5,3) need zero moves. A child who insists on at least one move would list 4 pairs. Zero-move cases are already established on the same pages, in P3 case 3 and P4 case 3, and the guide's six-pair key covers them.
- **P1 and the single-strip collection.** A single strip such as (4) counts as a collection under the shared rule ("Every strip has at least one unit"). Single-strip answers recur in P2 and P5.

## Outside scope (not mathematical)

Guide p. 8, "Verification", cites `guide-src/check_answers.py`. In the package the file is `guide/check_answers.py`. The guide README's package note says such paths are historical.
