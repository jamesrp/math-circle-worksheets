# A six-year path for returning children

A proposal for the organizer, October 24, 2026. Unpiloted: only Weeks 1 and 2 have been taught. Week 15's record says piloted because it was tried at home; it has not been used in the circle.

The circle is one mixed room where every session offers one theme at three tables (K–1, 2–3, 4–5), and many children come back year after year. AGENTS.md asks for "a varied six-year progression at twenty sessions per year … about 120 sessions along a child's path." This page proposes one such path through the existing library: 120 sessions, starting with this year's Weeks 1–10. It is a planning draft, not a schedule and not a record of use. The private session use log ([private records](../LOCAL-RESOURCES.md#private-records)) stays the record of what was taught, and actual use should replace these plans as it arrives.

The data is in [catalog/path.toml](../catalog/path.toml). [catalog/check_path.py](../catalog/check_path.py) checks it, and `python3 catalog/build.py` runs that check on every build. The explorer's **Path** view shows the path as six year columns; choose a starting grade there to follow one child. The tables below are generated from the data with `python3 catalog/check_path.py --tables`.

## Assumptions

- **A session is one meeting of about an hour** for the whole room, with the same theme at all three tables. A return visit, the encore and an atlas family each count as a session of their own. Three heavy themes take two consecutive sessions: Week 52 (hinged frames), Week 56 (corners of a solid) and Week 61 (triangles on a ball). Their guides plan a first visit and a return visit or continuation on the same kit, so the second hour reuses the evening of preparation.
- **Twenty sessions a year:** this fall's Weeks 1–10, then ten more. The second half could run in spring and summer. Year 1 is 2026–27.
- **Every session serves the K–1 and 2–3 tables.** A theme with only Grades 4–5 pages cannot carry a session in a mixed room. A week without K–1 pages counts only when its guide gives an adult-led K–1 route, and every such session is marked in the tables. Return visits use their own K–1 entries; two use the base week's K–1 packet, as the [return-visit index](../lowell-math-circle-year-2/BONUS-AND-RETURN-VISITS.md) suggests for weeks whose bonus choices start at Grade 2.
- **Who sees what.** A child who starts in kindergarten spends two years at each table and meets all 120 sessions. A child who starts in grade 2 meets 80 (Years 1–4), and one who starts in grade 4 meets 40 (Years 1–2). A child who joins later enters mid-path. Some return visits then come before the child has met the first visit. Our inference, not a tested claim: adults can open with the base week's concrete pages, as the return-visit index does for missing K–1 entries.
- **Pacing.** *Math Circle by the Bay* (printed p. x, via the [teaching-format notes](lesson-format-source-notes.md)) reports using the same material with both age groups at a different pace and depth. It also warns that classes differ too much to prescribe how long a topic takes. The slot counts here are planning estimates: a theme that runs long can take the next slot, and the following entries slide.

## How to read the tables

`#` is the session within the year. `Y2·3` means Year 2, session 3. **↩** lists the earlier sessions an entry returns to, all at least a year earlier. Week links go to the week's source README, the page the [year-2 print index](../lowell-math-circle-year-2/README.md) links each theme to, which lists its PDFs. Return-visit links open the student PDF, and atlas links open the combined student book at the given pages. *Area* is the area of the theme's central concept. *Main move* is the reasoning move children use most. *Kit* is light (under about 15 minutes to prepare), medium (a print-and-cut kit, about 15–45 minutes) or **heavy** (an evening or a build).

### Year 1, 2026–27

Fall Weeks 1–10 as planned (Weeks 1 and 2 taught in September; the others printed, not yet reported), then a light spring–summer half that adds chance, counting and symmetry. A kindergartner is at the K–1 table; every theme here is new to everyone.

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 1: Tiling lab](../lowell-math-circle-year-2/source/week-01/README.md) | Shape | colouring argument | Taught. First tiling obstructions; returns as the encore and its return visit. | light |
| 2 | [Week 2: Lamp lab](../lowell-math-circle-year-2/source/week-02/README.md) | Symmetry | invariant | Taught. Toggles and parity; returns as its return visit and Lamplighter streets. | medium |
| 3 | [Week 3: Shuffle machines](../lowell-math-circle-year-2/source/week-03/README.md) | Symmetry | construct | First permutations; prepares fair shuffles and derangements. | light |
| 4 | [Week 4: Stars and wheels](../lowell-math-circle-year-2/source/week-04/README.md) | Number | every case | First gcd and primes; returns as necklaces, Euclid squares and prime bags. | medium |
| 5 | [Week 5: Tower cities](../lowell-math-circle-year-2/source/week-05/README.md) | Logic | look at extremes | First deduction from clues; returns as shadows and public knowledge. | **heavy** |
| 6 | [Week 6: Code breaking](../lowell-math-circle-year-2/source/week-06/README.md) | Logic | pigeonhole | First information counting; returns as hidden changes and weighing. | medium |
| 7 | [Week 7: Take-away games](../lowell-math-circle-year-2/source/week-07/README.md) | Games | work backward | First winning and losing positions; prepares Nim, Hackenbush and Buckets of Fish. | light |
| 8 | [Week 8: Rook race and Nim](../lowell-math-circle-year-2/source/week-08/README.md) | Games | copy the opponent | Copying strategies and binary Nim; returns in Year 3 and as Hackenbush. | light |
| 9 | [Week 9: Bouncing paths](../lowell-math-circle-year-2/source/week-09/README.md) | Shape | unfold | First unfolding; prepares shortest routes and torus portals. | light |
| 10 | [Week 10: Bridges](../lowell-math-circle-year-2/source/week-10/README.md) | Networks | pair up | Euler's parity rule; returns as one-way streets and road detours. | light |
| 11 | [Week 42: Fair results from a bag](../lowell-math-circle-year-2/source/week-42/README.md) | Chance and infinity | pair up | First chance session: equally likely outcomes, which every later chance theme needs. | light |
| 12 | [Week 15: Nearest-site regions](../lowell-math-circle-year-2/source/week-15/README.md) | Shape | construct | Tried at home, not yet in the circle. Prepares shortest routes and three-armed tie lines. | light |
| 13 | [Atlas AD-21: Make a catalog that remembers every choice](../lowell-math-circle-year-2/combined/atlas-algebra-discrete-student-worksheets.pdf), pp. 66–68 | Counting | every case | Multiplying choices, which the subset and derangement themes need. | light |
| 14 | [Week 13: Route packing and bottlenecks](../lowell-math-circle-year-2/source/week-13/README.md) | Networks | example plus proof | Max-flow min-cut with two certificates; contrasts with cheapest networks in Year 3. | light |
| 15 | [Week 30: Two-pan weight kits](../lowell-math-circle-year-2/source/week-30/README.md) | Number | example plus proof | Balanced ternary; contrasts with two-length builders in Year 4. | light |
| 16 | [Week 24: Three random decks](../lowell-math-circle-year-2/source/week-24/README.md) | Chance and infinity | construct | Nontransitive decks; contrasts with take-or-pass and voting. | medium |
| 17 | [Week 36: Making threes](../lowell-math-circle-year-2/source/week-36/README.md) | Counting | pigeonhole | A nine-point world; contrasts with subset cards and scheduling in Year 2. | medium |
| 18 | [Week 34: Hidden turns](../lowell-math-circle-year-2/source/week-34/README.md) | Symmetry | example plus proof | First symmetry counting; prepares necklaces, frieze borders and mirror twins. | light |
| 19 | [Week 17: Machine memory](../lowell-math-circle-year-2/source/week-17/README.md) | Logic | pigeonhole | Fewest-state machines; returns in Year 3 and as substitution strips. | medium |
| 20 | [Week 16: Three-color triangles](../lowell-math-circle-year-2/source/week-16/README.md) | Shape | count two ways | Sperner's lemma by pairing doors; returns in Year 3. | medium |

