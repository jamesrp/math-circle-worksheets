# Week 61 source before the problem-file conversion

On October 23, 2026 the Week 61 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure, and the portable package moved into `../editable/`.

- `students.tex`: the hand-written student LaTeX the problem files replaced (footer W61-S-v3). Its head is `../template.tex`; its pages are in `../problems/*.md`; the figure macros it read from `figures.tex` are written by the first problem file's `macros()` figure section.
- `week-61-source.zip`: the October 16 source package that contained it. It builds the same two PDFs as the conversion.

SHA-256 of the ZIP: `9e9ca1185d5a1fca5436b9563efd42e77b699abcfc10344a91b84dcb41c01a10`.
