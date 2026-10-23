# Week 43: the review card's remaining shoulds, October 23, 2026

The second set of fixes from the review card (`plans/review/week-43.md` in the project, math check `plans/review/week-43-math.md`), made in the problem files the same afternoon as `card-fixes-2026-10-23.md`. K–1 pages 1–4, Grades 2–3 pages 1, 3 and 4, Grades 4–5 pages 1–3 and guide pages 1, 2, 4 and 5 changed, and a card kit page is new. Grades 2–3 page 2, Grades 4–5 page 4 and guide pages 3 and 6 are unchanged.

## What changed

- **Should 2, Grades 2–3 p. 4.** The all-slots demonstration ended "3 with 1" back at A B C, a second story for A B C beside (1,2,3), which Problem 5 asks children to find. It now ends "3 with 2" at C A B.
- **Should 3, Grades 2–3 and 4–5.** The method sentences are cut: "Use the possible choices to decide." (2–3 P1), "Settle the question using every possible choice story." (4–5 P1), "Find all its choice stories and their final orders." (4–5 P2) and "; a short run of random shuffles cannot settle the question." (4–5 P4, which now reads "Can this rule give every order the same chance? Find an exact reason."). The guide's hints (p. 2) carry them: "To decide fairness: “Use every possible choice story and its final row.” A short run of random shuffles cannot settle the question."
- **Should 6, spare rows.** K–1 P1 has 8 rows for 6 answers, K–1 P3 8 records for 6, K–1 P4 three rows per missing ticket for two answers, and Grades 2–3 and 4–5 P1 8 rows for 6. K–1 P4's card boxes are now 1.55 × 2.2 cm (were 2.13 × 2.2 cm) to fit three rows across.
- **Should 7, Grades 2–3 P4.** Now "Shuffle six times with the two-swap rule. A friend says six shuffles must show all six rows once. Is the friend right?" with six records. The key (guide p. 4): only 720 of the 46,656 equally likely runs show all six rows once, about 1 run in 65. To make room, Problem 3's targets are 0.6 cm closer together.
- **Should 8, card kit.** New `materials.pdf` (print copy `week-43-materials.pdf`), built by `materials/build_materials.py`: cards A–E at 1.7 × 2.2 in with the pages' pictures, tickets 1–5 as 2 cm squares, and a three-slot strip with the K–1 page 1 mat's 4.7 × 6.1 cm slots, one sheet per pair plus one per adult table. Guide p. 2's materials paragraph points to it.
- **Could 10, guide p. 5.** "Other designs pass too": exactly six choices of ticket sets for the swaps of slots 1, 2, 3 give one story per order, one for each order of the set sizes 4, 3, 2.
- **Could 11, in part.** "Example: choose triangle, then square; circle is left." is cut from K–1 p. 2 and Grades 2–3 and 4–5 p. 1; the picture shows it. The swap strip and launch still start from A B C, because the printed rule says "Start A B C"; changing that is not a one-line fix.
- **Could 14, rest.** Guide p. 1 names the no-self-swap rule (4–5 P5) as Sattolo's algorithm and points to Weeks 3, 23, 42, 44 and 63.

Not taken: coulds 9 (a new 4–5 P7), 12 (restructure the launch around five minutes of running) and 13 (K–1 P4–P5 changes); none is a one-line change. The card's redesign items stay with the organizer.

## Verification

- `python3 review/verify_card_shoulds_2026_10_23.py` enumerates the claims (the 27 all-slots stories, the 720 of 46,656 six-shuffle runs, Sattolo for n = 3 to 6, the six four-card designs) and reads the reference PDFs for each change above, including the number of answer rows. Run on the earlier PDFs it fails at its first page check. `review/verify_card_fixes_2026_10_23.py` still passes, updated for K–1 P3's eight records.
- `python3 materials/verify_materials.py` measures the kit from the PDF: five 43.18 × 55.88 mm cards with their pictures and letters, five 20 mm tickets, a 141 × 61 mm strip with slots at 47 mm, the same as the K–1 mat, and a 100 mm scale line.
- Unchanged pages (Grades 2–3 p. 2, Grades 4–5 p. 4, guide pp. 3 and 6) have identical text, drawings and 100-dpi pixels. Pixel allowances for changed pages are removed. Each changed page and the kit were rendered at 80 dpi and inspected.
- `problem-files/check_guide_copy.py` reports that every guide sentence still agrees with the problem files.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py`, both card verifiers and the kit verifier.
- The previous print PDFs and ZIP are archived in the project in `week-43/archive-before-card-shoulds-2026-10-23/` and `source/week-43/archive-before-card-shoulds-2026-10-23/`.

The theme remains unpiloted. The kit has been checked digitally but not cut out or used, and the changed pages have not been tried with cards on a table.
