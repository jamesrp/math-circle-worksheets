# Writer report — Week 57 K–1

## Deliverable and scope

- `draft/k1-guide.pdf`: **4 US Letter pages**, pdfLaTeX; `N57-K-FAC-v1`.
- Portable `draft/src/`: TeX, `build.sh`, independent `check_guide.py`, README.
- Writer stage only. No critic/reviser stage, student edits, base-guide edits, commits or public writes. Generated absolute-path stage prompts are not deliverables for commit. All repository work is within this run folder.
- On approval, this replaces **“K–1 route, outside the numbered packet,” p. 3 of `week-57-facilitator.pdf` (W57-FAC-v4)**. The base guide's p. 1 K–1 pointer and p. 2 younger print quantities also need synchronization at later integration, not in this writer task.

## Mathematical overview and verified answers

The opening states Pick's rule in half-square units, **B + 2I = H + 2**, with one side-connected, nonoverlapping, gap-free lattice shape; no holes, pinches or corner-only connected groups. It separates experiment/conjecture/explanation, the three-piece quarter-turn obstruction, the four-piece possibility, and the six-cell obstruction for two neighboring stars. It refers to the existing guide for the older tables' general destination rather than reprinting that proof.

Recomputed against the **final seven-page student PDF**, not the historical six-page reviews:

- P1, p. 1: `(halves, outline) = (1,3), (2,4), (2,4), (2,4), (4,6), (4,6)`; no inside dots.
- P2, p. 2: always five outline dots. P3, p. 3: minimum four, uniquely the tilted square up to symmetry; other four-half shapes have six.
- P4, p. 4: impossible with three pieces. P5, p. 5: six rotational classes, fully illustrated/listed, with paper-in-halves and outline counts `4,5,6,6,7,8`.
- P6, p. 6: six pieces; six-square rectangle and two-square/four-half roofed hexagon witnesses; six required unit cells prove the lower bound.
- P7, p. 7: exactly two improving shapes up to turns/flips, each with six outline dots and two inside dots. Both are illustrated with eight-half divisions.

The independent checker imports no student/review script. Exact quarter-triangle enumeration produces `1,3,4,14,30,107,318,1116` regions for one through eight halves. Boundary-edge cancellation and vertex incidence determine admissibility and dot counts without assuming Pick. At eight halves, the 1,105 admissible shapes have `(B,I)` counts `(10,0):1038`, `(8,1):65`, `(6,2):2`. P5's 16 fixed placements collapse to six rotation classes; the P6 six-cell configurations are exhaustively checked too. Polygon winding/shoelace independently checks the printed covers, named witnesses and non-task three-square launch. Kit and print arithmetic are checked.

## Output and portability evidence

- Personally rendered/read all **7 final K–1 student pages** at 120 dpi and all **4 final guide pages** at 150 dpi. No clipping, overlap, missing symbols or broken tables found. Headers/footers and page mapping verified. Base guide, materials, older student content, outline, both reviews, draft README, model source/render and local research notes consulted; both materials pages inspected visually.
- Vector checks of every working board found 20.00024–20.00027 mm pitch in both directions. Final board inventories are p. 1: `2×2,2×2,3×2,3×2,3×2,4×2`; pp. 2–3: six `3×4`; p. 4: `5×5`; p. 5: nine `3×3`; p. 6: `6×5`; p. 7: a `3×3` reference and two `4×5` boards. Working dots are 2.6 mm across.
- Build passes with no LaTeX errors/overfull boxes. Intermediate files are not in `draft/src/`.
- Clean copy outside the repository, containing only copied `src/` and student `k-1.pdf` beside it, builds and passes the checker. `pdftotext -layout` matches exactly; **the rebuilt PDF is byte-identical**, SHA-256 `b63245acb7c7098d584321357b4f54a0971f7770e5aa2ddc4e2aff8974edfe95`.
- Builder has no host-specific environment path. The checker first searches beside `src/`, then ascends to find the repository-relative student folder. Local compile used the supplied isolated TeX environment; the portable source does not embed it.

## Risks and limits

No new mathematical error found on the final student pages. The guide handles continuing operational risks: pieces hide dots; tracing can bottleneck one adult; 12 mm convention illustrations on p. 1 are not workboards; stars are targets rather than “inside” marks; tiny cracks are not proof a dot is outside; a corner-pinched gap and two groups touching at a tip remain illegal. P2's six boards and P5's nine boards do not demand six distinct or nine distinct answers. P6 and P7 are later/readiness-dependent work, not a one-hour completion requirement.

**No additional unprinted activity object is needed** beyond the week's standard kit; the table demonstration uses an existing spare older-student p. 4 grid. The section gives explicit new K–1 printing and an estimated extra 10–15 minutes of preparation. Private book originals are absent from this checkout; source continuity is taken from the existing guide/research notes, not presented as fresh consultation of those books.

**Unpiloted and physically unrehearsed:** real printer scaling, hand cutting, piece alignment, dot visibility, child handling, tracing workload, staffing and timing could not be established digitally. No claim of classroom readiness is made. Claude's formal critique remains next.
