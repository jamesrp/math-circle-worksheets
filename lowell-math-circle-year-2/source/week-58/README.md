# Week 58: Fair division with different values — current editable source

One shared student packet (7 pages, W58-shared-v4: Grades K–5 pages 1 and 5, Grades 2–5 pages 2 and 3, Grades 3–5 pages 4, 6 and 7), an 8-page materials file of goods, preference cards, panels and whole 240 mm strips (W58-materials-v3) and a 9-page theorem-first adult guide (W58-guide-v4). Later on October 23, 2026 the guide's roster code "KK11", "3333", "445" became the band labels "K–1", "2–3", "4–5" (W58-guide-v4); the previous guide and ZIP are in the `archive-before-roster-label-fix-2026-10-23/` folders. Unpiloted; card, strip and cutting handling are physically unrehearsed. The print PDFs are in [../../week-58/](../../week-58/).

**Critic follow-up, October 23, 2026 (W58-shared-v4, W58-guide-v3).** An independent critic noted that Problem 5, on a page headed Grades K–5, asked for a division "so neither person envies the other", while envy is defined only on page 2, which the K–1 route does not use. It now asks for a division "so that neither person would rather have the other's cards" and ends "Can you now make such a division?". The guide's K–1 route names pages 1 and 5 only and does Problem 2's two color splits with the cards, matching its print list and the K–1 band slice. Only page 5 changed above the footer; the materials did not change. `plans/review/checks/week-58/check_critic_fixes.py` checks it. The v3 PDFs and ZIP are in `archive-before-critic-fixes-2026-10-23/` folders.

**Review-card fixes, October 23, 2026.** The [review card](../../../plans/review/week-58.md)'s six shoulds and coulds 11–13: pages 1 and 5 are headed Grades K–5, and the guide's KK11 table becomes an adult-led K–1 route on pages 1, 2 and 5 with a plain-words key; Problem 2 asks for every way to give all four cards to A and B so that neither envies the other; the guide's Visit A names the all-red / blue partition; Problem 7's observer boxes and the Problem 2 and 6 tables are gone (Problem 6 gets three empty boxes for the envy-free division); the materials print whole 240 × 40 mm strips with 120 mm panels, so cuts move to 80 and 160 mm and nothing is taped; page 3's launch is 120 → 60 + 60 with outputs as wide as the halves; the guide says "at least one third"; Problem 1 prints five record boxes. Coulds 7–10 (reordering Problem 4, moving Problem 5, asking for every envy-free Problem 6 division, relabelling the three-person observers) are left. The replaced PDFs are in [../../week-58/archive-before-card-fixes-2026-10-23/](../../week-58/archive-before-card-fixes-2026-10-23/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the head of the old `students.tex`, with `common.tex`'s definitions written out) and one file per problem in `problems/`, in the flow layout. This is a shared-packet week: `week.toml` defines one band, `shared`, whose packet is `week-58-students.pdf`, and each page's header range is set by `\newband` in the text that opens the page. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by the written-out preamble and three blank lines between sections. The rebuilt packet matches the old builder's in pages, extracted text and 100-dpi pixels; against the print copy, compiled with a newer pdfTeX (1.40.27), the old and new builders both differ by the same small pixel counts. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-58 --out tmp/week-58-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-58-views lowell-math-circle-year-2/week-58 week-58
  ```

  The build also writes a first-route and a return packet, a one-page problem menu and a key view into `tmp/`; they are not published. The published views of this week are its band slices and page menu in [band-views/week-58/](../../band-views/README.md), built from the page index `../band-views/indexes/week-58.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide and materials:** `editable/guide/guide.tex` and `editable/student/materials.tex` (with `editable/student/common.tex`), built by the package.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files, and the package `build.py` runs it before compiling. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-58-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-58 --zip ../week-58-source.zip --top week-58
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-58/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-58/](../../../plans/new-themes-52-63/week-58/outline.md) and the review card in [plans/review/week-58.md](../../../plans/review/week-58.md).
