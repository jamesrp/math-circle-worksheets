# Hidden armies v1: mathematical review of the draft

Reviewer: independent math check (CRITIC-MATH stage). I did not edit the draft.

## How I checked it

I wrote my own enumerator in the scratchpad. It does not use the author's `check_answers.py`. A plan is an ordered triple (hill 1, hill 2, hill 3) of non-negative integers. A hill goes to the larger number, an equal hill goes to nobody, and the player with more hills wins. The checks:

- Plans nobody can beat, for every N from 0 to 15. The only ones are N=1 (every plan), N=2 (1-1-0, 1-0-1, 0-1-1) and N=3 (1-1-1 only). There are none for N from 4 to 15.
- The counter-plan rule (one more cube on each of the two smaller hills, the rest on the biggest) beats every plan for every N from 4 to 30.
- The fewest cubes that beat a plan q are (sum of the two smaller hills) + 2, for every plan with N from 1 to 14. The only exception is the empty plan 0-0-0.
- The full 28 × 28 table for 6 cubes, every 3-cycle, the Ben and Mia lists, and 4–5 Problem 8.
- I rebuilt every cube diagram on the K–1 pages from the TikZ coordinates in `draft/src/k-1.tex` (counting the cube rectangles above each hill ellipse, and the tokens). I read every strip value on the 2–3 and 4–5 pages from the PDF text and from page renders. Every diagram matches the plan the text intends. The rules picture is correct: 1-0-4 against 2-3-0, with tokens on hill 3 for the top plan and on hills 1 and 2 for the bottom plan, which wins 2 hills to 1.

## Problems found

### 1. K–1, page 1, Problem 2: the page assumes a plan that does not exist

Quoted: "Your partner can see your plan and tries to beat it. Find a plan with 5 cubes that nobody can beat."

Evidence: No 5-cube plan is unbeatable. Each of the 21 plans is beaten by at least one other; for example, 2-1-2 is beaten by 3-2-0 and by 0-2-3. The intended outcome is to find that there is no such plan. The wording tells the child that one exists, so a child who keeps failing has no reason to conclude "there isn't one". The older bands ask the same thing as an open question (2–3 P2, 4–5 P1).

Smallest fix: "Your partner can see your plan and tries to beat it. Is there a plan with 5 cubes that nobody can beat?"

### 2. K–1, page 3, Problem 4: the 4-cube case is impossible but is posed as a find

Quoted: "Find a plan that nobody can beat when each player has 2 cubes, then 3 cubes, then 4 cubes."

Evidence: 2 cubes works (1-1-0, 1-0-1 and 0-1-1 are the only unbeatable plans). 3 cubes works (1-1-1 only). 4 cubes has no unbeatable plan. The counter rule beats each one; for example, 0-2-2 beats 2-1-1 and 2-2-0 beats 1-1-2. The question "does it exist?" is the mathematics here, and the contrast between 3 and 4 is the point. The wording tells the child that all three cases succeed.

Smallest fix: "Is there a plan that nobody can beat when each player has 2 cubes? 3 cubes? 4 cubes?"

### 3. Grades 2–3, page 5, Problem 7: the stated permission rules out the 1-1-1 item

Quoted: "Now you may use fewer cubes than your partner. Beat each plan below with as few cubes as you can." The list includes "3 cubes 1 1 1".

Evidence: The fewest cubes that beat 1-1-1 is 4: for example 2-2-0, which wins two hills. That is more than the partner's 3. With 3 cubes or fewer, 1-1-1 cannot be beaten; P4 of this packet makes that point. So under the permission as printed, the 1-1-1 item has no answer. The intended rule, "two smaller hills + 2", also gives 4. The other items fit the wording:

| Plan | Fewest cubes | Partner's cubes |
|---|---|---|
| 6-0-0 | 2 | 6 |
| 4-1-1 | 4 | 6 |
| 3-2-1 | 5 | 6 |
| 2-2-2 | 6 | 6 |
| 3-3-0 | 5 | 6 |
| 8-1-1 | 4 | 10 |
| 5-3-2 | 7 | 10 |

Smallest fix: "Now you may use a different number of cubes from your partner." The 4–5 wording ("the two players may have different numbers of cubes") is already correct.

