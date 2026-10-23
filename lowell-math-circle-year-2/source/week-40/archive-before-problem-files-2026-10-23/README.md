# Week 40 source before the problem-file conversion

On October 23, 2026 the Week 40 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the rebuilt PDFs match the print PDFs in pages, extracted text and 100-dpi pixels (no differing pixel).

- `make_packets.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py` and its wording in `../problems/*.md`.
- `common.py`: the page template and drawing primitives it imported; they are in `../figures.py` too. The trefoil geometry of `../editable/src/knot_geometry.py` is repeated there, and `knot_geometry.py` stays for `check_math.py`.
- `loop-color-certificates-week40-editable-source.zip`: the complete source package that contained them (the October 4 fresh-review release). SHA-256: `99c522237b27b350f551f2a2f9c0024e01014dd505c08e17b7e0ee7f73a3e8e5`.
