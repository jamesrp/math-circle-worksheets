# Week 87: Voting and agendas

Prepared shared Grades 2–5, line Grades 3–5, and upper Grades 4–5 investigations: 3+4+2 student pages, 5 materials pages, and a 6-page theorem-first facilitator guide. No independent K–1 packet. Unpiloted; cutting, physical token fit, reset handling and timing remain untested. This is a library entry with several possible visits, not an adopted date.

Revised October 23, 2026 from the review card (plans/review/week-87.md in the repository): equal favorite stems on the line pages with one set numbered out of order, line Problem 3 asks how to tell the winner without trying every vote, upper Problem 1 named as the agenda visit's continuation, a K–1 route and a corrected shared Problem 3 key in the guide, small wording trims, a numbered work line on upper p. 2 and roomier Out and Winner boxes on the knockout mat. `review/check_card_fixes_2026_10_23.py` (claims) and `review/check_pdf.py [FOLDER]` (read from the PDFs) check them.

## Print and routes

Print US Letter, single-sided at Actual Size. Shared explores fixed imaginary rankings and agenda choice. Line begins a separate nearest-location visit, including repeated favorites, the odd-voter explanation and an even-voter limit. Upper offers pair-vote explanations and an impossibility question about the common-line model. Problems restart numbering within each packet; the guide identifies each packet. Read its prerequisites, preparation, concrete launches, first routes, return choices and full arguments. Finishing every page is not the goal.

Materials provide fixed and blank ranking cards, letter slips, option tiles, vote tokens, a tally mat, knockout mat and a five-lane favorite board. Keep favorites fixed and proposals on the board while tally labels identify the same comparison. A favorite at zero still votes; repeated favorites retain separate identities. Equal-distance voters place one token in Tie. Remove both the fifth favorite and its token for the four-voter visit. Check all five tokens fit any tally destination after actual-size printing.

## Rebuild offline

Requires Python 3.11 or later and TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, geometry, fancyhdr, AMS, hyperref, T1 and Latin Modern. No third-party Python module, network, private reference or repository file is needed.

    python3 build.py --out output
    python3 build.py --verify-only

The first builds all five named PDFs; the second runs independent finite checks without TeX. The student pages are stored as problem files (October 23, 2026): edit `problem-files/problems/*.md` for the wording of each problem in the three packets, `problem-files/figures.py` for the cards, number lines, tallies and the materials pages, and `guide/facilitator.tex` for the guide. `student/build.py` writes the student and materials LaTeX from those files with the tools in `problem-files/tools/` (Python 3.11 or later, for `tomllib`). In the repository the problem files are in `lowell-math-circle-year-2/source/week-87/`, one folder up. The wrapper uses temporary build directories and fixed metadata. Different TeX/font versions may change bytes. `reference-pdfs/` contains the delivered owned PDFs for comparison.

## Evidence and limits

The production record in `plans/seven-families-85-91/production/week-87/` preserves separate fresh writer, adversarial critic, mathematical reviewer and reviser stages, independent final student–guide review and release audit. The guide is separately authored. Finite enumeration supports the examples; universal arguments and their assumptions appear in the guide. Physical rehearsal and classroom testing remain distinct from digital checks. The ZIP excludes downloaded references, borrowed prompt exemplars, caches, raw renders and private records. Canonical Git publication does not imply a Drive upload.