### Year 2, 2027–28

First returns: the encore and six return visits to Year 1 themes, with new themes that lean on Year 1 (necklaces after Week 4, codes after Week 6, Pólya's urn after Week 42). A child who started in K is in grade 1, still at the K–1 table, so these returns are new problems at the same level.

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 11: Chip-firing with a sink](../lowell-math-circle-year-2/source/week-11/README.md) | Networks | monovariant | Chip-firing; returns in Year 4 and as rotor-routers in Year 5. | light |
| 2 | [Week 45: The visible side](../lowell-math-circle-year-2/source/week-45/README.md) | Chance and infinity | every case | Conditional probability, which the urn and inference themes need. | light |
| 3 | [Week 3 return visit: Shuffle machines](../lowell-math-circle-year-2/week-03/week-03-return-visit.pdf) | Symmetry | example plus proof | ↩ Y1·3. Shortest adjacent sorting and reachability: new questions on the same machines. | light |
| 4 | [Week 33: Prime-length necklaces](../lowell-math-circle-year-2/source/week-33/README.md) | Number | up to symmetry | ↩ Y1·4. Week 4's prime rings return as Fermat's necklace count. | light |
| 5 | [Week 62: Conflict networks and scheduling](../lowell-math-circle-year-2/source/week-62/README.md) | Networks | greedy | Names graph colouring, which Week 1 met in tiles; prepares the encore and pursuit. | medium; K–1 by adult-led route |
| 6 | [Week 18: Hidden changes](../lowell-math-circle-year-2/source/week-18/README.md) | Logic | count two ways | ↩ Y1·6. Week 6's question counting becomes error-correcting codes. | medium |
| 7 | [Week 7 return visit: Take-away games](../lowell-math-circle-year-2/week-07/week-07-return-visit.pdf) | Games | work backward | ↩ Y1·7. A shared pass, no repeated move, adjacent pairs: changed rules, new positions. | light |
| 8 | [Week 19: No card inside another](../lowell-math-circle-year-2/source/week-19/README.md) | Counting | example plus proof | Antichains of subsets; prepares derangements and sliding arrays. | medium |
| 9 | [Week 21: The shortest route that touches a line](../lowell-math-circle-year-2/source/week-21/README.md) | Shape | unfold | ↩ Y1·9. Week 9's unfolding proves a route shortest, with Week 15's reflection. | light |
| 10 | [Week 10 return visit: Bridges](../lowell-math-circle-year-2/week-10/week-10-return-visit.pdf) | Networks | pair up | ↩ Y1·10. One-way streets, safe local choices, password windows. | light |
| 11 | [Week 44: The bag that copies](../lowell-math-circle-year-2/source/week-44/README.md) | Chance and infinity | invariant | ↩ Y1·11. Pólya's urn after Week 42's fair coin and Week 45's clues. | light |
| 12 | [Week 1e: Pattern blocks II](../lowell-math-circle-year-2/source/week-01-encore/README.md) | Games | copy the opponent | ↩ Y1·1. The encore: a copying-strategy game and cube stacks on Week 1's blocks. | light |
| 13 | [Week 40: Loop colors](../lowell-math-circle-year-2/source/week-40/README.md) | Shape | invariant | Knot three-colouring; returns as the atlas knot family in Year 5. | medium |
| 14 | [Week 89: Growing shapes and totals](../lowell-math-circle-year-2/source/week-89/README.md) | Number | count two ways | Differences and sums of growing shapes; the same object as Week 50's staircases in Year 3. | medium |
| 15 | [Week 15 return visit: Nearest-site regions](../lowell-math-circle-year-2/week-15/week-15-return-visit.pdf) | Shape | construct | ↩ Y1·12. Farthest-site cells, taxi distance, largest clearance. | light |
| 16 | [Week 5 return visit: Tower cities](../lowell-math-circle-year-2/week-05/week-05-return-visit.pdf) | Logic | construct | ↩ Y1·5. Latin trades, diagonal conditions, climbing routes. | medium |
| 17 | [Week 14: Polygon triangulations and flips](../lowell-math-circle-year-2/source/week-14/README.md) | Counting | smaller cases | Triangulations and flips; Catalan numbers return in Year 3. | light |
| 18 | [Week 2 return visit: Lamp lab](../lowell-math-circle-year-2/week-02/week-02-return-visit.pdf) | Symmetry | invariant | ↩ Y1·2. Hidden wiring, ring switches, moving ON states. | medium |
| 19 | [Week 20: Averaging](../lowell-math-circle-year-2/source/week-20/README.md) | Chance and infinity | look at extremes | The maximum principle; contrasts with gentle-step landscapes in Year 4. | light |
| 20 | [Week 38: Seams](../lowell-math-circle-year-2/source/week-38/README.md) | Shape | unfold | Möbius bands; returns as the atlas cut-prediction family in Year 4. | medium |

