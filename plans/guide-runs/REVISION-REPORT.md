# Eleven week-tied guides: reviser result

Reviser-only stage completed November 6, 2026. **11 guides / 63 pages**; all **3 must-fix and 58 should-fix findings addressed**, none declined. Every guide has a fresh reviser, a final PDF and portable source/checker, and a finding-by-finding report. The preserved critic reports cover 98 minor findings; individual reports distinguish edits, already-sufficient behavior and justified limits.

| Run | Topic | Revised guide | Finding dispositions and checks | Critic must / should / minor |
|---|---|---|---|---|
| k1-57 | Area from dots | [5 pages](k1-57-v1/final/k1-guide.pdf) | [Report](k1-57-v1/reviser-report.md) | 0 / 7 / 5 |
| k1-66 | Lamplighter streets | [4 pages](k1-66-v1/final/k1-guide.pdf) | [Report](k1-66-v1/reviser-report.md) | 0 / 3 / 10 |
| k1-81 | Buckets of Fish | [5 pages](k1-81-v1/final/k1-guide.pdf) | [Report](k1-81-v1/reviser-report.md) | 0 / 6 / 8 |
| k1-87 | Voting and agendas | [5 pages](k1-87-v1/final/k1-guide.pdf) | [Report](k1-87-v1/reviser-report.md) | 0 / 3 / 12 |
| k1-91 | Rotor-router machines | [4 pages](k1-91-v1/final/k1-guide.pdf) | [Report](k1-91-v1/reviser-report.md) | 1 / 5 / 7 |
| k1-97 | Square remainders | [4 pages](k1-97-v1/final/k1-guide.pdf) | [Report](k1-97-v1/reviser-report.md) | 1 / 2 / 10 |
| k1-98 | Growing from a few seeds | [5 pages](k1-98-v1/final/k1-guide.pdf) | [Report](k1-98-v1/reviser-report.md) | 0 / 6 / 10 |
| rv-53 | Connecting networks | [7 pages](rv-53-v1/final/facilitator.pdf) | [Report](rv-53-v1/reviser-report.md) | 0 / 6 / 13 |
| rv-58 | Fair division | [8 pages](rv-58-v1/final/facilitator.pdf) | [Report](rv-58-v1/reviser-report.md) | 0 / 7 / 6 |
| rv-62 | Conflict networks | [8 pages](rv-62-v1/final/facilitator.pdf) | [Report](rv-62-v1/reviser-report.md) | 0 / 6 / 8 |
| rv-63 | Cards away from home | [8 pages](rv-63-v1/final/facilitator.pdf) | [Report](rv-63-v1/reviser-report.md) | 1 / 7 / 9 |

## Required corrections

- **RV63:** each young pair receives surplus counters rather than the six that answer its problem, and each middle pair receives a separate unmarked outcomes sheet. Extra sheets and minimum cutting counts are explicit.
- **K1-91:** exhausting both switch starts or all eight tree starts is accepted as a finite impossibility proof. The Problem 7 statement now precisely connects first/fourth arrivals to first/last second arrivals.
- **K1-97:** the younger table leaves the shared launch before the older bundles-of-four example that reveals its Problem 1 answer. Its own demonstration uses a non-task instance.

The should-fix revisions add theorem/discovery maps, concrete non-task demonstrations, accessible explanations, flexible first/return routes, recording/reset/reading/staffing guidance and checked material plans. All numerical task keys remain correct. RV53 is shorter by a page; several K–1 sections add a page to preserve readable diagrams and complete adult keys. RV62's extracted words fell about 16%; RV58's fell about 8%. RV63's concision minor is only partly pursued: redundant prose was removed, but new required explanations offset it; its report justifies retaining complete keys instead of imposing a 3,000-word target. K1-87 minor 12 was already implemented; both fallback modes were verified. No must/should was rejected.

## Student pages and later companion work

All **19 served student PDFs / 144 pages** retain their pinned hashes. Every reviser checked actual final problem/page numbering, pictures and material quantities; each report gives the exact map and workarounds. Notable retained issues: RV53's price/tie domains and 36-counter road use written totals; RV58's arbitrary-value problem uses each person's total divided by three, with a quarter-panel mark needed for some games; RV62's crowded labels and small demonstration circles need adult handling/enlargement. The K–1 reports identify stale base-guide “no K–1 packet” or route/insertion sentences and Week 98's existing older-band page references. These existing guides remain untouched for the later packaging stage. No student-page correction is implied by a guide fix.

## Verification and scope

All revised guides compile using real pdfLaTeX, with no errors or overfull boxes. Their exact mathematical checkers pass, including new examples/proofs or finite enumerations where needed. Revisers rendered and inspected every final guide page and every served student page, using Poppler for authoritative final checks where a PyMuPDF rasterizer artifact was observed. Digital inspections found no remaining clipping/overlap or unreadable tables. All fonts are embedded; pages are US Letter and text bounds pass.

The coordinator independently reran every final build in the checkout and from clean outside-repository directories containing only each `src/` and the corresponding unchanged student PDF(s). All checkers passed; all **11 rebuilt PDFs and `pdftotext -layout` outputs match exactly**. [reviser-verification.json](reviser-verification.json) records hashes/results. A disposable guide-branch copy passed `catalog/build.py` and `catalog/check_path.py`; generated files were not retained. This is not a claim of testing future packaged guides against the newer catalog integration.

Original draft PDFs/sources, writer reports, critic reviews/check scripts and their outputs are preserved. Generated local stage prompts, TeX intermediates, renders, downloaded toolchain and caches are excluded from commits. No student pages, existing guides, packaged draft folders, catalog code/data, readiness files or explorer files were edited. No packaging, substantive guide integration to main, PR merge, deployment or external-agent contact occurred. PR #6 remains draft.

## Coordination and remaining dependency

The initial guide-only claim was pushed and remotely verified at **`3ca54531b52a541e444b58f11d7199005f8aa07a`** on main, preserving the parallel catalog claim. The catalog implementation later landed independently at **`2e81d569119a26e28caad9bf93253f05ff4b9ddc`**. This branch retains its guide-stage base; it has not rebased or overwritten that implementation. The completion update changes only this guide's row on freshly read main; the exact final branch and board SHAs are reported with the handoff.

No revision blocker remains. Packaging is intentionally pending a separate follow-up after this checkpoint is checked, despite the catalog task having completed. That follow-up must preserve current main and carry the per-guide insertion notes into the packaged result.

**Every guide remains untested with children and physically unrehearsed.** Printing at size, cutting/fit, handling, material resets, adult staffing, recording burden and timings are digitally reviewed proposals, not classroom evidence. Referenced private books were not newly consulted or claimed reread in this bounded stage.
