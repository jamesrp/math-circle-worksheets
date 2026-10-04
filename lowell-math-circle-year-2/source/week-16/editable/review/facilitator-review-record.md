# Three-color triangles facilitator guide

Separate adult guide, draft and unpiloted. Library slot 16 is not a calendar assignment.

Run `python3 check_math.py` and `python3 build_guide.py` here. All paths are relative to __file__. Python dependency: reportlab; DejaVu Sans optional with Helvetica fallback. Output: ../facilitator-guide.pdf (10 US Letter pages). The builder imports only geometry/helpers from check_math.py; the main enumeration runs only when invoked directly.

Final numbering: each band has Problems 1-6. K-1 has six student pages; both older packets have seven because Problem 1 is repeated on a second recording copy. This is 18 distinct numbered problems, all covered.

Independent checker reconstructs regular triangular cells from geometric adjacency, verifies cell area and shared-edge incidence/Euler counts, enumerates all legal colorings (including fan refinements and exceptions), checks all sixteen sole-cell locations, ten local types, and ordered printed door components. It also verifies the guide's structural three-step maximum proof formula for every boundary choice with center Y and the explicit five-cell witness. math-checks.json contains exact row-code witnesses and distributions; check-output.txt preserves the successful run.

QA 2026-10-03: reviewed PROMPT, reviews, final source, PDF text and all 20 final student-page renderings. Final adult PDF rendered at 70 dpi; all ten pages individually inspected after pagination and table-width repairs. Numbered cells, door marks, route orders, source fidelity and all page cross-references checked. No observed clipping, overlap or missing glyphs. No student files edited. qa/ retains inspected images.

The guide supplies real general parity/path proofs, a separate structural bound of five for the three-step board, a local 2+2+2+1 proof for the fixed fan maximum seven, and explicit witnesses for all sixteen possible sole-cell positions. The upper printed interior door route is correctly described as an open path between two all-three cells, not a loop.
