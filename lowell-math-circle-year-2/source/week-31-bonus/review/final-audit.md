# Week 31 final independent mathematical audit

**Pass.** Audited actual `final/bonus.pdf` (4 pages), every rendered page, and actual `final/src/bonus.tex`. All printed tasks and represented examples are mathematically valid. No correction remains.

The final orchard is explicitly infinite beyond the printed grid. Former Problem 4 was merged into Problem 3 as “Which have clear sides but dots inside?”; former Problems 5/6/7 are now 4/5/6. All six actual tasks were independently rechecked. Triangle B is the requested clear-sided/nonempty witness. Its exact interior dots are (1,1),(2,1), while C has only extra boundary dots. All three empty-shape examples, rows 3/6, row-4 impossibility for the infinite orchard, neighbor addition example, simultaneous (4,3)/(3,4) route, exclusion of (4,2), and all 23 allowed primitive directions remain valid. The checks.json problem numbering and detailed record keys are updated to the final mapping.

The standalone `independent-check.py` now reads only the final source/PDF paths, re-runs all independent finite checks, confirms actual PDF task numbers [1, 2, 3, 4, 5, 6], and writes the current `checks.json`. It binds the inspected source by SHA-256 so a subsequent task/diagram edit cannot silently retain a pass. It does not require any draft file. The reader/rendered-page audit and mathematical proof details are in this report and `review-math.md`; the numerical checks do not substitute for physical rehearsal.

Final source SHA-256: `071dd4b0ca5a0f46244aff9cb8c4121382af221e93ec776b2976946fe6cc5125`. Final PDF SHA-256: `8177a0bd84983a8b969857533f283675c34fff7cfe4a1a842c85fc31634a670e`.

Mathematical geometry and recording spaces were inspected on each final page. Physical materials and classroom timing remain untested. This audit is mathematical; it does not claim classroom piloting or physical readiness.
