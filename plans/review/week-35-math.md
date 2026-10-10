# Week 35 (Footprint borders): math check

Scope:
- Student packets in `lowell-math-circle-year-2/week-35/`:
  - `week-35-k-1.pdf` (footer W35-k-1-v2, 5 pp., Problems 1–7)
  - `week-35-grades-2-3.pdf` (W35-grades-2-3-v2, 4 pp., Problems 1–6)
  - `week-35-grades-4-5.pdf` (W35-grades-4-5-v2, 4 pp., Problems 1–6)
  - the bonus companion `week-35-bonus.pdf` (W35-BONUS-v1, 3 pp., Problems 1–3)
- Adult guides: `week-35-facilitator.pdf` (7 pp., including the p. 7 route update) and `week-35-bonus-facilitator.pdf` (W35-BONUS-FAC-v1, 2 pp.).
- Sources read: `source/week-35/editable/src/*.tex`, `facilitator-src/guide.md` and `route-note.json`, and `source/week-35-bonus/student/*.py` and `guide.md`. All six delivered PDFs are byte-identical to the reference copies in the sources.

Archive folders were not reviewed. The archived K-1 PDF was read only to compare its footer label (item 4). Checked October 10, 2026. My scripts and outputs are in this run folder: `extract.py`, `compare_source.py`, `check.py`, `geometry.py` and `common.py`, with `extracted.json` and the `out_*.txt` files. `render/` holds the 100 dpi page images I inspected. It doesn't need committing.

**Result: no wrong answer, diagram or theorem anywhere in the packet. Grades 2–3 checks out completely. I found 6 minor problems, and none changes a printed answer:**

1. **Grades 4–5 P3:** the page doesn't say which line the flip is over. If the flip is over a perpendicular line, the answer to "Must a 6 cm slide also match?" becomes no.
2. **Guide p. 3, answer bank:** the recipe positions don't say what a motif "anchor" is. They build without overlaps only if the anchor is the footprint's centre.
3. **Guide p. 2, motif size:** Border E needs footprints no wider than 30 mm. The guide sets only a 25 mm minimum, and tracing the printed outline gives 17.7 mm.
4. **K-1 footer:** the current 7-problem packet and the archived 6-problem packet both print W35-k-1-v2. The guide calls the current one v3 and numbers its keys for it.
5. **Bonus p. 2, P2:** each "changes: ______" blank is printed next to the following row's heading.
6. **Bonus guide p. 2, P3:** "alternating every other join" describes the wrong construction if read as "at alternate joins".

## How it was checked

- **`extract.py`** reads the delivered PDFs, not the sources (pdfplumber vector data). It records:
  - every polygon, arrowhead, line (with dash, colour and width), rectangle and word;
  - the page text of both guides.
- **`compare_source.py`** checks that the sources match the print:
  - every box, tick and motif scope in the three `.tex` files is printed at its source place and orientation, within 0.05 pt;
  - the bonus P2 rows and slide labels in `build.py` are the printed ones;
  - all six PDFs equal their source reference copies.
- **`check.py`** with **`geometry.py`** uses my own code: the standard library plus pdfplumber for reading.
  - **The motif.** The notched F is read from the printed launch figure. Its 12-vertex outline has only the identity as a self-isometry (checked over all vertex correspondences). Its edge-length word is 2.6, 0.7, 0.5, 0.25, 1.3, 0.65, 1.1, 0.45, 1.1, 0.65, 0.8, 2.2.
  - **The launch figure.**
    - Panel 2 is exactly the start motif reflected in its own panel line (panels are 6.6 cm apart). The arrow on the top arm becomes an arrow on the bottom arm, still pointing right.
    - Panel 3 is panel 2 moved 1.00 cm right. The "then slide right" arrow is 0.96 cm from the start of its shaft to its tip.
    - The 2–3 and 4–5 figures are the K–1 figure moved 2.5 cm on the page.
  - **The boards.** All 25 working boards are 17.65 × 6.00 cm. Each middle line is centred in its box, and the ticks are 3.0 cm apart. The crossing line on 4–5 p. 3 is perpendicular to the middle line and spans the box.
  - **Exact frieze engine.** It uses the real motif points (outline plus arrow), the four forms A, H A, V A and R A, and rational coordinates. The motif has no symmetry, so a symmetry of a border is fixed by where one motif goes. The engine lists every such candidate and verifies each one by transforming the point sets. This gives the complete symmetry group of each guide recipe: T (4 and 6), G, H, R, E, the K–1 P4 variant G8, and the 2–3 P6 edit.
  - **Physical fit.** Overlaps are tested by point-in-polygon sampling, and I measured how far each recipe reaches from the middle line. This was done for several anchor choices and footprint widths.
  - **Random borders.** 1,500 random borders built from the motif (periods 2–8, half-cm grid, many with built-in glides, flips or half-turns) test the guide's stated theorems:
    - G_a² = T_2a;
    - shortest glide P/2 when the middle flip fails, and every glide then has displacement (k + ½)P;
    - glides are nonzero multiples of P when the flip holds;
    - two perpendicular flips force the half-turn at their crossing.
  - **Bonus.**
    - Every printed footprint's colour matches its R/B letter, and all P1–P2 footprints have one form and orientation.
    - "mirror A" is A reflected. The four necklace rings are regular, with 5, 6, 7 and 8 circles centred on the vertices.
    - Shortest shared slides are found by brute force. Every recolouring of each P2 block is enumerated, including a doubled block whose two copies may be repaired differently. Every A/mirror-A necklace of 5–8 cards is enumerated.
    - The material counts are recomputed.

