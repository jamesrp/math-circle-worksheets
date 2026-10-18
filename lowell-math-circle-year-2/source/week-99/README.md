# Week 99: Moving piles with the least work

Prepared for organizer review. Unpiloted; printing, preparation, material handling, adult procedures and timing have not been physically rehearsed. This family has Grades 2–3 and Grades 4–5, selected by prerequisites rather than forced K–5 coverage. No K–1 packet is claimed. Entry: counting small piles and counter-steps while keeping a fixed target visible. Later work adds unavoidable-crossing certificates, position totals and comparisons between whole arrangements. Ordinary adult reading or recording is supported; children should retain the mathematical choices. The guide gives a manageable first visit and later routes rather than requiring every page in one hour.

## Rebuild

Requires Python 3 and a configured TeX Live/pdfLaTeX installation with TikZ, geometry, fancyhdr, lmodern, amsmath, amssymb, array, booktabs, hyperref and the standard article/extarticle classes. Week 99 also requires pypdf to assemble its mixed-orientation student packets. No private reference, external image, nonstandard font or network download is needed by the builder.

From this source folder:

```sh
python3 build.py --out ../../week-99
```

From an extracted source ZIP:

```sh
python3 week-99/build.py --out rebuilt --work tmp/build
```

`build.py` runs the independent mathematical checks, rejects TeX errors and overfull boxes, and builds the targets listed in `build-targets.json`. Intermediates go to repository `tmp/` or the supplied work directory. The source files omit volatile PDF dates/IDs; the build fixes SOURCE_DATE_EPOCH for reproducibility. A normal TeX installation must have its format and font-map configuration in place. The cloud verification used the already installed TeX files with a local runtime configuration; no machine-specific cache is packaged.

## Editable contents

- `student/*.tex`: canonical final student source, from fresh writer, critic, mathematical review and reviser stages. Edit these files directly; there is no stale parallel generator to overwrite changes.
- `guide/facilitator.tex` and `guide/solutions.tex`: separately authored theorem-first adult guide. Guide authoring is an untested addition to the tested student workflow.
- `check_math.py`: independent standard-library finite checks. It prints its results without changing the source tree.
- `build.py` and `build-targets.json`: portable build entry point and exact output list.
- `reference-pdfs/`: current verified PDFs for comparison.
- `QA.md` and `SOURCES.md`: verification, status, scholarly sources and precise overlap boundaries.

The adjacent source ZIP contains the same owned editables and reference PDFs. Generated workflow prompts, borrowed style excerpts, raw session traces, build caches and downloaded works are excluded. Print US Letter single-sided at Actual Size. Keep facilitator pages separate. The guide identifies any separate reusable workmat and extra cutting copies needed for the small student reference diagrams.
