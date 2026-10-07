# Week 78 final student/adult pair review

Reviewed on 2026-10-07 against the actual `final/students.pdf` and `final/facilitator.pdf`, not earlier draft reviews. Fresh, review-only stage. No PDF/source edits, commits, publication, or delegation.

## Verdict

**The mathematics, pair alignment, page presentation, source scope, and isolated rebuilds pass. Make the one wording correction below before release, then rebuild and inspect the changed guide.** There is no incorrect numerical answer, missing full solution, faulty general proof, or other blocking substantive issue. This review does not claim physical readiness or classroom validation.

### PR78-01 — Low severity; correct the stated parameter domain before release

- **Location:** adult guide page 1, immediately after the three-ray definition; `final/guide-src/facilitator.tex:28`.
- **Evidence:** the display correctly requires `t ≥ 0`, but the next sentence says, “Coordinates and t may be any real numbers.” Taken literally, that permits negative ray parameters and describes whole supporting lines rather than the intended closed rays. The adjacent correct display and repeated fixed-ray descriptions make the intended definition clear, so none of the solutions depends on the mistaken sentence.
- **Smallest fix:** replace that sentence with “Coordinates may be any real numbers; t is any nonnegative real number.” Preserve the existing display and other text.
- **Required recheck:** rebuild `facilitator.pdf` from `guide-src`, confirm the corrected sentence in the PDF, render and inspect the changed page and any reflow, and update the guide hash/verification. No student change is needed. The coordinator has elected to make this correction before release.

No other located issues.

## Controlled artifacts and visual coverage

| Artifact | SHA-256 | Pages inspected | Size |
| --- | --- | ---: | ---: |
| `final/students.pdf` | `4460ba48641f9ece9ba163f296d53ff23c1b34a6681acba17b6b7797719f7c46` | 4 of 4 | 139,104 bytes |
| `final/facilitator.pdf` | `da98efdc88847f5cbafe741586f7c438a11f8093790dfe554594a01d834ac1bc` | 4 of 4 | 179,431 bytes |

Both are unencrypted US Letter PDFs, 612 × 792 pt, with all fonts embedded. I rendered the actual PDFs with Poppler at 110 dpi and visually inspected every page. Consistent headers, packet IDs, footers and page numbers are present. No clipping, collisions, broken symbols, missing answers or blank overflow pages were found. The guide is compact but legible; its source notes remain within the page. The rebuilt guide reports no overfull/underfull boxes, missing characters or warnings.

- Student page 1: the opening visual puts the junction at (2,2), P at (4,2), Q at (4,4), and arrows in the correct east/north/southwest directions. The two top A points are (4,4); the lower fixed pairs match the guide.
- Student page 2: all four A/B diagrams match the guide's order and coordinates. There is usable answer space for Problem 3.
- Student page 3: all P/Q targets match the two uniqueness examples and three aligned inverse examples. The smaller three boards remain legible and give an initial working window; larger continuation sheets are explicitly supplied.
- Student page 4: A=(2,7) is plotted correctly. B=(10,5) is intentionally outside the 0–8 window, with its coordinates supplied in the task. The adjacent blank space and larger prepared grids support continuation.
- Every board has equal horizontal/vertical scale. Main grid units are 0.78 cm (P1), 0.82 cm (P2), 0.83 cm (P4), 0.66 cm (P5), and 0.76 cm (P6/P7), corroborated by the source and identical rebuild raster. The introductory visual uses 0.61 cm units.

## Independent mathematical verification

I wrote `tmp/pair-inspection/independent_check.py` without importing either package's checker/data or any earlier review. It uses one-variable affine equality/inequality constraints along each ray, rather than running the guide writer's determinant assertions as the independent check. Coordinates were transcribed from the final PDF diagrams and checked against the source. Closed rays are solved as sets, including endpoints and non-grid points.

### Complete numerical answer audit

