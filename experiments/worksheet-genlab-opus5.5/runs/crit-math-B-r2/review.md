# Mathematical review: Week 7 take-away games (base draft)

Method: I rendered all 15 pages (5 per band) and read every one, then checked each problem with my own script (`scratch/verify.py`). The script does the following:
- computes W/L labels by backward induction;
- brute-forces the two-pile games directly, without using Grundy values;
- tries every plan in 2–3 Problems 2 and 5 against every possible partner reply, flagging illegal moves;
- brute-forces 4–5 Problem 5 over all rules {1} ∪ C with C ⊆ {2..19} and |C| ≤ 5;
- finds the start and period of the 4–5 Problem 9 pattern by checking up to 2000.

I also checked every counter picture, table and grid against the source coordinates and the rendered pages.

Overall, the mathematics is sound. Every intended answer exists and is correct, and every plan can be carried out in every line of play. Every "find them" or "is it possible" task has the answer the page implies. I found two issues, both on the K–1 packet. Grades 2–3 and grades 4–5 check out completely.

---

## Located problems

### 1. K–1, page 4, Problem 8: the winning rule for two piles is ambiguous, and the answers depend on it

Quoted text: "Take 1 or 2 counters from one of the two piles on each turn. For each pair of piles, circle whether you want to go 1st or 2nd." The pictures show the pairs 2|2, 1|2, 3|3 and 1|4.

The only winning rule a K–1 child hears is the packet-wide line "Take turns taking counters from **the pile**. Whoever takes **the last counter** wins." That line was written for one pile. With two piles, a young child (or the non-mathematician parent reading aloud) can easily take "the last counter" to mean the last counter of a pile, so that emptying either pile wins. The 2–3 and 4–5 versions of this problem avoid this by saying "whoever takes the very last counter wins". The K–1 version does not.

Evidence (both readings brute-forced):

| Piles | Intended reading (very last counter) | Alternative reading (empty either pile) |
|---|---|---|
| 2, 2 | 2nd | **1st** (take both from one pile) |
| 1, 2 | 1st | 1st |
| 3, 3 | 2nd | 2nd |
| 1, 4 | 2nd | **1st** (take the single counter) |

Under the alternative reading, two of the four cases flip, and two of them become one-move wins.

Smallest fix: add the sentence the older bands already use: "Take 1 or 2 counters from one of the two piles on each turn. **Whoever takes the very last counter wins.** For each pair of piles, circle whether you want to go 1st or 2nd."

### 2. K–1, page 5, Problems 9 and 10: the number of rows suggests more ways than there are (minor)

Quoted text:
- Problem 9: "A game starts with 4 counters, and each turn takes 1 or 2. Draw rings around the counters taken on each turn to show every different way the game can go." The box has **7 rows** of 4 counters.
- Problem 10: "Now find every different way a game with 5 counters can go, taking 1 or 2 on each turn." The box has **10 rows** of 5 counters.

Evidence: I enumerated the ordered sequences of 1s and 2s.
- A sum of 4 has **5** ways: 1111, 112, 121, 211, 22.
- A sum of 5 has **8** ways: 11111, 2111, 1211, 1121, 1112, 221, 212, 122.

(These are Fibonacci numbers. On a row of counters, contiguous ring patterns match these sequences one to one, so the count does not depend on how the rings are read.)

A kindergartner, or the parent volunteer, will naturally treat the rows as the number of answers to find. They may then hunt for 2 more ways that do not exist, or fill the rows with repeats or with rings around counters that are not next to each other.

Smallest fix: keep the spare rows, so the page does not give away the count, and add one short sentence to each problem: "Some rows may stay empty." If the organizer prefers, he could instead draw exactly 5 and 8 rows. That gives the count away, but it keeps the task of finding distinct ways.

---

## Problems verified correct (answer key from independent computation)

### K–1
All problems are correct apart from the two issues above.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 2–5: go 1st or 2nd | 2: 1st, 3: 2nd, 4: 1st, 5: 1st |
| 2 | Moves {1,2}, piles 4, 5, 7, 8: cross out a winning take | 4: take 1, 5: take 2, 7: take 1, 8: take 2. Each move is unique. All four piles are winning, so the instruction can always be carried out. |
| 3 | Moves {1,2}, piles 1–12: color where 2nd is better | 3, 6, 9, 12 |
| 4 | Ben moves first and always takes 2 when he can: where can you beat him? | Piles 3, 4, 6, 7. You cannot beat him at 2 or 5. |
| 5 | Moves {1,2,3}, piles 1–12 | 4, 8, 12 |
| 6 | Moves {1,3}, piles 1–12 | 2, 4, 6, 8, 10, 12 |
| 7 | Pile of 20 under each rule | {1,2}: 1st; {1,2,3}: 2nd; {1,3}: 2nd |
| 8 | Two piles, moves {1,2}, "very last counter" reading | 2,2: 2nd; 1,2: 1st; 3,3: 2nd; 1,4: 2nd. See issue 1. |
| 9, 10 | Every way a game can go | 5 ways and 8 ways. See issue 2. |

