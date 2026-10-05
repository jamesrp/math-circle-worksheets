# Week 33 (prime-length necklaces): math check

Scope: `lowell-math-circle-year-2/week-33/week-33-k-1.pdf` (6 pp., Problems 1–6), `week-33-grades-2-3.pdf` (5 pp., Problems 1–6), `week-33-grades-4-5.pdf` (5 pp., Problems 1–6) and `week-33-facilitator.pdf` (5 pp.). I also checked the bonus companion in the same folder: `week-33-bonus.pdf` (5 pp., Problems 1–7) and `week-33-bonus-facilitator.pdf` (5 pp.). I ignored archive folders. My scripts and outputs are in [checks/week-33/](checks/week-33/). Checked October 5, 2026.

**Result: no stated answer is wrong in any band, the guide or the bonus. I found 4 minor problems. In all three bands, P1 prints recording space that fits the mixed-only reading (2 rings), not the intended 4. The base guide's alternative argument for 2–3 P3 leaves out one case. The bonus guide has a P7 answer sentence that is false if read literally, and a launch description that relies on a bead order the page does not show.**

## How it was checked

- The delivered PDFs are byte-identical (MD5) to `source/week-33/editable/reference-pdfs/` and `source/week-33-bonus/reference-pdfs/`.
- `pdf_extract.py` uses PyMuPDF to read every ring, bead, fill, letter, start arrow, direction arc and card straight from the delivered PDFs, and writes `pdf_geometry.json`. Results are in `pdf_extract.out` (223 checks, 0 failures):
  - Every circle has a square bounding box, so x and y are scaled equally.
  - The beads of all 41 base rings and 23 bonus rings sit on their guide circles at equal angular steps (120°, 90°, 72°, 60° and 45°), with the first bead at 12 o'clock.
  - Every start arrow points at a bead, every direction arc runs clockwise, and no beads overlap.
  - In the launch example, all three pictures show the same fixed ring, AAB. With the start at beads 0, 1 and 2, the clockwise readouts are AAB, ABA and BAA, matching the printed labels.
  - On the 8-card and 32-card pages, card k shows the k-th word in A-before-B binary order. Every word appears exactly once. Letters agree with fills (A white, B grey), "start" sits over the first bead, and the arrow points left to right.
  - I read the six bonus P1 rings clockwise from the top. In the bonus, the working spots measure 24.0 mm and the eight-ring spot centres are 25.3 mm apart, as the guide states. The window example is the ring ABAAB with the start at its last B, so its first window is BAB.
- `check_base.py` enumerates every base task by brute force: rings, rotation families, readout counts, the card families (taken from the extracted card numbers) and periods. It parses the guide's tables and lists from the PDF and compares each one. It also tests the overview's theory:
  - least period = number of readouts and divides n (all binary words n ≤ 12, ternary n ≤ 8);
  - early repeats occur exactly at composite n;
  - c + (c^p − c)/p equals the brute-force ring count for c ≤ 4 and p ≤ 7;
  - p divides c^p − c;
  - the formula fails at composite n;
  - 341 is a counterexample to the converse;
  - the reflection extension holds, and 6 is the smallest binary length with a mirror pair.
  
  Result: 67 checks, 0 failures (`check_base.out`).
- `check_bonus.py` checks every bonus task and guide claim (43 checks, 0 failures, `check_bonus.out`):
  - the P1 rotation classes and rotation-and-flip classes, the guide's 0/1 words, gap sequences, the general three-mark gap criterion (n ≤ 12), the "≤ 2 marked spots" reflection claim, and that no binary ring of length ≤ 5 has a mirror twin;
  - P2 at n = 4, 5, 6 and parity for n ≤ 12;
  - P3: all 30 fixed words, 6 classes, 2,2,1 multiplicities, 3 classes under flips, and the formula (c−1)^n + (−1)^n(c−1) together with the S/D recurrence against brute force;
  - P4–P7: every ring of length ≤ 2^k checked for k = 2, 3.

## K–1: no errors; one recording-space problem (Problem 1 below)

