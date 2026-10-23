# Week 81: Buckets of Fish — current editable source

One shared student packet (5 pages, W81-S-draft-v1) and a 4-page theorem-first adult guide. Organizer-approved and promoted October 17, 2026. Unpiloted. The print PDFs are in [../../week-81/](../../week-81/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem or material page in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print copy in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-81 --out tmp/week-81-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-81-views lowell-math-circle-year-2/week-81 week-81
  ```

  Week 81 is a shared-packet week, so its band slices and one-page menu in [band-views/week-81/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-81.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first, then the mathematical checker. The [portable source ZIP](../week-81-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-81 --zip ../week-81-source.zip --top week-81
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-81/build.py --out rebuilt --work tmp/build`.

The research and review record is in [plans/infinity-prototypes-79-84/](../../../plans/infinity-prototypes-79-84/README.md) and the review card in [plans/review/week-81.md](../../../plans/review/week-81.md).
