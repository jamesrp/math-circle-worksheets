# Week 97 K–1 adult guide, writer draft

Build with Python 3, Poppler (`pdftotext`, `pdfinfo`) and pdfLaTeX / TeX Live
(`geometry`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `array`, `booktabs`,
`fancyhdr`, `tikz`). No external artwork, fonts or Python package is required.

```sh
cd src                 # or guide-src, after packaging
./build.sh
```

The builder writes `../k1-guide.pdf`, rejects TeX errors/overfull boxes,
removes its temporary TeX directory and ends by running `check_guide.py`.
It regenerates `answers.tex` from independently computed answers before compiling.

Place the unchanged final 13-page `k-1.pdf` in the folder above this source
folder. If absent, the checker searches parent directories for the repository's
`plans/k1-drafts/week-97/k-1.pdf`. There are no machine-specific paths.
The checker binds the final student PDF to its inspected SHA-256, confirms each
printed problem's page and group size, independently enumerates every finite
answer and checks all additional numerical examples and ring counts. Universal
claims still rely on the printed explanations, not on finite numerical tests.

The 4-page section is a writer-stage draft: no guide critic or reviser stage has
run. Student pages are unchanged. Unpiloted and physically unrehearsed. See the
run's writer-report.md for visual inspection, clean-rebuild evidence and risks.
