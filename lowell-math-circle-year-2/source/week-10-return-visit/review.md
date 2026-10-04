# Week 10 return-visit critic review

Reviewed the actual shared seven-page `draft/return-visit.pdf`, the complete writer brief, current `AGENTS.md`, and the editable source. The shared packet explicitly overrides the generic three-band harness filenames. This is the fresh critic stage only; the separate fresh math review and revision stages still remain necessary.

**Recommendation: retain all three investigations and the seven-page student layout. No essential student-page defect was found.** There are two precise handoff corrections for the separate adult/materials work below. Do not cut the password investigation or print a bridge-avoidance algorithm on the student pages.

## Scope and visual evidence

I rendered the actual draft at 1.5 scale and inspected all seven individual pages, rather than relying on extracted text or a contact sheet. Renders and a check of active street commands are in `critic-render/`. Draft PDF SHA-256: `3b50c56c4ff4a82b7ee875e5174ca1c6f7ef74216eea7bfb4ce5c57c6008c9a1`. Generated TeX SHA-256: `71882a72e31c568c743537d6924c17d095500b724501305e30320d80038fd63b`.

| Page | Investigation and band | Review finding |
| --- | --- | --- |
| 1 | Problem 1, four small arrow towns, K–5 | Worked X → Y → Z action has input, a consumed first street, and output with matching labels. Actual arrows are visible and correctly directed. The two triangle orientations and two path orientations make purposeful contrasting attempts. Adult reading at K–1 is realistic; walking and resetting remain the children's choices. |
| 2 | Problem 1 continued, towns 5–6, 2–5 | Two large towns share the underlying undirected shape but have different direction obstructions. Counter locations, island labels and arrows are separated; no clipping or unmarked crossing. |
| 3 | Problem 1 continued, towns 7–8, 2–5 | The disconnected pair of cycles deliberately contrasts with two cycles sharing an island. This exposes the connectivity assumption rather than treating balance alone as sufficient. |
| 4 | Problem 2, towns 1–2, 2–5 | Same undirected triangle-and-tail with different starts is purposeful. Star locations are unmistakable. The reset instruction correctly restores the original town before each first-choice trial. |
| 5 | Problem 2 continued, towns 3–4, 2–5 | Square-plus-diagonal supplies an all-first-choices case; two joined cycles supply another premature-bridge trap. Large boards support direct counter work. |
| 6 | Problem 3, linear passwords, 4–5 | The non-task two-button window has three explicit consecutive positions and outputs 01, 11, 10. All eight target triples are supplied; the row construction and minimum question leave the method open. Blank row regions do not reveal the optimum. |
| 7 | Problem 3 continued, circular passwords, 4–5 | Clockwise reading and the join are explicit. The illustrated last–first window is 10 and the complete two-button example has exactly the three displayed windows. Blank circles have no predetermined number of positions. |

Headers, footer ID, page numbers, typography and margins are consistent. No Name/Date fields, second page titles, generic encouragement, numbered micro-steps or automatic proof follow-ups are present. Continuations do not falsely count as new investigations. Town numbers are diagram identifiers, not extra activity headings.

## Mathematical consistency checked by the critic

The active street commands in the generated TeX, not an import of the writer's checker, give these results (`critic-render/instance-check.json`). This check is supplemental critic evidence, not a substitute for the requested fresh math stage.

- Directed Problem 1: towns 1, 3, 5 and 8 have complete walks; towns 2, 4, 6 and 7 do not. Legal starts respectively are A/B/C, A, A, and A/B/C/D/E. Town 5 permits either outgoing street from A first. Town 7 is balanced but disconnected, so its failure is essential.
- Undirected Problem 2: the safe first streets are town 1 AB/AC, town 2 AD, town 3 AB/AC/AD, and town 4 AB/AC. Crossing AD first in town 1 strands the token at the leaf even though the remaining triangle is internally connected; a later explanation must include reachability **from the new token location**. Town 2 correctly shows that the same bridge is safe when it is the only available first street.
- The printed row demonstration gives 01/11/10; the clockwise circle demonstration also gives 01/11/10. A linear row of length L has L−2 three-button windows, so eight distinct triples require at least ten tiles; `0001011100` attains ten. A circle of n tiles has n starting positions, so it requires at least eight; `00010111` attains eight. These are lower-bound-plus-construction arguments, not conclusions from testing a few rows.
- The two canonical triple necklaces mentioned in the adult draft are genuine continuation material; they need not be enumerated by each child or added to the student task.