- **P1:** four rings: AAA, AAB, ABB, BBB. See Problem 1.
- **P2:** groups {1}, {2,3,5}, {4,6,7}, {8}. The sizes 1,3,3,1 are not all equal, so the answer is "no".
- **P3:** exactly two rings, AABB and ABAB. The page prints four boards; the spare boards are harmless.
- **P4:** 1, 2 and 4 readouts are possible (AAAA, ABAB, AAAB); 3 is impossible.
- **P5:** exactly two rings, AABBB and ABABB, with five readouts each. The page prints four boards.
- **P6:** two, three and six readouts all occur (ABABAB; AABAAB or ABBABB; e.g. AAAAAB). No other count is possible with both colours.

## Grades 2–3: no errors; same P1 issue

- **P1–P2:** same as K–1. 4 groups of sizes 1,3,3,1.
- **P3:** 1, 2 and 4 are possible; 3 is impossible.
- **P4:** 8 rings: two singletons and six families of five. The card numbers match the guide's table exactly.
- **P5:** impossible. All 30 mixed five-bead words have five readouts.
- **P6:** 32/5 is not a whole number; 2 + 30/5 = 8.

## Grades 4–5: no errors; same P1 issue

- **P1–P2:** as above. 8/3 is not a whole number; 2 + 6/3 = 4.
- **P3:** six length-4 rings, with 1, 2 or 4 readouts each. The early repeat comes from the block AB repeated twice.
- **P4:** as 2–3 P4.
- **P5:** exactly p readouts for every mixed prime-length ring.
- **P6:** 51 rings. The general count is c + (c^p − c)/p, and p divides c^p − c.

## Adult guide (base)

The overview is true with its stated hypotheses: period divides length, the prime case, the counting proof of p | c^p − c, and the limits, including the composite failure and that this is not a converse primality test. The 4–5 P5 proof is correct, and so is the page-4 proof that the least period divides n and equals the number of readouts. Every table, readout list, card number, example and count matches my enumeration: the 3-bead and 32-card tables, the AABBB/ABABB lists, the 0,2,4,1,3 step sequence, the six length-4 rings, and 243/240/48/51. So does the reflection extension (AABABB vs AABBAB). The page references (page 3, page 4) are correct.

## Bonus companion and its guide

Every student answer is as the guide states:

- **P1:** turns only gives {a,c}, {b}, {d,f}, {e}; turns and flips gives {a,b,c}, {d,e,f}.
- **P2:** 4 and 6 work (ABAB, ABABAB); 5 is impossible.
- **P3:** exactly the six listed rings: ABABC, ABACB, ABCAC, ABCBC, ACACB, ACBCB.
- **P4:** AABB is unique.
- **P5:** n windows for n beads.
- **P6–P7:** exactly the two classes AAABABBB and AAABBBAB, which are mirror twins. 16 of the 256 eight-words qualify.

The overview, the gap arguments, the "≤ 2 marked spots" lemma, the 2,2,1 argument, the chromatic formula and recurrence, the forced-completion argument and the 2^k bound all check out. Problems 3–4 below are wording problems only.

## Problems found

### 1. All bands, Problem 1 (p. 1): two boards for a four-ring answer, and "using A and B" reads as "both"

- **Quoted text:**
  - K–1 and 2–3: "Problem 1: Make every different three-bead ring using A and B." (2–3 adds "Find all its readouts as you move the start.")
  - 4–5: "Problem 1: Find every three-bead ring using A and B. How many different readouts does each ring have?"
  - Diagram: two large blank three-bead boards and two ruled lines.
- **Evidence:** There are exactly 4 three-bead rings: AAA, AAB, ABB and BBB (`check_base.out`). The guide's key expects four ("There are four rings, with family sizes 1,3,3,1"). Only 2 of them use both letters, and the page prints exactly 2 boards in every band (`pdf_extract.out`, page 1). Elsewhere the packet says "both A and B" (K–1 P6, 2–3 P5) or "at least two colors" (4–5 P5) when it means mixed rings. So "using A and B" with two boards invites the 2-ring reading, despite the shared rule "one-color rings are allowed". This matters most in K–1, where an adult reads the problem aloud. Later "find every" pages print four boards for two answers (K–1 P3, P5), so P1 is the one page whose space undercounts.
- **Smallest fix:** Replace the two large boards and two ruled lines with four smaller three-bead boards (2 × 2, radius about 2.3 cm), so the space does not match the mixed-only count. Alternatively, keep the layout and write "…using A and B. One-color rings count."