### 4. K–1, page 5, Problem 6: the rule changes without being stated, and the 1-1-1 answer depends on the reading

Quoted: "For each plan below, draw a plan that beats it with as few cubes as you can." The shared rule at the top of page 1 is still "Both players have the same number of cubes."

Evidence: The fewest cubes are 2, 3, 4, 5 and 4 for 5-0-0, 1-4-0, 1-3-1, 2-2-1 and 1-1-1. The last item needs 4 cubes against the partner's 3. If the page-1 rule still holds, 1-1-1 cannot be beaten at all, which matches P4 of the same packet. If it does not hold, the answer is 4. The page does not say which reading applies.

Smallest fix: add one short sentence: "You may use a different number of cubes from the plan." (or "You may use any number of cubes.")

### 5. Grades 2–3, page 2, Problem 3, and grades 4–5, page 2, Problem 2: "beat any plan" is false for small numbers of cubes

Quoted:
- 2–3: "Then explain how you can beat any plan that your partner names."
- 4–5: "Then explain a way to beat any plan that your partner names."

Evidence: Some plans with 1, 2 or 3 cubes cannot be beaten: every 1-cube plan, 1-1-0 and its arrangements, and 1-1-1. The very next problem asks for one of them (2–3 P4: "Each player has 3 cubes. Find a plan that nobody can beat"; 4–5 P3: 1 to 5 cubes). The counter rule works exactly when the biggest hill has at least 2 cubes, which holds for every plan from N = 4 on. So the printed claim is false, and it contradicts the next problem. All the listed plans have 6, 7, 9, 10, 20 or 100 cubes, so a restriction to those sizes keeps the intent and leaves the 3-versus-4 discovery to the next problem.

Smallest fix: "...beat any plan with 6 or more cubes that your partner names."

### 6. Grades 2–3, page 1, Problem 1: "circle the plan that won" has nothing to circle in a tie, and ties are common

Quoted: "For each game, write both plans and circle the plan that won."

Evidence: With 6 cubes, every one of the 28 plans ties exactly 13 of the 28 plans, counting itself. So 364 of the 784 ordered pairs are ties, about 46%. Examples are 3-2-1 against 1-2-3, and 5-1-0 against 0-1-5. A large share of recorded games will have no plan to circle. The rules do define a tie, so this is minor, but the instruction cannot be carried out for those games.

Smallest fix: "...and circle the plan that won, if one did."

### 7. K–1, page 6, Problem 7 (low severity): many more answer boards than answers

Quoted: "For each plan below, find every plan with 5 cubes that beats it." 3-1-1 has 6 boards and 4-0-1 has 9 boards.

Evidence:
- 3-1-1 is beaten by exactly 3 plans with 5 cubes: 1-2-2, 0-3-2 and 0-2-3.
- 4-0-1 is beaten by exactly 6: 2-1-2, 1-2-2, 1-1-3, 0-3-2, 0-2-3 and 0-1-4.

Kindergartners tend to treat empty boards as tasks still to do. Twice as many boards as answers for 3-1-1 invites them to draw plans that do not win, or to repeat plans, and it hides the moment when they have found them all. Extra space for 2–3 P6 (6 strips for 3 answers, 20 for 15) is less of a concern, because that problem asks the child to explain completeness.

Smallest fix, if the organizer wants it: 4 boards for 3-1-1 and 7 or 8 for 4-0-1. That still does not give away the counts. Otherwise, keep the boards and tell the adult the true counts.

### 8. Grades 4–5, page 6, Problem 7 (negligible edge case, no change needed)

Quoted: "Find a rule that works for any plan."

The rule "two smaller hills + 2" holds for every plan with at least one cube, but not for the empty plan 0-0-0, which 1 cube beats. Nobody plays with 0 cubes, so I mention it only for completeness.

## Answers I verified (no problem found)

### K–1

- **P1:** Open play with 5 cubes. No 5-cube plan is safe, so the play is sound.
- **P3:** Every given plan (5-0-0, 0-4-1, 0-3-2, 2-1-2) has 5 cubes and can be beaten with 5. Each board leaves room for a 4-cube tower. The number of beating plans is:

  | Plan | Plans that beat it |
  |---|---|
  | 5-0-0 | 10 |
  | 0-4-1 | 6 |
  | 0-3-2 | 4 |
  | 2-1-2 | 2 (3-2-0 and 0-2-3) |

  The last item is the hardest and is fair.
