# Week 52 revised student source

This is the revised student packet, F52-S-v2, following the authorized one-combined-PDF stage routing. It is prepared for review, not released or classroom-tested. All 14 investigations and the original grade routes are retained. Wording and TikZ figures were freshly authored around established grid-bracing mathematics. No exemplar passages or reference figures were copied. A hand test is an experiment rather than a proof of ideal rigidity. Pin friction, bar stiffness, diagonal fit and classroom handling have not been physically rehearsed or piloted.

The mathematical model is a complete rectangular grid initially made of square cells, with every side bar present, fixed bar lengths, freely turning pins, and movement in the plane. A brace is a rigid square-length diagonal joining the existing opposite corner pins of one cell, with at most one brace per cell. No missing bars, holes, sliding pins, cross-grid braces or joints at link crossings occur. Under these assumptions a brace fixes the right angle between one row-strip direction and one column-strip direction; connected row/column links force one common whole-frame turn, while separate linked groups permit different turns and a change of shape. This finite-motion conclusion is justified for this model separately from the first-order theorem. It does not describe cardboard stiffness, arbitrary frameworks or out-of-plane folding.

Build with a portable TeX Live installation containing `pdflatex`, `extarticle`, `geometry`, `fontenc`, `helvet`, `tikz`, `fancyhdr`, `xcolor` and `microtype`:

```sh
sh build.sh /absolute/output/directory
```

The command creates only `students.pdf` in the chosen output directory and removes its temporary build intermediates. It does not depend on repository files or downloaded sources.

The authored check helpers run as follows. `verify_math.py` uses only Python's standard library; the PDF checks require `pymupdf` (PyMuPDF). `render_verify.py` creates page PNGs and checks page dimensions, all grade headers, text bounds and consecutive numbering. Its checks complement visual inspection of every page. `audit_pdf_math.py` re-runs the independently authored mathematical review's actual-PDF geometry, finite-flex and enumeration audit; only input/output routing was adapted for this portable source. `clean_rebuild.py` checks both a complete copied-source build and a ZIP-extracted-source build, from fresh directories and a different working directory, comparing every page's text, dimensions and rendered pixels; it removes temporary builds and the test archive when done.

```sh
python3 verify_math.py --output /absolute/output/math-checks.json
python3 render_verify.py /absolute/output/students.pdf /absolute/output/render
python3 audit_pdf_math.py /absolute/output/students.pdf /absolute/output/actual-pdf-math-checks.json
python3 clean_rebuild.py /absolute/output/students.pdf /absolute/output/clean-rebuild-checks.json
```

## Page prerequisites and routes

- Pages 1–2, approximate Grades K–1: adult reading, manipulation of preassembled models, distinguishing a change of shape from moving the entire object. No arithmetic is needed; counting one brace is optional. Adults assist with pins; children choose the shape or placement. These are genuine physical entries, rather than a full separate younger-level session.
- Pages 3–4, approximate Grades 2–3: adult or independent brief reading; count up to four; retain the same cell positions while reproducing a design. Children use a preassembled complete 2-by-2 model.
- Page 5, approximate Grades 3–5: the same demands, now a 2-by-3 model and counts up to six. The extra spatial choices justify its different task.
- Page 6, approximate Grades 3–5: retain two label systems and convert braced cells to row/column links after the explicit non-task visual. Children make and test both designs on the standard 2-by-3 model; this is experimental evidence, not yet the general criterion.
- Pages 7–9, approximate Grades 3–5: retain the strip directions and labels, trace groups of linked dots, and reason about a single change from an unchanged reference design. These pages require the physical-to-link handoff below before using links to decide a paper-only frame's behavior. Page 8 can also be tested directly on the standard 2-by-3 model. Pages 7 and 9 use an optional additional rehearsed 3-by-3 model or the justified strip-direction explanation; the printed maps do not claim physical testing. There is no algebra or calculus.
- Pages 10–12, approximate Grades 4–5: explain why a design is minimal or a statement must hold. Small sums and products support possible arguments; the child can use drawings instead. These pages concern ideal complete grids and require readiness for connectivity arguments. They are reasonable return-visit material.

All maps have equal axis scales and are deliberately smaller than the kit. Kits use 60 mm hole-center side bars and 60√2 mm hole-center diagonals. The opening identifies the diagrams as recording maps. Numbering is consecutive within the combined packet. A short whole-group physical launch precedes distribution, as required by the supplied outline; student instructions rely on that live demonstration.

