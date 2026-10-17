# Week 79: Numbered-ball detectives

**Verdict: revise.** One must, in the guide: the hint headed "Problems 3–4" states two smallest-card facts that are false under Problem 3's rule, so an adult can steer children against what their cards show. The pages, the mathematics and every printed answer are right; the fix is a relabel and two sentences.

Reviewed October 17, 2026 by Claude (second card run), with math.md and card2_chosen_moves.py. Packet: week-79-students.pdf (79-ST-v1, 5 pp.: pp. 1–2 Grades 2–5, P1–P3; p. 3 Grades 4–5, P4; p. 4 cards 1–24; p. 5 A/B mat). Adult guide: week-79-facilitator.pdf (4 pp.). Companions: none. Status: unpiloted; organizer-approved October 15, 2026 (content review, not piloting). I agree with both math-check findings; I rate item 1 a must, item 2 a should.

## The mathematics

Each day two numbered cards go into A and one moves to B, so both bowls hold n cards after day n (P1). Moving A's smallest card, card k enters on day ⌈k/2⌉ and leaves on day k (P2): every card settles in B, yet A is never empty, since card N + 1 is there on day N. Moving the larger new card keeps the counts but settles the odd cards in A (P3). Counts don't decide where cards settle, and "each card eventually" is not "all cards by one day" (P4): the Ross–Littlewood vase. A mathematician would enjoy it. P3 and P4 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real quantifier distinction and a count that doesn't pass to the limit, reached with cards; the guide states the interpretation and its limits. |
| Problems | adequate | The order carries it: counts, one card, a changed rule, settling. P3 and P4 hold five minutes or more. P2 is read off the bowl (fix 3); Grades 4–5 get one new problem (fix 4). |
| Student pages | strong | Spec header and footer, rules once, a day-1 visual (Before, Add 1 and 2, Move 1 to B), no slop or hints, P4 boards empty. Coulds only. |
| Concreteness | strong | Supplied cards and a mat holding the 13-card peak carry the state; B's count is the day. A three-minute whole-group launch shows one move. Partners enforce the rule; numbers expose a wrong move. |
| Correctness | adequate | Every printed answer checks (math.md). The P3–4 hint is false for P3's rule (fix 1). |
| Adult guide | adequate | Theorem-first overview, launch, timed route, roles, P1–P2 keys, day-0 caveat, sum–limit analysis. Fixes 1 and 2. |
| Age fit, K–1 | no route | By design: "No K–1 edition is forced" (WEEKS-79-84-DRAFT.md). Fix 5. |
| Age fit, grades 2–3 | strong | Comparing numbers to 24; the adult reads P3 aloud; no tallies, since the mat holds the state. |
| Age fit, grades 4–5 | strong | P4 is a quantifier argument without notation, with the organizer at the table; feeder, mover and detective roles fit three children. |

## Keep

- p. 1's three-sentence rule and day-1 visual.
- P2's card 20, which leaves on day 20, past the twelve days the 24 cards allow, so it must be predicted.
- P3's "from the bowl counts alone" and "Find a way to show the difference using the cards"; card 1 alone does it.
- P4's definition of "settled", its finite-day question, and boards titled by rule.
- Guide: the overview, "do not require children to track counts and every label at once", inspecting labels 1–6 then 1–12 in place, the day-0 caveat.

## Fix

