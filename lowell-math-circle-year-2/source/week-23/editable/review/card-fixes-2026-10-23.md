# Week 23: the review card's shoulds and coulds, October 23, 2026

The review card (`plans/review/week-23.md` in the project) had one must, the table kit, fixed earlier the same day, and deferred the rest. These are now made in the problem files (converted first with no wording change), the guide source and the bonus companion. The student packets are F23-K-v3, F23-23-v3 and F23-45-v3; the guide keeps its 13 pages and now says "revised 2026-10-23" in its footer; the bonus is W23-BON-v2. The table kit did not change: no kit page quotes the rules, and K–1 Problem 3's pictured starts use the cards the kit already supplies.

## Made

- **Should 2, K–1 p. 1.** The rule is the card's: "Cards move left to right. At each bar, look at the two cards at its ends: the one with fewer dots goes up. Equal cards stay. The bars stay the same for every start. The machine sorts when the fewest dots finish at the top." Bar ends are no longer called dots.
- **Should 3, grades 2–3 and 4–5 p. 1, and the bonus.** "the smaller value goes to the upper lane and the larger to the lower lane" replaces "Put the smaller value in the lower-numbered lane and the larger in the other", and "A machine sorts when the final values never get smaller from lane 1 down." replaces "... increase from lane 1 downward, allowing ties." The bonus rule now says "sends the smaller value to the upper lane" (its guide too). The guide's common-confusions line now explains "upper lane" instead of "lower-numbered".
- **Should 4, K–1 Problem 3.** Problem 1's six starts are printed under each machine, in Problem 1's order, and the prompt is the card's: "For each machine, circle every start that finishes in the wrong order." The bank of three cards above the machines is gone, as in Problem 1; the two machines are unchanged. The guide's key says which pictures get circled: none under the upper machine, the fourth and sixth (231, 321) under the lower one.
- **Should 5, guide p. 1.** A "Partners keep the rule" note: one child chooses the start; the partner slides the time strip one bar at a time, moves the cards behind it and says "swap" or "stay"; they switch jobs for each start; at the 4–5 table a third child referees. The kit's time strip stands in for the card's ruler.
- **Should 6, guide p. 1.** The rehearsal and the launch run 312 on bars (1,2), (2,3), which sorts, instead of 231, which is the failure the first problems ask for; the adult writes the start and finish beside the lanes, top to bottom.
- **Should 7, guide p. 7.** "1110 finishes 1011" (it said 1101).
- **Should 8, guide p. 7, grades 2–3 Problem 3.** Certifying a repair by tests takes all 24 starts: split them by top card (six each) and pool them across children, or argue that the smallest card reaches lane 1 and the largest lane 4 before the last bar.
- **Should 9, guide p. 8, grades 2–3 Problem 5.** A held question after a complete record: "Does your machine sort every order of 1, 2, 3, 4? Can a machine sort every 0-1 start and still fail one?", answered for adults by the zero-one principle with a pointer to grades 4–5 Problem 4.
- **Could 10, guide p. 2.** The time table starts with about five minutes of running around (0–5 min) and keeps 38 minutes of table work (12–50 min), as `worksheet-workflow/context.md` describes the hour. "For ten children" had already gone with the kit fix, which plans for three tables.
- **Could 11, guide p. 12.** The "Final student authority" paragraph (build residue naming final/ files and workflow prompts) is cut.
- **Could 12, grades 4–5 Problem 7.** "Count each bar, even when two bars could happen at the same time" is cut; the guide keeps "Count bars, not parallel stages."

## Left

Nothing on the card's Fix list is left. The card's Overlaps note (cross-reference Week 6's 2^k count from 4–5 P6–P7) is not a fix item and was not made.

## Verification

- `review/verify_card_fixes_2026_10_23.py [build] [bonus-build]` checks each change in the built PDFs (rules, K–1 Problem 3's prompt, starts and 48 boxes, the Problem 7 cut, every footer, each guide sentence, the bonus rule and footers) and recomputes every changed claim: which pictured starts each K–1 Problem 3 machine fails and where they sit, 312 sorting on (1,2), (2,3), the 1110 trace, six starts per top card, the smallest and largest cards reaching lanes 1 and 4 in both repairable machines, the time table, and the zero-one principle for every four-lane machine of up to six bars. It passes (1,082 checks).
- `src/check_networks.py` and `facilitator-src/checks.py` pass unchanged; no machine changed.
- Changed pages were rendered at 80 dpi and inspected: K–1 pp. 1 and 3, grades 2–3 p. 1, grades 4–5 pp. 1 and 7, guide pp. 1, 2, 4, 7, 8 and 12, bonus p. 1.
- `verify_rebuild.py` passes against the new references, and a clean rebuild from the extracted ZIP passes it and the card-fix verifier.
- The replaced PDFs are in the project's `week-23/archive-before-card-shoulds-2026-10-23/`, and the replaced ZIPs in `source/week-23/archive-before-card-shoulds-2026-10-23/`.

All of this is digital checking. The week, the partner rule and the kit remain unpiloted and physically unrehearsed.
