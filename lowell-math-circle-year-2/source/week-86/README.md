# Week 86: Pursuit and escape

Prepared shared Grades 2–5 and upper Grades 4–5 investigations: 4+6 student pages, 3 materials pages, 6-page theorem-first facilitator guide. No independent K–1 packet. Unpiloted; printed counter fit, stacking, turn-tile assembly and fold-cover procedures remain physically untested. This is a library entry with several possible visits, not an adopted date.

## Printing and routes

Print US Letter, single-sided at Actual Size. The shared packet explores paths, trees and rings. The upper packet preserves road edits, game design, graph folds and two-cop strategies as return visits; it repeats the path launch so it can stand alone. Read the guide for prerequisites, preparation, launch, first routes and full mathematical arguments. Materials pages 1–2 contain unchanged original and working copies of the fold graphs; page 3 contains turn tiles, counters and cover preparation instructions. Use opaque removable covers: ink printed underneath a sleeve cannot be erased. Keep surviving features visible. Two cops on one dot may be stacked or slightly offset with both identities visible.

## Rebuild offline

Requires Python 3 and TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, geometry, fancyhdr, AMS, hyperref, T1 and Latin Modern. No third-party Python module, network, private reference or repository file is needed.

    python3 build.py --out output
    python3 build.py --verify-only

The first builds all four named PDFs; the second runs independent finite-state checks without TeX. Edit `student/build.py` for student/material content and `guide/facilitator.tex` for the guide. The wrapper builds in temporary directories with fixed metadata. Different TeX/font versions may change bytes. `reference-pdfs/` contains the delivered owned PDFs for comparison.

## Evidence and limits

The production record in `plans/seven-families-85-91/production/week-86/` preserves separate fresh writer, adversarial critic, mathematical reviewer and reviser reports, final student–guide review and release audit. The guide is separately authored. `student/QA.md` records all 13 final student/material page inspections and geometric checks. Finite checks support examples; general strategies and assumptions appear in the guide. Source ZIP excludes downloaded references, borrowed prompt exemplars, caches, logs and private records. Canonical Git publication does not imply a Drive upload.
