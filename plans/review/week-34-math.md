# Week 34 (Hidden turns): math check

Scope:
- Student packets in `lowell-math-circle-year-2/week-34/`:
  - `week-34-k-1.pdf` (W34-k-1-v2, 5 pp., Problems 1–6)
  - `week-34-grades-2-3.pdf` (W34-grades-2-3-v2, 5 pp., Problems 1–5)
  - `week-34-grades-4-5.pdf` (W34-grades-4-5-v2, 5 pp., Problems 1–5)
  - the encore `week-34-bonus.pdf` (W34-BON-v1, 4 pp., Problems 1–6, Grades 2–5)
- Adult guides: `week-34-facilitator.pdf` (6 pp.) and `week-34-bonus-facilitator.pdf` (W34-BON-FAC-v1, 5 pp.).
- Sources read: `source/week-34/editable/src/*.tex` and `source/week-34-bonus/student-src/bonus.tex`. The six reference PDFs in the sources are byte-identical to the delivered PDFs.

Archive folders were ignored. Checked October 5, 2026. My scripts and outputs are in [checks/week-34/](checks/week-34/) (`extract.py`, `compare_source.py`, `check.py`, `common.py`, with `extracted.json` and the `out_*.txt` files).

**Result: no wrong answer, diagram or theorem anywhere in the packet. Grades 2–3 and Grades 4–5 check out completely. I found 3 minor problems, and none changes a printed answer:**

- **Encore P3–P4:** "change" is undefined, and two other readings give different answers.
- **Encore starting pattern:** it already matches a flip, which the bonus guide does not mention.
- **K-1 P6 (base guide key):** the key neither accepts nor excludes a recoloured second pattern.

## How it was checked

- **`extract.py`** reads the delivered PDFs, not the sources (PyMuPDF vector data). For every one of the 50 printed rings it gives:
  - the outline and the spot circles;
  - the mark in each spot (filled dot, hollow ring, outline square or letter), read clockwise from the top;
  - the motion-card arrows with their arrowheads, and the dashed flip line.
- **`compare_source.py`** checks that the sources match the print:
  - every spot in the three base `.tex` files is printed at the same place and size, within 0.05 mm;
  - the 19 `\ring` calls in `bonus.tex` match the printed rings, including the starting word.
- **`check.py`** uses my own brute-force code and the standard library only. Matching is defined exactly as on the pages: kinds are fixed, the copy moves by one of the 2n maps i→i+k or i→k−i, and the identity does not count.
  - From the coordinates: every printed ring is regular. Its distance-preserving spot permutations are exactly those 2n maps, with the first spot at the top.
  - Fewest kinds for n = 3–12, by exhausting 1, 2 and 3 kinds.
  - Distinguishing two-kind words for n = 3–10, and the least minority count for n = 6–12.
  - Every witness and edit in both guides.
  - Every lemma used in the base guide's p. 5 proofs, for n = 3–20.
  - All dihedral orbits of distinguishing two-kind 8-rings.
  - Flip counts of all two-kind words on 6 and 8 spots (and all three-kind words on 6), and the d | n, 0-or-n/d flip theorem for all two-kind words with n ≤ 10 and all three-kind words with n ≤ 8.
  - Minimum repairs by brute force over all target words, the cycle formula against brute force for every two-kind word and motion with n ≤ 8, and two other readings of "change".
  - All 4096 ordered pairs of six-ring layers, for the intersection rule and for P5 and P6.

## K–1 (pp. 1–5, Problems 1–6): correct

All answers are right. Item 3 below is a recolouring shortcut in P6 that the key does not mention.

- **Launch figure** (same in all three bands): start = dot, ring, dot, ring clockwise from the top. "turn 2 spots: match" is the start turned two spots, which is the start itself. "turn 1 spot: no match" is the start turned one spot (ring, dot, ring, dot), which differs. The figure does not give away a task answer.
- **P1** (3-ring, two kinds): every two-kind 3-ring has a matching flip. Every mixed one has exactly one flip and no matching turn, so a partner always finds a match.
- **P2** (4-ring): 3 kinds is the fewest. ABCC works; every two-kind 4-ring has a flip.
- **P3:** both outcomes exist.
  - From ABCC, 6 of the 12 one-counter changes keep it distinguishing (2 of the 8 that use kinds A–C; the other 4 use a fourth kind D).
  - From each of the 24 three-kind distinguishing 4-rings, both outcomes are available using kinds A–C only.
  - The guide's edits are right: ABAC matches only the flip k=2, which fixes the B and C spots, and ABBC stays distinguishing.
- **P4** (5-ring): two kinds cannot work; three can (ABCCC).
- **P5** (6-ring): possible. There are exactly 12 two-kind distinguishing words, all in one orbit: AABABB.
- **P6** (8-ring): possible. There are 6 different non-matching distinguishing two-kind 8-rings: two with 3 A, two with 4 A and two with 5 A. See item 3.

