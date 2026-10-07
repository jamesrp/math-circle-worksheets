# Week 76 final student/adult pair review

## Verdict

**PASS for digital pair review. No blocking or nonblocking correctness, answer-completeness, layout, or package-portability issues found. No source changes requested.** This verdict applies only to the exact files identified below. It does not establish physical handling, timing, age feasibility, learning outcomes, or classroom readiness. Those remain untested, as the guide explicitly says. Release/publication remains the coordinator's decision.

Fresh review-only stage on `dot/week-76-pair-review`. The final PDFs, not earlier reviews or author assertions, controlled this review. Read AGENTS.md, README.md, the run-local PROMPT.md/GUIDE.md and the mathematical research note. No delegation, source/PDF edits, commits, or pushes were performed.

## Controlling artifacts

| Artifact | Pages inspected | Bytes | SHA-256 |
|---|---:|---:|---|
| `final/students.pdf` | 4 of 4 | 95,388 | `58da69e16b1c4f3b5cf637a655efd340939c107cde8176baf6c2a768416d928a` |
| `final/facilitator.pdf` | 4 of 4 | 189,840 | `e5094cf9256fa6da6b9dcc416fae260b2c65f3b7a7d3b7521582263e5e4c7393` |

All four student pages and all four guide pages were rendered at 110 dpi and individually inspected. Page size is US Letter, 612 × 792 points. Source hashes are recorded separately in `pair-verification.json`. Both original PDF hashes were checked again when the reports were written.

## Located findings

None. Therefore there are no severity-rated defects or required fixes. The checks below explain the basis rather than treating a successful compile as a content review.

## Independent mathematical and answer checks

The reviewer wrote `pair-review/independent_math.py` without importing or reusing either packaged checker. Fixed instances were transcribed from the final PDFs. The exact bounded-language check uses a different certificate from the guide checker's closure algorithm: partition the infinite fixed point into 16-letter fourth-generation supertiles. A factor of length at most 16 is contained in one or two adjacent supertiles. All four parent bigrams AA, AB, BA and BB occur already in the eight-letter generation. Consequently the union of the windows in their four substituted 32-letter blocks is exactly the genuine factor language through length 16. This is an exhaustive finite certificate with a stated covering argument, not an inference from inspecting a long prefix. A separate binary-digit-parity implementation cross-checks the generated word and local identities.

- **Student p.1 conventions; guide p.2 launch:** BA produces BA | AB and then BAAB. The old row remains separate, and each original tile is used once. The non-task example does not disclose the requested triple inventory.
- **Problem 1, student p.1 / guide p.2:** the generations are A → AB → ABBA → ABBABAAB → ABBABAABBAABABBA. All 14 overlapping windows in the final row give exactly AAB, ABA, ABB, BAA, BAB and BBA. All six already occur in the eight-letter row, as the guide states. The guide correctly explains that the eight blank recording slots are not a claim of eight answers.
- **Problem 2, student p.1 / guide p.2:** AAA and BBB are impossible. In either start parity, a three-position window contains a full AB/BA child-pair. The argument applies at every generation where a triple exists, not merely to the printed row.
- **Problem 3, student p.2 / guide p.2:** the complete four histories agree. ABBABAAB → ABBA → AB → A succeeds. ABBAABBA → ABAB → AA fails. ABBABBAB contains the invalid first-generation split AB | BA | BB | AB. ABBABAABABBABAAB → ABBAABBA → ABAB → AA fails. Only the first is a whole generation. The separate convention example BAABBA → BAB is correct and carries no whole-generation claim.
- **Problem 4, student p.3 / guide p.3:** all end-removal choices were enumerated. ABA has AB | (A), retaining A, and (A) | BA, retaining B. BAABA has only BA | AB | (A), retaining BA. AABB has only (A) | AB | (B), retaining A. ABBAABBA has only AB | BA | AB | BA, retaining ABAB. The guide lists all of them in the same reading order as the student page. Completeness follows because the first tile is either paired or lone; all later positions are then forced. The worked AABBA crop has only (A) | AB | BA and retains AB.
- **Problem 4 genuineness and limits:** all four crops really occur. Zero-based witnesses in the generated word are ABA at 3, BAABA at 8, AABB at 5 and ABBAABBA at 20; the last is already witnessed in the 32-letter generation. ABAB occurs at 10. Thus the crucial distinction between a crop and a full generation is mathematically real. Immediate legal pairing is not confused with recovering an absolute location or a unique full ancestry.
- **Problem 5, student p.3 / guide p.3:** all 12 genuine five-letter factors have exactly one immediate pairing. The full list is AABAB, AABBA, ABAAB, ABABB, ABBAA, ABBAB, BAABA, BAABB, BABAA, BABBA, BBAAB and BBABA. The printed general explanation is sound: a five-letter alternating word would have three equal first, or three equal second, members of consecutive true child-pairs, forcing a forbidden triple in the parent. Thus a genuine five-letter crop has equal neighbors, whose gap fixes the seam parity. The true decomposition exists, so the argument proves uniqueness, not merely at-most-one. A crop longer than five inherits the same forced alignment. Clipped endpoints are explicitly accounted for rather than silently declared to be generation boundaries.
- **Problem 6, student p.4 / guide p.3:** ABABA is a valid finite obstruction inside the repeating AB strip. The first ten tiles ABBAABBAAB of the repeating ABBA strip have forced pairing AB | BA | AB | BA | AB, retaining forbidden ABABA. The length-ten crop has no discarded endpoint in this pairing. ABBAABBA itself is genuine, so the guide correctly declines to use that shorter aligned prefix as an obstruction. The repeating ABBA word avoids AAA, BBB, ABABA and BABAB at every possible start modulo four, demonstrating the stated limit of the local bans.
- **Problem 7, student p.4 / guide p.4:** the eventual-nonperiodicity proof was checked analytically. The fixed point identities are T[2n] = T[n] and T[2n+1] = the complement of T[n]. Every aligned block beginning at 4k is ABBA or BAAB, so an equal pair occurs at 4k+1 arbitrarily far into any proposed tail. An odd period shifts that equal pair to an even start, impossible inside an unequal child-pair. If an eventual period is 2q with tail threshold N, use n ≥ ceil(N/2) to obtain T[n+q] = T[2n+2q] = T[2n] = T[n]. Thus q is an eventual period of the same word. Repeated halving eventually yields an odd positive integer, completing the contradiction for every period and every finite discarded beginning. No finite computation is substituted for this argument.
- **Guide p.2 fallback:** for both allowed row lengths, every possible single-tile flip was independently checked to invalidate a whole generation. The unchanged row remains valid.

