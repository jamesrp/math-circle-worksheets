# Week 88: Packing and kissing circles

One shared Grades K–5 menu, selected by prerequisites. Optional K–1 touch/fit entry; Grades 2–3 constructions; Grades 4–5 center-distance proofs and readiness-dependent return visits. The late size formula uses trigonometry as adult background. This is a library investigation, not an adopted meeting schedule. **Unpiloted; physical rehearsal, circle accuracy, printing and handling remain untested.**

## Rebuild

Requires Python 3.11 or later (standard library) and TeX Live/pdfLaTeX with TikZ, geometry, fancyhdr, lmodern, amsmath, amssymb, array, booktabs and hyperref. No network, private reference, external font or image asset is needed.

```sh
python3 build.py --out ../../../week-88
```

From an extracted portable ZIP:

```sh
python3 week-88/build.py --out rebuilt --work tmp/build
```

The builder runs independent mathematical checks, builds deterministically, rejects TeX errors and overfull boxes, and keeps intermediates in repository `tmp/` or the supplied folder. The student pages are stored as problem files (October 23, 2026): edit `problem-files/problems/*.md` in the ZIP, or `lowell-math-circle-year-2/source/week-88/problems/` in the repository. `student/regenerate.py` writes `student/students.tex` from them with the problem-file tools, and the build runs it first; the separately authored theorem-first guide is in `guide/`. Current reference PDFs are packaged for comparison. See [QA.md](QA.md) for actual review and reconstruction evidence, and [SOURCES.md](SOURCES.md) for provenance and prior-use distinctions.

Print US Letter, single-sided, Actual Size. The practical tray is 160×112 mm inside; exact later trays are 160×110 and 160×108 mm. Do not scale a larger ring mat to fit a page: use a separate desk surface at least 260×260 mm. Measure actual disks and printed interiors before classroom use. A digital fit does not certify physical tolerances.

The portable ZIP includes only owned editable sources, check/build scripts, documentation and current reference PDFs. It excludes generated stage prompts, borrowed workflow examples, whole downloaded papers/books, render/build caches and private records. No Drive upload is implied.