## K–1 (pp. 1–5, Problems 1–7): correct

All answers are right. Item 4 concerns the footer label.

- **P1:** T at 4 cm matches after 4 cm (and every multiple) and fails after 2 cm.
- **P2:** T4 and T6 have primitive slides of 4 and 6.
- **P3:** G (A at (6k, 1.5), H A at (6k+3, −1.5)) matches after the flip and a 3 cm slide. The bare flip fails: it sends A to (0, −1.5), an empty place. So the answer to "Can you make the flip alone fail?" is yes.
- **P4:** G8 (8k / 8k+4) has the same kind of match (glides 4 + 8k, no flip).
- **P5:** H matches the middle flip. Moving its lower row 3 cm gives G, and the flip fails.
- **P6:** R has half-turns about (1.5 + 3k, 0). T has no half-turn about any point.
- **P7:** open.
- **Launch figure:** placed before P3, the first glide task.

## Grades 2–3 (pp. 1–4, Problems 1–6): checks out completely

- **P1:** two primitive slides, 4 and 6.
- **P2:** G.
- **P3:** On every border with a glide and no middle flip, the shortest glide is half the primitive slide. This is the guide's p. 6 proof, and no counterexample turned up in 401 random borders.
- **P4:** H has the middle flip and no half-turn.
- **P5:** R has half-turns and no middle flip.
- **P6:**
  - H → G breaks the flip.
  - The guide's edit moves A at 12k to 12k + 0.5. Its gaps alternate 5.5 and 6.5, its primitive slide is 12, and the 6 cm slide fails.

## Grades 4–5 (pp. 1–4, Problems 1–6): correct

All answers are right. Item 1 below concerns the wording of P3.

- **P1:** as 2–3 P1.
- **P2:** G has shortest slide 6 and shortest glide 3. Glides are exactly 3 + 6k.
- **P3:** In the intended reading (a glide), the answers are right: a 6 cm slide must match because G_3² = T_6, and a 3 cm slide need not match (G is a counterexample).
- **P4:** E has:
  - flips in y = 0 and in every x = 3k;
  - half-turns about (3k, 0), including the crossing (0, 0);
  - slides 6k, and glides by nonzero 6k.
  The printed crossing lines are perpendicular.
- **P5:** R fails every middle flip and every perpendicular flip.
- **P6:** The guide's complete lists for G and R match the computed groups exactly.

## Bonus packet (pp. 1–3, Problems 1–3): correct

All answers are right. Items 5 and 6 below are layout and guide wording.

- **P1:**
  - RBB and RBBB have periods 3 and 4. The shortest shared slide is 12 (brute force).
  - The 6-slot and 8-slot designs exist with neither row constant: RB/RBB gives 6, and RB/RBBBBBBB gives 8.
  - The possible primitive-period pairs are (2,3), (2,6), (3,6), (6,6) for 6 and (2,8), (4,8), (8,8) for 8.
  - The "repeat" bars span exactly 3 and 4 slots.
- **P2:**
  - RBBBRB, slide 3: minimum 2. The optima are BBBBBB, BRBBRB, RBBRBB and RRBRRB.
  - RBBBBRRB, slide 2: minimum 3. The optima are BBBBBBBB and RBRBRBRB.
  - RRBBRB, slide 2: minimum 2. The only optimum is RBRBRB.
  - Letting a doubled block's two copies differ doesn't lower any minimum.
  - The demonstration's boxed footprint is the one changed slot of RBB → RRB.
- **P3:** Fewest equal joins: 1, 0, 1, 0 for 5–8 cards. Equal joins always have the parity of the card count.

## Adult guide (7 pp.): correct

The overview is right, with the right hypotheses and limits:
- the glide theorem, and the shortest-glide statements with their discrete-period and fixed-axis hypotheses;
- two perpendicular flips give a half-turn, and the angle is doubled for general lines;
- the motif has no symmetry.

Every recipe on p. 3 and every key on pp. 4–5 and 7 matches the computed groups. This includes "the bare flip lands in the gaps", "a 3 cm bare slide lands on the wrong row" and "a 3 cm slide preserves locations" (E). The completeness argument and the p. 6 proof are sound. The cross-references are right: "page 3" is the answer bank, "page 4" the K–1/2–3 keys, "page 5" the completeness argument and "page 6" the proof. Items 2–4 below are about the recipes' physical scale and the K–1 label.

