# Week 48 source before the problem-file conversion

On October 23, 2026 the Week 48 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the PDFs built from it match the print PDFs in pages, extracted text and 100-dpi pixels.

- `make.py` and `draw.py`: the student builder the problem files replaced. Their drawing code is carried over in `../figures.py`, their wording in `../problems/*.md` and their asserts in `../editable/src/check.py`.
- `inside-outside-covers-week48-editable-source.zip`: the complete portable package that contained them, the October 4 fresh-review release. Its PDFs are the current ones at the time of the conversion.

SHA-256 of the ZIP: `2c2d9215ad56616368059ec02607559237e4348e8a405fdae53b332672d2e06d`.
