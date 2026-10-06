# Week 65: Hyperbolic octagon streets

One shared Grades 3–5 packet: six student pages (five problems plus a loose route-record sheet), with a separate seven-page theorem-first adult guide. Grade labels are approximate: local heading, partner checking and distinguishing street walks from room crossings matter more than arithmetic. No forced K–1 version is included.

## Portable build

With Python 3 and a standard TeX Live/MacTeX installation providing pdfLaTeX, TikZ, amssymb, geometry, enumitem, fancyhdr, hyperref and Helvetica:

    python3 build.py --out output

This reconstructs `week-65-students.pdf` and `week-65-facilitator.pdf` in an isolated temporary directory. No repository, network, external artwork, private books, custom Python packages or absolute project paths are required. The default output folder is `output` under your current directory. Mathematical checks alone can run without TeX:

    python3 build.py --verify-only

`student/build.py` is the editable student-page builder and generates `student/students.tex`. Edit the builder rather than only the generated TeX when changing student text or figures. `guide/facilitator.tex` is the editable adult guide. The independent geometry and route verifiers are in `guide/`. The source package contains original authored assets only; workflow prompts, borrowed style exemplars, downloaded references, old versions and render caches are excluded.

## Use and limits

Print US Letter at 100%, single-sided. A small arrow counter, another coin/counter and pencils are sufficient. The geometry is the genuine hyperbolic {8,4} tiling, with four right-angled octagons at each junction. Streets are geodesics represented by circle arcs, not ordinary Euclidean lines drawn incorrectly. This activity is separate from Week64's Euclidean octagon edge-identification and does not claim to reconstruct the user's remembered seminar.

These activities are prepared and digitally checked, but not physically rehearsed or classroom-piloted. The source notes explain assumptions, source provenance and overlap with earlier themes. Clean ZIP extraction checks compare final text, page sizes and rendered pixels in the production environment; a different TeX/font version can change rendering.
