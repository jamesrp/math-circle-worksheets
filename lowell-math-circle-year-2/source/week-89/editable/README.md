# Week 89 — Growing shapes and totals

Owned editable source for the current unpiloted release. The shared K–5 menu has 20 problems; the header does not imply every page fits every age. K–1 may handle square/staircase layers with adult reading; 2–3 work with a single total and hidden additions; 4–5 can optimize two-stage inputs, investigate explicit building laws, peel cube shells and connect repeated sums to corner piles. Readiness and return routes are in the theorem-first facilitator guide. Physical copying/retention, tile fit, counters/cards, shell and pile handling remain untested.

- `student/students.tex`: 11 student pages, problems 1–20, written from the problem files by `student/regenerate.py` (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`). Edit the problem files, not `students.tex`; the build regenerates it first. Stored this way since October 23, 2026.
- `student/materials.tex`: two 20 mm working-board pages and reusable input cards.
- `guide/facilitator.tex`: theorem-first overview, complete keys, proofs and limits, routes, preparation, sources.
- `check_math.py`: independent standard-library checks of examples and finite cases; general proof explanations are in the guide.
- `reference-pdfs/`: copies of the current print PDFs.

Run `python3 build.py --out rebuilt` (after extracting the ZIP: `python3 week-89/build.py --out rebuilt --work tmp/build`). Requires Python 3.11 or later and pdfLaTeX with TikZ, geometry, fancyhdr, AMS packages and Latin Modern (standard TeX Live). No network, absolute reference checkout, external art or external Python package is needed. The builder runs the independent checks and two LaTeX passes, fixes output metadata and rejects overfull content. A clean extracted ZIP rebuild matches the reference PDFs in pages, extracted text and pixels; a reference compiled with a different pdfTeX version can differ by a few antialiased glyph pixels.

Print US Letter, Actual Size. Boards use 20 mm cells; keep reference pictures compact and build on the supplied boards or table. One current shape at a time; do not require simultaneous snapshots. Input cards are reusable across different visits; totals remain writable. The 72-tile kit covers the largest pairing; third-stage work uses numeral cards when counters exceed the supplied 40. A shared 64-cube kit supports one side-four cube.

The rich reserved plan is retained as a shared menu and distinct return visits, rather than three forced packets. The optional general third-stage formula follows concrete pile work when useful. No claim of classroom use, physical rehearsal or remote Drive upload is made. See `SOURCES.md` for actual primary research and provenance and `QA.md` for review/rebuild evidence.