## Grades 2–3 (pp. 1–5, Problems 1–5): checks out completely

- **P1–P3:** 3 kinds on 3, 4 and 5 spots.
- **P4:** two kinds suffice on 6 spots (AABABB). A full check is 5 turns plus 6 flips.
- **P5:** "How few counters of one kind can it have?" The answer is 3. On every ring with 6–12 spots, a kind used at most twice always leaves a flip. AABABBBB attains 3.

## Grades 4–5 (pp. 1–5, Problems 1–5): checks out completely

- **P1–P3:** 3 kinds on 3, 4 and 5 spots. The shared explanation the page asks for in P3 exists: with two kinds on at most 5 spots, some kind has at most two spots, and any set of at most two spots is kept by a flip (checked for n = 3–20).
- **P4:** AABABB.
- **P5:** "a two-kind pattern … on any ring with at least six spots" exists. A at spots 0, 1, 3 distinguishes every n from 6 to 30; its gaps 1, 2, n−3 are distinct exactly when n ≥ 6.

## Encore packet (pp. 1–4, Problems 1–6): correct

All answers are right. Items 1–2 below concern P3–P4.

- **P1:** six-ring flip counts over all 64 two-kind words are 0 (12 words), 1 (42), 2 (6), 3 (2) and 6 (2), so exactly 1, 2 and 3 are all achievable.
- **P2:** exactly four is impossible, even with three kinds.
- **P3:**
  - Both printed starting patterns read AAABBABB.
  - The "half-turn: 4 spots" arrow sweeps 180°.
  - The minimum is 2 changed spots, and there are exactly four best words: AAABAAAB, AABBAABB, BAABBAAB and BABBBABB.
- **P4:**
  - The dashed line on the flip card passes through spots 0 and 4 (k=0). The turn arrows sweep 1 and 2 spots.
  - Minimum costs: flip 3 (8 best words), turn 1 spot 4 (2 best), turn 2 spots 4 (4 best). So the flip card is cheapest.
- **Layer figure (p. 4):** first layer {0,1}, second layer {1,3}. The stack shows first-only at 0, both at 1, neither at 2 and second-only at 3.
- **P5:** possible. 42 six-ring layers have exactly one flip, and none of them has a matching turn. 1416 ordered pairs of these stack to no match.
- **P6:** no stack of two half-turn layers ever loses the half-turn (all 64 pairs).
- **Ring sizes:** working spots are 28 mm. Adjacent centres are 31.0 mm on the six-rings and 28.3 mm on the eight-ring (gap 0.32 mm), as the bonus guide states.

## Adult guides

**Base guide:** correct throughout. I checked these statements:

- Overview:
  - 3 kinds for n = 3, 4, 5 and 2 for n ≥ 6;
  - the minority-at-most-two lower bound;
  - adjacent unique kinds suffice;
  - the 0, 1, 3 construction with gaps 1, 2, n−3;
  - at least three of each kind in any binary distinguishing ring, and the eight-ring minority answer 3;
  - n−1 nonidentity rotations and n reflections.
- Keys for all 16 problems. These include the K-1 P3 edit outcomes and the P6 gap multisets {1,2,5} and {1,3,4}. The two P6 key patterns cannot match each other.
- The p. 5 proofs:
  - a set of at most two spots is preserved by a reflection;
  - a reflection fixes at most two spots, and they are opposite;
  - a three-spot set is distinguishing exactly when its three gaps differ;
  - "one kind never distinguishes".
- The p. 5 counts 0, 0, 0, 12, 28, 96, 252, 600 for n = 3–10.
- The material figures: 28 mm spots, and 8 counters of each kind suffice for every single pattern.

**Bonus guide:** correct throughout. I checked:

- The subgroup / n/d-flip theorem, with its hypotheses.
- The P1 witnesses: AABBBB has k=1; ABBABB has k=0,3; ABABAB has k=0,2,4; AABABB has none.
- The eight-ring witnesses for 1, 2, 4 and 8 flips.
- The P2 proof.
- The P3 pairs, the minimum 2 and the four words.
- The P4 cycles, costs and best-repair counts: 4, 8, 2 and 4.
- The cycle-length-minus-top-frequency formula, which equals brute force for every case.
- The P5 witness (mark 0 has k=0 only; mark 1 has k=2 only), and the failure of opposite marks 0 and 3, which share k=0.
- The P6 argument and example {0,3}, {1,4}.
- The intersection rule.
- The ring spacing figures.

Item 2 below is an omission in this guide, not an error.

## Located problems (3, all minor; no incorrect answers)

### 1. Encore p. 2–3, Problems 3 and 4: "change" is not defined, and two natural readings change the answers

- **Quoted text:**
  - P3: "Change as few counter kinds as possible so that a half-turn matches. Find two different best repairs. Explain why fewer changes cannot work."
  - P4: "For each motion card, make the fewest changes that let it match. Which motion needs the fewest changes?"
  - The metric appears only in the bonus guide (p. 3): "count changed spots, not moves of the overlay."
