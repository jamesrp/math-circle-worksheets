# Week 76 source before the problem-file conversion

On October 23, 2026 the Week 76 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../problems/`), with no change to any wording or figure: each page is still one TikZ canvas, each problem's prompt is placed by `\promptat{y}` at the height it had, and the print PDF matches in pages, extracted text and 100-dpi pixels.

- `students.tex`: the hand-written student source the problem files replaced. Its preamble is carried over in `../template.tex` and its wording and drawing code in `../problems/*.md`.
- `week-76-source.zip`: the complete source package that contained it. Its PDFs are the same as the current ones.
