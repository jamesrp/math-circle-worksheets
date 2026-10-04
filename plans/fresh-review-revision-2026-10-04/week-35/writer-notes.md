# Week 35 writer stage: K–1 slide entry

Draft only; prepared October 4, 2026. Unpiloted. The targeted-revision contract at the end of `PROMPT.md` governed this stage.

## Files

- Changed source generator: `tmp/fresh-review-revision-2026-10-04/week-35/src/build_packets.py`.
- Regenerated changed student source: `tmp/fresh-review-revision-2026-10-04/week-35/src/k-1.tex`.
- Draft PDFs in `tmp/fresh-review-revision-2026-10-04/student-stages/week-35/draft/`: `k-1.pdf` (5 pages), `grades-2-3.pdf` (4 pages), and `grades-4-5.pdf` (4 pages).
- Writer checks: `tmp/fresh-review-revision-2026-10-04/week-35/writer-checks.json`; baseline source hashes: `writer-baseline-hashes.json` in the same folder.
- Rendered draft pages: `tmp/fresh-review-revision-2026-10-04/week-35/render-student-writer/`.
- Clean source-only rebuild: `tmp/fresh-review-revision-2026-10-04/week-35/clean-student-writer/`.

## Decisions and preserved work

K–1 now begins with one repeating border: find slides that match its tracing copy and slides that fail. This isolates translation before the existing task comparing two shortest matching slides, and before combining reflection and translation.

All six original K–1 problem texts are retained verbatim, with original Problems 1–6 renumbered as Problems 2–7. The new Problem 1 is the only added task. The unchanged, equally scaled three-panel glide visual is moved to page 3, immediately before the first glide task (new Problem 3). It still shows the same A-labelled footprint as input, reflected intermediate and shifted output. The second glide construction remains on that page as Problem 4. Reflection, half-turn and partner investigations remain intact on pages 4–5. Shared rules, half-turn explanation, motif geometry, labels and drawing helpers remain intact.

Every recording strip remains 17.65 cm by 6 cm; positions change to accommodate the new sequence, and no strip or motif is scaled down. The new first task supplies one additional full-size strip. Both older-band TeX files match their baseline hashes. Their delivered draft PDFs are byte-for-byte copies of current `reference-pdfs/` files; no older-band task, visual or dimension is changed.

## Checks

- Read current source and current student PDFs before editing. Inspected all four original K–1 pages.
- Ran the original generator's asymmetric-motif checks and `src/check_revised_cases.py`; all original symmetry witnesses pass, including glide-only, reflection without half-turn, half-turn without reflections, perpendicular reflections and larger-repeat edits.
- Checked an explicit single-border witness for the added task: identically oriented asymmetric footprints spaced every 3 cm have matching 3 cm and 6 cm slides and a failing 1.5 cm slide. A footprint's occupied x-residue modulo the primitive period supplies the infinite-pattern check, rather than treating the printed ends as the object.
- Asserted every original K–1 problem text occurs in the new TeX and problem numbers are consecutive 1–7.
- Confirmed `motif`, `strip` and `demo` function bodies are unchanged. Measured all nine actual recording-strip rectangles in the new PDF at the original dimensions.
- Compiled each band twice with pdfLaTeX. No overfull/underfull boxes or LaTeX warnings/errors were found. The unchanged upper-band local rebuilds have the same text and geometry (maximum text-bound difference from the existing reference PDFs is under 0.017 pt); copies of the existing PDFs preserve those deliveries exactly.
- Rendered and visually inspected all 13 delivered student pages. No clipping, overlap or inconsistent header/footer placement was found. The glide page retains two full-size working strips.
- Rebuilt from a fresh source-only directory. All five changed K–1 pages render pixel-identically and have identical extracted text. The PDF trailer identity depends on output location, so the two PDF files are not byte-identical.

## Handoff

No facilitator source, root/local AGENTS, indexes, current release folder, bonus file, or source ZIP was edited. Parent/reviser should apply the +1 K–1 problem-number map in the adult guide and adjust any four-page metadata when releasing the five-page draft. Release ZIP extraction checks belong to the later release stage. Physical cutout handling and classroom timing remain untested; this revision remains unpiloted.
