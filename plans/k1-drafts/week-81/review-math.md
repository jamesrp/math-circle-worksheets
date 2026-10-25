# Week 81 K–1 (W81-K-v1): mathematical review

I reviewed `draft/k-1.pdf` (7 pages) and `draft/src/k-1.tex`. I did not use the author's `check.py`. I wrote a separate solver for the one-each refill rule that labels positions as wins or losses, lists every legal move and winning move, collects every possible game length, and finds the most counters on the board at once. I also wrote a parser that reads every bucket rectangle and dot from the TikZ source and counts the dots inside each bucket. The scripts are in the session scratchpad (`chk/solve.py`, `chk/parse.py`, `chk/alt.py`).

**Overall:** every answer the packet relies on is correct. Every start picture matches the position the problems assume. The worked rule picture shows a legal move: (0, 2), take from bucket 2 into Removed giving (0, 1), then one from Supply into bucket 1 giving (1, 1), with Supply going 3, 3, 2 and Removed 0, 1, 1. The rule wording rules out both misreadings named in the outline: "may" keeps the refill optional, and a refill can go only into a smaller-numbered bucket. The problems I found are in how the pages are set up (slot counts, ambiguous wording and where a rule is placed). None of them is a wrong answer.

## Verified answers (no error found)

| Problem (page) | Start(s) as drawn | Verified outcome |
|---|---|---|
| Rules (1) | (0, 2) → (0, 1) → (1, 1) | Legal move; Supply and Removed counts correct |
| 1 (1) | one bucket: 2, 3, 4, 5, 6, 7, 10, 11 | No choices are possible, so the game lasts exactly n moves. First player wins 3, 5, 7, 11; second player wins 2, 4, 6, 10 |
| 2 (2) | (1,1) (2,0) (0,2) / (2,1) (1,2) (2,2) | First player wins (1,1), (2,1), (1,2); second player wins (2,0), (0,2), (2,2) |
| 3 (2) | (1,1) (2,1) / (1,2) (3,1) / (2,3) (3,3) | All are first-player wins with exactly one winning move each: (2,0) refill; (2,0) no refill; (0,2) take from 1; (4,0) refill; (2,2) no refill; (4,2) refill |
| 4 (3) | (4,2), (3,4) | (4,2): second player wins (6–8 moves). (3,4): first player wins, and the only winning move is to take from bucket 1, giving (2,4) |
| 5 (3) | (2,2) | The partner has exactly **3** moves: (1,2), (2,1), (3,1). The unique winning replies are (0,2), (2,0), (4,0) |
| 6 (4) | 4 and 6 counters | 4 counters: (4,0), (2,2), (0,4), which is **3** ways. 6 counters: (6,0), (4,2), (2,4), (0,6), which is 4 ways |
| 7 (4) | 5 counters | Impossible: every split of 5 has an odd bucket, and all six such positions are first-player wins |
| 8 (5) | (0,1) (0,2) (0,3) / (1,1) (2,2) (3,3) | Shortest/longest: 1/2, 2/4, 3/6, 2/3, 4/6, 6/9. Every length in between also occurs. The most counters a game uses is 9 |
| 9 (5) | (0,0,1) (0,0,2) (0,0,3) | Most counters on the board at once: 2, 4, 6 |
| 10 (6) | same three starts | Longest games: 4, 8, 12 (the shortest are 1, 2, 3) |
| 11 (6) | (3,3,3) | Cannot go on forever. Games last 9 to 21 moves, with at most 12 counters on the board |
| 12 (7) | (2,0,1) (1,0,1) (0,1,1) (1,1,1) | All are first-player wins with one winning move each: (2,0,0) take from 3 and add nothing; (2,0,0) take from 3 and add to bucket 1; (0,2,0) take from 3 and add to bucket 2; (2,2,0) take from 3 and add to buckets 1 and 2 |

I also confirmed the rule behind the whole packet: the second player wins exactly when every bucket holds an even number. I checked this for two buckets up to 10 each and three buckets up to 6 each.

## Located problems

### 1. Problem 5 has four answer rows, but the partner has only three moves

- **Band/page/problem:** K–1, page 3, Problem 5.
- **Text and diagram:** "Draw the buckets after every move your partner can make. Next to each, draw a move that lets you always win." Below it are **four** rows of answer pictures (blank bucket pair → blank bucket pair).
- **Evidence:** from (2,2) there are exactly three legal moves, giving three different positions: take from bucket 1 → (1,2); take from bucket 2 → (2,1); take from bucket 2 and refill bucket 1 → (3,1). Any fourth position a child draws must come from an illegal move, such as (1,3) from putting a counter into bucket 2, or a duplicate of one already drawn. A K–1 child who fills every row will be pushed toward an illegal move.
- **Smallest fix:** draw three rows (`rows = 4` → `rows = 3` in `p5()`). If the author prefers not to reveal the count, the fourth row needs to be clearly marked as extra space. An unmarked fourth row on a "find every" task tells the child that a fourth answer exists.