The student and guide packaged checkers also pass. Their results supplement, rather than replace, the reviewer's independent finite computation and the analytical proof review.

## Mathematical overview, teaching route and preparation

- **Guide p.1 opens theorem-first:** definition, pair invariant, local bans, crop alignment and the precise infinite claim all precede timing and individual answers. Assumptions and limitations are explicit. The endless word is defined through nested prefixes; no infinite object is inferred from a long finite experiment.
- **Hints and stopping points, guide pp.2–4:** each problem begins its hint sequence with a question or action. Core Problems 1–4, further Problems 5–6 and adult-supported Problem 7 are distinguished. The text records experiments/conjectures separately from all-case explanations and distinguishes adult-supplied proof from a child's explanation. It does not demand that every child finish the packet in one hour.
- **Prerequisite-led scope, guide p.1:** the target is the current three-child 4–5 table with one organizer, using a pair and rotating referee. The optional four third graders use two pairs with their own mathematician. Reading A/B strings, preserving order and working with a partner are explicit; parity and arbitrary-period reasoning arrive late. No K–1 route or unsupported learning-outcome claim is invented. The separate K–1 activity is correctly left as an advance organizational requirement.
- **Legal concrete operation:** the shared student rule and launch preserve old/new state, and the partner checks one substitution per original tile. The p.2 decode example precedes inverse use. The p.3 example explicitly distinguishes a lone endpoint from a complete pair before children use cropped strips. There is no need to fabricate exact-fit pieces.
- **Guide p.1 quantities:** one kit has 36 reversible A/B tiles including four spares, four dividers, two pencils, one key, two labels and two blank sheets. One target kit plus two spare dividers yields 36 tiles and six dividers. Three kits plus two shared spare dividers yields 108 tiles and 14 dividers, with the other listed quantities tripled correctly. Reversible labeling allows either letter distribution.
- **Dimensions/capacity:** the largest required growth holds eight old plus 16 new tiles, needing 24 simultaneously; two 16-tile rows for a shift demonstration also fit the 32 working tiles. Sixteen minimum-width 15 mm tiles take 240 mm before gaps, consistent with about 300 mm including working space. Four markers are explicitly for local use while gaps separate other pairs. The printed 7–10 mm boxes are labeled as references rather than 15 mm counter mats. Larger tiles require proportionately more table space, which the tile-width wording already states.
- **Printing:** four student sets for the three-child table plus a spare are 16 sheets; five further sets for the optional four-child table plus a spare add 20. One four-page guide per participating adult, US Letter, single-sided at 100%, and staged issue of pages 2–4 are all explicit. No cutting or taping is required; optional scissors are counted per active table.
- **Timing and physical limits:** the hour totals 60 minutes and includes initial movement, a three-minute launch, flexible investigation blocks, fallback, sharing and clearing. Timings are explicitly estimates. Rehearsal with actual tiles and classroom piloting are explicitly unperformed, so practical feasibility remains a hypothesis to test rather than a verified property.

