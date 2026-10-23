# Week 23: the K–1 sorting rule, October 23, 2026 (Critic L)

An independent review of the day's revisions found one must in K–1 p. 1. The card's rule ended "The machine sorts when the fewest dots finish at the top." Read as printed, that asks only for the smallest card on top, and three K–1 problems then have other answers than the guide's keys: Problem 2 needs only 2 bars (for example (2,3), (1,2)), Problem 6 only 3 ((1,2), (1,3), (1,4)), and the second half of Problem 4 has no machine at all, because any machine that always brings the one blank to the top also does so for two blanks (the guide's R = (2,3), (1,2) "fails" 100 only by finishing 010, blank on top). The packet's earlier wording asked for the whole order and was right.

## Made

- **K–1 p. 1.** The rule's last sentence is now "The machine sorts when the cards finish in order: fewest dots at the top, most dots at the bottom." The packet is F23-K-v4 (`version` in the K–1 band of `week.toml`); grades 2–3 and 4–5 stay at v3 and did not change.
- **Guide.** p. 1 names the F23-K-v4 packet, and the numbered pages' footer reads "revised 2026-10-23 for F23-K-v4", so a printed page shows which K–1 packet it goes with. The overview's comparator now puts the minimum "in the upper lane (the lane 1 side)", the students' word, instead of "the lower-numbered lane" (the review's could 3). No key changed: they were right for the whole-order rule.
- **K–1 Problem 5 key line.** The problem file's kernel, printed in the key view, said the three machines' last bars are "(1,2), (2,3) and (1,3) respectively"; the bottom machine (1,3), (1,2) needs (2,3), as the guide already says. Fixed in `problems/05-k1-one-more-bar.md`.
- `review/verify_card_fixes_2026_10_23.py` now accepts the new rule sentence, the K–1 v4 footer and the guide's new packet line as well as the old ones.

## Left

The review's could 2 (the guide's launch runs 312 on (1,2), (2,3), which every band's Problem 1 machine also uses) changes the launch the card chose and is left. Could 4 (each return-route view opens with a rules-only page) is the tools' behaviour, not this week's.

## Verification

- `review/verify_sorts_rule_2026_10_23.py [build] [views]` recomputes every K–1 key by exhaustive search under both readings (all three-lane machines up to four bars, all four-lane machines up to five) and checks the printed rule, the footers of all three bands, the guide's packet line, footer and overview, and the Problem 5 kernel (in the key view too, given the views folder). It passes (24 checks); `verify_card_fixes_2026_10_23.py` still passes (1,079 checks without the bonus).
- K–1 p. 1 and guide pp. 1–2 were rendered at 80 dpi and inspected: the four-line rule clears Problem 1. Against the previous PDFs, K–1 differs only in the rule and the footers, the guide only in its overview sentence, p. 1's packet line and the footers; grades 2–3, grades 4–5 and the kit are pixel-identical.
- `verify_rebuild.py` passes against the new references, and a clean rebuild from the extracted ZIP passes it and both verifiers.
- The replaced K–1 packet and guide are in the project's `week-23/archive-before-sorts-rule-fix-2026-10-23/`, and the replaced ZIP in `source/week-23/archive-before-sorts-rule-fix-2026-10-23/`.

All of this is digital checking. The week remains unpiloted and the kit physically unrehearsed.
