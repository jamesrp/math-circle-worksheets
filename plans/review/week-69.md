# Week 69: Thin and fat road triangles

**Verdict: keep.** No must: the mathematics is real, every answer checks, and the pages meet the spec. Problem 3 is thin and repeats Problem 2's board, and the younger tables have no route; both are should items.

Reviewed October 10, 2026 by Claude, with the math check in [week-69-math.md](week-69-math.md). Packet: week-69-students.pdf (GGT69-S-v1, 4 pp., one shared Grades 4–5 packet, Problems 1–5). Adult guide: week-69-facilitator.pdf (GGT69-FAC-v1, 2 pp.). Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review; guide p. 1: "no physical rehearsal has been performed".

## The mathematics

A road triangle is three homes and one chosen shortest route per pair; a dot's gap is its distance, through any road, to the other two sides. On a tree the routes are forced and form a tripod, so every road of a side lies on a second side and every gap is 0 (P1, P5). On the grid, homes (0,0), (n,0), (n,n) with AC up the left and across the top give gap n at (0,n), so no bound holds for all grid triangles (P3, P4); the same homes also allow an all-zero triangle (P2). A 0-hyperbolic tree against a non-hyperbolic plane, reached with pencils: a mathematician would enjoy it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Thinness of chosen geodesic triangles, with honest limits on guide p. 1: gaps at dots, all roads usable, continuous edges, experiment apart from proof. |
| Problems | adequate | P1 searches two trees; P2 contrasts two choices on the same homes; P4–P5 are late general arguments. But every grid board has corner homes, so AB and BC are forced and one route answers all of P3, whose middle board is P2's again (fix 1). |
| Student pages | strong | Spec header and footer, no slop or hints, non-task worked visuals before first use (pp. 1, 2). Boards at 12.5–16 mm spacing, equal axes. Small faults: fixes 4–6. |
| Concreteness | adequate | Pencil work with home counters and three colours. A partner checks every route and tries to beat every claimed gap. Repeated tries share one copy of each board (fix 2). Guide p. 1 launch: trace P–Q, draw a second three-road route, add colours; the gap waits for p. 2. |
| Correctness | strong | No error (math.md: 385 tree triples, 6/70/924 AC routes, n to 12). One guide key spoils P3 (fix 1). |
| Adult guide | strong | Theorem-first overview with assumptions, limits and a readiness map; launch; first visit with a stopping point; keys, held hints and proofs for all five problems. |
| Age fit, K–1 | weak | No route, by design: "No K–1 route is implied" (source README). Fix 3. |
| Age fit, grades 2–3 | weak | No route, by design, though Week 67 gives third graders the same three-colour drawing. Fix 3. |
| Age fit, grades 4–5 | strong | About 85 words of rules, counting to 12, three routes held on the page. P1 starts at once; P4–P5 come late, with the organizer. Measuring gaps along coloured roads only is a prediction the guide's P3 hint covers. |

## Keep

- p. 1: the P–Q route; "Routes may overlap; draw the colors side by side when they do."; P1's two trees, homes left to the children, and "Can you make a road that belongs to exactly one of the three colored routes?"
- p. 2: "Use any road on the map, including uncolored roads." and "A dot already on another side has gap 0."; the dashed example; P2's two boards with the same homes.
- P3's "Your partner tries to find a shorter route from that dot to another side."; P4's partner-names-a-number; P5's "every choice of three homes".
- Guide: the overview, both tree proofs, the min(y, n − x) ≤ n bound, the coloured-outline hint, the stopping point.

## Fix

