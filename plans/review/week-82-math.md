# Week 82 (Endless class lines): math check

Scope:
- `lowell-math-circle-year-2/week-82/week-82-students.pdf`: one Grades 3–5 packet, 6 pages.
  - p. 1: the opening class-lines paragraph and three pictures, then Problem 1.
  - p. 2: Problem 2 (lines A, B, C). p. 3: Problem 3 (lines D, E). p. 4: Problem 4.
  - p. 5: 24 kid cards. p. 6: 4 star cards and 4 "after EVERY kid" panels.
- `week-82-facilitator.pdf`: 4 pages.

Sources read: `source/week-82/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md` and `SOURCES.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-82/`. Checked October 17, 2026.

**Result: every diagram, answer and guide statement is mathematically correct. I found 1 problem, minor. The page defines only "complete match" and shows a match that leaves a kid out. Problems 1–3 then ask about "every match" and "a match". Read literally, that changes Problem 1's count from 6 to 34, and makes "Can a match keep order?" trivially yes in Problems 2 and 3.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures):
  - **Finite cases.** Enumerates every complete match, and every match that may leave kids out, for the opening pictures (5 with 5, 5 with 6) and Problem 1 (3 with 3). Tests the page's order rule on every pair of kids.
  - **Endless lines.** Models each class line exactly as a word in W (one endless row 1, 2, 3, …) and S (one star kid). From the word it computes four order invariants symbolically, not by sampling:
    - which kids have infinitely many predecessors;
    - which kids have no kid immediately before them;
    - whether there is a last kid;
    - how many kids have only finitely many successors.

    It compares these with ordinal arithmetic below ω² (ω·a + b), computed separately.
  - **Matching rules.** The guide's rules and my own are written as formulas on every kid. For each one the script checks the inverse, one-to-one, onto, and order kept or broken on all kids up to n = 3000.
  - **Problem 4.** Covers all 16 arrangements of one or two endless rows with 0–2 stars, all 120 pairs of them, and the panels each one needs.
  - **Guide overview.** Checks the natural (surreal) sum against the ordinal sum.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures) reads the delivered student PDF with pdfplumber:
  - **Every page.** Headers, footers and consecutive problem numbers 1–4.
  - **p. 1 opening.** Both endpoints of every partner line in the three pictures. Each endpoint is mapped to the box whose label sits nearest it, and the result is compared with the captions. Also checks that "left out" is under F.
  - **p. 1 Problem 1.** R1–R3 and B1–B3 lie on two lines.
  - **p. 2 Problem 2.** The cards of lines A, B and C in order. C's star panel lies wholly to the right of the dashed box around its endless row.
  - **p. 3 Problem 3.** D's six cards lie on one horizontal line, with the red box entirely left of the blue box. E's cards run R1 B1 R2 B2 R3 B3, alternating colours, with the arrow after B3.
  - **pp. 4–6.** Four equal sketch boxes on p. 4. The 24 card labels on p. 5, each once, with frame colours. The stars and panel texts on p. 6.
  - **Guide.** Confirms every sentence quoted below with pdftotext.

The scripts replay the infinite statements on finite prefixes. The proofs, by hand:
- **A and B (1 + ω = ω).** f(★) = 1 and f(n) = n + 1, with inverse g(1) = ★ and g(m) = m − 1. Both are increasing.
- **A and C (ω + 1 ≠ ω).** An order-keeping complete match must send a last kid to a last kid, because everything is ≤ the last kid's image. C has a last kid and A has none. Ignoring order, ★ → 1 and n → n + 1 is a complete match.
- **D and E (ω + ω ≠ ω).**
  - The namesake match is a complete match, with Rₙ at position 2n − 1 of E and Bₙ at position 2n. It breaks order: R2 is before B1 in D, but B1 is at position 2 of E and R2 at position 3.
  - No order-keeping match exists, not even a one-to-one one into E. If B1 went to position p, then R1, …, Rp would need p increasing positions below p, and only p − 1 exist.
- **Problem 4.** For one or two rows, the number of limit kids and the number of kids with finitely many successors determine ω·a + b. Both are order invariants, so arrangements of different type cannot be matched keeping order.
  - Arrangements of the same type can be: stars waiting before a row go to the front of that row, and stars after the last row form the finite tail.
  - Every arrangement can be matched with 1, 2, 3, … ignoring order: stars first, then the rows' kids interleaved.
- The page's order rule is symmetric for complete matches between lines, so which class counts as "first" never matters.

## Student packet, Grades 3–5 (pp. 1–6): correct except item 1

- **Opening (p. 1).** The three pictures read back as 1–A … 5–E (complete, keeps order), 1–B, 2–A, 3–C, 4–D, 5–E (complete, does not keep order), and 1–A … 5–E with F unconnected and "left out" under it. All three captions are true. Of the 120 complete matches of 5 with 5, only the first keeps order, and 5 with 6 has no complete match.
- **P1.** 6 complete matches; only R1–B1, R2–B2, R3–B3 keeps order. Checking neighbours gives the same answer as checking every pair, as it must by transitivity. See item 1 for the other reading of "match".
- **P2.** A vs B: yes and yes (★ → 1, n → n + 1). A vs C: a complete match exists, but none keeps order (C has a last kid). The star panel is drawn wholly after the boxed endless row, as "after EVERY numbered kid" requires.
- **P3.** D vs E: a complete match exists (namesakes), but none keeps order (B1 has infinitely many kids before it). D is one horizontal line with the whole red block first, and E alternates R and B as printed.
- **P4.** Both requested pair types exist.
  - The 16 legal arrangements fall into six order types:

    | Order type | Arrangements |
    |---|---|
    | ω | W, SW, SSW |
    | ω+1 | WS, SWS |
    | ω+2 | WSS |
    | ω·2 | WW, SWW, WSW, SSWW, SWSW, WSSW |
    | ω·2+1 | WWS, SWWS, WSWS |
    | ω·2+2 | WWSS |
  - 22 pairs of different arrangements can be matched keeping order, and 98 only if order may change.
  - Under the other reading, where each arrangement is matched to one plain endless row, W, SW and SSW keep order.
  - The four equal boxes fit two pairs.
