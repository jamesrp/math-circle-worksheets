# New themes for games, logic, networks and counting

October 24, 2026. Proposals only: twelve week outlines ready for the [worksheet workflow](../../worksheet-workflow/README.md), with no student pages or guides written. Nothing here is reviewed by the organizer, piloted or physically rehearsed.

The [six-year path](../six-year-path.md) uses every games (7), logic (7), networks (12) and counting (9) theme, so those areas have no reserves for swaps or a second cycle (its gap 3). Games for the younger tables are thinnest: only 4 of the 7 games themes have K–1 pages. This folder scouts new themes for those four areas, games and K–1 entry points first.

## Method

1. **Read.** AGENTS.md, the workflow README, `context.md`, the outline template and the Week 7, 66, 83 and 96 outlines; [CATALOG.md](../../CATALOG.md) and the catalog records for every theme in the four areas; the return-visit inventories ([1–17](../bonus-weeks-01-17.md), [18–34](../bonus-weeks-18-34.md), [35–51](../bonus-weeks-35-51.md)), since a return visit can already hold an idea (Week 7's adjacent-pairs game, Week 8's coins that cannot jump, Week 10's directed passwords, Week 33's windows on a ring, Week 36's Ramsey-style colouring); the path's gaps and left-out list; the review [calibration](../review/calibration.md); the year-1 handouts in `lowell-math-circle-year-1/`; and the [original grades 2–3 plan](../grades-2-3-year-a.md), whose summer list already proposed frogs and toads, map colouring and domino tilings.
2. **Search.** The JRMF activity index (`external-resources/jrmf/index.html`) and its public pages (Chomp, Sprigs, Graceful Gourds, Apple Picking and others); the MSRI Mathematical Circles Library list; Fomin, Genkin and Itenberg; Gardner; *Winning Ways*; Winkler; Knuth; Concrete Mathematics; the NYT Numberplay columns already downloaded; and undergraduate combinatorics, graph theory, combinatorial game theory and algorithms. The downloaded originals are not in this checkout, so local PDFs are named but their pages are not cited unless a public copy was read.
3. **Judge.** Each candidate had to have a theorem or invariant a mathematician finds compelling, a physical entry a parent volunteer can prepare in under 30 minutes, an honest K–1 entry (play, sort, build or move, with almost no reading), room for grades 4–5, and something genuinely new against the closest existing week or atlas family: a different theorem, representation or reasoning move. A repeat of a return visit counted as a repeat.
4. **Check.** Every number and small case quoted in the outlines is computed and asserted by [`check_claims.py`](check_claims.py) (standard library, about 30 seconds: `python3 plans/topic-scouting/check_claims.py`). Hand proofs in the outlines were checked by reasoning; general theorems that were not computed are cited.

44 candidates were considered: 12 kept and 32 set aside.

## Kept, ranked

Areas follow `catalog/concepts.toml`. "RV" is a week's return visit.

| # | Outline | Area | Kernel | K–1 entry | Materials | Closest existing themes | Sources |
|---|---|---|---|---|---|---|---|
| 1 | [Towers from either end](towers-from-either-end.md) | games | With an even number of towers, shading the slots alternately lets the first player take every tower of the richer colour, so they never lose; best play comes from a backward table of margins, and odd rows can be lost (1, 5, 1). | Take end towers in turn and compare hauls by stacking; find the 1, 5, 1 trap. | Snap cubes; plain and tinted slot strips. | 7, 8, 1e, AP-21 | Winkler 2004; Peterson, *Science News* 2005 |
| 2 | [Games decided before they start](games-decided-before-they-start.md) | games, networks | A bar always takes mn − 1 breaks, 2-Sprigs always n moves and Brussels Sprouts 5n − 2, so the winner is known in advance; Sprouts is only bounded (2n to 3n − 1 moves). | Break card bars and play 2-Sprigs with end tokens; the same player always wins. | Card grids or cube slabs; whiteboards; life tokens. | 56, 11, 1e | Fomin–Genkin–Itenberg; JRMF Sprigs guide pp. 1, 4–5; Gardner, *Mathematical Carnival* ch. 1; *Winning Ways* ch. 17 |
| 3 | [Poisoned cookie (Chomp)](poisoned-cookie.md) | games | Strategy stealing: the first player wins every rectangle, though no formula gives the winning bite; squares and two-row boards have explicit strategies. | Play small boards with a bite card; find the adult's winning first bite. | Grid boards, counters, an L-shaped bite card. | 7, 8, 1e, 83 | Gale 1974; Zeilberger 2001; JRMF Chomp |
| 4 | [Who beat whom](who-beat-whom.md) | networks | Every round-robin has a line-up in which each player beat the next (Rédei, an odd number of them), a top scorer is a king, and Landau's test says which win counts can happen. | Lay arrow cards between four animals after quick games and line them up. | Picture cards, arrow strips. | 87, 24, 23, 10 RV | Rédei 1934; Landau 1953; Maurer 1980; Moon 1968 |
| 5 | [Hidden armies](hidden-armies.md) | games | From 4 soldiers on, every split over three hills loses to a counter-plan; beating goes round in circles, so no plan is safe. | Split 5 or 6 cubes behind a folder and compare hill by hill. | Cubes, folders, hill mats. | 24, 87, AP-22, 58 | Borel 1921; Roberson 2006 |
| 6 | [Patterns you cannot avoid](patterns-you-cannot-avoid.md) | counting | Nine squares force an equally spaced one-colour three, five numbers a one-colour sum, six dots a one-colour triangle (pigeonhole); the game Sim. | Colour strips red and blue, checking threes with spacing combs. | Strips, counters, spacing combs, dot boards. | 36 and 36 RV, 62, 55 | Graham–Rothschild–Spencer; Greenwood–Gleason 1955; NYT Numberplay |
| 7 | [Pancake flips](pancake-flips.md) | logic | Two flips per pancake sort any stack (at most 2n − 3); counting breaks gives a lower bound; the worst stacks need 1, 3, 4, 5, 7, 8 flips for 2 to 7 pancakes. | Sort stacks of three card pancakes; find the stack that needs three flips. | Card or foam disks in six sizes. | 3 RV, 23, 3 | Dweighter 1975; Gates–Papadimitriou 1979; OEIS A058986 |
| 8 | [Train-yard sorting](train-yard-sorting.md) | logic, counting | One dead-end siding sorts exactly the arrival orders with no 2-3-1 pattern, and these are counted by the Catalan numbers through mountain paths. | Drive three numbered cars through the siding to leave 1, 2, 3. | Printed track mat, numbered cubes. | 12, 23, 3 | Knuth vol. 1 §2.2.1; Tarjan 1972 |
| 9 | [Counting-out circles](counting-out-circles.md) | counting | When every second person sits, the last standing is 2L + 1 for n = 2^m + L, from a doubling recurrence and a binary rotation. | Act out circles with counters that flip when they sit. | Circle mats, two-sided counters. | 4, 89, 8, 30 | *Concrete Mathematics* §1.3 |
| 10 | [Untangling networks](untangling-networks.md) | networks | Euler's formula gives E ≤ 3V − 6 (and 2V − 4 without triangles), so K5 and K3,3 can never be untangled; both fit on a torus. | Untangle pipe-cleaner networks until no link lies on another. | Paper dots, pipe cleaners. | 56, 40, 41, 10 | West §6.1; Kuratowski 1930; Tantalo's Planarity |
| 11 | [Hex](hex.md) | games | A full Hex board always has exactly one winner, so there are no draws; strategy stealing gives the first player a win nobody can describe on big boards. | Fill boards any way and try to make nobody win; play 3-by-3. | Printed hex boards, two colours of counters. | 16, 1e, Chomp (3 above) | Gale 1979; Gardner; Hayward–Toft 2019 |
| 12 | [Graceful labels](graceful-labels.md) | networks | A loop is graceful only when its length leaves 0 or 3 on division by 4 (parity); K4's ruler 0, 1, 4, 6; the graceful tree conjecture is open. | Label paths with cube towers and compare neighbouring towers. | Number cards, cubes, printed networks. | 10, 29, 55 | Rosa 1967; Golomb 1972; Gallian DS6 (2013) §§2.1–2.4 |

## Recommended top four

1. **Towers from either end.** The strongest K–1 game in the set: cube towers, end moves the material enforces, and a haul compared by stacking. The colouring guarantee is a real theorem that a 4–5 child can prove, and the backward table of margins carries Week 7's method from win/lose labels to scores.
2. **Games decided before they start.** Breaking a bar and 2-Sprigs give K–1 a game whose winner never changes, which children can notice for themselves; the older tables explain the count and then meet Sprouts, where a monovariant only bounds the length. It also links games to Week 56's Euler formula.
3. **Poisoned cookie (Chomp).** A classic children love with a deep idea new to the library: strategy stealing proves a win exists without finding it. The bite card enforces the rule physically, and the square trick and two-row rule give every table something to find.
4. **Who beat whom.** A networks theme with a natural K–1 action (lay arrows, line up the animals) and a sequence of theorems (Rédei's line-up, kings, Landau's win counts) that grows to grades 4–5. It revisits Week 87's cycles and Week 24's circles as directed networks.

Hidden armies is a close fifth and the best choice if the organizer wants a simultaneous game instead of a fourth game of perfect information.

## Set aside

Close behind, in rough order: each would make a reasonable theme, and the reason is why it is not in the twelve.

- **Champion and runner-up** (logic): the largest of n hidden cards takes n − 1 comparisons, the largest and second largest n + ⌈log₂ n⌉ − 2 (Kislitsyn; Lewis Carroll's lawn-tennis complaint). The K–1 core lasts a few minutes, the lower bounds are adversary arguments that are hard to make concrete, and it sits beside Weeks 6 and 23; best as a Week 23 return visit.
- **Tchoukaillon sowing** (games): exactly one winning board for each number of beans, built by playing backward ([1], [0, 2], [1, 2], [0, 1, 3], …). K–1-friendly with egg cartons, but it is a one-person routine whose proof repeats Week 7's work-backward move, and its striking fact (boards grow like n²/π) is for adults; first reserve for games.
- **Tower of Hanoi** (counting): 2^n − 1 moves, a 3^n-state map shaped like Sierpiński's triangle, and the ruler sequence shared with Gray codes. Widely met at home and school, so least fresh for returning children, and the K–1 core is brief; first reserve for counting, perhaps paired with Gray codes.
- **Squares on a dot grid** (counting): tilted squares counted by their upright boxes, n²(n² − 1)/12 (1, 6, 20, 50, 105). Needs geoboards or careful drawing and sits beside Weeks 57 and 31; a good companion to 57.
- **Circle regions** (counting): 1, 2, 4, 8, 16, then 31, from 1 + C(n, 2) + C(n, 4). Drawing 15 chords with no three through a point and counting 31 regions is beyond K–1 and error-prone at 2–3; a 4–5 extension of Week 12 or 56.
- **Venn loops** (logic): n circles make at most n² − n + 2 regions, so four circles cannot show all 16 kinds of a four-attribute deck. Excellent K–1 sorting, but the theorem is one region count and AD-01 and Week 36 already sort attribute cards.
- **Sliding tokens on networks** (networks): with one empty dot a 2-by-3 grid reaches only 60 of 120 arrangements, a loop only rotations, and the grid plus one diagonal all 120 (Wilson's theorem). The parity proof needs Week 3's permutation work first; a return visit for Week 3 or 90.
- **Locks and keys** (logic): "any 3 of 5 can open" needs C(5, 2) = 10 locks. Thin K–1 entry and abstract bookkeeping; near Week 19's subsets.
- **Frogs and toads** (counting): m frogs and n toads swap in mn + m + n moves, by counting jumps and slides. One fixed puzzle and one formula; the original grades 2–3 plan already proposed it; a K–1 warm-up.
- **Making teams** (counting): set partitions (Bell numbers 1, 2, 5, 15, 52) against Week 54's integer partitions. Listing the 15 splits of four children is bookkeeping-heavy and the recurrence is abstract.

Not kept:

- **Dots and Boxes**: the long-chain rule needs long play experience; a good club game.
- **Euclid's game** (the golden-ratio threshold): the same object as Week 32; a games-area return visit for it.
- **Kayles and JRMF's Apple Picking**: Week 7's return visit (adjacent pairs) and the copying of 1e, 7 and 8 already carry it.
- **Domineering and Cutcake**: partizan values belong with Week 83.
- **Bridg-it, the Shannon switching game**: Lehman's two-tree theorem is beautiful, but the strategy is abstract for K–5; an extension for Hex.
- **Tic-tac-toe in disguise** (Pick 15, and the word games of Gardner, *Mathematical Carnival* ch. 16, "Jam, Hot and Other Games"): addition to 15 shuts out K–1, and the theorem is an exhaustive search.
- **Gerrymandering** (JRMF): a thin theorem (a counting bound) in a politically loaded frame.
- **Polyomino enumeration and the five tetrominoes**: overlaps Weeks 26 and 98, Week 1's colouring obstructions and the old plan's pentomino week.
- **Degree builders** (Havel–Hakimi; two dots always share a degree): near Week 10's odd count, and strings tangle at K–1.
- **Knights and knaves**: year 1 used it (Handouts 9 and 11); reading-heavy, no K–1 entry.
- **Pool testing** (JRMF): Week 6's halving bound and Week 18's codes carry it.
- **Hat-colour parity strategies**: Week 84's headbands and Week 18's parity checks.
- **River crossings and state maps**: year 1 Handout 6.1; Week 29's rods share the jug idea.
- **Firefighter on a grid**: spreading and blocking on grids belong to Weeks 68 and 98.
- **Graph pebbling**: a nice weight argument, but "from any starting pile" is a heavy quantifier; near Week 11.
- **Domino trains**: Week 10's Euler theorem in new clothes; a Week 10 encore.
- **Round-robin schedules** (1-factorizations of K₂ₙ): adult-led, and overlaps Who beat whom and Week 62.
- **Spot it** (the Fano plane): finite geometry is Week 36's.
- **100 prisoners and boxes**: chance, which has reserves.
- **Peg solitaire and Conway's soldiers**: the positive part is fun, but the impossibility needs golden-ratio weights; 4–5 only.
- **Hamiltonian room tours**: Week 41's return visit has nine-cell tours.
- **Travelling salesman heuristics**: near Weeks 53 and 99.

## Using an outline

Each file follows [the template](../../worksheet-workflow/outlines/TEMPLATE.md) and starts "Week NN" because numbers are assigned on approval. To draft one, copy it to `worksheet-workflow/outlines/week-NN-<slug>.md` with the number filled in and run the workflow; every outline here has answers from enumeration, so add `CRITIC-MATH.md`. The workflow writes student pages only; the theorem-first facilitator guide is a separate step. Record the result as unpiloted, add its catalog record, and place it on the path in its area.

## Open points

- **Unchecked pages.** Several sources are cited by title without a page (Winkler, Fomin–Genkin–Itenberg, *Winning Ways*, Knuth's exercise numbers, *Concrete Mathematics*, West, Dudeney); the JRMF PDFs and NYT columns are local inputs not in this checkout.
- **Counting-out circles and year 1.** The year-1 "solitaire card game" (Handouts 6.7 and 7.8) may be this elimination run backward, but the handouts do not state the deal; ask the organizer before treating the theme as a return.
- **Chomp and Hex** share strategy stealing. If both are used, teach Chomp first and treat Hex's argument as a return.
- **K–1 load to watch in a pilot:** checking the 12 equally spaced threes on an 8-square strip (Patterns), tower differences in Graceful labels, and pipe cleaners that spring back (Untangling).
- **Physical materials are unrehearsed:** the bite card, spacing combs, siding mat, life tokens, pipe-cleaner networks and pancake sets.
