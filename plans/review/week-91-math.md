# Week 91 (Rotor-router machines): math check

Scope:
- `lowell-math-circle-year-2/week-91/week-91-students.pdf`, 6 pages: Grades 2–3 pp. 1–3 (the rules and a three-picture demonstration, then Problems 1–3), Grades 4–5 pp. 4–5 (Problems 4–6), Grades 2–5 p. 6 (Problem 7).
- `week-91-return-visit.pdf`, 4 pages, Grades 4–5: the road rules and a worked short-road example, then Problems 1–6.
- `week-91-materials.pdf`, 7 pages: one-switch board, 4- and 8-exit tree boards, road boards 0–4 and 0–5, fold-and-glue cards, arrival strips and ENTRY markers.
- `week-91-facilitator.pdf`, 6 pages.
- There is no K–1 packet. The guide offers only an adult-run one-switch station.

Sources read: `source/week-91/student/generate.py` (the student, return and materials coordinates), `guide/facilitator.tex`, `build.py`, `README.md`, `SOURCES.md` and `QA.md`. All 23 pages were rendered at 80 dpi and inspected. The delivered guide PDF is byte-identical to the packaged reference copy. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-91/`. Checked October 23, 2026.

**Result: every student problem, diagram and material is mathematically correct, and so is the guide's theorem-first overview. I found 4 problems, all in the adult guide's keys or in layout:**
1. The guide's key for return Problem 4 gives the wrong output word.
2. The guide doesn't tell adults that the cards can change only during the first block, which is the answer under the other natural reading of return Problem 4.
3. The guide calls DABC's failure "a deeper reason", though it is the same root-alternation rule as ABCD.
4. On student p. 4, two target words sit closer to the tree above them than to their own tree.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 67 checks, 0 failures). It uses the packet's convention throughout: each card shows the NEXT exit, the counter follows it and the card then flips, one counter finishes before the next enters, and cards persist between counters.
  - **One switch.** Both 12-counter runs. The four printed strings, read anywhere in a run. The at-most-one discrepancy over every window of up to 40 visits. All 64 length-6 coin words against the 2 words a switch can make.
  - **Four-exit tree.** All 8 states: the 4- and 8-counter words, and whether the cards return. The D-first starts. The four targets of Problem 3. The guide's full key, using its card-word convention (root, left child, right child).
  - **Eight-exit tree.** All 128 states. The three targets of Problem 4. Whether each achievable order comes from exactly one start. The guide's Problem 5 witnesses.
  - **Complete trees, depths 1–4.** Every state, depth 4 included (32,768 states), over three consecutive blocks of 2^d, plus every sliding window of 2^d counters. Also an unequal-depth tree, as a counterexample.
  - **Roads.** Every state at every interior entry for m = 2–10 edges, 3m counters each (227,316 walks, 3,598,292 steps). It checks:
    - that every counter exits;
    - that position plus the number of right cards is unchanged at every step;
    - mR + S_final = ns + S_initial at every n;
    - exactly s right exits in every window of m consecutive launches;
    - whether the state after one block equals the state after two and three blocks.

    It also reproduces every printed trace: the worked example, P1, the P4 example and the guide's score table. It also checks the all-left words of P2 and P3 and the all-start counts.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 102 checks, 0 failures) reads the delivered PDFs with PyMuPDF. It recognises circles, counter dots, arrows (with the direction taken from the tip), lines and boxes. It checks:
  - **Every page.** Headers, footers and consecutive problem numbers.
  - **Tree diagrams.** All 12 student trees and both tree boards are complete binary trees of the stated depth, connected centre to centre, with blank switches, leaves A… from left to right, and round circles.
  - **p. 1 demonstration.** The arrows read down-left, down-left, down-right. The counter is beside the switch, then at X, then at X.
  - **Return p. 1 example.** The cards read R,L / R,R / L,L, with the counter at 2, then 1, then 3, and the entry arrow on 2.
  - **Return pp. 2–3.** Road lengths, entry positions (1, 2, 3 and 1, 2, 4), interior numbering and strip lengths.
  - **Materials.** 24 mm switch circles. 7 tree cards with faces down-left and down-right, and 4 road cards with faces left and right. The 50 mm bar and 48 squares of 15 mm.
- **By hand**, in a form the guide could use. After a block of m launches from an interior s, every interior card has been used. Each card's last departure points either to an endpoint or to a circle whose last departure came later. So the reversed arrows contain no loop: the NEXT word has no L immediately before an R, and it reads R…RL…L. Such a word is fixed by its number of R cards. The invariant gives S_final = S_initial over each block. So the state after every later block equals the state after the first block. The cards change during a block exactly when the start contains "LR" (4 of 8 starts on road 0–4, 11 of 16 on road 0–5, at every entry; the script confirms both).

## Grades 2–3, student pp. 1–3: correct

- **Rules and demonstration (p. 1).** The three pictures show the input arrow toward X with the counter beside it, then the counter at X with the arrow not yet flipped, then the arrow flipped toward Y. This matches "follow the NEXT arrow, then flip its card".
- **P1.** The 12-counter runs are XYXY… (first arrow L) and YXYX… (first arrow R). Of the printed strings, XYXY and YXYX can be made; XXYY and XYYX cannot.
- **P2.** D first forces the root R and the right child R. The left child is free, so RLR gives DACB DACB and RRR gives DBCA DBCA. "Find every arrival order" therefore has exactly 2 answers, which matches the two printed tree-and-strip pairs.
- **P3.** ACBD comes from LLL and BDAC from LRR. ABCD (counters 1–2) and DABC (counters 2–3) are impossible, because two consecutive outputs never share a root half. The four-exit tree makes 8 of the 24 orders.

## Grades 4–5, student pp. 4–5: correct except item 4 (layout)

- **P4.** AECGBFDH comes only from all seven cards L, and HDFBGCEA only from all seven R. AEBFCGDH is impossible: it alternates at the root, but the left subtree receives A, B first. The tree makes 128 distinct orders, each from exactly one start.
- **P5.** 40,192 of the 40,320 orders are valid answers. The guide's ABCDEFGH and AEDFBGCH are both impossible orders that use each exit once. AEDFBGCH's left subtree order ADBC is legal, as the guide says.
- **P6.** Both answers are yes, from every start, at depths 2 and 3, for aligned blocks and for any window of 2^d consecutive counters.

## Grades 2–5, student p. 6: correct

- **P7.** The coin can make all 64 six-counter words, so XXXXXX or any word with a repeated letter is a valid answer. The switch makes only XYXYXY and YXYXYX, so the coin covers everything the switch can make.

## Grades 4–5 return packet: correct

- **Example (p. 1).** 2→1 gives cards R,R; 1→2 gives L,R; 2→3 gives L,L, and the counter exits at 3. This matches the pictures and the guide's launch script.
- **P1.** Road 0–4, entry 1, starting cards LLR. The exits are 0,0,4,0,0,0,4,0, and the next four are 0,0,4,0. The cards are RLL after four counters and after eight.
- **P2.** Entries 1, 2 and 3 give 2, 4 and 6 right exits in eight launches, from all 8 starts. The all-left words are 0004, 0404 and 0444, each repeating.
- **P3.** From all 16 starts, entries 1, 2 and 4 give exactly 1, 2 and 4 counters at 5, so the answer is no for every entry. The all-left words are 00005, 00505 and 05555. Entry 3, which is not printed, gives 05055.
- **P4.** An example exists, but see item 2 for the other reading.
- **P5.** s at the right end and m − s at the left, from any start. The overview's proof is correct.
- **P6.** A counter cannot travel forever. Every walk exits; the longest single walk for m ≤ 10 is 45 steps.

## Materials: correct

Every board's structure and labels match the problems. The card faces are right: a sideways flip turns ↙ into ↘ and ← into →. One kit has 7 tree cards and 4 road cards, enough for the 8-exit tree and road 0–5.

## Adult guide: overview correct, except items 1–3

The overview's facts are all true, with the right hypotheses:
- At one switch, any n consecutive visits differ by at most one.
- A complete depth-d tree sends every block of 2^d once to each leaf, and the cards return. This needs equal depth: the unequal-depth tree fails.
- The road invariant mR + S_final = ns + S_initial holds, and with 0 ≤ S ≤ m − 1 it gives exact s-per-m blocks with no burn-in. The full state need not return, as the LLR example shows.
- Every counter terminates.
- On probability: a switch never makes XX, each coin word has probability 1/64, the fair-walk exit probability is s/m, and the 2^−m absorption bound holds.

The guide's keys match the computations: the first packet's P1, the P2 table, the full eight-word key in P3, P4, P5, P6 and P7, and the return packet's P1 trace, P2, P3 and the P5 score table.

## Problems found

### 1. Guide, return Problem 4 (p. 5): wrong output word

- **Text:** "Use the first problem's road, entry 1, initial LLR and block size four. The first two output blocks are both 0004."
- **Evidence:** from LLR the exits are 0, 0, 4, 0 | 0, 0, 4, 0 (`check_math.py.out`, "Return P1 / guide P1 / P4"). The guide gives the same thing on the same page: P1 says "initial LLR gives 0,0,4,0,0,0,4,0", and its trace table has counter 3 exiting at 4. "0004" is the all-left entry-1 word from P2, also on the same page. An adult checking a child's strip against this key will see 0040 and may think the child made a mistake. The guide's next sentence, "even the same endpoint word", is still true with 0040.
- **Fix:** change "both 0004" to "both 0040".

### 2. Guide, return Problem 4 (p. 5): no answer for the "keep changing" reading

- **Page:** "Can the exit counts repeat in equal blocks while the complete arrow positions change? Find an example or explain why none can exist." The record has three slots: "Starting arrows", "After one block" and "After two blocks".
- **Guide:** "Card states are LLR initially, RLL after the first block, and RLL after the second." It never says whether a change between "after one block" and "after two blocks" can happen.
- **Evidence:** it can't. On every road with m ≤ 10, from every start and every entry, the state after one block of m equals the state after two and three blocks. On the two printed roads this holds for every block size from 1 to 2m whose counts repeat (`check_math.py.out`). The proof is under "By hand" above. The cards change during a block exactly when the starting word has an L immediately before an R, so the change can happen only once, in the first block.
- **Consequence:** a child who reads "change" as "keep changing from block to block" will find After one = After two every time. That child can correctly answer "impossible after the first block". The guide gives the adult no way to recognise that answer as right, or to answer a child who asks why the second slot never differs.
- **Fix:** add to the guide's P4 entry: "The cards can change only during the first block. A block uses every interior card and leaves a word of the form R…RL…L, which is fixed by its number of R cards, and that number returns after each block. So 'after one block' and 'after two blocks' always agree. The cards change during the first block exactly when the start has an L immediately before an R, as LLR does." Optionally, the page could read "…while the arrows end the block in different positions from where they started it?"

### 3. Guide, first packet Problem 3 (p. 3): "deeper reason" misdescribes DABC

- **Text:** "ABCD is impossible because the first two outputs must lie in opposite root halves… DABC is impossible for a deeper reason: outputs 1 and 3 must come from the same half; D is right and B is left."
- **Evidence:** both words fail the same root-alternation rule. ABCD fails at counters 1–2 (A, B), and DABC at counters 2–3 (A, B both left). No four-exit output has two consecutive letters in one root half (`check_math.py.out`). The guide's own "Equivalently, after D,A, the third counter must go right" is that same root reason. An adult told the reason is "deeper" may look below the root for it, or fail to accept a child's correct "A and B are next to each other and both on the left".
- **Fix:** replace "for a deeper reason" with "for the same root reason, one step later: counters 2 and 3, A and B, are both left (equivalently, outputs 1 and 3 must share a half)".

### 4. Student p. 4, Problem 4: target words sit against the tree above

- **Diagram:** the words "H D F B G C E A" and "A E B F C G D H" are left-aligned at x = 15 mm. Each one's top edge is 1.9 mm below the leaf circles of the tree above it (130.2 mm against 128.3 mm; 195.2 mm against 193.3 mm). Its own tree's root is 4.3 mm lower and centred about 90 mm to the right. In the render, each word reads as a caption under the previous tree.
- **Consequence:** a child may record a program for HDFBGCEA on the first tree's miniature, or one for AEBFCGDH on the second. The mathematics is unaffected, but saved starts can end up beside the wrong target.
- **Fix:** move each of the three target words down about 10 mm, so that it sits level with its own tree's root, to the left of it. The words span x ≈ 15–60 mm, while at that height the root's edges run at x ≈ 103–108 mm, so nothing overlaps. Each word then sits about 12 mm below the tree above it, and the page length is unchanged.
