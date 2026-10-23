# Week 59 source before the problem-file conversion

On October 23, 2026 the Week 59 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure, and the portable package moved into `../editable/`.

- `students.tex`: the hand-written student LaTeX the problem files replaced (footer W59-S-v2). Its head, without `\input{assets.tex}`, is `../template.tex`; its pages are in `../problems/*.md`, whose figure sections call `asset(name)` in `../figures.py` for the TikZ code each `assets.tex` macro held.
- `week-59-source.zip`: the October 4 source package that contained it. It builds the same three PDFs as the conversion.

SHA-256 of the ZIP: `dc44dd7e4b30e95f72ceb12989f159ffa7c8e0a5a4ad373ce00dcaf1df77a4e0`.
