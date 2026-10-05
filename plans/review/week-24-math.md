# Week 24 (nontransitive dice and decks): math check

Scope: `lowell-math-circle-year-2/week-24/week-24-k-1.pdf` (F24-K-v2, 8 pp., Problems 1–8), `week-24-grades-2-3.pdf` (F24-23-v2, 7 pp., Problems 1–7), `week-24-grades-4-5.pdf` (F24-45-v2, 7 pp., Problems 1–7) and `week-24-facilitator.pdf` (an unnumbered overview, printed pages 1–13 and a route page printed 15). I also checked the companion `week-24-bonus.pdf` (W24-BON-v1, 4 pp., Problems 1–5) and `week-24-bonus-facilitator.pdf` (W24-BON-FAC-v1, 5 pp.). Sources: `lowell-math-circle-year-2/source/week-24/editable/src/`. I did not open the archive folders, use logs or session records. My scripts and their outputs are in [checks/week-24/](checks/week-24/). Checked October 5, 2026.

**Result: I found no errors in any student band or in the bonus companion. The base adult guide has 1 error: one sentence of a grading gate is false for half of the problem it covers. It changes no printed answer.**

## How it was checked

- The delivered base PDFs are byte-identical to `source/week-24/editable/reference-pdfs/` (same MD5). Re-running `build_packets.py` in a scratch copy reproduced the shipped `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` exactly. I did not recompile the PDFs because no pdflatex was available.
- `extract_decks.py` (needs PyMuPDF) reads every card back out of the delivered PDFs' vector drawings and text. Its output is in `out_extract_decks.txt` and `decks.json`. It records each card's numeral (or blank), its dots and the deck label beside or above it, and it separates the unlabelled card pools.
  - It found all 325 cards (K–1 121, Grades 2–3 98, Grades 4–5 106), and every deck label has its cards.
  - On every one of the 108 dotted K–1 cards, the dot count equals the numeral. No dots fall outside a card.
  - Cards have one size per layout.
- `check_math.py` (output in `out_check_math.txt`) recomputes every answer by brute force from `decks.json`. It locates each transcribed guide claim in the guide's text and compares it with the computation. Its one `FAIL` line is finding 1 below. General facts it establishes exhaustively:
  - **Fixed maxima** (9 in A, 8 in B, 7 in C, with 1–6 filling the rest): of the 90 cases, exactly 3 are cycles.
  - **All partitions of 1–9:** of the 1,680 labelled partitions into three decks of three, 15 are strict cycles (5 unlabelled). None has all three cyclic counts ≥ 6; the best cycle's smallest count is 5.
  - **Two-card rule:** over all 812 ordered pairs of disjoint two-card decks with values 1–8 (repeats allowed inside a deck), A wins a majority exactly when its sorted cards both beat B's sorted cards. No three two-card decks over 1–8 form a cycle. The majority relation is transitive.
- `check_bonus.py` (output in `out_check_bonus.txt`) does the same for the bonus companion, by exhaustive enumeration.

## K–1: checks out completely

- **P1:** A=(2,4,9) beats B=(1,6,8) 5 to 4, with winning pairs (2,1), (4,1), (9,1), (9,6), (9,8). The nine pictured pairs are exactly the nine A–B pairs, each once, labelled A then B. The same holds for P2 (B then C) and P3 (C then A).
- **P2:** B beats C=(3,5,7) 5 to 4.
- **P3:** C beats A 5 to 4. No deck wins more pairs than both others.
- **P4:**
  - The deck to choose is C against A, A against B and B against C.
  - The answer is no. The favoured deck loses all six rounds with chance (4/9)⁶ ≈ 0.8%. It finishes strictly ahead with chance 240625/531441 ≈ 45.3%, and a 3–3 tie has chance ≈ 30.1%.
- **P5:** with 3, 5, 7 or 9, A wins 3, 3, 4 or 5 pairs, so only 9 works.
- **P6:** five of the nine swaps work: A2/B1, A4/B1, A9/B1, A9/B6 and A9/B8. B then wins 5, 6, 9, 6 and 5.
- **P7:** this is impossible. All 20 splits fail, because the 9 decisive pairs cannot split evenly.
- **P8:** this is impossible. All 90 labelled arrangements fail, and the deck holding 1 never wins more than 2 of its 4 pairs.

## Grades 2–3: checks out completely

- **P1:** the cycle is A > B > C > A, each 5 to 4. No deck beats both others.
- **P2:** the answer is no, for any fixed number of results. In every matchup each bag has a win chance of 5/9 or 4/9. Every finite record of which bag won therefore has positive probability whichever way the decks are assigned.
- **P3:** exactly two arrangements besides Problem 1's:
  - (1,5,9), (3,4,8), (2,6,7) with counts 5, 5, 5;
  - (2,3,9), (1,6,8), (4,5,7) with counts 5, 5, 6.
- **P4:** only 2 and 4 work. With x = 0, 2, 4, 9, 10 the counts are (4,5,6), (5,5,6), (5,5,5), (7,5,3) and (7,5,3), in the order A over B, B over C, C over A.
- **P5:** each favoured deck wins 20 of the 36 pairs, against 16. No winner changes.
- **P6:** there is exactly one solution, A=(3,5,7), B=(2,4,12), C=(1,9,11), with counts 5, 5, 6. It is one of the 119 labelled assignments that meet all three totals. The page asks for one construction, so this is consistent.
- **P7:** this is impossible, as in K–1 P8.