## Page-by-page visual inspection

- **Student p.1:** consistent header/footer and ID; BA → BA/AB → BAAB diagram has correct ordered labels, arrows and parent brackets; square cells are undistorted; 16-cell record and eight triple slots are clear; both questions have usable space.
- **Student p.2:** six-to-three inverse example is clear; all four claimed strings match the answer key; generous separation and record space; no clipped symbols or ambiguous labels.
- **Student p.3:** dashed lone tile and retained AB distinguish end clipping; all four crop strings match the key; both Problems 4–5 are complete and separated.
- **Student p.4:** both 16-tile repeating illustrations and continuation ellipses are correct; Problems 6–7 have generous working space; the ordinary line-end hyphenation in “repeat” is legible.
- **Guide p.1:** theorem-first hierarchy is clear; all quantities, optional-table instructions and untested-status statement fit without clipping.
- **Guide p.2:** launch, schedule, fallback and all Problems 1–3 answers are complete; chains and inline bars are legible, with no overlap.
- **Guide p.3:** all pairing-table rows and parent outputs are correctly aligned; Problems 5–6 explanations and complete finite certificate are legible.
- **Guide p.4:** the complement bar over T[n] is visible in the rendered self-similarity equation; the odd-period and even-period cases are complete; source URLs wrap legibly; after-session notes and footer fit.

Every page has its correct Week 76/topic/packet header and Bellingham footer, matching packet version, and correct consecutive page number. No overflows, overlaps, cropped text, black boxes, mislabeled diagrams or answer omissions were found.

## Research/provenance check

The three cited author-hosted references were opened and checked on 2026-10-07:

1. Richard G. Swan, *The Morse Sequence*, p.2 Lemma 2.2 supports the pair parity, triple prohibition and stronger actual-occurrence alignment facts. https://www.math.uchicago.edu/~swan/expo/Morse.pdf
2. Carl D. Offner, *Repetitions of Words and the Thue-Morse sequence*, §3 pp.2–3 properties 1–6 supports the recurrence, parity and five-symbol arguments. https://www.cs.umb.edu/~offner/files/thue.pdf
3. Jean-Paul Allouche and Jeffrey Shallit, *The ubiquitous Prouhet-Thue-Morse sequence*, §3.3 Proposition 3 gives the substitution fixed point; §4 Proposition 4 identifies the recurrent but not ultimately periodic sequence. https://cs.uwaterloo.ca/~shallit/Papers/ubiq15.pdf

Titles, authors, named locations and mathematical scope are accurate. The sources are substantive mathematical expositions, and the guide does not present them as the original historical publications. Its independently arranged teaching presentation does not claim a new theorem. The aperiodic-tiling remark is limited to a general connection and expressly claims no geometric tiling result; no hat artwork or hat proof is represented as part of this packet.

Each portable source folder contains only its owned README, builder, checker and TeX source. There are no downloaded papers, whole books, copied workflow exemplars, images, external font files, TeX runtime dumps or raw tool reports in either source folder.

## Isolated reconstruction and evidence

Copied only the four guide-src files into `pair-review/isolated-guide/source/`, then ran its unchanged builder from the isolated parent directory. The builder uses only those files plus the documented standard Python/TeX installation. Used the supplied minimal-cloud TeX environment (`TEXMF` pointing to system TeX trees and `TEXFORMATS` pointing to the run's initialized format); this is environment configuration, not a hidden package-source dependency. A normal TeX Live/MacTeX prerequisite is acceptable and documented.

The rebuilt guide passes its checker and overfull-box rejection, has four pages, and matches the original extracted layout text and all four 110-dpi PNGs byte-for-byte. Its PDF hash is `596b871d9b23744fc3cf283f1341502a98f6e5642a1ad891bcca5fa54a477c96`. The rebuilt PDF itself differs in build timestamps and PDF ID, so byte-identical PDF output is not claimed.

As an additional source/output consistency check, the student package was rebuilt in its own isolated folder using only its four portable files and the same standard environment. All four extracted-text/raster comparisons also match exactly. The rebuilt student PDF hash is `8d922cdaf8f41b31719d074c84f9fa7112a6af562ac94a02da8e1077d1a81e00`.

Evidence remains in this run:

- `pair-review/independent_math.py` and `pair-review/independent-math-results.json`
- `pair-review/rendered/` (all eight inspected final-page PNGs)
- `pair-review/logs/` (original hashes, independent math and isolated build logs)
- `pair-review/isolated-guide/` and `pair-review/isolated-student/` (copied portable sources, rebuilt PDFs, extracted text and comparison rasters)
- `pair-verification.json` (exact controlling and source hashes, page counts and checks)

No physical printing, tile handling, teaching rehearsal, classroom pilot, or remote publication verification was performed. Those are not silently promoted to passed digital checks.