### Year 3, 2028–29

The K starter moves to the 2–3 table. Deeper returns to Year 1 (shuffles asked fairly, Euclid's algorithm as a third view of gcd) and the first two-hour theme.

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 41: Portals](../lowell-math-circle-year-2/source/week-41/README.md) | Shape | unfold | ↩ Y1·9. Week 9's mirror rooms become a torus; returns in Year 5 and as strange surfaces. | medium |
| 2 | [Week 25: Row and column shadows](../lowell-math-circle-year-2/source/week-25/README.md) | Logic | example plus proof | ↩ Y1·5. Week 5's clue logic as row and column counts. | light |
| 3 | [Week 43: Shuffling picture cards](../lowell-math-circle-year-2/source/week-43/README.md) | Chance and infinity | pair up | ↩ Y1·3. Week 3's shuffles asked fairly; prepares derangements. | medium |
| 4 | [Week 4 return visit: Stars and wheels](../lowell-math-circle-year-2/week-04/week-04-return-visit.pdf) | Number | every case | ↩ Y1·4, Y2·4. Two moving counters, two-hop routes, coloured necklaces classified. | light |
| 5 | [Week 53: Cheapest connected networks](../lowell-math-circle-year-2/source/week-53/README.md) | Networks | greedy | ↩ Y1·14. Cheapest networks against Week 13's route packing; prepares moving piles. | light |
| 6 | [Week 6 return visit: Code breaking](../lowell-math-circle-year-2/week-06/week-06-return-visit.pdf) | Logic | example plus proof | ↩ Y1·6, Y2·6. Weighing with three outcomes, unequal question costs, joined messages. | light |
| 7 | [Week 58: Fair division](../lowell-math-circle-year-2/source/week-58/README.md) | Games | construct | Fair division; contrasts with stable pairings and voting. | medium |
| 8 | [Week 26: Same area, different boundaries](../lowell-math-circle-year-2/source/week-26/README.md) | Counting | look at extremes | Perimeter at fixed area; returns as its return visit in Year 6. | light |
| 9 | [Week 9 return visit: Bouncing paths](../lowell-math-circle-year-2/week-09/week-09-return-visit.pdf) | Shape | unfold | ↩ Y1·9, Y2·9. Prescribed wall orders, periodic returns, self-crossings. | light; K–1 uses the Week 9 K–1 packet |
| 10 | [Week 32: Squares inside rectangles](../lowell-math-circle-year-2/source/week-32/README.md) | Number | monovariant | ↩ Y1·4. Euclid's algorithm by cutting squares: gcd a third way. | light |
| 11 | [Week 46: Two boards forget their starts](../lowell-math-circle-year-2/source/week-46/README.md) | Chance and infinity | invariant | ↩ Y2·11. Coupling: two random boards forget their starts. | light |
| 12–13 | [Week 52: Hinged frames and braces](../lowell-math-circle-year-2/source/week-52/README.md) | Networks | construct | Rigidity. Hour one can end after the concrete Problems 1–7, as the guide suggests; hour two follows its return-visit section (repair, or fewest and universal braces). | **heavy**, two hours |
| 14 | [Week 35: Footprint borders](../lowell-math-circle-year-2/source/week-35/README.md) | Symmetry | every case | ↩ Y1·18. Frieze symmetries after Week 34's turns and flips. | medium |
| 15 | [Week 16 return visit: Three-color triangles](../lowell-math-circle-year-2/week-16/week-16-return-visit.pdf) | Shape | pair up | ↩ Y1·20. A fourth label, boundary parity, signed rainbow triangles. | light |
| 16 | [Week 60: Take it or pass](../lowell-math-circle-year-2/source/week-60/README.md) | Chance and infinity | work backward | ↩ Y1·16. Optimal stopping by working backward, as in Week 7. | medium |
| 17 | [Week 17 return visit: Machine memory](../lowell-math-circle-year-2/week-17/week-17-return-visit.pdf) | Logic | pigeonhole | ↩ Y1·19. Detect RR anywhere, combine two memories, why equal counts need unbounded memory. | medium |
| 18 | [Week 12: Catalan bijections](../lowell-math-circle-year-2/source/week-12/README.md) | Counting | smaller cases | ↩ Y2·17. Catalan numbers again, now as pairings, mountain paths and trees. | light |
| 19 | [Week 8 return visit: Rook race and Nim](../lowell-math-circle-year-2/week-08/week-08-return-visit.pdf) | Games | copy the opponent | ↩ Y1·8. Misère Nim, coins that cannot jump, two races as one game. | light |
| 20 | [Week 50: Staircases and lengths](../lowell-math-circle-year-2/source/week-50/README.md) | Shape | follow it forever | ↩ Y2·14. The staircase paradox; same-theorem link to Week 89's sums, and prepares sums and medians. | light |

