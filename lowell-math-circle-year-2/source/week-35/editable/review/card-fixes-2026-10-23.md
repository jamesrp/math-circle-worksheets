# Week 35: the review card's shoulds and coulds, October 23, 2026

The review card (`plans/review/week-35.md` in the project) had one must, the footprint kit, fixed earlier the same day with the anchor part of should 5, and deferred the rest. A second card run (`plans/review/checks/week-35/card-second-run.md`) reached the same must and added shoulds for page 1, Grades 2–3 Problems 2–3, K–1 Problem 4 and Grades 4–5 Problem 6. These are now made in the problem files (converted first with no wording change), the guide source and the kit's checker. All three packets are v4: W35-k-1-v4, W35-grades-2-3-v4 and W35-grades-4-5-v4. The guide has eight pages and the table kit did not change.

## Made

- **Should 2 and the second run's should 2, page 1 and guide p. 2.** Every band's rules start "Use the loose footprints. Build each border in its box, or on a long strip if it needs more room." The guide says a box holds two and a half to three repeats of a 6 cm border with the kit's cards, and to move to a long strip only when one repeat is longer than 6 cm (K–1 Problem 4's longer slide, a 12 cm repeating part in Grades 2–3 Problem 6).
- **Should 3, guide p. 2.** Tack finished borders down with removable tape; always trace the middle line first, since the flip is made over it; a rough outline with its arrow is enough, because the arrow's place and direction tell the four forms apart; at K–1 the adult traces and the children move the copy.
- **Should 4, every K–1 footer.** W35-k-1-v4, not the card's v3: the October 4 guide had already called the packet printed W35-k-1-v2 "K-1 v3", so a new number avoids a third meaning. The guide's packet-basis line says so. Grades 2–3 and 4–5 changed too and are v4.
- **Should 5 and the second run's should 7, guide p. 4.** Positions are footprint (card) centres; footprints should be 25–30 mm wide, since Border E's same-row footprints are 3 cm apart; the kit's are 26 mm. The page now draws T, G, H, R and E with three repeats each at 30% of actual size, in the space that was empty.
- **Should 6 and the second run's should 4, Grades 4–5 Problem 3.** "A border matches after a 3 cm glide." Problem 2 on the same page defines a glide along the middle line.
- **Should 7 and the second run's should 6, Grades 4–5 Problem 6.** "Explain why no other move matches." The problem has its own page (p. 5), so it has more than half a page to write on; the guide's key says the completeness argument is what is asked for, in a child's form.
- **The second run's should 3, Grades 2–3 Problems 2–3.** Problem 2 asks for two glide borders with different shortest matching slides (both boxes are used); Problem 3 asks "On each border". The guide keys G and G4 (4 cm period: glide 2, slide 4).
- **Could 11 and the second run's should 5, K–1 Problem 4.** "Make another border like Problem 3's, with a longer slide." The key is G8 (flip and a 4 cm slide).
- **Could 8 and the second run's could 9, guide p. 3.** The session plan counts from the launch after about five minutes of running around, with about 35–40 minutes at the tables and a few minutes of sharing.
- **Could 9 and the second run's could 11, K–1 p. 1.** The K–1 rules keep four sentences; the launch says the other three aloud (the border repeats forever both ways; only footprints count, not strip ends or guide lines; a slide must move the copy).
- **Could 10 and the second run's could 12.** The second box under a one-border problem is labelled "Extra workspace": Grades 2–3 Problems 4 and 5, Grades 4–5 Problems 2, 4 and 5. (Grades 2–3 Problem 2 now uses both boxes.)
- **Could 12.** "Shortest" throughout: Grades 2–3 Problem 1 and Grades 4–5 Problem 1 ("explain why a shorter slide cannot match").
- **The second run's could 10, guide p. 3.** "At the K-1 table, start with one repeating row".
- **The second run's could 13.** The revision residue on guide pp. 1 and 7 is cut, and the K–1 Problem 1 key moved from the route note into the K–1 key (now p. 5, since the launch and session plan have their own page 3).

The guide's "Checking a child's own border" section moved to page 3 to leave room for the drawn witnesses. The kit's checker (`materials/verify_materials.py`) now also fits G at 4 and 8 cm; the kit PDF did not change.

## Left

Nothing on either card's fix list. The math check's items 5 and 6 concern the bonus, which neither card reviewed.

## Verification

- `review/verify_card_fixes_2026_10_23.py [build]` checks every change in the built PDFs (footers, rules, prompts, boards, label positions, page room, the guide's page plan, sentences and references, and the 33 drawn witness footprints, three repeats in each of five boxes) and recomputes the changed claims with an exact frieze test on the package's motif: shortest slides of T4, T6, G4, G, G8, H, R and E; glides of G4, G and G8 at odd multiples of half the period with the flip and the half-length slide failing; every glide twice a slide; G's 3 cm glide without a 3 cm slide; H, R and E's moves; how many repeats of each 6 cm witness fit a box with 29 mm cards. It passes (186 checks).
- `verify_math.py` (the student, motif and guide checks) and `materials/verify_materials.py` pass.
- Changed pages were rendered and inspected: all student pages and all eight guide pages.
- The reference PDFs and `review/reference-manifest.json` are the new builds; `verify.py` and `verify_revision.py` pass from a clean rebuild of the extracted ZIP, with no pixel allowances needed.
- The replaced PDFs are in the project's `week-35/archive-before-card-shoulds-2026-10-23/`, and the replaced ZIP in `source/week-35/archive-before-card-shoulds-2026-10-23/`.

All of this is digital checking. The week, the kit, the taping and tracing routine and the new pages remain unpiloted and physically unrehearsed.
