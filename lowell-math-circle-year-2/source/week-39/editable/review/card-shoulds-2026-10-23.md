# Week 39: the review card's remaining shoulds, October 23, 2026

The second set of fixes from the review card (`plans/review/week-39.md` in the project, math check `plans/review/week-39-math.md`), made in the problem files the same afternoon as `card-fixes-2026-10-23.md`. Every Grades 2–3 and 4–5 page changed, and both packets now print v3 IDs (F39-23-v3, F39-45-v3). K–1 pages 1, 3, 4 and 5 changed; K–1 pages 2 and 6 are unchanged, and K–1 keeps F39-K-v3 from the morning. Every guide page changed, at least in its footer.

## What changed

- **Should 2, Grades 4–5 Problem 4.** The third recorded trip A→B→C→D→A→B→C→B→A had only one removal order. It is now A→B→C→B→C→D→A→B→A: three first choices, four orders, still ending at A→B→C→D→A. The key (guide p. 5) shows two orders.
- **Should 3, Grades 4–5 Problem 6.** Now "Join the same four ring trips in every possible order. Which orders disappear?" with a large answer box. Key: of the 24 orders, 16 disappear; the 8 that alternate left and right survive.
- **Should 4, Grades 2–3 Problem 5.** Now defines left forward, left backward and right forward and asks children to join them in all six orders: "Which orders shorten to the same trip?" Four shorten to H→C→D→H; the other two survive and differ. The map is smaller to make room for an answer box.
- **Should 5, every band.** The rules name "an out-and-back pair" once, and every problem uses that name in place of "immediate out-and-back steps", "immediate reversals" and "detours".
- **Should 6.** "an adult may record" is cut from the rules.
- **Should 7, every page 1.** The worked example labels the input row A→B→C→B→D and the output row A→B→D; the "replay" and "then replay" labels are gone.
- **Should 8, Grades 2–3 and 4–5 Problem 1.** Each recorded trip has an answer line under it, using the space above the routes, and two lines are added for the new seven-step trip.
- **Should 9, K–1 Problems 5 and 6.** "Make trips from C to F that use every road and shorten each one. Can two of them end differently?" and "Make eight-step trips from A back to A and shorten each. Find every different result." The K–1 Problem 5 key now answers that question.
- **Should 10, rest.** The guide's footers count "n / 7": `facilitator-src/build.py` adds the route note's page to the total, and the route note page reads "7 / 7".
- **Should 11.** One K–1 key, Problems 1–7 in order, on guide p. 3 (Problems 1–2 had been on the route note page). The route note gives a first route for every band: K–1 Problems 1–2, Grades 2–3 Problems 1–4, Grades 4–5 Problems 1–4. The removal-order problem is on the Grades 4–5 first route in the problem files too.
- **Should 12.** Guide p. 2 says the printed maps on the student pages are the mats; the unprinted two-ring mat is gone.
- **Could 13.** Guide pp. 1 and 7 say "a zero-net-count trip that cannot disappear".
- **Could 14.** Grades 2–3 and 4–5 Problem 5 say "H to A to B and back to H" in place of "around the left ring through A".
- **Could 15.** Grades 2–3 Problem 2 asks for two 12-step trips, not three.

## Verification

- `python3 review/verify_card_shoulds_2026_10_23.py` enumerates the claims (removal orders of both routes, the six three-trip orders, the 24 four-trip orders) and reads the reference PDFs for each change above. Run on the earlier PDFs it fails at its first page check. `review/verify_card_fixes_2026_10_23.py` still passes, updated for the v3 IDs and the reworded p. 6 note.
- The package's own math checks follow the new examples: `src/check_math.py` and `facilitator-src/verify_answers.py` check A→B→C→B→C→D→A→B→A and its listed removal chains, and `src/check_math.py` also checks both ring-order classifications.
- K–1 pages 2 and 6 have identical text, drawings and 100-dpi pixels. The audited pixel allowances for the old Grades 2–3 and 4–5 packets are removed, since every page of both changed; all three packets are now compiled with this project's TeX. Each changed page was rendered at 80 dpi and inspected.
- `problem-files/check_guide_copy.py` reports that every guide sentence still agrees with the problem files.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and both card verifiers.
- The previous print PDFs and ZIP are archived in the project in `week-39/archive-before-card-shoulds-2026-10-23/` and `source/week-39/archive-before-card-shoulds-2026-10-23/`.

The theme remains unpiloted, and the pawn-and-tile procedure has not been tried with children.

## Footer id, later on October 23

These shoulds changed K–1 pages 1, 3, 4 and 5 after the morning's must fix had already printed F39-K-v3, so two K–1 printings shared that id. A footer-version sweep the same day bumped K–1 to F39-K-v4 (`version` in the K–1 table of `week.toml`) and guide p. 6's key-alignment line to match; Grades 2–3 and 4–5 keep v3, and the key view keeps F39-G-v3. The rebuilt K–1 packet and guide differ from the previous ones only in that id: the text is identical after the id swap, and the differing pixels lie in the footer row and the key-alignment line. Both card verifiers now expect F39-K-v4.
