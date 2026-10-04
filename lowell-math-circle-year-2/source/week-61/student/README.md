# Week 61 revised student packet: Triangles on a ball

Original editable student packet, revised after fresh adversarial and independent mathematical reviews. One combined seven-page `students.pdf`; no facilitator guide and no K–1 coverage claim. This revision is ready for organizer review and remains unpiloted. The packet can support more than one visit. The upstream workflow prompts are deliberately excluded from this portable source.

## Build

Requires Python 3 (standard library) and `pdflatex` from TeX Live with `article`, `geometry`, `fontenc`, `helvet`, `tikz`, `array`, `fancyhdr`, `amsmath`. No fonts, pictures, downloads or files outside this folder are used.

```sh
python3 build.py /absolute/path/to/output
python3 verify_math.py /absolute/path/to/output/math-checks.json
```

`students.pdf` is placed in the chosen output directory. Generated TikZ, TeX logs and auxiliary files stay in that directory's `build/` subfolder. Build from a copied source folder or extracted ZIP with the same command. Source stays clean. US Letter, single sided, 100% scale. Pictures are schematics, not globe-fitting templates or protractor targets. No extra materials PDF is necessary: the adult supplies accurately marked balls/globes and the physical tools.

`compare_pdfs.py` requires PyMuPDF. It compares all page dimensions, exact extracted text, and rendered pixel bytes at 144 dpi:

```sh
python3 compare_pdfs.py original/students.pdf copied/students.pdf extracted/students.pdf --output rebuild-checks.json
```

## Actual page bands and prerequisites

| Pages | Header | Reading / arithmetic | Reasoning and physical control |
| --- | --- | --- | --- |
| 1–3 | Grades 2–5 | Adult reading is suitable; recognize a right angle. No sums required. The 135° example models the angle record, not an entry arithmetic test. | Fix endpoints, keep string on the surface, distinguish front/back, compare actual surface corners and change a construction. An adult may hold the ball and record children's choices; children must still choose points/routes. |
| 4 | Grades 3–5 | Degree gaps, equal slices, whole-sphere fractions. Divide 360 by 45, 72 and 120, or use equally spaced meridian models. | Preserve poles/equator and the selected triangle; connect a two-corner lune to its northern triangular half. |
| 5–6 | Grades 4–5 | Count overlapping pairs; recognize a pair as one contribution, even though it contains two opposite lunes. Whole-sphere fractions and counted areas greater than one whole; degree-based lune areas. | Keep one recoverable record for eight regions of the same ball. Select both containing and opposite lunes at each corner. Compare the equal octant cells with unequal 80° cells without assuming equal areas. A mathematician adult is anchored at the table. |
| 7 | Grades 4–5 | Add angles through 300, subtract 180 and divide by 720; work with eighths, twelfths and twenty-fourths. | Distinguish experiments on a model, a conjecture from two coverings, and an exact explanation for every allowed triangle. Explain structural pair membership and antipodal equality of area, not just fit three numerical records. |

No equal-band quota. Ready third graders can enter page 4. Return gates: retain physical routes/corners on pages 1–3 until children can make and check their own choices; return to the sphere with page 4 once equal rotations and fractions make sense; use pages 5–6 when children can track overlapping counted areas, possibly in a separate visit. Page 7 is the universal explanation destination. Children may continue concrete covering work alongside this readiness-dependent explanation. Exact angular data are supplied for the 80° map and the three application records; these are mathematical diagrams and records, not exact physical construction assignments. No one needs to extract angles from the flat figures.

## Physical tools and status

Per pair/trio: firm nearly round 15–20 cm ball/globe, stable bowl/ring, two flexible 80 cm strings, movable markers, narrow paper right angle, washable marks and pencil. Retain the third side of a triangle with a washable arc or another string so all three sides remain recoverable. Pages 3–4 use a model whose equator and meridians have been checked. Page 4 needs marked meridian pairs separated by 45°, 72°, 120°; page 5 needs the three mutually perpendicular center-plane circles of the octant model. Page 6 supplies its full-circle 80° geometry on the page. Marking several meridians does not require distributing another printed template.

A lifted string is a chord, a friction-held loop is not reliable evidence of a great circle, and a flat protractor on the globe is not a surface-angle meter. Page 5 can use removable marks/tallies on the actual regions; the packet supplies the front/back record. Upper covering views show the same ball from opposite sides, perpendicular to one side plane, with four complete cells on each hemisphere. They omit hidden projected arcs. The boundary points are labelled in both views. Earlier oblique diagrams retain dashed back arcs under the opening convention.

The actual ball/string/marker/paper-corner/meridian handling pretest and classroom pilot remain **unperformed**. Numerical and rendering checks do not establish physical readiness. Before classroom use, separately rehearse string contact, stable supports, opposite markers, a known right-angle corner, calibrated meridian gaps, the region/lune tally, and removal of markings. This source note records the operational gate; it is not a facilitator guide.

## Provenance and checks

See `source-notes.md` for the exact mathematical scope and proof, prior library overlap, scholarly and pedagogical precedents, and original wording/figure authorship. `verify_math.py` checks coordinates, angles, areas, open-hemisphere containment, eight regions and six-lune multiplicities. The fresh critic and independent math reviews were completed on the preceding draft. This revision also has an independent reconstruction of final emitted paths, fills, IDs and the patch count, every rendered final page inspected, and exact copied/extracted source rebuild comparisons; the evidence lives alongside the run, outside this lean source. Digital checks do not establish physical readiness or successful classroom use.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