All counter counts in the pictures match their numerals (checked on the rendered pages).

### Grades 2–3
This band checks out completely. Every plan was tested against every possible partner reply, and no plan ever calls for an illegal move.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 4, 6, 7, 9, 11, 12 | first, second, first, second, first, second |
| 2 | Plans with moves {1,2} | Mia (8, first): wins every time. Leo (10, first): can lose, for example 10, 8, 7, 5, 4, 2, 0. Ana (9, second): wins every time. Sam (11, first): can lose; in fact he loses in all 8 lines of play, for example 11, 10, 9, 7, 6, 4, 3, 1, 0. |
| 3 | Moves {1,3,4}, piles 1–20 | Second at 2, 7, 9, 14, 16; first at all the others |
| 4 | Moves {1,3,4}, piles 25, 30, 37, 50 | first, second, second, first (losing piles leave remainder 0 or 2 when divided by 7) |
| 5 | Plans with moves {1,3,4} | Kai (10, first, always takes the most): can lose, for example 10, 6, 5, 1, 0. Theo (7, second, copies his partner): can lose, for example 7, 6, 5, 4, 3, 2, 1, 0. Zoe (9, second): wins every time; her "take all" step only happens at piles 4 or 1, where it is legal. |
| 6 | Jon's claim about {1,2,4} versus {1,2} | Jon is wrong. Both rules have losing piles 3, 6, 9, 12, 15, and they stay the same at least up to 500. |
| 7 | Two piles, moves {1,2} | 5,5: second (copy the partner's move in the other pile); 3,6: second; 1,5: first; 2,5: second |

### Grades 4–5
This band checks out completely.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 1–15, and a pile of 100 | Second at 3, 6, 9, 12, 15. With 100, go first: take 1, then always make each pair of turns add up to 3. |
| 2 | Moves {1,3,4}, W/L for piles 1–30 | WLWWWWL repeating; L at 2, 7, 9, 14, 16, 21, 23, 28, 30 (remainder 0 or 2 when divided by 7) |
| 3 | Seven rules, losing piles 1–24, pairs with the same losing piles | Three pairs: {1,2} and {1,2,4} (multiples of 3); {1,3} and {1,3,5} (even piles); {1,4} and {1,4,6} (remainder 0 or 2 when divided by 5). There are no other coincidences up to 24, and each pair stays identical up to 2000. |
| 4 | Kai always takes the most | Under {1,3,4}, his move hands his partner a winning pile at 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29. His move always leaves a losing pile only for {1,3} and {1,3,5}. For the other rules, the first pile where it fails is 4 for {1,2}, 5 for {1,2,3}, 8 for {1,4}, 5 for {1,2,4} and 9 for {1,4,6}. |
| 5 | Find a rule (including 1) for each list of losing piles | 4, 8, 12, …: {1,2,3}. 2, 5, 7, 10, …: {1,4}. 3, 7, 10, 14, …: {1,2,6}. 3, 5, 8, 10, …: impossible. Pile 2 must be winning, so 2 must be an allowed move. Then 5 can move to the losing pile 3, so 5 cannot be losing. A brute-force search found no rule. |
| 6 | Two piles, moves {1,2}, piles 0–7 | A pair is losing exactly when both piles leave the same remainder when divided by 3. Checked by brute force up to 30 by 30. |
| 7 | Two piles, moves {1,3,4}, piles 0–8 | Losing pairs (with the smaller pile first): the 9 equal pairs from 0,0 to 8,8, plus 0,2; 0,7; 1,3; 1,8; 2,7; 3,8; 4,6. All of these are pairs of piles with equal numbers from Problem 8. |
| 8 | Pile numbers (Grundy values) for {1,3,4}, piles 0–20, and two pairs | 0,1,0,1,2,3,2 repeating. 11 and 13 (both numbered 2) are a losing pair. 12 and 18 (numbered 3 and 2) are a winning pair: take 1 from the 12 to reach 11 and 18. Both results were confirmed by brute force of the two-pile game. |
| 9 | Moves {1,6,9}, W/L for piles 1–40, and where the pattern starts to repeat | L at 2, 4, 7, 12, 14, 17, 19, …, 39. From pile 10 on, the pattern WWLWL repeats every 5 (checked up to 2000). Before that, pile 9 is the only pile from 1 on that breaks the pattern. That makes the task a fair one: careless reading gives "repeats from the start". |