- **Materials (pp. 5–6).** R1–R12 and B1–B12 appear once each, in red and blue. There are 4 stars, 2 "This kid comes after EVERY kid" panels and 2 "This whole row starts after EVERY kid" panels.

### 1. p. 1 Problem 1, p. 2 Problem 2, p. 3 Problem 3 (minor): "match" is used without "complete", after the page has shown a match that is not complete

- **Quoted text:**
  - Opening (p. 1): "A complete match gives each kid a partner in the other class, with nobody left out." The third picture draws five partner lines, 1–A to 5–E, under "5 kids and 6 / no complete match possible", with "left out" under F.
  - Problem 1: "Find every match between these two class lines. Which matches keep order?"
  - Problems 2 and 3: "Can you match every kid? Can a match keep order?"
  - The word "complete" does not appear again after the opening (`check_diagrams.py.out`).
- **Evidence.** The page only ever qualifies "match" with "complete", and its third picture shows a pairing that is a match but not complete. So a child can read "match" as any pairing in which each kid has at most one partner.
  - **Problem 1.** There are then 34 matches between R1–R3 and B1–B3: 1 empty, 9 with one pair, 18 with two, and 6 complete. Of these, 20 keep order (1, 9, 9, 1), or 33 and 19 without the empty match (`check_math.py.out`). The guide's answer is 6 matches, 1 keeping order, and its "three choices, then two, then one" exhaustiveness argument covers only complete matches.
  - **Problems 2 and 3.** Read the same way, "Can a match keep order?" is trivially yes. For A vs C, pair n with n and leave the star out. For D vs E, pair each Rₙ with Rₙ (positions 1, 3, 5, … rise) and leave the blue kids out. The intended answer in both comparisons is no. The preceding "Can you match every kid?" points toward the complete reading but does not fix it.
- **Smallest fix:** insert "complete" three times and leave the organizer's opening paragraph unchanged:
  - Problem 1: "Find every complete match between these two class lines. Which matches keep order?"
  - Problems 2 and 3: "Can you match every kid? Can a complete match keep order?"

## Adult guide (4 pp.): checks out completely

The overview's facts are true with the stated hypotheses:
- 1 + ω = ω via ★ → 1, n → n + 1, and ω + 1 ≠ ω because of a last element.
- In ω + ω the first kid of the second block has infinitely many predecessors and no immediate one.
- A row of pairs has type 2·ω = ω, with finitely many predecessors for every kid, so it cannot be matched with ω + ω keeping order.
- All the lines are countable.
- Surreal (natural) addition is commutative, and 1 ⊕ ω = ω + 1 ≠ ω, so the warning against transferring 1 + ω = ω to Week 83 is right.

The solutions and examples are correct:
- Problem 1's six lists and the single order-keeping one, with the 3·2·1 exhaustiveness argument.
- Problem 2's onto, one-to-one and order argument, the last-kid contradiction, and the order-breaking size match for C.
- Problem 3's positions 2n − 1 and 2n and its B1 obstruction.
- Both Problem 4 examples.
- The launch description, "first two partners exchanged" and "counting proves every attempt fails".
- The page references: cards on p. 5, stars and panels on p. 6, continuation arrows on pp. 2–3.

The encore's ω² remark is correct.

**Not counted (outside the math scope, accepted design, or correct as printed):**
- **Identifier rule placement.** It first appears in Problem 2, by the organizer's choice. A child who assumes R1 must pair with B1 in Problem 1 would find one match. The opening's second picture (1–B, 2–A) already shows that partners are chosen freely, and "Find every match" implies more than one.
- **Problem 4 "two different arrangements."** A red row and a blue row differ only in labels, which the page says only identify kids. That would be a trivial same-type pair. The guide's examples make clear that structurally different arrangements are meant, and an adult can redirect.
- **Material counts.** These are physical, not mathematical, and hand-drawn rows on blank paper, as the guide suggests, avoid both limits.
  - p. 5 has one card per label, so D and E, which both contain R1–R3 and B1–B3, cannot both be laid out from one sheet with namesakes.
  - p. 6's two "this kid" panels suffice for any single Problem 4 arrangement, which needs at most 2. Two same-type pairs need 3 at once: WWS with WSWS, and SWWS with WSWS.
- **Guide hint "ask about the first kid of block B."** The student pages call this block "the blue row", and B is also Problem 2's line, whose first kid is the star. This is wording only.
- **Guide "Matching only six physical cards leaves an apparent unmatched card at the right edge."** This is true when both lines show numbered kids 1–6 (B also has the star, so 7 cards against 6). It is not true if each line has exactly six cards. This is wording only.
