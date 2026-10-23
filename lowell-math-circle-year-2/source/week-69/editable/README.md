# Week 69: Thin and fat road triangles

## Introduction-audit follow-up

Student GGT69-S-v2 and guide GGT69-FAC-v2 (now v3, after the review card of October 23, 2026) show one complete road triangle: P is one step from green and two from blue, so its gap is 1. All revisions remain unpiloted; material handling has not been rehearsed. Older release descriptions below are historical.

One shared Grades 4–5 prototype: 4 student pages and a separate 3-page theorem-first adult guide. Independently reviewed and digitally checked, awaiting organizer review. Unpiloted; physical preparation and handling have not been rehearsed. The week number is a library identifier, not an adopted schedule.

## Build from this portable package

Use Python 3.11+ and a normal TeX Live/MacTeX installation with pdfLaTeX, TikZ/PGF, AMS fonts, geometry, fancyhdr and Latin Modern (the guides may additionally use enumitem and hyperref). No network, repository files, private references, external artwork or custom Python packages are needed.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs both named PDFs; the second runs the independent, student and adult mathematical checks without TeX. Builders run in an isolated temporary directory. All required authored input is here.

The student pages are stored as problem files (since October 23, 2026): one file per problem in `problem-files/problems/`, with `problem-files/week.toml` and `problem-files/template.tex` (in the repository, `lowell-math-circle-year-2/source/week-69/`). Edit a problem there. `student/regenerate.py` writes `student/students.tex` from them, and `build.py` runs it first, so do not edit `students.tex` by hand. `problem-files/tools/build.py problem-files --out DIR` builds the same student packet together with a one-page problem menu and first-route and return packets. Edit the adult guide in `guide/facilitator.tex`. `reference-pdfs/` holds the current print PDFs, for comparing a rebuild.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. The grade band is approximate and not a readiness guarantee. Read `student/README.md` for the particular reading, arithmetic, spatial and representational prerequisites, and the adult guide for materials, preparation, a manageable first route, hints and stopping points. No K–1 route is implied. Page completion is not the goal.

The mathematical destination is distinct from the familiar props: A geodesic triangle chooses one shortest path between each pair of three vertices.

`MATHEMATICS.md` records assumptions and general arguments. `SOURCES.md` gives verified primary-source locations and attribution limits. Independent adversarial review and revision decisions are preserved in the repository's `plans/ggt-prototypes-66-75/week-69/` record. The actual ZIP extraction/rebuild comparison is recorded there as `release-checks.json`; a source/PDF build does not establish physical readiness.

The package excludes stage prompts, borrowed exemplars, downloaded references, cached fonts, generated render images, build logs, old versions and private classroom information.
