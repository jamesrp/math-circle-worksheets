# Week 72: A robot that remembers area — current editable source

One shared Grades 4–5 packet (5 student pages, GGT72-S-v2) and a 3-page theorem-first adult guide (GGT72-FAC-v2). Unpiloted; the cut-out strip, cards and markers have not been rehearsed. The print PDFs are in [../../week-72/](../../week-72/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026** (GGT72-S-v2, GGT72-FAC-v2). Made in the problem files after the conversion, from the review card's should-fixes and clear coulds: Problem 3 adds a 2-by-2 square outline (8 cards like the L, but memory 4) and prints a turn arrow before each blank instead of asking for one; Problem 2 has six answer lines; page 1 drops two facilitation phrases and the arrowhead under the start panel's dot; page 5 drops "Extra workspace for every problem." Page 4 changed only in the footer. The guide's launch now shows N and S on column −2 with the marker reading, the Problem 1 key reads each memory as the squares left of the route, the Problem 3 key adds the square and the rival rule "half the cards minus one", and the materials count page 5 once; `editable/MATHEMATICS.md` no longer cites a missing `topics.json`. Could 9 (a new fifth problem) is left for the organizer. Checked by `plans/review/checks/week-72/check_card_fixes.py`. The replaced PDFs are in [../../week-72/archive-before-card-fixes-2026-10-23/](../../week-72/archive-before-card-fixes-2026-10-23/README.md) and the conversion's ZIP in `../archive-before-card-fixes-2026-10-23/week-72-source.zip` (SHA-256 `4d9505fe2f53d48ffcb20a4a126b82893f503aa92e030a84aeed2b1e41c6e91c`).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-72 --out tmp/week-72-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-72-views lowell-math-circle-year-2/week-72 week-72
  ```

  Week 72 is a shared-packet week, so its one-page menu in [band-views/week-72/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-72.toml` by `band_views.py build`; update the index when a problem moves to another page or the footer changes.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-72-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-72 --zip ../week-72-source.zip --top week-72
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-72/` folder. The print copies in `../../week-72/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/ggt-prototypes-66-75/week-72/](../../../plans/ggt-prototypes-66-75/week-72/) and the review card in [plans/review/week-72.md](../../../plans/review/week-72.md).