1. **should**, p. 3, P3, and guide p. 2, P2 key. P3's middle board is P2's 4×4 board with the same homes, and the P2 key ("take AC up the left and across the top… Its gap is 4") is its unique optimum (math.md finding 1). Prediction: P3 then falls to one route in a few minutes. Fix:
   - P2 key: AC up 2, right 4, up 2 (gap 2 at (0,2)); add "Save the left/top choice for Problem 3."
   - Replace P3's 4×4 board with homes A = (0,0), B = (4,2), C = (2,4). All three sides have choices (15, 6, 15 routes); the largest gap is 3, only at (0,3) or (3,0). Example: AB along the bottom then up, BC through (3,2) and (3,4), CA across the top and down; (0,3) has gap 3. Every dot is within 3 steps of a home and a dot's other two sides hold all three homes, so no gap exceeds 3: a child's proof. I checked all 1,350 triangles. Update the guide's P3 table; P2 still supplies the 4 for P4.
2. **should**, guide p. 1 materials; pp. 1 and 3. P1 says "Swap roles and try new homes" and P3 asks for a best by trial, but the pair has one copy of each tree and grid, in coloured pencil; "Try the mark-and-erase procedure" is unperformed. Prediction: a second triangle on a coloured tree is unreadable. Fix: two extra copies of pp. 1 and 3 per pair; draw in graphite, colour after the partner's check.
3. **should**, guide p. 1, "Readiness map": no route for the K–1 or 2–3 table. It is recorded design (plans/ggt-prototypes-66-75/README.md: "No K–1 edition is forced"), so a should, as on the Week 60 and 62 cards. Fix, one guide paragraph: 2–3 take P1–P2 with the adult reading, stopping where the first visit stops; K–1 put counters on the first tree, trace each pair's road with a finger, colour it and answer P1 aloud. Both are predictions.
4. **could**, p. 2: "either of the other two colored sides" → "the nearer of the other two colored sides".
5. **could**, P5: "a positive gap" → "a gap bigger than 0".
6. **could**, p. 2: cut the two ruled lines under P2; nothing is written there.
7. **could**, guide p. 1: mark the home counters A, B, C, as Week 67 does.
8. **could**, guide p. 2: cut "All student and guide pages were digitally inspected."

No disagreement with math.md; its guide finding joins a student-page repeat in fix 1.

## Overlaps

- Week 67, Meeting on shortest roads (Grades 3–5): the same homes, colours side by side, partner check, trees and grids; its tree meeting dot is P5's tripod centre. Week 67 asks where routes meet, Week 69 how far a side strays. Complementary, 67 first; no merge. Each guide should name the other.
- Week 50: every right/up staircase has the same length, which is why any monotone AC is shortest in P2–P3.

## App fit

Proposed: B, size M. Row: "69 | Thin and fat road triangles | Choose a shortest route for each pair of three homes on trees and grids; find the largest gap | Tree triangles have gap 0 (tripod); grid gaps grow without bound (corner triangle, gap n); homes alone don't fix the gap | No (shares Week 67's routes) | B | Draw three routes the app holds to shortest; tap a dot to flood its gap; reach a gap, claim Best, or Can't on trees | M".

The app refuses a route longer than shortest, which paper cannot enforce, and a tapped dot floods every road until it meets another side. Solves: an all-zero triangle; a gap of at least k; Best, checked against every triangle; "Make a gap of 1" on a tree, answered Can't. Certificates: the lit tripod, every road in two colours; for Best, k-step rings around the homes covering the map (true on the corner boards and fix 1's board; check each). Ladders (1×3, 1×5, 1×7) never beat 1 and a 12-road ring reaches 3 (my enumeration): natural contrasting maps.

Pitfalls: corner-home boards fall to one route; the flood must use uncoloured roads; no predict-the-gap, no "x of N". P4–P5 stay on paper. Share the route engine with Week 67 and the graph editor. Draw on P1, P2, a revised P3 and P5's Can't.

**Decision, October 10, 2026.** Not ported in the October 10, 2026 round: it needs Week 67's three-walker routes plus a gap flood. Add it as a group in Meeting roads once children have played that.

## Classroom evidence

None reported. Unpiloted prototype awaiting organizer review; themes.md lists only Weeks 1, 2 and 15 as taught, and the guide calls marking, erasing and partner checking unrehearsed.
