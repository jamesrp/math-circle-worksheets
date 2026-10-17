# Week 79: Numbered-ball detectives

**Original verdict: revise.** One must at review: the guide's hint headed "Problems 3–4" states two facts that are false under Problem 3's only rule. The pages, cards, mat and mathematics are right and should stay.

**Fix 1 resolved October 17, 2026 (organizer-approved scope).** The guide page 3 hint now names Problem 4's smallest-card rule and gives the card-1 contrast for Problem 3. The original review below is retained; all other proposals are unimplemented and deferred. Student PDF unchanged; organizer promotion and unpiloted status preserved. [Correction checks](../infinity-prototypes-79-84/reviews/week-79/hint-correction-2026-10-17.md).

Reviewed October 17, 2026 by Claude, with the math check in math.md. Packets: week-79-students.pdf (79-ST-v1, 5 pp.: Grades 2–5 P1–P3, Grades 4–5 P4, a 24-card sheet, an A/B mat). Adult guide: week-79-facilitator.pdf (4 pp.). Companions noticed but not reviewed: none printed; the guide's encore is one paragraph. Status: unpiloted; the organizer read and approved it for promotion on October 15, which is review, not piloting. The card agrees with both math-check findings, rating item 1 a must and item 2 a should. A second card run ([card-second-run.md](checks/week-79/card-second-run.md)), written without reading this one, reached the same verdict on the same must and the same app fit.

## The mathematics

Each day two cards enter A and one moves to B, so both bowls hold n after day n under any such rule (P1, P3). Moving A's smallest keeps A = {n+1, …, 2n}, so card k moves on day k (P2): every label settles in B and A settles empty, yet card N+1 is in A on every day N ≥ 1 (P4). Moving the larger new card keeps the counts but settles the odd labels in A (P3, P4). This is the Ross–Littlewood paradox with a control: the limit of the counts is not the count of the limit, and "each label by some day" is not "all labels by one day". A mathematician would enjoy it. Only P4 reaches the infinite part.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A classic paradox with a sharp control, proved by one induction. |
| Problems | adequate | The order carries it: enact, count, follow a card, change the rule, then limits. P1–P3 each settle in minutes (fixes 3–4). |
| Student pages | strong | Spec header and footer, one brief rule, an input–intermediate–output visual, no hints or slop, empty P4 boards. Grades 2–3 get two problem pages (fix 3). |
| Concreteness | adequate | The mat holds the whole state, and guide p. 2's launch demonstrates the move. The child, not the material, enforces "smallest"; P3 has one kit for two states (fix 5); the launch skips K–1. |
| Correctness | adequate | Every printed answer is right (math.md; my replays agree). One guide hint is false for P3 (fix 1). |
| Adult guide | adequate | Theorem-first overview with assumptions and band map; prerequisites, launch, route, induction, P1–P2 keys, adult limit analysis. Gaps: fixes 1–2. |
| Age fit, K–1 | weak | No route, by design ("No K–1 edition", outline). |
| Age fit, grades 2–3 | adequate | An adult reads the rule; numbers to 24; the mat keeps every record. Prediction: a quick pair finishes P1–P3 well inside the guide's 35 minutes. |
| Age fit, grades 4–5 | adequate | P4 is the right deep question, with the organizer at the table, but it alone carries the hour and half of it has no key. |

## Keep

- p. 1: the rule ending "Cards in B stay there." and the Before / Add 1 and 2 / Move 1 to B visual.
- P1's "Can the bowls ever end a day with different numbers of cards?"; P2's card 20, beyond the 24-card kit, so a rule is needed; P3's open "Find a way to show the difference using the cards."
- P4's definition of "settled", its finite-day question, and four empty boards.
- 30 mm cards, 180 × 96 mm regions (room for the 13-card peak), unused cards laid out in pairs.
- Guide: the overview; "Show a legal finite move, not the limiting answer."; "do not require children to track counts and every label at once"; the induction; p. 4's caution on nonuniformity.

## Fix

