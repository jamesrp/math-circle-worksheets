# Week 62 (conflict networks): math check

Scope: `lowell-math-circle-year-2/week-62/week-62-students.pdf` (W62-S-v1, 9 pp., Problems 1–9) and `week-62-facilitator.pdf` (W62-FAC-v1, 10 pp.). The student PDF is one combined packet. Pp. 1–3 (Problems 1–3) are headed Grades 2–5 and pp. 4–9 (Problems 4–9) Grades 4–5. I also read the editable source in `lowell-math-circle-year-2/source/week-62/`. I opened no use logs or session records. Checked October 5, 2026. My scripts and outputs are in [checks/week-62/](checks/week-62/).

**Result: no wrong answers, diagrams or theorems anywhere in the packet. I found 3 minor problems, none of which changes an answer. Two are readings of student wording (p. 1 rules, p. 9 worked example), and one is a missing hypothesis in the guide overview.**

## How it was checked

- `extract.py` reads the delivered student PDF itself, not the source. It takes the vector circles, line segments and letters, and rebuilds all 18 task networks and the four worked figures (output `extracted.json` and `out_extract.txt`). The 18 networks match the guide's count.
- `compare_source.py` confirms that `source/week-62/student/graphs.json` gives the same vertices, edges and relative positions as the PDF, within 0.01 pt, for all 18 networks (`out_compare_source.txt`).
- `check.py` uses my own brute-force code and the standard library only (`out_check.txt`). For every network it computes:
  - the chromatic number by exhausting colourings, and the clique number;
  - every simple cycle and which cycles are odd;
  - first-fit over every vertex order (all 24 for the paths, all 40,320 for the p. 8 tree);
  - every minimum set of added edges on p. 6, searching all subsets of missing pairs up to size 3;
  - named-slot counts for k = 0–5.

  It then checks every schedule, certificate, order, table row and count in the guide (transcribed by hand). It also checks the guide's general claims exhaustively on small graphs:
  - two slots iff no odd cycle, on all 33,867 labelled graphs with 1–6 vertices;
  - ω ≤ χ ≤ first-fit ≤ Δ+1, with first-fit always legal, for all graphs and all orders on n ≤ 5;
  - deletion–contraction, on n ≤ 5;
  - tree plus one edge stays two-slot iff the tree distance is odd, and trees have exactly two named 2-colourings, for all labelled trees with n ≤ 6.
- Geometry, from the PDF coordinates:
  - All 104 network sites are round 20.0 × 20.0 mm circles.
  - Every conflict line runs centre to centre between two distinct labelled sites.
  - The closest any printed line, or any possible p. 6 added line, comes to a third site's centre is 13.0 mm. That leaves 3.0 mm to the circle's edge (p. 6 AC passing B, DF passing E).
  - The smallest gap between circles is 5.0 mm. Crossings occur only on p. 2 and never at a site.

## Grades 2–5 (pp. 1–3, Problems 1–3): checks out completely

- **P1:** path ABCD needs 2 slots. The star with centre A and leaves B–F also needs 2, although A has degree 5.
- **P2:**
  - The diamond (AB, AC, BC, AD, BD) needs 3. Both ABC and ABD are triangles; C and D can share a slot.
  - The complete graph on ABCD needs 4.
  - The graph joining each of A, B to each of C, D, E needs 2 with its six lines. Its three crossings add no sites, as the rules say.
- **P3:**
  - Five-cycle ABCDE with leaf AF: needs 3, largest every-pair group 2.
  - Six-cycle ABCDEF with leaves AG, DH: needs 2, largest group 2.
  - So the answer to "Does that group's size always give the fewest slots?" is no, and the page supports it. Removing the leaves changes neither answer.
- **Worked figure (p. 1):** only X–Y conflict. The finished schedule X1, Y2, Z1 is legal and uses 2 slots, and the cards drawn in the slots match the circle marks.

## Grades 4–5 (pp. 4–9, Problems 4–9): checks out completely

- **P4:**
  - Upper network: six-cycle ABCDEF with chord AD, leaf BG and isolated H. It is two-slot, with classes {A,C,E,G} and {B,D,F}; H can go in either. Its only cycles have lengths 4, 4 and 6.
  - Lower network: seven-cycle ABCDEFG with chord AD and leaf GH. It needs 3. Its cycles are ABCD (4), ADEFG (5) and the outer 7. The worked figure (square W–X–Y–Z, thick lines matching "W–X–Y" and "W–X–Y–Z–W") is an even cycle, so it does not give away the odd-cycle rule.
- **P5:**
  - Square ABCD, separate EF and isolated G: two-slot.
  - Five-cycle ABCDE, branch C–F–G and isolated H: needs 3. Its only cycle is the 5-cycle.
- **P6:**
  - Upper tree (AB, BC, AD, BE, CF): exactly one added line is needed. Exactly 6 of the 10 missing pairs work (AC, AE, CE, BD, BF, DF). AF, CD, DE and EF keep two slots.
  - Empty six-site network: exactly three lines are needed. The minimum solutions are exactly the 20 triangles.
