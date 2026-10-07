# Week 68: How many ways out

One shared Grades 3–5 prototype: 4 student pages and a separate 2-page theorem-first adult guide. Independently reviewed and digitally checked, awaiting organizer review. Unpiloted; physical preparation and handling have not been rehearsed. The week number is a library identifier, not an adopted schedule.

## Build from this portable package

Use Python 3 and a normal TeX Live/MacTeX installation with pdfLaTeX, TikZ/PGF, AMS fonts, geometry, fancyhdr and Latin Modern (the guides may additionally use enumitem and hyperref). No network, repository files, private references, external artwork or custom Python packages are needed.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs both named PDFs; the second runs the independent, student and adult mathematical checks without TeX. Builders run in an isolated temporary directory. Edit `student/students.tex` and `guide/facilitator.tex`; if a README says a diagram file is generated, edit its included generator and rebuild. All required authored input is here.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. The grade band is approximate and not a readiness guarantee. Read `student/README.md` for the particular reading, arithmetic, spatial and representational prerequisites, and the adult guide for materials, preparation, a manageable first route, hints and stopping points. No K–1 route is implied. Page completion is not the goal.

The mathematical destination is distinct from the familiar props: Ends describe components continuing infinitely far after deleting a finite region, as larger finite deletions are considered.

`MATHEMATICS.md` records assumptions and general arguments. `SOURCES.md` gives verified primary-source locations and attribution limits. Independent adversarial review and revision decisions are preserved in the repository's `plans/ggt-prototypes-66-75/week-68/` record. The actual ZIP extraction/rebuild comparison is recorded there as `release-checks.json`; a source/PDF build does not establish physical readiness.

The package excludes stage prompts, borrowed exemplars, downloaded references, cached fonts, generated render images, build logs, old versions and private classroom information.