- **Evidence:** `check.py`, section H.
  - **Changed spots (intended):** P3 needs 2. In P4 the flip needs 3 and each turn card needs 4, so the flip is cheapest.
  - **Exchanging two loose counters counted as one change:** this is a natural single action with loose counters.
    - P3 needs only 1. Exchanging spots 0 and 6 gives BAABBAAB, one of the guide's own best words.
    - In P4 the flip and the 2-spot turn tie at 2 exchanges. The 1-spot turn cannot be reached at all, because the start has 4 A and 4 B.
  - **"Change as few counter kinds" read literally:** recolouring every B as A changes one kind and gives AAAAAAAA, which matches the half-turn.
  - Under either other reading, "Explain why fewer changes cannot work" and "Which motion needs the fewest changes?" get different answers from the guide's.
- **Smallest fix:**
  - On p. 2, P3: "Each change replaces one counter with the other kind. Change as few counters as possible so that a half-turn matches." P4 then inherits the definition.
  - In the guide's P3–4 section, add: "Exchanging two counters counts as two changes."

### 2. Encore p. 2–3, starting pattern: it already matches a flip, which the guide does not mention

- **Quoted figure:** "starting pattern" A A A B B A B B, clockwise from the top (both pages). Guide p. 3: "Thus the selected flip is cheapest, three versus four and four."
- **Evidence:** `check.py`, section H.
  - AAABBABB matches the flip k=2, the axis through spot 1 (upper right, A) and spot 5 (lower left, A). That flip pairs spots 0↔2 (A,A), 3↔7 (B,B) and 4↔6 (B,B), so it needs 0 changes.
  - Costs for all eight flips from this start: k=0: 3, k=1: 2, k=2: 0, k=3: 2, k=4: 3, k=5: 2, k=6: 2, k=7: 2. The printed vertical axis (k=0) and the horizontal axis (k=4) are the two most expensive flips.
  - P4's answer is still right for the cards as printed, because the card fixes the axis.
  - But P1 has just trained children to "test every possible flip". The base rules let them turn a flipped copy until the spots line up. A child who does not hold the card's axis can therefore report a flip that needs no changes. An adult with this guide is not told why.
- **Smallest fix:** add one sentence to the guide's P3–4 solutions. "The start already matches the flip through spots 1 and 5 (upper-right and lower-left A), so a child who flips about another axis may find 0 changes; hold the card's vertical line, and keep the discovery as an extension."

### 3. K-1 p. 5, Problem 6: recolouring satisfies "cannot match each other", and the key does not say whether that counts

- **Quoted text:**
  - Student: "Build two two-kind patterns that no turn or flip can hide and that cannot match each other. Keep each on its own tracing copy."
  - Guide p. 3: "Use A A B A B B B B and A A B B A B B B. … A mere rotation, reflection, or shifted drawing of the first pattern is not a second answer."
  - Guide p. 1: kinds "are fixed categories and may not be permuted during testing".
- **Evidence:** `check.py`, section F.
  - Under the fixed-kind rule, swapping the two kinds of AABABBBB gives BBABAAAA. It is distinguishing and cannot match the original, because it has five A instead of three.
  - Building the same arrangement in kinds A and C instead of A and B also cannot match, and each pair's kit has three kinds.
  - So once a child has one pattern, a valid second answer takes no further search. The key lists only two 3-A arrangements with different gap multisets. It neither accepts nor excludes a recoloured copy, so adults may judge the same answer differently.
  - There are 6 non-matching distinguishing two-kind 8-rings in all. Two of them, the 5-A ones, are the swaps of the key's two.
- **Smallest fix:** in the guide's P6 key, add: "Swapping the two kinds, or using a different pair of kinds, also cannot match under the fixed-kind rule. Accept it, then ask for a second arrangement with the same two kinds and the same numbers of each (gaps {1,2,5} versus {1,3,4})." If recoloured answers should not count, change the page instead to "…that use the same two kinds the same number of times and cannot match each other."

## Not checked

- **Sources:** the citations to Albertson and Collins (EJC 3, R18) and *Math Circle by the Bay*. The base guide cites Preface pp. viii–ix and the bonus guide cites viii–x. The reference PDFs are not in this checkout. The mathematics they are cited for is standard, and I verified it independently above.
- **Physical fit and handling:**
  - 20 mm counters on 28 mm spots;
  - the bonus eight-ring, whose spots are 0.32 mm apart;
  - tracing copies that must read from both sides.

  Both guides already mark these untested. Counter supply is sufficient: the guide's two K-1 P6 key patterns together need 10 B against a kit of 8 per kind, but the page keeps each pattern on its own tracing copy, so they can be built one at a time.
- **The packets' own checkers:** `verify.py`, `verify_math.py`, `verify_revision.py`, `check_revised_cases.py` and `independent-check.py`, which I did not run, by design.
