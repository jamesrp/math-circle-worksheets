# Week 24 final revision-stage notes

Prepared October 4, 2026. **Disposition: accepted without further student changes.**

Read `PROMPT.md`, `REVISE.md`, `writer-notes.md`, `review.md` and `review-math.md`, then the canonical copied student sources and actual accepted PDFs. The targeted-revision contract governs this stage. The independent reviewers found no mandatory student defects. The final stage adds no polishing, method hints or microsteps.

## Decision and preservation

The accepted writer revision already gives K–1 Problems 1–3 a complete pooled nine-pair record per deck comparison, with each pair pictured once. Preserve that shared-work instruction and all later K–1 tasks. Both older bands are unchanged from the current packet. No further student edit was needed. All original full-size deck diagrams are preserved; the new smaller pair cards are recording illustrations rather than physical templates.

## Exact deliverables

All paths below are relative to `tmp/fresh-review-revision-2026-10-04/student-stages/week-24`. The complete three-band source set is `final/src/`, copied from `../../week-24/src/` (excluding Python cache files). Generators were run only in this final source copy; no parent working sources were edited.

| Final PDF | Pages | Revision-stage status |
|---|---:|---|
| `final/k-1.pdf` | 8 | Byte-identical accepted draft |
| `final/grades-2-3.pdf` | 7 | Byte-identical accepted draft |
| `final/grades-4-5.pdf` | 7 | Byte-identical accepted draft |

## Checks and mathematical evidence

Read the independent adversarial and mathematical reviews. Complete Cartesian-product comparisons remain nine equiprobable outcomes each, with directed counts A–B, B–C and C–A all 5:4 and no ties. The reviews also checked every retained construction/impossibility task under the stated fair independent replacement-draw model. The student generator reproduces all three TeX files exactly; `check_answers.py` passes. The source-only K–1 rebuild is pixel-identical to the accepted draft.

Every final PDF is byte-identical to its accepted draft; every page also matches extracted text, page geometry, vector drawing geometry/style and 108 dpi pixels. All pages are US Letter (612 × 792 points). Sources were compiled from this source-only copy until the TikZ page-position references stabilized; final compilation logs contain no LaTeX warnings or overfull/underfull boxes.

Rendered and visually inspected every delivered page (22 pages across all three bands) in legible two-page contact sheets at original image resolution. Checked prompts, labels, diagrams, record/workspace, footers, and continuation pages. No clipping, overlap, missing label or changed physical scale was found. The actual vector diagrams equal the accepted drafts, retaining every reviewed board/material dimension.

The two unchanged older-band source-only rebuilds preserve extracted text, page dimensions and every vector drawing geometry/style, but do not render pixel-identically to the existing reference PDFs under this TeX runtime. Exact measured differences:

| Band | Maximum text-bound delta | Pixels differing at 108 dpi, all pages |
|---|---:|---:|
| grades-2-3 | 0.02770996 pt | 2648 |
| grades-4-5 | 0.02767944 pt | 1833 |

These are the existing writer-noted runtime glyph differences. Final PDFs intentionally preserve accepted older-band bytes exactly. No source/rebuild pixel-equality claim is made for those four PDFs.

Machine-readable per-page evidence and source hashes: `final/verification/verification-results.json`. Generator/math/compiler logs and final page renders are in `final/verification/`; rebuilt comparison PDFs are in `final/verification/rebuild/`. All four weeks are also summarized in `../../reviser-final-results.json`.

## Release handoff and honest limits

The parent guide should assign pair cases among children and collect one checkable nine-outcome page for each comparison. No guide edits were made here.

The parent owns release synchronization, reference copies, source ZIPs and extracted-ZIP rebuild checks. This stage did not edit adult guides, AGENTS, releases, references, ZIPs, indexes or bonus files, and did not commit, push, publish or upload. Physical material rehearsal, actual-size handling and classroom piloting remain unperformed. There is no student-stage blocker; those release and physical checks are outside this stage.
