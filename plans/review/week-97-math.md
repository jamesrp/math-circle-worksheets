# Week 97 (Square remainders): math check

Scope:
- `lowell-math-circle-year-2/week-97/week-97-students.pdf`: one Grades 3–5 packet, 6 pages, one problem per page. There are no other bands and no archive folder.
  - p. 1: the opening rules, the input-3 picture with bundles of 4, the bundles-of-4 table for inputs 0–3, and Problem 1 with five input boxes.
  - pp. 2–6: Problems 2–6, each with printed square-fact cards and a work box.
- `week-97-facilitator.pdf`: 6 pages.

Sources read: `source/week-97/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md` and `SOURCES.md`. I did not run or import the package's `check_math.py`. Both delivered PDFs are byte-identical to `source/week-97/reference-pdfs/`. When I recompiled both sources with pdflatex, the extracted text matched the delivered PDFs exactly, so the sources I read are what was printed. The byte hashes differ in this TeX installation. My scripts and their outputs are in this run folder, for `plans/review/checks/week-97/`. The page renders in `render/` were only for inspection. Checked October 23, 2026.

**Result: I found 0 problems. Every printed fact card, diagram, finite answer and guide statement is correct, and so is every proof in the guide.** One note on page support, which is not a mathematical error, is at the end.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). Standard library only.
  - **The operation.** Squares are built by repeated addition. Outputs come from removing bundles one at a time, as the page describes. Python's `%` serves only as a cross-check.
  - **Fact cards.** Parses all 51 `\support` cards and checks each a × a = a². Checks which inputs each page's cards cover.
  - **Opening.** Parses the printed bundles-of-4 table and compares it with the computed outputs.
  - **Problems 1–6.** Enumerates every collection (output → inputs) and the requested maxima, minima and missing outputs.
    - Problem 3 is tested under three readings of "hide among the most possibilities": the largest single collection, the expected collection size of a uniformly chosen secret, and the fewest distinct outputs.
  - **Universal claims.**
    - The identity n² − s² = mq(mq + 2s) and the strip decomposition n² = mq·n + mq·s + s², for m < 40 and q < 40.
    - Square outputs mod 7 for inputs below 100 000.
    - The collision criterion (x² ≡ y² mod p iff x = y or x + y = p) and the (p+1)/2 count, for every odd prime below 400.
    - The product-class table QQ = Q, QN = N, NN = Q for every odd prime below 400.
    - As side facts: no odd composite below 400 has (m+1)/2 outputs, and the class table fails for 8.
  - **Guide tables.** Parses the guide's tables for sizes 5, 7, 8 and 9 (p. 3), 15 (p. 4), and 3 and 11 (p. 5), and compares each with the computed collections.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures) reads the delivered PDFs with PyMuPDF.
  - **Every student page.** Header, footer, one numbered problem per page, and problems numbered 1–6 in order.
  - **Student p. 1, the drawn dots.**
    - The input-3 picture is a 3 × 3 square grid with equal x and y spacing (18.4 pt).
    - Each bundle loop holds exactly 4 dots, with 1 dot outside, and the output picture has 1 dot.
    - Problem 1 box n holds an n × n square grid with equal spacing (11.3–11.4 pt) under the label "Input n". Box 0 says "0 counters", and there are 30 dots in all.
  - **Student pp. 2–6.** Every fact card is read back from the PDF text.
  - **Guide p. 4 strip diagram.** The outer square measures 90.71 × 90.71 pt. The shaded regions are 7 × 10 and 3 × 7 units, which leaves 3 × 3.
  - **Guide page references.** The section headings fall on the pages the overview cites (pp. 4, 5 and 6).
  - **Rebuild.** Recompiles both sources and compares the extracted text.

## Student packet, Grades 3–5 (pp. 1–6): checks out completely

- **Opening (p. 1).** 3 × 3 = 9 = 4 + 4 + 1, so the output is 1. Bundles of 4 with inputs 0–3 give 0, 1, 0, 1, as printed. "Output 1 hides two possible inputs: 1 and 3. There are two different outputs: 0 and 1" is true. The stopping rule ("until fewer than one bundle's worth remain") makes the output the unique remainder.
- **P1 (bundles of 5, inputs 0–4).** Collections: 0:{0}, 1:{1,4}, 4:{2,3}.
  - Every pair of different inputs with the same output: {1,4} and {2,3}.
  - Outputs from 0 to 4 that cannot occur: 2 and 3. These never occur for any input, which Problem 5 settles.
- **P2 (bundles of 7, inputs 0–6).** Collections: 0:{0}, 1:{1,6}, 2:{3,4}, 4:{2,5}.
  - Among outputs that occur, 1, 2 and 4 tie for the most (two inputs each), and 0 has the fewest (one).
  - Outputs 3, 5 and 6 do not occur, and the page correctly excludes them from the minimum.
