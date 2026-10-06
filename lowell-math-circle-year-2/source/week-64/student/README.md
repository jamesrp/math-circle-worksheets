# Week 64 student packet source

Newly authored, unpiloted nine-page Grades 3–5 packet. Pages 7–9 carry readiness-dependent Grades 4–5 labels. The build produces `../students.pdf`.

## Build

Requirements: Python 3 (standard library), pdfLaTeX, PGF/TikZ and the standard Computer Modern fonts. Run from this directory:

```sh
./build.sh
python3 verify.py > ../verification.json
```

`generate.py` writes the fully editable `students.tex`. The build places temporary TeX files in `../build/` and copies the compiled PDF to `../students.pdf`. No local absolute paths are embedded in the builder. In an environment that needs custom TeX search paths, configure its TeX environment before running this command.

To render all pages for review, with Poppler installed:

```sh
mkdir -p ../render
pdftoppm -r 90 -png ../students.pdf ../render/page
```

## Print and material facts

Print single-sided on US Letter at 100%, with no fit-to-page scaling. Page 5 contains the essential cutout sectors and a one-inch check bar. All figures use equal x/y scaling. The original octagon coordinates are `(1,a),(a,1),(a,-1),(1,-a),(-1,-a),(-a,-1),(-a,1),(-1,a)`, where `a=1+sqrt(2)`. Working octagons are 3.94 inches across (page 1), 5.35 inches (page 2), and 4.65 inches (page 3). L squares have eighth grids and sides 2.47 inches (page 6), 2.52 inches (pages 7–8), and 2.20 inches (page 9).

Use tracing paper, ruler, colored pencils, paper, scissors, a small counter and a separate direction arrow. Page 3 develops a path across individually numbered, translated tracings. Copies retain separate identities even when paper overlaps. Page 5 sectors model corner neighborhoods; eight octagon sectors cannot occupy one plane without overlap.

## Checks and limits

`verify.py` checks regularity, edge translations, the octagon vertex equivalence class, sector edge/arrow correspondence, all twelve L-corner identifications, and prescribed L trajectories with exact rational arithmetic. Its universal rational-direction comment is a finite-permutation argument, not an inference from examples.

Digital geometry, compilation and page rendering do not establish material fit or classroom readiness; neither a physical print rehearsal nor a classroom pilot has been completed.

## Provenance

All student wording and drawings are newly authored. The mathematical background is documented in the companion guide and its `PROVENANCE.md`, with these primary references:

- Alex Wright, [From Rational Billiards to Dynamics on Moduli Spaces](https://public.websites.umich.edu/~alexmw/BilliardsToModuli.pdf), pp. 3–6: regular octagon, translation gluing, cone angle and genus.
- The [official surface-dynamics square-tiled-surface documentation](https://flatsurf.github.io/surface-dynamics/examples/square_tiled_surfaces.html), including `Origami('(1,2)','(1,3)')`.
- Giovanni Forni and Carlos Matheus, [Introduction to Teichmüller Theory and Its Applications to Dynamics of Interval Exchange Transformations, Flows on Surfaces and Billiards](https://www.math.uchicago.edu/~masur/gm.pdf), pp. 17–18 and 78: the three-square L and its translation structure.

The particular starting points, exercises and figures are newly written around established mathematics; novel mathematical results are not claimed.

No third-party book pages, borrowed worksheets, or other source pages are included in the student PDF or editable sources.
