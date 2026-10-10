# Week 41 (torus portals and lifts): math check

Scope:
- `lowell-math-circle-year-2/week-41/week-41-k-1.pdf` (F41-K-v2, 4 pp., Problems 1–4), `week-41-grades-2-3.pdf` (F41-23-v2, 5 pp., Problems 1–5), `week-41-grades-4-5.pdf` (F41-45-v2, 5 pp., Problems 1–6) and `week-41-facilitator.pdf` (7 pp., including the p. 7 route update).
- The bonus companion in the same folder: `week-41-bonus.pdf` (W41-BONUS-v1, 3 pp., Problems 1–3) and `week-41-bonus-facilitator.pdf` (3 pp.).
- I ignored the archive folders.

Sources read: the generator `source/week-41/editable/src/make_packets.py` and `common.py`, the three generated `.tex` files (the diagram coordinates come from these), `facilitator-src/build.py` (the guide's copy diagram), and the bonus `student/build.py` and `student/materials.py`. The six delivered PDFs are byte-identical (MD5) to `source/week-41/editable/reference-pdfs/` and `source/week-41-bonus/reference-pdfs/`. I did not run or import `src/check_math.py`, `verify_math.py`, `facilitator-src/verify_answers.py` or the bonus `student/verify.py`. I rendered every page at 100 dpi and read each one. Checked October 10, 2026.

**Result: every answer, count and claim in the three bands, the base guide, the bonus and the bonus guide is correct, and every base diagram matches its text. I found 1 problem: the bonus portal boards (pp. 1–2) mark only the left/right seams, though the rule and the tasks need top/bottom wrapping too. There is also one note outside the mathematics: the bonus guide gives a wrong path for the copy-sheet script.**

## How it was checked

The model is the 3 × 3 torus. A lifted position is a point of Z² with the original H at (0,0). Its cell is read off mod 3 from the board A B C / D H E / F G I, and its copy is (⌊(x+1)/3⌋, ⌊(y+1)/3⌋).

- **`check_math.py`** (output `out_check_math.txt`, 140 checks, 0 failures):
  - It reads every printed move word from the `.tex` sources and checks it against the page.
  - It replays every printed trip and every guide replay, and enumerates all two-step words, all closed words of length 2–6, the two-pawn state space and the 6-step return displacements (also checked by the spectral count (4⁶ + 4·1 + 4·(−2)⁶)/9 = 484).
  - For the Grades 4–5 moves it implements the page-4 rules (adjacent inverse pair inserted or erased; adjacent perpendicular pair replaced by the other two sides of its unit square). It checks that every move keeps the lifted endpoint (all words up to length 7). It also checks that the moves connect all closed words of length ≤ 8 with the same finishing copy (9,789 words, 13 classes). It confirms each step of the guide's P4 reduction and P5 nine-slide sequence geometrically.
  - Bonus: it computes round-end orbits, tests the guide's lcm period formula on every a-by-b board with a, b ≤ 7, and enumerates all nine-step tours. It runs a BFS on the periodic plane with B and E closed. It also counts which words and tours need a top/bottom crossing.
  - It finds guide sentences in the `pdftotext` output before checking them.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`, 112 checks, 2 failures, which are Problem 1 below):
  - It reads every board in the three base PDFs with pdfplumber. Every board is square (48, 45, 75, 180, 72, 60 and 25 mm) and carries A B C / D H E / F G I, or H alone in the centre cell of a copy.
  - From the TeX it checks every portal board's marks: circles at the same height on the left and right edges; diamonds at the same x on the top and bottom edges; side arrows at the same place, both pointing up; top/bottom arrows at the same place, both pointing right. That is a translation gluing with no reversal, as the guide says.
  - It checks the bold original frame and the nine (m,n) labels (right = +m, up = +n), the page-1 example arrows (H through E to the right edge, then the left edge to D; the original H to D in the next copy) and the slide example (F→G→H against F→D→H on the D H / F G block).
  - For the bonus it checks the board letters, the example strips, the 81-cell repeated map, the 7 × 7 obstacle patch (shading exactly on B and E), the three circled targets and the "original" label.

## K-1 (pp. 1–4): checks out

- **Worked example (all bands):** RR from H goes H → E → D. On the copies, D is in the next copy to the right.
- **P1 (all bands):** RRD, UU, LD and UURR end at F, G, F and F. Three of the four ending at F is deliberate (guide p. 3).
- **P2:** all nine cells are reachable in exactly two steps. H needs a reversal (RL). D, E, B and G need a seam crossing (RR, LL, DD, UU). Without crossing an edge, only A, C, F, H and I are reachable. Every guide witness is valid.
- **P3:** the numbers of closed words are 4, 4, 36 and 100 for 2, 3, 4 and 5 steps, so "more than one trip" is always possible. The 3-step trips are exactly RRR, LLL, UUU and DDD. All the guide's examples return to H.
- **P4:** no. Only 9 of the 81 pawn-pair states can be reached from (H, E), and in all of them the E-pawn stays one cell right of the H-pawn mod 3. The swap needs +1 ≡ −1 (mod 3), which is false. The guide's argument is valid.

## Grades 2–3 (pp. 1–5): checks out

- **P2:** the 3-step list RRR, LLL, UUU, DDD is complete. There are 484 six-step returns: 400 balanced, 1 each for (±6,0) and (0,±6), and 20 each for (±3,±3). No other displacement occurs. The guide's ten examples are valid.
- **P3:** RRR → (1,0), UUU → (0,1), RRRUUU → (1,1), RRLL → (0,0). All four stay on the printed 3 × 3 array of copies. RRLL enters the right copy before returning.
- **P4:** both trips finish at H in copy (1,1), so the answer is yes and yes.
- **P5:** RRRLLL, UUUDDDRRRLLL and RRRUUULLLDDD all return to the original H. The last one passes through the right, upper-right and upper copies, as the guide says. The shortest trip that visits a copy above and a copy to the right has 8 steps (for example RRLLUUDD).

## Grades 4–5 (pp. 1–5): checks out

- **P2:** RRR, LLL, UUU and DDD finish in (1,0), (−1,0), (0,1) and (0,−1).
- **P3:** RRRUUU and UUURRR finish in (1,1); RRLL and RRRUUULLLDDD finish in (0,0). Every copy label sits in its copy, and each copy's H is at (3m,3n).
- **P4:** RRRUUULLLDDD shrinks and RRR does not. The guide's route (nine slides to RRRLLLUUUDDD, then six cancellations) is 15 legal moves and stays on the page-3 map. RRR finishes in (1,0), and no move changes that.
- **P5:** every step of the guide's nine-slide sequence is one legal slide. Nine is the minimum (BFS over words up to length 8), which equals the 9 R-before-U pairs that have to be undone.
- **P6:** two loops can be changed into each other exactly when they finish in the same copy. This is confirmed both ways up to length 8, as described above.

## Base adult guide: correct throughout

- **Overview (p. 1):**
  - A route returns to H iff both displacements are multiples of 3, and its finishing copy is (x/3, y/3). Checked on all words up to length 8.
  - The based-loop classification by lifted endpoint is correct, with the right hypotheses (basepoint fixed, self-overlap allowed, square faces available).
  - The claim that the printed moves generate exactly equality of lifted endpoints is correct.
  - The remark that without faces the commutator need not vanish is correct: RULD is freely reduced, yet it finishes in (0,0).
- **Materials (p. 2):** the numbers match the sources: 180 mm mat, 60 mm recording copies, 25 mm copies with 8.3 mm cells in 2–3 P4.
- **Copy diagram (p. 2):** it shows H → E → D with D in the right copy.
- **Keys (pp. 3–5):** every key matches my enumeration, including the replay table, the nine witnesses, the 400 + 4 + 4·20 = 484 count, the copy tables and both slide sequences.
- **Proofs (p. 6):** the lifting argument, the linear homotopy and the sorting-and-cancellation argument are sound.
- **Packet references:** the key-alignment line and the p. 7 route note cite problem numbers that exist.
- **Not verified:** the Hatcher section and example numbers; the book is not in this checkout. Example 1.1 in §1.1 is, to my knowledge, the linear-homotopy example, and the facts it is cited for are standard.

## Bonus companion and its guide: correct, apart from Problem 1 below

- **P1:**
  - The round ends are R: H, E, D; RU: H, C, F; RRR and RULD: H only; RRU: H, A, I.
  - No word reaches more than 3 round-end cells (checked up to length 7), so none reaches all nine.
  - The guide's period formula lcm(a/gcd(a,x), b/gcd(b,y)) is right for every board up to 7 × 7.
- **P2:**
  - There are exactly 96 rooted oriented tours (2 × 48 Hamiltonian cycles of K₃□K₃).
  - They finish in exactly the guide's 12 copies, with counts 18 for (±1,0) and (0,±1) and 3 for each (±2,±1) and (±1,±2). All 12 witnesses are tours ending where the table says.
  - The parity argument against (0,0) is valid.
  - The extension holds: under the board's 8 symmetries about H, two examples generate all 12 copies.
  - Only the 72 tours ending in (±1,0) or (0,±1) fit on the printed 3 × 3 compact map. The guide supplies extension copies for the others.
- **P3:**
  - The shortest routes have 5, 5 and 8 steps. There are 2, 2 and 4 of them, all inside the printed patch.
  - DRRRU, LUURU and LUURRRRU are legal.
  - The lower-bound arguments (RRR blocked, parity, a six-step diagonal route must be R/U only and both first steps are blocked) are correct.
- **Materials arithmetic:** 27.5, 22.6 and 8.5 mm cells; 5 kits × 9 markers = 45; 15 sheets × 4 boards = 60 = 5 × 12 copies. A nine-step route touches at most 10 positions, so 12 copies suffice.

## Problems found

### 1. Bonus pp. 1–2, Problems 1 and 2 (minor): the portal boards mark only the left/right seams, so they draw a cylinder although the rule makes a torus

- **Quoted text:** p. 1 rules: "On the 3-by-3 board, cross an edge to the opposite edge in the same row or column." Diagram: both portal boards (p. 1, P1; p. 2, P2) have a right-pointing arrow beside each row on both sides (six arrowheads) and nothing above or below any column (`out_check_diagrams.txt`, bonus p. 1 and p. 2). The base packet marks all four edges (circles and up-arrows on the sides, diamonds and right-arrows on top and bottom).
- **Evidence** (`out_check_math.txt`, "Bonus pages 1-2"):
  - In P1, the printed words RU and RRU cross the top edge in their second round: C → A, then U from A to F; and A → B → C, then U from C to I. A child working from the picture stops at A or C. The guide's "RU visits H,C,F" and "RRU visits H,A,I" need the unmarked wrap.
  - In P2, 84 of the 96 tours cross the top or bottom edge. If the board is read as the cylinder it draws, only 12 tours remain, and they finish in just two copies, (1,0) and (−1,0). That leaves "Find tours with different finishing copies" with almost nothing to find, against the guide's 12.
  - The rule sentence does state the column wrap, so an adult reading it can correct the picture. That is why I rate this minor.
- **Smallest fix:** in `student/build.py` `portal()`, add a matching up-pointing arrow above and below each column, for example `arrow(x+t*cell, y-18, x+t*cell, y-4)` and `arrow(x+t*cell, y+3*cell+4, x+t*cell, y+3*cell+18)` for t in 0.5, 1.5, 2.5. Both pages have at least 30 pt free above and below the board.

## Note outside the mathematics (bonus guide p. 1, minor)

"For a physical repeated map, run `python3 src/materials.py --out /path/to/scratch`". The bonus source has no `src/` folder; the script is `source/week-41-bonus/student/materials.py`. An adult following the guide would get "No such file". Smallest fix: print `python3 student/materials.py --out /path/to/scratch` (run from `source/week-41-bonus/`).
