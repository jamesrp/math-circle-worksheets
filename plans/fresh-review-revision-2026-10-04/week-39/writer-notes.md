# Week 39 writer-stage targeted revision

Writer stage only. Draft, unpiloted; independent critic/reviser and release integration remain with the parent.

## Exact files

Changed in the copied working package:
- `tmp/fresh-review-revision-2026-10-04/week-39/src/make_packets.py`
- `tmp/fresh-review-revision-2026-10-04/week-39/src/common.py` (page break count now follows the actual number of bodies; older-band generation is identical)
- `tmp/fresh-review-revision-2026-10-04/week-39/src/check_math.py`
- `tmp/fresh-review-revision-2026-10-04/week-39/src/README.md`
- `tmp/fresh-review-revision-2026-10-04/week-39/src/k-1.tex` (regenerated)

Draft PDFs:
- `tmp/fresh-review-revision-2026-10-04/student-stages/week-39/draft/k-1.pdf`: 6 pages, 7 problems.
- `tmp/fresh-review-revision-2026-10-04/student-stages/week-39/draft/grades-2-3.pdf`: 4 pages, preserved.
- `tmp/fresh-review-revision-2026-10-04/student-stages/week-39/draft/grades-4-5.pdf`: 4 pages, preserved.

No guides, AGENTS files, reference PDFs, releases, bonus files, indexes, ZIPs, commits or remote copies were edited. Intermediate LaTeX files and renders are in the copied `week-39/qa/` and stage `writer-qa/` folders.

## Decisions and original preserved tasks

K–1 now starts with Problem 1 on page 1: a three-step A-to-E tree trip and four-step B-to-B and A-to-D trips, constructed as physical ordered step tiles. This keeps the existing input/removal/output visual convention example, shared rules, map and 32 mm coordinate scale. Problem 2 on page 2 asks for four-step ring trips home and which disappear or retain steps. The ring uses the existing 53 mm coordinate scale and a full recording area. Neither introductory problem requires a complete catalogue; children choose trips and perform actual cancellations.

All five original K–1 prompts are preserved verbatim, with renumbering:
- original Problem 1 → Problem 3, page 3: seven-step A-to-E and C-to-F trips.
- original Problem 2 → Problem 4, page 4: 4/6/8/12-step tree returns.
- original Problem 3 → Problem 5, page 4: C-to-F trip using every road and the extra-step question.
- original Problem 4 → Problem 6, page 5: complete reduced results of eight-step ring returns.
- original Problem 5 → Problem 7, page 6: complete reduced results of six-step A-to-C ring trips and order comparison.

The additional pages preserve this material as continuation rather than squeezing it into the first route. First-route recommendation for the parent guide: K–1 Problems 1–2; retain Problems 3–7 for readiness-dependent continuation/return visits. The guide currently refers to four pages and old problem numbers and must be synchronized during release integration.

Original board scales remain 32 mm for the first tree, 49 mm for the large tree, and 53 mm for the K–1 rings. Original ring and large-tree working space is unchanged. The old first tree is also retained at 32 mm on the later seven-step page, with added answer space. All older-band tasks, examples, map coordinates, scales, and layout remain untouched. Older-band generated TeX SHA256 values before and after regeneration were identical:
- grades-2-3: `10b46af82fac6a8fffd5e33dd6f5e8f66f4ed04d60de3c1c3b9893a3a9910e10`
- grades-4-5: `c0f78cc98989fcf94cc11ff7196bb2d57f3187e802f660d7f8623abe5a0bf411`

## Checks

Ran source generator and `src/check_math.py` using the designated Python environment. The new tree entry has one legal three-step A-to-E trip, eleven legal four-step B-to-B trips, and five legal four-step A-to-D trips; every possible cancellation order reduces them respectively to ABDE, B, and ABD. The four-step A-to-A ring has eight legal trips and reduced outcomes A, ABCDA, ADCBA. Existing route checks, tree walks through ten edges, eight-step ring return outcomes, six-step A-to-C ring outcomes, and covering-route existence checks still pass.

Compiled all three TeX packets twice with pdfLaTeX. Rendered and inspected all 14 final draft pages with PyMuPDF/PIL, including a full-size inspection of the changed first page. No clipped or overlapping content was seen. Page geometry remains 612 by 792 points (US Letter). Extracted all five original K–1 problem prompts and matched them verbatim to new Problems 3–7. Both older-band PDFs have exactly the same extracted text and every vector diagram bounding box as the reference PDFs. Raster byte equality differs on rebuild despite unchanged source/geometry; no such equality is claimed. Parent release verification should refresh reference copies from its final accepted rebuild and use its normal extracted-ZIP reproducibility checks.

The exact tile set and replay/recording procedure have not been physically rehearsed and no classroom piloting is claimed. Repeated edge uses require enough duplicated edge/direction tiles; the adult guide should retain its before-use check and realistic preparation. No top-level package build or reference-PDF equality verifier was run because those affect or depend on adult/reference outputs outside this writer-stage scope.