## Required physical-to-link handoff before page 7

This is a source route and prerequisite for the later guide, not evidence that a demonstration has been rehearsed. Keep page 6's worked frame → labeled cell → link visual before the first conversion. After its physical comparison, return to the already available 2-by-2 frame from Problem 4B, with braces in (R1,C1) and (R2,C2); retain that brace record. Borrow the standard 2-by-2 kit after its group finishes. Alternatively, the upper table's standard 2-by-3 kit can use (R1,C1), (R1,C2), (R2,C3): it also covers every strip and has exactly two linked groups. This alternative needs no borrowed or additional kit.

Put R1/R2 tabs beside the vertical side bars across the two row strips and C1/C2 (also C3 for the alternative) beside the horizontal side bars across the column strips. Children choose gentle flat pushes and identify which bars remain parallel as the cells become parallelograms. In this complete equal-sided grid, opposite bars of each cell remain parallel near the starting placement, so all vertical bars in a row strip share a direction and all horizontal bars in a column strip share a direction. The row/column labels therefore describe actual bar directions, not only cell addresses. A braced cell remains two fixed triangles, keeping its row direction perpendicular to its column direction.

Children draw the matching links and check that the two braced groups can turn relative to one another even though every row and column is covered. They choose an empty cell for one added brace, predict what it will couple, and test their choice; the adult services the pin without choosing the cell. In either comparison, every available empty cell links the two formerly separate groups and fixes their relative directions. Children retain the choice of push, addition, record and explanation. The adult supplies the geometric fact about parallelograms and the meaning of the tabs as needed, rather than performing the whole investigation.

Advance to page 7 only when children can connect a cell brace to its two directions and distinguish a tested observation, a prediction for a new frame, and an explanation from the ideal fixed-bar model. Linked right-angle relations propagate through a group; disconnected groups can be assigned different small turns. That geometric reason supports using the links for the later paper-only designs. If children are still converting addresses without this meaning, continue the physical Problems 4–7 or return another day; page completion is not a prerequisite. The optional 3-by-3 physical comparison can add experimental evidence after material rehearsal, but does not replace the explanation. Pages 10–12 also require this handoff and readiness for a universal/minimum argument.

## Mathematical and pedagogical sources

The exact statements, limits and separately justified finite-motion argument are in `plans/new-themes-52-63/week-52/research-notes.md`. The two primary mathematical references are Ethan D. Bolker and Henry Crapo, “Bracing Rectangular Frameworks. I,” *SIAM Journal on Applied Mathematics* 36(3) (1979), pp. 473–490, DOI 10.1137/0136036 (publisher abstract; full original paper unavailable), and Georg Grasegger and Jan Legerský, “Bracing frameworks consisting of parallelograms,” arXiv:2008.11521v1 (2020), Theorem 1.1 p. 3 and finite-flex argument pp. 16–17. The elementary grid-specific proof in the research notes is newly written.

The research notes cite concrete polygon work reported in Rozhkovskaya's *Math Circles for Elementary School Students*, Lesson 7, “At the lesson,” §2, printed p. 122; the accessible manipulative teaching discussion in Givental, Nemirovskaya and Zakharevich's *Math Circle by the Bay*, “How we teach,” p. ix; and the organizer's first-year physical shape tasks. Those are teaching precedents, not pilots of this adaptation. `REPUBLISHING.md` was read; the writer did not reuse its identified borrowed exemplars.

## Revision and verification scope

Problem 3 asks whether the same removed diagonal fits a changed four-bar shape; it has no minimum-count request. The minimum-design tasks remain explicit in Problems 2, 5, 6 and 12. The youngest opening no longer contains fabrication dimensions. Problems 8 and 11 have more separation between their link drawings and response lines. Problem 8 explicitly asks for both link drawings before deciding its universal question. A later facilitator guide must supply its own theorem-first overview and independent review; this revision stage creates only student pages and source notes.

Fresh extraction, renders and reports belong beside this source in the final output's `render/` and check files, never inside `src/`. The stale draft extraction is not current evidence and is not copied. A clean copied-source build and an extracted source-archive build must reproduce every page's text, dimensions and rendered pixels. These digital checks verify neither physical fit/handling nor classroom piloting, both of which remain unperformed.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