| Final question/example | Complete result independently obtained |
| --- | --- |
| Opening, L(2,2) | (4,2) is on the line; (4,4) is off despite the two larger values tying |
| Launch translation, L(3,2) | (5,2) lies on its east arm |
| P1 guide choices, A=(4,4), B=(6,5) | One point (5,4) |
| P1 guide choice B=(6,4) | East ray from (6,4) |
| P1 guide choice B=(4,6) | North ray from (4,6) |
| P1 guide choice B=(6,6) | Southwest ray from (4,4) |
| P1 guide choice B=(4,4) | The whole L(4,4); equal junctions are allowed here |
| P1 lower left, (2,2) and (6,5) | One point (3,2) |
| P1 lower right, (2,2) and (5,6) | One point (2,3) |
| P2 upper left, (2,5) and (6,2) | One point (6,5) |
| P2 upper right, (3,2) and (3,6) | {(3,y): y≥6} |
| P2 lower left, (2,4) and (6,4) | {(x,4): x≥6} |
| P2 lower right, (2,2) and (6,6) | {(2−t,2−t): t≥0} |
| P4 left targets (2,5),(6,2) | Unique junction (2,2) |
| P4 right targets (2,2),(6,5) | Unique junction (5,5) |
| P5 left targets (2,4),(6,4) | All junctions {(2−t,4): t≥0} |
| P5 middle targets (3,2),(3,6) | All junctions {(3,2−t): t≥0} |
| P5 right targets (2,2),(5,5) | All junctions {(5+t,5+t): t≥0} |
| P6 junctions (2,7),(10,5) | One point (10,7), beyond the printed window |

Thus all 17 numerical answer-set cases in the guide, plus its opening/launch examples, pass. The inverse answers are full loci, not sampled lists of integer junctions.

The independent finite audit also passed 1,296 forward and 1,296 inverse ordered pairs on an asymmetric rational grid. Coverage: 36 coincident pairs, 180 same-column pairs, 180 same-row pairs, 30 distinct same-diagonal pairs, and 870 unaligned pairs. A further 1,296 translated rational point/line cases verify minimum-tie membership and invariance under a common added constant. These computations support the examples; they do not prove the all-real claims.

### General proofs and claimed impossibilities

I independently checked the complete geometric argument on guide page 4, including why no additional arms meet:

1. A tied minimum of x−a, y−b, 0 gives exactly the north, east or southwest closed ray. A tie of the two larger scores contributes nothing. A common additive constant preserves the minimizers.
2. For northwest/southeast junctions, the east/north arms meet at the rectangle's northeast corner. Parallel or outward-facing arm pairs add no point.
3. For southwest/northeast junctions and unequal positive width/height, the northeast southwest-arm exits at the nearer left/bottom edge of the rectangle, giving exactly one point on the other line. Its later continuation cannot reach the other permitted side-ray. The other northeast arms cannot return to the southwest line.
4. A square gives the southwest shared ray from the southwest junction. Zero width gives a north shared ray from the higher junction; zero height an east shared ray from the rightmost. Zero width and height gives the whole line. These cases exhaust arbitrary real junctions, with no reliance on an integer grid or page boundary.
5. Consequently P3 is impossible: different junctions yield a singleton or a ray, never exactly two points. They also cannot have no intersection, a nonzero bounded segment, or two shared rays. P6's classification includes coincident junctions correctly.
6. For fixed target P=(r,s), solving for the junction gives the west ray from P, the south ray from P, and the northeast ray from P. Every point on that reversed figure works, and no other point works. Intersecting two such figures finds exactly the permitted junctions. Reflecting both through the origin gives the already proved fixed-orientation line family. Distinct targets therefore allow one line or infinitely many, with the three complete exceptional loci stated in the guide. Distinct junctions define distinct line sets. This proves P4/P5 completeness and P7, including exclusion of zero or finite multiplicity above one. Coincident targets are explicitly outside P7 and correctly discussed for adults.

The mathematical opening is theorem-first and precedes timing and solutions. It states the actual classification, closed-ray geometry, fixed orientation, all-real scope, intended discoveries, and which later tasks need adult proof support. Except for PR78-01's wording, assumptions and limits are precise. The guide explicitly distinguishes trials, conjectures and explanation, ordinary set intersection and stable intersection, and the allowed-junction figure from a line of the original family. Hints never present failed trials as an impossibility proof.

## Teaching route, materials and operational scope

