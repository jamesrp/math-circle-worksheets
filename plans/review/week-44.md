# Week 44: The bag that copies

**Verdict: keep.** Every answer checks, the 4–5 sequence reaches the uniform law with a finite proof, and no must survives: K–1 Problem 1's wording, which decided the second review's revise, is a should (fix 1).

Reviewed October 5, 2026 by Claude in two independent reviews, reconciled, with the math check in [week-44-math.md](week-44-math.md). Packets: week-44-k-1.pdf (W44-k-1-v2, 4 pp., P1–4), week-44-grades-2-3.pdf (W44-grades-2-3-v2, 4 pp., P1–6), week-44-grades-4-5.pdf (W44-grades-4-5-v2, 4 pp., P1–6). Adult guide: week-44-facilitator.pdf (6 pp.). Companions noticed but not reviewed: week-44-bonus.pdf (W44-BONUS-v1, 3 pp.) and its guide (W44-BONUS-FAC-v1, 3 pp.). Status: unpiloted (October 4 revision).

## The mathematics

Each draw goes back with a copy of its colour, starting from one red and one blue (Pólya's urn). After n draws neither colour has vanished, and the number of red draws is uniform on 0 to n. A word's chance depends only on its colour counts, though draws are dependent. Labelling each copy by the step that added it makes all (n+1)! marked histories equally likely, so the proof is a count: two per total at two draws, six at three. A mathematician would enjoy it: the lopsided bag is exactly as likely as the balanced one. 4–5 P1–P6 and 2–3 P1–P4 carry the theorem; K–1 carries reachable bags and the never-vanish invariant.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Uniform law, exchangeability without independence, a contrast rule, each with a finite proof. |
| Problems | adequate | 4–5 builds from two draws to every length; K–1 has an impossible bag (P2) and a backward step (P4); 2–3 ends thin (fix 5). |
| Student pages | adequate | Format right, no slop, worked visuals before first use. Faults in fixes 1–3, 7–8. |
| Concreteness | adequate | Counters, cups and labels; guide p. 2's launch enacts RB → RRB and a second draw. Nobody draws at random (fix 6). |
| Correctness | strong | Every key and student claim checks (math check; appfit_check.py). Fixes 1–2, 9. |
| Adult guide | strong | Theorem-first overview with assumptions, limits and a band map; full keys, hints, launch, routes. Fixes 1, 4, 14. |
| Age fit, K–1 | adequate | Short prompts read aloud; counting to six. Fixes 3, 7. |
| Age fit, grades 2–3 | adequate | Chance by counting marked stories stretches third graders; the table's mathematician can carry it (prediction). |
| Age fit, grades 4–5 | strong | One new idea per problem, each checkable by building histories; P6 is open. |

## Keep

- Every band's p. 1 launch figure, guide p. 2's launch, and the marks rule with its R1 → R1 B1 R2 visual.
- K–1: P2's impossible 5R/0B; P3's six orders of RRBB; P4's backward boards.
- 2–3: P1 then P2, where only the middle bag has two colour stories yet all three tie at two marked stories; P3; P4.
- 4–5: P1–P6 in order. Guide: the overview, the K–1 P4 and 4–5 P5 tables, the hints, the p. 6 routes.

## Fix

1. **should**, K–1 p. 1, P1: "Which bags can come from two different draw stories?" Key p. 3: "Only the middle bag has two different two-draw color stories." The launch shows "both red identities can be selected" (guide p. 2) and kits carry R1, B1, R2 labels; counted by identity, every bag has two stories, and the key does not accept that. The second review rated this a must; it is a should, because no K–1 page mentions marks, P3's six rows fit only colour stories and the key says "color stories", so a parent can redirect without saying anything false (unlike week-25.md's false hint); a K–1 child taking the identity reading is a prediction. Fix: print "two different color stories"; the key accepts the identity count and then asks about colour orders.
2. **should**, K–1 p. 2, P2: "Which bags can you make after three draws?" 3R/2B is possible and not printed; the key answers "For the printed choices". Fix: "Which of these bags…"; keep 3R/2B as a follow-up.
3. **should**, K–1 p. 3, P3: six rows for six stories show when the list is complete, and "Can you also make every four-draw bag with more blue than red?" has no space. The second review rated the row count a could; it is a should, as in week-53.md, because finding every story is the task. Fix: eight rows, and two bag boxes with rows in the empty bottom of the page.
4. **should**, guide p. 2: "For ten children … per pair, five red plus five blue counters". The group is eleven, and K–1 P1's three bags side by side, or a five-draw one-colour story (4–5 P6), need six of a colour. Fix: eleven children, six of each per pair.
5. **should**, 2–3 p. 4: P5 asks for "two different color stories for each final bag below", a minute's work, and P6 ("A friend says one color must eventually vanish…") repeats K–1 P4. Fix: P5 asks for every colour story, with room for 1, 4 and 6; P6 asks "After four copying draws, which bag is more likely: five red and one blue, or three red and three blue?" Both are 1/5: RRRR has 24 of 120 marked histories, each of the six 3R/3B words 4.
6. **should**, 2–3 P3–P4 and 4–5 P1–P5 ask about chance, but no task or route draws at random. Fix in the guide's first route: pairs play about ten random two-draw games, copying then return only, and pool results on a chart before P2, as a conjecture. The first review rated this a could; it is a should, because chance is the older bands' central word and AGENTS.md asks for concrete action before abstraction.
7. **should**, neg.md: cut 4–5 P6's "an exact argument for every length is a further question", K–1 p. 1's unused "For random play, each counter has the same chance", and 2–3 P2's repeat of it, "Each counter in the bag has the same chance of being drawn."
8. **should**, 2–3 p. 3, P4: three ruled lines, no room to compare chances. Fix: an unlabelled box like P3's (the second review's labelled boxes would print the answer).
9. **should**, companion, bonus guide p. 3: "123=6" and "34...*(n+2)", asterisks lost to italics. Fix: × in guide.md.
10. **could**, K–1: after P1, sort the six labelled two-draw ways onto the three bags. The second review rated it a should; it is a could, because K–1 already has four substantial problems and the guide says "Do not insist that K-1 compute probabilities".
11. **could**, 2–3 P1: four rows for four stories; add a spare.
12. **could**, 4–5: "marked stories" (P1) against "marked histories" (P4); use one, and write "1 red draw" on P4.
13. **could**, 4–5 P1: "has the greatest chance" presumes one winner; add "if any".
14. **could**, guide p. 2: a 0–60 minute plan, though the hour has 35–40 minutes at tables. The second review rated it a should; it is a could, as in week-63.md, because p. 6 says "The timing menus are examples".
15. **could**, the bonus marks originals R0/B0, the base R1/B1; use one.
16. **could**, write one story in cells during the launch.

