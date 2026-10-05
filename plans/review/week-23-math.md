# Week 23 (sorting networks): math check

Scope: `lowell-math-circle-year-2/week-23/week-23-k-1.pdf` (F23-K-v2, 6 pp., Problems 1–6), `week-23-grades-2-3.pdf` (F23-23-v2, 6 pp., Problems 1–6), `week-23-grades-4-5.pdf` (F23-45-v2, 7 pp., Problems 1–7) and `week-23-facilitator.pdf` (an unnumbered overview page plus numbered pages 1–12). Sources: `lowell-math-circle-year-2/source/week-23/editable/src/`. The companion `week-23-bonus.pdf` and `week-23-bonus-facilitator.pdf` were not checked. I opened no use logs or session records. My scripts and their outputs are in [checks/week-23/](checks/week-23/). Checked October 5, 2026.

**Result: I found no errors in any student band. The adult guide has 1 error: a wrong output in one trace. It changes no answer.**

## How it was checked

- The delivered PDFs are byte-identical to `source/week-23/editable/reference-pdfs/` (same MD5). Re-running `build_packets.py` in a scratch copy reproduced the shipped `k-1.tex`, `grades-2-3.tex` and `grades-4-5.tex` exactly. I did not recompile the PDFs because no pdflatex was available.
- `extract_networks.py` (needs PyMuPDF) reads every diagram back out of the delivered PDFs' vector drawings and text. Its output is in `out_extract_networks.txt` and `networks.json`. It records each machine's lanes, its bars in left-to-right order, the endpoint dots, the card banks (dot counts or numerals), the K–1 start columns and the 4–5 notation examples.
  - Every bar has endpoint dots on exactly its two lanes. Long bars ((1,3), (2,4), (1,4)) have no dot on the lanes they cross.
  - No two bars in a machine share a position, and lane spacing is uniform within each machine.
  - The guide's drawings of S3, S4 and N4 (printed p. 3) and its drawing of the lower 4–5 P5 candidate (printed p. 10) match the bar lists printed beside them.
- `check_math.py` (output in `out_check_math.txt`) is my own compare-exchange simulator. It takes each machine from `networks.json`, recomputes every answer by brute force and compares each stated guide answer with the result. General facts it establishes exhaustively:
  - **Fewest bars:** 3 lanes need 3 bars (no list of 2 or fewer works; there are 6 three-bar sorters). 4 lanes need 5 (all 1,296 four-bar lists fail; there are 12 five-bar sorters). With neighbouring lanes only, 4 lanes need 6 (all 243 five-bar lists fail; there are 16 six-bar sorters).
  - **Zero–one principle:** I checked all 121 lists of up to 4 bars on 3 lanes and all 9,331 lists of up to 5 bars on 4 lanes. Each sorts every 0–1 start exactly when it sorts every input in {1..n}ⁿ, repeats included.
  - **Swap/stay records:** for the same lists, no record is shared by two distinct-value starts that both finish sorted, and a k-bar list never produces more than 2ᵏ records.

## K–1: checks out completely

- **P1:** the machine is (1,2),(2,3). The six pictured starts, read top to bottom, are 123, 132, 213 / 231, 312, 321. The starts to circle are 123, 132, 213 and 312. Starts 231 and 321 both finish 213.
- **P2:** the minimum is 3 bars.
- **P3:** the upper machine is (1,2),(2,3),(1,2). It sorts all six starts. The lower machine is (1,2),(1,2),(2,3). It fails exactly on 231 and 321, which finish 213.
- **P4:** the left set is blank, blank, one dot; the right set is blank, one dot, one dot. Both machines exist, and two bars is the minimum for each. For the left set there are exactly three two-bar machines: (1,2),(2,3); (1,3),(2,3); and (2,3),(1,3). For the right set there are also three: (1,2),(1,3); (1,3),(1,2); and (2,3),(1,2).
- **P5:** each printed machine fails as printed. The only working last bar is (1,2) for the top machine, (2,3) for the middle and (2,3) for the bottom.
- **P6:** the minimum is 5 bars.

## Grades 2–3: checks out completely

