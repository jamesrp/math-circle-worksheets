# Week 80: October 15, 2026 revision checks

User-directed revision only; the mathematical investigations are retained.

## Digital checks

- pdfLaTeX built both PDFs twice without TeX errors or overfull boxes.
- Student packet: 5 US Letter pages. Facilitator guide: 4 US Letter pages.
- Every student and guide page was rendered and visually inspected. Changed content: student pages 1, 3 and 5; guide pages 1–2. No clipping, collisions, unreadable labels or unintended blank pages found.
- The portable source ZIP was extracted into an isolated folder and both PDFs rebuilt using only its sources. Page counts, 612 × 792 pt dimensions, extracted text and 108-dpi rendered pixels agree with the released PDFs.
- The portable mathematical checker passes. It corroborates finite examples; general infinite arguments remain in the facilitator guide.

## Independent review

A fresh reviewer inspected the revised student pages and guides independently of the editor. The review covers mathematical correctness, the requested visual changes, printed instructions, and page references. See the week-specific October 15 review record in the repository plans folder.

## Limits

These checks do not establish classroom readiness. Physical printing, fit, folding/counter/card handling, timing, and classroom use remain untested and unpiloted.

Organizer promotion: October 17, 2026. Status/metadata only; accepted student and facilitator PDFs unchanged. Unpiloted; physical rehearsal remains untested.

## October 23, 2026 card fixes (v2)

- `check_card_fixes.py` (run by `build.py`) passes 40 checks: Problem 3's keys by exact replay (flipping only at the first two marks settles OFF; flipping at every second mark never settles; jumping end to end moves 180 mm each time; the two-direction counter goes 90, 45, 112.5, 56.25 mm, every move at least 45 mm, and swings toward 120 and 60 mm); the overview's claim that short moves alone do not make a counter settle; the encore's approach to 90 mm; the six problem numbers, the changed wording, the 80 × 58 mm MIDNIGHT box against the 76 × 54 mm card, the band headers and the footer in `students.tex`; and every changed guide phrase and problem reference.
- Student packet: 6 pages; guide: 4 pages. Every changed page was rendered at 80 dpi and inspected: student pp. 2–5 and all four guide pages. Pages 1 and 6 differ from v1 only in the footer id.
- The portable ZIP was extracted into an empty folder and rebuilt: both PDFs match the installed copies in pages, text and 100-dpi pixels.
- Unpiloted; the new Problem 3, the larger box and the K–1 route are unrehearsed.
