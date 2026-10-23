# Week 66 card fixes, October 23, 2026

The review card is `plans/review/week-66.md` (verdict keep). This pass made its five shoulds and four coulds. The student pages were converted to problem files first, with no wording change (a separate commit), and edited there afterwards. The packet is now GGT66-S-v2 (five pages, Problems 1–6) and the guide GGT66-FAC-v2 (three pages).

| Card item | Change |
|---|---|
| should 1 | Problem 5 reads "Does every target have at least one next move, L, R or F, that makes it harder to reach from all-off at 0? Use your results to settle this question." The guide's answer cites the Problem 3 target, all of whose next moves were checked in Problem 4. |
| should 2 | New Problem 6 on p. 5, in the card's wording, with a large working street, six small draw-in streets with blanks for the fewest moves to the target and after L, R and F, and three answer lines. Key in the guide's Problem 6 entry and a new "Which targets are dead ends" paragraph in the overview: walker at 0, lamp 0 on and a lamp on each side, with the proof and the smallest examples (7; 9, 9; 10, 10; 11). |
| should 3 | Problem 2 no longer says "These targets have the same lamps on, but the walker ends in different places." |
| should 4 | Guide materials: 13 mm lamps on 19 mm centres, counters 17 mm or smaller or paper squares dark on one side, counters kept on their lamps, the walker above its lamp; a prediction until rehearsed. |
| should 5 | Guide "K–1 tables": an adult-led route on the existing pages (the launch, Problem 1, Problem 2's A and C as picture matching, a cube per move, stacks compared) with a key in plain words. No K–1 pages. Unpiloted. |
| could 6 | "Every target starts with every lamp off and the walker at home, 0." is stated once in the rules; Problems 1–3 no longer repeat it. Problem 4 keeps its bold "all lamps off, walker at 0". |
| could 7 | The working streets (Problems 1, 2, 3's workspace and 6) print a "home" mark at 0 instead of the walker. Problem 3's target street keeps its walker. |
| could 8 | Problem 1 no longer says "Use the large street for your counters." |
| could 9 | The guide's launch shows the goal with a non-task target, lamp −1 on and the walker at 0: LFLRR (5 moves), then LFR (3). |

Also: the first route reserves Problems 4–6, the guide headings no longer end a page, and `guide/check_math.py` checks the new guide claims.

Checks: `review/verify_card_fixes_2026_10_23.py` checks the dead-end rule by BFS to distance 13 and by the distance formula on 26,624 targets, that neighbouring targets always differ by one move, the Problem 5 and 6 keys and non-examples, the K–1 routes and the launch words by replay, the lamp sizes in `template.tex`, and the printed wording, numbering and footers (and the PDFs' page counts when given them).

Nothing was physically rehearsed; the packet remains unpiloted.
