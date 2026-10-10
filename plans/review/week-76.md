# Week 76: Substitution strips

**Verdict: keep.** No must: real Thue–Morse mathematics in seven well-ordered problems, every answer right, a theorem-first guide. The missing K–1 route is a should, as on the Week 60 and 62 cards, because the prototype is routed to Grades 3–5 by design.

Reviewed October 10, 2026 by Claude, with the math check in [week-76-math.md](week-76-math.md). Packets: week-76-students.pdf (F76-35-v1, 4 pp., one shared Grades 3–5 packet, Problems 1–7). Adult guide: week-76-facilitator.pdf (F76-FAC-v1, 4 pp.). Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review; guide p. 1: "Physical rehearsal and classroom piloting remain unperformed." The card agrees with all three math-check findings (fixes 2–4) and rates each a should.

## The mathematics

Rows grow from A by replacing every A with AB and every B with BA at once; each row extends the last, giving the Thue–Morse word. True pairs are unequal, so no row has AAA or BBB (P1–P2). An alternating ABABA would force a parent AAA or BBB, so a genuine piece of five or more tiles splits into pairs one way only, and hidden seams can be recovered (P4–P5). A whole row is not a piece: ABBAABBA fails as a row (P3) yet occurs as a piece (P4). The repeating ABBA strip passes every local ban, but ABBAABBAAB decodes to ABABA (P6), and the endless word never settles into a repeat, by period halving (P7). A mathematician would enjoy it: decoding is the proof tool at every scale.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Substitution, local bans, unique desubstitution, a finite certificate against a periodic impostor, aperiodicity; limits stated. |
| Problems | strong | Claims failing after one, two and three undos (P3); ABA's two pairings against forced longer pieces (P4); impostors caught at one level and at two (P6). The order carries the development. Thin spot: fix 2. |
| Student pages | strong | Spec header and footer, no slop or hints. Each new procedure gets an input, intermediate, output visual on a non-task instance (BA → BAAB; BAABBA → BAB; AABBA → AB, dashed lone tile). Eight triple slots for six answers. Faults: fix 3. |
| Concreteness | adequate | Lettered tiles, a kept old row, a partner check; guide p. 2's launch has children build BA → BAAB. But nothing supplies the tiles (fix 5), pairs drift from parents (fix 6), the partner rather than the material enforces the rule, and the launch covers two tables. |
| Correctness | strong | No wrong answer (math.md: strips, factors to length 24, all pairings, every key). My enumeration agrees on P3, P5 and the P6 offsets. |
| Adult guide | strong | Theorem-first overview with limits and routing; full keys, ordered hints, stopping points, the P5 and P7 proofs, kit counts, a fallback game. Gaps: fixes 2 and 4. |
| Age fit, K–1 | weak | No route, by design: "This is not a K–1 packet." (guide p. 1). |
| Age fit, grades 2–3 | adequate | Claims grade 3 only; no grade 2 route. Third graders work with their mathematician and stop at P4 (guide p. 1). No arithmetic; the adult reads P4's two conventions aloud. |
| Age fit, grades 4–5 | strong | A pair and a referee with the organizer; P1–P4 concrete, P5–P7 late, P7 offered as a later visit. |

## Keep

- p. 1: the opening rule; BA → BA | AB → BAAB with "from B" and "from A"; P1's eight slots; P2's "Explain why, or build a row that contains one."
- p. 2: the BAABBA → BAB visual; P3's claims, failing at different depths.
- p. 3: the dashed lone tile; P4's ABA (two pairings), AABB (lone tiles at both ends), and ABBAABBA, just rejected as a whole row; P5's "Find such a piece, or explain why none exists."
- p. 4: P6's impostors, the ABBA strip passing all four bans; P7.
- Guide: the overview and Limits, the launch script, the P4 table, the P5 and P7 proofs, the flip-one-tile fallback.

## Fix

