# Week 12 return-visit student packet

Four single-sided US Letter pages, containing three investigations: unlike-color noncrossing pairings (Problem 1, with extra workspace), height-limited paths (Problems 2–3), and shortest local path changes (Problem 4). This is unpiloted review material. Print at 100% scale; the three main circle boards are 3 inches in diameter. Physical use has not been rehearsed.

## Rebuild

Requires pdfLaTeX with TikZ, geometry, fancyhdr and Helvetica. On macOS the builder also recognizes `/Library/TeX/texbin/pdflatex`.

From this directory:

```sh
sh build.sh
```

The script writes `../return-visit.pdf` and build intermediates under `../build/`. The TeX file has no external asset or repository dependencies.