### Year 4, 2029–30

Third meetings with Year 1 ideas: derangements after shuffles, Hackenbush after take-away and Nim, prime bags after gcd, the pattern-block return visit after the tiles and the encore. Euler's formula prepares the curvature themes.

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 1 return visit: Tiling lab](../lowell-math-circle-year-2/week-01/week-01-return-visit.pdf) | Shape | look at extremes | ↩ Y1·1, Y2·12. Boundary length, corners around a point, rotational symmetry: the third pattern-block visit. | light |
| 2 | [Week 39: Road detours](../lowell-math-circle-year-2/source/week-39/README.md) | Symmetry | monovariant | ↩ Y1·10. Walks on Week 10's networks reduced to free-group words. | light |
| 3 | [Week 63: Cards away from home](../lowell-math-circle-year-2/source/week-63/README.md) | Counting | smaller cases | ↩ Y1·3, Y3·3, Y2·8. Derangements: the third meeting with Week 3's arrangements. | medium |
| 4 | [Week 29: Two-length builders](../lowell-math-circle-year-2/source/week-29/README.md) | Number | example plus proof | ↩ Y1·15. The last gap ab − a − b; contrasts with Week 30's weights. | medium |
| 5 | [Week 27: Stable pairings](../lowell-math-circle-year-2/source/week-27/README.md) | Networks | monovariant | Stable pairings; contrasts with Year 3's fair division. | medium |
| 6 | [Week 83: Hackenbush balances](../lowell-math-circle-year-2/source/week-83/README.md) | Games | construct | ↩ Y1·7, Y1·8. Take-away and Nim positions get values: partizan games. | light; K–1 by adult-led route |
| 7 | [Week 42 return visit: Fair results from a bag](../lowell-math-circle-year-2/week-42/week-42-bonus.pdf) | Chance and infinity | pair up | ↩ Y1·11. Three-way fair outputs, recycling skipped pairs, fair positions. | light |
| 8 | [Atlas GA-32: Predict the cut before using scissors](../lowell-math-circle-year-2/combined/atlas-geometry-analysis-student-worksheets.pdf), pp. 89–91 | Shape | unfold | ↩ Y2·20. Predict the cut before using scissors: Week 38's bands with seam journeys. | medium |
| 9 | [Week 18 return visit: Hidden changes](../lowell-math-circle-year-2/week-18/week-18-bonus.pdf) | Logic | count two ways | ↩ Y2·6. Recover a known hole, check counters, locate a change. | medium |
| 10 | [Week 96: Prime bags](../lowell-math-circle-year-2/source/week-96/README.md) | Number | construct | ↩ Y3·10, Y1·13. Prime factorization as bags of prime tokens; prepares square remainders. | light; K–1 by adult-led route |
| 11–12 | [Week 56: Corners of a solid](../lowell-math-circle-year-2/source/week-56/README.md) | Networks | invariant | Euler's formula and angular defect; hour two takes the guide's later-visit problems on the same solids. Prepares the curvature themes. | **heavy**, two hours |
| 13 | [Week 21 return visit: The shortest route that touches a line](../lowell-math-circle-year-2/week-21/week-21-bonus.pdf) | Shape | unfold | ↩ Y2·9. Two walls in order, routes inside windows, routes around a rectangle. | light |
| 14 | [Week 11 return visit: Chip-firing with a sink](../lowell-math-circle-year-2/week-11/week-11-return-visit.pdf) | Networks | monovariant | ↩ Y2·1. Sink-free stabilization, avalanche lengths, every legal history. | light |
| 15 | [Week 37: Mirror twins](../lowell-math-circle-year-2/source/week-37/README.md) | Symmetry | up to symmetry | ↩ Y1·18. Chirality: mirror twins that no turn can match. | **heavy** |
| 16 | [Week 95: Count the unseen](../lowell-math-circle-year-2/source/week-95/README.md) | Chance and infinity | simulate | ↩ Y2·2. Capture–recapture: inference after Week 45's clues. | medium; K–1 by adult-led route |
| 17 | [Week 84: Public knowledge](../lowell-math-circle-year-2/source/week-84/README.md) | Logic | smaller cases | ↩ Y1·5. Common knowledge, Week 5's deduction about other minds. | medium; K–1 by adult-led route |
| 18 | [Week 36 return visit: Making threes](../lowell-math-circle-year-2/week-36/week-36-bonus.pdf) | Counting | pigeonhole | ↩ Y1·17. Avoid-a-three game, two or three ownership colours, nine safe tiles. | light; K–1 uses the Week 36 K–1 packet |
| 19 | [Week 54: Partitions and rebuilding](../lowell-math-circle-year-2/source/week-54/README.md) | Counting | pair up | Odd parts and distinct parts; prepares sliding number arrays. | light; K–1 by adult-led route |
| 20 | [Week 47: Gentle-step landscapes](../lowell-math-circle-year-2/source/week-47/README.md) | Shape | look at extremes | ↩ Y2·19. Lowest and highest landscapes; contrasts with Week 20's averaging. | light |

### Year 5, 2030–31

