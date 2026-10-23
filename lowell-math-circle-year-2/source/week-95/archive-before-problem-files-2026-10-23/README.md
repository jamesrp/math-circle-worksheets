# Week 95 source before the problem-file conversion

On October 23, 2026 the Week 95 student packets were converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure. The rebuilt LaTeX differs from the old builder's only by blank lines between sections and a comment line, and the new package build gives byte-identical student PDFs to the old builder's in the same TeX installation.

- `student/build.py`: the student builder the problem files replaced. Its preamble is carried over in `../template.tex`, its `table()` and `records()` helpers in `../figures.py`, and its wording and diagrams in `../problems/*.md`.
- `week-95-source.zip`: the complete October 17 source package that contained it. Its PDFs are the print copies of that date.
