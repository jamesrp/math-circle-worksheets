# Week 64 source before the problem-file conversion

On October 23, 2026 the Week 64 student packet was converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure. The package stays in this week folder, as Week 65's does.

- `generate.py`: the builder that wrote `student/students.tex`. Its drawing code and page template are `../figures.py`, unchanged apart from returning each figure's lines; its wording is in `../problems/*.md`.
- `students.tex`: the LaTeX it wrote (footer W64-G35-v1). The new `../student/students.tex` differs only by writing the rules' paragraph break on page 1 as `\par`.
- `week-64-source.zip`: the October 5 source package that contained them. It builds the same two PDFs as the conversion.

SHA-256 of the ZIP: `7eecec7c2e522c1c2eaf069ad26054798f86f8ac7006a7793b34a659daa97a0d`.
