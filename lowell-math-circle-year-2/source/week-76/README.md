# Week 76: Substitution strips — current editable source

One shared Grades 3–5 packet (4 student pages, F76-35-v2), a 5-page theorem-first adult guide (F76-FAC-v3) and a page of letter tiles (F76-M-v1). Promoted after organizer review on October 15, 2026 (F76-35-v1).

**Revised after the organizer's approval.** The organizer approved the 4-page packet (F76-35-v1) on October 15, 2026. The October 23 revision (v2), from the review card's shoulds and coulds, post-dates that approval and has not been re-approved: Problem 3 asks children to show what settles each claim, Problem 5 says "as in Problem 4", and the guide adds an adult-led K–1 route and a printed tile page. The approved PDFs are in [../../week-76/archive-before-card-fixes-2026-10-23/](../../week-76/archive-before-card-fixes-2026-10-23/README.md); show v2 to the organizer before printing it as the approved packet. Unpiloted; tile handling has not been rehearsed. The print PDFs are in [../../week-76/](../../week-76/).

**Critic follow-up, October 23, 2026 (F76-FAC-v3).** An independent critic found that the guide's print list gave the K–1 route no copies of pages 1–2 and read as one kit for a table of two pairs. The list now names one copy of pages 1–2 for the parent at a K–1 table and says that table's kit is shared by its children, as the route describes. Nothing else changed. The [band-view menu](../../band-views/README.md) now lists the K–1 route's pages 1–2. The previous guide is in `../../week-76/archive-before-critic-fixes-2026-10-23/` and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. Each page is still one TikZ canvas: a problem's `text` sections are its drawing code and `\promptat{y}` places its numbered prompt. The conversion changed no wording or figure, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Review-card fixes, October 23, 2026.** Problem 5 now says "as in Problem 4", so its answer rests on Problem 4's lone-tile rule, and Problem 3 asks children to show what settles each claim (F76-35-v2; pages 1 and 4 change only their footer). The guide (F76-FAC-v2, now 5 pages) adds an adult-led K–1 route on pages 1–2, the Problem 1 matching shortcut for Problem 3, both starting cases for Problem 6, the tile-width gap in the launch, a 38-minute working plan and a Problem 7 readiness check, and its kits use a new page of printed letter tiles (`editable/materials/`). `editable/review/verify_card_fixes_2026_10_23.py` checks the changes in the built PDFs. The replaced print PDFs are in [../../week-76/archive-before-card-fixes-2026-10-23/](../../week-76/archive-before-card-fixes-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-76 --out tmp/week-76-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-76-views lowell-math-circle-year-2/week-76 week-76
  ```

  Week 76 is a shared-packet week, so its one-page menu in [band-views/week-76/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-76.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide and letter tiles:** `editable/guide/facilitator.tex` and `editable/materials/materials.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-76-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-76 --zip ../week-76-source.zip --top week-76
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-76/` folder. The print copies (students, guide and tiles) in `../../week-76/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/frontier-prototypes-76-78/week-76/](../../../plans/frontier-prototypes-76-78/week-76/) and the review card in [plans/review/week-76.md](../../../plans/review/week-76.md).
