# Week 55: Few sums and equal spacing — current editable source

One student packet (10 landscape pages, W55-S-v3, all headed Grades 3–5, Problems 1–10) and a 9-page theorem-first adult guide (W55-F-v3; W55-S-v2 and W55-F-v1 before the October 23 card fixes), with an adult-led K–1 route on guide p. 2. Unpiloted; kit fit, handling and the launch are unrehearsed. The print PDFs are in [../../week-55/](../../week-55/). Later on October 23 the guide became W55-F-v3: it names the fixed tables "K–1 / 2–3 / 4–5" where it printed the roster code "KK11 / 3333 / 445" (K, K, 1, 1 / four third graders / 4, 4, 5); W55-F-v2 is in `archive-before-roster-label-fix-2026-10-23/` beside the print copy.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old `students.tex` preamble as the page template) and one file per problem or shared rule in `problems/`, in the canvas layout. Prompts are placed with `## prompt @y`, and the TikZ drawing code is copied as written. The conversion changed no wording or figure: in this container the rebuilt packet is byte-identical to the old `students.tex` compiled with the same TeX. Against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 193 on a page at 100 dpi) and the same `pdftotext -layout` spacing; pages and the words on each page are identical. The hand-written `students.tex` and the October 4 source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made after the conversion, from the review card ([plans/review/week-55.md](../../../plans/review/week-55.md)). Student pages: the p. 1 rule reads "No number repeats within an input; A and B may share numbers.", so Problem 5 keeps its seven answers; on p. 8 every grid segment is drawn before the dots, so no line crosses a number; Problem 10 asks the easier converse first. Guide: an adult-led K–1 route on student pp. 1–3 with dot cards 0–6, the parent reading and supplying facts (Problems 1 and 2, then Problem 3's "as few" half with cards 0–5), a plain-words key and kit counts, in place of the Week 1 tiling boards; a print set with pp. 4–5 for each third-grade pair; spoken follow-ups for Problems 3 (four cards each: fewest 7, most 16 only with {0, 1, 8, 9} and a gap-2 run) and 6 ({0, 2, 4} + {0, 3, 6}, 9 totals). Coulds 4 and 5, which would change Problem 3's card count and Problem 6's examples, are left for the organizer and given aloud in the guide instead; the pages keep their Grades 3–5 headers. Changed pages: students pp. 1, 8 and 10; guide pp. 1–5 and 8; the other pages are pixel-identical to the previous build. `editable/review/check_card_fixes_2026_10_23.py` checks the rule's effect, the K–1 key, the spoken variants and Problem 10's claim; `editable/review/check_pdf.py` reads the wording and the p. 8 paint order from the PDFs; the package's own `student/verify_pdf.py` and `guide/verify.py` still pass. The previous print copies are in [../../week-55/archive-before-card-fixes-2026-10-23/](../../week-55/archive-before-card-fixes-2026-10-23/README.md). Unpiloted; the K–1 route and dot cards are physically unrehearsed.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-55 --out tmp/week-55-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-55-views lowell-math-circle-year-2/week-55 week-55
  ```

  The build also writes a first-route packet, a one-page problem menu and a key view into `tmp/`; they are not published. Week 55 is a shared-packet week, so its page menu in [band-views/week-55/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-55.toml` by `band_views.py build`; update the index when a page's header range or problems change.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package `build.py` runs it first. `editable/reference-pdfs/` holds copies of the print PDFs. The [portable source ZIP](../week-55-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-55 --zip ../week-55-source.zip --top week-55
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-55/build.py --out rebuilt`.

The research and review record is in [plans/new-themes-52-63/week-55/](../../../plans/new-themes-52-63/week-55/outline.md) and the review card in [plans/review/week-55.md](../../../plans/review/week-55.md).
