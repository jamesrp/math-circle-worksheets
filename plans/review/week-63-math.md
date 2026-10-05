# Week 63 (cards away from home): math check

Scope:
- `lowell-math-circle-year-2/week-63/week-63-students.pdf`: one combined packet, 9 pages, Problems 1–9. Pages 1–2 are headed Grades 2–5, pp. 3–5 Grades 3–5 and pp. 6–9 Grades 4–5.
- `week-63-materials.pdf`: 3 pages.
- `week-63-facilitator.pdf`: 10 pages.

Sources read: `source/week-63/student/` (`students.tex`, `common.tex`, `materials.tex`, README) and `source/week-63/guide/facilitator.tex`. I did not run or import the writer's or the guide's `verify.py`. My scripts and their outputs are in [checks/week-63/](checks/week-63/). Checked October 5, 2026.

**Result: every answer, count, catalog, construction and theorem in the packet and guide is correct, and every diagram encodes what its text says. I found 2 problems, both minor. One is a domain choice on student p. 9 that conflicts with the guide's own advice. The other is a misworded sentence in the guide on p. 6.**

## How it was checked

- **`rows63.py`** lists rows by its own backtracking. It also computes home matches, card→home arrows and their loops, and an independent version of the two-family deletion and restoration.
- **`check_math.py`** (output `out_check_math.txt`, 102 checks, 0 failures):
  - It recomputes every answer for P1–P9 and every intersection for the four- and five-card overlaps.
  - It checks the per-row alternating weight of all 24 and all 120 rows, and the match-count distribution.
  - It finds the D-at-A, E-at-A and E-at-B/C/D branches and their two families. It checks that deletion is a bijection onto smaller home-free rows and that restoration inverts it. This holds for every n ≤ 6, every distinguished card and every destination.
  - It checks D₀…D₇ by enumeration against the recurrence and against the inclusion–exclusion sum.
  - It reads the delivered guide with `pdftotext` and compares every printed row list, table entry and count with the enumeration. That covers the P1 table, P2 groups, P3/P4 branch catalogs, all 15 P5 intersections, the P6 sizes and distribution, the P7 and P8 reduction tables, and all 44 rows of the P9 table.
  - It also checks the guide's preparation arithmetic: 223 pieces, 12 sheets and the 36,288 mm² outcome area.
  - It checks the Week 43 cross-reference. Week 43 Grades 4–5 p. 3, P5 does yield exactly BCA and CAB.
- **`pdfgeom63.py`** is a standard-library reader for the delivered PDFs' content streams (compressed object streams included). It reads back rectangles, circles, Stealth arrowheads (tip and direction) and text positions.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`, 44 checks, 0 failures) rebuilds the diagrams from the delivered PDFs:
  - the p. 1 and p. 2 convention rows with their yes/no checks;
  - every blank board and its home labels;
  - the four working boxes, which measure 173 × 70, 95, 97 and 127 mm as the guide states;
  - the p. 7 placement and its arrow pentagon;
  - all four p. 8 arrow diagrams: letters, arrow directions, regular polygons, and that each output is the stated removal of U from its input;
  - on the materials pages, card, cell, label and outcome sizes, equal-sided shapes, and the full A–C and A–D outcome decks with matching row IDs.

## Grades 2–5 (pp. 1–2): checks out

- **Convention (p. 1):** VUWX in U/V/W/X homes checks no, no, yes, yes, giving "2 home matches". All of this is correct.
- **P1:** there are exactly 2 home-free rows, BCA and CAB. No row has exactly two matches: the third card is then forced home. The page has 10 boards for 2 answers.
- **Outcome example (p. 2):** a 56 × 27 mm card showing VUWX, matching the materials format. "W in home W: yes" and "X in home X: yes" are both true for VUWX.
- **P2:** the A-home group is {ABC, ACB} and the B-home group is {ABC, CBA}. They share only ABC. The rows outside both are BAC, BCA and CAB, so 6 − 2 − 2 + 1 = 3. The printed student count 6 − 2 − 2 = 2 is the subtract-only error, as intended.
- **Materials p. 2:** the six outcome cards are exactly the six rows and the IDs match. The five labels and twelve blank A–E records are as stated.

## Grades 3–5 (pp. 3–5): checks out

- **P3:** there are 9 home-free A–D rows, 3 for each card in home A. Three of them are two reciprocal pairs (BADC, CDAB, DCBA) and six are 4-cycles. The page has 16 boards.
- **P4:** 14 rows have A away from A and B away from B: 24 − 6 − 6 + 2, where the shared rows are ABCD and ABDC. The printed check count 24 − 6 − 6 = 12 is the intended wrong count.
- **P5:** each group has 6 rows, each pair overlap 2, each triple overlap 1 (always ABCD), and the fourfold overlap 1. So 24 − 24 + 12 − 4 + 1 = 9, which matches P3's catalog.
- **Materials p. 3:** the 24 outcome cards are exactly the 24 rows, and the IDs match.

## Grades 4–5 (pp. 6–9): mathematics checks out; see Problem 1 for the p. 9 wording

