# Week 59 revised student source: constant width

This is one combined six-page student packet and a three-page materials packet,
authored for the fresh writer and revision stages. The draft received separate
adversarial and independent mathematical reviews; the revision addresses their
two required convention changes. It remains unpiloted. No facilitator guide was
authored here. All source files in this directory are original prose,
LaTeX/TikZ, geometry, or verification code. The established mathematics is not
claimed as newly invented.

## Build and check

From any directory, using Python 3 and `pdflatex` on PATH:

```sh
python3 /path/to/student/build.py /path/to/output
python3 /path/to/student/verify_math.py /path/to/output
python3 /path/to/student/verify_rebuild.py /path/to/output
```

The build writes `students.pdf`, `materials.pdf` and an `.build/` directory inside
the supplied output directory. It never writes LaTeX intermediates into source.
The verifier requires PyMuPDF (`pymupdf`); building uses only Python's standard
library. Tested here with `/Library/TeX/texbin/pdflatex` and
`tmp/bonus-35-51-venv/bin/python`. Standard TeX packages: `geometry`, T1 `fontenc`,
`helvet`, `tikz` with `arrows.meta`, and `fancyhdr`. No external images or downloads
are needed. All diagrams are built with equal x/y millimetre units.

`verify_math.py` audits every authored nominal arc/polygon and the task answers,
then measures compiled PDF paths, including every depicted Reuleaux triangle,
the full-size cutouts, template dimensions, the 200 mm grid and all 100 mm bars.
PDF circles/arcs use TikZ's cubic approximation of nominal circular geometry;
the audit reports this small digital deviation separately from physical errors.
Numerical checks do not replace the all-direction proof in mathematical-notes.md.
The revision also checks the non-task off-center rectangle, its marked point,
whole-body supporting line, perpendicular segment, right-angle marks and matching
32 mm record. The original construction, material geometry and output-directory
build command are preserved.

`verify_rebuild.py` copies the nine explicit source files into a clean directory,
creates and extracts a lean check ZIP, and rebuilds both PDFs in each environment.
It compares every page's text, dimensions and rendered pixel hash at 108 dpi.
Its ZIP is a QA artifact, not a publication or an approved release. QA outputs
remain beneath the supplied output directory. Prompts, exemplars, books,
reference PDFs and render images are excluded from the source ZIP.

## Prerequisites and route

| Pages | Approximate band | Required actions and reasoning |
|---|---|---|
| 1–2 | Grades 2–5 | Choose and retain shape positions; understand touching parallel supports and perpendicular gap; compare whole-mm ruler readings up to about 85. An adult may read or record and help keep rails parallel, while children choose positions and make the mathematical comparisons. |
| 3 | Ready Grades 3–5 | Understand an equilateral triangle and a compass opening as a fixed radius; choose/test the predicted width. Adult management of compass points and cutting is needed. |
| 4 | Ready Grades 3–5 | Use radius/tangent perpendicularity and the three construction centers to explain an invariant over all orientations, beyond a finite set of measurements. The universal support argument is substantial and readiness dependent. |
| 5 | Ready Grades 3–5 | Measure the perpendicular distance from a marked point to a support line; distinguish this distance from total width. No axle or rolling procedure is needed. |
| 6 | Ready Grades 4–5 | Relate three one-sixth arcs of a radius-60 circle to the full boundary of a radius-30 circle. Fractions and length scaling by two are needed; knowledge of pi is optional. |

No K–1 printed route is fabricated. These pages can support several visits:
the physical comparisons stand on their own; construction, all-turn explanation,
marked-point comparison and exact boundary comparison remain available for
later use. This is source routing information, not a tested session schedule.

## Physical preparation and unresolved pretests

For five pair kits, print five copies of materials page 1 at **100%**, single-sided
US Letter, and make six pieces per kit in flat 0.5–1 mm stiff card: a 60 mm diameter
disk (marked O), 60 by 40 mm ellipse, 60 mm square, 60 mm equilateral triangle,
60 mm-width Reuleaux triangle, and a second Reuleaux triangle marked at the
underlying equilateral centroid. Cut the middle of the thin boundary outline.
Dimensions/captions outside the boundaries are not part of the cutouts. The
square is an added contrasting control, beyond the research outline's four.

Supply two straight 300 mm rulers/rails with at least 100 mm contacting edges,
one 150 mm measuring ruler, two movable right-angle guides, one printed 200 by
200 mm grid mat (materials page 2), pencil and blank paper per pair. The shape
lies flat and is free to translate as it turns. The rulers are laid flat as two
parallel enclosing edges. There is no fixed center pin. At upper tables, the
third child can check contact and swap roles. Three adults are available, one
at each table. Before printed tasks, let children handle the pieces and use a
brief whole-group demonstration of legal parallel contact and a perpendicular
measurement, using the first-page visual convention.

When measuring width, adjust both edges into contact. In Problem 2, keep their
gap fixed at 60 mm while the shape turns and slides; gaps between an edge and the
piece are legal fitting positions. These are different procedures. Problem 5
uses only one supporting edge and the perpendicular distance from the mark O;
the new off-center marked-rectangle visual precedes that task.

For Problem 3, six adjustable compasses and adult-managed scissors are optional.
Print three copies of materials page 3 for six templates at each size. Children
draw the three minor arcs on the appropriate templates; an adult can cut the
new pieces. Construction is a continuation, not a required entry gate.

**Unperformed:** actual printer 60/100/200 mm checks; cutting precision and
smoothness; full rail clearance and contact while turning; retention of the
parallel/perpendicular convention; right-angle guide handling; compass stability;
marked-point-to-edge measurement; timing; classroom piloting. A trial might consider an apparent-width tolerance
of ±1–2 mm, but no tolerance has been established or tested. Exact-fit claims
apply to ideal geometry; the 60 mm fixed-gap experiment needs a real print/cut
pretest. Paper line thickness, nearest-mm readings, cutting and contact error
are experimental limits. No thin-card roller, platform, axle or square-hole
demonstration has been built or tested.

## Provenance and scope

Read `mathematical-notes.md` for exact construction, checks and source references.
The writer read the Week 59 research/outline/novelty/audit notes and root
`REPUBLISHING.md`; that file was preserved. ThinkMaths labels its activity KS3–5.
Its existence does not pilot this elementary adaptation. No borrowed source
prose, figures, assets or workflow exemplars are included in the authored files.
Nothing was published, uploaded, committed, or moved into the approved library.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
