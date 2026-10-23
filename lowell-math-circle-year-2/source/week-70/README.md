# Week 70: Four shields in a portal room — current editable source

One shared Grades 4–5 packet (4 student pages, GGT70-S-v2) and a 3-page theorem-first adult guide (GGT70-FAC-v3). Unpiloted; no physical rehearsal has been performed. The print PDFs are in [../../week-70/](../../week-70/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and the rebuilt packet matches the print PDF with identical text and no differing pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card shoulds, October 23, 2026** (GGT70-S-v2, GGT70-FAC-v2), made in the problem files after the conversion. Problem 1 is one large room with the four diagonal shots and two drawn portal shots, toward the copies (2,6) and (6,2): the fewest shields is still 4, but (1,3) and (3,1) are forced, and a shield where the drawn shots cross leads to 5. "Swap jobs" is gone. Page 1's rules say a shield is a pencil cross, that "a shield stops a shot only if the shot passes exactly through that point", and that each large square of a map is a copy of the room with every T the same target; page 2 lost its narrating paragraph, its map and room are larger (1 cm a unit), its four target copies are lettered A–D, and it says "an X or Y edge". Page 3's map is at the room's scale (1.05 cm a unit) with no small room, and shields go in the bold room. The launch picture's "start" labels sit below the dots. The guide adds a tracing square that carries the crosses from copy to copy, clear centre-dot counters as the only counters, about 5 minutes for Problem 1 with its forced shields, the map's unique answer, an extension (shots back to S need the three shields (2,0), (0,2), (2,2)) and an untested 2–3 route. `checks/verify_kernels.py` now reduces each aimed lift to its first T before testing the midpoint, and `editable/guide/check_math.py` checks each changed claim and the printed wording. Problem numbers and pages are unchanged. The previous PDFs are in [../../week-70/archive-before-card-fixes-2026-10-23/](../../week-70/archive-before-card-fixes-2026-10-23/) and the conversion's ZIP in [../archive-before-card-fixes-2026-10-23/](../archive-before-card-fixes-2026-10-23/). Unpiloted; the tracing square has not been rehearsed.

**Critic follow-up, October 23, 2026 (GGT70-FAC-v3).** An independent critic noted that the guide's possible Grades 2–3 route was "Problem 1 alone", a problem the same guide budgets at about 5 minutes. The route now continues to Problem 2's shots A–C, aimed with a ruler at the letters on the map without reading coordinates (A and B are Problem 1's drawn shots unfolded; C stops at the room's own T), about 15–20 minutes in all. The student packet is unchanged (GGT70-S-v2). `editable/guide/check_math.py` checks the new wording. The v2 guide is in [../../week-70/archive-before-critic-fixes-2026-10-23/](../../week-70/archive-before-critic-fixes-2026-10-23/) and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-70 --out tmp/week-70-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-70-views lowell-math-circle-year-2/week-70 week-70
  ```

  Week 70 is a shared-packet week, so its one-page menu in [band-views/week-70/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-70.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide:** `editable/guide/facilitator.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`, which keeps the week's earlier release notes); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-70-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-70 --zip ../week-70-source.zip --top week-70
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-70/` folder. `editable/reference-pdfs/` holds copies of the print PDFs.

The review and research record is in [plans/ggt-prototypes-66-75/week-70/](../../../plans/ggt-prototypes-66-75/week-70/) and the review card in [plans/review/week-70.md](../../../plans/review/week-70.md).
