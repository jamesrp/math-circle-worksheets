# Week 10 return visits: Bridges

Prepared October 4, 2026. **Unpiloted; physical material-fit and procedure rehearsal not performed.** Three distinct investigations in one shared student companion, with actual suitable bands on each page. The adult companion opens with precise facts, assumptions and limits, then gives practical entries and checked solutions. These files remain separate from every base packet and guide.

- Current student PDF: [week-10-return-visit.pdf](../../week-10/week-10-return-visit.pdf).
- Adult PDF: [week-10-return-visit-facilitator.pdf](../../week-10/week-10-return-visit-facilitator.pdf).
- Inventory, novelty and verification: [range inventory](../../../plans/bonus-weeks-06-10.md).

## Portable clean build

Requires Python 3.9 or later and pdfLaTeX. The source imports these LaTeX packages: amsmath, amssymb, enumitem, fancyhdr, fontenc, geometry, sourcesanspro, tikz, xcolor. An `extarticle` class, when used by the student source, is provided by the extsizes collection. The Source Sans Pro font package is used for the guide. No external images, network access or repository-relative imports are required. The MacTeX binary is found automatically if it is not on PATH.

From any working directory run `sh /path/to/week-10-return-visit/build.sh /tmp/week-10-rebuild`. With no output argument a fresh system temporary directory is created and printed. The selected output directory holds the two PDFs and `.build/` intermediates. In the repository use an output under `tmp/pdfs/`; the builder never replaces current reviewed PDFs automatically.

`student/return-visit.tex` is editable student source; `facilitator.tex` is the adult source. `verify.py` independently verifies the kernels and every finite domain stated there without importing the student builder. Standard-library writer checks in `student/check*.py`, when present, check represented task instances too; the builder runs them and saves their output in `.build/`. The optional `check_pdf.py` and `check_independent.py` require PDF arguments and PyMuPDF and are excluded from the clean builder. Reviews and writer notes preserve the stage evidence; they are records, not classroom observations.

The builder copies student authoring files into `.build/student/` before working. If `student/generate.py` is present, that standard-library generator regenerates the TeX there from its included data. Edit `generate.py` and its data (for example `towns.json`) for such a packet; the adjacent TeX is the reviewable generated reference. Without a generator, edit the TeX directly. No rebuild changes the editable source directory.

The student source is compiled twice to resolve remembered TikZ page anchors. Copy the PDF only after both passes; a first-pass file can contain empty anchored pages.

When `student/check_pdf.py` is present, it is an optional geometry and render checker requiring PyMuPDF. After building, run `python /path/to/student/check_pdf.py /path/to/built/student.pdf --render-dir /tmp/week-10-pdf-qa` with a Python environment that has PyMuPDF. Its outputs stay in the chosen QA directory. It is deliberately excluded from the standard-library-only clean builder.

When `student/check_independent.py` is present, run it separately with `python /path/to/student/check_independent.py /path/to/built/student.pdf --output /tmp/week-10-independent.json` using that same PyMuPDF environment. It independently checks the mathematics and actual PDF vectors without importing the other checkers.

When `independent-math/` is present, it preserves the fresh mathematics reviewer's separate code and finite-result report. Its README or script argument help gives the optional built-PDF check; PyMuPDF is required. It remains outside the standard-library-only clean builder.

All five outlines and fresh per-week stages were assembled via the worksheet workflow. This week's run is `tmp/worksheet-runs/encore-week-10-20261004-v1/`. Explicit companion scope selects one shared student collection instead of the harness's three copies. The workflow prompt set was unchanged. Guide writing is separate and untested.

Print US Letter at 100%. Give one investigation at a time; repeat, pause or return by readiness. Record the exact examples actually tried before marking material as used. No commits, uploads or remote currentness claims were made.
