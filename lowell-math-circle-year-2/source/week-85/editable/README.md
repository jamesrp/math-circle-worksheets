# Week 85: Drawing machines

Prepared shared Grades 2–5 and upper Grades 4–5 investigations: 4+4 student pages, 10 materials pages, 6-page theorem-first facilitator guide (v2, October 23, 2026). No independent K–1 packet; the guide gives an adult-led K–1 route. Materials page 2 and the guide name one build (foam-board strips, brass fasteners at X, Q and Y, a pin at O, the pencils as the T and P axles) and a bought-pantograph fallback, but nobody has built it: assembly, branch retention and full-zone hand and board clearance are untested. An assembled machine must pass the guide's rehearsal before use. This week is a library identifier, not an adopted date.

## Print and routes

Use `week-85-shared.pdf` for concrete copying/inverse control; `week-85-upper.pdf` for frame explanation, area, reversal and changed-center return visits. Each packet numbers problems separately. Read the guide for prerequisites, three-pair-kit preparation, first route and later visits. Finishing every page is not the goal.

Print US Letter, single-sided at Actual Size. Material pages: 1 adult cutting template; 2 adult build, fallback and setup; 3–4 joined mat; 5 seam bridge and A/B inserts; 6 D/E; 7 F/G/H; 8 I/L/M/C; 9 J/K; 10 area pieces and kit list. The joined two-Letter mat is 431.8×279.4mm (nominal 432×279); the 44×145mm seam bridge restores printer-margin gaps. Check the 100mm scale bar after joining. Use a base at least 450×400mm (a 20×30in foam-board sheet) with the mat centered; the bars extend beyond the paper. The supplied inserts must retain their inside-cut letters. Use fresh tracing-paper overlays; do not rescale thumbnails into working parts.

## Rebuild offline

Requires Python 3.11 or later and TeX Live/MacTeX: pdfLaTeX, TikZ/PGF, geometry, fancyhdr, AMS, hyperref, T1 and Latin Modern. No third-party Python package, network, external artwork, private reference or repository file is required.

    python3 build.py --out output
    python3 build.py --verify-only

The first builds all four named PDFs; the second runs the independent finite checks without TeX. Source paths: since October 23, 2026 the student packets are problem files (in the repository `../week.toml`, `../figures.py` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`), and `figures.py` also draws the materials pages (`materials_tex()`). `student/build.py` writes the student and materials `.tex` files from them into its work folder; edit the problem files and `figures.py`, not generated `.tex`. `guide/facilitator.tex` is directly editable. The wrapper builds in temporary directories and uses fixed metadata. Different TeX/font versions can change bytes. `reference-pdfs/` contains the delivered owned PDFs for comparison.

## Evidence and limits

The production record in `plans/seven-families-85-91/production/week-85/` preserves separate fresh writer, adversarial critic, independent mathematics and reviser stages, final pair review, revisions and release audit. The guide is separately authored. `student/QA.md` records all 18 student/material final-page inspections and cut-border crops. Portable finite checks support examples; the guide supplies general arguments. Source ZIP excludes borrowed prompt exemplars, downloaded references, caches, renders, logs and private records. `check_math.py` also checks the v2 claims (the Problem 4 region, the fold and collapse poses, overlay, base and template sizes); `student/check_math.py` checks the v2 diagrams. The previous PDFs are archived beside the print copies. Canonical Git publication does not imply a Drive upload.
