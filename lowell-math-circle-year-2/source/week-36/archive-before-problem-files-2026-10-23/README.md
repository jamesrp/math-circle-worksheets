# Week 36 source before the problem-file conversion

On October 23, 2026 the Week 36 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's and the print PDFs match in pages, extracted text and 100-dpi pixels.

- `build_packets.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py`, its wording in `../problems/*.md`, and its exact checks in `../editable/src/student_checks.py`.
- `nine-point-world-week36-editable-source.zip`: the complete source package that contained it (the October 4 fresh-review release). Its PDFs are the same as the conversion's. SHA-256: `84136c41845c6a946002c529fb6f02a331a83e86b49b8a84a0919e4c8b7c43f7`.
