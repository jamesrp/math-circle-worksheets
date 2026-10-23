# Week 39: fixes from the review card, October 23, 2026

K–1 page 6, the K–1 footer id and adult guide page 3 changed. The Grades 2–3 and 4–5 packets and guide pages 1, 2 and 4–7 are unchanged. The review card is `plans/review/week-39.md` in the project, with its math check `plans/review/week-39-math.md`. The student page was changed in the problem files (`problem-files/problems/08-k1-ring-a-to-c.md` and the K–1 `version` in `problem-files/week.toml`), the guide in `facilitator-src/content.json`.

## What changed

- **Must (card fix 1), K–1 p. 6, Problem 7.** "Can two of your remaining trips visit exactly the same roads in a different order?" had two readings: ABCDABC and ADCBADC use the same four roads, but each crosses a different two roads twice, so a child comparing tiles can rightly say no, and the key called that wrong. The question now reads "Can two of your remaining trips use the same four roads?", and the guide's key (p. 3) adds "Accept no with the reason that the tiles differ."
- **Should (fix 10, the K–1 part).** Guide p. 6 says the K–1 packet is F39-K-v3, but it printed F39-K-v2. The revised K–1 now prints F39-K-v3 on every page; Grades 2–3 and 4–5 keep v2.

Deferred: the rest of should 10 (the guide's "n / 6" page footers in a 7-page file), shoulds 2–9, 11 and 12, and coulds 13–15.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates the 32 six-step A-to-C trips on the ring. They leave ABC and ADC (15 each) and ABCDABC and ADCBADC (1 each). Only ABCDABC and ADCBADC use the same four roads, and their tiles differ: each crosses a different pair of roads twice. It then reads the reference PDFs for the new question, the F39-K-v3 footers and the key's added sentence. Run on the October 4 PDFs, it fails.
- The rebuilt guide differs from the October 4 guide only on page 3; the other six pages have identical 100-dpi pixels. The Grades 2–3 and 4–5 packets rebuild with exact reference pixels. Each changed page was rendered at 80 dpi and inspected.
- The K–1 packet is now compiled with this project's TeX Live (pdfTeX 1.40.25); the October 4 copy was compiled with pdfTeX 1.40.27. On K–1 pages 1–5 the text (apart from the footer id) and the vector drawings are identical to the October 4 copy, and the glyph rasters differ slightly. A clean rebuild here now reproduces every page exactly.
- `problem-files/check_guide_copy.py` reports that every guide sentence and table row still agrees with the problem files' keys.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and the card-fix verifier.
- The previous print PDFs and ZIP are archived in the project in `week-39/archive-before-card-fixes-2026-10-23/` and `source/week-39/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted, and the changed question has not been tried with children.
