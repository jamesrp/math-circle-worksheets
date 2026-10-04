# Week 7 return visits: Take-away games

Prepared October 4, 2026. **Unpiloted; physical material-fit and procedure rehearsal not performed.** Three distinct investigations in one shared student companion, with actual suitable bands on each page. The adult companion opens with precise facts, assumptions and limits, then gives practical entries and checked solutions. These files remain separate from every base packet and guide.

- Current student PDF: [week-07-return-visit.pdf](../../week-07/week-07-return-visit.pdf).
- Adult PDF: [week-07-return-visit-facilitator.pdf](../../week-07/week-07-return-visit-facilitator.pdf).
- Inventory, novelty and verification: [range inventory](../../../plans/bonus-weeks-06-10.md).

## Portable clean build

Requires Python 3 and pdfLaTeX with TikZ, fancyhdr, geometry, lmodern, enumitem, amsmath and Source Sans Pro. No external images, network access or repository-relative imports are required. The MacTeX binary is found automatically if it is not on PATH.

From any working directory run `sh /path/to/week-07-return-visit/build.sh /tmp/week-07-rebuild`. With no output argument a fresh system temporary directory is created and printed. The selected output directory holds the two PDFs and `.build/` intermediates. In the repository use an output under `tmp/pdfs/`; the builder never replaces current reviewed PDFs automatically.

`student/return-visit.tex` is editable student source; `facilitator.tex` is the adult source. `verify.py` independently verifies the kernels and every finite domain stated there without importing the student builder. The writer checks in `student/check*.py`, when present, check represented task instances too; the builder runs them and saves their output in `.build/`. Reviews and writer notes preserve the stage evidence; they are records, not classroom observations.

All five outlines and fresh per-week stages were assembled via the worksheet workflow. This week's run is `tmp/worksheet-runs/encore-week-07-20261004-v1/`. Explicit companion scope selects one shared student collection instead of the harness's three copies. The workflow prompt set was unchanged. Guide writing is separate and untested.

Print US Letter at 100%. Give one investigation at a time; repeat, pause or return by readiness. Record the exact examples actually tried before marking material as used. No commits, uploads or remote currentness claims were made.
