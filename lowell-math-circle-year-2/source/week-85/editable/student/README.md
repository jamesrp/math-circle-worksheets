# Week 85 revised source

Revised student and material pages; no facilitator guide is included. The run-folder critic and independent mathematical reviews informed this revision. Shared Grades 2–5 and upper Grades 4–5 packets replace the generic three-band request according to the outline. No independent K–1 route is claimed.

Build all three self-contained PDFs:

```sh
python3 build.py --out .. --work ../build
```

Requires Python 3 and pdfLaTeX with TikZ, geometry, T1 fonts and Latin Modern. The builder uses PATH or the standard macOS TeX location. Sources require no repository assets. Since October 23, 2026 the pages are stored as problem files: `build.py` writes the `.tex` files from `week.toml`, `figures.py` and `problems/` (beside this package in the repository, `problem-files/` in the ZIP) into its work folder; edit those, not generated `.tex`. Fixed `SOURCE_DATE_EPOCH`, omitted PDF dates and empty trailer IDs make rebuilds deterministic. `check_math.py` checks ideal mechanism lengths, target bounds, areas and the anchor translation. It is not a physical test.

Print the materials at actual size. They include four bar templates, a topology/setup page, two nominal 432×279 mm joined-mat sheets, a seam bridge, thirteen inserts A–M, 48 ten-millimeter squares and 16 half-square triangles. Rigid bar stock, pivot hardware, spacers, coaxial tip mounts, a board, clear overlays, ruler, straightedge and tape must be supplied. Exact mount engineering and physical support, branch-control and hand-clearance rehearsal remain untested. The bridge fills ordinary nonprinting margins at the mat seam without reducing the two-sheet dimensions.

Operation examples show three genuine poses and visible partial/completed strokes. All A–M identifiers sit inside cut borders; G/H/I use the supplied area pieces without a printed grid. F and L refer explicitly to their small solid target outlines.

The shared packet leaves the doubling rule for discovery. The upper packet offers four separate return investigations; it does not imply completion within one meeting. The material output is a printable prototype and does not establish classroom readiness.
