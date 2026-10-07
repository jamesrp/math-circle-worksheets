# Week 78 guide wording revision

Completed 2026-10-07, guide-only correction of PR78-01 from `pair-review.md`.

## Exact change

In `final/guide-src/facilitator.tex`, line 28, changed only:

- Before: “Coordinates and t may be any real numbers.”
- After: “Coordinates may be any real numbers; t is any nonnegative real number.”

The adjacent display still requires t ≥ 0. No examples, proofs, answers, other
mathematical content, or student material changed. No matching portable source
documentation contained the old assertion, so no documentation wording change
was needed. `guide-verification.md` now records the current PDF hash and size.
The independent `pair-review.md` and `pair-verification.json` remain unchanged
as records of the pre-correction artifacts.

## Guide artifact hashes

- Prior `final/facilitator.pdf` SHA-256: `da98efdc88847f5cbafe741586f7c438a11f8093790dfe554594a01d834ac1bc`.
- Revised `final/facilitator.pdf` SHA-256: `1b22c5b28f6d0eb6d15661dcfe4346556246e17206c1b701dd83db79904c12d9`.
- Prior TeX SHA-256: `727268b0b784f6afcc159ca4827bbe6df5a5edf8e3c4d8a663afc1bf2a39bcf7`.
- Revised TeX SHA-256: `8be619e805ceba906c19c9dfb90f3584a9a7298deaea3aeb303aa0b9b17ed7e0`.
- Revised guide: 4 US Letter pages (612 × 792 pt), 179,447 bytes.

## Checks performed

- Ran the PDF-skill edit marker once before authoring.
- Built `final/facilitator.pdf` using the unchanged portable `build.py` and
  `TEXMF='{/usr/share/texmf,/usr/share/texlive/texmf-dist}'`; both TeX passes passed.
- The build ran the unchanged guide checker: all 17 answer cases, the opening
  and launch examples, 6,561 exact rational line pairs and 6,561 inverse pairs
  passed. These finite audits are not claimed as the all-real proof.
- Confirmed the exact corrected sentence in the final extracted PDF text and
  visually on page 1. Rendered the revised PDF at 110 dpi and inspected all
  four pages. No clipping, overlap, missing glyphs, or blank overflow pages;
  headers, footers, tables, equations and source notes fit. Compile logs contain
  no overfull/underfull boxes, missing-character notices or warnings.
- Prior and revised renders of pages 2–4 are byte-identical; only page 1's
  corrected paragraph changed.
- Created a temporary ZIP containing exactly README.md, build.py, check_math.py
  and facilitator.tex, extracted into a fresh directory, and rebuilt with
  TEXFORMATS empty. The isolated builder initialized its own format in its
  output tree. All four 110-dpi page rasters and the extracted layout text are
  byte-identical to the revised final guide.
- The portable `final/guide-src` still contains only those four authored files:
  no runtime formats, fonts, papers, generated build files or symlinks.
- Student PDF and all five student source files were hashed before and after;
  all six hashes are unchanged (listed below).
- Evidence is confined to `tmp/guide-revision/` within this run, including the
  prior PDF/TeX, renders, extracted text, build log, source ZIP, isolated rebuild,
  and before/after student hash manifests.

## Unchanged student SHA-256 values

- `final/students.pdf`: `4460ba48641f9ece9ba163f296d53ff23c1b34a6681acba17b6b7797719f7c46`
- `final/src/README.md`: `78e7a87a98ae858835d80cd54a550145621e9c392fe4a413a4e40176ece350a8`
- `final/src/build.py`: `888d4c6796421eabb394f42125d7c6caf6e0a66f73077d612522c6321360bf6f`
- `final/src/check_math.py`: `8bd05cdbda5ade566e6acfbc711fc9cb5722d2c587d9a7d20fc4d2ddc15750c3`
- `final/src/data.py`: `0315a6e8094c8a31f69a19e7ce89be86cd4e99ba031bf39aebd0a00f4143484e`
- `final/src/students.tex`: `2ae11b04debfadb2aac78cce554ebd5a8296b1337a97309c6b79ab9f5acded33`

## Scope and remaining limits

Only the guide TeX, rebuilt guide PDF and guide verification records changed.
No student edits, commits, pushes, new production stages or delegation occurred.
Physical rehearsal and classroom piloting remain unperformed.
