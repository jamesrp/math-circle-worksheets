# Week 65: Hyperbolic octagon streets

One shared Grades 3–5 packet: six student pages (five problems plus a loose route-record sheet), with a separate seven-page theorem-first adult guide. Grade labels are approximate: local heading, partner checking and distinguishing street walks from room crossings matter more than arithmetic. No forced K–1 version is included.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md) in this folder: `week.toml`, `figures.py` (the old builder's page template and drawing code) and one file per problem in `problems/`. The {8,4} construction moved unchanged into `student/geometry.py`, which `figures.py` draws with and `student/build.py` checks. The conversion changed no wording or figure: the generated `student/students.tex` is byte-identical to the old builder's, and the packet rebuilds with the same pages, text and 100-dpi pixels. The old builder and the October 6 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (figures and the page template in `figures.py`), then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-65 --out tmp/week-65-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-65-views lowell-math-circle-year-2/week-65 week-65
  ```

  Week 65 is a shared-packet week, so its one-page menu in [band-views/week-65/](../../band-views/README.md) is built from `../band-views/indexes/week-65.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Print copies:** `build.py` (below) first runs `student/regenerate.py`, which writes `student/students.tex` from the problem files, then compiles the packet and the guide. The print copies in [../../week-65/](../../week-65/) come from this build.
- **Portable ZIP:** [../week-65-source.zip](../week-65-source.zip) holds this folder with the problem-file tools in `tools/`, written by `python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-65 --flat --zip week-65-source.zip --top week-65-source`.

## Portable build

With Python 3 and a standard TeX Live/MacTeX installation providing pdfLaTeX, TikZ, amssymb, geometry, enumitem, fancyhdr, hyperref and Helvetica:

    python3 build.py --out output

This reconstructs `week-65-students.pdf` and `week-65-facilitator.pdf` in an isolated temporary directory. No repository, network, external artwork, private books, custom Python packages or absolute project paths are required. The default output folder is `output` under your current directory. Mathematical checks alone can run without TeX:

    python3 build.py --verify-only

The student pages' source is the problem files: `student/regenerate.py` writes `student/students.tex` from them, and `student/build.py` checks the geometry and compiles. Edit `problems/*.md` or `figures.py`, never only the generated TeX. `guide/facilitator.tex` is the editable adult guide. The independent geometry and route verifiers are in `guide/`. The source package contains original authored assets only; workflow prompts, borrowed style exemplars, downloaded references, old versions and render caches are excluded.

## Use and limits

Print US Letter at 100%, single-sided. A small arrow counter, another coin/counter and pencils are sufficient. The geometry is the genuine hyperbolic {8,4} tiling, with four right-angled octagons at each junction. Streets are geodesics represented by circle arcs, not ordinary Euclidean lines drawn incorrectly. This activity is separate from Week64's Euclidean octagon edge-identification and does not claim to reconstruct the user's remembered seminar.

These activities are prepared and digitally checked, but not physically rehearsed or classroom-piloted. The source notes explain assumptions, source provenance and overlap with earlier themes. Clean ZIP extraction checks compare final text, page sizes and rendered pixels in the production environment; a different TeX/font version can change rendering.
