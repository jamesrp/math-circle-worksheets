# Week 87 Voting and agendas: editable source

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old builder's drawing code, page template and materials pages, unchanged) and one file per problem in `problems/`. The three packets are the week's three bands: the card packet (Grades 2–5), the line packet (Grades 3–5) and the upper packet (Grades 4–5), each numbered from 1. The conversion changed no wording or drawing: the LaTeX of the three packets and of the materials is byte-identical to the previous builder's, and every PDF built by `editable/build.py` is byte-identical to a rebuild by the previous builder. The print copies were compiled with a newer pdfTeX (1.40.27) than this project's TeX Live (1.40.25), so a rebuild here, by the old builder or the new, has the same text and drawings with slightly different glyph rasters (at most 24 differing pixels on a student page at 100 dpi; the materials pages match exactly). The previous builder and source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/).

- **Student pages:** edit `problems/*.md` (cards, number lines and tallies in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-87 --out tmp/week-87-views --tex --publish lowell-math-circle-year-2/band-views/week-87
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-87-views lowell-math-circle-year-2/week-87 week-87
  ```

  The route packets, the one-page problem menu and the key arranged by problem are published in [band-views/week-87/](../../band-views/README.md#weeks-stored-as-problem-files). The routes follow the guide: the card packet is a first visit; the line packet's Problems 1–3 are a separate first visit and its Problem 4 a return; the upper packet is return work.
- **Materials and adult guide:** the materials pages are drawn by `materials_tex()` in `figures.py`; the guide's source is `editable/guide/facilitator.tex`. The problem files' `key` sections and `guide/overview.tex` repeat the guide's answer keys and overview for the key view; `python3 lowell-math-circle-year-2/source/week-87/check_guide_copy.py` checks that every copied sentence is still in the guide source. Change both together.
- **Portable package:** `editable/` is the package (README, mathematical checks, guide source, reference PDFs). `editable/student/build.py` writes the student and materials LaTeX from the problem files, and `editable/build.py` builds all five PDFs. The [portable source ZIP](../week-87-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-87 --zip ../week-87-source.zip --top week-87
  ```

Read `editable/README.md` for printing, dependencies and evidence. Current print copies are in [../../week-87/](../../week-87/). The week is unpiloted; cutting, token fit, resets and timing are physically unrehearsed.
