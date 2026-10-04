# Week 3 v4 review record

Reviewed September 30, 2026 by the authoring agent. **Unpiloted.** This is author QA, including an independent computational check of the finite mathematics; it is not a classroom trial or a second reviewer’s assessment. The previous v3 review is preserved with its source archive.

## Transfer from the current Week 2 updates

Reviewed the current top-level compact and upper Week 2 catalogs, their brief prompts, and the upper catalog's adult notes. The resulting Week 3 revision follows the substantial-problem guidance in AGENTS.md:

- 35 small numbered tasks become 17 substantial problems: K 5, middle 5, upper 4, extra 3.
- Shared rules appear once. Key tables define the action; contrasting clues and examples give each investigation substance.
- Prescribed traces, loop drawings, multiple-marking charts, and largest-loop procedures move to the guide as optional support. Student workspace remains open.
- The central problems still ask for all solutions, impossibility, complete sets of return times, maximal constructions and proofs, and a general monotonicity argument.
- Whole-message returns are distinguished from returns of a partially represented alphabet. Composition includes overlapping commuting keys as well as overlapping noncommuting swaps.
- The adult plan now uses the reported ten children and three adults, ten starting sheets, a brief common launch, stable table coverage, and flexible continuation.

The [plan](../../../plans/week-03-redesign.md) distinguishes locally read source observations from our design inferences. Prepared material remains unpiloted in the use log.

## Mathematics

`verify.py` exhausts permutations for every size 1–9. It confirms maxima 1,2,3,4,6,6,12,15,20; every largest-loop bound used in the guide; all printed clue solution sets; shape-message answers and ambiguous preimages; the partial-message comparisons; witnesses for every claimed return time; both composition orders and the inverse machine. The checked report is [plans/week-03-checks.json](../../../plans/week-03-checks.json).

The guide separately proves the loop decomposition, the LCM return rule, completeness for four and five letters, the eight/nine-letter upper bounds, the five/six plateau, and nondecreasing maxima at every size. Enumeration is not presented as a child’s proof. First return is positive, so a fixed letter or identity key has return one. Message positions stay fixed under substitution.

## Build and visual checks

Final counts: **3 K / 3 middle / 3 upper / 3 extra / 6 facilitator = 18 US Letter pages**. All five PDFs compile successfully. Final logs have no warnings or overfull/underfull boxes. Automated checks confirm consecutive problem numbering, v4 headers/footers, expected page counts, no obsolete student labels, and all text within safe page bounds.

All final pages were rendered with Poppler and visually inspected; the dense middle-solution page was also inspected at full page size. Fixed during review: return examples needed wider separation, the youngest shapes needed enlargement, message-answer boxes needed square proportions and baseline alignment, and the guide needed pagination repair and a breakable EPUB source reference. Final pages show no observed overlap, clipping, missing glyphs, or orphaned continuation pages. Source and output paths remain stable. Working renders and QA data are in `tmp/pdfs/week-03-concise/`.

## Combined sets and preservation

The five combined sets contain the revised Week 3 pages: K 67 pages, middle 70, upper 78, extra 66, facilitator 62. Contents page ranges and all nine weekly bookmarks are regenerated. `refresh-week.py` checks that replacement pages match the final weekly PDFs and that every other weekly page retains identical extracted text and PDF content streams. This preserves the Week 2 collection already embedded in those sets; it does not restore archived standalone Week 2 files or replace the current catalogs.

The immediately preceding Week 3 PDFs/sources and plan are preserved in separate `archive-before-concise-2026-09-30/` folders. The previous combined PDFs are in `combined/archive-before-week-03-concise-2026-09-30/`. The archived Week 3 builder has separate paths so it cannot overwrite current PDFs. Other preexisting working-tree changes were retained.

## Limits and next evidence

Layout and mathematical QA do not establish age fit, five-minute engagement, or actual timing. Record exact keys/messages attempted, invented records, adult rescue, conjectures and arguments, and requests to continue. Distinguish observations from hypotheses and tried/conjectured/checked/proved/supplied results. Use F03-K/M/U/X-v4 only for material actually encountered.
