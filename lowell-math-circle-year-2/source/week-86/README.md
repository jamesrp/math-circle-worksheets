# Week 86 Pursuit and escape: editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code, page template and materials pages, unchanged) and one file per problem in `problems/`. The two packets are the week's two bands: the shared Grades 2–5 packet and the upper Grades 4–5 packet, whose Problem 1 is the same file as the shared Problem 1. The conversion changed no wording or drawing: the LaTeX of both packets and of the materials is byte-identical to the previous builder's, and every PDF matches a rebuild by the previous builder in exact 100-dpi pixels. The print copies were compiled with a newer pdfTeX (1.40.27) than this project's TeX Live (1.40.25), so a rebuild here, by the old builder or the new, has the same text and drawings with slightly different glyph rasters (at most 42 differing pixels on a page at 100 dpi). The previous builder and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/).

- **Student pages:** edit `problems/*.md` (boards in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-86 --out tmp/week-86-views --tex --publish lowell-math-circle-year-2/band-views/week-86
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-86-views lowell-math-circle-year-2/week-86 week-86
  ```

  The first-route and return packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-86/](../../band-views/README.md#weeks-stored-as-problem-files). The routes follow the guide: the shared packet is the first visit; the upper packet's Problem 1 is its stand-alone entry and Problems 2–6 are return visits.
- **Materials and adult guide:** the materials pages are drawn by `materials_tex()` in `figures.py`; the guide's source is `editable/guide/facilitator.tex`. The problem files' `key` sections and `guide/overview.tex` repeat the guide's answer keys and overview for the key view; `python3 lowell-math-circle-year-2/source/week-86/check_guide_copy.py` checks that every copied sentence is still in the guide source. Change both together.
- **Portable package:** `editable/` is the package (README, mathematical checks, guide source, reference PDFs). `editable/student/build.py` writes the student and materials LaTeX from the problem files, and `editable/build.py` builds all four PDFs. The [portable source ZIP](../week-86-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-86 --zip ../week-86-source.zip --top week-86
  ```

Read `editable/README.md` for printing, dependencies and evidence. Current print copies are in [../../week-86/](../../week-86/). The week is unpiloted; counters, turn tiles and fold covers are physically unrehearsed.