The K starter reaches the 4–5 table: the lamplighter group on Week 2's lamps, curvature on a ball after Week 56's corners, ordinals, Burnside counting after Fermat's necklaces. Half the K–1 sessions now rely on untried adult-led routes (see the gaps).

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 66: Lamplighter streets](../lowell-math-circle-year-2/source/week-66/README.md) | Symmetry | example plus proof | ↩ Y1·2. Week 2's lamps on a walking street: the lamplighter group. | light; K–1 by adult-led route |
| 2 | [Atlas GA-26: Can colors detect a knot?](../lowell-math-circle-year-2/combined/atlas-random-ten-student-worksheets.pdf), pp. 2–5 | Shape | invariant | ↩ Y2·13. Can colours detect a knot? Week 40's colourings with changed crossings. | medium |
| 3 | [Week 99: Moving piles](../lowell-math-circle-year-2/source/week-99/README.md) | Games | greedy | ↩ Y3·5. Optimal transport after route packing and cheapest networks. | light; K–1 by adult-led route |
| 4 | [Week 82: Endless class lines](../lowell-math-circle-year-2/source/week-82/README.md) | Chance and infinity | pair up | Ordinal addition; prepares Buckets of Fish. | medium; K–1 by adult-led route |
| 5 | [Week 30 return visit: Two-pan weight kits](../lowell-math-circle-year-2/week-30/week-30-bonus.pdf) | Number | example plus proof | ↩ Y1·15. Kits that survive a loss, hidden masses, equal teams. | light |
| 6 | [Week 57: Area from dots](../lowell-math-circle-year-2/source/week-57/README.md) | Shape | invariant | Pick's theorem: area read from dot counts; area returns as angle excess in Week 61 and as Heron's rectangles in Week 93. | medium; K–1 by adult-led route |
| 7 | [Week 67: Meeting on shortest roads](../lowell-math-circle-year-2/source/week-67/README.md) | Networks | coordinates | Medians on shortest roads; contrasts with Week 68's ways out in Year 6. | light; K–1 by adult-led route |
| 8 | [Week 26 return visit: Same area, different boundaries](../lowell-math-circle-year-2/week-26/week-26-bonus.pdf) | Counting | count two ways | ↩ Y3·8. Shared fences, corners that remember holes, exposed cube faces. | light |
| 9 | [Week 87: Voting and agendas](../lowell-math-circle-year-2/source/week-87/README.md) | Games | construct | ↩ Y1·16, Y3·7. Condorcet cycles: Week 24's nontransitive decks as voters. | medium; K–1 by adult-led route |
| 10 | [Week 45 return visit: The visible side](../lowell-math-circle-year-2/week-45/week-45-bonus.pdf) | Chance and infinity | every case | ↩ Y2·2. Repeated clues, informed and blind hosts, noisy reports. | light |
| 11–12 | [Week 61: Triangles on a ball](../lowell-math-circle-year-2/source/week-61/README.md) | Shape | count two ways | ↩ Y4·11. Girard's theorem, curvature after Week 56's corners; hour two uses the guide's continuations on the same balls. | **heavy**, two hours; K–1 by adult-led route |
| 13 | [Week 86: Pursuit and escape](../lowell-math-circle-year-2/source/week-86/README.md) | Networks | copy the opponent | ↩ Y2·5. Cops and robbers on graphs; contrasts with Week 62's colouring. | light; K–1 by adult-led route |
| 14 | [Week 90: Sliding number arrays](../lowell-math-circle-year-2/source/week-90/README.md) | Counting | invariant | Jeu de taquin, after subset antichains and partitions. | medium; K–1 by adult-led route |
| 15 | [Week 97: Square remainders](../lowell-math-circle-year-2/source/week-97/README.md) | Number | pair up | ↩ Y1·4. Square remainders, after Week 4's remainders and Week 96's primes. | light; K–1 by adult-led route |
| 16 | [Week 91: Rotor-router machines](../lowell-math-circle-year-2/source/week-91/README.md) | Networks | pair up | ↩ Y2·1. Rotor-routers, Week 11's chips made deterministic. | medium; K–1 by adult-led route |
| 17 | [Atlas AD-24: Count necklaces when every bead count is fixed](../lowell-math-circle-year-2/combined/atlas-algebra-discrete-student-worksheets.pdf), pp. 75–77 | Symmetry | up to symmetry | ↩ Y2·4. Burnside counting where Week 33's prime trick fails. | light |
| 18 | [Week 23: Sorting machines](../lowell-math-circle-year-2/source/week-23/README.md) | Logic | counterexample | Sorting networks and the 0–1 principle. | medium |
| 19 | [Week 32 return visit: Squares inside rectangles](../lowell-math-circle-year-2/week-32/week-32-bonus.pdf) | Number | greedy | ↩ Y3·10. Biggest versus fewest squares, allowed sizes, size-free recipes. | light |
| 20 | [Week 41 return visit: Portals](../lowell-math-circle-year-2/week-41/week-41-bonus.pdf) | Shape | unfold | ↩ Y3·1. Round-end orbits, nine-cell tours, shortest routes through blocks. | medium |

### Year 6, 2031–32

The 4–5 culmination: games that end without a bound, glued surfaces, percolation, ultrametric distance, with atlas families as fresh representations of earlier themes.

