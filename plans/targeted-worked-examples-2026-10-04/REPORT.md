# Targeted worked examples — 4 October 2026

Completed 15 student packets and six facilitator guides across Weeks 18, 22, 25, 27, 38 and 47. This is the six-topic portion of the example audit; Week 20 was completed separately. These revisions remain unpiloted.

| Week | Changed student packets | Updated adult guide | Editable package and ZIP |
|---|---|---|---|
| 18 | [K–1](../../lowell-math-circle-year-2/week-18/week-18-k-1.pdf) (7 pp.), [2–3](../../lowell-math-circle-year-2/week-18/week-18-grades-2-3.pdf) (7 pp.), [4–5](../../lowell-math-circle-year-2/week-18/week-18-grades-4-5.pdf) (7 pp.) | [Guide](../../lowell-math-circle-year-2/week-18/week-18-facilitator.pdf) (10 pp.) | [Source](../../lowell-math-circle-year-2/source/week-18/README.md) |
| 22 | [K–1](../../lowell-math-circle-year-2/week-22/week-22-k-1.pdf) (8 pp.), [2–3](../../lowell-math-circle-year-2/week-22/week-22-grades-2-3.pdf) (8 pp.), [4–5](../../lowell-math-circle-year-2/week-22/week-22-grades-4-5.pdf) (11 pp.) | [Guide](../../lowell-math-circle-year-2/week-22/week-22-facilitator.pdf) (22 pp.) | [Source](../../lowell-math-circle-year-2/source/week-22/README.md) |
| 25 | [K–1](../../lowell-math-circle-year-2/week-25/week-25-k-1.pdf) (8 pp.) | [Guide](../../lowell-math-circle-year-2/week-25/week-25-facilitator.pdf) (19 pp.) | [Source](../../lowell-math-circle-year-2/source/week-25/README.md) |
| 27 | [K–1](../../lowell-math-circle-year-2/week-27/week-27-k-1.pdf) (7 pp.), [2–3](../../lowell-math-circle-year-2/week-27/week-27-grades-2-3.pdf) (6 pp.) | [Guide](../../lowell-math-circle-year-2/week-27/week-27-facilitator.pdf) (18 pp.) | [Source](../../lowell-math-circle-year-2/source/week-27/README.md) |
| 38 | [K–1](../../lowell-math-circle-year-2/week-38/week-38-k-1.pdf) (6 pp.), [2–3](../../lowell-math-circle-year-2/week-38/week-38-grades-2-3.pdf) (6 pp.), [4–5](../../lowell-math-circle-year-2/week-38/week-38-grades-4-5.pdf) (6 pp.) | [Guide](../../lowell-math-circle-year-2/week-38/week-38-facilitator.pdf) (6 pp.) | [Source](../../lowell-math-circle-year-2/source/week-38/README.md) |
| 47 | [K–1](../../lowell-math-circle-year-2/week-47/week-47-k-1.pdf) (5 pp.), [2–3](../../lowell-math-circle-year-2/week-47/week-47-grades-2-3.pdf) (5 pp.), [4–5](../../lowell-math-circle-year-2/week-47/week-47-grades-4-5.pdf) (5 pp.) | [Guide](../../lowell-math-circle-year-2/week-47/week-47-facilitator.pdf) (3 pp.) | [Source](../../lowell-math-circle-year-2/source/week-47/README.md) |

**Week 18.** Separate training transmission 0101 → flip position 3 → 0111; sender/changer information stays hidden and only the final row crosses the folder. Lower bands use filled/empty discs; the upper band uses digits. No-change is permitted.

**Week 22.** Three persistent convention panels: E is a point, F/G give the whole closed segment, H/I/J give the triangle edge and interior. No four-point split is shown.

**Week 25.** K–1 forward encoding on a separate 2×2 A/B, 1/2 grid: counters A1 and A2 give circled row counts 2,0 and column counts 1,1, with counting sweeps and plain coordinate labels.

**Week 27.** K–1 and 2–3 compare the same PV/QU matching and candidate PU: yes/yes blocks; reversing U’s preference gives yes/no and this pair does not block. The guide retains the BOTH-prefer readiness gate.

**Week 38.** Neutral flat washer before Problem 3: two outer-edge dots and one inner-edge dot, two distinct boundary trips, and two grouping ovals recording edge membership. No cutting outcomes are shown.

**Week 47.** The existing allowed 1,2,2,1 towers connect to one height marker per column and the boxed row 1|2|2|1. The four-position model remains separate from the five-site task.

## Verification

- Independent example checks use separate calculations and source assertions without importing the generator or answer data. Existing mathematical checks also pass. See [math checks](math-qa.json).
- Every original numbered prompt remains in order. All task drawing primitives retain their dimensions; Week 38’s Problem 3 choices moved to their own page. Week 47’s open landscape questions and main boards are preserved. See [preservation checks](preservation-check.json).
- All 102 student pages and 78 adult-guide pages were rendered and visually inspected. No off-page text, lost task workspace, TeX overflow, or missing-character warning was found. See [page checks](render-qa.json). Render intermediates are in the project’s `tmp/targeted-examples-2026-10-04/render/`.
- Fresh extractions of the six current source ZIPs reproduce all 21 changed PDFs, including every page’s text, Letter dimensions, and 100-dpi rendered pixels. See [fresh ZIP reproduction](zip-reproduction.json). Rebuilds use the included generators, pdfLaTeX, ReportLab and the required DejaVu/Liberation fonts; PyMuPDF rendered the review pages.
- Current print PDFs, editable reference PDFs and ZIP reference PDFs are byte-identical. Every ZIP entry matches its extracted editable counterpart. The same package/duplicate checks include the separately revised Week 20.
- Week 25’s 2–3 and 4–5 packets and Week 27’s 4–5 packet are byte-identical to the intake copies.

The [old/new SHA-256 report](old-new-hashes.json) covers every pre-existing changed file and every delivered PDF. Previous PDFs are in each week’s `archive-before-worked-examples-2026-10-04/`; previous portable ZIPs are in the matching source archive. Downloaded source archives under `external-resources/` are unchanged.

## Shared index and books

The [Weeks 11–51 index](../../lowell-math-circle-year-2/WEEKS-11-51.md) records the completed examples across these six topics and the [separate Week 20 revision](../week-20-worked-examples-2026-10-04/verification.json). All index links were checked. The Year 2 and source entrypoints link the generated activity library.

All ten current PDFs in `combined/` were inspected. They are separate atlas investigation/planning collections, contain no affected weekly packet identifiers, and remain byte-identical. There is no current combined Weeks 11–51 book to rebuild; the archived fall books cover Weeks 2–10. See [combined-book inspection](combined-inspection.json).

No unexpected user-edit conflicts or remaining blockers were found. No commits, pushes, remote uploads, or Week 20 packet/source edits were made by this task. Physical printing, material fit and classroom use remain untested.
