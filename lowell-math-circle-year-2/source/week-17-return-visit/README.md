# Week 17 return visits

**October 23, 2026.** From the Week 17 review card (should 4): Problem 1 now says "two red cards next to each other have appeared anywhere" instead of "in a row", which could be read as any two reds in the row of cards; the guide already gave RBR as NO (footer W17-RV-v2). The guide is unchanged. Rebuilt with TeX Live 2023, page 3 has the same words as the October 4 copy, with its boxes and lines up to 6 pt higher; rebuilding the unchanged guide shows small anti-aliasing drift (at most 194 pixels a page at 100 dpi), so its October 4 PDF stays current. The October 4 ZIP is in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

Three investigations within the Week 17 theme. Separate draft/unpiloted companions; existing base packets and guides are untouched. Readiness is labeled on each student page; the adult guide states prerequisites, precise facts, assumptions, materials, a common launch, first routes, flexible return-visit pacing, solutions, hints and extensions. Physical counter fit, preparation stock, procedures and classroom response are untested.

- Student: `../../week-17/week-17-return-visit.pdf`
- Adult: `../../week-17/week-17-return-visit-facilitator.pdf`

## Clean build

Requires Python3 standard library and pdfLaTeX with ordinary LaTeX packages including TikZ, extarticle, Latin Modern, Helvetica, fancyhdr, geometry and amsmath. No Python packages, custom fonts or figure assets outside this folder are needed to build.

From this folder: `sh build.sh /absolute/output/directory`. Without an argument, a fresh system-temporary output folder is used and printed. This never copies into printable week folders or overwrites base files. In the repository, use a folder under `tmp/`.

Editable student sources are in `student/`; `facilitator.tex` is the editable adult guide. `independent_checks.py 17` recomputes the finite audit and writes local JSON. `workflow/` preserves the generated writer, critic, math and reviser instructions and reviews. `outline.md` records mathematical kernels and physical constraints. Reference PDFs preserve the delivered version. The ZIP is portable and has been rebuilt after extraction; page text and rendered pixel hashes were compared.

The tested worksheet workflow applies to student pages only. The adult guide was written separately and checked against the final student instances. All materials remain unpiloted, and no remote copy has been uploaded. Record which investigation/examples children actually use before choosing a future return visit.
