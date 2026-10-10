# Week 10: Bridges and one-stroke drawings

**Verdict: keep.** No must. Counters picked up as bridges are crossed make the rule physical in every band, the pages are clean, and the math check found no student-page error. The main fix is one misleading legend sentence in the guide.

Reviewed October 10, 2026 by Claude, with the math check in [week-10-math.md](week-10-math.md); I agree with all three of its findings. Packets: `week-10-k-1.pdf` (F10-K-v4, 12 pp., Problems 1–8), `week-10-grades-2-3.pdf` (F10-M-v4, 12 pp., Problems 1–10), `week-10-grades-4-5.pdf` (F10-U-v4, 12 pp., Problems 1–11). Adult guide: `week-10-facilitator.pdf` (F10-FAC-v4, 8 pp.). Companions noticed but not reviewed: `week-10-return-visit.pdf` (F10-RV-v1, 7 pp., one-way streets) and its guide (RV10-FAC-v1, 5 pp.); the math check found a missing hypothesis on its p. 3. Status: unpiloted (October 3 revision).

## The mathematics

Towns are connected multigraphs. Euler's theorem: a walk over every bridge once exists exactly when zero or two islands have an odd number of bridges; with zero it starts anywhere and returns, with two it runs between them. Around it: the start set is never one island (2–3 P9, 4–5 P6); a new bridge fixes two odd islands (K–1 P6, 2–3 P4–P5, Königsberg); fewest strokes is half the odd points (4–5 P7); loops splice (4–5 P8–P9); and the fewest repeated bridges pair odd islands by paths, so the three-arm star needs 3, not 2 (4–5 P10–P11). A mathematician would enjoy it: a two-way theorem reached by walking and getting stuck.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Both directions of Euler's theorem, handshake, Listing's strokes, splicing, route inspection with a counterexample to the naive bound. |
| Problems | strong | Each problem has two to six contrasting towns or a design or impossibility goal; K–1 P8's towns give 6, 2 and 4 working bridges. 2–3 runs walk, every start, predict, repair, fewest, rule, then tracing. |
| Student pages | strong | Header, footer and Problem labels only; rules once; no do-not-list item. Bands sized for 1-inch counters; boxes and lines where needed. One layout slip (fix 4). |
| Concreteness | strong | A crossed bridge loses its counter; keeper, scribe and referee roles; at the floor-town launch a child walks the house from a bottom corner and gets stuck. Nothing to cut. |
| Correctness | strong | The math check confirms all 55 towns, 36 drawings, the Königsberg map and every key; three slips in guide prose. |
| Adult guide | strong | Theorem-first p. 1 with the pairing reason and a band map; counts and fit tests; timed hour, roles, fallback game; answer figures; full mathematics; record page. One wrong legend sentence (fix 1). |
| Age fit, K–1 | strong | Unlabelled towns, one or two sentences read aloud, colour or check or X. Counting to 6; counters hold the state; pencil dots mark tried starts. |
| Age fit, grades 2–3 | strong | A partner writes the island word during the walk, one recoverable record. P6 is the only long writing; P8's lettered hexagons and double sticks are supplied. |
| Age fit, grades 4–5 | strong | Ten towns before the rule. P4, P6, P9 and P11 are writing-only, each where explanation is the point; P9 is a real proof, late, with the organizer. |

## Keep

- The counter rule, the three table roles and the floor-town launch (guide p. 2).
- K–1: P2 (two starts of six, then all six); P3's three-bridge lens and all-odd arc town; P4's towns that can be walked but not closed; P6; P7's can and can't builds; P8.
- 2–3: P2's four towns (none, two, two, all); P5's 1, 2 and 3 new bridges; P8's four specs, two needing a double bridge; P9; P10.
- 4–5: the Königsberg map (5, 3, 3, 3, room for a B–C bridge); P8's three triangles to splice; P10–P11 with the star at (3, 1).
- Tracing pictures printed twice, with the envelope and circle-with-plus as the "no" cases.
- Guide p. 1, the fit tests and the K–1 answer figures.