- **P6:** there are 120 rows. Every k-fold intersection has (5 − k)! rows, so 120 − 120 + 60 − 20 + 5 − 1 = 44, which matches the enumeration. Every row has alternating weight 1 if it is home-free and 0 otherwise.
- **p. 7 bridge:** QRSTP in P–T homes puts P in home T. The drawn arrows are P→T→S→R→Q→P, which is exactly the card→home map, and the pentagon is regular.
- **P7:** with D in home A there are exactly 3 rows, DABC, DCAB and DCBA. Only DCBA has A in home D. The page has four A–D workspaces for these three rows. That extra space matches the rest of the packet, and I am not counting it as a problem.
- **p. 8 examples:** the top input reads as row UTQRSP. Removing the P↔U pair leaves the drawn Q→R→S→T→Q (TQRS). The bottom input UPQRST becomes P→Q→R→S→T→P (TPQRS) when T→U→P is bypassed. Both restorations return the input. The square, hexagon and pentagon are all regular. The bent P↔U arrows read correctly.
- **P8:** with E in home A there are 11 rows: 2 reciprocal ones (ECDBA, EDBCA), which reduce to the 2 home-free B/C/D rows, and 9 longer ones, which reduce bijectively to the 9 home-free A–D rows.
- **P9:** each of E's four homes gives 11 rows (2 + 9). The four branches are disjoint and total 44. The page has 16 boards per branch. The recurrence D_n = (n − 1)(D_{n−1} + D_{n−2}) holds for n ≥ 2 when D₀ = 1 and D₁ = 0. I checked it by enumeration through n = 7.

### 1. Page 9, Problem 9 (minor): "two or more distinct cards" makes the requested rule depend on an empty-row convention that the guide says not to demand

- **Quoted text:** student p. 9: "Use the two families to give a counting rule for two or more distinct cards, and explain why each row is counted once."
  - Guide p. 9 gives the key: "For two or more distinct cards, each of n − 1 destinations of the distinguished card has D_{n−2} reciprocal and D_{n−1} longer outcomes".
  - Guide p. 10 says: "Do not invoke a negative-index count or demand that children invent the empty-case convention."
- **Evidence:**
  - At n = 2 the reciprocal family reduces to the 0-card row. The rule then reads D₂ = 1·(D₁ + D₀), which is correct only if D₀ = 1.
  - A child who states the two-family rule correctly but says that zero cards have no home-free row (D₀ = 0) gets D₂ = 0. The true value is D₂ = 1 (`out_check_math.txt`: D_0..D_7 = 1, 0, 1, 2, 9, 44, 265, 1854).
  - So the printed range makes the guide's empty-case convention part of the requested answer, which conflicts with the guide's own instruction.
  - From n = 3 on, the rule needs only D₁ = 0 and D₂ = 1, which children can see directly: D₃ = 2(1 + 0) = 2, D₄ = 3(2 + 1) = 9, D₅ = 4(9 + 2) = 44.
- **Smallest fix:**
  - Print "for three or more distinct cards" on p. 9.
  - In the guide's p. 9 rule line, say "for three or more, starting from D₁ = 0 and D₂ = 1". Keep the n ≥ 2 / D₀ = 1 statement in the overview and on p. 10 as adult background.
  - Alternatively, keep "two or more" and add one guide sentence: at n = 2 the reciprocal family is the single swap, so a child's rule should treat "no cards left" as one row, and children should not be marked wrong for stating the rule from three cards.

## Adult guide: mathematically correct throughout, apart from one misworded sentence (Problem 2)

- **Overview:** these statements are all true with the stated hypotheses (distinct labels, fixed homes, own-home prohibitions only, n ≥ 2 with D₀ = 1 and D₁ = 0):
  - intersections that contain at least k specified matches have (n − k)! rows;
  - the subset-pairing cancellation proof is valid;
  - the inclusion–exclusion sum is correct;
  - in the two-family deletion, h → z gives the reciprocal family and x → z → h the longer one, and both inverses are unique;
  - the recurrence and its domain are correct, as is the remark that it does not transfer to arbitrary forbidden boards;
  - D₂…D₅ are correct, and 3 of 6 and 14 of 24 are correct.
- **Keys:** every key matches my enumeration:
  - the P1 match table;
  - the P2 groups;
  - the P3 and P4 catalogs;
  - the full P5 intersection table and the 18/14/11/9 extension;
  - the P6 size table, the ACD example (ABCDE, AECDB) and the match distribution 44, 45, 20, 10, 0, 1;
  - the P7 arrows and reductions (CB, CAB, BCA) and their inverses;
  - the p. 8 example rows (UTQRSP → TQRS, UPQRST → TPQRS);
  - all 11 P8 reductions, including "the reduction takes the last entry to the first entry";
  - all 44 P9 rows with their family split.
- **Proofs and arithmetic:** the general recurrence proof on p. 10 is valid. The preparation arithmetic (223 pieces, 48 records for 44 rows, 36,288 mm² against the 173 × 95/97 mm boxes) is correct.

### 2. Guide p. 6 (minor wording): "intersections of size k" means k-fold intersections

- **Quoted text:** "Let m be the number of its matches. The number of intersections of size k containing that row is (m choose k)."
- **Evidence:** the table just above uses "Each size" for the number of rows in an intersection (120, 24, 6, 2, 1, 1). Read that way, the sentence is false.
  - For example, with five cards a row with match set {A, C, D} (m = 3) lies in (3 choose 2) = 3 intersections that require two named matches. Each of those has 6 rows.
  - The same row lies in only (3 choose 3) = 1 intersection of 2 rows, namely ACD.
  - The count (m choose k) is correct for intersections of k named home-groups.
- **Smallest fix:** "The number of intersections of k named home-groups (k required matches) containing that row is (m choose k)."