### 2. Problem 6 has four slots in the 4-counter row but only three answers, and one reading of the wording changes the counts

- **Band/page/problem:** K–1, page 4, Problem 6.
- **Text and diagram:** "Find every way to put 4 counters into buckets 1 and 2 so that the player who goes second can always win. Then do the same with 6 counters." Both rows, "4 counters" and "6 counters", have **four** blank bucket pairs.
- **Evidence:**
  - With an empty bucket allowed, 4 counters give only (4,0), (2,2), (0,4): three answers. The page implies four. The 6-counter row has exactly four answers, so the two rows seem to tell the child that the counts are equal. A child looking for a fourth 4-counter answer will try (1,3) or (3,1), and both are first-player wins.
  - "Put 4 counters into buckets 1 and 2" can also be heard as "put some in each bucket." Under that reading the answers are just (2,2) for 4 counters and (4,2), (2,4) for 6.
- **Smallest fix:** draw three pairs in the 4-counter row and keep four in the 6-counter row. Add "A bucket can be empty." to settle the reading. If the intended reading is the other one (no empty bucket), the slots should be 1 and 2.

### 3. Problem 7 has three answer boards for a task that has no solution

- **Band/page/problem:** K–1, page 4, Problem 7.
- **Text and diagram:** "If you can, put 5 counters into buckets 1 and 2 so that the player who goes second can always win. If you can't, explain why." Below it are three blank two-bucket boards.
- **Evidence:** none of the six splits of 5 ((5,0), (4,1), (3,2), (2,3), (1,4), (0,5)) is a second-player win, because one bucket is always odd. The wording is neutral, but three answer boards suggest there are up to three solutions to draw. That works against the "explain why it can't be done" ending.
- **Smallest fix:** use a single two-bucket board, or none, and leave the rest of the space for the explanation. The page already has plenty of blank space below.

### 4. Problem 9's "at one time" can be heard as "in one move"

- **Band/page/problem:** K–1, page 5, Problem 9.
- **Text:** "Work together to get as many counters into the buckets at one time as you can. Write how many."
- **Evidence:** the intended answers are the most counters on the board at the same moment: 2, 4, 6. Read aloud, "get as many counters into the buckets at one time" also means "put in as many counters as you can in a single turn." Under that reading the answer is 2 for every start, since one move from bucket 3 adds at most 2. The three contrasting starts then lose their point.
- **Smallest fix:** "Work together to make the number of counters in the buckets as big as you can. Write the biggest number."

### 5. The bucket-3 rule appears only inside Problem 9, but Problems 10–12 depend on it

- **Band/page/problem:** K–1, pages 5–7, Problems 9, 10, 11, 12.
- **Text:** the shared rules give only the bucket-2 refill. The bucket-3 refill is stated only inside Problem 9: "If you take a counter from bucket 3, you may put one counter from Supply into bucket 1 and you may put one into bucket 2." Problems 10, 11 and 12 use three buckets and do not repeat or refer to it.
- **Evidence:** a table that skips Problem 9 has only the shared rule, under which taking from bucket 3 allows no refill. My solver gives these answers under that reading:
  - Problem 10's longest games become 1, 2, 3 instead of 4, 8, 12.
  - In Problem 12, **(1,0,1) becomes a second-player win**, so "Find a first move that lets you always win" has no answer for that start.
  - The winning moves for (0,1,1) and (1,1,1) change to (1,0,1).

  This is a rule for the whole three-bucket part of the packet, not for Problem 9 alone.
- **Smallest fix:** move the bucket-3 sentence into the shared rules, right after the bucket-2 sentence ("If you took it from bucket 3, you may put one counter from Supply into bucket 1 and one into bucket 2."). Problem 9 then opens with "Uncover bucket 3." A lighter alternative is to keep the rule in Problem 9 and start Problem 12 with "Use the bucket 3 rule from Problem 9."

### 6. Problems 8 and 10 give the wrong count if Removed is not emptied between games (minor)

- **Band/page/problem:** K–1, page 5 Problem 8 and page 6 Problem 10.
- **Text:** "make the game as short as you can and then as long as you can. Write how many counters end up in Removed."
- **Evidence:** the count in Removed equals the number of moves only if Removed starts empty. Problem 8 asks for two games in a row from each start. If Removed is not cleared, (0,1) reads 1 for the shortest game and then 1 + 2 = 3 for the longest, instead of 2. Problem 10 comes straight after Problem 9's games on the same starts, so the same thing can happen there.
- **Smallest fix:** add "Empty Removed before each game." to the shared rules, or tell the adult to do it. The answers are otherwise correct.

## Band verdict

K–1 is the only band in this run. All of its mathematics checks out: winners, winning moves, the partner's moves, the "every way" lists, game lengths and board maximums. Problems 1, 2, 3, 4, 8 (apart from item 6), 10 (apart from items 5 and 6), 11 and 12 (apart from item 5) need no change for correctness. Items 1 to 5 need fixing before printing; item 6 is optional.