- **P1:** (1,2),(2,3) sorts 123, 132, 213 and 312. (2,3),(1,2) sorts 123, 132, 213 and 231; 312 and 321 finish 132. (1,3),(1,2),(2,3) sorts all six starts.
- **P2:** the minimum is 3 bars, and every two-bar list fails.
- **P3:** the top and middle machines are each repaired only by (2,3). The bottom machine, (1,2),(3,4),(1,4),(2,3), cannot be repaired by one bar: 2413 finishes 2143, which no single bar fixes. Two bars, such as (1,2),(3,4), would repair it.
- **P4:** the machine is (1,2),(1,3),(2,3),(2,4). All six arrangements of 0011 sort. It does not sort every 0–1 start: 0010, 0100 and 1000 finish 0010, and 1110 finishes 1011.
- **P5:** S4 or N4 sorts all 16 starts.
- **P6:** the neighbour-only minimum is 6. The reverse order 4321 has six reversed pairs.

## Grades 4–5: checks out completely

- **P1:** (1,2),(2,3) fails on 231 and 321. It sorts every arrangement of 1, 1, 3, but 331 finishes 313. (1,3),(1,2),(2,3) sorts every start of 1, 2, 3, of 1, 1, 3 and of 1, 3, 3.
- **P2:** the minimum is 5 bars.
- **P3:**
  - The example is correct: 3, 7, 4 at t = 4 gives 0, 1, 0.
  - Over all real t, the rows are:
    - −2, 8, 5, 8: 1111, 0111, 0101, 0000 (4 rows).
    - 6, 2, 9, 4: 1111, 1011, 1010, 0010, 0000 (5 rows).
    - 4, 4, 4, 4: 1111, 0000 (2 rows).
  - The −2 start's row 1111 needs t < −2. A child who tries only t = 0, 1, 2, … finds 3 rows. The page says "Choose a number t" and the guide expects negative t, so this is consistent.
  - Thresholding commutes with a single bar. I checked every pair of values and every t over small ranges, ties included.
- **P4:** this cannot happen. A threshold t with 4 ≤ t < 9 turns that output into an unsorted 0–1 output. Among the 912 four-lane 0–1 sorters with at most 6 bars, none ever outputs 9 directly above 4. Sorting all 0–1 starts guarantees sorting all inputs.
- **P5:** the upper machine is S4 and sorts all 256 inputs over 1..4. The lower machine is (1,2),(3,4),(1,3),(2,3),(2,4). Its only 0–1 failures are 0100 and 1000, both finishing 0010. It also fails on 12 of the 24 distinct orders, all of which finish 1243.
- **P6:**
  - The example is correct: 3,1 → S → 1,3 → N, record SN.
  - (1,2),(2,3) gives NN: 123; NS: 132, 231; SN: 213; SS: 312, 321.
  - (1,2),(2,3),(1,2) gives a different record for each start: NNN 123, NSN 132, SNN 213, NSS 231, SSN 312, SSS 321.
  - The answer to the closing question is no: two distinct starts never both sort with the same record.
- **P7:** the minima are 3 and 5, and the lower bounds 6 > 2² and 24 > 2⁴ hold.

## Adult guide

The overview's facts are true as stated, with the right hypotheses. These are the zero–one principle, the minima 3, 5 and 6 (6 for neighbouring lanes), the 2ᵐ-versus-n! record bound and the inversion bound. Every other solution, table, trace, hint and extension matches the computations above. The tables are the K–1 P1 table, the K–1 P4 table, the nine-row two-bar table, the 16-row S4 audit, the threshold ranges and the record table. The traces are N4 on 4321 and the lower 4–5 P5 machine on 1000. The proofs are those of S3, Q, S4 and N4. The extensions are depth 3 being optimal on 4 lanes, with no sorter of two stages, and the neighbour-only optimum n(n−1)/2, which I confirmed for n = 5 by exhaustive search. The one exception is below.

### 1. Grades 2–3 Problem 4: wrong final row for 1110 (guide printed p. 7; low)

- **Quoted text:** "Exactly these fail: 0010,0100,1000 finish 0010; 1110 finishes 1101."
- **Evidence:** the printed machine W is (1,2),(1,3),(2,3),(2,4), read from the PDF. Start 1110 is unchanged by the first three bars, because each compares two 1s. The last bar compares lane 2 (1) with lane 4 (0) and swaps them: 1110 → 1110 → 1110 → 1110 → **1011**. The guide's 1101 cannot occur, because lane 3 holds a 1 throughout. The list of failing starts and the class table below it ("Only 1110 fails") are correct. An adult checking a child's correct trace against the key would see a mismatch.
- **Smallest fix:** change "1110 finishes 1101" to "1110 finishes 1011".

### Not checked

- The bonus companion `week-23-bonus.pdf` and its guide.
- The cited COMP308 lecture and the *Math Circle by the Bay* preface. Neither is available locally.
