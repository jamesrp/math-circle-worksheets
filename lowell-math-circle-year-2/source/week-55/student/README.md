# Week 55 revised student source

Status: fresh revision W55-S-v2, October 4, 2026, addressing the separate adversarial and independent mathematical reviews. One combined ten-page student packet, chiefly Grades 3–5, with no manufactured K–1 variant. Prepared for review; not approved, physically rehearsed, or classroom piloted. No publication, remote write, or facilitator-guide authorship is part of this stage. Only the assigned run is edited.

## Build and check

Requirements: Python 3 (standard library), pdfLaTeX, standard TeX Live packages `geometry`, `fontenc`, `helvet`, `tikz`/PGF (including `arrows.meta`), and `fancyhdr`. The checker additionally needs PyMuPDF. All figures are original editable TikZ inside `students.tex`; no external image asset is needed.

From any working directory:

```sh
python3 /absolute/path/to/student/build.py --out /absolute/path/to/output
python3 /absolute/path/to/student/verify_math.py --out /absolute/path/to/checks/math.json
python3 /absolute/path/to/student/verify_pdf.py --pdf /absolute/path/to/output/students.pdf --out /absolute/path/to/checks/pdf.json
python3 /absolute/path/to/student/verify_rebuild.py --pdf /absolute/path/to/output/students.pdf --work /absolute/path/to/checks/rebuild
```

`build.py` compiles twice in a temporary directory beneath the requested output and removes it on completion. It writes only `students.pdf` to the output and rejects overfull boxes. Source copies or ZIP extractions need no repository files, prompts, books, exemplars, or reference PDFs. Metadata dates and trailer IDs are omitted, and the build uses a fixed reproducible timestamp. PDF text, dimensions, and rendered pixels are the reproducibility criteria.

## Prerequisites and physical constraints

Problems 1–7: recognize and add whole numbers with totals up to 18; hold two small fixed inputs; merge equal results; choose and check new inputs. A zero card is an available choice. An adult may read the prompt or supply an addition fact while the children choose inputs and test results. A ready second grader can enter; the full investigation and catalog are aimed chiefly at third grade and above. The header is an approximate grade label, not a prerequisite guarantee.

Problem 8: coordinate ordered row/column inputs and follow right/up paths. Problems 9–10: read m and n as input counts, use multiplication as pair counting, and reason about every input size. The inverse argument requires coordinating full paths with a local change and distinguishing experiments from a general explanation. These are readiness-dependent upper tasks, likely requiring adult mathematical conversation. The last two pages retain open general explanations and do not print the local-swap proof as student instructions.

One pair needs two distinguishable sets of reusable 0–9 number cards, about 20 counters of diameter 8–10 mm, pencil/eraser, and paper or a whiteboard for overflow. A card and B card may show the same number; within one input each number appears once. A cards use rounded outlines and B cards double square outlines; color is unnecessary. The visible card slots are 13×14 mm and are pictorial input/recording spaces, not a guarantee that a purchased card kit fits. Source figures can be enlarged if that becomes necessary.

Print US Letter **landscape at 100%**, single sided. Every result cell is 12×18 mm; a complete 0–18 lane is 228 mm wide and fits the landscape content. The occupied result cells are marked before counters are reused so each trial remains recoverable. Count different occupied positions, not numbers of pair attempts or counters stacked at a position. The grid dots on page 8 are for drawing routes, not for full-size counters. No special polygon geometry is used.

Ten investigations intentionally support multiple visits. The core is concrete card/result work, followed by contrasting common and mismatched spacing and the singleton case. Problem 6 defines numerical equal spacing by differences between neighboring values in increasing order; printed card positions do not represent those differences. The grid convention has its own input → row/column addition → grid/result-route example before Problem 8. Before Problem 9, a separate input-card → count-letter → substitution example introduces m and n without finding the example's totals or resolving either general question. Problem 10 states its at-least-two-card restriction in ordinary language. Children choose routes and explanations. Page completion is not a required session goal. The omitted K–1 table needs a separate meeting choice; this packet is not a full three-table hour plan.

Unperformed checks: matching the organizer's actual counters/cards to paper, handling and moving counters, teaching rehearsal, and classroom pacing/understanding. Digital dimensions do not establish any of these. The eventual independently authored facilitator guide must retain these limits.

## Provenance

All student wording, trial selection, layout, card borders, result lanes, and grid figures were newly authored for this packet around established mathematics. The reviser added the numerical-spacing definition, count-conversion visual, and ordinary card-count restrictions, and removed the optional Problem 5 pooling instruction for a later guide to consider. No exemplar prose, third-party figure, copied worksheet, prompt block, reference book, or reading PDF is included in this portable source folder. REPUBLISHING.md was read and preserved. Mathematical proof reconstruction and scope are recorded in `MATH-NOTES.md`.

The writer read the supplied outline, research record, checks and stage routing at `plans/new-themes-52-63/week-55/` and `plans/new-themes-52-63/STAGE-ROUTING.md`, along with AGENTS.md, root README.md and REPUBLISHING.md. The outline and research supplied these documented precedents; the writer does not claim a new primary-source audit or verified age fit from them:

* Terence Tao and Van Vu, *Additive Combinatorics*, author-hosted sample: Prologue Definition 0.1 (sample pp.6–7), chapter 2 opening pp.67–69, and §2.1 pp.70–71. [Author sample](https://www.math.ucla.edu/~tao/preprints/additive_sample.dvi). Supports additive-set definitions, collision/cardinality context, and progressions; the sample omits chapter 5. It is not cited as a verified source for the exact two-set inverse theorem or its local path-swap proof.
* Tao, [*Sumset and inverse sumset theorems for Shannon entropy*, June 25, 2009](https://terrytao.wordpress.com/2009/06/25/sumset-and-inverse-sumset-theorems-for-shannon-entropy/), opening/final combinatorial comparisons: A+A lower-bound context. Its entropy mathematics is not adapted here.
* Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, Preface pp.viii–ix, “How we select our topics”/“How we teach”: research-record precedent for deep themes, independent work/dialogue and manipulatives. Cards/result lanes before grids are our design inference, not a prescribed source lesson or validated grade fit.
* Stankova and Rike, eds., *A Decade of the Berkeley Math Circle*, chapter 6 §3.6 “The burden of proof”, pp.113–114: research-record precedent for distinguishing empirical cases and proof. The final two pages keep this distinction.
* Organizer's year-1 *Handouts 1*, unnumbered figurate-number and sum/difference pictures: local precedent reported in the research record for visible addition. No sumset theorem is attributed to it.

The first-use concrete placement and recording conventions respond to the current project's observed need for rules that survive children's actions and to the organizer's explicit before-use visual requirement. Their classroom effectiveness remains untested. The final source bundle contains only the original source, builders, verifiers and these authored notes; evidence outputs belong outside `src/`.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