| # | Theme | Area | Main move | Returns to · what it revisits or prepares | Kit |
|---|---|---|---|---|---|
| 1 | [Week 65: Hyperbolic octagon streets](../lowell-math-circle-year-2/source/week-65/README.md) | Shape | counterexample | Hyperbolic streets: tilings and curvature at their far edge. | light; K–1 by adult-led route |
| 2 | [Week 80: Midnight laboratory](../lowell-math-circle-year-2/source/week-80/README.md) | Chance and infinity | follow it forever | The Thomson lamp: a process that never settles. | medium; K–1 by adult-led route |
| 3 | [Atlas AP-28: Four messages through a damaged strip](../lowell-math-circle-year-2/combined/atlas-probability-applications-student-worksheets.pdf), pp. 70–72 | Logic | pigeonhole | ↩ Y2·6, Y1·6. Four messages through a damaged strip: Week 18's bound and its limits. | light |
| 4 | [Week 55: Few sums and equal spacing](../lowell-math-circle-year-2/source/week-55/README.md) | Number | look at extremes | Fewest and most sums; equal spacing is the extreme case. | medium; K–1 by adult-led route |
| 5 | [Week 68: How many ways out](../lowell-math-circle-year-2/source/week-68/README.md) | Networks | follow it forever | Ends of infinite graphs, after meeting on shortest roads. | light; K–1 by adult-led route |
| 6 | [Week 100: Distance in nested worlds](../lowell-math-circle-year-2/source/week-100/README.md) | Shape | construct | Ultrametric distance in nested worlds. | medium; K–1 by adult-led route |
| 7 | [Week 12 return visit: Catalan bijections](../lowell-math-circle-year-2/week-12/week-12-return-visit.pdf) | Counting | smaller cases | ↩ Y3·18. Colour-restricted pairings, height limits, path surgery. | light |
| 8 | [Week 81: Buckets of Fish](../lowell-math-circle-year-2/source/week-81/README.md) | Chance and infinity | monovariant | ↩ Y5·4, Y1·7, Y1·8. Buckets of Fish: a take-away game that ends but has no bound. | medium; K–1 by adult-led route |
| 9 | [Week 64: Straight paths on strange surfaces](../lowell-math-circle-year-2/source/week-64/README.md) | Shape | unfold | ↩ Y3·1. Straight paths on glued surfaces: Week 41's torus generalized. | light; K–1 by adult-led route |
| 10 | [Week 35 return visit: Footprint borders](../lowell-math-circle-year-2/week-35/week-35-bonus.pdf) | Symmetry | construct | ↩ Y3·14. Layered slides, fewest recolourings, closing a necklace. | medium |
| 11 | [Atlas AP-23: Everyone chooses a faster road](../lowell-math-circle-year-2/combined/atlas-random-ten-student-worksheets.pdf), pp. 17–19 | Games | counterexample | ↩ Y4·5. Everyone chooses a faster road: stable need not be best, as in Week 27. | light |
| 12 | [Week 88: Packing and kissing circles](../lowell-math-circle-year-2/source/week-88/README.md) | Shape | example plus proof | Packing and kissing circles. | medium |
| 13 | [Week 98: Growing from a few seeds](../lowell-math-circle-year-2/source/week-98/README.md) | Chance and infinity | monovariant | Bootstrap percolation: a perimeter that never grows. | light; K–1 by adult-led route |
| 14 | [Week 76: Substitution strips](../lowell-math-circle-year-2/source/week-76/README.md) | Counting | work backward | ↩ Y1·19. Thue–Morse strips; same-theorem link to Week 17's machines. | medium; K–1 by adult-led route |
| 15 | [Week 25 return visit: Row and column shadows](../lowell-math-circle-year-2/week-25/week-25-bonus.pdf) | Logic | example plus proof | ↩ Y3·2. An extra shadow, adaptive questions, counts that cannot fit. | light |
| 16 | [Week 28: Flat folds](../lowell-math-circle-year-2/source/week-28/README.md) | Shape | invariant | Flat folding: Maekawa and Kawasaki at a single vertex. | **heavy** |
| 17 | [Week 13 return visit: Route packing and bottlenecks](../lowell-math-circle-year-2/week-13/week-13-return-visit.pdf) | Networks | example plus proof | ↩ Y1·14. Sharing dots or arrows, prescribed pairs, road capacities. | light |
| 18 | [Week 37 return visit: Mirror twins](../lowell-math-circle-year-2/week-37/week-37-bonus.pdf) | Symmetry | up to symmetry | ↩ Y4·15. Flat tiles and a lifted flip, two-colour edges, corner identities. | medium |
| 19 | [Atlas AD-01: Build a world that defeats a rule](../lowell-math-circle-year-2/combined/atlas-algebra-discrete-student-worksheets.pdf), pp. 4–6 | Logic | counterexample | ↩ Y1·5. Build a world that defeats a rule: a counterexample as proof. | light |
| 20 | [Week 93: Squaring a rectangle](../lowell-math-circle-year-2/source/week-93/README.md) | Shape | follow it forever | Heron's averaging: each same-area rectangle is more square than the last, trapping the square root in shrinking brackets; the path's last limit, after Weeks 50 and 80. | light; K–1 by adult-led route |

## What the check enforces

`check_path.py` fails the build on:

- an unknown id;
- a concept used or taught before a concept it requires (concepts that require nothing count as everyday background; one waiver is written out, below);
- the same theme twice in a year;
- more than two sessions in a row from one area;
- a year with fewer than five areas;
- a revisit closer than one year (twenty sessions), or a declared revisit with no catalog link behind it;
- three heavy kits in a row;
- a session with no K–1 or 2–3 entry.

It prints areas, kits and revisits per year. Current result: all checks pass.

- Every year has all eight areas.
- Kits per year: at most two heavy, and never two heavy in a row except a two-hour theme's own pair of meetings.
- 80 revisit links, all at least a year apart.
- All 34 themes first met in Years 1–2 come back one to three years later.

Every weekly theme on the path, and every return visit's base week, has a keep card (79 entries) or a revise card whose musts are fixed (31 entries).

The one waiver: Week 1 two-colours a grid with blocks before Week 62 names graph colouring (Y2·5). Week 1 is taught and stays first.

Of the 120 sessions:

- 85 come from 82 weekly themes, three of them two-hour themes;
- 28 are return visits;
- 7 are atlas families.

## What a returning child meets

**Starting in kindergarten (all 120 sessions; 68 of them return to something the child met in an earlier year).**

