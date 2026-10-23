# Week 56: portable editable source

**October 23, 2026.** The student pages are stored as problem files (in the repository `../week.toml`, `../template.tex` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`). `student/regenerate.py` writes `student/students.tex` from them, and `build.py` runs it before compiling; edit the problem files, not `students.tex`. `reference-pdfs/` holds copies of the current print PDFs. The same day the review card's K–1 fixes made the packet N56-S-v3, the materials N56-M-v2 (new p. 5, six 68 mm gap circles) and the guide N56-FAC-v2 (11 pages, a K–1 route section); a critic's follow-up the same day made them N56-S-v4, N56-M-v3 (60 mm gap circles, radius one face edge, cut along the two lines) and N56-FAC-v3; `student/verify.py`, `student/audit_math.py` and `guide/check_answers.py` check the new pages. The rest of this README records the October 4 package.

Current original student and facilitator sources, plus any necessary authored assets.
The student and guide READMEs give exact prerequisites, preparation, source references,
and any verification dependencies. Research/provenance notes are in `provenance/`.
Those notes record the research stage; the current PDFs are listed in the build manifest.
Their repository-relative reference links were updated for this package's local
location. Downloaded books, older packets and research caches are reference inputs
outside the ZIP; they are not required to build or check the included sources.
These adaptations are unpiloted. Digital diagram checks do not establish physical fit.

Build every delivered PDF from a fresh directory with Python 3 and TeX Live/MacTeX
(including TikZ, geometry, fancyhdr and the fonts named in the sources):

```sh
python3 build.py --out output
```

The build uses temporary directories and requires no repository paths or network.
Optional student/guide mathematical verifiers may require the packages documented in
their READMEs. No generated prompts, copied style exemplars, third-party books,
reference PDFs, rendered review images or old versions are included.

Outputs were verified against a clean ZIP extraction for exact text, dimensions and
rendered pixels in the production TeX/PyMuPDF environment. A later TeX/font version
can change rendering. Physical pretests and classroom piloting remain unperformed.
