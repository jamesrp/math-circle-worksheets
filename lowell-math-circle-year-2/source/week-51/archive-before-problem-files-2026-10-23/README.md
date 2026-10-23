# Week 51 source before the problem-file conversion

On October 23, 2026 the Week 51 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the PDFs built from it match the old builder's PDFs in pages, extracted text and 100-dpi pixels.

- `make.py` and `draw.py`: the student builder the problem files replaced. Their drawing code is carried over in `../figures.py`, their wording in `../problems/*.md` and their endpoint asserts in `../editable/src/check.py`.
- `honest-measurement-ranges-week51-editable-source.zip`: the complete portable package that contained them, the October 4 fresh-review release with the October 23 strip kit. Its PDFs are the current ones at the time of the conversion.

SHA-256 of the ZIP: `39920a0d9f7f445618d0c2073d4b515a82b6e51b9544ad7b7d8af18189b54b91`.