## Grades 4–5: checks out completely

- **P1:**
  - Every favoured direction is 5/9.
  - No deck wins more than half its pairs against both others.
  - All three totals are 15, so totals cannot settle the question.
- **P2:** the three arrangements above are all of them (90 cases checked).
- **P3:** with values 1–6 there are 30 labelled solutions. 12 of them use every value 1–6, so either reading of "Write numbers from 1 to 6" can be done. The guide's example, A=(1,4,4), B=(3,3,3), C=(2,2,5), gives 6, 6 and 5 out of 9.
- **P4:**
  - The six-card decks win 20/36 = 5/9 each way, unchanged.
  - The four-card decks give A over B 10/16, B over C 7/16 and C over A 10/16. Every chance changes, and B–C reverses, leaving no cycle.
  - The four-card decks on the page copy exactly each smallest value.
- **P5:**
  - A/B is 2–2, so neither wins. C/D is 3–1 (C). E/F is 4–0 (E). G/H is 1–3 (H).
  - The rule (sorted coordinates both larger) holds in every case. The guide proves it in both directions.
- **P6:** neither one-card nor two-card decks can form a cycle; I searched both exhaustively. The original decks show that three cards suffice, so the minimum is 3.
- **P7:**
  - This is impossible, as the exhaustive search above shows.
  - The guide's four-step proof is correct for any distinct values. I checked its step 3 directly: if A=(a,b,9) wins at least 6 against B, then at least two B cards lie below b.

## Adult guide

The overview's facts are true as stated, with the right hypotheses:

- the 5/9 cycle, with totals not determining it;
- equal duplication preserving chances, while selective duplication need not;
- the three-card minimum for equal-size decks with no shared values;
- the two-card coordinate rule and its transitivity;
- the impossibility of 6/9 on all three edges with 1–9;
- the positive probability of every finite record of which bag won.

Every other table, solution and hint matches the computations above:

- **Tables:** the three K–1 key matrices (printed p. 3), the swap table (p. 4), the 2–3 P4 table (p. 7), the fixed-maxima table and its 15-row certificate with both columns (pp. 8–9), the four-card chance table (p. 10) and the two-card table (p. 11).
- **Formulas:** the W(a,b) ≥ 2, W(b,c) ≥ 2 and W(c,a) ≥ 3 formulas. I checked them against the full counts in all 90 cases.
- **Constructions and proofs:** the exact-total construction and its uniqueness claim, and the proofs for K–1 P7–8 and 4–5 P5–7.
- **Audit counts:** 1,680 partitions and 15 cycles.
- **Extensions:** relabelling, r×s copying and the six-round probabilities 45.3% and 30.1%.

The one exception is below.

### 1. Grades 4–5 Problem 4: the counting gate is false for the six-card decks (guide printed p. 10; low)

- **Quoted text:** "Gate: use the correct total of equally likely pairs, 36 or 16. Counting distinct printed number-pairs as equally likely gives the wrong answer."
- **Evidence:** in the six-card decks every card appears exactly twice. Each of the 9 distinct number-pairs therefore has exactly 4 physical versions, so the distinct pairs *are* equally likely. Counting them gives 5/9 for every favoured direction, which is the right answer. The guide's own P4 solution uses this fact: "Each original outcome has four physical versions."
  - The sentence is true only for the four-card decks. There distinct-pair counting gives A over B 5/9 instead of 5/8, and B over C 5/9 instead of 7/16, the wrong winner. See `check_math.py`, section "duplicated decks".
  - An adult following the gate could tell a child that a valid six-card argument is wrong.
- **Smallest fix:** "Counting distinct printed number-pairs as equally likely gives the wrong answer for the four-card decks (B over C would look like 5/9 instead of 7/16). It works for the six-card decks only because every card is copied equally."

## Bonus companion: checks out completely

- **P1:**
  - Of the 27 triples, A wins 10, B 10 and C 7, so A and B tie for most often.
  - A's cards win 0, 1, 9 triples, B's 0, 4, 6 and C's 1, 2, 4.
  - The student table has the 27 rows needed.
- **P2:** the nine first/second rows of totals and the frequency lists in the bonus guide are correct.
- **P3:**
  - A/B is 37 wins to 44 with no ties, 74 points to 88.
  - B/C and C/A are each 39 to 38 with 4 ties, 82 points to 80.
  - Every pairing totals 162 points.
  - A's one-draw advantage over B reverses.
- **P4–P5:**
  - The pure policies score (1, 10/9, 8/9), (8/9, 1, 10/9) and (10/9, 8/9, 1).
  - A bag with proportions a, b, c averages 1+(c−b)/9, 1+(a−c)/9 and 1+(b−a)/9. I checked this on a grid of 91 bags.
  - No bag beats 1 against all three, and only equal proportions reach a worst case of 1.
  - If the label is revealed, the opponent holds the chooser to 8/9.
  - The printed example (B→6 against A→4, 2 points to 0) is correct.

### Outside the math check

These are not mathematical errors; I note them for whoever revises the guide.

- The guide (printed p. 1 and p. 13) says it accompanies "F24-K-v3", but every page of the delivered K–1 packet is footed "F24-K-v2". The pre-revision K–1 PDF in the archive also says F24-K-v2.
- The route-update page is numbered 15, but it directly follows printed page 13.

### Not checked

- The cited Conrey et al. paper and the *Math Circle by the Bay* preface. Neither is available locally.
- Physical card fit, mixing and classroom timing. Digital checks cannot establish these.
