# Week 13 return-visit revised student packet

`return-visit.tex` is the complete editable student source. It uses LaTeX, TikZ,
`geometry`, `fancyhdr`, and Latin Modern; it has no repository-relative includes.

Build from any copied source folder:

```sh
python3 build.py --pdflatex /path/to/pdflatex --out ../return-visit.pdf
python3 check_math.py
```

When `pdflatex` is on PATH, omit `--pdflatex`. Output is US Letter; print single-sided
at actual size. Writer, critic, independent math review, and revision stages have
run. This is draft/unpiloted review material. Physical use with 15 mm markers and
classroom use remain untested; the PDF marker-clearance check is digital only.

The 3-page shared collection contains consecutive Problems 1-3: page 1 compares
road and middle-dot sharing (K-1 entry), page 2 compares fixed terminal pairs and
choice of finishes (grades 2-3 entry), and page 3 packs simultaneous routes with
capacities and blocking-arrow totals (grades 4-5 entry).
