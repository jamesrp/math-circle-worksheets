# Week 62 return-visit guide — writer report

**Stage:** Codex writer only, 2026-10-31. No formal guide critic/reviser stage was
run. No commit, push, public-site change, student change or packaging change was
made. The generated WRITER/CRITIC/REVISE prompts and `tmp/` must not be committed.

## Deliverable

- `draft/facilitator.pdf`: **8 US Letter pages**, pdfLaTeX, header and footer on
  every page as requested; ID W62-RV-FAC-v1.
- `draft/src/`: `facilitator.tex`, `build.sh`, independent `check_guide.py`,
  `student-edition.json`, `README.md` and `SOURCES.md`. No LaTeX intermediates or
  borrowed/reference PDFs are in this source folder.
- Final PDF SHA-256:
  `379a40a6e5c61f27b58e2da52f89bb3e1e203858241de72679330cfc7a512730`.

The opening theorem-first overview covers two-list trees and rings, the
five-card/six-card list-coloring contrast, stuck three-color rings, invariant
up-count on three-color rings, four-color recoloring connectivity on every ring,
and earliest precedence scheduling versus longest directed paths. It states
hypotheses and proof ideas before individual answers. Separate paced routes keep
the three new conventions from becoming one oversized launch.

## Mathematical and edition evidence

I rendered and personally inspected **every final student page: K–1 6, Grades
2–3 10, Grades 4–5 10**, reading the diagrams, lists, starts/goals, arrows and
printed numbering. I read the outline, student source, both older reviews, draft
README, base guide/materials, and model-guide material. The older reviews' upper
packet had 9 pages and a different move-problem sequence. The writer guide uses
the final 10-page upper packet; the checker pins all three student PDF byte hashes
and their exact problem/page map. Student bytes remained unchanged.

`check_guide.py` is a new standard-library solver; it imports none of the student's
solver or instance modules. Its final run passes:

- Every printed allowed-list board, with complete solution sets (including the
  six solutions on upper P4's varied five-ring).
- Breadth-first minimum distances and replay of every printed move word; all
  impossible starts/goals are checked for unreachability.
- Every arrow schedule, the listed critical-path witnesses, and exhaustive
  smaller-slot assignment tests for lower bounds.
- Final middle P4: **24 of 7,776** assignments fail on the six-card board with
  A fixed to {1,3}; they are exactly B={2,4}, with the four mixed pairs permuted
  over C–F. **0 of 1,296** fail on its five-card comparison board.
- Upper P2: **0 of 7,776** fail; upper P3's eight-card tree: **0 of 1,679,616**
  fail, enumerated exhaustively rather than accepted from the old review.
- All legal states of rings of sizes 3–8 with three and four colors. The final
  four printed stuck-ring answers are no/no/yes/no; the six-ring has exactly six
  stuck states. The five-ring's 30 states form two families of 15. Four colors
  connect all tested sizes. General claims have proofs in the guide.
- All **64** upper and **256** lower orientations in final upper P11, including
  cycles. Schedulable minima are 3 and 2 cards; precisely two lower orientations
  attain 2. Both displayed orientation/schedule witnesses pass.
- Launch demonstrations, local up/down exchange, material arithmetic, 42-sheet
  complete-table print plan, 60-minute route totals, and counter capacity after
  reserving the four header key counters.

The final full checker/build output is in `tmp/build-final.txt`; the clean-copy
run has its own complete checker output in `tmp/clean-rebuild.txt`.

## Visual and build evidence

The final PDF has 8 pages at 612 × 792 points. I personally inspected all eight
final rendered guide pages (`tmp/final-guide-1.png` through `-8.png`, 1800-pixel
render), after the last edit. Headers, footers, tables, theorem text, solution
strings and the up/down worked visual are clear, with no clipping or overlap.
Initial writer QA caught and fixed one overfull table paragraph and a literal
`quad` typo in the invariant visual; both are absent in the final PDF. A retained
final compile log has no errors, overfull boxes, underfull boxes or warnings.

The build script compiles twice in a temporary directory, rejects overfull boxes,
copies to `../facilitator.pdf`, cleans up, and ends with the independent checker.
The supplied isolated TeX environment was sourced before compilation; no
machine-specific environment path is embedded in the deliverable builder.

A **clean copy outside the repository** contained only the six source files and
the three unchanged student PDFs beside `src/`. `sh build.sh` completed and the
checker passed there. Its PDF's `pdftotext -layout` output is **identical** to the
delivered PDF, and the PDF bytes are also identical (SHA-256 above). The checker
first finds sibling student PDFs and otherwise derives the repository ancestor;
it contains no absolute checkout fallback.

## Student-page findings and guide workarounds — no pages changed

1. **Adjacent allowed-slot labels can read across panels.** Most visibly K–1
   p.1, the lower star's C=2 sits very close to the next board's D={1,3}; upper
   p.3 has similarly close lower-board lists. These are legibility/association
   risks, not changed mathematical data. The guide names the affected locations,
   recommends pointing to the intended circle, and permits covering the unused
   neighboring board with scrap paper.
2. **Arrow preamble needs the transitive caveat.** Middle p.9 and upper p.8 say
   cards with no arrow between them may share a header. Every individual arrow
   must still be satisfied: an indirect directed path also prevents sharing.
   The guide states that explicitly before the arrow route and in its solutions.
3. **Older answer keys are not the final edition.** Middle P4 now has an
   attainable six-card failure before the five-card impossibility, and upper
   P5–11 includes the new triangle entry and reordered stuck/trapped sequence.
   Guide references and verifier data were rederived against final pages.
4. **Physical rule retention remains untested.** A simultaneous exchange of two
   counters would invalidate shortest routes and the invariant. The guide uses
   the revised replacement demo, one child choosing the change, a partner
   checking incident lines, and a single move word. This is a proposed safeguard,
   not evidence of success with children.

No erroneous intended mathematical instance was found in the final student
packets. There is **no missing bespoke printed object**: W62-M-v1 supplies all
letter cards and headers. Header 5 is intentionally absent; five-card arrow paths
are impossibility certificates for the four-header kit. Colored counters,
sleeves, markers and ordinary scrap paper are physical supplies, not missing
cutouts. The new student sheets themselves are the mats.

## Source and physical limits

MIT Lecture 4's opening recoloring theorem/proof and the 2018 MIT text's parallel
scheduling section (printed pp.435–438, Theorem 10.5.8/Corollary 10.5.9) were
consulted directly; the 2011 Cereceda et al. publisher abstract/bibliography was
checked. Other outline bibliography is explicitly marked not directly consulted
as a proof source, with unresolved edition/year/locator details recorded in
`SOURCES.md`. A direct Erdős-paper fetch failed; the optional MSRI originals are
absent. The guide does not pretend those sources were inspected or use their
unverified locators as proof authority. All needed elementary proofs are given.

**The guide and pages are unpiloted and physically unrehearsed.** Print scale,
counter/letter visibility, sleeve glare, kit handling, partner enforcement,
preparation times and one-hour pacing have not been tested in person. No claim
of approval or critic completion is made. Claude's independent guide critique is
next under the parent brief.
