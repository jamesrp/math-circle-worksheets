# Week 29 (two-length builders): math check

Scope:
- `lowell-math-circle-year-2/week-29/week-29-k-1.pdf` (6 pp., Problems 1–6)
- `week-29-grades-2-3.pdf` (5 pp., Problems 1–6)
- `week-29-grades-4-5.pdf` (5 pp., Problems 1–8)
- `week-29-facilitator.pdf` (5 pp.)
- the bonus companion in the same folder: `week-29-bonus.pdf` (4 pp., Problems 1–6) and `week-29-bonus-facilitator.pdf` (5 pp.)

I ignored archive folders. My scripts and outputs are in [checks/week-29/](checks/week-29/). Checked October 5, 2026.

**Result: no stated answer is wrong in any band, the base guide or the bonus. Every count, list, last gap, certificate and proof checks out. I found 5 minor problems:**
1. In Grades 4–5, Problem 2 already contains all of Problems 3 and 4.
2. The base guide lists only one of the three K–1 P6 failures for {2,4}.
3. The base guide calls the 4/6 gaps "odd targets", but 2 is also a gap.
4. The rod kit has no 6-rods, though 4–5 P5 names 3/6 and 4/6.
5. The base guide never says that the printed strips and rulers use 1 cm per unit.

## How it was checked

- **The delivered PDFs are the reference copies.** By MD5 they are byte-identical to `source/week-29/editable/reference-pdfs/` and `source/week-29-bonus/reference-pdfs/`. I rendered every page with pdftoppm and looked at each one. Diagram data came from the vector drawings themselves, read with PyMuPDF.
- **`pdf_geometry.py` measures every diagram: 149 checks, 0 failures** (`pdf_geometry.out`, data in `pdf_geometry.json`). It reads every strip, rod key, launch example, target box, ruler and bonus rod row from the PDFs.
  - **Strips and rod keys:** every unit strip and rod key in the base packets is exactly n cm long. Each has n equal 1 cm cells and carries the label n.
  - **Rulers:** every ruler has ticks exactly 1 cm apart, labelled 0…N in order, and fits on the page.
  - **Launch example:** in all three bands, the thick 3- and 4-outlines are butted end to end on a 7-cell strip, with "3 + 4 = 7" beside them.
  - **Text against diagrams:** every range in the problem text matches its boxes. These are K P4 6–18, K P5 1–12, K P6 6–12, 2–3 P1 1–16, 2–3 P3 1–20 and 4–5 P3 18–29. The strips are K P1 {1,2,5,6,8,9,10}, K P2 {12,12,15,15} and K P3 {4,7,…,12}.
  - **Bonus rows:** the drawn rods are in proportion, 0.43 cm and 0.38 cm per unit. The launch row reads 4,3,4. The used row is 3,3,3,4 = 13 and the unused row is 3,4,4 = 11, and together they make exactly the sealed box of four 3s and three 4s.
- **`check_base.py` recomputes every base task: 88 checks, 4 deliberate failures** (`check_base.out`). It does this by dynamic programming and multiset enumeration, and finds each guide claim in the guide PDF's text.
  - It evaluates every "n = a+b+…" decomposition in the guide: 28, all correct.
  - It tests the overview over all pairs a ≠ b ≤ 15:
    - last gap = ab − a − b for coprime a, b > 1;
    - a 1-rod leaves no positive gaps;
    - with gcd > 1, every non-multiple of the gcd is a gap.
  - It runs the guide's proof steps numerically: the j-choice gives i ≥ 0, F has no representation, and 0, b, …, (a−1)b have distinct residues.
  - The 4 failures are findings 2, 3, 4 and 5 below.
- **`check_bonus.py` checks every bonus task and guide claim: 35 checks, 0 failures** (`check_bonus.out`).
  - **Words:** it enumerates the ordered words for 7, 10, 11, 14 and 18. It tests the recurrence f(n) = f(n−3) + f(n−4) against brute force for n < 40, along with the binomial alternative and the general last-rod rule.
  - **Sealed box:** it finds all 20 subsets of the box and checks complement symmetry.
  - **Added rods:** it finds the new targets for each added rod and tests the redundancy theorem (a < b ≤ 8, c < 25). It also finds the fewest-rod minima and checks that the kit is big enough.

## K–1: no errors

