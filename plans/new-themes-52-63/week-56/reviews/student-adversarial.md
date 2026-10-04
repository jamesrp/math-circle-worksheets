# Week 56 adversarial student/preparation review

Fresh critic stage, October 4, 2026. Reviewed the actual **nine-page `draft/students.pdf` and four-page `draft/materials.pdf`**, following the combined-packet override in `plans/new-themes-52-63/STAGE-ROUTING.md`. Read the run's PROMPT.md and CRITIC.md, root README.md and REPUBLISHING.md, and the relevant sources. No draft or source edits were made. An independent mathematics reviewer separately checks all solutions and geometry; this report does not stand in for that review.

## Verdict

**Targeted revision, with the investigation and upper continuation retained.** The draft has a substantial concrete core, an honest optional younger entry, several useful contrasts, and worthwhile general explanations. It does not need a wholesale redesign or three duplicate grade packets. The principal correction is the fan-closure question on page 3. The count invariant also needs a small bridge to the existing contrasting model data, and the upper universal statements should name their polygon-face domain.

All thirteen actual pages were rendered with PyMuPDF at 108 dpi and individually inspected. No clipping, text/diagram collisions, missing glyphs, or page-boundary overflow were found. The preparation sheets are adult cutting/assembly assets, **not four additional student investigations**. Physical handling, assembly fit, and classroom use remain untested.

## Located issues and minimum fixes

### R1 — Correct the two fan-closure tests before children use them

**Student page 3, Problem 3; `draft/src/students.tex:143`. Priority: high.**

“Which groups lie flat?” is not the intended contrasting test: every listed group can lie flat as an **open** fan, which is exactly the configuration the children then draw. The difference is whether the free sides can meet while flat. Likewise, “pointed corner” has no no-dents condition at this point; convexity is first explained on page 7. The outline's intended conclusion concerns convex corners, so a pleated or inward-folded attempt should not acquire its legality from an unstated adult interpretation.

Minimum wording change: **“Which groups can close into a pointed corner with no inward dents? Which can close flat? Make each group, then draw its gap with the corners laid flat.”** This states the essential closure conditions while preserving all six experiments and leaving construction, comparison, and organization to the children. The existing worked fan visual should stay. Put discussion of positive gaps as a necessary local condition, rather than a guarantee of a whole solid, in the later adult guide.

### R2 — Connect the Euler investigation to the different solid inventories

**Student pages 1 and 6–7; `draft/src/students.tex:101–110, 202–222, 246`. Priority: medium; instructional gap, not a claim that the activity has failed in class.**

Page 1 obtains four genuinely contrasting `(V,E,F)` inventories. However, the first printed use of `V-E+F` on page 6 compares only the original cube with three redrawings of that same cube. Page 7 then asks for a fact about every closed convex solid. The children have the relevant data, but the packet never asks them to use those different models to test the count conjecture before explaining it. The total-gap strand handles this better: page 4 compares four models and page 5 adds unequal vertex types.

Minimum fix: make page 6's task explicitly include **the four models counted in Problem 1**, alongside the three cube redrawings. A short clause such as “What is `V-E+F` for the four models in Problem 1?” can precede the existing change question. Children can reuse their first-page records and the existing workspace; no new counting worksheet, supplied answers, or directed proof steps are needed. Alternatively, add a compact four-model comparison record at the appropriate point. Preserve the independent redrawings and the zero-gap question.

### R3 — State the polygon-face assumption in the upper universal prompts

**Student page 7, Problem 7; page 8, Problem 8; page 9, Problem 9; `draft/src/students.tex:246, 279, 285`. Priority: medium; precision.**

“Closed convex solids” includes curved bodies for which this packet's polygonal face/edge/corner counts and face-angle gaps have not been defined. The source README correctly specifies a finite convex polyhedron (or an appropriate sphere cell decomposition), but the printed universal claims are broader.

Minimum fix: use **“closed convex solids with polygon faces”** in these prompts, or introduce “polyhedron” with its short meaning and use it consistently. Keep the whole-edge, two-face-incidence assumptions in the adult theorem-first overview. No counterexample worksheet or extra elementary restriction is needed.

### R4 — Remove an unnecessary measurement direction

**Student page 4, final sentence of the opening rules; `draft/src/students.tex:152`. Priority: low.**

“Measure the flat face corners” suggests an angle-measuring procedure, although the relevant angles are supplied immediately before it and the material list includes no protractor. It also prescribes a method that is not necessary to the task. Delete that sentence. The worked two-triangle input/intermediate/output example already demonstrates the intended angle calculation without revealing a model's total gap.

## Page-by-page coverage

