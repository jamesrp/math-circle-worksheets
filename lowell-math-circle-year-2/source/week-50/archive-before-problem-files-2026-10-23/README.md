# Week 50 source before the problem-file conversion

On October 23, 2026 the Week 50 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the PDFs built from them match the print PDFs in pages, extracted text and 100-dpi pixels. The rebuilt LaTeX is byte-identical to this builder's for K–1; for Grades 2–3 and 4–5 the only difference is that the five spaces between "mm" and "Dashed:" in Problem 2's answer line are one space, which TeX typesets the same.

- `make.py` and `draw.py`: the student builder the problem files replaced. Their drawing code is carried over in `../figures.py`, their wording in `../problems/*.md` and their asserts in `../editable/src/check.py`.
- `staircases-and-lengths-week50-editable-source.zip`: the complete portable package that contained them, the October 4 fresh-review release. Its PDFs are the current ones at the time of the conversion.

SHA-256 of the ZIP: `42e8b0d5fa8f8ffafa0eb5b5c8fc6114a1a0f673caa918b6af95200118fd9807`.
