# Revision notes: Week 7 take-away games

All edits were made in `src/make.py`. I regenerated the three `.tex` files from it and rebuilt `final/k-1.pdf` (5 pages), `final/grades-2-3.pdf` (5 pages) and `final/grades-4-5.pdf` (6 pages). There are no overfull or underfull boxes. I rendered every page and checked it. Every changed problem was solved again by brute force (`scratch/solve.py`).

Reports are cited as R1 (adversarial review), R2 (classroom simulation) and R3 (mathematical check). Overlapping reports are listed as one issue.

## Fixed

1. **K–1 P10 does not state the moves** (R1 #1, R2 #5, R3 #2). Now reads: "Now there is one pile again. Each player takes 1 or 2 counters, and whoever takes the last counter loses. Put an X on every trap from 1 to 20." Answer: 1, 4, 7, 10, 13, 16, 19. R1's optional trim of the opening rule was skipped. With this fix, every problem that changes the game now states its new rule in full, and the opening rule is true for P1–P6.

2. **Two-pile choice words sit under each pile and read as pile labels** (R1 #2, R2 #3; K–1 P8, 2–3 P7). In `two_pile_panel`, both words now sit as a close pair centred under the middle of the pair, 0.7 cm apart. They are also set lower, so there is a clear gap between them and the trays. Before, each word was centred under its own tray. Both bands use the same function.

3. **K–1 P6 recording space** (R1 #3, R2 #4, R3 #3). The page now prints exactly 5 rows of 4 counters and 8 rows of 5 counters, which matches the answers (5 and 8 ways). Counter spacing went from 1.15 to 1.45 cm across and from 1.3 to 1.8 cm down, so loops have room. P7 still fits on the same page.
   Two parts were skipped:
   - R1's replacement problem. "Find every way" is K–1 mathematics the standard names explicitly. Listing every way a small game can go is the full set of plays that a strategy has to answer.
   - R2's extra sentence about order. The exact row count already shows that order matters (ignoring order gives only 3 ways for 4 counters). A third sentence would add read-aloud load.

4. **K–1 P2 and P8: "would rather go first or second"** (R2 #2). Kindergartners answer this as a preference. Both now say "Circle 1st or 2nd to show which player can be sure to win" (P2 adds "with each pile"). The answers are unchanged.

5. **K–1 P4: the trap definition is hard to take in on one hearing** (R2 #10, R1 #6 P4 item). Now reads: "A pile is a trap if you cannot be sure to win when it is your turn." R2's "like the pile of 3" was left out, because it reads as a reminder or hint.

6. **K–1 P5: "Ben always starts…" and circling piles** (R2 #6). Now reads: "Ben goes first and takes 2 counters. Put a check by each pile where Ben can still be sure to win." The answer is still 5, 8 and 11.

7. **K–1 P1 and P3: "the counters you take" could mean every counter taken over the whole game** (R2 #7). Added one word, "now". The answers are unchanged.

8. **Two-pile games: "the last counter" could be heard as emptying one pile** (R3 #1). Changes:
   - K–1 P8: added "Whoever takes the last counter on the table wins."
   - 2–3 P7: added the same sentence.
   - 4–5 P8: "the last counter" became "the last counter on the table".
   K–1 P9 and 4–5 P9 refer back to P8, so they are covered. The answers are unchanged under the intended reading.

9. **2–3 P7: only one equal pair before the generalization** (R1 #8, R2 #8). Replaced (5,3) with (4,4) and kept (4,1), as R1 asked. The page now has two equal pairs, and one of them, (4,4), is made of single piles that are each winning, so the "both piles are traps" reason fails on it. Answers: (3,3) Second, (4,2) First, (4,1) Second, (4,4) Second. Checked by direct minimax, and the diagram matches.

10. **2–3 P3 calls the opponent "partner"** (R1 #9). All three uses became "the other player".

11. **Grades 2–3 run out of work for a quick child** (R2 #1). Added Problem 9 on page 5, below P8, with a 20-box chart: "Now whoever takes the last counter loses. On each turn a player takes 1, 3, or 4 counters. Shade the box of every starting pile from 1 to 20 where you would rather go second." Answer: 1, 3, 8, 10, 15, 17. It contrasts with P4: same moves, opposite win rule. The opening sentence "Whoever takes the last counter wins" became "Unless a problem says otherwise, whoever takes the last counter wins", so the packet rule stays true. This matches the 4–5 wording.

12. **No rule for a player who cannot move** (R2 #12; 2–3 P8 and 4–5 P6). Added "If you cannot take any counters on your turn, you lose." to the packet rules on page 1 of grades 2–3 and grades 4–5. K–1 rules always include taking 1, so K–1 does not need it. Rechecked under this rule:
    - 4–5 P6 has exactly {1,2,3}, {1,2,3,5}, {1,2,3,6} and {1,2,3,5,6}.
    - 2–3 P8 has {1,2,3,4}, plus rules such as {1,2,3,4,6}.

13. **4–5 P8: the row 0 / column 0 square has no game** (R3 #4; R1 #11, last bullet). The no-move rule from item 12 settles it: the player to move cannot take a counter and loses, so the square is shaded. This matches the a ≡ b (mod 3) pattern, which I verified including (0,0). R1 valued the square as a base case, so I did not grey it out.

14. **4–5 P6: "allowed moves come from the numbers 1–6" read as the single game {1,…,6}** (R2 #9). Now reads "whose allowed moves are some of the numbers 1, 2, 3, 4, 5, and 6, and whose losing piles…". The answer is unchanged (item 12).

15. **4–5 P4: Dana's plan is unclear when the pile is smaller than the largest move** (R2 #13). Now reads: "Dana's plan is to always take the biggest number of counters she is allowed to take from the pile." The answers are unchanged: greedy fails at 4 in {1,2}, at 5 in {1,3,4} and at 8 in {1,4}, and always wins in {1,3,5}.

16. **"prob-lem" hyphenated across a line** (R1 #11, first bullet). Added `\hyphenpenalty=10000 \exhyphenpenalty=10000` to the preamble. No page now has a hyphenated line break, and there are no new overfull boxes.

17. **4–5 P4: the table header wraps** (R1 #11, second bullet). Widened the middle column from 5.0 to 5.6 cm. "Does the plan always win?" now fits on one line.

## Skipped

- **K–1 numeral strips 1–20 have no pictures** (R1 #4). Children build each pile from counters on the table, and the adult reads the numerals. Dot pictures inside 1.65 cm boxes would be too small to count, and the X would cover them. The simulation found the strips easy to mark. Each strip's rule is stated in its own problem.
- **K–1 P1–P4 repeat one question; P3 and P4 overlap** (R1 #5, R2 #14). The move from pictured piles to the 1–20 strip is the K–1 version of kernel 2, and seeing 3, 6, 9, … repeat across the whole strip is the point. Merging or cutting problems would reorganize the packet. R1 also calls the build-up defensible.
- **K–1 read-aloud load, other items** (R1 #6). The P4 item was fixed (item 5). The rest were skipped:
  - P1 and P3 are already two sentences, and splitting the second would make three.
  - P6 gains no words in this revision.
  - In P9, the adult reads "Problem 8", and it is directly above on the same page.
- **K–1 P9 has nothing to record** (R1 #7). The question says what to produce: a way for the second player to win every time. K–1 children answer by playing on the pictured trays with counters, with the adult beside them. They cannot write a strategy, so blank space would not be used. The organizer's examples also use plain questions.
- **2–3 P8: the leap to a second rule** (R1 #10). R1 marks this as a note, not a fix. It is a fair stretch as a late problem, and it remains solvable.
- **2–3 P2 uses piles already settled by P1** (R2 #11). Using P1's results to test a claimed strategy is the intended order: the idea is used before it is explained. Explaining why Lee's reply always works, and showing how to beat Mo, is the same work at 12 and 10 as at 21 and 20. The new P9 covers the quick child's need for more work.
- **4–5 strips: shading covers the centred numerals** (R1 #11, third bullet). A printed numeral stays readable under pencil shading, and the simulation found the strips shade fine. A corner numeral in a 0.78 cm box would be cramped.
- **K–1 counter pitch in P1, P3 and P5** (R1 #11, fourth bullet). Three trays already span the full text width. A larger pitch would mean dropping the five-per-row layout that helps counting, or would gain only about 1 mm.
- **K–1 page 5 is mostly empty** (R1 #11, fifth bullet). R1 calls this harmless. K–1 is still 5 pages, with four full pages before it.
- **Optional extra problem on pigeonhole periodicity for grades 4–5** (R1, optional). The 4–5 packet already holds more than the hour: in the simulation, P8 and P9 were unused reserve.
