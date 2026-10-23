# Week 37 source before the problem-file conversion

On October 23, 2026 the Week 37 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical and the print PDFs match in pages, extracted text and 100-dpi pixels.

- `build_packets.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py`, its wording in `../problems/*.md`, and its arithmetic checks in `../editable/src/student_checks.py`.
- `mirror-twins-week37-editable-source.zip`: the complete source package that contained it (the October 4 fresh-review release with the October 23 kit). Its PDFs are the same as the conversion's. SHA-256: `31f0171b40c391d96a2a441544b97926c2ab9ba591ba1582cfe7f1d88d391fda`.
