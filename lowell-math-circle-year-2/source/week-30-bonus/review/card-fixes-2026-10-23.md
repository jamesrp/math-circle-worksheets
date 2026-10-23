# Week 30 bonus guide: fixes from the base week's review card, October 23, 2026

The review card for Week 30 (`plans/review/week-30.md` in the project, with its math check `week-30-math.md`) found two wording slips in this companion's adult guide. Only the guide changed (now W30-BON-FAC-v2, pages 1 and 2). The bonus student packet and its source are unchanged.

- **Should 7, p. 1, Mathematical overview.** "every surviving pair cannot be that kit" read as saying no surviving pair can be {1,3}. It now reads "the three pairs left by the three possible removals cannot all be {1,3}".
- **Could 12, p. 2, Depth and further questions.** The equal-cards question assumed the conclusion changes. It now asks whether it changes and answers no: two equal cards a, a balance only a and 2a, so the surviving pairs must still be {1,2}, {1,3} or {2,3} (or {1,3} for targets 1–4).

`math/independent-check.py` still passes. The math check's `check_bonus.py` (in the project's `plans/review/checks/week-30/`) confirms both statements, including multisets with equal values up to 60. The rebuilt guide differs from v1 only on pages 1 and 2 and in the footer's version; pages 3–5 are unchanged above the footer at 100 dpi. `release-validation.json` records the original October 4 release and is left as it was. In this container the bonus student packet rebuilds with small glyph-raster differences from its print copy (a newer pdfTeX made the print copy), so `verify_rebuild.py` reports a pixel difference on the unchanged student pages; the print copy and its reference stay the original file.