### 2. Guide p. 3, Grades 2–3 P3: the "physical alternative" handles only one way a repeat can happen

- **Quoted text:** "A physical alternative: a match after three steps forces the same color all around the four-position cycle, so it was a one-readout ring already."
- **Evidence:** On a mixed four-bead ring, two starts can match only 2 steps apart (ABAB). A match 1 or 3 steps apart forces a single colour (`check_base.out`, coincidence table: {2: ['ABAB']}). To rule out exactly three readouts, the argument must also exclude a 2-step match: that gives positions 1 = 3 and 2 = 4, so at most two readouts. As written, the sentence assumes without reason that the first repeat comes after three steps. The page-4 period proof is complete; only this alternative is not.
- **Smallest fix:** "A physical alternative: any repeat is a match after 1, 2 or 3 steps. After 1 or 3 steps, following the match around reaches all four positions, so the ring is one colour (one readout). After 2 steps, opposite beads agree, so there are at most two readouts. Three never happens."

### 3. Bonus guide p. 4, P7: "Their flipped copies are rotations of each other" is false if read literally

- **Quoted text:** "P7: exactly two shortest rotation classes: AAABABBB and AAABBBAB. Their flipped copies are rotations of each other; allowing flips gives one class."
- **Evidence:** flip(AAABABBB) = BBBABAAA is a turn of AAABBBAB, and flip(AAABBBAB) = BABBBAAA is a turn of AAABABBB. So the two flipped copies are *not* rotations of each other: they are the two different classes again. The intended fact is that each ring's flip is a turn of the *other* ring, which answers the student question "How are their flipped copies related to your collection?" (`check_bonus.out`).
- **Smallest fix:** "Flipping either ring gives a turn of the other, so the collection is closed under flips; allowing flips gives one class."

### 4. Bonus guide p. 1, Launch: "the last B … across the closing gap" relies on a bead order the page does not show

- **Quoted text:** "enact the printed five-bead non-task example: starting at the last B, read clockwise B-A-B across the closing gap and match BAB."
- **Evidence:** The source draws the ring A,B,A,A,B from the top bead, so its "last" bead is the upper-left B. The printed picture, however, marks that B with the only "start" arrow (`pdf_extract.out`: ring ABAAB, start at index 4). For anyone looking at the page, B-A-B is therefore the *first* window from the marked start and crosses no gap. The windows that do wrap past the start are A-A-B and A-B-A, which start at the two lower beads. The demonstration as described never shows the wraparound that the page's opening rule stresses ("including windows that cross the closing gap"). The guide's own hint treats the viewer/start as what makes the closing gap visible.
- **Smallest fix:** "starting at the marked B, read clockwise B-A-B and match BAB; then move the viewer to the lower-left A and read A-B-A, which crosses the closing gap back past the start." (Or move the printed start arrow to the top A, so that the drawn B-A-B is the window that crosses the gap.)

## Notes (not errors)

- The base launch example is itself a task instance. AAB with readouts AAB, ABA and BAA is one of the four P1 rings and the card family {2,3,5} in P2. This is a design point for the card review, not a mathematical error.
- Bonus P4 and P6 print mats with exactly 4 and 8 spots, which shows the shortest length. P7 prints exactly two recording rings, which shows the class count. The guide acknowledges that the mat is construction capacity and that P5 carries the proof, so no answer is affected.
- The bonus materials list "at least eight counters each of kinds A/B". That exactly covers P7's two rings side by side (8 A, 8 B), but two P1 rings side by side need 10 B. The guide's P1 method (one counter ring plus a tracing copy) needs only one ring, so this is not an error.
