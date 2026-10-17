# Week 93: Squaring a rectangle

Unpiloted; physical rehearsal untested. Grades 3-5 area/fraction route, with Grades 4-5 proof continuation. Some Grades 2-3 children can do the concrete area entry; no K-1 packet.

New equal-area rectangle iteration, connected to area and interval certificates; distinct from atlas bisection and tangent tasks.

## Print and rebuild

The current owned PDFs are preserved in [reference-pdfs/week-93-students.pdf](reference-pdfs/week-93-students.pdf) and [reference-pdfs/week-93-facilitator.pdf](reference-pdfs/week-93-facilitator.pdf). Print US Letter at Actual Size for measured or cutting diagrams. Follow the facilitator preparation notes for duplicated cutting/card sheets and optional later pages.

Requirements: Python 3 and pdfLaTeX with TikZ, geometry, fancyhdr, Latin Modern, amsmath, amssymb and hyperref (TeX Live/MacTeX). The checker uses only Python's standard library. No downloaded books, network access, repository files outside this folder, or proprietary fonts are required.

```sh
python3 build.py --out out --work tmp/build
```

This builds `out/week-93-students.pdf` and `out/week-93-facilitator.pdf`, runs `check_math.py`, and keeps compilation/check logs under `tmp/build`. The fixed build epoch and PDF metadata permit byte-identical builds with the same pdfTeX/toolchain; different TeX versions may change bytes without changing content.

Edit `student/students.tex` or `guide/facilitator.tex`, rebuild, then repeat mathematical review and every-page visual QA. Reference PDFs and any distributed ZIP must be synchronized after changes. The student writer/critic/math/reviser workflow is separate from guide authoring. See [SOURCES.md](SOURCES.md), [PROVENANCE.md](PROVENANCE.md), and the review records for scope and evidence.

The portable ZIP contains only owned activity sources, current reference PDFs, checks, source notes and selected review records. It contains no wholesale books, private records, build intermediates or virtual environment.
