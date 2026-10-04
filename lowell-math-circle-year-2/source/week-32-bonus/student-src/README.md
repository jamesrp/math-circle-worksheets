Build with `python3 build.py [output-directory]`. Requires a TeX distribution with pdfLaTeX, TikZ, and Helvetica. Put pdflatex on PATH or set `PDFLATEX`. The default output is the enclosing directory. No absolute project paths or downloaded assets are needed.

`python3 writer-check.py` runs inherited finite mathematical checks using only the Python standard library and writes `writer-check.json` in the enclosing directory. Independent verification is recorded separately.

Unpiloted. Physical tile fit, cutting accuracy, larger recipe reconstructions, and classroom timing remain untested.
