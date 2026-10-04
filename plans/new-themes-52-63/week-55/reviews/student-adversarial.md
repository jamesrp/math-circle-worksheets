# Week 55 fresh adversarial student review

Reviewed October 4, 2026. **Verdict: retain the investigation and make two small convention revisions before release.** No incorrect task, sum, grid value, bound, or equality condition was found. The concrete entry is credible for children with the stated prerequisites; that is a design assessment, not a classroom result or source-supported age validation.

## Scope and evidence

This is the critic stage only. I read `AGENTS.md`, root `README.md`, `REPUBLISHING.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, `PROMPT.md`, and `CRITIC.md`. The direct routing supersedes the harness's three-PDF/four-pages-per-band defaults: the actual deliverable is one combined [draft/students.pdf](../../../../tmp/worksheet-runs/week-55-new-v1/draft/students.pdf), ten US Letter landscape pages. The absence of a K–1 packet is expressly authorized and is not a defect. I did not author or revise student pages or a facilitator guide, change workflow prompts, publish, or make remote writes.

I freshly rendered the actual PDF at 108 dpi and inspected **all ten pages**, including every header, footer, card value, result lane, and all three page-8 grids. I read all seven files in `draft/src/`. Evidence produced for this review is under `critic-evidence/`:

- `render/page-01.png` through `render/page-10.png`: images actually inspected.
- `pdf-checks.json`: all ten headers/footers/problem labels, landscape page dimensions, every input value and grid label, and all 380 result cells checked against the PDF.
- `math-checks.json`: separate critic calculations of every fixed trial, all legal 0–9 designs for the printed sizes, the complete Problem 5 catalog, and every route in the three grids; it also records the reviewed PDF/source hashes.
- `rebuild/rebuild-checks.json`: I reran the copied-source and ZIP-extracted-source build. Both reproduce all ten pages' text, dimensions, and rendered pixels at 108 dpi. This verifies this draft's build, not a future revised release package.

The independent mathematics reviewer remains a separate stage. This review does not replace that stage or release verification.

## Required student revisions

### R1 — Define numerical equal spacing at first substantive use (page 6, Problem 6)

The first substantive use says, “Each input is equally spaced,” but numerical equal spacing has not been defined. The earlier cards are all drawn at identical physical separations, including the deliberately irregular input 0,1,3 on page 2. The page therefore leaves a real representational ambiguity: the relevant gaps are differences between **ordered card values**, not the physical spacing of card drawings. Page 10 later relies on this meaning again.

**Revision requirement:** give one brief essential definition beside the first use, making clear that neighboring values in increasing order have the same difference. A small non-task numeric example may illustrate the term if useful; a full number-line activity or a printed method for finding extremizers is unnecessary. Preserve the four contrasting trials and the open question about whether equal spacing in each input suffices. Do not print the common-gap conclusion as a procedure.

This is a clarity finding about the printed representation. Whether children would infer the intended meaning from the current page is unpiloted.

### R2 — Bridge visible input counts to `m`, `n`, and the formulas (page 9 before Problem 9; page 10 inherits it)

Page 8 gives a good explicit bridge from cards to row/column sums and a route. Page 9 then first introduces letter counts and immediately asks about `m+n−1` and `m×n`; page 10 adds `m≥2` and `n≥2`. There is no count-to-letter worked example before that first use. The source notes correctly identify algebraic reading as a prerequisite, but a prerequisite note outside the student packet does not supply the required first-use convention example.

**Revision requirement:** before the general task, add a compact non-task visual showing input card collections → their counts labeled `m` and `n` → substitution into the displayed count expressions, or express the general questions in ordinary card-count language if the symbols add no benefit. The example should demonstrate what the letters count and how to read the expressions; it should not enumerate the example's sumset, establish the bound for the child, or prescribe the route-swap proof. Explain the “at least two cards in each input” restriction in ordinary language if the inequality notation remains unfamiliar. Keep the arbitrary-size lower bound and both directions of the inverse theorem.

This implements the project's explicit bridge/first-use convention requirement. It does not assert that Grades 4–5 cannot discuss a general theorem.

## Page-by-page findings

| Page / problem | Actual inspection and task assessment |
|---|---|
| 1 / 1 | Shared rules hold the two inputs fixed, require distinct values within each input, and merge duplicate results. The non-task input → three tries → positions-so-far visual shows two routes to 4 and a new result 1. “Positions so far” accurately marks the example as unfinished: 4+3 has not been attempted. The two printed trials have three and four totals. This is a short gateway rather than a long standalone investigation; its purposeful collision contrast and the immediate deeper continuation justify keeping it concise. Do not pad it with compulsory follow-ups. |
| 2 / 2 | Three contrasts give five, six, and nine totals from nine pairs. They reveal a meaningful distinction between irregularity, common small spacing, and separated sums. Clear next action, legible inputs, full working lanes, and no method prescribed. |
| 3 / 3 | The child chooses both inputs to minimize and maximize the result count. Four recoverable trial records give meaningful room to experiment. The maximum nine and minimum five are both achievable with the 0–9 kit. This is substantial mathematical design, not addition drill. |
| 4 / 4 | Sizes 2+3, 2+4, and 3+4 broaden the conjecture; minima are four, five, and six. Each input size is visible in the slots. One record per size is workable with pencil/eraser and the supplied off-page paper; extra trials can stay with the adults. The rule question is a conjecture at this point, not evidence of a proof. |
| 5 / 5 | Fixed A={0,3,6}, a complete finite catalog goal, eight B/result record spaces, and one reusable result lane. Seven valid B choices fit. Pooling is permitted and sensible for the 45-candidate space. The “you may share…” sentence is optional facilitation and can move to the guide for stricter brevity; it is not a mathematical or usability blocker. |
| 6 / 6 | Four useful common/mismatched-gap examples give counts 4,6,4,4. Shifted starts and a different common gap remain represented. Keep this page, subject to R1. |
| 7 / 7 | Translation by a singleton is concrete, uses both irregular and regular B, and includes A={0}. Counts are 3,3,4. The singleton exception is not lost when the general equality condition follows. Two lines and blank space support a rule stated in words or drawings. |
| 8 / 8 | Shared array rules explicitly order A upward and B rightward. The non-task example shows row value 1 and column value 2, the sum 3, then the correctly labeled grid and route 1,3,7,11. All arrows have a clear role. The two task grids have route lengths five and six and no repeated total along any legal route. Distinct routes can overlap on a single printed grid; an adult may offer erasure, colored pencils, or extra grids if preserving several routes matters. That is optional recording support, not a reason to turn the problem into directed steps. |
| 9 / 9 | The general lower/upper question is mathematically correct for nonempty whole-number sets and leaves the proof method open. Ample writing/drawing space. R2 addresses the abrupt symbolic conversion. |
| 10 / 10 | Both inputs have at least two values; common gap is explicitly required; both implication directions are requested. This preserves the real inverse problem, rather than stopping at a pattern. Large work area and no prescribed proof. R2 supplies the inherited count convention. The local path-swap argument belongs with adult hints unless a child chooses it. |

Every inspected page has the required single header and footer, consecutive Problem 1–10, and no Name/Date fields, duplicate page titles, generic encouragement, or enrichment labels. I found no clipping, overlap, lost numeral, or illegible graph label. The two convention-example blocks are justified exceptions that carry essential rules rather than optional solution scaffolding.

## Mathematical audit

The fixed totals independently checked are:

- Problem 1: {1,3,5}; {1,3,4,6}.
- Problem 2: {0,1,2,3,4}; {0,1,2,3,4,6}; {0,1,2,3,4,5,6,7,8}.
- Problem 6: {3,5,7,9}; {0,2,3,4,5,7}; {1,3,5,7}; {1,4,7,10}.
- Problem 7: {4,5,7}; {2,4,6}; {1,4,6,9}.

The critic enumeration checks 14,400 designs for 3+3, 5,400 for 2+3, 9,450 for 2+4, and 25,200 for 3+4. Their minima are 5,4,5,6. Problem 5 has exactly B={t,t+3} for t=0,…,6, with totals {t,t+3,t+6,t+9}; all 45 candidate B sets were considered. The task grids have 6 and 10 legal routes respectively, each visiting 5 or 6 strictly increasing values. The demonstration grid has 3 routes, each visiting 4 strictly increasing values. Every displayed entry equals its row value plus its column value.

I also audited the general argument in `MATH-NOTES.md`. A sorted monotone array route visits m+n−1 strictly increasing sums, establishing the lower bound; mn pairs establish the upper bound. In the equality case every such route contains the whole sumset. Two full routes differing only inside an adjacent square therefore have equal intermediate sums, which forces every A gap to equal every B gap. Because both inputs have at least two values, this implies one common positive gap. Conversely, common-gap progressions realize all indices from 0 through m+n−2. The proof is complete under the stated assumptions. Singleton translation is correctly separated. No wrapping, repeated input elements, empty sets, or assertion of a general Freiman theorem is smuggled into the student tasks.

## Readiness, launch, and physical feasibility

Problems 1–7 offer children mathematical choices after a short placement launch. Adult reading and occasional addition facts can support them without requiring the adult to choose inputs or operate the whole investigation. The fixed sets and occupied result positions externalize state. Checking all possible pairs still requires organized attention; unlike tiling, counters do not by themselves enforce complete pair coverage or correct addition. The eventual guide should make the partner's checking role concrete and treat missed pairs as a recoverable learning issue. This is an operational concern to pretest, not evidence that the activity has failed.

The source's prerequisite distinctions are sound: small addition and fixed-input trial work first; row/column coordinates later; arbitrary counts, general explanation, and local path comparison last. Problems 9–10 should remain optional upper work or a return visit. Retaining them is appropriate; finishing ten pages in forty minutes is not the aim. The combined Grades 3–5 label is an approximate audience label, and the README clearly avoids guaranteeing independent access to every page.

The fresh geometry check confirms 12×18 mm result cells and a 228 mm 0–18 lane on landscape Letter. An 8–10 mm counter has adequate nominal width; the numeral at the top leaves a useful lower counter area. This establishes nominal dimensions only. The 13×14 mm card drawings are explicitly described as pictorial input/recording slots, so fitting full-size purchased cards into those slots is not claimed. A volunteer still needs two distinguishable 0–9 card sets per pair. Twenty counters, reused after marking records, are sufficient for a trial, and the source calls for 60 across three active pairs. The page-8 9 mm grid dots are for pencil routes, not counter placement. No polygon fit is involved.

Actual counters/cards, handling, marking before reuse, partner enforcement, launch rehearsal, session pacing, and classroom understanding remain **unperformed**. Preserve that status in the eventual guide and release notes. This packet also supplies no activity for the omitted K–1 table; the routing permits that scope, but an organizer must make a separate meeting choice.

## Provenance check and limits

I checked the source notes against the local primary mathematics material rather than accepting an exact-theorem attribution on trust. Tao–Vu's converted author sample, printed/sample pp.6–7 and 67–71, gives additive-set/sumset definitions, progression examples, inverse-problem context, and the general product upper bound. Its chapter-5 contents entry is not the omitted chapter body. The exact sharp two-set integer equality theorem and local path-swap proof are correctly identified as independently reconstructed here. The saved Tao author post dated June 25, 2009 explicitly compares entropy results with |A+A|≥2|A|−1; it does not supply this packet's two-set equality proof. No entropy activity has been inserted.

I reread *Math Circle by the Bay*, Preface printed pp.viii–ix (PDF 9–10): the notes accurately identify deep themes, dialogue/independent work, clear statements, and manipulatives as precedents. They correctly label cards-before-arrays as the author's design inference. I reread *A Decade of the Berkeley Math Circle*, chapter 6 §3.6, printed pp.113–114 (PDF 133–134): the empirical-evidence/proof distinction is actually present. The existing local extraction of the organizer's *Handouts 1* supports visible figurate-number/addition work, with no sumset-theorem claim. I did not conduct a new exhaustive prior-packet overlap audit.

These sources support the mathematics or named pedagogical principles; **none validates this adaptation's Grades 3–5 suitability or physical procedure**. The lean seven-file `draft/src/` folder contains original editable figures and authored notes/builders/checkers, with no borrowed exemplar block, reference PDF, or prompt file. This narrow inspection is not a comprehensive originality or rights clearance. `REPUBLISHING.md` is preserved.

## Handoff

Reviser: address R1 and R2 in the student PDF, retain the concrete cases and upper theorem, then rebuild and inspect all changed pages and source consistency. Optional recording/wording suggestions above are not redesign mandates. A separately authored and independently reviewed facilitator guide, final portable-source verification, physical rehearsal, and classroom piloting remain later work. There was no tooling or access blocker to completing this critic stage.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
