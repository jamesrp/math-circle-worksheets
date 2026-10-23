# Week 14 source before the problem-file conversion

On October 23, 2026 the Week 14 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or drawing: the rebuilt LaTeX is byte-identical to this builder's, and the print PDFs match in pages, extracted text and 100-dpi pixels.

- `build_packets.py`: the student builder the problem files replaced. Its drawing code and page template are carried over in `../figures.py` (the map figure split into `flip_example` and `pentagon_map`, with its caption in the problem file), its wording in `../problems/*.md`, and its enumeration checks in `../editable/src/student_checks.py`, which writes the same `mathematical-checks.json`.
- `triangulations-week14-editable-source.zip`: the complete source package that contained it (the October 4 fresh-review release). Its PDFs are the same as the conversion's; rebuilt in TeX Live 2023 (pdfTeX 1.40.25), its unchanged guide differs from the reference in glyph antialiasing exactly as the conversion's does. SHA-256: `45533bfe454a862372f3ecc1bcfb5ff7cc2818697cc50b68ba05ca3dddf4a868`.
