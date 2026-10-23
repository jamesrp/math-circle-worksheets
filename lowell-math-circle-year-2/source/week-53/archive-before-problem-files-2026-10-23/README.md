# Week 53 source before the problem-file conversion

On October 23, 2026 the Week 53 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure. The rebuilt packet matches the previous source's build page for page, with identical extracted text and no differing pixel at 100 dpi in the same TeX installation; against the print PDF (built October 4 with TeX Live 2025) the text is identical and the pixels differ only as the previous source's own rebuild here does.

- `students.tex`: the hand-written student source the problem files replaced. Its wording is carried over in `../problems/*.md` and its preamble in `../template.tex`; `../editable/student/students.tex` is now generated from them, with the map macros that `student/diagrams.py` used to write to `generated-diagrams.tex` placed at the start of the body.
- `week-53-source.zip`: the October 4 portable source package that contained it, including the previous `student/build.py`, with the package files at its top level (they are now in `../editable/`).
