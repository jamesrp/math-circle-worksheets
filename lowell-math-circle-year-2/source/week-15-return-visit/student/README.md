# Week 15 return visit: portable student-page source

This is revised draft material, unpiloted and not physically rehearsed. It contains one shared collection, not three parallel grade-band packets. The three investigations are farthest straight-line ownership, grid-step nearest-site ties, and maximizing distance to a nearest existing site.

## Build

Requires a TeX distribution with pdfLaTeX, TikZ/PGF, geometry, fancyhdr, array, Helvetica, and T1 font support. No external assets, absolute source paths, generated diagrams, or Python packages are needed to build the PDF.

From any folder, run `sh /path/to/src/build.sh /path/to/output`. With no argument, output goes in the source folder's parent. The build script uses `pdflatex` on PATH, falls back to the standard macOS TeX location, or accepts `PDFLATEX=/path/to/pdflatex`. The delivered file is `return-visit.pdf`; build intermediates go in `output/build/`.

Print on single-sided US Letter at actual size (100%). All main maps and squares are 4.5 inches across with equal horizontal and vertical scales. Proposed materials are pencil, ruler, 12-inch nonstretch string, and tracing paper. Physical stock and measurement procedures have not been tested.

## Page and problem map

1. Problem 1, Grades K-1 and up: compare straight-line distances from chosen places to four square-corner dots and a center dot; mark farthest owners and ties, considering the entire plane.
2. Problem 2, Grades 2-3 and up: a worked fractional P-to-Q grid-step convention precedes a large A/B map; investigate nearest ownership, extended tie areas, and tied endpoints with an untied midpoint. Routes are horizontal/vertical and can start anywhere, including square interiors. A fraction of an edge counts as that fraction of a step; distance is shortest route length. The non-task example starts P at (0.5, 0.5), ends Q at (3, 1), and uses 2.5 horizontal plus 0.5 vertical steps, totaling 3.
3. Problem 3, Grades 4-5: maximize the distance to the nearest of four corner sites inside or on a square; provide a bound/explanation and all maximizing places.
4. Problem 4, Grades 4-5: revisit the same bounded square with its center added as a site, and find every maximizing place.

The source, package names, and mathematical checks are supporting materials for review, not a facilitator guide. The repository base worksheets, base guide, indexes, and remote copies have not been changed.

## Optional digital checks

`python3 verify.py /path/to/return-visit.pdf /path/to/render` requires PyMuPDF. It checks the four pages, the main map dimensions and actual site coordinates extracted from PDF vector paths, the route example, the tie and farthest comparisons, and the bounded clearance cases. It renders all pages and writes a JSON evidence report. It does not establish classroom fit or physical readiness.