1. **must — resolved October 17, 2026**, guide p. 3 (original finding): "Problems 3–4: inspect a named finite list of labels … Any fixed finite list eventually has all its labels in B. At every positive finite day N, label N + 1 is still in A." P3 uses only the changed rule, under which labels 1, 3 and 5 never reach B and label N+1 is in B on every odd day (math.md item 1). An adult following the heading would expect cards 1–6 all in B and may have children redo a correct run. Fix: change "Problems 3–4:" to "Problem 4, smallest-card rule:" and add "Problem 3: after day 1, card 1 is in B under the smallest-card rule and in A under the changed rule; the counts are equal every day."
2. **should**, guide p. 3, P4: "Can that arrangement happen on a finite day?" is answered only for the smallest rule. Under the changed rule every card present already sits where it settles, so "it always looks like that" is right about those cards (math.md item 2), the packet's sharpest contrast. Add math.md's sentence after "The smaller 2n − 1 never moves."
3. **should**, Grades 2–3, pp. 1–2: three problems on two pages, against spec's "usually … four or more pages per band"; P1 and P3 rest on the same count, and P3's difference shows on day 1. Prediction: a quick pair is done in 20 minutes. Fix: add "Choose which card to move each day. After six days, can B hold 1, 3, 5, 7, 9, 11? 2, 3, 5, 7, 8, 11? 1, 4, 6, 9, 11, 12?" Only the third fails: by day 4 four cards have moved, all at most 8, and only three target cards are (exhaustive search, card_targets.py).
4. **should**, p. 2, P2: "Find a rule for the day any numbered card moves to B." The answer is the card's number, and B after P1 already reads 1, 2, 3, …. The entry day ⌈k/2⌉, and so the wait in A that grows and drives P4, is only in the guide. Fix: under each card print "Enters day ___" and "Moves day ___".
5. **should**, guide p. 3: "compare the two actual sets." Each pair has one card set and P3 says "Start again", so the first set is memory. Fix: the two pairs run one rule each, side by side (at 4–5, the third child runs the second); add a card sheet per table.
6. **should**, K–1, guide p. 1: no route; a should, as on the Week 76 card, since the selected-band design is deliberate. P1's six days and card 1 under both rules need no reading (a prediction).
7. **could**, guide p. 1: the band map gives "changed-rule comparison" to 4–5, but P3 is on a Grades 2–5 page.
8. **could**, guide p. 3: "A is always equally full" means "A and B always hold the same number".
9. **could**, the header says "Numbered-ball" while the pages say cards; p. 3 switches to "label".
10. **could**, the guide header still reads "Facilitator draft".
11. **could**, guide p. 4: name the Ross–Littlewood paradox.

## Overlaps

Week 50's staircases are the same failed interchange in geometry; Week 81 has the same quantifier swap (every play finite, no common bound); Week 80 asks for the state at a limit time. Only Week 79 sets a set-valued limit against a count. No merge; 79, 80 and 81 make a return sequence.

## App fit

Proposed C, not porting; themes.md has no row. It should read: | 79 | Numbered-ball detectives | Put two cards in A each day and move one to B; follow a card; compare two rules; decide where every label settles | Each bowl holds n after day n; moving A's smallest sends card k on day k, so A settles empty though no finite day shows it; moving the larger new card settles the odds in A with the same counts | No | C | None: the rule makes every move, so a screen only plays days to watch | S |

There is no real on-screen solve. The rule makes every move, so a faithful port has one button, Next day, and each question becomes a prediction: equal counts (P1), the move day (P2), a yes/no on whether counts tell the rules apart (P3). The theorem is about all days at once; card 1,001 in A on day 1,000 restates the paradox without checking anything. P4 is a discussion about infinity and belongs at the table.

The one variant with a solve lets the child choose the moved card: reach a target B on day N, or Can't with a tap on the day d when fewer than d target cards had arrived, a certificate that can fail. By exhaustive search to N = 7 (card_choose_move.py), the reachable targets are exactly those with at least d cards among 1 … 2d for every d, sending the smallest wanted card each day solves all of them, and they number Catalan C(N+1). So the solve repeats after a puzzle or two, as Week 73's did, the counting is Week 12's (Circle strings), and infinity is gone. Recommendation: not porting; the variant goes on paper as fix 3.

**Decision, October 17, 2026.** Not porting. Under both printed rules the rule makes every move, so a screen version could only play the days for children to watch or ask them to predict, the mode the app avoids; and the theorem, that every card settles in B while A is never empty, is a claim about an endless process that no finite board can check. The one version with a real choice (choose which card moves to reach a target B) is solved every time by moving the smallest wanted card, so the solve repeats after a puzzle or two, as Week 73's did, and its counting is Week 12's. The week's experience is the cards on the mat and the conversation about infinity, which the worksheet keeps; the chosen-move variant goes on paper (fix 3). Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The organizer approved the packet on October 15 after reading it; no session has used it. Source README: "All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed."
