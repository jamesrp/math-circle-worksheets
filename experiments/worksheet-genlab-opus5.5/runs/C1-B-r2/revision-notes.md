# Revision notes: Week 7 take-away games

Reports: R1 = adversarial review, R2 = simulated session, R3 = mathematical check. Overlapping reports are merged into one issue. Final PDFs: K–1 5 pp., grades 2–3 5 pp., grades 4–5 5 pp. I rebuilt them from `src/` with no warnings, rendered every page and checked each one.

## K–1

1. **P8: the two-pile winning rule is not stated** (R1 #5, R2 #4, R3 #1). **Fixed.** I added "Whoever takes the very last counter wins." after the first sentence. I did not add R2's "Take from just one pile", because the problem already says "from one of the two piles". Answers are unchanged: 2|2 second, 1|2 first, 3|3 second, 1|4 second.
2. **P9/P10: the ring rows are cramped** (R1 #4, R2 #5). **Fixed.**
   - Counter spacing went from 1.35 to 1.6 cm, so the gap between counters grew from 0.79 to 1.04 cm.
   - Row spacing went from 1.55 to 2.0 cm, so the gap between rows grew from about 1.0 to 1.44 cm.
   - I resized the boxes to fit. Both still fit side by side on page 5.
3. **P9/P10: the number of rows suggests more ways than exist** (R3 #2; also R1 #4 and R2 #5). **Fixed in part.** The rows went from 7 to 6 and from 10 to 9, which leaves one spare row each for 5 and 8 ways. Keeping one spare row means the page does not give away the count, which R3 also wanted. I skipped R3's added sentence ("Some rows may stay empty"), because it would lengthen a K–1 problem.
4. **P9: does order count?** (R2 #5). **Skipped.** The rings run left to right along the row, so 2-1-1 and 1-1-2 are different pictures and different games. The proposed sentence would give away two of the five answers and add a third, long sentence to a K–1 problem.
5. **P9 wording** (R1 #4). **Skipped.** R1 raised four points:
   - *P9 is too long for one hearing.* It is two sentences, and R1's shorter version drops the "1 or 2" rule.
   - *Pre-ring one row as an example.* That row would be a worked answer.
   - *P10 does not repeat the ring instruction.* P10 sits beside P9 with the same rows and opens with "Now".
   - *Optionally add a star for the games the first player wins.* This is new content that no defect requires.
6. **P3, P5, P6: "Color" when the children have only pencils** (R1 nit, R2 #2). **Fixed.** "Color every pile" became "Circle every pile", which matches P1, P4, P7, P8 and the materials.
7. **The rule is given only in words; draw counter groups beside each rule** (R2 #1). **Skipped.** Each problem's first sentence states the rule and the adult restates it. Adding pictures of the rule to every K–1 problem would be a new visual convention (a restyle), not a targeted fix.
8. **P4: who plays Ben, and what "when he can" means** (R1 #10, R2 #3). **Skipped.**
   - The two reports disagree on who should play Ben (the partner or the adult). The adult at the table assigns roles.
   - Every turn must take 1 or 2, so with 1 left Ben takes 1. That is the reading the simulated parent reached. The answers (3, 4, 6, 7) rest on it.
9. **P1 overlaps P3 and is short** (R1 #10). **Skipped.** R1 itself calls it acceptable, and the simulation timed it at 6 to 8 minutes. It is the concrete opening that P3 extends.
10. **Header says "K–1", not "Grades K–1"** (R1 nit). **Skipped.** The brief itself names the band "K–1", and R1 leaves it to the organizer.
11. **Pages 1, 2 and 4 are partly blank** (R1 nit). **Skipped.** This is harmless. Page 5's extra spacing came from page 5 itself.

## Grades 2–3

12. **P6: checking piles 1 to 15 cannot settle Jon's claim; the cells do not say what to write; there is no answer space** (R1 #2, R2 #7). **Fixed.**
   - The text now reads: "Check every starting pile from 1 to 15 counters, and put an X under each pile where you would rather go second. Explain how you know."
   - An X fits the 0.98 cm cells.
   - I added a 2.8 cm writing box under the table. To keep the page count, the P7 box went from 6.2 to 4.6 cm.
   - Answer: Jon is wrong. Both rows are marked at 3, 6, 9, 12 and 15. If the partner takes 4, you take 2, which leaves a multiple of 3 again.
13. **P2/P5: "wins every time" is only circled, so no one has to check every reply** (R1 #3, R2 #6). **Fixed with R1's single sentence in P5:** "For a plan that wins every time, explain why it wins whatever the partner does." I skipped R2's added fourth plan (Max), because the sentence covers the same point with a much smaller change.
   - Zoe's plan works against every reply:
     - From 9: the partner takes 1, 3 or 4, and Zoe leaves 7, 2 or 2.
     - From 7: the partner takes 1, 3 or 4, and Zoe leaves 2, takes all 4, or leaves 2.
     - From 2: the partner must take 1, and Zoe takes the last one.
14. **The intro talks about the packet: "each problem says how many counters a turn may take"** (R1 #11). **Fixed.** I deleted the clause, here and in 4–5 (item 26).
15. **"I start with 8 counters" could be heard as Mia owning 8 counters** (R1 nit). **Skipped.** R1 calls it minor, the plan is about the game's pile, and an adult is present.
16. **P5 does not repeat P2's recording format** (R1 nit). **No change.** R1 itself says P2 already set the format.
17. **Sam's plan always loses, and `check.py` modeled a different plan** (R1, "Verification gap"; R3's table). **Fixed in `src/check.py` only.** Sam is now modeled as printed. He loses all 8 lines of play. The page's correct answer is still "can lose". I also added checks for every problem I changed.

## Grades 4–5

18. **P8: "number" is overloaded** (R1 #1, R2 #11). **Fixed.** The text now uses "a label", "gets label 0", "the label of a pile you can move to" and "Find the labels". The values are unchanged: 0,1,0,1,2,3,2 repeating. 11 and 13 are a losing pair; 12 and 18 are a winning pair.
19. **P8: the idea arrives before it has been used; swap P8 and P9** (R1 #1). **Skipped.** P6, P7 and P8 form a chain (two-pile grids, then the labels that explain them), and P9 is an equally hard last stretch. The new P7 question (item 24) brings out the unequal losing pairs before P8, which is the motivation R1 suggested.
20. **P3: you cannot circle a number inside a 6 mm cell** (R1 #6, R2 #8). **Fixed.** "Circle the losing piles" became "shade the losing piles". This was one word, and the layout is unchanged.
21. **P4: "always" is asked with no reason** (R1 #7). **Fixed.** I added "Explain why for one of them." Answer: under {1,3} and {1,3,5} the losing piles are the even piles, and Kai's largest take is odd, so from an odd pile he leaves an even one. I checked this up to 200.
22. **P4: "winning pile" is used twice in one breath** (R1 #7; noted in R2's walkthrough). **Skipped.** Both uses match the definition in P2 exactly, and R1's suggested "mistake" is vaguer.
23. **P5: the first two lists can be read straight off P3** (R1 #8, R2 #9). **Fixed.**
   - "4, 8, 12, …" became "5, 10, 15, 20, 25, 30, …", which is rule {1,2,3,4}.
   - "2, 5, 7, 10, 12, 15, …" became "2, 8, 10, 16, 18, 24, …", which is rule {1,4,5}: remainder 0 or 2 when divided by 8.
   - Both lists are checked up to 60, and neither is a P3 row.
   - The {1,2,6} case and the impossible case are unchanged.
24. **P7: a grid with no question** (R1 #9, R2 #10). **Fixed.** I added "Which pairs are losing pairs?" and a writing box to the right of the grid, matching P6. Answer: all the equal pairs, plus (0,2), (0,7), (1,3), (1,8), (2,7), (3,8) and (4,6).
25. **P5: delete "A rule is a list of how many counters a turn may take"** (R1 #8). **Skipped.** The sentence tells the child what form the answer takes, and it comes after the child has used rules, which the standard allows.
26. **The intro talks about the packet** (R1 #11). **Fixed.** This is the same deletion as item 14.
27. **P9: "where the pattern starts to repeat" has two reasonable answers** (R1 nit). **No change.** R1 says both answers are fine.
