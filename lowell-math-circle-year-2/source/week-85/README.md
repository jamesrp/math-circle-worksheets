# Week 85: Drawing machines — current editable source

Two student packets, shared Grades 2–5 (4 pages, W85-S-v2) and upper Grades 4–5 (4 pages, W85-U-v2, the return visit), a 10-page materials packet (W85-M-v3) and a 6-page theorem-first adult guide (W85-F-v3). Unpiloted; no pantograph has been built, and the guide's rehearsal has not been done. The print PDFs are in [../../week-85/](../../week-85/).

**Critic follow-up, October 23, 2026 (W85-M-v3, W85-F-v3).** An independent critic found that the red pencil at P sat in one 5 mm foam layer and could tilt 2–3 mm off its pivot. Materials pages 1–2 and the guide now glue an 18 by 25 mm offcut on the P end so the pencil goes through two layers, as at T; make the O hole with the pin; give the fasteners a length (20–25 mm); clip the binder clip to the pencil; push the pin in after the mat is down; and add a rehearsal check that pushes each pencil sideways. The guide's account of what stops full stretch and collapse now names the strips that meet first. `plans/review/checks/week-85/check_critic_fixes.py` models the build and checks each number. The student packets did not change. The previous materials, guide and ZIP are in `archive-before-critic-fixes-2026-10-23/` folders. Still unbuilt and unrehearsed.

**Review-card fixes, October 23, 2026 (v2).** Materials page 2 and the guide now name one build: 5 mm foam-board strips cut on the page 1 template, brass fasteners at X, Q and Y, a pushpin at O into a foam-board base, and the two pencils pushed through the T and P holes as their joints' axles, with parts, rough cost ($25–40 for three machines) and time. They also name a sturdier hardboard-and-bolts variant and a fallback, a bought pantograph set to 2. This build is unbuilt and unrehearsed: the costs and times are estimates, and the guide's rehearsal must come first. Overlays are tracing paper, since pencil barely marks clear film. Shared Problem 4 now asks where T can go while P stays in F's box; the shared and upper opening rules carry "Keep O fixed. Move T; P draws.", upper Problem 3 takes in its page's opening line, and upper Problem 4 loses its repeated line and dashed frame. The guide adds a K–1 route, the Problem 4 key, the fold and collapse poses, and suggested timings. The previous PDFs are in [../../week-85/archive-before-card-fixes-2026-10-23/](../../week-85/archive-before-card-fixes-2026-10-23/README.md).

**Problem files, October 23, 2026.** The student packets are stored as [problem files](../problem-files/README.md): `week.toml`, `figures.py` (the old generator's drawing code, page template and materials pages, unchanged) and one file per problem in `problems/`. The two packets are the week's two bands. The conversion (before the v2 fixes) changed no wording or drawing: the LaTeX of the shared, upper and materials packets is byte-identical to the old generator's, and the package build gives byte-identical PDFs. The print copies were compiled with a newer pdfTeX (1.40.27), so a rebuild here, by the old builder or the new, differs from them only in glyph rasters (at most 35 pixels on a page at 100 dpi). The old generator and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md` (drawings in `figures.py`), then build every view:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-85 --out tmp/week-85-views --tex --publish lowell-math-circle-year-2/band-views/week-85
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-85-views lowell-math-circle-year-2/week-85 week-85
  python3 lowell-math-circle-year-2/source/band-views/band_views.py readme
  ```

  The first-route packet (shared), the return packet (upper), the one-page problem menu and the key view are published in [band-views/week-85/](../../band-views/README.md#weeks-stored-as-problem-files).
- **Materials and adult guide:** the materials pages are drawn by `materials_tex()` in `figures.py`; the guide's source is `editable/guide/facilitator.tex`. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (README, mathematical checks, guide source, reference PDFs). `editable/student/build.py` writes the student and materials LaTeX from the problem files, and `editable/build.py` builds all four PDFs. The [portable source ZIP](../week-85-source.zip) holds the package plus the problem files and tools in `problem-files/`, written by `package.py`:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-85 --zip ../week-85-source.zip --top week-85
  ```

  Check a clean rebuild from the extracted ZIP with `python3 week-85/build.py --out rebuilt --work tmp/build`.

Read `editable/README.md` for printing, dependencies and evidence. The production record is in [plans/seven-families-85-91/production/](../../../plans/seven-families-85-91/production/STATUS.md) and the review card in [plans/review/week-85.md](../../../plans/review/week-85.md).