## Bonus guide (2 pp.): correct

All solutions match my enumeration:
- the lcm statement;
- the cycle lower bound and that it is attained;
- all the listed optimal repairs;
- the parity argument;
- three forms make every ring of 3 or more cards possible.

The material counts are right: 14 R + 34 B, 15 R + 33 B, and 288 = 6 × 48. Item 6 below is one wording slip.

## Problems found

### 1. Grades 4–5, p. 2, Problem 3: the flip's line is not stated

- **Text:** "A border matches after a flip and a 3 cm slide along the middle line. Must a 6 cm slide also match? Must a 3 cm slide match? Explain why."
- **Why it is open to another reading:** "along the middle line" attaches to the slide. The problem doesn't use the word "glide", which P2 defines just above it, and P5 on p. 4 uses "flip" for lines perpendicular to the border.
- **Evidence:** take V8: A at (1.5 + 8k, 1.5) and V A at (−1.5 + 8k, 1.5). It has no overlaps.
  - The flip over the perpendicular line x = −1.5 followed by a 3 cm slide right is the flip over x = 0, which matches.
  - V8's slides are multiples of 8, so a 6 cm slide fails.
  - So under this reading, the answer to the first question is "no". The guide's key ("apply the given 3 cm glide twice") assumes the middle line.
- **Smallest fix:** "A border matches after a 3 cm glide." Or: "…after a flip over the middle line and a 3 cm slide along it."

### 2. Guide p. 3, "A precise way to read these examples": the anchor is undefined

- **Text:** "Positions below are motif anchors in centimeters; translate the same anchor consistently. Take h = 1.5 cm and use the original motif at about 26 mm wide."
- **Evidence:** the symmetry statements hold for any anchor, provided each form is taken about it. The physical recipes work only with a central anchor. With a 26 mm motif, checked over ±3 periods:
  - **Centre anchor:** no recipe has overlapping footprints, and all stay within 2.6 cm of the middle line.
  - **Top-left-corner anchor:** H, R and E overlap (7, 7 and 38 overlapping pairs).
  - **Bottom-left-corner anchor:** footprints reach 3.7 cm from the middle line, past a 70 mm strip's 3.5 cm, and E still overlaps (12 pairs).
  - **Arrow-tail anchor:** H and E overlap.
- **Smallest fix:** "Positions are the centres of the footprints (the middle of each footprint's bounding box)."

### 3. Guide p. 2, "Motifs": Border E caps the footprint width, and tracing gives an undersized footprint

- **Text:** "use the exact notched F-like outline printed in the introduction, at least 25 mm long", and later "trace and copy its printed example".
- **Evidence:**
  - Border E puts A and V A centres 3 cm apart, so the footprint must be at most 30 mm wide. At 30 mm there are no overlaps; at 31 mm there are 26 overlapping pairs.
  - The printed outline is 17.7 × 15.0 mm, so a tracing is below the stated 25 mm minimum. All recipes still fit at 17.7 mm, so only the stated minimum conflicts.
- **Smallest fix:** "25–30 mm wide (the printed outline enlarged to about 150%)". Then "trace and copy" becomes "trace and enlarge".

### 4. K–1, all five pages, footer: the version label no longer identifies the packet

- **Text:** "Bellingham Math Circle / Week 35 / W35-k-1-v2" on the current packet, which has Problems 1–7.
- **Evidence:**
  - The archived pre-revision K–1 (`archive-before-fresh-review-2026-10-04/week-35-k-1.pdf`) has Problems 1–6 and carries the same id, W35-k-1-v2.
  - The guide's p. 6 says "K-1 v3, Problems 1-7" and numbers its K–1 keys for the new packet. For example, its "Problem 5: Start with Border H" is the archived packet's Problem 4.
  - An adult with an earlier printout would read every K–1 key one problem off, and the footer gives no way to tell.
- **Smallest fix:** change the K–1 footer to W35-k-1-v3.

### 5. Bonus p. 2, Problem 2: the answer blanks sit with the following row

- **Diagram:** each row's "changes: ______" is printed below that row's grey separator line.
  - Row 1's blank is at 413 pt from the top, while its separator is at 397 pt.
  - That puts each blank level with the next row's heading: the first blank sits beside row 2's "slide 2 slots".
  - The third blank stands alone at the foot of the page.
- **Effect:** a child can easily write row 1's minimum (2) as row 2's answer (3).
- **Smallest fix:** draw each blank above its separator line, at y − 45 instead of y − 78 in `student/build.py`.

### 6. Bonus guide p. 2, P3 solution: "every other join"

- **Text:** "One equal join is attained by alternating every other join."
- **Evidence:** read as "change form at alternate joins", this builds AMMAA for 5 cards (3 equal joins) or AMMAAMM for 7 (3 equal joins). The intended construction alternates at every join except one: AMAMA, with 1 equal join.
- **Smallest fix:** "One equal join is attained by alternating at every join except the last–first one."
