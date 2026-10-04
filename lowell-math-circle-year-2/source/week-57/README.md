# Week 57: portable editable source

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
