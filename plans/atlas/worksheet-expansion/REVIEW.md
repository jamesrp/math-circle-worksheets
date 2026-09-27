# Review of the remaining eighty worksheets

Release date: September 26, 2026. All ten author batches have closed independent design and PDF reviews. This release covers all eighty remaining atlas IDs exactly once, with the original ten excluded and preserved. It contains six books: 255 student-book pages (245 worksheet pages and ten contents pages) and 399 facilitator-book pages (389 body pages and ten contents pages).

The [page finder](INDEX.md) selects exact print ranges and prerequisite gates. The [release manifest](release-manifest.json) records the final files, SHA-256 hashes and automated evidence. Mathematical and visual review do not establish classroom effectiveness; all activities remain unpiloted.

## Design and mathematical review

Authors developed staged investigations from the atlas cards, including exact problems, learner choices, useful drawings or manipulatives, hints, complete solutions, extensions, honest prerequisite gates and source locators. Reviewers checked every family separately from its author, including finite examples, general arguments, degenerate cases, model assumptions and the point at which a prerequisite becomes necessary. Computations support finite claims and examples; they are not substitutes for general proofs.

Across the eighty families there are 497 student prompts with corresponding keys and 85 solved extensions. Reviewers also assessed whether a worksheet reached a worthwhile mathematical conclusion, whether a diagram prematurely supplied that conclusion, and whether an earlier stopping point was honestly described. The [author brief](AUTHOR-BRIEF.md) and [review contract](REVIEW-CONTRACT.md) document these requirements.

The review records contain the actual findings and repairs. Examples from the final production wave include making the edge/face bases explicit in AD-22, completing the trace-zero commutator argument in AD-20, removing premature solution scaffolds in AP-19 and AP-27, distinguishing detectable and undetectable error patterns in AP-28, and clarifying sphere-transport frames, reflection geometry and sublevel-set diagrams in GA3. GA-08 keeps its calculus gate. A concrete entry does not stand in for an advanced theorem.

## Batch evidence

Each row links the independent mathematical review, independent rendered-PDF review and author's layout record. The [accepted-preview registry](reviewed-previews.json) identifies the exact approved files and frozen data/renderer hashes.

| Batch | Design review | PDF review | Maker record |
|---|---|---|---|
| AD1 | [Closed](review-ad1-design.md) | [Closed](review-ad1-pdf.md) | [QA](ad1-maker-qa.md) |
| AD2 | [Closed](review-ad2-design.md) | [Closed](review-ad2-pdf.md) | [QA](ad2-maker-qa.md) |
| AD3 | [Closed](review-ad3-design.md) | [Closed](review-ad3-pdf.md) | [QA](ad3-maker-qa.md) |
| GA1 | [Closed](review-ga1-design.md) | [Closed](review-ga1-pdf.md) | [QA](ga1-maker-qa.md) |
| GA2 | [Closed](review-ga2-design.md) | [Closed](review-ga2-pdf.md) | [QA](ga2-maker-qa.md) |
| GA3 | [Closed](review-ga3-design.md) | [Closed](review-ga3-pdf.md) | [QA](ga3-maker-qa.md) |
| GA4 | [Closed](review-ga4-design.md) | [Closed](review-ga4-pdf.md) | [QA](ga4-maker-qa.md) |
| AP1 | [Closed](review-ap1-design.md) | [Closed](review-ap1-pdf.md) | [QA](ap1-maker-qa.md) |
| AP2 | [Closed](review-ap2-design.md) | [Closed](review-ap2-pdf.md) | [QA](ap2-maker-qa.md) |
| AP3 | [Closed](review-ap3-design.md) | [Closed](review-ap3-pdf.md) | [QA](ap3-maker-qa.md) |

Every student body page was visually inspected full-size by its maker and an independent reviewer. Every guide page was inspected at least through contact sheets, with dense keys and diagram pages inspected full-size. Where a repair changed only a few pages, reviewers inspected the changed pages on a fresh render path and used page-image identity to retain prior coverage of unchanged pages. The batch records state the exact coverage and approved revision; they do not claim that every guide page received a full-size pass.

## Assembly and release checks

The final books were built one subject at a time from frozen reviewed inputs. Their per-book build reports were combined into the aggregate report used by the page finder and release audit. No original-ten source or PDF was rebuilt.

An independent reviewer inspected all **20 newly assembled contents pages individually at full size** and verified all **160 printed family/title/gate/page entries** against the frozen data and per-book starts. See [final contents review](review-final-contents.md). The final body pages were not subjected to a redundant second complete visual pass: the release audit compares all **634 body pages** with their independently reviewed batch previews, retaining characters, font names and sizes, colors, positions, vector geometry and any image content. Only running headers, footers and page numbers are outside that comparison; PDF font subset tags are normalized.

The audit also requires the exact three subjects and both book kinds, all eighty family IDs, each student prompt exactly once, complete keys and extension gates, correct contents links and family bookmarks, actual page counts, a render for every page, and no blank pages, out-of-page characters or suspect glyphs. It verifies the preserved original atlas data, original-ten sources and original-ten PDFs, as well as accepted-preview hashes. It reruns every mathematical check program in this directory and writes the manifest only after all checks pass.

The final audit passed on September 26: all 634 body comparisons, all 18 mathematical check programs, all 160 contents destinations and family bookmarks, and all 14 preserved-file hashes. Across the 654 rendered pages, the build reports contain zero blank-page, out-of-page-character or suspect-glyph findings.

The [release-tool review](review-release-tools.md) records an independent review of the audit and index implementation, including fixes to missing-book detection, actual page-start verification, font-name comparison and geometry crossing the body boundary. The generated index and final documentation links were checked separately: 214 local links resolve and all 160 student/guide page ranges match the build records. An independent handoff reviewer matched all eighty index entries, gates, assessments and stopping points to the batch data and confirmed the release totals and coverage claims. The only noted issue was an inherited cosmetic missing space in AP-05’s assessment (“50%procedure”); it does not affect a prompt, solution or prerequisite.

## Practical limits

The family assessments and proposed timing are editorial judgments, not pilot evidence. Some investigations suit an elementary circle after oral launch and manipulative play; others require sustained algebra, calculus, linear algebra or more advanced preparation. The full eighty are neither eighty interchangeable hour-long sessions nor a complete elementary curriculum. Use one page at a time, take the stated satisfying stop, and record what learners actually tried and understood before scheduling a revisit.