- **P7:** on path ABCD, first-fit uses 2 slots in 18 orders and 3 in 6 orders (ABDC, ADBC, ADCB, DABC, DACB, DCAB), never more. After a 3-slot order, moving cards gets back to 2. The worked figure's order X, Y, W on X–W–Y gives X1, Y1, W2.
- **P8:** on the tree (HA, HB, BC, HD, DE, DF, FG), first-fit over all 40,320 orders gives 2 slots in 12,810, 3 in 26,880 and 4 in 630. It never uses 5, since the maximum degree is 3, at H and D. The minimum is 2. The kit's four headers are enough for every order on pp. 7–8.
- **P9:**
  - Path: 24 with slots 1–3 and 108 with slots 1–4, which is k(k−1)³.
  - Diamond: 6 and 48, which is k(k−1)(k−2)².
  - With "Slots may be empty" printed, the reading where every slot must be used is excluded.

## Adult guide

Every stated answer is correct. I checked:
- the schedule tables for P1–P5;
- the P3 alternation argument;
- the P4 certificates (A–D–E–F–G–A, or the outer 7-cycle) and the cycle counts in the follow-up;
- the P5 BFS layers {A},{B,D},{C} and {E},{F};
- the P6 one-edge table with its six odd-cycle certificates, the completeness argument and the 20-triple list;
- the P7 witnesses A,B,C,D → A1 B2 C1 D2 and A,D,B,C → A1 D1 B2 C3, and the repair D 1→2 then C 3→1, which is legal at each step;
- the P8 four-slot table (A,C,B,H,E,G,F,D, ending D4) and the two-slot witness H,A,B,D,C,E,F,G;
- the P9 derivations, the two-slot counts (2 and 0), and the remark that 108/4! is not an integer.

The overview's theorems hold with the stated hypotheses (finite simple graphs, "fits in two" meaning at most two): ω ≤ χ with the C5-plus-leaf gap, two slots iff no odd cycle, and first-fit is legal and at most Δ+1. The p. 6 sufficiency proof is correct: the endpoint distances differ by at most 1, and equal depths give a (2t+1)-cycle through the last common ancestor. The extensions are true and are confirmed by the exhaustive checks above:
- rooted increasing-distance orders use 2 slots on trees (on the p. 8 tree, for every root and every order within the layers);
- odd versus even tree distance for one added edge;
- one edge between two components keeps two slots;
- exactly two named 2-colourings of a connected two-colourable component;
- deletion–contraction with duplicate edges suppressed.

The preparation arithmetic is also correct (kit totals 56/28/224/14/7; 26 student and 30 guide sheets). The one guide problem is item 3 below.

## Located problems (3, all minor; no incorrect answers)

### 1. Student p. 1, shared rules: "Put every card in one slot" has a second reading
- **Quoted text:** "A line means its two cards cannot share a slot. Put every card in one slot. A slot can hold any number of cards if none of them conflict."
- **Evidence:** "Put every card in one slot" can be read as "put all the cards into a single slot". The next sentence, "A slot can hold any number of cards", reads as support for that reading. Taken that way, the rule cannot be carried out on 17 of the 18 networks (every one except the empty p. 6 board), and it conflicts with Problem 1's "fewest slots". The worked figure directly below shows two slots, so the risk is small, but this is the activity's core rule.
- **Smallest fix:** "Put each card in exactly one slot."

### 2. Student p. 9, worked example: its "two" depends on a slot range the figure does not state
- **Quoted figure:** "conflict X–Y → place X in slot 1: X 1, Y _ → two different schedules: X 1, Y 2 / X 1, Y 3". Problem 9 then asks about "only slots 1, 2 and 3" and about "slots 1, 2, 3 and 4".
- **Evidence:** with X fixed in slot 1, Y has 2 completions when slots 1–3 are available and 3 when slots 1–4 are (`check.py`, edge-case section). The figure does not say which range it uses, and Problem 9 asks about both. A child who takes "the neighbour has two choices" from the figure into the four-slot question gets 4·2·2·2 = 32 for the path instead of 108. The guide's note says "The printed two-card example fixes X in 1 and displays two completions; it is not a total count." It does not give the range either. Nothing printed is false.
- **Smallest fix:** caption the middle step "place X in slot 1 (slots 1, 2, 3)". In the guide sentence, add "with slots 1–3 available".

### 3. Guide p. 1, overview: "Swapping slot numbers gives a different assignment" needs a hypothesis
- **Quoted text:** "Counting uses named slots. Student p. 9 counts assignments to fixed vertices and fixed slot names, allowing empty slots. Swapping slot numbers gives a different assignment."
- **Evidence:** this page allows empty slots, and swapping two unused numbers leaves an assignment unchanged. On the p. 9 path with slots 1–4, A1 B2 C1 D2 and A2 B1 C2 D1 are both fixed by swapping 3 and 4 (`check.py`). The guide's own p. 9 says exactly this: "permutations can fix an assignment by swapping two unused names". The overview contradicts its own p. 9, and no count is affected. The student sentence "switching slot numbers counts as a different schedule" has the same literal gap, but it cannot cause a miscount, because swapping two empty slots leaves the written schedule unchanged.
- **Smallest fix:** "Assignments that differ only by renaming slots are counted separately (swapping a used slot number with another changes the assignment)."

## Not checked

- The page references for M1–M4 (MIT 6.042 §12.6, Frieze D18 Thm 1, MIT 18.310 Lecture 14, Pak 18.315 Lecture 9). Only the manifest is in this checkout, not the reference PDFs. The mathematical statements they are cited for are standard, and I verified them independently above.
- Physical fit and handling: counters on 20 mm sites, and pencil lines drawn freehand through the 3.0 mm clearance on p. 6. The guide already marks these untested.
- The packet's own `verify.py`, `verify_pdf.py` and `qa.py`, which I did not run, by design.
