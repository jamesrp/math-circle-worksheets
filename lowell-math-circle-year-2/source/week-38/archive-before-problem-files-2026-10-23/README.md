# Week 38 source before the problem-file conversion

On October 23, 2026 the Week 38 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the rebuilt PDFs match its output in pages, extracted text and 100-dpi pixels. Against the print PDFs both builders show the same small font differences (at most 18 pixels on a page), the audited alternates that `verify_revision.py` already allowed.

- `make_packets.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py` and its wording in `../problems/*.md`.
- `examples.py`: the washer example it imported; its drawing is `washer_example()` in `../figures.py`, and its two sentences are text sections of `../problems/02-two-dots.md`.
- `seams-and-cuts-week38-editable-source.zip`: the complete source package that contained them (the October 4 fresh-review release). SHA-256: `09c3033ecc6c565a76cf14e947f06da976c409995eb6627cb6cc029edd1abf85`.
