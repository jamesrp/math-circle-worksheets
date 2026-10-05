# Week 63: Cards away from home

**Verdict: revise.** The mathematics, the problems and their order are right, and every answer checks. The one must is the K–1 table, which has no route after the launch, although P1, P3 and P2's sorting are object work K–1 can do.

Reviewed October 5, 2026 by Claude, with the math check in [week-63-math.md](week-63-math.md). Two card runs agreed on the verdict, the must and every should; this card reconciles their wording and fixes. Packets: week-63-students.pdf, W63-S-v2, 9 pages (pp. 1–2 Grades 2–5, Problems 1–2; pp. 3–5 Grades 3–5, Problems 3–5; pp. 6–9 Grades 4–5, Problems 6–9); week-63-materials.pdf, W63-M-v2, 3 pages. Adult guide: week-63-facilitator.pdf, W63-G-v1, 10 pages. Companions noticed but not reviewed: none exist. Status: unpiloted; guide p. 3 lists cutting, placement, markers and the reversal rehearsal as unperformed. Written October 4 under the 52–63 routing, whose source notes say "do not create a forced independent K-1 packet"; the fix below adds a route through existing pages, not a packet.

## The mathematics

Children place lettered cards in lettered homes and hunt for rows with no card at home (derangements): 2 for three cards, 9 for four, 44 for five. Fixing k chosen matches leaves (n − k)! rows. Subtracting each home-group removes shared rows twice; the alternating correction counts a row with m ≥ 1 matches 1 − m + C(m,2) − … = 0 times and a home-free row once. Separately, with E's home fixed, the home-free rows split into a reciprocal family and a longer-loop family, each rebuilt reversibly from a smaller home-free row, so D_n = (n − 1)(D_{n−1} + D_{n−2}). A mathematician would enjoy two proofs meeting at 44. P1 and P3 (catalogs), P2, P4 and P5 (overlap repair), P6 (cancellation) and P7–P9 (families) carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Two classical proofs of one count, with honest hypotheses: inclusive overlaps, D₀ and D₁, own-home bans only. P4 (only A and B forbidden: 14, not 9) separates some homes from all. |
| Problems | strong | Each is a catalog, a repair or a construction. Contrasts: overlap 1 (P2) against 2 (P4); two forbidden homes (P4) against four (P5); D at A (P7, 3 rows) against E at A (P8, 11). P1 and P3 print more boards than answers. Thin spots: P2 is short, and p. 8 pre-solves P8 (fix 2). |
| Student pages | adequate | Header, footer and numbering right; no Name/Date, no slop. Non-task worked visuals before first use on pp. 1, 2, 7 and 8. Faults: no K–1 route, p. 8 prints P8's constructions, P8 has four ruled lines for eleven rows. |
| Concreteness | strong | One physical card per letter enforces one card per home, with home letters visible above. Complete 6- and 24-outcome decks make the universe sortable, and open rings make "one row in two groups" physical. Guide p. 2 launch: handle cards, freeze a placement, check, record the non-task VUWX. P6 and P8–P9 are paper work by design. |
| Correctness | strong | No student error (math.md, 146 checks). Both card runs' own enumerations agree on P1–P4, P7, P8's 11 rows, all four P9 branches and D₅ = 44. Two minor items (fixes 4 and 5). |
| Adult guide | strong | Theorem-first overview with hypotheses, limits, band map and levels of evidence. Full keys, including all fifteen P5 intersections and the 44 rows by family; the general proof, launch, route, kit counts, pretest list. No K–1 route. |
| Age fit, K–1 | weak | No page. Guide p. 2: "The youngest have no independent K–1 packet. Offer an oral two-card, then three-card home-free trial …"; otherwise "return to free arranging or an already familiar concrete activity". |
| Age fit, grades 2–3 | strong | Cards and decks hold the state; sums stay within 24, and an adult may write the subtraction. P3's catalog of 9 is real work. The p. 1 rules (seven sentences, two new terms) need reading aloud. P5's four groups come late. |
| Age fit, grades 4–5 | adequate | P3–P4 and P7 are concrete starts, acted out and checked with cards; P6 and P9's rule come late, with the organizer. P8 asks a child to track eleven rows, arrows, two families and smaller rows in four ruled lines; P9 packs catalog, pooling, rule and explanation into one problem. |

## Keep

- p. 1: the VUWX placement → check the same placement → record visual on non-task letters; P1's ten boards for two rows, and "Can a row of these three cards have exactly two home matches?"
- p. 2: the one-outcome, two-group visual; P2's six outcome cards, "C may stay home", and the 6 − 2 − 2 = 2 count to repair (likewise 24 − 6 − 6 in P4).
- P3: sixteen boards for nine rows; "a catalog your table can check for repeated or missing rows". P4 on the 24-card deck. P5's inclusive-overlap sentence. P6's per-row explanation.
- p. 7: QRSTP → "P is in home T" → pentagon; P7's A-in-home-D split, which matches a P3 branch.
- P9: one branch per child, pooled; its 44 cross-checks P6.
- Materials: picture-and-letter cards, whole strips, complete decks with row IDs, twelve blank A–E records per copy.
- Guide: the overview, the launch, the P5 intersection table, the 44-row family table, the P8–P9 keys and the pretest list.

## Fix

