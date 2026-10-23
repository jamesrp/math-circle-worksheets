# Week 13 return visits

**Roster labels, October 23, 2026 (RV-13-FAC-v2).** The adult guide printed the roster code "KK11 / 3333 / 445" (K, K, 1, 1 / four third graders / 4, 4, 5) on page 2, where readers expect band labels; it now prints "K–1 / 2–3 / 4–5". Nothing else changed in the words; the guide was rebuilt with pdfTeX 1.40.25 (the October 4 copy used 1.40.27), so glyph edges drift by a few pixels on every page. The previous guide and ZIP are in the `archive-before-roster-label-fix-2026-10-23/` folders beside the current copies. Checked by `plans/review/checks/roster-labels/check_roster_labels.py`. Unpiloted.

Three investigations within the Week 13 theme. Separate draft/unpiloted companions; existing base packets and guides are untouched. Readiness is labeled on each student page; the adult guide states prerequisites, precise facts, assumptions, materials, a common launch, first routes, flexible return-visit pacing, solutions, hints and extensions. Physical counter fit, preparation stock, procedures and classroom response are untested.

- Student: `../../week-13/week-13-return-visit.pdf`
- Adult: `../../week-13/week-13-return-visit-facilitator.pdf`

## Clean build

Requires Python3 standard library and pdfLaTeX with ordinary LaTeX packages including TikZ, extarticle, Helvetica, fancyhdr, geometry and amsmath. No Python packages, fonts or assets outside this folder are needed to build.

From this folder: `sh build.sh /absolute/output/directory`. Without an argument, a fresh system-temporary output folder is used and printed. This never copies into printable week folders or overwrites base files. In the repository, use a folder under `tmp/`.

Editable student sources are in `student/`; `facilitator.tex` is the editable adult guide. `independent_checks.py 13` recomputes the finite audit and writes local JSON. `workflow/` preserves the generated writer, critic, math and reviser instructions and reviews. `outline.md` records mathematical kernels and physical constraints. Reference PDFs preserve the delivered version. The ZIP is portable and has been rebuilt after extraction; page text and rendered pixel hashes were compared.

The tested worksheet workflow applies to student pages only. The adult guide was written separately and checked against the final student instances. All materials remain unpiloted, and no remote copy has been uploaded. Record which investigation/examples children actually use before choosing a future return visit.
