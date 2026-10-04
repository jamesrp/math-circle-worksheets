# Revision notes, Week 7 (take-away games)

All edits are in `src/make.py`. I regenerated the three .tex files from it and rebuilt `final/k-1.pdf` (5 pages), `final/grades-2-3.pdf` (5 pages) and `final/grades-4-5.pdf` (6 pages). The page counts and page breaks are the same as in the draft. I checked every affected answer again with code. The diagrams and their counter counts did not change.

## K–1

1. **Fixed: Problem 10 had no move rule.** It now reads: "Now there is one pile again, each player takes 1 or 2 counters, and whoever takes the last counter loses. Put an X on every trap from 1 to 20." Rechecked: the traps are 1, 4, 7, 10, 13, 16, 19.
2. **Fixed: Problem 8 did not say who wins with two piles.** I kept the first sentence as it was and added one short sentence after it: "Whoever takes the last counter on the table wins." Answers are unchanged: 1-1, 2-2, 3-3 and 1-4 are 2nd, and 1-2 and 2-3 are 1st.
3. **Fixed: in Problem 8, "1st" and "2nd" looked like labels for the two piles.** In `two_pile_panel`, the two words are now drawn as one pair, centred under the whole frame and 0.8 cm apart (`choice_gap`). Neither word is centred under a pile any more, and there is still room to circle one of them.
4. **Fixed: Problem 5 said "always starts".** It now reads "Ben goes first and takes 2 counters." The answers are unchanged: Ben wins from 5, 8 and 11.
5. **Fixed: Problem 3 repeated what the picture shows.** I removed "with a bigger pile", so it now begins "It is your turn." The rest of the sentence is unchanged.

## Grades 2–3

6. **Fixed: Problem 8 said "exactly when", which is easy to miss.** It now reads: "… so that you would rather go second when the starting pile is 5, 10, 15, 20, 25, and so on, and you would rather go first for every other pile. Then find a different rule that does the same thing." Rechecked: {1, 2, 3, 4} works, as does {1, 2, 3, 4} plus any moves that are not multiples of 5. {1, 4} no longer passes, because it also makes 2, 7, 12, … second-player piles.
7. **Fixed: Problem 7 did not say who wins with two piles, and its choice words looked like pile labels.** I added "and whoever takes the last counter on the table wins" to the rule sentence. The choice words use the same `two_pile_panel` change as item 3. "First" and "Second" are long enough to fill most of the frame, so with the default gap "First" still sat right under the left pile. For this panel I set the gap to 0.4 cm, so the words read as one centred phrase. Answers are unchanged: 3-3 and 4-1 are second, and 4-2 and 5-3 are first.
8. **Fixed: two passages did no work.** I deleted "Each problem says how many counters a player may take on a turn." from the rules on page 1. Problem 4 now begins "Use the rule from Problem 3." This matches how Problems 2 and 5 refer back to an earlier rule, and Problem 3 is a few lines above on the same page.

## Grades 4–5

9. **Fixed: Problem 6 did not say what happens when a player cannot move.** I added "If a player cannot move, that player loses." before "Explain why your list is complete." It does not say that 1 must be allowed. Rechecked: the complete list is {1, 2, 3}, {1, 2, 3, 5}, {1, 2, 3, 6} and {1, 2, 3, 5, 6}.
10. **Fixed: the rules at the top of page 1 described the packet.** I deleted "Each problem says how many counters a player may take on a turn." "Unless a problem says otherwise, whoever takes the last counter wins." is kept.

No issue was skipped.
