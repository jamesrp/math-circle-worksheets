# Week 52 independent math review

Reviewed the actual `draft/students.pdf`: 12 pages, Problems 1–14; SHA-256 `a0a78506c7072052433879e06622805b08ce16ab55a0d0b0dab34db75f06b95a`. Every page was independently rendered and inspected. All printed tasks were independently solved; cell sets, bar endpoints, row/column graph links and sizes were checked from actual PDF coordinates. The mathematical audit does not rely on the writer's verification code or claims. Full independent solutions, a finite-motion proof, exhaustive data and reproducible code are in `math-audit-assets/math-audit.md`, `independent_audit.py` and `independent-results.json`.

No false mathematical assertion, incorrect brace/link mapping, wrong side count or distorted regular shape was found. One located ambiguity affects what physical/mathematical action the youngest children are asked to carry out:

## K–1 / actual page 2 / Problem 3

**Exact text:** “Remove the diagonal and make a new shape with the four side bars. Which shapes can keep the diagonal?”

**Evidence:** The requested bar has already been removed. “Keep” can mean leaving it attached during a shape change, whereas the intended investigation is trying to refit that same fixed bar to a changed frame. Under the fixed-length planar rules, four side bars of length L and that square diagonal of length sqrt(2)L permit only a square: the cell vectors satisfy |U+V|²=2L², hence U·V=0. The unbraced frame has a continuous family of non-square rhombi, but none of them accepts the same square diagonal. Thus the precise distinction children can check is whether that removed bar fits, and its identity/length must remain the same.

**Smallest fix:** Replace the second sentence with “Which shapes can you fit that same diagonal into?” The existing opposite-corner definition and fixed-bar-length rule supply the rest. Do not print the square-only answer.

## Band status

- **K–1, pages 1–2, Problems 1–3:** Mathematical content and diagrams check out; resolve the Problem 3 action ambiguity above.
- **Grades 2–3, pages 3–4, Problems 4–5:** All tasks and diagrams check out completely. C/D in Problem 4 hold shape; the minimum in Problem 5 is three braces.
- **Grades 3–5, pages 5–9, Problems 6–11:** All tasks and diagrams check out completely. The 2-by-3 minimum is four; all single/pair removal and single-addition sets independently verified. Both link conventions and recoverable reference states are correct.
- **Grades 4–5, pages 10–12, Problems 12–14:** All tasks and diagrams check out completely. The 4-by-5 minimum is eight; the answer to Problem 13 is yes; the answer to Problem 14 is no, with an exact nine-brace covered counterexample and an actual finite flex.

The audit separately proves the finite rigidity/flex statements for these complete initial square grids; it does not infer arbitrary finite motion from a first-order flex. Physical fit/handling and classroom piloting remain unperformed. No draft edits or changes outside this review report and its math-audit assets were made.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