## Fix

1. **should**, guide p. 3, K–1 legend: "When every island is filled, it ends where it started." The P3 lens town (two islands, three bridges) has both filled, captioned "✓ any island", and every walk ends on the other island; a parent may expect it to come home. Write "When every island has an even number of bridges, every island is filled and the walk ends where it started" (math check item 1).
2. **could**, guide p. 7: "Directed graphs: an Euler circuit exists if and only if in-degree equals out-degree everywhere" needs "connected" (math check item 2).
3. **could**, guide p. 1: section 1's rule omits "for a town in one piece", which the K–1 rules never state; add it there and to the K–1 P7 key.
4. **could**, 2–3 p. 8: the H town ending P5 sits directly above "Problem 6:", so a child given p. 8 alone may read it as P6's town; start P6 on a fresh page.
5. **could**, source README: `plans/fall-forecast-2026-10-03.md` is not in the repository; link `LOCAL-RESOURCES.md#private-records` as the top README does.

## Overlaps

Week 2 (lamps) shares the parity step: a press flips both ends of a wire as an extra counter does at both ends of a bridge, and its T-joins are 4–5 P10's repeated-bridge sets; its theorem is linear algebra over F₂. Week 39 walks similar maps for another theorem; Week 56 shares only Euler's name. No merge.

## App fit

Fit A, shipped as Bridge Courier; the row stands. Used roads are marked and refused in exact-once mode, as the counters do, and children enjoyed it. My check confirms all 12 instances: the exact-once ones are walkable as posed, and each distance target is the route-inspection optimum. The later problems are well covered: route-07 is the house, route-08 splices loops like Lee's walk, route-09 and route-12 pair six odd junctions as the H town does, route-10 is the window picture, and route-04 shows a repeat costing a path.

It misses the worksheet's centre. Only route-01 and route-07 leave the start open; no town lacks a walk; nothing asks for every start or a repair. A new group could add:

- **Where can it start?** Tap every island that works, or No walk, then Done, with no count shown. A wrong "no walk" gets a walk played back; a right one lights the odd islands.
- **Add a bridge** (K–1 P6, 2–3 P4–P5): tap two islands, then walk. For fewest, half the odd islands certifies that fewer fail.
- **The three-arm star** as a delivery route: 3 repeats, not 2.

Pitfalls:

- In family play the screen says "This route cannot finish within the rules" as soon as a route is doomed, unasked (`dist/networks.js` writes it and `puzzleView` in `dist/ui.js` shows it). In route-07 it appears the moment A, B or E is chosen as the start, so the child is told before walking into the dead end. Keep it behind Hint.
- Roads are straight segments, so a double bridge would hide its twin; Königsberg and K–1 P4 need curved parallel roads.
- "Crossings without dots are not junctions" is the opposite of the tracing pictures; one-stroke pictures need a dot at every crossing.
- Seven of twelve are delivery routes and two are easy, so K–1 entry is thin.

Draw on K–1 P1–P4, P6 and P8; 2–3 P2–P5 and P10; 4–5 P5 and P10–P11. Building towns to a spec (K–1 P7, 2–3 P8–P9) belongs with the shared graph editor.

**Decision, October 10, 2026.** In the app as Bridge Courier. Wave 9's touch-ups of in-app families add the group this card proposes: where can it start (tap every island that works or "No walk", then Done, with the odd islands lit as the certificate), add a bridge with half the odd islands certifying fewest, and the three-arm star. The same pass moves "This route cannot finish within the rules" behind Hint so children walk into the dead end themselves, and lets towns draw double bridges so Königsberg can appear as it is. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported for these packets; unpiloted. Counter fit, counters on craft sticks and timing are unrehearsed. On October 5 the organizer reported that children much enjoyed Bridge Courier in the app; that shows the object works on a screen, not that the paper packets do.