The current ordinary-walk language and worked action are sufficient after the shared launch: one walker travels along available streets rather than jumping between components. There is no need to add a list of prohibitions. The explicitly stated either-way rule at Problem 2 correctly resets the earlier arrow convention.

## Substance, independence and operational age fit

There are **three investigations**, not twelve town problems or two separate password investigations. Each has enough independent mathematical work for a return visit: contrasting arrow obstructions, first-choice experiments with counter resets, and shortest linear/circular constructions with genuinely different window counts. The children retain route, starting-point and construction choices. No advanced notation or formal graph theory is needed for entry.

Page 1 is a plausible K–1 acted entry with ordinary adult reading; pages 2–5 ask for more sustained comparison and are sensibly labeled 2–5. Do not create a nominal K–1 password version. The password task requires holding the idea of overlapping triples; the two-button example and physical window make it accessible for the upper group without giving away a construction. A first route can use just page 1 or a few first-choice cases. Remaining pages support later visits, not a completion demand.

Printed counter circles are placement marks, not the required counter diameter. The source uses inch scaling without unequal axes or unmarked street intersections. Arrowheads on the short path examples are close to the physical 0.75-inch counter limit; the recorded clearance is digital evidence only. The delivered guide should require actual-size printing, the stated counter limit, and a tabletop fit trial. No physical rehearsal or classroom success has been established by this review.

## Novelty and two adult-work handoff corrections

I read the current Week 10 K–1, 2–3 and 4–5 student PDFs and adult guide, and extracted the actual prior-year `Handouts 10.docx`. The base students investigate undirected starts, parity, repairs, drawings, loop splicing and minimum repeated crossings. They do not supply directed-town or safe-first-street investigations. The prior-year second Problem 10.1 really does ask for shortest two-digit-password strings over three and then four symbols. The new binary triples, linear-versus-circular change and directed overlap connection therefore make a substantive continuation rather than a mere change of numbers.

1. **Correct the history wording in the guide/inventory.** The current base adult guide, page 7, under “Where it goes next”, already names directed incoming/outgoing balance, de Bruijn sequences and Fleury's advice. The outline's categorical statement that F10-v4 does not include these topics is too broad. State that this companion turns those previously named extension directions into concrete student investigations, and acknowledge the year-1 password precursor. This does not undermine the three-investigation count; it makes the distinction between a named theme and delivered tasks accurate. The existing student draft makes no false novelty claim, so no student rewrite is needed.

2. **Synchronize guide preparation and the optional conversion launch.** The provisional guide says the larger town layout boxes are 6.8 × 2.95 inches, but `generate.py` and the actual TeX use **6.8 × 3.2 inches**. Correct that dimension before release. If the optional overlap-to-street conversion is used with children, add a small worked visual in the adult guide or preparation card before the full four-island map: for example input triples `ABC`, `BCD`; highlight their shared `BC`; then output `AB → BC → CD` and the joined row `ABCD`. This is a non-task alphabet and does not reveal the binary target necklace. The conversion is absent from the student pages and may stay as an adult-led readiness-dependent continuation.

The first point is an evidence correction; the second combines a definite dimension mismatch with an explicit current AGENTS.md convention-example requirement that applies when the new conversion is introduced. Neither warrants expanding the student packet or adding optional scaffolding to its tasks.

## Revision boundary

The reviser may preserve the student content and use the final-source/build/package workflow. Keep the optional proofs, graph conversion and first-route timing in the adult guide. Re-render and inspect the actual final seven pages after any revision, then complete the fresh mathematical review, portable package checks and clean extracted-source rebuild before release. This review establishes a usable draft, not classroom piloting or physical readiness.
