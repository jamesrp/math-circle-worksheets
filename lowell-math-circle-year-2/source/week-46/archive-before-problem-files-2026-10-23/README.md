# Week 46 source before the problem-file conversion

On October 23, 2026 the Week 46 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical, and the rebuilt PDFs match the print PDFs in pages, extracted text and 100-dpi pixels.

- `write.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py` and its wording in `../problems/*.md`.
- `forgetting-boards-week46-editable-source.zip`: the complete October 4 fresh-review source package that contained it. Its PDFs are the same as the current ones.