1. **must**, K–1, guide p. 2, student pp. 1–3, materials pp. 1–2. The K–1 table (four children with the parent volunteer) gets an oral two-card, then three-card trial and then nothing: neg.md's K–1 packet shorter than the mathematics allows, though the placing and checking suit K–1 well. The Week 53 card treated its one-page K–1 route the same way. Fix:
   - Head pp. 1–3 "Grades K–5".
   - Draw each card's shape in its home cell (materials p. 1) and beside the letters on the six A–C outcome cards (materials p. 2), so non-readers can see a match.
   - Replace the guide paragraph with a K–1 route: the launch; P1, both questions; P2's two-ring sort up to "How many rows are outside both groups?" (the student's count optional); P3 split by the card in home A, one branch per pair (three rows each; the p. 4 table is the key), pooled to 9; then aloud, "Can exactly three of A, B, C, D be home?" Give a plain-words key.
   - The adult reads the rules as two sentences and scribes; children place and check.
2. **should**, 4–5, p. 8, P8. The worked removals ("P and U point to each other. Remove both."; "T → U → P becomes T → P") are the two constructions P8 asks for ("How can each family be built from smaller home-free rows? Give constructions you can reverse."). AGENTS.md wants a non-task demonstration "without revealing the main theorem"; these are its proof. Fix: move both to guide p. 7 as a held hint and keep "Smaller arrow loops keep their remaining letters." If the organizer prefers the demo, cut "These examples remove U, then can be read backward to restore U." and end P8 with "Turn each row into a smaller home-free row. Does every smaller home-free row come from exactly one of yours?"
3. **should**, 4–5, p. 8, P8 asks for eleven A–E rows with their arrows; the page has four ruled lines, while P9's branch of the same size gets sixteen boards. The guide reserves materials p. 2 blanks only in its prep table ("if taking P8–9"). Fix: replace the lines with 12 A–E boards, some with five-circle arrow spaces like P7's, or say in the guide's P8 section that the pair takes one set of 12 blank records, which become P9's A branch.
4. **should**, 4–5, p. 9, P9: "a counting rule for two or more distinct cards". At two cards the rule needs D₀ = 1, which guide p. 10 says not to demand (math.md item 1). Print "three or more"; on guide p. 9 write the rule from D₁ = 0 and D₂ = 1.
5. **could**, guide p. 6: "The number of intersections of size k containing that row is (m choose k)." The table above uses "size" for row counts; write "intersections of k named home-groups" (math.md item 2).
6. **could**, p. 2: "It can belong to several groups at once" repeats P2's "A card may belong to both groups"; keep one, and move "Group the outcome cards on the table." to the guide.
7. **could**, p. 1: cut "different rows count separately", which gives a child nothing to do.
8. **could**, P9: "Choose one of homes B, C, D for E", since P8 builds the A branch.
9. **could**, guide p. 3: name the "small lettered markers" (lettered sticky dots), or let children circle matches on the outcome card. Guide p. 2's launch also needs a VUWX outcome card and W/X markers that no material supplies; point to the printed p. 2 example.
10. **could**, guide p. 2: the first route runs 43–53 minutes after a 6–8 minute launch; context.md allows thirty-five to forty minutes at the tables.
11. **could**, guide p. 2 launch: "Put one card in each matching set of homes" reads oddly; "Put each card on the strip with the same letters."
12. **could**, guide pp. 2 and 10: cut residue ("superseding the older ten-child snapshot in the root README"; "not a claim of publication, remote upload or classroom success").

## Overlaps

- Week 43 obtains BCA and CAB from a no-self-swap shuffle (Grades 4–5 p. 3, P5); guide p. 4 credits it.
- Week 3's machine loops are P7–P9's card-to-home arrow loops, drawn the same way; the guides could point returning children there.
- Week 19 has overlapping subsets but no inclusion–exclusion count. No other theme has derangement counts, overlap correction or the two-family recurrence. No merge.

## App fit

B, confirmed: size S for catalogs, M with the families. Lettered cups on lettered homes replace the cards, and the app lights any cup at home, so the rule enforces itself. Solves:
- **Catalogs.** Home-free rows for three cups (2) and four (9); branches with D at A (3) or E at A (11); partial bans on the 24 rows: 18, 14 and 11 for one, two and three forbidden homes. Keep every row, then claim "That's all" with no visible count; a wrong claim gets "There's another." The certificate is the catalog split by the cup in home A.
- **Ring sort.** Rows into two overlapping hoops (P2, P4), with those outside both counted.
- **Impossibility.** Exactly two of three home, or three of four. The certificate is an argument (the last cup is forced home), not an object, so it suits a playground or grown-up prompt better than a puzzle.
- **Removal pairing.** Match each of the eleven E-at-A rows to its smaller row; the pairing is the certificate (P8).

Pitfalls: no "x of 9" counters; four cups are few enough to brute-force, so ask for every row, not one; 44 rows is a chore. No typed inclusion–exclusion totals or predict-the-count questions: P5–P6 and P9's rule stay on paper. Only the final row counts here; a fewest-swaps puzzle (every cup away in ⌈n/2⌉ swaps of any pair) would belong in Cup swaps.

Ported October 5, 2026 as Mixed-up cups in the app's puzzle satchel (catalogs, hoops, the two families as columns, a playground), on the app's shared case engine; not on the Lantern Road, not deployed and not yet played by children. Impossibility and removal pairing are not in it.

## Classroom evidence

None reported. The packet is unpiloted; themes.md lists only Weeks 1, 2 and 15 as taught, and no use record mentions Week 63.
