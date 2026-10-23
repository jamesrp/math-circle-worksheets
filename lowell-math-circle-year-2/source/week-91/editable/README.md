# Week 91: Rotor-router machines

Prepared review draft. Unpiloted; physical printing, cutting, flipping, counter placement, timing and classroom handling remain unrehearsed. This is a library investigation with several visits, not an adopted meeting schedule.

The six-page student packet has tree programming for Grades 2–5 on pp1–3, upper tree continuations on pp4–5, and a Grades 2–5 coin comparison on p6. The four-page return packet is Grades 4–5, with concrete absorbing roads before optional general arguments. Seven separately printable materials pages supply boards, cards and records. A six-page theorem-first guide gives proofs, complete answers, preparation, launch, hints and first-route choices. There is no K–1 packet; the guide gives an adult-read K–1 route on the one-switch board and the four-exit tree, which needs its own adult and kit.

## Build

Requires Python 3 standard library and pdfLaTeX (TeX Live/MacTeX) with TikZ, geometry, fancyhdr, lmodern, helvet, amsmath/amssymb, array, booktabs, enumitem and hyperref. No Python package, external artwork, font download or private reference is required.

```sh
python3 build.py --out ../../../week-91
```

After extracting the portable source ZIP:

```sh
python3 week-91/build.py --out rebuilt --work tmp/build
```

The builder writes `student/students.tex` from the problem files (`student/regenerate.py`), runs the independent finite verifier, generates the return-visit and materials TeX from `student/generate.py`, checks those against the packaged readable snapshots, compiles every PDF twice with deterministic metadata, and rejects errors/overfull boxes. Intermediates stay in `tmp/` or the supplied `--work` directory. The `reference-pdfs/` copies are the current print PDFs, for comparison, never build inputs; one compiled with a different pdfTeX version can differ from a rebuild by a few antialiased glyph pixels.

The student packet is stored as problem files since October 23, 2026 (in the repository `../week.toml`, `../figures.py` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`): edit those, not `student/students.tex`, which the build rewrites. Edit the return-visit packet and the materials in `student/generate.py`. Its `.tex` files are readable generated snapshots; refresh them after a generator edit by running `python3 student/generate.py /path/to/scratch` and copying the two emitted `scratch/src/*.tex` files back into `student/`. Edit the separate adult guide in `guide/facilitator.tex`. Rebuild, review changed pages and recreate the source ZIP after any change. `check_math.py` is the independently authored finite checker, adapted only for portable paths/output and final examples. General proofs remain in the guide. `review/verify_card_fixes_2026_10_23.py` checks the October 23, 2026 review-card fixes (`review/card-fixes-2026-10-23.md`).

Print US Letter, single-sided, Actual Size, preserving the four landscape apparatus pages. Use the guide's selected-route print list instead of printing the entire set for every child. The 50 mm bar and 15 mm squares permit print-scale checking; they do not establish physical fit. A partner enforces each move and flip. Arrow cards persist between counters; endpoints retain counters.

See SOURCES.md for primary mathematics, convention differences and prior-use boundaries, and QA.md for actual stage/reconstruction evidence. Only owned sources, checks, documentation and current reference PDFs are packaged. No books, downloaded papers, stage prompts, borrowed style examples, caches, machine paths or private records are included.
