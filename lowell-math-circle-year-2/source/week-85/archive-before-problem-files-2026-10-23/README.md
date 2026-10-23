# Week 85 source before the problem-file conversion

On October 23, 2026 the Week 85 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or drawing: the generated LaTeX of the shared, upper and materials packets is byte-identical to this generator's.

- `generate.py`: the student and materials generator the problem files replaced. Its drawing code, page template and materials pages are carried over in `../figures.py`; the wording of its `shared()` and `upper()` pages is in `../problems/*.md`.
- `week-85-source.zip`: the October 17 source package that contained it. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `3e589b58451c0ac3af27026226be4dbc7cc47c681cbd0d2a1bfdd5c8133b3807`.