- **P1:** of the strips 1, 2, 5, 6, 8, 9, 10, these can be built: 6 = 3+3, 8 = 4+4, 9 = 3+3+3, 10 = 3+3+4. The lengths 1, 2 and 5 cannot (3, 4 and 7 are shown in the launch).
- **P2:** exactly two ways for each length. 12 is (4,0) or (0,3), and 15 is (5,0) or (1,3), written as (3-rods, 4-rods). The page prints two strips per target, which matches.
- **P3:** with 3 and 5, of the strips 4, 7, 8–12, only 4 and 7 are impossible. There are no strips for 1, 2 (impossible) or 6 (possible); that is harmless.
- **P4:** every length from 6 to 18 can be built, and the chains 6, 7, 8 plus 3s cover every n ≥ 6.
- **P5:** with 2 and 4, exactly the even targets work.
- **P6:** exactly {2,3}, {2,5} and {3,4} reach every target from 6 to 12. See finding 2 for the guide's failure list.

## Grades 2–3: no errors

- **P1:** only 1, 2 and 5 fail.
- **P2:** 12 is (4,0), (0,3). 16 is (4,1), (0,4). 24 is (8,0), (4,3), (0,6). The 4 ruled lines per target are enough.
- **P3:** the impossible lengths are 1, 2, 4 and 7, and 7 is the last.
- **P4:** the gaps stop after 5 for 3/4 and after 7 for 3/5. The first run of three consecutive builds is 6, 7, 8 for 3/4 and 8, 9, 10 for 3/5, as the guide says.
- **P5:** in the boxes 12–28, 13 and 17 fail; 17 is the last gap overall. The certificate 18–21 is correct, and so is the 17/10/3 argument.
- **P6:** the claim is false (2/4 never reaches an odd length). 4/7 has only finitely many gaps.

## Grades 4–5: no errors; one redundancy (finding 1)

- **P1:** the impossible lengths are exactly 1, 2 and 5 (checked to 400, with the 6, 7, 8 certificate).
- **P2:** the last gaps are 7, 11 and 17. Each guide certificate is min(a,b) consecutive builds starting just after the last gap. The argument that 11 fails (11, 6, 1) is correct.
- **P3–P4:** all of 18–29 can be built, and 17 cannot. See finding 1.
- **P5:** a pair has infinitely many gaps exactly when the two lengths share a divisor greater than 1: 2/4, 3/6 and 4/6 do; 3/5 and 4/7 do not. See findings 3 and 4.
- **P6:** 24 can be built three ways, (8,0), (4,3), (0,6). Neighbouring ways differ by trading four 3-rods for three 4-rods, and every pair of builds of the same n differs by multiples of that trade (n < 120).
- **P7:** the last gap is 23. In the boxes 19–31, 23 is the only gap. The certificates for 24–28 and the 23/16/9/2 argument are correct. The last gaps 5, 7, 11, 17, 23 all fit ab − a − b.
- **P8:** the guide's example is correct: 2/5 builds 4 and 5, so every n ≥ 4 works. The general residue argument is correct.

## Adult guide (base)

- **Overview:** true, with the right hypotheses: two positive lengths, unlimited copies, coprime with a, b > 1 for the formula, the gcd > 1 case, and the 1-rod case. It does not claim that the gaps of a gcd > 1 pair are exactly the non-multiples; that would be false, since 4/6 misses 2 and 6/9 misses 3.
- **Proofs:** the run-of-a certificate lemma, the proof of the last-gap formula (both halves) and the P8 residue proof are all correct.
- **Other claims:** the launch, the hints and the extension (2/7 and 3/4 both have last gap 5) are correct. Every answer is correct apart from findings 2–3.

## Bonus companion and its guide: no errors

- **P1:** 7 has the words 34, 43. 10 has 334, 343, 433. 14 has 3344, 3434, 3443, 4334, 4343, 4433. That makes 2, 3 and 6 words, within the 6 slots per column.
- **P2:** 18 has 11 words, 333333 and the ten listed. The 12 slots do not imply a 12th; the guide says so, and P1 already shows unused slots.
- **Recurrence:** f(n) = f(n−3) + f(n−4) with f(0) = 1 is correct, and so are the counts 2, 3, 6, 11. With rods 1 and 2 the counts are 1, 1, 2, 3, 5, 8.
- **P3:**
  - 6, 9 and 10 each have a unique stock choice: (2,0), (3,0) and (2,1). The unused rods total 18, 15 and 14.
  - 19 and 22 are impossible from the box, because their complements, 5 and 2, are not box totals.
- **P4:** a length n can be made from the box exactly when 24 − n can. The reachable list in 0–24 and the gaps 1, 2, 5, 19, 22, 23 are correct. The only subsets of total 12 are four 3s and three 4s.
- **P5:** with 3 and 5, adding 8 gives no new targets, adding 7 gives only 7, and adding 4 gives 4 and 7. The theorem "c adds nothing exactly when c was already reachable" holds.
- **P6:** the fewest rods are 4, 2, 6 and 3. The lower bounds (largest piece, and the parity of five 3/5 rods, 15 + 2y) are correct, and so is the finite-stock counterexample 3+5+8 = 16.
- **Materials:** every fewest-rod build fits the stated kit.

