# Week 57 source before the problem-file conversion

On October 23, 2026 the Week 57 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure, and the portable package moved into `../editable/`.

- `students.tex`: the hand-written student LaTeX the problem files replaced (footer N57-S-final-v2). Its preamble is `../template.tex`; its pages are in `../problems/*.md`; its `\input{figures.tex}` became the figure section of `../problems/00-shared-rules.md`.
- `week-57-source.zip`: the October 4 source package that contained it. It builds the same two PDFs as the conversion.

SHA-256 of the ZIP: `b3b5f4ea1e01b740f968bd8fc9684a5882f6e719b9aa229bbfc92c8db403235d`.
