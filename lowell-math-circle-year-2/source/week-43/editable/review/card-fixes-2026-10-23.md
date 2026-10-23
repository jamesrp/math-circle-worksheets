# Week 43: fixes from the review card, October 23, 2026

K–1 pages 2 and 3 and adult guide pages 3 and 6 changed. K–1 pages 1 and 4, the Grades 2–3 and 4–5 packets and guide pages 1, 2, 4 and 5 are unchanged. The review card is `plans/review/week-43.md` in the project, with its math check `plans/review/week-43-math.md`. The student pages were changed in the problem files (`problem-files/problems/01-chooser.md`, `02-chooser-rows.md`, `03-swap-rule.md` and `problem-files/figures.py`), the guide in `facilitator-src/guide.json` and `facilitator-src/route-note.json`.

## What changed

- **Must (card fix 1), K–1 p. 2, Problem 2.** Each card was struck through above four empty rows, which also fits the reading "this card can't be first"; the key read it as drawn first. The slashes are gone. A, B and C are each printed in the first box of two empty rows, and the problem reads "Each row starts with the card drawn first. Find every row that can still happen. Could two different first-two draws make the same row?" The guide's key (p. 3) now begins "Each displayed card is the card drawn first."
- **Should (fix 4), K–1 pp. 2–3.** No K–1 problem asks about chance. "Each card has the same chance." is cut from the K–1 chooser rule, and the K–1 swap rule now reads "Start A B C. Pick a ticket from 1, 2, 3 and swap that slot with slot 1. Then pick from 2, 3 and swap that slot with slot 2. A slot may swap with itself." These are K–1 sections in the problem files; Grades 2–3 and 4–5 keep their rules.
- **Should (fix 5), K–1 p. 3, Problem 3.** The second slot mat is gone; Problem 1's mat serves. The six records now have card boxes 2.07 × 2.2 cm (0.81 × 0.87 in), up from 1.03 × 1.4 cm and about the size of Problem 4's (2.13 × 2.2 cm). The tickets stay 1 cm, as on Problem 4.
- **Could (fix 14, the typo), guide p. 6.** "The27-story" now reads "The 27-story".

Deferred: shoulds 2 (the Grades 2–3 example before Problem 5), 3 (method sentences on the Grades 2–3 and 4–5 pages), 6 (spare answer rows), 7 (Grades 2–3 Problem 4) and 8 (a print-and-cut kit page), coulds 9–13, and the Sattolo naming in could 14. Later the same day shoulds 2, 3, 6, 7 and 8, coulds 10 and 11 (in part) and the Sattolo naming were made; see `card-shoulds-2026-10-23.md`.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates the chooser (with A, B or C drawn first exactly two rows can still happen, and the six first-two draws give six different rows). It then reads the reference PDFs. On K–1 p. 2 it checks the new wording, that no cross-out stroke is drawn, and that each card fills the first box of exactly two empty rows. On p. 3 it checks the new rule, that no K–1 page mentions chance, and that Problem 3 has no mat and six records at Problem 4's size. In the guide it checks the key sentence and the rows it lists, and the p. 6 typo. Run on the October 4 PDFs, it fails at the first check.
- The rebuilt K–1 packet differs from the October 4 one only on pages 2 and 3. Pages 1 and 4 have identical 100-dpi pixels, drawings and text, so their audited font alternates in `rebuild-pixel-allowances.json` still apply; those of pages 2 and 3 are removed. The Grades 2–3 and 4–5 packets rebuild with exact reference pixels. The guide differs only on pages 3 and 6. Each changed page was rendered at 80 dpi and inspected.
- `problem-files/check_guide_copy.py` reports that every guide sentence and table row still agrees with the problem files' keys.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and the card-fix verifier.
- The previous print PDFs and ZIP are archived in the project in `week-43/archive-before-card-fixes-2026-10-23/` and `source/week-43/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted, and the changed pages have not been tried with cards on a table.
