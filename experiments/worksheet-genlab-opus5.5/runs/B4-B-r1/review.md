# Correctness review: Week 7 take-away games (base draft)

Method: I rendered all 16 pages (K-1: 5, grades 2-3: 5, grades 4-5: 6) and looked at each one. I regenerated the .tex files from `src/make.py` and they match the submitted sources byte for byte. I parsed every TikZ picture to count the counters in each tray and to check the box, strip and grid labels. Then I solved every game by brute force (`scratch/solve.py`, `scratch/solve2.py`): win/lose labels, winning moves, Grundy values, direct minimax on the two-pile games (no Grundy shortcut), a game tree for the claims in 2-3 P3, a minimax against Dana's greedy plan, and a search over all move sets for the "find a rule" and "find every game" problems.

**Overall:** every intended answer is correct, and every diagram matches its text (pile sizes, pair sizes, box and strip numbering, grid labels). No problem is impossible, and no claim on any page is false. I found four wording or layout issues. Two of them (items 1 and 2) can change a child's answer.

---

## Located problems

### 1. Two-pile games: "the last counter" has a second reading that changes the answers (all three bands)

- **Where:**
  - K-1, page 4: Problems 8 and 9.
  - Grades 2-3, page 4: Problem 7.
  - Grades 4-5, pages 5-6: Problems 8 and 9.
- **Text:**
  - The general rule on each page 1 is stated for a single pile: "Two players take turns taking counters from a pile. … Whoever takes the last counter wins."
  - The two-pile problems then say only "Now there are two piles, and on your turn you take 1 or 2 counters from one pile" (K-1 P8) and "Now there are two piles. On each turn, a player takes 1 or 2 counters from one of the piles" (2-3 P7).
  - 4-5 P8 says "…from one of the piles, and whoever takes the last counter wins."
- **The problem:** With two piles, each pile has its own last counter. A child can easily hear "whoever takes the last counter wins" as "whoever empties a pile wins", especially K-1 children, who hear the problem read aloud once. The intended reading is "the last counter of all".
- **Evidence (brute force under both readings, take 1 or 2):**

  | Position | Intended reading | "Empty a pile wins" reading |
  |---|---|---|
  | K-1 P8 (1,1) | 2nd | 1st |
  | K-1 P8 (2,2) | 2nd | 1st |
  | K-1 P8 (1,4) | 2nd | 1st |
  | 2-3 P7 (4,1) | Second | First |

  - Under the second reading, five of the six K-1 cases become "1st". That makes the problem nearly trivial and destroys the contrast the author built in with (1,4).
  - The 4-5 P8 grid also changes completely. Under the intended reading the "second" squares are exactly those with a ≡ b (mod 3). Under the other reading, every square with a pile of 1 or 2 is a first-player win.
- **Smallest fix:** Name the winning counter explicitly in each two-pile problem.
  - K-1 P8: "Now there are two piles. On your turn, take 1 or 2 counters from one pile. Whoever takes the very last counter on the table wins."
  - 2-3 P7: add "Whoever takes the last counter on the table wins."
  - 4-5 P8: change "whoever takes the last counter wins" to "whoever takes the last counter on the table wins".
  - P9 in K-1 and in 4-5 refers back to P8, so it is covered.

### 2. K-1, page 5, Problem 10: the move rule is not restated after Problem 7 changed it

- **Text:** "Now there is one pile again, and whoever takes the last counter loses. Put an X on every trap from 1 to 20."
- **The problem:** Problem 7 switched the moves to "1, 2, or 3". Problems 8 and 9 restate "1 or 2", but Problem 10 says nothing about the moves. An adult reading aloud, or a child who starts at this page (the brief allows stopping and starting anywhere), may carry "1, 2, or 3" over from the last one-pile track problem, which is P7.
- **Evidence:** In the misère game the traps depend on the move rule:

  | Moves | Traps from 1 to 20 |
  |---|---|
  | {1, 2} (intended) | 1, 4, 7, 10, 13, 16, 19 |
  | {1, 2, 3} (carried over from P7) | 1, 5, 9, 13, 17 |

- **Smallest fix:** "Now there is one pile again. Take 1 or 2 counters on each turn, and whoever takes the last counter loses. Put an X on every trap from 1 to 20."

### 3. K-1, page 3, Problem 6: the number of blank rows suggests the wrong number of ways

- **Text and diagram:** "Show every different way a game with 4 counters can go, and then every way a game with 5 counters can go." The page gives 8 blank rows of 4 counters and 10 blank rows of 5 counters.
- **Evidence:** The games are the ordered sequences of 1s and 2s with the right sum.
  - 4 counters: 5 ways (1111, 112, 121, 211, 22).
  - 5 counters: 8 ways (11111, 1112, 1121, 1211, 122, 2111, 212, 221).
  - A K-1 child, or the adult, who sees 8 rows and 10 rows will expect 8 and 10 ways. They may keep searching, or fill the extra rows with repeats, on a "find all" task whose real answer is 5 and 8.
- **Smallest fix:** In `make.py`, change `range(8)` to `range(5)` and `range(10)` to `range(8)` so the page shows exactly 5 and 8 rows.
  - If the organizer would rather not reveal the count, keep spare rows but make the difference obvious and not suggestive. For example, put one extra row in each column, so a child can see a spare row is left over.

### 4. Grades 4-5, page 5, Problem 8: the row 0 / column 0 square is not a playable starting position

- **Text:** "row 0 or column 0 stands for an empty pile. Shade every square where you would rather go second."
- **The problem:** Square (row 0, column 0) is two empty piles. No counter is ever taken, so the page's rule ("whoever takes the last counter wins") does not decide who wins, and "would you rather go first or second" has no answer. In the backward-induction sense it counts as a loss for the player to move. A careful child will be stuck on it, or will argue either way.
  - The rest of row 0 and column 0 is fine: those squares are one-pile games. For example, (0,3) and (0,6) are "second" squares.
  - In P9 the task asks only for unequal piles from 1 to 8, so the corner square is not part of that task.
