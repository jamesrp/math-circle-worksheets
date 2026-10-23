# Week 52: Hinged frames and braces — current editable source

One shared student packet (12 pages, F52-S-v3: pages headed K–1, Grades K–3, Grades 3–5 and Grades 4–5) and a 10-page theorem-first adult guide (F52-FAC-v4). Unpiloted; the bar-and-pin kits have not been built or handled in a session. The print PDFs are in [../../week-52/](../../week-52/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`, in the flow layout. Each page's first file opens with the `\band{...}` line that names that page's grade range. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections. The rebuilt packet matches the old source's build in pages, extracted text and 100-dpi pixels; the print copy, compiled with TeX Live 2025 (pdfTeX 1.40.27), differs from both builds by the same few glyph pixels (at most 166 on a page at 100 dpi). The hand-written `students.tex` and the October 4 ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-52 --out tmp/week-52-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-52-views lowell-math-circle-year-2/week-52 week-52
  ```

  Week 52 is a shared-packet week, so its band slices and one-page menu in [band-views/week-52/](../../band-views/README.md) are built from the page index `../band-views/indexes/week-52.toml` by `band_views.py build`; update the index when a page's grade range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-52-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-52 --zip ../week-52-source.zip --top week-52
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-52/build.py --out rebuilt`.

**Card fixes, October 23, 2026 (v3).** From the review card: pages 3–4 are headed Grades K–3, and the guide gives each K–1 pair its own 2-by-2 kit and routes K–1 through Problems 4–5 after Problem 3 (kits now 108 side bars, 35 braces, 90 pins); Problem 13 says "braces in six different cells, with a brace in every row and column". The frame rules now open pages 3, 5 and 10 (the new setup files `08-upper-rules.md` and `16-return-rules.md`; problem files renumbered, printed problem numbers unchanged), page 1 no longer narrates the drawings and its square uses the triangle's bar length, and Problem 14 has two boards. The guide's launch, stock test, print plan, handoff and Problem 13 key were revised. `plans/review/checks/week-52/check_card_fixes.py` checks the counts, the claims and the printed pages. The previous PDFs and the conversion ZIP are in `archive-before-card-fixes-2026-10-23/` folders beside the current files.

**Critic follow-up, October 23, 2026 (F52-FAC-v4).** An independent critic found the guide's page 4 handoff asking aloud "Can you brace it so every row and column has a brace but it still changes shape?", which is Problem 8's question. The handoff now asks "Use three braces so that every row and every column has one. Does it hold?" (children still find one of the six designs and test it), and the Problem 8 key says a child may cite that 2-by-3 as a counterexample, leaving the A/B link contrast as the work. Guide pages 4 and 6 changed; the student packet did not. `plans/review/checks/week-52/check_critic_fixes.py` checks the designs and the wording. The previous guide is in `../../week-52/archive-before-critic-fixes-2026-10-23/` and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md).

The research and review record is in [plans/new-themes-52-63/week-52/](../../../plans/new-themes-52-63/week-52/) and the review card in [plans/review/week-52.md](../../../plans/review/week-52.md).
