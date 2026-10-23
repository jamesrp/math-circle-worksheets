# Week 92 adversarial review

Reviewed the consolidated `draft/students.pdf`, all six pages rendered independently with PyMuPDF, plus `draft/src/students.tex`, `verify.py`, and `build.py`. This is the critic stage only; no student files were edited. The run-specific override authorizes no K–1 packet and one consolidated six-page packet; those are not defects.

## Overall judgment

The mathematical content is sound, the examples are purposeful, and the pages are restrained and legible. Keep the investigation, including its ambitious final questions. Revise the operational support before treating the draft as ready: the requested reusable physical rule aid is missing, and Problem 8 does not give children an unambiguous way to distinguish the images of its separate starting pieces. The change of scale on page 5 also needs a clearer visual bridge. These are specific usability concerns, not evidence that the underlying theme is unsuitable for children.

## Findings, in priority order

### 1. High priority: the worked point example is not the reusable apparatus requested by the brief (page 1)

The input at 13, distance 3, and output at 6 correctly demonstrate one calculation. But the delivered equipment is still a set of ordinary tracks. For every new marker position children must decide the nearer end, find a distance, double it mentally or with a ruler, and transfer the result. Nothing physically connects a general input to its legal output. There is no folding overlay, doubled-scale output aid, V-shaped input/output map, or reusable matched strip system. The instruction “measure ... distance” is also easy to interpret as measuring centimetres or millimetres, although the result to double is in track units.

This matters directly given the supplied classroom evidence: the previous paper-only rule needed repeated adult intervention. A successful worked arithmetic example is insufficient evidence that pairs can sustain the action themselves, especially when moving a continuous band rather than a single whole-number point.

Revision target: include a reusable, mechanically clear input-to-output aid that works for arbitrary points, including between ticks, and can be used on a whole strip. A correctly labelled tent/V mapping with an explicit projection convention, or an actual matched/folded strip apparatus, would satisfy the outline. Keep the existing non-task 13 → distance 3 → 6 worked visual, integrating it with that aid. Make track units explicit without a long explanation. Do not replace this with additional prose about doubling or many worked answers. The apparatus still needs physical rehearsal; do not claim that drawing it certifies classroom readiness.

### 2. High priority: Problem 8 can be completed by moving the union instead of each piece (page 6)

Each starting row shades the entire track in the same pale colour, with divider lines into 2, 4, or 8 cells. Each row then provides one unlabelled “After the moves” track. The words say “For each shaded piece,” but the visual recording affords one answer for the whole row. Moving the union gives the whole track immediately, without investigating the intended fact that **each individual small piece** covers the whole track after the corresponding number of moves. Once a child shades the output track for the first cell, the page cannot show whether the others were considered.

Revision target: make the separate starting pieces identifiable and their individual results recoverable. This need not mean a fourteen-row diary: use movable, labelled pieces and a compact keyed collection, or a small contrasting selection plus space to pool the remaining cases. The final explanation should still concern every piece in a subdivision. Preserve the open mathematical question; do not print the induction as a procedure. Visually show shared endpoints as included, consistent with the band rule.

### 3. Medium priority: the new scale on page 5 is only named, not visually connected

Problem 6 moves from a 160-mm track representing 0–16 to equally long lines representing 0–1. The labels are mathematically correct, but there is no bracket or connector from the first unit of the full track to the enlarged view and no worked use of the new convention. This is an important change precisely when children first need fractions of one track unit. They can easily place a correct-looking length on the enlarged line and then apply the physical move rule at the wrong scale.

Revision target: add a small explicit bridge from the 0–1 segment on the full track to the enlarged line, with one non-answer position shown in both views. Make clear that the enlarged lines record starting bands and that moves still use the original 0–16 rule. Preserve the task of finding the widest band; do not pre-divide the answer lines into quarters, eighths, and thirty-seconds or give away repeated halving as a required method.

### 4. Medium priority: distinguish the proof continuation from the common upper-band route

Page 6 asks children to explain both arbitrary dyadic subdivision and eventual coverage for every nonzero interval, including intervals with endpoints between ticks. This is substantial and appropriate to retain as a readiness-dependent continuation. It is materially more demanding than simply applying the rule to the bands on pages 2–3, yet its header is indistinguishable from the rest of the upper-band work. The outline explicitly calls for an honest readiness-dependent continuation.

Revision target: make the page header identify it as an upper-band continuation while retaining the required week/topic/level format, or otherwise clearly identify the intended stopping boundary in the eventual adult packaging. Do not weaken the problems or add a student-facing recipe for the proof. With the research mathematician at this table, a concrete subdivision argument is plausible; independent completion by every fourth grader is not established.

## Page-by-page audit