- **Years 1–2 at the K–1 table.** Tiles, lamps, shuffle machines, towers, take-away games and bridges, then a light spring of bags, regions, choices and threes. In grade 1 the same child meets the first returns at the same table: the shuffle machines again with a sorting question (Y2·3), take-away with a shared pass (Y2·7), and the encore's copying game on the pattern blocks (Y2·12). Only one of these forty sessions, Week 62, relies on an adult-led K–1 route.
- **Years 3–4 at the 2–3 table, third meetings.** The child asks whether a shuffle is fair (Y3·3), then counts arrangements where no card is home (Y4·3). Take-away and Nim positions get values in Hackenbush (Y4·6). The pattern-block return visit (Y4·1) asks about boundaries and corners after the tiles and the encore.
- **Years 5–6 at the 4–5 table.** Week 2's lamps return on a walking street as the lamplighter group (Y5·1). Week 56's corners lead to triangles on a ball (Y5·11–12). The game strand ends with ordinals (Y5·4) and Buckets of Fish (Y6·8), a game that always ends but can be made as long as you like.

**Starting in grade 2 (80 sessions: 40 at the 2–3 table, 40 at 4–5; 43 return to an earlier theme).**

- **The gcd strand:** Week 4's stars at 2–3 (Y1·4); Fermat's prime necklaces in grade 3 (Y2·4); then, in grade 4 at the 4–5 table, the Week 4 return visit (Y3·4) and Euclid's algorithm by cutting squares (Y3·10); prime bags in grade 5 (Y4·10).
- **The chance strand, complete:** fair results from a bag (Y1·11), clues (Y2·2), Pólya's urn (Y2·11), coupling (Y3·11), and the bag's return visit (Y4·7).
- **What this child misses:** they leave before Years 5–6, so they miss the curvature on a ball that follows Week 56, the lamplighter streets and the infinite games.

**Starting in grade 4 (40 sessions, all at the 4–5 table; 11 return to an earlier theme).**

- **Year 1:** the fall themes at their deepest printed level.
- **Year 2, the first returns:**
  - One machine run twice, the 4–5 investigation in the shuffle return visit (Y2·3);
  - Fermat's necklaces (Y2·4);
  - error-correcting codes after Week 6 (Y2·6);
  - a shortest-route proof by unfolding after Weeks 9 and 15 (Y2·9);
  - password windows in the bridges return visit (Y2·10);
  - Pólya's urn (Y2·11);
  - the encore (Y2·12).
- **Natural extras:** this child leaves before most of Weeks 52–100. The Grades 4–5-only themes left off the path (69–78, below) suit their table as continuations.

### Three revisit chains worth noticing

- **From take-away to games with no bound:** Weeks 7 and 8 (Y1) → their return visits (Y2·7, Y3·19) → Hackenbush (Y4·6) → ordinals (Y5·4) → Buckets of Fish (Y6·8).
- **From shuffles to derangements:** Week 3 (Y1·3) → its return visit (Y2·3) → fair shuffles (Y3·3) → cards away from home (Y4·3). The object, arrangements, stays the same while the question moves from return times to sorting, fairness and inclusion–exclusion.
- **From stars to Burnside:** Week 4 (Y1·4) → prime necklaces (Y2·4) → the return visit (Y3·4) → squares inside rectangles (Y3·10) → prime bags (Y4·10) → square remainders (Y5·15) and fixed-bead necklaces (atlas AD-24, Y5·17).

Two shorter chains:

- unfolding: Week 9 → Week 21 → portals (Y3·1) → strange surfaces (Y6·9);
- polyhedra: Week 56 → Week 61 → hyperbolic streets (Y6·1).

## Gaps: proposals for future writing

These are proposals, not activities. Nothing below has been written.

