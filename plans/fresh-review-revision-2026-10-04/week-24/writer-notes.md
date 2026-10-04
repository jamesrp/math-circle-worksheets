# Week 24 writer-stage notes

Scope: authorized targeted revision of K–1 Problems 1–3 only. This is a draft for independent review, not a release.

## Changed sources and outputs

- `tmp/fresh-review-revision-2026-10-04/week-24/src/build_packets.py`: added `shared_pairs`, which pictures each of the nine distinct card pairs as two labeled numeral/dot cards; revised K–1 Problems 1–3 to use this pooled record.
- `tmp/fresh-review-revision-2026-10-04/week-24/src/k-1.tex`: regenerated from the generator.
- `tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft/k-1.pdf`: revised eight-page student packet.
- `draft/grades-2-3.pdf` and `draft/grades-4-5.pdf`: unchanged seven-page reference PDFs, copied byte-for-byte for the complete writer-stage deliverable.
- `draft/src/build_packets.py` and `draft/src/k-1.tex`: review copies of the changed sources. Canonical draft source remains in the copied `week-24/src/` package.

No facilitator sources, AGENTS, indexes, released PDFs, bonus files, or reference PDFs were edited. The top-level builder was not run.

## Decisions

Problem 1 now states the shared convention for Problems 1–3: split the pairs among children, and circle all nine winners on one shared page for each comparison. A–B, B–C, and C–A each have every pair already pictured, so children do not transcribe 27 pairs. The pooled nine-outcome comparison remains compulsory; it is not replaced by random trials. Problem 2 retains the pairwise advantage question, and Problem 3 retains the question of whether any deck beats both others.

The original full-size deck diagrams and their numeral/dot combinations remain at exactly their former positions and sizes. The new record cards use the existing `.73 × 1.1 inch` numeral/dot illustration scale; they are illustrations, not physical card templates. Each pair has separate deck labels, avoiding a new row/column decoding convention.

## Preservation evidence

K–1 Problems 4–8 are unchanged byte-for-byte in generated TeX. They retain choosing a counter-deck and playing six rounds, trying replacements 3/5/7/9, finding every A–B swap that reverses advantage, equal-win impossibility with six distinct cards in two three-card decks, and the three two-card deck cycle question. Their rendered PDF pages are pixel-identical to the original source compiled in the same runtime.

Both older TeX files are byte-identical to the writer baseline. Both older draft PDFs are byte-identical to the original references. All older mathematics, including every 4–5 problem, is retained.

## Checks

- Parsed the generated numeral nodes for each changed page: the original six deck cards followed by precisely the nine Cartesian-product pairs, each occurring once.
- Independently counted winners: A beats B 5:4; B beats C 5:4; C beats A 5:4; no ties. Thus no deck beats both others.
- Ran all original `src/check_answers.py` assertions successfully; `answer-checks.txt` remained byte-identical. The output is in `week-24/build/writer-math-checks.txt`.
- Compiled all three bands with two pdflatex passes; no overflow or LaTeX warnings in the student console logs. Page counts: 8, 7, 7.
- Rendered and visually inspected every delivered page: all eight K–1 pages and all fourteen older-band pages. Changed pages have clear labels, room to circle the winning cards, and no overlap with the preserved deck diagrams or footer.
- The old reference K–1 PDF has tiny prompt glyph raster differences under this TeX runtime; rebuilding the original source confirms these are runtime rendering differences, because original/revised pages 4–8 render pixel-identically when built together.

Physical handling, classroom pacing, and classroom piloting remain untested. Extracted portable-ZIP rebuild and release synchronization belong to the parent revision path; this writer stage has not created or altered a source ZIP.