The math check's four items are fixes 9, 1, 2 and 4, each a should.

## Overlaps

Weeks 42, 43 and 45 also label look-alikes to get equally likely cases, and 42's unchanged bag is this week's return-only contrast. None has a reinforcing bag or the uniform law. No merge.

## App fit

B, confirmed; size M. Tap a numbered counter to draw it; the app returns it and adds the next labelled copy, so the rule enforces itself. Solve, on the case engine's shelf and bins: keep every history, binned by red draws, then "That's all" with no visible count; the binned catalog is the certificate. Cases: six histories, two per bin (4–5 P1); colour stories and return only, both 1, 2, 1 (2–3 P1, 4–5 P2); RRB, RBR, BRR two each (4–5 P3); 24 histories, six per bin (P4). K–1: reach a bag, every story to 3R/3B, bags one draw back (P2–P4). 5R/0B's impossibility (B1 never leaves) is a grown-up prompt. Hard: the bonus's add-the-other-colour rule (1, 4, 1) and three-colour bag (six bins of two). The Week 44 row of docs/cases.md asks for "Weighted cases: histories are not equally likely, so groups compare total weight, not counts". That holds for colour words only; marked histories are equally likely, so `evenGroups` works unweighted, and weights would give the answer away. Pitfalls: more than 24 histories; 4–5 P5–P6, which stay on paper; random-simulation solves; predict-the-bin questions.

## Classroom evidence

None reported; the theme is unpiloted. The source README: "The theme remains unpiloted and can span several meetings." Guide p. 2: "Prepared, unpiloted material."
