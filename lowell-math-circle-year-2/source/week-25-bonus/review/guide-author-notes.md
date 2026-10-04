# Guide author record: Week 25

Adult-guide stage only. Base, student, global index and AGENTS files were not edited.

- Final student input: `tmp/worksheet-runs/week-25-bonus-v1/final/bonus.pdf`. Exact input, answer-note, revision-note, math-review and output hashes are recorded in `guide-sync.json`.
- Authoritative guide content: `guide.json`; rendered output: `bonus-facilitator.pdf`, five Letter pages.
- Exactly three genuine investigation groups, using actual printed problem numbers: 1 / 2-3 / 4.
- Mathematical mapping: Six one-per-row/column pictures and one diagonal-shadow collision; adaptive minimum three versus prechosen minimum four cell queries; row-subset capacity obstruction for binary margins.
- Current staffing is explicitly stated: fixed KK11 / 3333 / 445 tables, one anchored adult each, one investigation and its launch per table visit. Adults read/record while children own choices. No extra adult is assumed. Week24 pools complete casework and reuses nine ordered outcome cards per deck, retaining multiplicity.

Read every final student task through the actual PDF and synchronized final answer/revision notes, plus the separate student math review. Re-derived proposed kernels and guide explanations. The range design checks are in `plans/encore-18-34/check_design_24_29.py` and `plans/encore-18-34/design-24-29-checks.json`; they are supporting author checks, not a substitute for the fresh guide review.

All current guide pages were rendered at 110 dpi with the shared helper and visually inspected. Every changed page was inspected again after the staffing addition; Week27's corrected switch extension was also inspected. No clipping, overlap, missing glyph, outside-page text or broken section flow was found. The latest geometry report has no issues. `guide-checks.json` records the scope of these checks. The shared builder was not edited.

Sources actually read: Week01 encore source/model; actual Week24-29 base packets and guide/outline material; current final student packets; Rozhkovskaya, Math Circles for Elementary School Students, Introduction (downloaded EPUB OEBPS/part0010.xhtml), Lesson12 Symmetry/One Mirror/Two Mirrors/At the lesson (part0022.xhtml), and Lesson13 Gnomes/At the lesson (part0023.xhtml). Guide sources distinguish relevant directly read passages from mathematical references merely attributed in the base. No fresh reading of cited external paper bodies is claimed.

Independent status: the student tasks have separate fresh math reviews. The adult-guide audit is underway separately. Its Week27 correction was applied: from minimum AY/BZ/CX, forming BX breaks BZ and CX, leaves C/Z unpaired, and preserves AY; CZ then completes the stable matching. All other fresh audit findings, if any, remain release checks. Root owns packaging and extracted portable-source rebuild verification; neither is claimed here.

Counter/grid fit, covers and retaining one hidden reference while answering occupied/empty are unrehearsed. Staffing and pacing have not been physically rehearsed or piloted. All bonus materials remain unpiloted. Timings in the guide are proposals, not observed results.

Rebuild this guide:

```sh
tmp/encore-18-34-venv/bin/python tmp/encore-18-34/tools/build_guide.py tmp/encore-18-34/guides/week-25/guide.json tmp/encore-18-34/guides/week-25/bonus-facilitator.pdf
```