- The shared prototype is accurately scoped to three Grades 4–5 children and their organizer. It does not invent a K–1 route or imply that it supplies the other eight children's work.
- Prerequisites are operational: square-grid plotting, comparing small numbers, retaining fixed directions, and later reasoning beyond finite drawings. Adult reading/ruler support is allowed; signed arithmetic is unnecessary for entry. Children still choose junctions and do the drawing.
- Two working pairs are specified (two children, and one child with the adult), with rotation. The fallback instead uses all three child roles explicitly. Staffing is feasible on paper and transparent, not a claim of successful classroom operation.
- Two active pairs require 2 student packets, 4 coloured pencils, 2 rulers, 4 counters, 2 erasers, and 4 grid sheets. Listed table totals add 1 packet, 2 pencils, 1 ruler, 2 counters, 1 eraser, and 2 sheets as spares: 3 packets/12 single-sided pages, 6 pencils, 3 rulers, 6 counters, 3 erasers, 6 sheets. One four-page adult guide is specified. Optional tracing totals (4 active + 2 spare) are correct.
- Extra grids use 0–12 on each axis with 1 cm squares: a 12 × 12 cm working area, which fits Letter paper. It includes the explicit off-page example's B=(10,5) and intersection (10,7). No exact-fit manipulative or specialty transparency is mandatory.
- The launch demonstrates fixed orientation and a legal translation before investigation without announcing the classification. The 60-minute route has movement, core P1–P3, conditional P4–P5, deferred P6–P7, fallback and closing share. Every problem has ordered hints and a clear stopping/struggling option. Completing all pages is not required.
- Actual pencil contrast, ruler handling, tracing visibility, printed scale, ray continuation, timing and children's understanding remain **unrun**. The guide tells the adult to rehearse and accurately declares both physical rehearsal and classroom piloting unperformed. These are limitations, not failed digital checks.

## Sources and provenance

I opened both cited primary sources rather than relying on the guide's source note:

- David Speyer and Bernd Sturmfels, *Tropical Mathematics* (2004), §§1 and 3, supplies min-plus arithmetic, the repeated-minimum corner locus, and the north/east/southwest line convention. Printed pp. 6–8 also discuss generic intersection/interpolation. The guide accurately uses this framework without attributing its exact worksheet classifications or proof to the paper. https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf
- Ayush Kumar Tewari, *Point-Line Geometry in the Tropical Plane* (2020), §§3–4, treats incidence, duality, shared-ray versus stable intersection, and infinitely many lines through aligned targets. It explicitly uses max-plus and west/south/northeast rays. The guide's convention warning and research connection are accurate and substantive. https://arxiv.org/abs/2006.04425 and https://arxiv.org/pdf/2006.04425

The guide's next question about three targets follows naturally from its unique-junction construction. No unearned research theorem or educational result is claimed.

`final/guide-src` contains only four authored files: README.md, build.py, check_math.py, facilitator.tex. `final/src` contains five authored files: README.md, build.py, check_math.py, data.py, students.tex. No papers, books, external figures/fonts, raw reports, workflow exemplars, symlinks, or format dumps are packaged. Builds need only those files and ordinary Python/TeX packages. Earlier prompt exemplars elsewhere in the run are not in the portable packages.

## Reproducibility and evidence

The guide was rebuilt in `tmp/pair-inspection/isolated/` from a copied source-only guide folder. In this minimal cloud TeX environment the known configuration `TEXMF='{/usr/share/texmf,/usr/share/texlive/texmf-dist}'` was used. The builder generated its own format in the isolated output tree; no run-local format or source from outside the package was copied or loaded. A preliminary invocation had a reviewer-typed space in the first TeX path; rerunning with the exact documented environment resolved it. This was not a package defect.

- Guide: extracted layout text is byte-identical to the reviewed final PDF; all four 110-dpi page PNGs are byte-identical.
- Student: additionally rebuilt independently from a copied student-source-only folder; extracted layout text and all four 110-dpi page PNGs are byte-identical.
- Packaged guide checker passes its own 17 cases and 6,561 forward/6,561 inverse audits. Packaged student checker also passes. These runs are supplementary; the reviewer-owned checker and proof review above are the independent verification.
- PDF file-byte identity is not required across rebuild timestamps; source-to-text/raster identity was verified instead.
- A separate normal TeX Live/MacTeX machine was not exercised. Those documented prerequisites are acceptable; the isolated cloud build establishes that neither package depends on repository-only source material.

Machine-readable record: `pair-verification.json`.

Review scratch and evidence remain under `tmp/pair-inspection/`: independent checker and results/log, all eight inspected page PNGs, extracted texts, source-only isolated rebuild trees, rebuilt page PNGs, and build logs. Both input PDFs and both source packages are unchanged by this review.