- **Smallest fix:** Cross out or grey out the top-left square of the grid, in P8 and, for consistency, in P9. The alternative is to say "Shade every other square where…". The text would not need to say anything else.

---

## Bands checked with no further problems (verified answers)

### K-1 (moves 1 or 2, last counter wins, unless stated)

| Problem | Verified answer |
|---|---|
| P1 | 1 → take 1; 2 → take 2; 3 → cross out; 4 → take 1; 5 → take 2. The winning move is unique in each pile. |
| P2 | 6: 2nd; 7: 1st; 8: 1st; 9: 2nd. |
| P3 | 10 → take 1; 11 → take 2; 12 → cross out. |
| P4 | Traps 3, 6, 9, 12, 15, 18. |
| P5 | After Ben takes 2, he can be sure to win only at 5, 8, 11 (they leave 3, 6, 9). At 4, 7, 10 he cannot. |
| P6 | 5 ways and 8 ways. See item 3 for the row counts. |
| P7 | Moves {1, 2, 3}: traps 4, 8, 12, 16, 20. |
| P8 | (1,1) 2nd; (1,2) 1st; (2,2) 2nd; (2,3) 1st; (3,3) 2nd; (1,4) 2nd. Checked by direct minimax. |
| P9 | (6,6): the second player wins by copying each move in the other pile. |
| P10 | Misère {1, 2}: traps 1, 4, 7, 10, 13, 16, 19. |

All tray counts match their labels: 1-5; 6-9; 10-12; 4, 5, 7, 8, 10, 11; the six P8 pairs; 6 and 6.

### Grades 2-3

| Problem | Verified answer |
|---|---|
| P1 | 5: first, take 2. 6: second. 7: first, take 1. 8: first, take 2. 9: second. 10: first, take 1. |
| P2 | Lee is right: 12 is a multiple of 3 and his reply always restores a multiple of 3. Mo is wrong: 10 − 2 = 8, so the opponent takes 2 (leaving 6) and then makes 3 each round. Mo should take 1. |
| P3 | Jo is right; 7 is losing under {1, 3, 4}. Full tree from 7: partner takes 1 → 6, Jo takes 4 → 2, partner must take 1, Jo takes the last. Partner takes 3 → 4, Jo takes 4. Partner takes 4 → 3, Jo takes 3. Kai is wrong: from 8 the partner takes 1, leaving 7. Kai's winning move from 12 was 3. |
| P4 | Shade 2, 7, 9, 14, 16. In every other box, take 4 at 4, 6, 11, 13, 18, 20; take 3 at 5, 12, 19; take 1 at 1, 8, 15; take 1 or 3 at 3, 10, 17 (two correct answers there). |
| P5 | 30: second. 50: first, take 1. 61: first, take 3. 100: second. |
| P6 | {1, 3, 5}: shade the even piles. Every move is odd, so the number of moves has the same parity as the pile. From an even pile the second player makes the last move however anyone plays. |
| P7 | (3,3) Second; (4,2) First; (4,1) Second; (5,3) First. The second player wins on equal piles by copying. See item 1. |
| P8 | {1, 2, 3, 4} works. A rule works exactly when it contains 1, 2, 3 and 4 and no multiple of 5; 64 such rules use numbers up to 12. A different rule therefore has to add a non-multiple of 5 above 5, for example {1, 2, 3, 4, 6}. The task is solvable as posed. |

The P7 diagram pairs (3,3), (4,2), (4,1), (5,3) match.

### Grades 4-5

| Problem | Verified answer |
|---|---|
| P1 | {1, 3, 4}: shade 2, 7, 9, 14, 16, 21, 23. The winning first moves are as in 2-3 P4, plus 22 → 1 and 24 → 1 or 3. |
| P2 | 100: losing (100 mod 7 = 2). 1000: winning, take 4. 2026: winning, take 1 or 3 (2026 mod 7 = 3). |
| P3 | {1, 2}: multiples of 3. {1, 2, 4}: multiples of 3. {1, 4}: 2, 5, 7, 10, 12, 15, 17, 20 (remainder 0 or 2 mod 5). {1, 3, 5}: the even numbers. |
| P4 | Greedy fails in {1, 2} (e.g. 4), {1, 3, 4} (e.g. 5) and {1, 4} (e.g. 8; 3 is fine because only 1 is allowed there). Checked by minimax with Dana greedy on every turn. It always wins in {1, 3, 5}, because every play wins from an odd pile. |
| P5 | The {1, 3, 4} pattern (losing iff n mod 7 is 0 or 2) holds for every n. |
| P6 | Exactly 4 games: {1, 2, 3}, {1, 2, 3, 5}, {1, 2, 3, 6}, {1, 2, 3, 5, 6}. Searched all 63 subsets, checked to n = 1000. |
| P7 | Misère {1, 2}: 1, 4, 7, 10, 13, 16, 19. Misère {1, 3, 4}: 1, 3, 8, 10, 15, 17. Both are the normal-play pattern shifted up by one. |
| P8 | "Second" squares are exactly those with a ≡ b (mod 3). Equal piles are a second-player win. See items 1 and 4. |
| P9 | The unequal pairs from 1 to 8 are exactly {1,3}, {1,8}, {3,8}, {2,7}, {4,6}: 5 pairs. Grundy values 0,1,0,1,2,3,2 repeat with period 7. Confirmed by direct minimax. |

All strip, chart and grid labels are correct: 1-24; 1-20 on each strip; grids 0-7 and 0-8.