1. **must**, guide p. 3: "Problems 3–4: … Any fixed finite list eventually has all its labels in B. At every positive finite day N, label N + 1 is still in A." Problem 3 uses only the changed rule, under which cards 1, 3 and 5 never reach B and label N + 1 is in B on every odd N (math.md item 1). The next paragraph has the right mechanism, but an adult looking up Problem 3's hint reads the opposite of the cards and may tell a child card 1 will leave. Fix: "Problems 3–4:" becomes "Problem 4, smallest-card rule:", and add "Problem 3: after day 1, card 1 is in B under the smallest-card rule and in A under the changed rule, and stays there." The verdict rests on this item; it is a must because the heading names Problem 3, as with the keys on the Week 6, 29 and 31 cards.
2. **should**, guide p. 3, for P4: "Can that arrangement happen on a finite day?" is never answered for the changed rule. Under it, every card present is already in its settling bowl on every day, so "yes, every day looks like that" is right about the cards present; the whole arrangement never occurs only because later cards haven't come (math.md item 2). After "The smaller 2n − 1 never moves." add: "So in Problem 4 the odd labels settle in A and the even labels in B. Every finite day shows this for the cards present, but never for labels above 2N. Accept either answer with its reason, and contrast the smallest-card rule, where cards N + 1 to 2N always sit in the bowl they will leave."
3. **should**, p. 2, P2: "Find a rule for the day any numbered card moves to B." B fills 1, 2, 3, … one a day, so after P1 the answer is read off the bowl. The guide's 10-minute label slot rests on its prompt about when a card "enters and when it leaves A". Print it: "…the day any numbered card goes into A and the day it moves to B", with In and Out blanks. Key: in on days 2, 3, 5 and 10.
4. **should**, Grades 4–5, p. 3: P1–P3 are quick for this table, and P4 is its one new problem (that a quick child runs out is a prediction). Add Problem 5: "Now you choose which card in A moves each day. Which cards can you keep in A forever? Try cards 1 and 3; cards 1 and 2; cards 2, 3 and 4; every odd card." Key: a set can be kept exactly when, for every t, at most t of cards 1 to 2t are in it, since t of them have left by day t; moving the smallest unkept card achieves it. So yes, no, no, yes (card2_chosen_moves.py).
5. **should**, K–1: no route, and the shared launch shows four children an action they won't use. A should, as on the Week 76 and 78 cards, because the scope is recorded. A route needing no reading: the launch, P1 with cards 1–8, counting both bowls aloud, then P3's rule and "Which cards never leave A?" That K–1 manage it is a prediction.
6. **could**, guide p. 2: "Use one mat repeatedly" leaves P3 no reference state; let a table's two pairs run the two rules side by side.
7. **could**, guide p. 1: the band map gives the changed rule to Grades 4–5, but P3 is on the Grades 2–5 page and the first route.
8. **could**, guide p. 3: "A is always equally full" → "A and B are always equally full".
9. **could**, guide p. 3: add the day-12 state P1 invites (A = 13–24, B = 1–12).
10. **could**, header: "Numbered-ball" when children handle cards.
11. **could**, guide: four near-empty pages fit on two.

## Overlaps

Week 80 asks what an endless lamp process says about its endpoint, where nothing settles; here each card does. Week 50's staircases show length failing to pass to the limit, as counts do here. Week 76's endless strip is also a limit taken position by position. With free choice, the bowls reachable after n days number 2, 5, 14, 42 (card2_chosen_moves.py), a Catalan link to Week 12. No merge: only Week 79 separates counts from labels.

## App fit

C, not porting. Proposed row: | 79 | Numbered-ball detectives | Run numbered cards through two bowls, two in and one out; find a card's move day; change the rule; decide where cards settle | Counts tie every day; card k leaves on day k; every card settles in B yet A is never empty; moving the larger new card settles the odds in A | No | C | Not porting: both rules are forced and the limit can't be checked on a board | S |

Under both printed rules every move is forced, so on a screen the child watches cards slide or predicts an outcome (card 20's day, which rule made these bowls), the mode children enjoyed least. "Every card settles" and "A is never empty" are claims about an endless process that no finite board checks, so a tap on "all in B" is a guess the app can only mark. The one variant with a choice is fix 4's, which on a screen becomes "make A hold these cards on day n". It has a tappable certificate for "can't" (a day t with more than t target cards among 1 to 2t), but no decision once a child sees not to move a target card: any other card works (card2_chosen_moves.py), so the solve repeats after a puzzle or two. As with Week 73, the substance belongs with cards on a mat and an adult asking "which day?". Port no problem.

## Classroom evidence

None reported. The organizer read and approved the packet on October 15, 2026; plans/organizer-revisions-2026-10-15/README.md: "Promotion records human content review, not classroom piloting." Card handling, fit and timing are unrehearsed (guide p. 4).
