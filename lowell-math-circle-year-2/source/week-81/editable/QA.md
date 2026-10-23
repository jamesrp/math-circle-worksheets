# Week 81: October 15, 2026 revision checks

User-directed revision only; the mathematical investigations are retained.

## Digital checks

- pdfLaTeX built both PDFs twice without TeX errors or overfull boxes.
- Student packet: 5 US Letter pages. Facilitator guide: 4 US Letter pages.
- Every student and guide page was rendered and visually inspected. Changed content: student pages 1, 3, 4 and 5; removal of former page 6; guide page 2. No clipping, collisions, unreadable labels or unintended blank pages found.
- The portable source ZIP was extracted into an isolated folder and both PDFs rebuilt using only its sources. Page counts, 612 × 792 pt dimensions, extracted text and 108-dpi rendered pixels agree with the released PDFs.
- The portable mathematical checker passes. It corroborates finite examples; general infinite arguments remain in the facilitator guide.

## Independent review

A fresh reviewer inspected the revised student pages and guides independently of the editor. The review covers mathematical correctness, the requested visual changes, printed instructions, and page references. See the week-specific October 15 review record in the repository plans folder.

## Limits

These checks do not establish classroom readiness. Physical printing, fit, folding/counter/card handling, timing, and classroom use remain untested and unpiloted.

Organizer promotion: October 17, 2026. Status/metadata only; accepted student and facilitator PDFs unchanged. Unpiloted; physical rehearsal remains untested.

## October 23, 2026 card fixes (v2)

- `check_math.py` passes with Problem 3's new start list. `check_card_fixes.py` (run by `build.py`, with its own move generator) passes 34 checks: the corrected repair move on every 1–4 bucket start with counts 0–3, and the old wording's (1, 0, 1) failure; from (0, 3) every play takes from bucket 2 exactly three times and the longest capped play is 3(K + 1), for caps 1–6; the longest capped game a1 + a2(K + 1) + a3(K + 1)² for caps 1–3, and 7 from (1, 1, 1) with a cap of one; the K–1 key on the nine cards; Problem 3's starts and key; Problem 5's pictures and wording, page 1's cap sentence and the footer in `students.tex`; and every changed guide phrase.
- Student packet: 5 pages; guide: 4 pages. Every changed page was rendered at 80 dpi and inspected: student pp. 1, 4 and 5 and all four guide pages. Pages 2–3 differ from draft-v1 only in the footer id.
- The portable ZIP was extracted into an empty folder and rebuilt: both PDFs match the installed copies in pages, text and 100-dpi pixels.
- Unpiloted; the (0, 3) start and the K–1 route are unrehearsed.
