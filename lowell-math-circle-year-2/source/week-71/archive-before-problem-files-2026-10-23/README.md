# Week 71 source before the problem-file conversion

On October 23, 2026 the Week 71 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure: the generated LaTeX differs from the old source only by blank lines between sections and by the window macros moving from the preamble to the start of the body, and the print PDF matches in pages, extracted text and 100-dpi pixels.

- `students.tex`: the hand-written student source the problem files replaced. Its preamble is carried over in `../template.tex` and its wording and figures in `../problems/*.md`.
- `windows.tex`: the window macros it read, as `../editable/student/make_diagrams.py` wrote them; `make_diagrams.generate()` now returns the same text to `../figures.py`.
- `week-71-source.zip`: the complete October 6 source package that contained them. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `5b42722e8340bcc4896caaceaa153e241083824cab17c3636950da881989460d`.