## Problems found

### 1. Grades 4–5, Problems 2–4 (pp. 2–3): P2's third pair already contains P3 and P4

- **Quoted text:**
  - P2: "Find the last impossible length for each pair: 3 and 5; 4 and 5; 4 and 7. For each pair, give a finite collection of builds that settles every longer target."
  - P3: "Which lengths from 18 through 29 can be built with 4-rods and 7-rods? Convince someone without checking twelve separate cases."
  - P4: "Can 4-rods and 7-rods make 17? Explain your answer."
- **Evidence:**
  - A complete answer to P2 for 4 and 7 is the last gap 17, together with the certificate 18 = 4+7+7, 19 = 4+4+4+7, 20 = 4×5, 21 = 7×3 plus added 4-rods.
  - That certificate with one or two added 4-rods is the whole of P3. "17 is the last impossible length" includes P4.
  - The guide's own P3–4 key says "use the four builds 18-21 and add 4 once or twice. Target 17 fails by the three-case argument above", which is the P2 answer.
  - The guide's first route is "4-5 P1-2", then "upper P3-8". A child who finishes P2 therefore meets two problems with nothing new in them. (`check_base.out`, "G45 P2 third pair".)
- **Smallest fix:** delete "; 4 and 7" and its answer block from P2, and drop "and 18,19,20,21 as above" from the guide's P2 key. P3–P4 then carry the 4/7 case. P7's "earlier pairs" (5, 7, 11, 17) still works, because P3–P4 establish 17. Alternatively, move P3–P4 ahead of P2 as the 4/7 entry.

### 2. Base guide, p. 2, K–1 P6 answer: incomplete failure list for {2,4}

- **Quoted text:** "The failures are {2,4}: 7; {3,5}: 7; {4,5}: 6,7,11."
- **Evidence:**
  - With 2- and 4-rods, the targets 7, 9 and 11 all fail in 6–12.
  - The {3,5} and {4,5} entries list every failure, so "{2,4}: 7" reads as the complete list. An adult could tell a child who reports 9 and 11 that they are wrong.
- **Smallest fix:** "{2,4}: 7, 9, 11".

### 3. Base guide, p. 3, Grades 4–5 P5 answer: the 4/6 gaps are not just the odd targets

- **Quoted text:** "2/4, 3/6 and 4/6 have infinitely many gaps (odd targets, nonmultiples of 3, and odd targets respectively)."
- **Evidence:**
  - The 4/6 gaps are 1, 2, 3, 5, 7, 9, …, so 2 is also impossible, because both rods are longer than 2.
  - The 2/4 and 3/6 descriptions are exact, so the parallel wording suggests the 4/6 one is exact too.
- **Smallest fix:** "(odd targets, nonmultiples of 3, and odd targets plus 2 respectively)", or "(including all odd targets …)".

### 4. Base guide, p. 1, Materials vs Grades 4–5 P5 (p. 4): no 6-rods

- **Quoted text:**
  - Guide: "ten copies each of rods 2, 3, 4, 5 and 7 on one unit scale, plus graph-paper strips and scissors for invented lengths".
  - P5: "Which pairs have infinitely many impossible lengths: 2 and 4; 3 and 6; 4 and 6; 3 and 5; 4 and 7?"
- **Evidence:** 3/6 and 4/6 need a 6-rod, which the kit does not contain (`check_base.out`, "missing [6]"). The "graph-paper strips" are offered only for invented lengths in P8.
- **Smallest fix:** add "and a few 6-rods (or cut 6-unit graph-paper strips for 4–5 P5)" to the kit line.

### 5. Base guide, p. 1, Materials: the printed unit size is never stated

- **Quoted text:** "ten copies each of rods 2, 3, 4, 5 and 7 on one unit scale … Use the printed ruler scale when placing rods directly on a worksheet".
- **Evidence:**
  - Every K–1 strip (P1–P3) and every ruler (K P4–P6, 2–3 P1) is exactly 1 cm per unit (`pdf_geometry.out`).
  - The K–1 strips are working outlines that the rods must fill. Rods of any other unit will not fit them.
  - The base guide contains no "cm" at all. (The bonus guide does say "a 1 cm unit scale".)
- **Smallest fix:** "… rods 2, 3, 4, 5 and 7 at 1 cm per unit (Cuisenaire scale); print at 100%."
