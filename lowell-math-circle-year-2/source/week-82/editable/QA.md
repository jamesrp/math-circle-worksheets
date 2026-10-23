# Week 82: revision checks

## October 17, 2026 current revision

Six student/material pages and four guide pages. All ten final pages rendered at 108 dpi and visually inspected; no clipping, collisions or unreadable labels found. The organizer's three-sentence class-lines introduction is exact; the identifier rule first appears in Problem 2. The old page 5 was inspected before removal and contained only four continuation-strip cutouts. Problems 1–4, their diagrams/workspaces and the remaining materials are preserved. The guide now references cards on page 5, panels on page 6, and drawing continuation arrows on blank paper.

The existing independent checker and a separate fresh mathematical reviewer checked the unchanged finite/infinite arguments. Clean extracted-ZIP build results and hashes are recorded in the October 17 review record. Organizer-approved and promoted after the subsequent “LGTM” review. This promotion changes metadata only; accepted PDFs and mathematical sources are unchanged. Unpiloted; physical preparation, handling and classroom procedures remain untested.

## October 15, 2026 prior revision

User-directed revision only; the mathematical investigations are retained.

## Digital checks

- pdfLaTeX built both PDFs twice without TeX errors or overfull boxes.
- Student packet: 7 US Letter pages. Facilitator guide: 4 US Letter pages.
- Every student and guide page was rendered and visually inspected. Changed content: student pages 1 and 3; guide pages 1–3. No clipping, collisions, unreadable labels or unintended blank pages found.
- The portable source ZIP was extracted into an isolated folder and both PDFs rebuilt using only its sources. Page counts, 612 × 792 pt dimensions, extracted text and 108-dpi rendered pixels agree with the released PDFs.
- The portable mathematical checker passes. It corroborates finite examples; general infinite arguments remain in the facilitator guide.

## Independent review

A fresh reviewer inspected the revised student pages and guides independently of the editor. The review covers mathematical correctness, the requested visual changes, printed instructions, and page references. See the week-specific October 15 review record in the repository plans folder.

## October 23, 2026 card fixes (v2)

- `check_card_fixes.py` (run by `build.py`) passes 37 checks: Problem 4's ten two-row arrangements, three shapes, 18 same-shape and 27 other pairs; the WSW-to-WW match (★ → B1, Bn → B(n + 1)) increasing and onto on the first 2000 kids of each row; WWS's last kid; three panels for WSWS beside WWS and no pair needing more; the guide's six-shape table against every one- and two-row arrangement; the launch rule (top kid 20 with bottom 19, a complete match); the K–1 key (six ways, one uncrossed); the changed wording, answer-line spacing, panel count and footer in `students.tex`; and every changed guide phrase.
- Student packet: 6 pages; guide: 4 pages. Every changed page was rendered at 80 dpi and inspected: student pp. 1–4 and 6 and all four guide pages. Page 5 differs from draft-v1 only in the footer id.
- The portable ZIP was extracted into an empty folder and rebuilt: both PDFs match the installed copies in pages, text and 100-dpi pixels.
- Unpiloted; the third panel, the launch demonstration and the K–1 route are unrehearsed.

## Limits

These checks do not establish classroom readiness. Physical printing, fit, folding/counter/card handling, timing, and classroom use remain untested and unpiloted.

Critic follow-up, October 23, 2026 (W82-FAC-v2): the guide's footer carries a version id and page 1 points to the next page for the K–1 route. `check_card_fixes.py` checks both; a clean build from the extracted ZIP matches the print copies. The student packet is unchanged. Unpiloted.