| Actual PDF page | Inspection and mathematical role |
|---|---|
| Students 1 / Grades 2–5 | Clear closed-model rules; shared sides → assembled edge → assembled vertex visual appears before counting. Four physical solids supply hidden faces, so the small perspective drawings need not bear that inference. Legible table and sufficient recording space. Counting is preparatory to the substantive comparisons, not a complete standalone destination. See R2. |
| Students 2 / Grades 2–5 | Side incidence and corner incidence are meaningfully contrasted. Cube and octahedron each have 24 separate face corners but different assembled vertex counts, giving the second question a concrete counterexample. Reuses the four models; no unexplained net counting. |
| Students 3 / Grades 2–5 | Six contrasting physical fans, including zero-gap cases, support substantial experimentation. Marked common vertex and a completed non-task worked visual precede use. Circles on this student page are records; the supplied 80 mm circles are the physical mats. Correct the closure tests in R1. |
| Students 4 / Grades 2–5 | Four regular/equal-type models allow the children to find the same total through different local gaps and vertex counts. Degree arithmetic follows concrete fans. Good non-target worked example and generous record space. See R4. |
| Students 5 / Grades 2–5 | The square pyramid is a valuable additional contrast: four base vertices and one top vertex have unequal gaps. Closed model is supplied; the base is not to be inferred from the thumbnail alone. Top/base labels and table are clear. |
| Students 6 / Grades 2–5 | Diagonal, center subdivision, and inserted edge vertex are different operations; the page explicitly changes counting conventions for a redrawn surface. The zero-defect question retains real reasoning. Source preparation instructions correctly reset each case to the original cube. Keep them. See R2. |
| Students 7 / Grades 4–5 | Opened tetrahedron → plane drawing → tree gives a concrete bridge, and the cube drawing leaves children a different case. All vertices and bounded regions are visible; extra workspace is labelled correctly. The example does not print the alternating-count answer or its cancellation explanation. Substantial adult-supported proof continuation. See R3. |
| Students 8 / Grades 4–5 | Five-sided polygon → three triangles → angle sum is an explicit first-use bridge with equal x/y scaling. The global gap explanation is left to the child, with room for drawings and algebra. Retain this depth; use prerequisite-based continuation pacing. See R3. |
| Students 9 / Grades 4–5 | Five triangle corners and three regular pentagon corners give two rich reverse problems. Fans show local data without a complete solid. Actual triangles/pentagons have 3/5 sides and appear regular. Does not falsely promise that arbitrary local fans assemble globally. See R3. |
| Materials 1 | Cube's six square faces and tetrahedron's four equilateral faces, distinct tabs, paired seam letters, assembled vertex identities, face numbers, and a 30 mm print check. Legible at inspected resolution; no face/tab overlap in the actual vector PDF. |
| Materials 2 | Octahedron's eight triangles and right prism's two triangles plus three squares. All required closing faces are supplied. Seam/vertex labels and dash/solid distinction are visible; no vector face/tab overlap. |
| Materials 3 | Square pyramid's square and four equilateral triangles, followed by eight marked triangular fan pieces. Nets and loose fan pieces are visually distinct adult preparation items. No vector face/tab overlap. |
| Materials 4 | Eight marked square pieces and two 80 mm full-turn circles. Spacious cutting separation and clear center dots. Squares' far corners extend slightly beyond a 40 mm radius circle when centered at a vertex; that does not prevent the circle from showing the angular gap, but handling remains a physical pretest. |

## Supporting checks and limits

- The writer's verifier ran successfully into `review-assets/author-verifier/`. Independently extracted **actual PDF vectors** confirm all **28 net face polygons** and **16 fan cutouts** have 30 mm edges, with triangle/square interior angles within approximately `0.000031°` of 60°/90°. Both circle diameters are approximately `80.0006 mm`. Evidence: `review-assets/independent-vector-check.json`.
- Independent polygon intersection checks on the actual PDF's blue faces and gray tabs found **no positive-area face/face, face/tab, or tab/tab overlap** above `0.001 mm²`. The sheets contain 24 tabs, distributed 10/10/4 on the three net pages. Evidence: `review-assets/independent-pdf-overlap-check.json`. This establishes printed net separation, not assembled tab handling.
- An extracted lean source ZIP rebuilt **both PDFs**, with equal text, Letter dimensions, and every rendered pixel at the comparison resolution across all 13 pages. Evidence: `review-assets/clean-rebuild/clean-rebuild-check.json`. This check ran entirely under review assets and did not replace the draft.
- Source notes correctly distinguish assembled surfaces from open nets, geometric corners from zero-gap subdivision vertices, observed agreement from a general explanation, and local fan feasibility from whole-solid existence. Source notes honestly state prerequisites, adult reading/recording for an optional younger fan entry, and later visits for pages 7–9. Keep these distinctions in the separately authored guide.
- The later adult guide should retain the shared launch with actual closed models, a realistic five-group fan allocation, three stable adult tables, and readiness-based stopping/return routes. Fifteen small preassembled solids plus reusable fan pieces is a finite preparation load, but the 30 mm pieces, 6 mm tabs, folding/tape stiffness, marker use, and elapsed assembly/session times need an actual rehearsal. Do not claim physical readiness or piloting from this digital review. These handling concerns are hypotheses, not grounds for discarding the investigation.

The report and review assets are the only outputs of this critic stage. There is no requested facilitator guide to review yet, and its absence is not a writer-stage failure.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