- **Page 1, Grades 2–3, Problem 1:** The rule and 13 → 3 → 6 example are correct. The visual has input, intermediate quantity, and output before use. The paired goals are mathematically connected: finding merging starts followed by sustained separation gives a useful contrast. There are exactly eight unordered merging pairs of distinct whole-number starts. Two 160-mm tracks support token experiments; open space permits recording the pairs. The missing reusable apparatus is the principal concern. A “pair” can reasonably mean an unordered pair here; no need for extra combinatorial terminology.
- **Page 2, Grades 2–3, Problem 2:** Strong example choice. The non-task interval [5,10] visibly includes 8 and maps to [10,16], with the two endpoints and midpoint explicitly tracked. This meets the requirement to introduce whole-band images before the first task. The four tasks include a left-half band, a right-half band, an asymmetric crossing band, and a symmetric crossing band. The statement about one fixed unknown start avoids random resampling. The final answer line is low on the page but remains above the footer; no clipping was seen. The thin pale shading merits a real grayscale print check, but this is not an observed defect.
- **Page 3, Grades 2–3, Problem 3:** Both supplied bands first cover the track after four moves, and each has exactly four answer tracks. They offer meaningfully different behaviour: [1,2] doubles on each step, while [7,9] initially keeps its width and then grows. The provided record externalizes state without a second tally. Three lower-band problems across three pages are acceptable under this run's override; whether this fills the actual table's available time is an unpiloted pacing question, not grounds to add filler.
- **Page 4, Grades 4–5, Problems 4–5:** The endpoint counterexample and request for two further bands are correct. Problem 5 asks the right substantive question and allows an object/drawing explanation. A nonzero symmetric interval around 8 keeps its width; other nonzero intervals grow. The pages do not falsely claim that every interval grows strictly or that pair separation never shrinks. Page 4 explicitly depends on the rules and examples on pages 1–2, so the consolidated packet must be distributed accordingly; it is not a self-contained three-page upper-band handout.
- **Page 5, Grades 4–5, Problems 6–7:** The optimization is well posed and meaningful, and “through the first ... moves” correctly requires containment at intermediate times. The enlarged lines make tiny intervals drawable. The maximum right endpoints are 1/4, 1/8, and 1/32. The bridge between the two scales needs revision as described above. Problem 7 generalizes the finite experiments without requiring formal powers notation.
- **Page 6, Grades 4–5, Problems 8–9:** Correct mathematical destinations and a worthwhile connection between subdivisions and eventual uncertainty. The individual-cell/whole-row ambiguity is significant. Preserve both questions after fixing the representation and identifying the continuation. The supplied space is enough for a short drawing or explanation, with larger arguments naturally continuing on the available whiteboard; there is no need to force a formal proof into a table.

## Mathematical verification

Ran the supplied exact-arithmetic verifier successfully and independently checked the specific task data with rational arithmetic.

- Move rule: T(x) = 2 min(x,16−x), on the closed track [0,16].
- For [a,b], the minimum output is min(T(a),T(b)); the maximum is 16 when a ≤ 8 ≤ b, and max(T(a),T(b)) otherwise. Continuity gives the entire interval between these extremes.
- Problem 1 merging pairs: (0,16), (1,15), (2,14), (3,13), (4,12), (5,11), (6,10), (7,9). Starts 0 and 1 have separations 1,2,4,8, so the three successive increases are achievable. Starts 1 and 2 do as well.
- Problem 2 output bands, in order: [2,8], [2,12], [10,16], [4,16].
- Problem 3 first sequence: [1,2] → [2,4] → [4,8] → [8,16] → [0,16]. Second: [7,9] → [14,16] → [0,4] → [0,8] → [0,16].
- Problem 4: [6,10] maps to [12,16], not the singleton {12}.
- Problem 5: on one half, width doubles. For a crossing interval [8−u,8+v], output width is 2 max(u,v), at least u+v, with equality exactly when u=v. A zero-width band is a separate trivial equality case; Problems 7 and 9 appropriately require some width.
- Problems 6–7: for n ≥ 1 the widest permitted initial band is [0,2/2^n]. A wider [0,b] cannot exploit the fold to evade an intermediate-time restriction: to have its first image contained in [0,2], b must be at most 1, and subsequent permitted images remain on the doubling branch. A positive-width band exists for each finite n.
- Problem 8: each closed cell [16k/2^n,16(k+1)/2^n] maps onto [0,16] after n moves. The affine branches of T^n alternate direction. The exact verifier checks every cell through n=9; the general claim additionally follows by folding/stretching induction, not by that finite test alone.
- Problem 9: every positive-width interval contains a sufficiently small complete dyadic cell. Its image therefore contains the whole track after that cell's corresponding number of moves and cannot exceed the track. The image is exactly the track. This is an explanation of the universal fact, distinct from experiments on grid points.

No task claims that every exact real starting point reaches 0, confuses intervals with probability distributions, or promises strict growth on every move. Preserve those distinctions.

## Layout, source, and verification limits

All six rendered pages were inspected. Headers, footers, consecutive Problems 1–9, ticks, endpoint dots, and answer tracks are legible; no text collision or cropped task was observed. The source draws ordinary tracks at 10 mm per unit, hence 160 mm total, and intentionally expands 0–1 to 160 mm on page 5. The draft uses portable TikZ and includes a deterministic build script. This review did not alter or rebuild the PDF, reconstruct a source ZIP, rehearse an apparatus, print on a physical printer, or pilot the lesson. The revision stage must rebuild and inspect its changed PDF, and any later claim of physical readiness needs separate evidence.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
