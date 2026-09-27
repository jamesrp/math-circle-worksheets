# AP1 maker PDF QA

Current preview: `tmp/pdfs/atlas-remaining/ap1-final-review-fixes/`.

- Student PDF: `atlas-ap1-student-worksheets.pdf`, **25 pages**: one contents page plus 24 investigation pages (three for each family).
- Facilitator PDF: `atlas-ap1-facilitator-guide.pdf`, **39 pages**, including contents, all 51 student prompt keys, delayed hints, eight guide extensions, source evidence and three worked-figure sections.
- Student SHA-256: `27906dd427dfcf4c5b6eecf5f43d2b640575893cb1c6b771c5a91477e1f16ed9`.
- Guide SHA-256: `b1298ca1cd7828fcd248b7fa48c39c99635dfa655502d3223442bee9bc63ebe3`.

## Inspection coverage

Inspected every student investigation page at full size in the first preview, repaired findings, then inspected **all pages 1–25 at full size again in `ap1-preview-v3`**. The final reviewed-preview student body PNGs 2–25 are byte-for-byte identical to those inspected v3 body pages; I verified all 24 files. I inspected the updated final contents page 1 separately after the shared contents adjustment.

Inspected every final guide page 1–39 on all five contact sheets. Inspected final guide pages **5, 22, 28, 32 and 38 at full size**, covering the exact bag outcome map, dense Newton safeguard solutions, six-state machine with both symbol transitions, dense normal-mode/nonrepeat proof, and all worked three/four-spring networks. Earlier v2 guide contacts and corresponding full-size diagrams were also reviewed before the final shared pagination change.

No clipped text, overlapping required labels, ambiguous spring connections, missing tasks, unintended answer values in student diagrams, or suspect glyphs remain in this maker pass. Independent PDF review is now closed in `review-ap1-pdf.md`; the paragraph above describes the earlier maker pass, before the independent findings below.

## Repairs made during maker QA

- Separated bag headings from column labels in both student and guide draw grids.
- Positioned each complementary-assignment sum under its own triple; ordinary paragraph whitespace had collapsed an earlier spacing attempt.
- Added actual concise prerequisite lines to the family entries and core student launch pages. AP-06 explicitly requires calculus; AP-09 separates algebraic force-mode work from its calculus continuation.
- Moved machine self-loop labels below the complete prompt and above the diagram, leaving a separate shortest-counterexample work area.
- Removed preprinted six rooms from AP-08's optional two-condition target. Learners choose both the number and arrangement; the minimal size is proved later.
- Separated the side-by-side spring title, stiffness labels, bar guides and load arrow. Only the total terminal load is supplied.
- Gave AP-10's four-spring question neutral arrangement/certificate boxes, rather than implying that the learner must use a particular dual construction.
- Reused sparse guide pages for worked diagrams so a final hint is not stranded on a page before an unconditional new figure page.
- Rechecked source/solution typography and repaired remaining fused prose around subscripts, parameters and units. Kept equations and URLs intact.
- Rebuilt with the editor's shared guide change removing repeated verification blocks; final pagination is 39 guide pages, down from 43 initially.

## Mechanical and mathematical evidence

The build confirms the exact eight-family set, 51 distinct student prompts printed exactly once, complete keyed solutions, and stable contents pagination. Both final PDFs report **zero blank pages, zero out-of-page text characters and zero suspect glyphs**. These mechanical checks supplement the visual inspection; they do not certify the meaning of a diagram.

`ap1-checks.py` and the independent `review-ap1-checks.py` pass. The independent design review in `review-ap1-design.md` is closed; it covers all 51 student prompts and eight guide extensions. The full ordinary-language probability mechanisms, universal proof scopes, Newton safeguard, normal modes, and recursive spring class remain in the data and guide.

## Candid classroom assessment

AP-02 is the strongest accessible pilot for learners comfortable with finite fractions: two messengers make the reporting rule matter immediately. AP-04 gives a particularly concrete impossibility argument through two indistinguishable hidden populations. AP-08 has low arithmetic demands but a real abstraction step: the machine's room must be its entire memory; the distinguishing-suffix proof is the new payoff.

AP-10 is promising for algebra-ready learners because its compatibility/force distinction grows into a complete network classification and reciprocal construction. AP-06 and the dynamic portion of AP-09 remain specialist calculus investigations. AP-03 and AP-05 are mathematically satisfying but most sensitive to facilitation: the null experiment and the distinction between coverage and belief need patient explanation. The deliberately poor confidence procedure is optional. None of these worksheets has been classroom-piloted, and three pages are staged destinations rather than a requirement to finish in one meeting.

## Independent PDF repair closure

The independent reviewer found a supplied-population reference error in AP-04, the AP-06 two-cycle disclosed by its exploratory graphic, a missing X in AP-05’s first optimal-interval key, and answer-count scaffolds in AP-05/AP-10. All were repaired. AP-03’s exact ten-pair record was also replaced with an open list area. The printed interval is now `[X−2,X+1]`, with a direct checker assertion guarding both displayed optimal rules.

The fresh preview retains 25 student and 39 guide pages. I reopened all six changed student pages 5, 9, 10, 12, 14, 24 and the corrected guide page 17 at full size. The independent reviewer reopened every changed student and guide page, confirmed all other 51 PNGs byte-identical to the prior complete review, and closed all findings. Its report records the exact seven changed guide pages and hashes above. No author data or renderer changes follow this release. Final assembly still requires the editor’s page-body identity and contents checks.