- **P3.**
  - Size 7: maximum 2, at outputs 1, 2 and 4.
  - Size 8: 0:{0,4}, 1:{1,3,5,7}, 4:{2,6}. Output 1 alone has the maximum, 4 inputs.
  - Size 9: 0:{0,3,6}, 1:{1,8}, 4:{2,7}, 7:{4,5}. Output 0 alone has the maximum, 3 inputs.
  - Size 8 wins under all three readings of "most possibilities": largest collection 4 vs 2 and 3; expected collection size 3.0 vs 1.86 and 2.33; fewest outputs 3 vs 4 and 4.
  - Output 0 hides more than one input for 8 and 9, so the answer is yes.
- **P4 (bundles of 15, inputs 0–14).** Output 1 hides 1, 4, 11 and 14, whose squares 1, 16, 121 and 196 are each one more than a multiple of 15.
  - No output hides more than 4 inputs. Output 4 ({2,7,8,13}) ties, so the answer to "even more" is no.
  - The 15 cards cover inputs 0–14.
- **P5.** The cards for 7–15 give outputs 0, 1, 4, 2, 2, 4, 1, 0, 1. Every input gives an output in {0,1,2,4}, by the column/row strip argument, so the answer is no.
- **P6.** Sizes 3, 5, 7 and 11 give 2, 3, 4 and 6 outputs, counting 0, which is (p+1)/2. The rule fails for 8 (3 outputs), 9 (4) and 15 (6).
  - Every natural statement of the rule fails there: (m+1)/2, half rounded up, and the number of inputs from 0 to m/2.
  - Even a child who counts 1 as an "odd prime" under the printed definition is not misled: size 1 has one output, which equals (1+1)/2.
- **Diagrams.** All dot arrays are square grids with equal spacing. The bundle picture matches 9 = 4 + 4 + 1, and all 51 fact cards are correct.

## Adult guide (pp. 1–6): checks out completely

- **Overview (p. 1).** Every statement holds, with the right hypotheses.
  - The remainder definition is correct.
  - Periodicity holds via n² − s² = mq(mq + 2s).
  - The prime pairing is exact: x = y or x + y = p, zero is alone, and there are (p−1)/2 nonzero outputs and (p+1)/2 including zero.
  - The composite examples are true: 8 → output 1 has four inputs, 9 → output 0 has three, and 15 → outputs 1 and 4 have four each.
  - The stated limits are accurate. For example, 15 gives output 0 only from input 0.
  - The optional class rule is stated for odd primes with zero excluded.
  - The page references (pp. 4, 5, 6) point to the right sections.
- **pp. 2–3.**
  - The launch arithmetic is right, and 64 counters cover the largest square children build (8 × 8 in Problem 3).
  - All four tables (sizes 5, 7, 8, 9) match the enumeration.
  - The answers for Problems 1–3 and the points about occurring outputs and ties are right.
- **p. 4.**
  - The size-15 inventory and the sizes 1, 4, 4, 2, 2, 2 (total 15) are right.
  - So is the sequence 0, 1, 4, 2, 2, 4, 1, 0, 1, and the worked example 100 = 70 + 21 + 9 with 100 = 14·7 + 2 and 9 = 1·7 + 2.
  - The diagram is drawn to equal scale with the right regions. The general argument (7qn and 7qs removed, leaving s × s) is valid, including when q = 0 or s = 0.
  - The hint "what adding seven to a side adds" works: (n+7)² − n² = 7(2n + 7).
- **p. 5.**
  - The inventories for sizes 3 and 11 are right.
  - The pairing proof is complete. The bounds |x−y| < p and 0 < x+y < 2p are justified, and zero is alone because p | x² implies p | x.
  - Both proofs of the prime-divides-a-product lemma are correct: Bezout, and the least positive combination.
  - The composite counts 3, 4 and 6 are right. The non-opposite collisions (1, 3 mod 8; 0, 3 mod 9; 1, 4 mod 15) and "15 divides 3·5 but neither factor" are true.
- **p. 6.**
  - For size 7, Q = {1,2,4} and N = {3,5,6}. The examples 2·4 → 1, 2·3 → 6 and 3·5 = 15 → 1 (two bundles of 7, one left) are right, and the 36-counter bound is right.
  - The class table is true for every odd prime.
  - The proof is complete: cancellation gives a permutation and inverses, squares are closed under products and inverses, and a·Q lists all of N by counting.

## Note (not a mathematical error, not counted)

- **Student p. 6, Problem 6.** "Does it also work for 8, 9 or 15?" needs the outputs for inputs 0–14 with bundles of 15. The page's cards stop at "10 × 10 = 100", so 11² to 14² appear only on p. 4.
  - The guide suggests "Problems 3–4 can fill another visit, and Problems 5–6 another". A child who meets p. 6 without p. 4 must therefore compute 121, 144, 169 and 196, or have p. 4 to hand.
  - Possible fix: add the four cards 11 × 11 to 14 × 14 to p. 6, or have the guide say to keep p. 4 (or the child's Problem 4 table) available for the size-15 check.
