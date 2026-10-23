# Week 49 source before the problem-file conversion

On October 23, 2026 the Week 49 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the PDFs built from them match the print PDFs in pages, extracted text and 100-dpi pixels. The rebuilt LaTeX is byte-identical to this builder's for K–1 and Grades 2–3; for Grades 4–5 the two lines of the even/odd rule are one text node with a 10 mm line break instead of two nodes 10 mm apart.

- `make.py` and `draw.py`: the student builder the problem files replaced. Their drawing code is carried over in `../figures.py`, their wording in `../problems/*.md` and their asserts in `../editable/src/check.py`.
- `four-tower-differences-week49-editable-source.zip`: the complete portable package that contained them, the October 4 fresh-review release. Its PDFs are the current ones at the time of the conversion.

SHA-256 of the ZIP: `b66fd407e2e7e7bcce5c7271d40cce499da99b89840a7da0c153e92d8e576e04`.
