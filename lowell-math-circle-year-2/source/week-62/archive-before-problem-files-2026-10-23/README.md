# Week 62 source before the problem-file conversion

On October 23, 2026 the Week 62 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure, and the portable package moved into `../editable/`.

- `make_source.py`: the builder that wrote `students.tex` and `graphs.json`. Its drawing code (`graph()`, the network coordinates and helpers) is `../figures.py` unchanged; its text is in `../problems/*.md`.
- `students.tex`: the generated student LaTeX the problem files replaced (footer W62-S-v1). Its head is `../template.tex`.
- `week-62-source.zip`: the October 4 source package that contained them. It builds the same two PDFs as the conversion.

SHA-256 of the ZIP: `916dc039591e6a58116ad0f69b05d4e72acdc02b892207b36e09c272ee95732b`.
