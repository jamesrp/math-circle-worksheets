# Week 78 guide verification

## Authored conclusion

The single final Grades 4–5 packet supports a prerequisite-led table of three
children and one mathematician. The four-page guide makes Problems 1–3 the
first-session core, allows Problems 4–5 when ready and reserves the all-real
classification proofs in Problems 6–7 for adult-supported continuation. It does
not invent a K–1 or Grades 2–3 edition or redeploy their adults. Preparation is
specified for two working pairs, one consisting of a child and the organizer,
with partner rotation and exact spare counts.

The guide opens with the complete ordinary-intersection theorem and the joining
theorem, including equal-junction, aligned and noninteger cases. It keeps actual
shared rays distinct from stable intersection and separates finite trials from
proof. Every final numbered problem has a full answer and ordered hints.
Problem 5 gives full real rays of allowed junctions, not just visible grid dots.
The rectangle proof and reverse-junction construction supply the adult reasoning.

## Final artifacts

- `final/facilitator.pdf`: 4 US Letter pages, 179,431 bytes.
- PDF SHA-256: `da98efdc88847f5cbafe741586f7c438a11f8093790dfe554594a01d834ac1bc`.
- `final/guide-src/`: exactly `facilitator.tex`, `build.py`, `check_math.py`,
  and `README.md`; no external fonts, figures, papers, format files or prompts.
- Student pages were read and rendered, not edited. Current student PDF SHA-256:
  `4460ba48641f9ece9ba163f296d53ff23c1b34a6681acba17b6b7797719f7c46`.

## Mathematical checks

The guide checker independently transcribes the final PDF coordinates and
imports no student code. It solves all nine pairs of parameterized arms exactly
using rational linear algebra, retaining common closed rays as rays. It checks
the opening and launch comparisons plus 17 explicit forward/inverse answer
cases. Full ray intersections certify the all-enumeration answers.

An additional audit checks 6,561 ordered rational junction pairs, including
negative and half-integer coordinates, against the classification; another
6,561 checks the inverse target construction. All passed. These finite audits
are not a proof for all real coordinates. The guide's separate geometric proof
establishes that claim.

Key final-case answers include Problem 1's lower crossings `(3,2)` and `(2,3)`;
Problem 2's crossing `(6,5)` and north/east/southwest shared rays; Problem 4's
unique junctions `(2,2)` and `(5,5)`; Problem 5's west ray from `(2,4)`, south ray
from `(3,2)` and northeast ray from `(5,5)`; and Problem 6's off-page crossing
`(10,7)`.

## Build and page inspection

- Ran `python3 final/guide-src/build.py --out final`; mathematical checks and two
  pdfLaTeX passes succeeded. Final compile log has no overfull or underfull boxes.
- Rendered every final guide page at 110 dpi and visually inspected all four.
  Headers, footers, equations and complete answer tables fit; no overlap,
  clipping or missing content was observed.
- Checked all four final student PDF pages visually at 80 dpi before authoring
  and cross-checked their coordinates with the final authored student data.
- Rebuilt a standalone copy with only the four authored guide-source files;
  extracted PDF text matched the delivered guide.
- Created a temporary ZIP of those four files, extracted into a fresh directory,
  and rebuilt using only the extracted files. All four 60-dpi rendered PNGs were
  byte-identical to corresponding renders of the delivered guide.
- Intermediates and the temporary test archive are confined to the run's `tmp/`
  and the output build directory; they are not part of portable guide source.

## Lineage and limits

Consulted the owned Week 78 mathematical research and independently checked the
final examples. Verified primary-source pages for the min-plus line convention
and the point-line-incidence follow-on:

- Speyer and Sturmfels, *Tropical Mathematics* (2004), §§1 and 3:
  https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf
- Tewari, *Point-Line Geometry in the Tropical Plane* (2020), §§3–4:
  https://arxiv.org/abs/2006.04425

The second source uses max-plus; the guide warns that its arms are reversed.
No downloaded papers or borrowed figures are packaged. Physical handling and
material rehearsal, classroom piloting and observed learning outcomes remain
unperformed. No commits, pushes, student edits or additional production stages
were undertaken in this guide-writing stage.