1. **K–1 pages for Years 4–6.** Weeks 52–100 fill 35 path entries, but only 8 of them have K–1 pages. The K–1 table depends on untried adult-led routes from guides in 5 sessions of Year 4, 11 of Year 5 and 10 of Year 6. A child who starts in kindergarten is at the 4–5 table by then. Younger siblings and new kindergartners joining in those years are not. Writing tested K–1 pages for the strongest of these would make the later years sound for a mixed room, starting with 66, 57, 87, 91, 97, 81 and 98. [K–1 page drafts](k1-drafts/README.md) for those seven (October 25) await the organizer's review; none is piloted.
2. **Return visits for Weeks 52–100.** Return visits exist only for Weeks 1–51, so themes first met in Years 3–6 come back only through related themes or not at all. The best candidates are themes from Years 2–4 that later themes build on: 62 (colouring), 53 (cheapest networks), 58 (fair division), 63 (derangements) and 56 (Euler's formula).
   [Return-visit drafts](return-visit-drafts/README.md) for 53, 58, 62 and 63 (October 25) await the organizer's review; none is on the path yet.
3. **Games, logic, networks and counting are used up.** The path uses all 7 games themes, all 7 logic themes, all 12 networks themes and all 9 counting themes. Only shape (12 left out) and chance (4 left out) have reserves, which is why Year 6 has six shape sessions. A second cycle, or any swap in those four areas, needs new themes. Games for the younger tables matter most: only 4 of the 7 games themes have K–1 pages.
   [Topic scouting](topic-scouting/README.md) (October 24) proposes twelve outlines for these areas, five of them games and all with K–1 entries; student-page drafts of all twelve [await the organizer's review](topic-scouting/drafts/README.md), and none is on the path yet.
4. **Classroom evidence.** The order rests on prerequisites and catalog links, not on observed children. After each term, compare the use log with the path and move what children wanted to continue.

## Left out, by group

Leaving a theme out of this path says nothing against it; each line says why it is not load-bearing here.

| Group | Themes | Why |
|---|---|---|
| Grades 4–5 pages with no route for the younger tables | 70, 71, 72, 73, 75, 77 | A session must serve all three tables. Offer one as the 4–5 table's continuation beside its parent theme: 70 and 75 with 41, 71 with 9's return visit, 72 with 57, 73 with 47, 77 with 2's return visit. |
| Grades 4–5 pages with only an adult-led younger entry | 69, 74, 78 | Thin younger routes on 4–5-only pages; the same use as above (69 with 50 or 68, 74 with 66, 78 with 15's return visit). 78 also awaits re-approval. |
| Heavy, physically unrehearsed build | 85 | A foam-board pantograph for each pair costs an evening and $25–40 and has not been built; add it as a two-hour theme once an adult has rehearsed one. |
| Revise cards, fixed on October 23, whose theorem a path theme carries | 31, 51, 94 | Not yet re-reviewed after the fixes. 31 shares its gcd theorem with 4, 9 and 32; 51 shares a theorem with 55; 94 shares one with 84 and contrasts with 95. All of these are on the path. |
| Close partners of a theme the path uses | 79, 92 | 79's bowls and 80's midnight switches are paired supertasks (a catalog revisits link); the path takes 80, and 79's version 2 awaits re-approval. 92's fold-and-stretch track shares a theorem with 81 and contrasts with 46 and 93, all on the path. Either is a ready swap. |
| Strong reserves in the fullest areas | 22, 48, 49, 59 | Shape and dynamics have more good themes than slots: meeting regions (22), covers (48), Ducci rings (49) and constant width (59) are keep cards with pages for all three tables (22, 48 and 49 also have return visits), and the first swaps to make. |
| Atlas families whose entry needs algebra or calculus | 23 families: AD-12, AD-14, AD-15, AD-19, AD-20, AD-23, AP-06, AP-07, AP-12, AP-15, AP-17, AP-18, AP-19, AP-30, GA-06, GA-07, GA-08, GA-09, GA-17, GA-19, GA-27, GA-33, GA-34 | No K–5 band: no table in the room could enter. |
| Atlas families with a Grades 4–5 entry only | 27 families: AD-11, AD-16, AD-18, AP-03, AP-04, AP-05, AP-09, AP-10, AP-11, AP-13, AP-14, AP-26, AP-27, GA-03, GA-04, GA-10, GA-11, GA-12, GA-13, GA-14, GA-15, GA-18, GA-20, GA-23, GA-28, GA-35, GA-36 | Two tables would have nothing; use them as 4–5 continuations of the related weekly theme. |
| Atlas families with Grades 2–5 entries and no K–1 entry | 28 families: AD-02, AD-04, AD-06, AD-07, AD-08, AD-09, AD-10, AD-13, AD-17, AD-22, AP-01, AP-02, AP-16, AP-20, AP-21, AP-22, AP-24, AP-25, AP-29, GA-01, GA-02, GA-05, GA-16, GA-21, GA-24, GA-29, GA-30, GA-31 | The K–1 table would have nothing; several (AD-08, AD-09, AP-02, GA-21, GA-30) are good older-table continuations of a path theme. |
| Atlas families with a K–1 entry whose idea a path theme already carries | AD-03, AD-05, AP-08, GA-22, GA-25 | AD-03 repeats 19's antichains, AD-05 and GA-25 sit beside 52 and 53, AP-08 repeats 17 and its return visit, and GA-22 returns to 22, which is in reserve; each is a ready swap. |

**Return visits not on the path (23).** Each adds three new investigations to its theme, so any can replace a session or follow its theme for a group that wants more.

- **Base theme left out:** 22, 31, 48, 49, 51.
- **The second meeting comes through a related theme or atlas family instead:**
  - 14 (via 12);
  - 19 (via 63);
  - 20 (via 47);
  - 24 (via 60 and 87);
  - 27 (via atlas AP-23);
  - 33 (via the Week 4 return visit and AD-24);
  - 34 (via 35 and 37);
  - 38 (via GA-32);
  - 40 (via GA-26);
  - 43 (via 63);
  - 44 (via 46).
- **Base theme first met in Year 3 or later:** 23, 28, 29, 39, 46, 47, 50. The later slots go to Weeks 52–100 instead. These are the first candidates if the cycle repeats.

## For the organizer to decide

- **The encore's year.** Week 1e was added to this fall's plan on October 3; the path puts it in Year 2 (Y2·12) as a return to the tiles. If it is used this fall, move it into Year 1, drop its declared revisit of Week 1, and give Y2·12 to a reserve. The pattern-block return visit (Y4·1) still comes a year later.
- **Twenty sessions a year.** Is a spring–summer half of ten sessions realistic? With fewer sessions, keep the order and let each year end earlier. The check's area and revisit rules still apply.
- **Reviews behind Years 4–6.** The later years lean on themes the organizer has not yet signed off in their current form. The [organizer queue](review/ORGANIZER-QUEUE.md) lists Weeks 76, 80, 81 and 82 for re-approval after the October 23 card fixes. It lists 66, 67 and 68 for a first review. Fifteen path themes from Weeks 83–100 have no approval on record. Their reviews decide how firm Years 4–6 are.
- **Two-hour themes.** Should two-hour themes run on consecutive meetings, as here, or with a gap? A gap would let children's saved records carry the second visit, as the guides suggest. The cost is that the kit has to be stored.
- **Atlas families as whole sessions.** Seven atlas families stand as sessions here. Each has a K–1 entry, and six of them return to an earlier theme. Are atlas pages suitable as a whole room's hour, or better kept as table extras?
- **The published explorer.** The organizer's published [Math Circle Explorer](https://claude.ai/artifact/DarUYkLh2qfEBBDGF4cZm1) has not been updated; it still has four views. Republish it if the Path view should be shared.
