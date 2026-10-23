# Week 13 source before the problem-file conversion

On October 23, 2026 the Week 13 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or board: the rebuilt LaTeX is byte-identical to this builder's, and the print PDFs match in pages, extracted text and 100-dpi pixels.

- `build_packets.py`: the student builder the problem files replaced. Its boards and page template are carried over in `../figures.py`, its wording in `../problems/*.md`, and its exhaustive checks in `../editable/src/student_checks.py`.
- `route-packing-week13-editable-source.zip`: the complete source package that contained it (the October 4 fresh-review release). Its PDFs are the same as the conversion's. SHA-256: `7a36cd4a11e45c259857e598933732aa8a68dc133012e101380663f2adf2c64a`.