- **P5:** No row is a tie.
  - Group 1: 2-2-1 beats 4-1-0, 4-1-0 beats 0-0-5, and 2-2-1 beats 0-0-5. 2-2-1 is the best.
  - Group 2: 0-1-4 beats 2-0-3, 2-0-3 beats 1-2-2, and 1-2-2 beats 0-1-4. This is a circle with no best plan.
- **P6** (under the "any number of cubes" reading): the fewest cubes are 2, 3, 4, 5 and 4. Examples: 0-1-1, 2-0-1, 2-0-2, 3-0-2, and 2-2-0 (or 2-1-1).

### Grades 2–3

- **P2:** No 6-cube plan is safe.
- **P3:** All nine given plans have the stated totals, and each can be beaten with the same total.
- **P4:** 1-1-1 is the only unbeatable 3-cube plan. There is none with 4 cubes.
- **P5:** A 3-cycle containing 2-2-2 exists, for example 2-2-2 → 4-1-1 → 3-3-0 → 2-2-2; there are 12 such cycles. 6-0-0 beats no plan, so no cycle contains it. The arrow direction (top → right → left → top) is consistent.
- **P6:** Exactly 3 plans beat 2-2-2 (3-3-0, 3-0-3, 0-3-3). Exactly 15 beat 6-0-0: the plans with at least one cube on each of hills 2 and 3.
- **P7:** Fewest cubes as in item 3 above. The "quick way" is two smaller hills + 2.

### Grades 4–5

- **P1:** No 6-cube plan is safe.
- **P2:** All nine given plans have the stated totals and can be beaten; 50-0-50 is beaten by 48-1-51.
- **P3:** Unbeatable plans exist for 1, 2 and 3 cubes, and not for 4 or 5. None exists for any larger N (checked to 15, and the counter rule proves it for N ≥ 4).
- **P4:** The table shows all 28 plans, each exactly once. The counts of plans beaten:

  | Arrangements of | Plans it beats |
  |---|---|
  | 6-0-0 | 0 |
  | 5-1-0 | 5 |
  | 4-2-0 | 8 |
  | 4-1-1 | 9 |
  | 3-3-0 | 9 |
  | 3-2-1 | 11 |
  | 2-2-2 | 12 |

  2-2-2 alone beats the most. 6-0-0, 0-6-0 and 0-0-6 beat the fewest (none). For the adult: every plan ties exactly 13, so "beats" plus "is beaten by" is always 15, and symmetry reduces the work to 7 cases.
- **P5:** Every plan except 6-0-0, 0-6-0 and 0-0-6 lies on some 3-cycle; there are 180 cycles up to rotation. Example cycles for each type:

  | Type | Example cycle |
  |---|---|
  | 5-1-0 | 0-4-2 → 5-1-0 → 2-0-4 |
  | 4-2-0 | 1-1-4 → 5-0-1 → 4-2-0 |
  | 4-1-1 | 1-2-3 → 4-1-1 → 2-4-0 |
  | 3-3-0 | 2-1-3 → 5-0-1 → 3-3-0 |
  | 3-2-1 | 1-3-2 → 3-2-1 → 2-0-4 |
  | 2-2-2 | 2-2-2 → 5-1-0 → 3-0-3 |

- **P6:** Ben's list is all arrangements of 3-2-1. Exactly 3-3-0, 3-0-3 and 0-3-3 beat 2 of his plans and lose to none. Mia's list is all arrangements of 4-2-0. No 6-cube plan beats more of her plans than it loses to; the best is even, at 2 wins and 2 losses. Both of the page's intended outcomes are correct. The die faces 1 to 6 are drawn correctly.
- **P7:** The fewest cubes are 2, 4, 5, 6, 4 and 62. For 40-30-30, 0-31-31 wins and no 61-cube plan wins; I checked all 61-cube plans.
- **P8:** Against a 6-cube partner, 8 cubes is the fewest for a plan they cannot beat (3-3-2 and its arrangements). 9 is the fewest for a plan that beats every 6-cube plan (3-3-3 only). Both answers are the same if the partner may also use fewer than 6 cubes, because adding cubes never hurts the partner.