1. **should**, K–1, guide p. 1. No route, so the K–1 table spends the hour elsewhere and the launch is not whole-group. A should because WEEKS-76-78-PROTOTYPES.md says "no forced K–1 editions". Growing with lettered two-colour tiles needs no reading. A route: the launch, P1's growth to 8 tiles, P2 aloud, the fallback game, and P3's claims 1 and 3 undone with tiles. That K–1 manages this is a prediction.
2. **should**, student and guide p. 2, P3 (math.md item 1). Each length has one whole row, and children have just recorded ABBABAABBAABABBA on p. 1: claim 1 is its first 8 tiles; claims 2, 3 and 4 differ at tiles 5, 6 and 9. Matching settles all four in a minute, against 12 planned minutes, and the guide lists only decode records. Add: "Matching against the Problem 1 row also settles every claim, because each length has only one whole row. Accept it, then ask why a rejected row cannot shrink to A."
3. **should**, p. 3, P5 (math.md item 2): "Can two different ways of pairing it fit the replacement rule?" The lone-tile limit is stated only in P4. With a lone tile mid-piece, P4's own BAABA pairs two ways (BA | AB | (A) and BA | (A) | BA), as do ABAAB, ABBAB and BABBA. Write "Can two different ways of pairing it, as in Problem 4, fit the replacement rule?"
4. **should**, guide p. 3, P6 (math.md item 3). Hint 3, "extend the piece by one complete pair", fits pieces starting on the strip's first or third tile (10 tiles); from the second or fourth, complete pairs need 11 (BBAABBAABBA → BABAB). Reading lone end tiles' parents, as the P5 explanation does, makes 8-tile BBAABBAA and AABBAABB certificates. No right answer is called wrong, so not a must. Add both cases.
5. **should**, guide p. 1: "32 reversible A/B tiles plus 4 spare (36 total)… Label both faces". Nothing supplies them or says how to make them, and they carry the concrete core. Name the object (two-colour counters lettered in marker) or add a print-and-cut sheet.
6. **should**, guide p. 2: "Each old tile makes one pair below it." A pair is two tiles wide, so under an adjacent old row of 8 the last pair lands about 10 cm right of its parent, and hint 1's "Can your partner point to it?" becomes counting (a prediction; unrehearsed). Add: "Leave one tile-width between old tiles, so each pair sits under its parent."
7. **could**, guide p. 2: 8–53 is 45 working minutes; context.md allows thirty-five to forty.
8. **could**, P5: "Cut a piece" when nothing is cut; "Choose five neighboring tiles".
9. **could**, guide P7: check that children have seen each row begin with the last, which "the endless strip" presumes.
10. **could**, AB and BA dominoes for growth would make the pair invariant physical.
11. **could**, P3: "Keep a record that settles each decision" → "Show what settles each claim."

## Overlaps

Week 35's footprint borders and bonus study periodic strips, the counterpart of P7. Week 17's machines read two-letter rows; T[n] is the parity of n's binary 1s, a two-state machine, a good return link. Week 39 shortens words by a different local rewriting. The guide's "Where next" points to aperiodic tilings (Week 1) without a shared theorem. No other theme has substitution or aperiodicity. No merge.

## App fit

Proposed B, size M; themes.md has no row. It should read: | 76 | Substitution strips | Grow A→AB, B→BA rows; undo them; find hidden seams in cut pieces; catch repeating impostors | No AAA, BBB, ABABA or BABAB; a piece of five or more pairs up one way; the endless word never repeats (Thue–Morse) | No (Detours' step row is the nearest UI) | B | Tap gaps to place seams and Shrink a level; find the stretch of an impostor that shrinks to AA, BB or AAA | M |

On screen: a strip of lettered tiles. Tapping a gap drops a seam; Shrink replaces each complete pair by its first letter and marks any AA or BB. Growing is a playground, not a solve. Solves:
- **Catch the impostor** (P6). A repeating AB or ABBA strip, or a long grown strip with one tile flipped: select at most k tiles that no grown row contains. The certificate is the child's shrink chain ending at AA, BB or AAA; the validator is the exact factor language, as in the math check.
- **Repair a piece.** A cut piece with one tile flipped: find every fixing flip, then That's all. Screen instances: about 3% of single flips of a 12-tile piece stay genuine, and some pieces have two fixes.
- **Every seam** (P4): short pieces such as ABA have two placements.

Pitfalls: seam placement is a two-way choice with instant feedback, so it is a tool, not the puzzle; no yes/no "Is this a whole row?", which is predict-shaped and settled by comparison (fix 2); no "6 of 8" counter for P1. Draw on P4–P6; leave P2, P5's explanation and P7's proof on paper.

**Decision, October 10, 2026.** Port, in Wave 8, with a Shrink tool on a strip of lettered tiles and the exact factor language as the check: catch the impostor in at most k tiles with the child's shrink chain ending at AA, BB or AAA as the certificate, repair a cut piece by finding every fixing flip with "That's all", and every seam placement for short pieces. Growing rows is the playground. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. Unpiloted; WEEKS-76-78-PROTOTYPES.md: "Physical preparation/handling and classroom piloting remain unperformed." themes.md lists only Weeks 1, 2 and 15 as taught.
