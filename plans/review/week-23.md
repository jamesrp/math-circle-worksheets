# Week 23: Sorting networks and fixed machines

**Verdict: revise.** The mathematics, problems and order are right in every band, and every student answer checks. The one must is materials: the guide runs the week on a full-size mat with removable bars and 3 cm cards, forbids the printed diagrams as card holders, and nothing in the week supplies them.

Reviewed October 5, 2026 by Claude, with the math check in [week-23-math.md](week-23-math.md). Two card runs agreed on every fix but split keep/revise over the kit; CARD.md counts a missing board as a must, so revise. Packets: week-23-k-1.pdf (F23-K-v2, 6 pp.), week-23-grades-2-3.pdf (F23-23-v2, 6 pp.), week-23-grades-4-5.pdf (F23-45-v2, 7 pp.). Adult guide: week-23-facilitator.pdf (an unnumbered overview, then pp. 1–12). Companions noticed but not reviewed: week-23-bonus.pdf and its guide. Status: unpiloted; the mat, cards and launch are unrehearsed.

## The mathematics

A bar puts the smaller of two lanes' values above the larger; a machine is a fixed list of bars. One failing start disproves a sorter. A machine sorts every input exactly when it sorts every 0–1 input, because thresholding commutes with each bar (4–5 P3–P5). k bars make at most 2^k swap/stay records and one record sorts at most one order, so three lanes need 3 bars and four need 5 (4–5 P6–P7). With neighbouring lanes only, the six reversed pairs of 4321 force 6 bars (2–3 P6). A mathematician would enjoy this. K–1 and 2–3 reach counterexamples, fewest bars and an impossible repair (K–1 P1–P5, 2–3 P1–P3 and P6).

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | The zero–one principle with a child-sized proof; exact minima from two different lower-bound arguments. |
| Problems | strong | Each is many runs or a build. Contrasts: the same bars reordered (K–1 P3, 4–5 P5); repairable against unrepairable (2–3 P3); two 0–1 card sets (K–1 P4); repeated values (4–5 P1). |
| Student pages | adequate | Short prompts, no hints, worked examples before first use (4–5 pp. 3, 6). Misleading rule wording (fixes 2, 3); K–1 P3 has nowhere to mark (fix 4). |
| Concreteness | adequate | Cards, bars, a ruler as time cursor; the launch handles materials first. The kit is not supplied (fix 1), and only adults enforce the rule (fix 5). |
| Correctness | strong | No student error (math check; both card runs' own simulations agree). One wrong guide trace (fix 7). |
| Adult guide | strong | A theorem-first overview with hypotheses and a band map, full keys, held hints, routes per band, sources with pages. Prep counts only printing (fix 1). |
| Age fit, K–1 | adequate | Dot cards up to four, circling, no writing or arithmetic. The rules are long when heard once (fix 2). P4 and P6 are for the quickest. |
| Age fit, grades 2–3 | adequate | Little reading, no arithmetic; explanation only where it is the point (P2, P3, P6). Prediction: P3's certification load needs steering (fix 8). |
| Age fit, grades 4–5 | strong | Variables, negative t and contradiction come late, after concrete P1–P2, with two proof routes and the organizer present. |

## Keep

- K–1: P1's six pictured starts to circle; P3's reordered bars; P4's two card sets (blank and one-dot, each with two-bar answers); P5's three repairs, each with one working last bar.
- 2–3: P2's "explain why fewer bars cannot work"; P3's bottom machine, where 2413 finishes 2143 and no last bar fixes it; P4's machine, which sorts all six 0011 orders but fails 0010, 0100, 1000 and 1110; P6 with the 4321 argument.
- 4–5: P1's repeats (1, 1, 3 and 1, 3, 3); the threshold route P3–P5 with the t = 4 example, rows −2 8 5 8, 6 2 9 4 and 4 4 4 4, and the 9-above-4 black box; the record route P6–P7 with the SN example, 6 > 4 and 24 > 16.
- Guide: the launch, spare bars "so equipment does not announce the optimum", the band routes.

## Fix

1. **must**, all bands, guide p. 1: "a reusable four-lane mat at least 24 x 30 cm, eight removable comparator strips plus spares… sixteen cards at least 3 x 3 cm… Do not use the small printed input boxes as card holders: they are recording diagrams." The printed boxes are about 0.9 cm, and nothing in the week prints a mat, cards or bars; "Before children arrive, 10-15 minutes" covers printing and laying out a mat that does not exist. A parent volunteer would have to design the kit. Fix: a print-and-cut materials PDF, as Weeks 56, 58, 59 and 63 have: a four-lane mat on two taped Letter sheets (numbered lanes about 4.5 cm apart, 3.5 cm start and finish boxes); 3.5 cm cards (dots 1–4, two blanks and two one-dots for K–1 P4, numerals 1–4 with spare duplicates, four 0s, four 1s); bars with end dots spanning one, two and three lanes. Restate the prep time to include cutting.
2. **should**, K–1 p. 1: "A bar compares the two lanes with black dots: fewer dots go above, more dots below." Bar ends and card values are both "dots", heard once. Use: "Cards move left to right. At each bar, look at the two cards at its ends: the one with fewer dots goes up. Equal cards stay. The bars stay the same for every start. The machine sorts when the fewest dots finish at the top."
3. **should**, 2–3 and 4–5 p. 1: "Put the smaller value in the lower-numbered lane and the larger in the other." "Lower" reads as lower on the page; the guide lists this confusion itself (p. 2). Write "the smaller value goes to the upper lane", and "A machine sorts when the final values never get smaller from lane 1 down." The bonus repeats it.
4. **should**, K–1 p. 3, P3: "Find every start that makes either machine finish in the wrong order." Unlike P1, there are no start pictures, so a non-writer must draw dot stacks. Fix: print P1's six starts under each machine and write "For each machine, circle every start that finishes in the wrong order."
5. **should**, guide p. 1, ground rules: "never reorder by hand elsewhere" names the likely failure, but no one checks it (prediction; context.md asks for rules enforced by the materials or the other player, and says the paper lamp session failed this way). Add: one child chooses the start; the partner moves the cards one bar at a time behind the ruler and says "swap" or "stay"; they switch each start. At 4–5 a third child referees.
6. **should**, guide p. 1, launch: "rehearse input 231 on bars (1,2), (2,3)", then "Run one two-bar example". That run shows exactly the failure K–1 P1, 2–3 P1 and 4–5 P1 ask children to find. Rehearse and run 312, which sorts. While running it, write the start and finish beside lanes 1–3 (top to bottom), since 2–3 and 4–5 list starts and nobody shows how.
7. **should**, guide p. 7, 2–3 P4: "1110 finishes 1101". It finishes 1011; only the last bar swaps (math check, item 1). The failing starts are right, so not a must, but an adult checking a child's correct trace will see a mismatch. Fix the string.
8. **should**, guide p. 7, 2–3 P3: each of the two repairable machines needs 24 starts to certify (prediction: too much tracking). Add: split the starts by top card and pool them across children, or argue that the smallest card reaches lane 1 and the largest lane 4.
9. **should**, guide p. 8, 2–3 P5: the band never learns why a 0–1 sorter matters. Add a held question: "Does your machine sort every order of 1, 2, 3, 4? Can a machine sort every 0–1 start and still fail one?"
10. **could**, guide pp. 1–2: "For ten children" and "0-8 min" ignore the eleven children in context.md and the five-minute run of a full machine.
11. **could**, guide p. 12: cut the build residue ("Final student authority: final/k-1.pdf … The local PROMPT.md, review.md and review-math.md were consulted").
12. **could**, 4–5 P7: cut "Count each bar, even when two bars could happen at the same time"; the guide says it.

I agree with the math check, which did not cover materials, wording or the launch.

## Overlaps

Week 3's fixed machine is a permutation, with a theorem about cycles. Week 6 uses the same count (k yes/no answers separate at most 2^k cases) as 4–5 P6–P7; the guides could cross-reference. Week 43 counts orders of cards with repeated pictures, as 2–3 P4 counts the orders of 0011. In the app, Cup Swaps chooses adjacent swaps after looking; 2–3 P6 gets the same inversion bound for a machine fixed in advance. None has comparator networks or the zero–one principle, so no merge. The bonus stays a companion.

## App fit

B, size M, confirmed; a port is claimed. Cards ride through the bars and swap themselves, so the screen enforces the rule that fix 5 asks a partner to enforce. The child taps two lane ends to place a bar. Solves:
- break a machine by arranging cards into a failing start (K–1 P1, P3; 4–5 P1);
- build within a budget (3 bars on three lanes, 5 on four, 6 neighbour-only), checked on every start;
- repair with one bar, or find a start that no last bar can fix (2–3 P3's 2413);
- break a machine with 0s and 1s, then with numbers (4–5 P4–P5).

Certificates: a failing start for "doesn't sort"; every start, shown after a passing test, for "sorts"; a finish with two separate reversed pairs for "no one bar repairs it". The 2^k argument stays in grown-up notes.

Pitfalls:
- Testing everything invites wiggling bars until it passes; three lanes have few short machines. Show one counterexample per failed test.
- No answer slots or "2 of 6" counters in find-every puzzles.
- No predict-the-output quizzes.
- Mark long-bar end dots clearly; don't duplicate Cup Swaps.

Draw on K–1 P1 and P3–P5; 2–3 P2–P4 and P6; 4–5 P1, P2, P5 and P7.

## Classroom evidence

None reported. The source README and the guide mark the week unpiloted; the fresh review it mentions (October 4) is a review, not classroom evidence.
