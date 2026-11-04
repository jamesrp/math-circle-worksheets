# Kid-fit review of every week (November 4, 2026)

Will each week actually work for children, and will they enjoy it? This review asked that question, band by band, of all 209 themes: Weeks 1 to 100, the Week 1 encore (1e), and the 108 draft plans for Weeks 101 to 208.

It complements the review cards in this folder, which check mathematics, page format and usability. The cards rarely ask whether a five-year-old would enjoy minute 25.

## How it was done

- Eighteen fresh reviewers (Claude subagents), none of them an author of these weeks, each took 10 to 14 weeks. They worked from one shared brief, kept in [kid-fit/BRIEF.md](kid-fit/BRIEF.md): the room (about 11 children, three tables, one adult per table at best, one hour), the kitchen table (a parent with a 5- and an 8-year-old), and three questions per band. Does it work in a room? Is it fun, with joy or surprise, or a chore? Can children that age do the core move themselves?
- Each band got one verdict. **strong**: most children that age would be absorbed and want more. **workable**: works with a capable adult and some care. **weak**: likely to fall flat unless redesigned. **skip**: wrong for that band.
- For Weeks 1 to 100 and 1e, reviewers read text extracts of the current student packets and facilitator guides, and opened PDF pages where diagrams mattered. Bonus, return-visit and extension packets were not reviewed. For Weeks 101 to 208 they read the draft plans.
- Reviewers were told not to read the existing cards, catalog verdicts, readiness report or draft triage, and to treat authors' claims as unverified. The busy beaver concern was not mentioned to them.
- The raw verdicts are in [kid-fit/verdicts.jsonl](kid-fit/verdicts.jsonl), one JSON line per week.

### Limits

- One reviewer per week, with no second opinion. Treat a single verdict as a hypothesis, the same as any unpiloted reviewer concern.
- These are model judgments, not observations. Text extracts lose diagrams, and a draft plan is easier to imagine going well than a finished packet. That probably makes the drafts look a little better than the existing weeks.
- Reviewers were lenient with grades 4–5: only 4 of 209 weeks got weak there. Read 4–5 "workable" as "unproven", not "fine".

## Counts

| Set | Band | strong | workable | weak | skip |
|---|---|---|---|---|---|
| Weeks 1–100 and 1e (101) | K–1 | 7 | 39 | 44 | 11 |
| Weeks 1–100 and 1e (101) | 2–3 | 21 | 58 | 18 | 4 |
| Weeks 1–100 and 1e (101) | 4–5 | 31 | 67 | 3 | 0 |
| Drafts 101–208 (108) | K–1 | 12 | 55 | 40 | 1 |
| Drafts 101–208 (108) | 2–3 | 25 | 72 | 11 | 0 |
| Drafts 101–208 (108) | 4–5 | 43 | 64 | 1 | 0 |
| All (209) | K–1 | 19 | 94 | 84 | 12 |
| All (209) | 2–3 | 46 | 130 | 29 | 4 |
| All (209) | 4–5 | 74 | 131 | 4 | 0 |

Grades 2–3 and 4–5 are mostly workable. K–1 is the weak band: 96 of 209 weeks are weak or skip there. Many K–1 routes in Weeks 60 to 100 are adult-led add-ons to activities designed for older children.

Twelve weeks are strong in all three bands: 1e (pattern-block blocking game), 5 (tower cities), 7 (take-away games), 8 (rook race and Nim), 10 (bridges), and drafts 120 (eight triangle gems), 123 (gallery guards), 124 (one straight cut), 141 (leaning towers), 153 (soap-film shortcuts), 170 (rep-tiles) and 204 (fastest slide).

## Checked against what actually happened

The use log records nine uses. On five of them the reviewers agree with what happened, or nothing was judged:

| Week | What happened | Reviewer verdicts (K–1 / 2–3 / 4–5) |
|---|---|---|
| 1 Tiling | went well in the circle | strong / strong / workable |
| 3 Shuffle machines | "pretty good" at home | workable / workable / strong |
| 5 Tower cities, 7 Take-away games, 86 Pursuit games | taught Oct 21, not judged | all strong except 86 K–1 workable |
| 2 Lamp lab | **went poorly on paper**: the rule lived only on the page | workable / workable / workable |
| 11 Chip firing | **"a big success"** at home, a success in the circle | weak / weak / workable |
| 15 Nearest-site maps | "good" at home with three children | weak / workable / workable |

Two of the clearly judged cases go against the reviewers, in opposite directions:

- **Week 11** was a hit, but the reviewer rated its pages a chore. Both may be true. Firing chips is a pleasure to do, and the pages are mostly tables of firing words and final piles. At home the activity was probably run as play rather than page by page. The lesson: judge the activity and the page separately, and don't let a dull page sink a good action.
- **Week 2** flopped on paper, but the reviewer called it workable in every band. The reviewer did notice that "the rule is easy to break by flipping one lamp". It didn't see that this would sink the session.

A cold kid-fit review is a useful filter, but it doesn't replace a pilot.

## The weakest weeks

Ordered by how little works in any band. Week 11 would rank here on its verdicts alone. It is left out because children enjoyed it, as above.

| Week | Title | K–1 / 2–3 / 4–5 | Why it struggles | The reviewer's one change |
|---|---|---|---|---|
| 77 | Persistent holes | weak / weak / weak | Rules and token bookkeeping dominate; the adult polices a procedure. | Physical "pour water in the loop" framing; drop the token cancelling. |
| 70 | Shields in a portal room | skip / weak / weak | Whether a shot is blocked is a precise point-on-line judgment, so the game becomes careful drawing. | Lattice-point shields and shots on a coarse grid or a pegboard with string. |
| 73 | The gentlest stretch | skip / skip / weak | Measuring differences under a millimetre can't show what it is meant to show. | Stretch a gridded rubber sheet; compare a few dramatic pairs. |
| 84 | Public knowledge (logic cafe, headbands) | weak / weak / workable | A possible-worlds card protocol so heavy the adult does the reasoning. | Act out the three-person cafe with real hidden cards. |
| 27 | Stable pairings | weak / weak / workable | Cross-checking preference lists overloads reading and working memory. | Role-play: each child holds one character's card and acts out the asking. |
| 80 | Midnight laboratory (lamp paradox) | weak / weak / workable | Almost no concrete action; an abstract endpoint debate. | A commit-and-defend betting game plus a physical Zeno walk. |
| 138 | Busy beaver (draft) | skip / weak / workable | Executing a rule table step by step; the record of 6 can't be beaten, and the "aha" is told. | Grades 4–5 only, as "stops or forever?": sort and prove a deck of small ready-made cards. |
| 39 | Road detours | weak / weak / workable | The pawn gives way to cancelling letter strings. | A yarn trail around posts, pulled tight to see what survives. |
| 51 | Honest measurement ranges | weak / weak / workable | Abstract ranges with no natural surprise. | A bluffing game: promise a range for a hidden length. |
| 92 | Fold-and-stretch predictions (tent map) | weak / weak / workable | Repeated map-reading and shading; the striking idea stays on paper. | Two markers start close; bet how many moves until they are far apart. |
| 115 | Wallpaper patterns (draft) | weak / weak / workable | Tracing and spinning dense printed patterns is fiddly and slow. | Bold pre-made patterns with pre-cut overlays; build and stamp. |
| 125 | One tile that never repeats (draft) | weak / weak / workable | Non-repetition is invisible on any patch children can build. | A kite-grid mat the hats snap into; build a floor together. |
| 175 | The chaos game (draft) | weak / weak / workable | Depends on many precisely measured dots. | A few hand jumps, then reveal the picture on a screen. |
| 65 | Hyperbolic octagon streets | weak / weak / workable | The geometry is told, not felt. | Tape paper octagons four to a corner and watch the surface ruffle. |
| 82 | Endless class lines (ordinals) | weak / weak / workable | After the finite warm-up there is nothing to do with hands. | Act out a class line that can't end. |

Close behind: 163 arrow multiplication, 166 hairy ball, 127 coastline, 93 Babylonian square roots, 78 tropical lines, 90 jeu de taquin, 64 octagon surface, 100 2-adic distance, 69 thin and fat triangles, 97 square remainders and 71, 72 and 75, which are grades 4–5 only and just workable there.

Weeks 60 to 100, the advanced prototypes, hold most of the weakest existing weeks. Several are marked keep on their cards, and 78, 80 and 82 are organizer-approved. Their cards checked the mathematics and the pages. Nothing in them asked whether children would enjoy it.

## Patterns behind the weak weeks

Tags reviewers attached (a week can have several):

| Tag | Weeks |
|---|---|
| bookkeeping-heavy | 78 |
| fiddly-materials | 65 |
| fine-motor | 58 |
| simulation-chore | 38 |
| abstract-start | 36 |
| adult-runs-it | 32 |
| no-surprise | 31 |
| wrong-age | 29 |
| too-many-rules | 28 |
| payoff-too-late | 27 |
| other | 19 |
| reading-heavy | 18 |
| luck-or-waiting | 17 |
| too-easy | 4 |

1. **A good physical start that turns into record-keeping.** This is the commonest problem (78 weeks). The launch is concrete, then the session becomes tables, tallies and lists that confirm an invariant: Week 11's firing tables, Week 39's letter strings, Week 60's card scoring. Children came to play and are filling in forms.
2. **The theorem needs precision children don't have** (58 weeks fine-motor, 65 fiddly materials). If the pattern only shows with accurate measuring, folding, tracing or dot-placing, noise hides it and the adult ends up asserting it. Examples: 73, 70, 64, 175, 127, 166, and Buffon's needle (130) for 2–3.
3. **Running a procedure instead of making choices** (38 weeks). Rule tables, sliding procedures, update rules and long simulations: busy beaver (138), Game of Life (137), jeu de taquin (90), tent map (92). Each step is rote, and the interesting thing happens only after many steps, if at all.
4. **Told, not felt** (36 abstract starts, 31 no surprise, 27 payoff too late). The surprise lives in a theorem children can't see at the scale they can build: aperiodicity, hyperbolic space, ordinals, the lamp paradox, recurrence of random walks. The "aha" arrives as the adult's story.
5. **The adult runs it** (32 weeks). Too many rules held at once, or too much reading, so the adult operates the activity while children watch. This is most of the K–1 weakness.
6. **Pitched older than the bands claim** (29 weeks). Many weeks offer all three bands on paper, but the K–1 route is a token.

**What the strong weeks have in common.** A game against a partner, or a puzzle with a clear goal. Instant physical feedback that settles who is right: the blocks fit or don't, the tower falls or holds, the soap film forms. A surprise a child can see with their own eyes. Few rules. Recording is optional or serves winning.

### For a "will kids enjoy this?" step in the authoring workflow

These findings suggest checks a fresh reviewer could apply to an outline before a writer drafts anything:

- Picture one child at minute 10 and minute 25. What are their hands doing? Is that a choice or a step in a procedure?
- Can the pattern be seen at the precision a child of that age actually has? If not, change the material or drop the claim.
- When is the first surprise or laugh? If it comes after 15 minutes of setup or recording, move it forward.
- What does the adult do? If they reason while children watch, redesign or cut that band.
- Is there more than one record per attempt? If so, cut it.
- Would they ask to play again? If not, what game could carry the same idea?
- Rate the activity and the printed page separately (the Week 11 lesson). Use real session outcomes from the use log to calibrate the reviewer (Weeks 2 and 11).

## Every week

| Week | Title | Kind | K–1 | 2–3 | 4–5 | What holds it back |
|---|---|---|---|---|---|---|
| 1 | Tiling lab (pattern blocks) | existing | strong | strong | workable | bookkeeping-heavy, reading-heavy |
| 1e | Pattern blocks encore: blocking game and fewest pieces | existing | strong | strong | strong | bookkeeping-heavy |
| 2 | Lamp lab (flip both ends of a line) | existing | workable | workable | workable | payoff-too-late, no-surprise |
| 3 | Shuffle machines (permutations) | existing | workable | workable | strong | simulation-chore, bookkeeping-heavy |
| 4 | Stars and wheels (star polygons, Caesar cipher) | existing | workable | strong | strong | fine-motor |
| 5 | Tower cities (visibility / skyscraper puzzles) | existing | strong | strong | strong | fiddly-materials, bookkeeping-heavy |
| 6 | Code breaking (yes/no questions, mastermind) | existing | workable | workable | workable | too-many-rules, adult-runs-it |
| 7 | Take-away games (subtraction Nim) | existing | strong | strong | strong | nothing major |
| 8 | Rook race and Nim | existing | strong | strong | strong | bookkeeping-heavy |
| 9 | Bouncing paths (paper pool) | existing | workable | strong | workable | bookkeeping-heavy, fine-motor |
| 10 | Bridges (Euler walks) | existing | strong | strong | strong | other:long-packet |
| 11 | Chip-firing with a sink | existing | weak | weak | workable | bookkeeping-heavy, simulation-chore, no-surprise, reading-heavy, adult-runs-it |
| 12 | Catalan pairings, paths and trees | existing | workable | workable | workable | bookkeeping-heavy, fine-motor, payoff-too-late |
| 13 | Route packing and bottlenecks | existing | workable | workable | workable | too-many-rules, fine-motor |
| 14 | Polygon triangulations and flips | existing | weak | workable | workable | fine-motor, fiddly-materials, bookkeeping-heavy |
| 15 | Nearest-site regions (Voronoi) | existing | weak | workable | workable | fine-motor, abstract-start, no-surprise |
| 16 | Three-colour triangles (Sperner) | existing | workable | workable | strong | too-many-rules |
| 17 | Machine memory (finite automata) | existing | weak | workable | workable | simulation-chore, abstract-start, wrong-age |
| 18 | Hidden changes (error-correcting codes) | existing | workable | workable | strong | bookkeeping-heavy |
| 19 | No card inside another (antichains) | existing | weak | workable | workable | no-surprise, bookkeeping-heavy, abstract-start |
| 20 | Averaging boards | existing | workable | workable | workable | no-surprise, bookkeeping-heavy, abstract-start |
| 21 | Shortest route touching a line | existing | weak | workable | workable | adult-runs-it, fine-motor, no-surprise |
| 22 | Meeting regions (Radon) | existing | weak | workable | strong | too-many-rules, fine-motor, bookkeeping-heavy |
| 23 | Sorting machines | existing | workable | workable | workable | simulation-chore, bookkeeping-heavy, fiddly-materials |
| 24 | Three random decks (nontransitive) | existing | workable | strong | strong | bookkeeping-heavy |
| 25 | Row and column shadows | existing | workable | workable | workable | bookkeeping-heavy, no-surprise |
| 26 | Same area, different boundaries | existing | workable | strong | workable | bookkeeping-heavy |
| 27 | Stable pairings | existing | weak | weak | workable | too-many-rules, bookkeeping-heavy, simulation-chore, adult-runs-it, wrong-age |
| 28 | Flat folds at one vertex | existing | weak | workable | workable | fiddly-materials, fine-motor, too-many-rules |
| 29 | Two-length rod builders | existing | workable | strong | strong | fine-motor |
| 30 | Two-pan weight kits | existing | workable | workable | strong | bookkeeping-heavy, fiddly-materials |
| 31 | Hidden orchard | existing | workable | workable | strong | fine-motor, bookkeeping-heavy |
| 32 | Squares inside rectangles | existing | weak | workable | workable | simulation-chore, fine-motor, no-surprise |
| 33 | Prime-length necklaces | existing | weak | workable | workable | reading-heavy, bookkeeping-heavy, abstract-start |
| 34 | Hidden turns | existing | weak | workable | workable | fiddly-materials, bookkeeping-heavy, adult-runs-it |
| 35 | Footprint borders | existing | weak | workable | workable | too-many-rules, fiddly-materials, adult-runs-it, wrong-age |
| 36 | Making threes | existing | workable | strong | strong | too-many-rules |
| 37 | Mirror twins | existing | weak | workable | workable | fiddly-materials, fine-motor |
| 38 | Seams and cuts (Möbius bands) | existing | workable | strong | strong | bookkeeping-heavy, adult-runs-it |
| 39 | Road detours | existing | weak | weak | workable | bookkeeping-heavy, simulation-chore, adult-runs-it, payoff-too-late |
| 40 | Loop color certificates (knot tricoloring) | existing | weak | workable | workable | fiddly-materials, fine-motor, reading-heavy, payoff-too-late, wrong-age |
| 41 | Torus portals and lifts | existing | workable | workable | workable | bookkeeping-heavy, simulation-chore, fiddly-materials, abstract-start |
| 42 | Fair results from a lopsided bag | existing | weak | workable | workable | reading-heavy, bookkeeping-heavy, wrong-age |
| 43 | Shuffling picture cards (fair shuffles) | existing | workable | workable | strong | simulation-chore, too-many-rules |
| 44 | The bag that copies (Pólya urn) | existing | workable | workable | workable | bookkeeping-heavy, payoff-too-late |
| 45 | The visible side (Bertrand's box) | existing | weak | workable | workable | fiddly-materials, too-many-rules, reading-heavy, wrong-age |
| 46 | Two boards forget their starts | existing | workable | workable | workable | no-surprise, simulation-chore |
| 47 | Gentle-step landscapes | existing | strong | strong | workable | too-easy |
| 48 | Inside and outside covers (area bounds) | existing | weak | workable | workable | bookkeeping-heavy, no-surprise, fiddly-materials, fine-motor |
| 49 | Four towers and differences (Ducci) | existing | workable | strong | strong | simulation-chore |
| 50 | Staircases and lengths | existing | weak | workable | workable | fine-motor, abstract-start, wrong-age |
| 51 | Honest measurement ranges | existing | weak | weak | workable | abstract-start, reading-heavy, no-surprise, fiddly-materials |
| 52 | Hinged frames and braces | existing | workable | strong | workable | fiddly-materials, adult-runs-it |
| 53 | Connecting networks | existing | workable | strong | workable | reading-heavy |
| 54 | Partitions and rebuilding | existing | workable | workable | strong | bookkeeping-heavy |
| 55 | Few sums and equal spacing | existing | weak | workable | workable | bookkeeping-heavy, payoff-too-late, no-surprise |
| 56 | Corners of a solid | existing | workable | workable | workable | fiddly-materials, bookkeeping-heavy, fine-motor |
| 57 | Area from dots (Pick's theorem) | existing | weak | workable | workable | bookkeeping-heavy, payoff-too-late |
| 58 | Fair division | existing | weak | workable | workable | abstract-start, reading-heavy |
| 59 | Constant width | existing | workable | workable | strong | fiddly-materials, fine-motor |
| 60 | Take it or pass | existing | weak | workable | workable | bookkeeping-heavy, too-many-rules, reading-heavy, payoff-too-late |
| 61 | Triangles on a ball | existing | weak | workable | workable | fiddly-materials, fine-motor, payoff-too-late, reading-heavy |
| 62 | Conflict networks (graph coloring) | existing | workable | strong | strong | fiddly-materials, other:redundant card+counter layer |
| 63 | Cards away from home (derangements) | existing | workable | workable | workable | bookkeeping-heavy, no-surprise, other:no story hook |
| 64 | Straight paths on an octagon surface | existing | skip | weak | workable | fine-motor, too-many-rules, reading-heavy, wrong-age |
| 65 | Hyperbolic octagon streets | existing | weak | weak | workable | abstract-start, no-surprise, other:key facts taken on trust |
| 66 | Lamplighter streets | existing | weak | workable | strong | fine-motor, other:small counters on printed strip |
| 67 | Meeting on shortest roads | existing | weak | workable | workable | too-many-rules, bookkeeping-heavy, no-surprise |
| 68 | How many ways out (ends of graphs) | existing | weak | workable | strong | fine-motor, too-easy |
| 69 | Thin and fat road triangles | existing | skip | weak | workable | abstract-start, too-many-rules, wrong-age |
| 70 | Shields in a portal room | existing | skip | weak | weak | fine-motor, abstract-start, adult-runs-it, payoff-too-late |
| 71 | Can you hear the room? (billiard bounce words) | existing | skip | skip | workable | fine-motor, too-many-rules, payoff-too-late |
| 72 | A robot that remembers (signed area) | existing | skip | skip | workable | bookkeeping-heavy, too-many-rules |
| 73 | The gentlest stretch (rectangle to square) | existing | skip | skip | weak | abstract-start, bookkeeping-heavy, fine-motor, no-surprise, wrong-age |
| 74 | Doubling elevators | existing | weak | workable | strong | fine-motor |
| 75 | Twists on a cylinder (winding) | existing | skip | skip | workable | fiddly-materials, fine-motor, abstract-start |
| 76 | Substitution strips (Thue-Morse) | existing | workable | workable | strong | fiddly-materials |
| 77 | Persistent holes | existing | weak | weak | weak | too-many-rules, bookkeeping-heavy, adult-runs-it, abstract-start, payoff-too-late, fiddly-materials |
| 78 | Three-armed lines (tropical geometry) | existing | weak | weak | workable | abstract-start, reading-heavy |
| 79 | Numbered-ball detectives (Ross-Littlewood) | existing | weak | workable | workable | simulation-chore, payoff-too-late |
| 80 | Midnight laboratory (lamp paradox) | existing | weak | weak | workable | abstract-start, no-surprise, adult-runs-it, reading-heavy |
| 81 | Buckets of Fish | existing | weak | workable | strong | too-many-rules, bookkeeping-heavy |
| 82 | Endless class lines (ordinals) | existing | weak | weak | workable | abstract-start, reading-heavy, wrong-age |
| 83 | Hackenbush balances | existing | workable | workable | strong | nothing major |
| 84 | Public knowledge (logic cafe and headbands) | existing | weak | weak | workable | too-many-rules, adult-runs-it, abstract-start, fiddly-materials, reading-heavy |
| 85 | Drawing machines (pantograph) | existing | weak | workable | workable | fiddly-materials, fine-motor, luck-or-waiting |
| 86 | Pursuit and escape (cops and robbers on graphs) | existing | workable | strong | strong | nothing major |
| 87 | Voting and agendas | existing | weak | workable | workable | bookkeeping-heavy, simulation-chore, abstract-start |
| 88 | Packing and kissing circles | existing | workable | strong | strong | fiddly-materials |
| 89 | Growing shapes and totals (differences and accumulators) | existing | workable | workable | workable | simulation-chore, bookkeeping-heavy, fiddly-materials |
| 90 | Sliding number arrays (jeu de taquin) | existing | skip | weak | workable | simulation-chore, too-many-rules, fiddly-materials, no-surprise, bookkeeping-heavy |
| 91 | Rotor-router machines | existing | workable | workable | strong | fiddly-materials, simulation-chore |
| 92 | Fold-and-stretch predictions (tent map) | existing | weak | weak | workable | abstract-start, simulation-chore, bookkeeping-heavy, wrong-age |
| 93 | Squaring a rectangle (Babylonian square roots) | existing | weak | weak | workable | payoff-too-late, wrong-age, fine-motor |
| 94 | Calibration lab (secret-extra machines) | existing | workable | workable | workable | too-easy, abstract-start |
| 95 | Count the unseen (capture-recapture) | existing | skip | workable | workable | luck-or-waiting, fiddly-materials, bookkeeping-heavy |
| 96 | Prime bags (factorization and divisors) | existing | weak | workable | workable | no-surprise, other:close-to-schoolwork |
| 97 | Square remainders (quadratic residues) | existing | skip | weak | workable | bookkeeping-heavy, wrong-age, no-surprise |
| 98 | Growing from a few seeds (bootstrap percolation) | existing | workable | strong | strong | nothing major |
| 99 | Moving piles (least work / earth mover's distance) | existing | weak | workable | workable | bookkeeping-heavy, no-surprise |
| 100 | Distance in nested worlds (ultrametric / 2-adic) | existing | skip | weak | workable | reading-heavy, abstract-start, wrong-age, payoff-too-late |
| 101 | Bead machines and the odd triangle | draft | workable | workable | workable | bookkeeping-heavy, fine-motor, other:errors-propagate |
| 102 | Domino diamonds (Aztec diamond) | draft | workable | workable | workable | bookkeeping-heavy, fiddly-materials |
| 103 | Tower maps and one-switch codes | draft | weak | workable | workable | adult-runs-it, bookkeeping-heavy, fiddly-materials, abstract-start |
| 104 | The sixteen-card square | draft | workable | workable | strong | too-many-rules |
| 105 | Knight's tours on small boards | draft | weak | workable | strong | wrong-age, other:hard-move-for-young |
| 106 | Colouring maps | draft | workable | strong | strong | fine-motor |
| 107 | Mazes, walls and random trees | draft | strong | strong | workable | fiddly-materials, simulation-chore |
| 108 | Hailstone numbers | draft | weak | workable | strong | simulation-chore, wrong-age |
| 109 | Sharing loaves the Egyptian way | draft | weak | workable | workable | fine-motor, fiddly-materials, adult-runs-it |
| 110 | Fibonacci coins | draft | weak | workable | strong | too-many-rules |
| 111 | Staircase numbers | draft | workable | strong | strong | nothing major |
| 112 | Spreading claps around a circle | draft | strong | workable | workable | other:noise-and-space |
| 113 | One magic square | draft | weak | workable | strong | wrong-age, other:arithmetic-practice |
| 114 | Sunflower spirals | draft | workable | workable | workable | fine-motor, payoff-too-late, fiddly-materials |
| 115 | Wallpaper patterns | draft | weak | weak | workable | fine-motor, abstract-start, adult-runs-it, wrong-age |
| 116 | Kaleidoscopes | draft | strong | strong | workable | fiddly-materials |
| 117 | Commutator puzzles | draft | workable | weak | workable | simulation-chore, fiddly-materials, bookkeeping-heavy |
| 118 | Card magic | draft | workable | strong | strong | nothing major |
| 119 | Juggling patterns | draft | weak | workable | workable | fiddly-materials, simulation-chore, fine-motor |
| 120 | Eight triangle gems | draft | strong | strong | strong | fiddly-materials |
| 121 | Cube nets | draft | workable | strong | workable | fine-motor, other:familiar-school-topic |
| 122 | Tangram shapes with no dents | draft | weak | workable | workable | fine-motor, payoff-too-late |
| 123 | Guards in a gallery | draft | strong | strong | strong | nothing major |
| 124 | One straight cut | draft | strong | strong | strong | fine-motor |
| 125 | One tile that never repeats | draft | weak | weak | workable | fiddly-materials, payoff-too-late, no-surprise, adult-runs-it |
| 126 | Cut and rearrange | draft | workable | workable | strong | fine-motor |
| 127 | How long is a coastline? | draft | weak | weak | workable | simulation-chore, bookkeeping-heavy, fine-motor |
| 128 | Splitting necklaces | draft | workable | workable | strong | too-easy, fiddly-materials |
| 129 | Wobbly table and crumpled map | draft | workable | workable | workable | fiddly-materials, bookkeeping-heavy |
| 130 | Buffon's needle and noodle | draft | workable | weak | workable | bookkeeping-heavy, luck-or-waiting, no-surprise |
| 131 | Collecting every sticker | draft | workable | workable | workable | luck-or-waiting, bookkeeping-heavy |
| 132 | Penney's coin-pattern races | draft | workable | strong | strong | luck-or-waiting |
| 133 | Simpson's paradox with bags | draft | weak | workable | workable | luck-or-waiting, wrong-age |
| 134 | Peg solitaire and Conway's soldiers | draft | workable | strong | strong | fiddly-materials |
| 135 | Trust game (prisoner's dilemma) | draft | weak | workable | workable | bookkeeping-heavy, adult-runs-it, other:social-upset-risk |
| 136 | Sealed-bid auctions | draft | weak | workable | workable | abstract-start, wrong-age |
| 137 | Game of Life | draft | weak | workable | workable | simulation-chore, adult-runs-it, too-many-rules |
| 138 | Busy beaver | draft | skip | weak | workable | simulation-chore, adult-runs-it, too-many-rules, no-surprise, wrong-age |
| 139 | Secret messages and two padlocks | draft | workable | strong | workable | bookkeeping-heavy |
| 140 | Proving without telling | draft | workable | workable | workable | luck-or-waiting, fiddly-materials |
| 141 | Leaning towers off the table | draft | strong | strong | strong | nothing major |
| 142 | Space-filling curves | draft | workable | workable | workable | payoff-too-late, fine-motor, bookkeeping-heavy |
| 143 | Domino computers | draft | workable | workable | workable | fiddly-materials, fine-motor, adult-runs-it |
| 144 | The MU puzzle | draft | workable | weak | workable | too-many-rules, fiddly-materials, payoff-too-late |
| 145 | Fake coin and the balance | draft | workable | strong | workable | fiddly-materials, bookkeeping-heavy |
| 146 | Easy to check, hard to find | draft | workable | workable | workable | no-surprise, other:K-1 example bag has odd total |
| 147 | Pairing strategies | draft | workable | workable | strong | fiddly-materials |
| 148 | Guess two-thirds of the average | draft | weak | workable | strong | adult-runs-it, luck-or-waiting, other:degenerate with 2 or 3 players |
| 149 | Racetrack | draft | workable | workable | strong | fine-motor, too-many-rules |
| 150 | Same network or different | draft | weak | workable | workable | fiddly-materials, bookkeeping-heavy, fine-motor |
| 151 | Instant Insanity | draft | weak | workable | workable | fiddly-materials, fine-motor, payoff-too-late |
| 152 | Who is most important? | draft | weak | workable | workable | simulation-chore, luck-or-waiting, bookkeeping-heavy |
| 153 | Soap-film shortcuts | draft | strong | strong | strong | fiddly-materials |
| 154 | Bulgarian solitaire | draft | workable | workable | workable | simulation-chore, bookkeeping-heavy |
| 155 | Weird dice | draft | workable | workable | workable | luck-or-waiting, wrong-age |
| 156 | Lining up by height | draft | weak | workable | strong | wrong-age |
| 157 | Remainders that repeat | draft | weak | workable | workable | simulation-chore, payoff-too-late, adult-runs-it |
| 158 | Squares from two squares | draft | workable | workable | strong | bookkeeping-heavy |
| 159 | Rectangles of a number | draft | workable | workable | strong | bookkeeping-heavy |
| 160 | Times tables on a circle | draft | weak | workable | workable | simulation-chore, fine-motor, payoff-too-late |
| 161 | Flexagons | draft | workable | strong | strong | fine-motor, fiddly-materials |
| 162 | Thirty coloured cubes | draft | workable | workable | workable | fiddly-materials, bookkeeping-heavy |
| 163 | Arrow multiplication | draft | weak | weak | workable | wrong-age, abstract-start, simulation-chore |
| 164 | Borromean rings | draft | workable | strong | workable | fiddly-materials, fine-motor |
| 165 | Inside or outside? | draft | workable | strong | workable | fiddly-materials |
| 166 | You can't comb a hairy ball | draft | weak | weak | workable | fiddly-materials, abstract-start, wrong-age |
| 167 | Walking a loop | draft | workable | strong | workable | fiddly-materials |
| 168 | Folding beats the compass | draft | weak | workable | workable | fine-motor, adult-runs-it |
| 169 | Stacking oranges | draft | workable | workable | workable | fiddly-materials, no-surprise |
| 170 | Rep-tiles | draft | strong | strong | strong | fiddly-materials |
| 171 | Shared birthdays | draft | workable | workable | workable | luck-or-waiting, bookkeeping-heavy, no-surprise |
| 172 | First digits (Benford) | draft | weak | workable | workable | bookkeeping-heavy, abstract-start, no-surprise |
| 173 | How long does Snakes and Ladders last? | draft | strong | workable | workable | luck-or-waiting, abstract-start |
| 174 | Shrinking piles | draft | workable | workable | strong | luck-or-waiting, bookkeeping-heavy |
| 175 | The chaos game | draft | weak | weak | workable | fine-motor, simulation-chore, payoff-too-late, fiddly-materials |
| 176 | Hide the bean (mixed strategies) | draft | strong | workable | workable | luck-or-waiting, bookkeeping-heavy |
| 177 | Pirates share the gold | draft | weak | workable | strong | too-many-rules, adult-runs-it |
| 178 | Bidding for turns | draft | weak | workable | workable | too-many-rules, abstract-start |
| 179 | Sharing the taxi fare | draft | weak | workable | workable | no-surprise, adult-runs-it, abstract-start |
| 180 | Who holds the power? | draft | workable | weak | strong | bookkeeping-heavy |
| 181 | A new road makes traffic worse | draft | workable | strong | strong | adult-runs-it |
| 182 | Passing secrets by phone | draft | workable | strong | strong | fiddly-materials |
| 183 | Can everyone get a partner? | draft | workable | workable | strong | fine-motor |
| 184 | Your friends have more friends | draft | weak | workable | workable | abstract-start, fiddly-materials, adult-runs-it |
| 185 | One-way streets | draft | workable | workable | strong | bookkeeping-heavy |
| 186 | Counting trees on numbered pegs | draft | weak | workable | workable | bookkeeping-heavy, fine-motor, other:overlaps-existing |
| 187 | Coin forests (percolation) | draft | weak | workable | workable | luck-or-waiting, simulation-chore, payoff-too-late, fine-motor |
| 188 | Small worlds and shortcuts | draft | workable | workable | workable | bookkeeping-heavy, other:needs-large-group |
| 189 | Guessing your own hat | draft | weak | workable | strong | abstract-start, adult-runs-it |
| 190 | Follow the loop (prisoners and boxes) | draft | workable | workable | strong | simulation-chore, fiddly-materials |
| 191 | Look-and-say | draft | workable | workable | strong | simulation-chore, bookkeeping-heavy |
| 192 | Short codes for common letters | draft | workable | workable | strong | bookkeeping-heavy, other:overlaps-existing |
| 193 | Langton's ant | draft | weak | workable | workable | simulation-chore, payoff-too-late, adult-runs-it, luck-or-waiting |
| 194 | Hilbert's hotel and the diagonal | draft | weak | workable | strong | abstract-start, wrong-age |
| 195 | Ordering stones with a balance | draft | workable | workable | workable | fiddly-materials, other:worst-case-abstract, adult-runs-it |
| 196 | Change ringing | draft | workable | workable | workable | simulation-chore, bookkeeping-heavy |
| 197 | Star patterns from crossing lines | draft | weak | workable | workable | fine-motor, other:overlaps-existing |
| 198 | Nibble a tile | draft | workable | strong | strong | fine-motor |
| 199 | Steering a card with perfect shuffles | draft | weak | workable | workable | fiddly-materials, simulation-chore, wrong-age |
| 200 | Kaprekar's sorting machine | draft | weak | workable | strong | simulation-chore, adult-runs-it |
| 201 | Prime pairs (Goldbach) | draft | workable | workable | workable | bookkeeping-heavy, no-surprise |
| 202 | Halfway to the wall | draft | workable | workable | strong | fine-motor |
| 203 | Press it again | draft | workable | workable | strong | fiddly-materials, reading-heavy |
| 204 | The fastest slide | draft | strong | strong | strong | fiddly-materials |
| 205 | Pi from polygons | draft | workable | workable | workable | bookkeeping-heavy, fine-motor, no-surprise |
| 206 | Folding the square root of two | draft | weak | workable | workable | fine-motor, abstract-start, wrong-age |
| 207 | Random walks home | draft | workable | workable | weak | luck-or-waiting, simulation-chore, payoff-too-late |
| 208 | Long runs | draft | workable | strong | strong | bookkeeping-heavy |

## Notes by week

### Week 1: Tiling lab (pattern blocks) (existing)

- **K–1, strong.** Filling a sailboat, cat and star with real pattern blocks at 1-inch scale is pure hands-on puzzling with no reading; five-year-olds happily turn pieces to fit corners. 'Ask an adult to trace' for the two-ways task is the only fiddly bit.
- **2–3, strong.** Getting stuck filling a board with blue rhombi and then discovering why (odd count, too many up-triangles) is a real, child-findable aha. Problem 3 (six boards, blues then purples, three numbers each) drifts into repetitive recording and can be trimmed.
- **4–5, workable.** Finding the six rhombus tilings and the flip map is engaging, but the ribbon-code pages (L/R codes, matching tables, circling RL pairs) become reading- and recording-heavy, and ten problems mostly ask for written explanation. A capable adult is needed to keep the letters tied to the blocks.
- **Best moment:** A 2-3 child realises the blue rhombus always covers one up and one down triangle, so board A can never be filled no matter how they turn it.
- **Biggest problem:** The grades 4-5 path piles ribbon codes, tables and written explanations onto a lovely flip-map discovery, so the second half becomes paperwork.
- **One change:** Cut the 4-5 ribbon section to one problem (trace the ribbon with string, read its code, rebuild a tiling from a code) and let children spend the saved time flipping real blocks between tilings.

### Week 1e: Pattern blocks encore: blocking game and fewest pieces (existing)

- **K–1, strong.** Placing blues in a turn-taking game and filling pictures with fewest/most pieces is all hands; kids can play many fast games and 'beat the grown-up'. Deciding who 'can always win' is beyond most five-year-olds, but the playing itself carries the hour.
- **2–3, strong.** The rhombus-placement game on symmetric boards gives a genuine surprise (second player wins by copying) that children can discover and test against the adult. The trapezoid up/down counting in Problems 4 and 7 is drier and more recording-driven.
- **4–5, strong.** The game and its centre-move exceptions give real strategy, and seeing a rhombus filling as a stack of cubes in a box corner is a memorable gasp. The flip-distance and odd-cycle proofs and the trapezoid-move problem ask a lot of written explanation, so expect few children to reach them.
- **Best moment:** A child spots that copying every move on the opposite side always wins, then beats the adult with it; or a 4-5 child builds the cube pile and suddenly sees the flat rhombi as 3D.
- **Biggest problem:** Several problems (trapezoid up/down tallies, later flip proofs) shift from building to counting and explaining, which is where attention will drop.
- **One change:** Front-load the game and the cube-pile reveal for every band and move the trapezoid up/down tally problems to an optional page.

### Week 2: Lamp lab (flip both ends of a line) (existing)

- **K–1, workable.** Flipping two counters at the ends of a line is a clear physical move, but matching small start/target pictures and planning which line to press is abstract for five-year-olds; an adult will read every prompt and steer. The early targets are easy enough to give some success.
- **2–3, workable.** Problems 1-7 are short, mostly easy 'make this picture' puzzles that may feel samey; the payoff (the impossible islands puzzle and the bridge that fixes it) arrives at Problem 8. The pointer/flipper/checker roles help, but the rule is easy to break by flipping one lamp.
- **4–5, workable.** The upper catalog asks real questions (which targets are possible, all solution sets, fewest moves, ring records) and the even-per-island rule is a nice discovery, but 'find every set of lines' on six-node graphs is search-and-record heavy without much play.
- **Best moment:** Trying and failing to move the light across to the other island, then realising every press changes two lamps so the lone light can never go out.
- **Biggest problem:** The impossibility surprise that makes the week sing comes late, after many easy and similar-feeling puzzles.
- **One change:** Put the islands puzzle (and a 'can you make just one lamp on the square?' puzzle) early, so children hit the impossibility within ten minutes and spend the rest explaining and inventing.

### Week 3: Shuffle machines (permutations) (existing)

- **K–1, workable.** The chair launch is great fun and moving cubes down arrows is doable, but each turn is a two-step procedure (all down, then slide up) repeated many times with a tally, so it leans toward rote simulation. Drawing their own machines for a target number of turns is the best part but needs adult help.
- **2–3, workable.** Predicting from coloured loops and finding the 5-slot machine that takes 6 turns is a nice surprise, but there are many machines to run and record, and Problems 6-8 (composition, all 6-slot orders, 7-slot maximum) ask for long explanations.
- **4–5, strong.** Predicting return times without cubes, the 'slowest machine' race and doing perfect card shuffles by hand give real puzzles and a surprising result (52 cards return after 8 shuffles). Composition and inverse problems are abstract but optional.
- **Best moment:** Children discover that a 5-slot machine takes 6 turns, more turns than cubes, because the pair and the trio only line up at 6.
- **Biggest problem:** Most of the hands-on time at K-1 and 2-3 is executing turns and tallying, so the activity can feel like a simulation chore before any pattern appears.
- **One change:** Do more machines as human chair-switching (whole body, everyone counting) and have tables predict first, so physical simulation is short, social and always paired with a guess.

### Week 4: Stars and wheels (star polygons, Caesar cipher) (existing)

- **K–1, workable.** Hopping a counter around big dots and watching a star appear is appealing, and the dots are large, but the same task repeats on rings of 4, 5, 6, 7 and children must also draw straight lines on small rings. The picture-ring 'secret hop' pages are a nice change but abstract.
- **2–3, strong.** Drawing stars on 8-12 dot rings with guesses is satisfying, and making a real code wheel and sending secret messages is exactly the kind of thing 8-year-olds love. Cutting the wheels takes about 10 minutes, which the guide plans for with spares.
- **4–5, strong.** Cracking codes with unknown settings, the crack race, predicting pieces on big rings and the cardioid coda give variety and real reasoning; the gcd rule is reachable by experiment.
- **Best moment:** Cracking a partner's coded message on your own spinning wheel, or seeing a five-pointed star draw itself from a simple hop.
- **Biggest problem:** The K-1 packet repeats one procedure across many rings with little new to notice each time.
- **One change:** Give K-1 a simple picture-wheel 'secret message' game earlier and drop two of the repetitive ring pages.

### Week 5: Tower cities (visibility / skyscraper puzzles) (existing)

- **K–1, strong.** Building rows of 1-2-3 cube towers, putting your chin on the table and counting what you see is concrete and a bit silly in a good way; the hidden-row game behind a folder is a real game they can play themselves.
- **2–3, strong.** Building 3-by-3 cities with coloured towers and solving and inventing edge-number puzzles is genuinely absorbing; colour-by-height makes checking easy. Problems 6-7 (count all 12 cities, totals always 22) are more bookkeeping but optional.
- **4–5, strong.** 4-by-4 skyscraper puzzles are a proven, addictive puzzle type, and making minimal-clue puzzles for a partner adds challenge. The counting problems (24 and 120 rows sorted in a table) are dry and will be skipped by many.
- **Best moment:** A partner lifts the folder and the guessed row matches the hidden one, or a child realises you can never see just one tower from both ends.
- **Biggest problem:** Preparation is heavy: about 96 pre-built towers and over 240 cubes, likely more than a 30-minute job for one parent.
- **One change:** Have children build their own towers as the first five minutes of play (or reuse a stored kit) rather than asking a parent to pre-build every tower.

### Week 6: Code breaking (yes/no questions, mastermind) (existing)

- **K–1, workable.** Guessing a hidden pattern block with yes-or-no questions is a great kitchen-table game for five-year-olds. The counter code game needs the adult to keep the secret and do all the copying and scoring, and 'can you always be sure' questions are beyond most of them.
- **2–3, workable.** Children like code games, but the scoring procedure (copy the test behind a folder by column number, place triangles, count) is error-prone and a wrong score spoils the game; the two-colour codes are small enough that deduction can feel thin.
- **4–5, workable.** The 1-16 number game and finding a method for 3- and 4-counter codes are solid, and the lower-bound 'why not fewer' arguments are real reasoning, but the play is slowed by the folder-and-copy scoring ritual and a referee role.
- **Best moment:** Pinning down a hidden block in exactly three questions after realising each good question cuts the blocks in half.
- **Biggest problem:** The keeper's copy-and-score routine is a fragile procedure that eats time and produces wrong scores, which breaks the deduction that is the whole point.
- **One change:** Simplify scoring: the keeper looks over the folder at the test and places one triangle per match directly on the breaker's side, with no copying, and add a third colour for 4-5 so the deduction is richer.

### Week 7: Take-away games (subtraction Nim) (existing)

- **K–1, strong.** Taking 1 or 2 counters, losing to the grown-up and hunting for the secret is a fast, competitive game five-year-olds will replay; the track helps them see 'land on 3, 6, 9'. Colouring the squares is light.
- **2–3, strong.** The 1-3-4 rule has a non-obvious pattern (0, 2, 7, 9...) that children can find by playing and colouring, and testing Lena's and Omar's claims gives real reasoning. Rounds are short so tears and boredom are manageable.
- **4–5, strong.** Many rules, the repeating patterns, 'take as many as you can is wrong', misère and two-pile copying give plenty of depth; Race to 100 against the organizer is a reliable hook. Fourteen problems is more than anyone needs.
- **Best moment:** A child finally beats the grown-up because they figured out to leave 3, 6 or 9 counters.
- **Biggest problem:** Later problems shift from playing to colouring tracks, which can feel like filling in charts once the pattern is found.
- **One change:** Keep every colouring problem paired with a 'play the adult from a pile you choose' challenge so the charts are always used to win something.

### Week 8: Rook race and Nim (existing)

- **K–1, strong.** Sliding a token to the star and taking counters from two piles are simple moves, and discovering that copying wins from 7 and 7 is a real aha a first grader can find and use against the adult. Seating so the star is in the same corner for both matters.
- **2–3, strong.** Colouring the 8-by-8 board and seeing the diagonal, then realising the board is just two piles, is a satisfying surprise; three-pile searches in Problems 8-9 get long but are optional.
- **4–5, strong.** Finding the binary-stack rule for Nim and using it to beat the organizer from a big start is a classic thrill; the queen game is a good stretch. Explaining why the rule always works will need adult conversation.
- **Best moment:** A child beats the adult from piles of 7 and 7 by copying every move, or a 4-5 child wins from 13, 9, 7 using the stacks rule.
- **Biggest problem:** The three-pile search problems (all starts up to 6 or 7) can turn into systematic listing before the rule is found.
- **One change:** Replace the 'find all starts' listing with 'beat the organizer from these five starts', letting the rule emerge from wanting to win.

### Week 9: Bouncing paths (paper pool) (existing)

- **K–1, workable.** Walking the ball on a taped floor grid and guessing the stopping corner is excellent, but tracing diagonal paths on paper and keeping the right direction after each bounce is error-prone for five-year-olds, and the ruler-cut-fold-hold-to-light Problem 7 is a fine-motor stretch.
- **2–3, strong.** Tracing tables, predicting the corner and the prediction game against a partner are engaging, and noticing that 4 by 6 behaves like 2 by 3 is a findable aha. Folding the unfolded strip to see the bounce is a lovely but fiddly extra.
- **4–5, workable.** The rule (lowest terms, parity decides the corner, p+q-2 bounces) is a great target, but filling a 36-table chart by tracing is a long chore even split three ways, and the folding sheet needs careful cutting and marker work.
- **Best moment:** Children stand at the corner they guessed while a classmate walks the floor grid as the ball and everyone shouts 'bounce'.
- **Biggest problem:** The 4-5 path relies on tracing dozens of tables to fill a chart before the pattern appears.
- **One change:** Give 4-5 a partly filled chart (or let each child trace only the tables that test a conjecture) so time goes to predicting and explaining instead of tracing.

### Week 10: Bridges (Euler walks) (existing)

- **K–1, strong.** Walking a token over printed bridges and picking up counters is a concrete game that 5-year-olds can run themselves, and getting stuck and trying again is the activity. The floor-tape town launch and the build-a-town fallback give movement and choice; the adult only reads the problem once.
- **2–3, strong.** Pairs walk, get stuck, retry and write the walk as letters. Counting bridges per island leads to a rule they can state themselves and then use to predict towns before walking. Problem 8, where they build a town to a spec for a partner, is a good puzzle-making task.
- **4–5, strong.** Königsberg, the odd-island argument, the impossible exactly-one-odd-island question, Lee's loop-splicing walk and the fewest-extra-counters route are all real reasoning that stays grounded in counters. The referee role keeps the third child involved.
- **Best moment:** Realising that the stuck towns all have more than two islands with an odd number of bridges, then correctly predicting a new town without walking it.
- **Biggest problem:** The packets are long (12-13 pages), and the counter-per-bridge setup and reset take real time, so pairs can spend a lot of the hour resetting counters rather than thinking.
- **One change:** Cut each packet to the core 4-5 problems, and have children mark the starts they have tried with a pencil dot so the reset loop stays short.

### Week 11: Chip-firing with a sink (existing)

- **K–1, weak.** The page opens with a dense paragraph of rules, and every problem is a table of sharing words and final piles that an adult must scribe. The investigation's answer, that order never matters, is a non-event for a 5-year-old, and K-1 P6 adds chips one at a time eleven times.
- **2–3, weak.** Firing chips is a pleasant physical move, but every page repeats the same experiment: finish a start in two orders and fill a table row. The finding is always the same, so the surprise wears off after the first table. P6 is 24 add-and-stabilize runs.
- **4–5, workable.** Older children can carry out the firings and appreciate why the finish is unique. P5's termination proof and P6's order-independence proof are real mathematics, but they will need a strong adult to supply the weight-function idea, and the tables are still long.
- **Best moment:** A child's 12-chip pile cascades around the board, and the finish matches the partner's even though they fired in a completely different order.
- **Biggest problem:** The activity is mostly recording firing words and final piles in tables, to confirm an invariant whose payoff is that nothing changes.
- **One change:** Drop most of the tables and replace them with one striking challenge: two children race different orders on the same big pile and bet on whether they will match. Then pose a goal-seeking puzzle, such as which start ends at a target pile.

### Week 12: Catalan pairings, paths and trees (existing)

- **K–1, workable.** Pairing six dots on a circle with strings without crossings is a good hands-on puzzle with a findable answer (5). The odd-dots impossibility is a nice aha. Fourteen eight-dot pairings and drawing chords on the small recording circles are too long and too fiddly for most 5-year-olds.
- **2–3, workable.** Enumerating six-dot rainbow pairings is good. The U/D path code is a clear, concrete bridge, and spotting illegal codes is a nice puzzle. But P6, drawing all 14 eight-dot pairings, is a long drawing chore, and the matching tasks are mostly transcription.
- **4–5, workable.** Ordered trees and walk codes are a real bijection puzzle, and the legal-code rules are good reasoning. But trees start abstract on paper with no physical material. P6 asks children to count 42 and 132 trees, which is hopeless by hand unless an adult steers them to the recurrence.
- **Best moment:** Noticing that the counts of different objects come out the same (1, 2, 5, 14), or that a pairing's string code turns into a mountain path that never dips below ground.
- **Biggest problem:** Much of the work is drawing complete collections of 14 near-identical small diagrams, which turns into tedious bookkeeping before the interesting matching appears.
- **One change:** Stop each band's enumeration at 5 objects, and spend the saved time on the code puzzles: a mystery code to decode, and a broken code to spot.

### Week 13: Route packing and bottlenecks (existing)

- **K–1, workable.** Tracing coloured routes on small arrow boards and blocking all travel with markers are concrete, findable puzzles, and the closure game in P6 adds real play. But the one-route-per-arrow rule is easy to break unnoticed, and coloured pencil cannot be undone.
- **2–3, workable.** Children can find maximum route sets and minimum blocking sets, and may notice that the two numbers match. The complete list of 8 blocking pairs and the add-an-arrow puzzle are good tasks. The proofs that a collection cannot be larger will mostly come from the adult.
- **4–5, workable.** The max-flow/min-cut duality is a real aha. But the change-walk (augmenting path with backward steps) adds a new rule set that many 10-year-olds will find confusing. P7 is a general theorem proof most will not reach.
- **Best moment:** Finding that the most routes that fit always equals the fewest markers that stop every route.
- **Biggest problem:** Routes drawn in pencil on paper are hard to revise, and nothing physical stops a child from reusing an arrow. So the key constraint is policed by an adult rather than by the material.
- **One change:** Use physical route pieces (yarn or coloured strips laid on arrows, one per arrow) so routes can be moved and the one-route-per-arrow rule is enforced by the material.

### Week 14: Polygon triangulations and flips (existing)

- **K–1, weak.** Drawing straight diagonals with a straightedge on one-inch recording pentagons and hexagons, then flipping lines with tracing paper, is beyond most 5-year-olds' motor control. The adult ends up drawing, and the triangle-count question has little pull at this age.
- **2–3, workable.** Finding the 5 pentagon fillings is satisfying. Discovering that the flip map of a pentagon is itself a pentagon is a genuine surprise. The 14 hexagon fillings and the tracing-paper flips are long and fiddly.
- **4–5, workable.** Shortest flip routes to a fan and the connectivity proof are substantial, reachable reasoning. The odd-cycle question is a good twist. Children spend a lot of time redrawing octagon triangulations by hand.
- **Best moment:** Drawing the join map for the five pentagon fillings and seeing that it makes a pentagon.
- **Biggest problem:** Every move requires precise redrawing of small diagrams, so drawing labour crowds out the thinking, especially for younger children.
- **One change:** Use a physical board, such as pegs or dots on a whiteboard polygon with sticks or wiki sticks for diagonals, so a flip is lifting one stick and placing another rather than redrawing on tracing paper.

### Week 15: Nearest-site regions (Voronoi) (existing)

- **K–1, weak.** Comparing string lengths to label crosses is doable but slow. But 'divide the sheet' asks a 5-year-old to draw an accurate perpendicular-bisector boundary on a blank frame, which needs abstraction and precision they lack, so the adult will draw it.
- **2–3, workable.** Folding to find the fair line between two dots is a nice trick, and three or four sites give a reasonable puzzle. But the dry 'dots and regions' framing and accurate line drawing make it more of a construction exercise than a game.
- **4–5, workable.** The inverse puzzles are genuinely good: place dots so A owns exactly the shaded triangle, and decide whether new dots can steal R but not P and Q. Convexity and the question of whether adding a dot can ever help an old one give real reasoning.
- **Best moment:** Placing three new dots so that A's region snaps exactly onto the shaded triangle.
- **Biggest problem:** The core action is accurate geometric drawing on a blank frame, with no story or game to make children care who owns which place.
- **One change:** Give it a story and a body launch, such as kids as ice-cream stands in the room with a 'which stand is closest?' walk-around. Lead with the inverse placement puzzles rather than ruler construction.

### Week 16: Three-colour triangles (Sperner) (existing)

- **K–1, workable.** Placing R/B/Y counters on a six-dot board and trying not to make a rainbow triangle is simple and concrete, and failing every time is a real surprise. With only four little triangles the boards are small enough, though the side rules are an extra thing to remember.
- **2–3, workable.** Trying to avoid an all-three triangle on bigger boards is a good hook. But the doors-and-routes argument (routes cross edges, must exit two-door triangles) piles on rules, and writing letters on many dots is slow.
- **4–5, strong.** The odd-count conjecture comes from children's own failed attempts. The door pairing argument is a proof 10-year-olds can follow and check by tracing. P6's broken side rule shows why the hypothesis matters.
- **Best moment:** After several tries to avoid a rainbow triangle, a child realises it is impossible and that the count is always odd.
- **Biggest problem:** For 2-3, the jump from 'try to avoid it' to marking doors and drawing routes adds a rule-heavy representation before children want an explanation.
- **One change:** Make the opening a two-player game: one player places counters trying to avoid a rainbow triangle while the other hunts for one. Introduce doors only after the group asks why it never works.

### Week 17: Machine memory (finite automata) (existing)

- **K–1, weak.** Moving a marker along R/B arrows is a fine board-game move for P1. But listing every 4-card row (P2), finding distinguishing rows (P3, P6) and designing machines (P4-5) are abstract tasks that a 5-year-old will watch an adult do.
- **2–3, workable.** Designing a machine for 'saw a red' or 'last card blue' is a good puzzle, and the groups-of-three cycle is satisfying. P1 is 16 rows times two machines of rote running, and the 'fewest circles, explain why' lower bounds will mostly be adult-led.
- **4–5, workable.** Building divisible-by-k machines and spotting the cycle pattern is engaging. The distinguishing-histories lower bound is deep and reachable for strong 10-year-olds, but it is a verbal proof with little hands-on payoff.
- **Best moment:** Building a machine that correctly says YES to every row with a multiple of three reds, and testing it on a friend's long row.
- **Biggest problem:** After the first page, the activity shifts from operating a machine to abstract design and proofs of minimality, with no game element to sustain it.
- **One change:** Add a 'guess my machine' game: one child secretly builds a two- or three-circle machine, and the others feed it rows and try to work out what it detects.

### Week 18: Hidden changes (error-correcting codes) (existing)

- **K–1, workable.** The secret sender-changer-receiver game behind a folder is a role-play kids enjoy, and trying to fool the receiver is fun. But P2's listing of every possible outcome, P4's every key and P5's every row are enumeration that adults will record.
- **2–3, workable.** Playing the game and then designing keys that the changer cannot beat is a good puzzle with an adversary. Finding every four-counter key (P4) and the two-change extension get heavy.
- **4–5, strong.** The shortest key for four pictures, why three pictures cannot fit in four positions, and the 'differ in 3 places' rule are excellent puzzles that grow straight out of the game and allow real proofs.
- **Best moment:** The changer secretly flips a counter, and the receiver still names the right picture, then finds the one flip that would have fooled a bad key.
- **Biggest problem:** The game is the fun, but most printed problems switch to exhaustive listing of rows and keys, which is bookkeeping for younger children.
- **One change:** Keep children in game mode longer: a team designs a key, and the other team plays changer trying to break it. Score breaks, and let the 'every row' listing come only when a dispute needs settling.

### Week 19: No card inside another (antichains) (existing)

- **K–1, weak.** Comparing whether one card's pictures are all on another is a doable check, but the goal of avoiding inclusion is a negative rule with no game or story. Recording collections means drawing cards, so 5-year-olds are unlikely to stay engaged past Problem 1.
- **2–3, workable.** Searching for the largest legal hand from a physical deck is a decent puzzle. The chain-row bound is clever but adult-guided, and listing every collection is tedious.
- **4–5, workable.** Maximal-versus-maximum and the six-card two-symbol answer with a matching six-row proof are real mathematics that 10-year-olds can check. The activity is fairly dry, and classifying every largest collection is bookkeeping.
- **Best moment:** Getting stuck at a collection that cannot take another card, then finding a bigger one elsewhere.
- **Biggest problem:** There is no game or tension: children sort cards against an abstract rule, and the payoff (a size bound) is invisible to younger children.
- **One change:** Turn it into a two-player game, where players take turns adding a card to a shared pile without breaking the rule and the last to move wins. The size question then arises naturally.

### Week 20: Averaging boards (existing)

- **K–1, workable.** Problem 1, sharing a copied 0-stack and 4-stack into equal piles with cubes, is a real concrete move a 5-year-old can do. But 'one pile per joined shape, including empty ones' is subtle, linked circles that must work at once are beyond most K-1 children, and Problem 2 asks them to record about ten triples in tiny boxes.
- **2–3, workable.** Adding and halving to fill a circle is easy. Filling chains of linked circles by guess-and-adjust is a decent puzzle, but kids will mostly be doing arithmetic checks. 'A circle can't beat every square' is close to obvious, so it doesn't land as a surprise.
- **4–5, workable.** Filling linked boards (some needing thirds) is a fair puzzle. Most of the packet, though, asks for proofs 'for every finite board' (maximum principle, uniqueness), and kids will reach those through adult talk rather than their own discovery.
- **Best moment:** On a chain of circles between 0 and 6, finding that the values have to step up evenly (2, 4) for everything to balance.
- **Biggest problem:** The rule that every circle must work at the same time turns each board into solving a linear system by trial, and the theorem it leads to feels obvious to kids, so the work is checking with no gasp.
- **One change:** Make it a balance or 'fair neighbour' game with one free circle on a long chain and a hidden target, so kids predict before checking, and drop the 'every finite board' proof pages to adult notes.

### Week 21: Shortest route touching a line (existing)

- **K–1, weak.** K-1 children can bend a string around one contact point, but the guide admits a contact 1.5 cm off is only 1-3.5 mm longer, so string can't tell them which is shortest. Seven near-identical 'find the shortest' boards leave them guessing, holding taut string on dot centres, with no tool to settle the question.
- **2–3, workable.** Folding or tracing to reflect B and drawing a straight line is a real aha, and straightedge work suits the age. But kids rarely invent the fold themselves, so an adult usually supplies it, and the remaining pages are repetitive construct-the-route boards.
- **4–5, workable.** This is the classic Heron problem, and the reflection proof is within reach. The locus and restricted-segment problems give it depth. The concrete string phase is short and inconclusive, and once kids have the trick the boards become routine constructions.
- **Best moment:** Folding the paper on the line and seeing that the best bent route becomes one straight line to the reflected dot.
- **Biggest problem:** The physical experiment can't tell routes apart, so the discovery depends on an adult revealing the reflection trick, and most pages repeat the same construction.
- **One change:** Open with a big-difference board and a 'river and well' story so string comparisons actually decide something, then use a mirror or fold reveal as the single surprise and cut the number of near-duplicate boards.

### Week 22: Meeting regions (Radon) (existing)

- **K–1, weak.** Children have to juggle splitting four labels into two groups, using every label once, drawing hulls, shading, and finding a shared point. That is too many rules for a 5-year-old, and drawing triangles through small dots on record boards is fiddly, so the adult ends up doing the split while the child watches.
- **2–3, workable.** Finding a split for a given placement is a decent puzzle, and the placement game (try to beat your partner) has real pull. But listing all seven splits on many small boards is a chore, and drawing hulls accurately slows things down.
- **4–5, strong.** The adversarial game, placing four dots to defeat your partner and always failing, gives a real 'why can't I win?' moment. The contrast with three dots, and explaining the guarantee, suits this age.
- **Best moment:** A child places four dots sure the partner can't split them, and the partner finds the crossing anyway.
- **Biggest problem:** The packet buries the game under split enumeration and record boards, and the rules page is dense for younger children.
- **One change:** Lead every band with the 'beat your partner' placement game using movable markers and a rubber band, and keep the complete-list enumeration as an optional 4-5 extension.

### Week 23: Sorting machines (existing)

- **K–1, workable.** Sliding dot cards past a bar so the smaller one goes up is a simple physical move, and 'find a start that breaks the machine' is concrete. But keeping track of all six starts, and building machines that sort one set but fail another, needs adult bookkeeping. Most K-1 children will run starts the adult chooses.
- **2–3, workable.** Building a three-lane sorter with fewest bars and hunting for failing starts is satisfying. But the four-lane tasks mean running many starts (24 orders, or 16 zero-one starts) through the mat, which turns into a repetitive simulation.
- **4–5, workable.** Finding the five-bar four-lane sorter is a good challenge, and the zero-one shortcut is real depth. The threshold, swap-record and lower-bound pages are abstract and heavy, though, and still need lots of hand runs.
- **Best moment:** Finding the one starting order that sneaks through a machine unsorted.
- **Biggest problem:** Testing a machine means running many starts card by card, so the minute-to-minute work is simulation and recording, and the kit takes about 40 minutes to cut and tape the first time.
- **One change:** Run it as a floor game with kids as the cards walking the lanes, and frame the main task as 'build a machine your partner can't break' with a challenger choosing starts, so kids test only the starts that matter.

### Week 24: Three random decks (nontransitive) (existing)

- **K–1, workable.** Circling the bigger number in nine pairs is easy, and drawing from bags is fun. But the three comparison tables are 27 near-identical circles, and the cycle surprise needs an adult to point it out. The later construction problems (swaps, two-card decks) are beyond most K-1 children.
- **2–3, strong.** Playing the bag game, then finding that A beats B, B beats C and yet C beats A, is a genuine gasp. Building their own cycles with 1-6 and 7-9 is a puzzle they'll want to keep at, and 'can six wins in a row make you sure?' sparks good arguments.
- **4–5, strong.** Kids get the cycle surprise, then construction puzzles with all-arrangements searches, then a clean proof that two-card decks can't cycle. Each step builds on a hands-on game, and the reasoning is within reach.
- **Best moment:** Realising that whichever deck your partner picks, you can always pick one that beats it.
- **Biggest problem:** The K-1 pages front-load three tables of rote comparisons before any play, so the youngest kids may tire before the surprise.
- **One change:** Start every band with the 'you choose first, I'll choose second and beat you' game, and have kids count pairs only after they suspect something odd.

### Week 25: Row and column shadows (existing)

- **K–1, workable.** Putting counters on a small grid to match row and column counts is concrete and nonogram-like, and finding a second picture is a nice challenge. Matching rows and columns at once strains some 5-year-olds, and drawing the full six-picture catalog is long for them.
- **2–3, workable.** The switch move and 'make a picture your partner can't copy differently' are good puzzles. Several pages are find-every-picture or find-every-switch catalogs that become recording work.
- **4–5, workable.** Counting pictures and shortest switch routes leads to a real general rule for two rows. But the tasks are dry catalog-and-distance work on 2-row grids with little surprise, and the payoff is a formula rather than an aha.
- **Best moment:** Two children build different pictures that cast exactly the same shadows.
- **Biggest problem:** After the first ambiguity surprise, most pages are catalogs of near-identical small grids, so recording takes over from discovery.
- **One change:** Make the partner challenge, 'hide a picture, give only its shadows, can I find a different one?', the spine for all bands, with catalogs as optional proof work.

### Week 26: Same area, different boundaries (existing)

- **K–1, workable.** Building the five four-tile shapes and making long or short shapes with tiles is concrete and fun. Counting 10-14 exposed sides with edge markers is doable but slow, and Problem 5 (explain why some lengths are impossible) is beyond most K-1 children.
- **2–3, strong.** Kids build with tiles, discover that every perimeter is even, and find the 4n-2e rule by counting shared sides. Explaining why a straight row is longest gives them an aha earned by building.
- **4–5, workable.** The early optimisation problems are good, and the row/column bound is real reasoning. Later pages (37, 50 and 73 tiles, a general area-perimeter rule) move to paper-and-formula work far from the tiles, so it gets abstract and dry.
- **Best moment:** Noticing that no matter how you arrange the tiles, the boundary count is always even.
- **Biggest problem:** Counting boundary sides one by one is slow and error-prone, and it dominates the younger tables' time.
- **One change:** Give K-1 a 'snake versus blob' race (longest and shortest boundary with the same tiles) using a string or edge-marker loop instead of a full catalog, and keep the large-n formula pages as optional 4-5 extensions.

### Week 27: Stable pairings (existing)

- **K–1, weak.** A 5-year-old has to read preference strips, remember who is currently paired, and check two different preferences at once for each possible blocking pair. The adult reads and checks while the child points at tokens, so the child isn't making the mathematical move.
- **2–3, weak.** Finding every stable pairing among six (or 24) pairings means checking many cross pairs against two strips each. That is a long, error-prone bookkeeping task with little joy, and the four-pair problem is especially heavy.
- **4–5, workable.** Running the asking algorithm and proving it ends and is stable is a classic upper-elementary investigation, and the 'make the greedy rule fail' task is a good construction. But tracking holds and requests by hand is a long simulation, and kids may lose track before the proof.
- **Best moment:** Running the asking rules with the other side asking and getting a different stable pairing.
- **Biggest problem:** The core action is cross-checking abstract preference lists, which overloads working memory and reading at the lower bands and turns into bookkeeping at the upper one.
- **One change:** Run it as role-play with characters such as animals choosing houses: each child holds one character's card and acts out the asking rules, and only grades 4-5 try to prove stability.

### Week 28: Flat folds at one vertex (existing)

- **K–1, weak.** Folding a precreased disk flat is a nice hands-on move. But labelling mountain and valley from a fixed front after unfolding is confusing, small tabs are fiddly, and finding all eight labelings needs systematic bookkeeping a 5-year-old won't sustain.
- **2–3, workable.** Fitting loose angle wedges into half-turns is a pleasant physical puzzle, and 'which disks can't fold, and why' gives a real obstruction. Folding precreased paper reliably and reading M/V labels will need adult rescue.
- **4–5, workable.** The alternating-angle condition is a satisfying discovery from paper, and classifying the eight right-angle labelings is solid reasoning. Paper models of the odd angles may not cooperate, and the angle-arithmetic pages are fairly dry.
- **Best moment:** A disk that looks fine refuses to fold flat, and the wedges show why: the alternating angles don't add to a half-turn.
- **Biggest problem:** The kit takes about two and a quarter hours of cutting and precreasing, far beyond a busy parent's 30 minutes, and none of it has been physically folded yet.
- **One change:** Cut the kit to one or two precreased squares per child, folded from plain paper at the table, plus one wedge set per table, and drop the K-1 tab and route-card materials.

### Week 29: Two-length rod builders (existing)

- **K–1, workable.** Building lengths from 3-rods and 4-rods and noticing that 5 can't be made is concrete and a 5-year-old can do it. The 1 cm card-stock rods are small and fiddly to line up for little hands, and 'could you keep going forever?' needs adult framing.
- **2–3, strong.** Hunting for the last impossible length is a gripping puzzle. Discovering that three consecutive builds plus one more 3-rod cover everything after gives a real aha, and 2-rods and 4-rods are a nice counterexample.
- **4–5, strong.** Comparing last gaps across pairs and conjecturing ab-a-b is a genuine pattern discovery. The 'finite certificate covers infinitely many' argument is accessible and satisfying.
- **Best moment:** Realising that once you can build three lengths in a row with 3-rods and 4-rods, you can build every length forever.
- **Biggest problem:** At K-1 the 1 cm paper rods are small and fiddly, so building sometimes becomes alignment work instead of thinking.
- **One change:** Use larger rods (2 cm per unit, or Cuisenaire rods or linking cubes) for K-1 and frame it as a 'which numbers can the shop sell?' story with a hunt for the last impossible one.

### Week 30: Two-pan weight kits (existing)

- **K–1, workable.** Laying cube sticks end to end and matching row lengths is a real hands-on move a 5- or 6-year-old can do, and finding that 3 beside the 2 balances 1 is a nice small surprise. But 'beside the target' takes careful adult modelling, and checking every target from 1 to 6 for three kits, then up to 13, becomes adult-tracked checking well before minute 25.
- **2–3, workable.** Choosing 8, 9 or 10 and finding that only 9 fills 1 to 13 is a satisfying puzzle with sticks in hand. P3 asks for about 40 balance checks, and the counting bound (P5) and the fourth weight (P6) turn into adult explanation for most children this age.
- **4–5, strong.** It is a classic puzzle with a real 'aha': powers of three, and placing weights on the target's side. Kids can build, guess and check the next weight themselves, and the proofs that it's unique and best possible stretch strong 4-5 children without asking them to know algebra.
- **Best moment:** Realising a weight can go on the same pan as the target, so 1 and 3 suddenly make 2.
- **Biggest problem:** The younger bands drift from moving sticks into systematic checking of long target lists, which is bookkeeping rather than discovery.
- **One change:** For K-1 and 2-3, make it a partner challenge game: one child names a target, the other races to balance it with the kit, and the 1-3-9 kit is revealed as 'the kit that never loses'.

### Week 31: Hidden orchard (existing)

- **K–1, workable.** Stretching a taped thread to a dot and seeing that another dot sits right on it is concrete and easy to show. But keeping the thread exactly through small dots is a fine-motor strain for 5-year-olds, and circling every visible dot on 24 to 48 dots, plus P3's systematic blocker counts, becomes long checking.
- **2–3, workable.** Thread testing gives way to pattern hunting: 'both even means hidden' fails on (4,4) and (6,6), which is a good surprise. Children can make the divisibility guess themselves, but there's a lot of coordinate listing and near-miss arguing about whether the thread really touches a dot.
- **4–5, strong.** Kids can discover the common-factor rule from the thread, and (13,8), where the thread seems to hit dots that the rule says it misses, is a genuine 'the math beats the string' moment. The both-directions proof and the target with 99 blockers give real depth.
- **Best moment:** Finding that (1,1) hides the whole diagonal, and later that (13,8) is visible even though the thread looks blocked.
- **Biggest problem:** Thread precision on small dots causes disputes and fine-motor frustration, especially for the youngest, and P1-P3 ask for full-grid sweeps.
- **One change:** Use a large floor or table grid with pegs or coins as trees and a long string held by two children, so 'can you see it?' becomes a physical game before any recording.

### Week 32: Squares inside rectangles (existing)

- **K–1, weak.** Placing card squares onto rectangles is a fine fitting task, but the 1 cm grid and 1 cm cut squares are tiny for 5-year-olds, and each problem's payoff ('which square comes last?', 'do they match?') is an outcome nobody that age cares about. An adult will run the rule while kids place pieces.
- **2–3, workable.** Drawing the biggest square, then the next, is a clear procedure children can do, and linking the last square to equal tilings is a real pattern to find. Minute to minute, though, it's repeated drawing and recording of side lists, with the 'aha' resting on comparisons an adult has to steer.
- **4–5, workable.** Predicting the last square (the greatest common divisor) and proving the invariant are substantial, and the 49-rectangle search crowning 13x8 (Fibonacci) is a nice reveal if the search is shared. Kids who already know common factors may find the rule unsurprising, and the search is largely bookkeeping.
- **Best moment:** The pooled search revealing that 13 by 8 alone gives five different square sizes.
- **Biggest problem:** The core activity is a repeated draw-a-square-and-record procedure with a quiet payoff, and the K-1 materials are too small to handle comfortably.
- **One change:** Make it a race or prediction game on big grids (2 cm or larger, with large cut squares): predict the last square before cutting, and score correct predictions, so the procedure serves a guess children care about.

### Week 33: Prime-length necklaces (existing)

- **K–1, weak.** Putting counters on a ring is easy, but the work is reading letter strings from a moved start arrow and judging whether two readouts are the same ring by rotation. That's too many things to hold in mind for most 5- to 6-year-olds, and counting 'readouts' is an abstraction that an adult will end up tracking.
- **2–3, workable.** Sorting the eight and then the 32 printed cards into rotation families is a real, checkable group task, and finding that every mixed five-bead family has exactly five cards, so 32/5 'doesn't work', is a nice puzzle. But reading and rotating 5-letter strings is dry, and cutting and sorting 32 cards takes much of the hour.
- **4–5, workable.** The contrast between 4 and 6 beads (early repeats) and 5 and 7 beads (never) is a genuine surprise, and it leads to a real proof and Fermat-style divisibility. The path there is a long letter-card sort, and P6-P7 are abstract enough that only stronger 4-5 children will own them.
- **Best moment:** Discovering that six-bead rings can repeat after 2 or 3 steps but seven-bead rings never do.
- **Biggest problem:** Using letters instead of beads turns a physical, colourful idea into string reading and card sorting.
- **One change:** Use real coloured beads on pipe-cleaner loops or coloured counters only (no A/B letter cards), and let children physically spin rings to compare, keeping cards as an optional record for older kids.

### Week 34: Hidden turns (existing)

- **K–1, weak.** Making a counter pattern 'your partner can't match' is a lovely challenge, but testing each pattern means tracing and colouring every circle onto tracing paper, then turning and flipping it accurately. 5-year-olds can't do that reliably, so the adult traces and the kids watch.
- **2–3, workable.** The 'can you beat the tester?' framing works, and finding that two colours fail on small rings but work on six is a real surprise. However, each candidate needs a fresh coloured tracing and up to 11 move checks, so much of the time goes to copying rather than thinking.
- **4–5, workable.** Minimum-colour questions, the unequal-gaps construction and the minority-of-three bound give 4-5 children real reasoning to defend. Tracing-paper overhead still slows the exploration, and kids who can mentally rotate may find the physical testing tedious.
- **Best moment:** Finding that two colours are hopeless on five spots but suddenly enough on six.
- **Biggest problem:** The tracing-copy workflow (trace, colour, lift, flip, for every candidate) dominates the session and sidelines the youngest.
- **One change:** Put patterns on a rigid clear disc or paper plate with stickers, so a child can simply pick it up, turn or flip it, and drop it on the printed ring, with no tracing.

### Week 35: Footprint borders (existing)

- **K–1, weak.** Laying footprint cards into a repeating border is fun, but the tasks then require tracing-strip copies (the adult traces), measured 'shortest slides', glides and half-turns about chosen points. That's far beyond a 5-year-old's grip on the rules, so the adult operates the testing.
- **2–3, workable.** Building borders that meet a challenge (matches after a glide but not a flip) is a genuine construction puzzle with cards in hand. But the vocabulary, the tracing strips and the 'shortest matching slide' comparisons pile up rules, and few 7- to 8-year-olds will keep them all straight.
- **4–5, workable.** Glide-squared-is-a-slide and forced half-turns are real discoveries 4-5 children can test with cards and a copy. P6, 'every symmetry and why no other', is a proof-heavy finish, and handling 24 small cards plus tracing strips is fiddly.
- **Best moment:** Seeing that a walking line of left-right footprints matches itself only by a flip-and-slide, not by either move alone.
- **Biggest problem:** Too many moves and rules (slide, flip, glide, half-turn, shortest lengths) for a tracing-paper workflow, so younger children lose the thread.
- **One change:** Start with children actually walking in paint or chalk, or stamping footprints, then use a single clear acetate strip for testing, and limit the K-1 and 2-3 pages to slides and glides.

### Week 36: Making threes (existing)

- **K–1, workable.** Big shape-and-fill tiles and 'find the third' is SET-like play that some 6-year-olds love. But applying two all-same-or-all-different tests at once is hard for many 5-year-olds (the guide itself gates it), and the largest no-three collection needs checking every triple, which an adult will do.
- **2–3, strong.** Completing pairs, trading puzzles, and the turn-taking game are quick, tactile and replayable, and finding that every game lasts exactly four moves (so the second player always wins) is a lovely surprise children can test many times.
- **4–5, strong.** Kids can discover and then prove unique completion, the four-tile maximum (with the pair-markers-in-dishes proof), and the forced game length themselves with tiles in hand. It's a compact, complete world with real proofs.
- **Best moment:** Playing the adding game repeatedly and realising it always ends on move four, whatever anyone does.
- **Biggest problem:** For the youngest, juggling two attributes at once is the bottleneck, and failing it makes every later task adult-checked.
- **One change:** Give K-1 a one-attribute (shapes only, or colours only) version of the game and pair puzzles first, adding the second attribute only for children who are breezing through.

### Week 37: Mirror twins (existing)

- **K–1, weak.** Turning a model to match a partner's is fun, but matching four corners of a 3D tetrahedron in your head and hands is hard at 5 or 6. Repeatedly failing on the mirror pair gives no sense of 'impossible' at this age, and the caps held by sticky tack will fall off small hands.
- **2–3, workable.** Mirror twins that just won't match is a genuine 'wait, why?' moment (like left and right hands), and the twist that making two letters the same makes them match is a second surprise. Building and relabelling models is fiddly, and P3 and P6 need careful bookkeeping of which caps changed.
- **4–5, workable.** Children can own the viewing-order certificate, the any-merge-works argument and the count of 12 rotations and 2 classes, which is strong mathematics. But about 1.5 to 2 hours of folding models and caps far exceeds the 30-minute prep limit, and the model has never been pretested.
- **Best moment:** Trying every turn and discovering the mirror-image pair can never be made to match.
- **Biggest problem:** Material prep (13 folded card tetrahedra plus sticky-tack letter caps) is far beyond a busy parent's 30 minutes, and the models are untested.
- **One change:** Use cheap ready-made objects, such as four coloured gumdrops or clay balls on toothpick tetrahedra or a pack of plastic tetrahedra, with coloured stickers instead of letter caps.

### Week 38: Seams and cuts (Möbius bands) (existing)

- **K–1, workable.** Running a marker along a Möbius band and colouring 'both edges' with one colour, then watching an adult cut it into one big loop, gives real gasps even at 5. The four-dot partition pictures and the yes/no grids are too abstract for this age and should be skipped.
- **2–3, strong.** The middle cut and especially the one-third cut (two linked loops) are guaranteed delight. U/L seam tracking gives children a real way to predict and explain. The four-dot yes/no grids are a dull middle, but the cutting surprises carry the session.
- **4–5, strong.** Predicting pieces versus edges, explaining them from the seam recipe, and the arrow that comes back reversed give older children deep, checkable reasoning tied to a famous surprise.
- **Best moment:** Cutting the Möbius band down the middle and getting one long loop instead of two, and then the one-third cut giving two linked loops.
- **Biggest problem:** The abstract four-dot partition pictures with yes/no grids sit between the magical cuts and the children, and keeping all cutting adult-only removes much of the hands-on joy for 7- to 10-year-olds.
- **One change:** Let grades 2-5 do their own cuts with safety scissors and replace the four-dot grids with a simple predict, cut and count table (pieces, edges, twists), keeping the partition question as an optional extension.

### Week 39: Road detours (existing)

- **K–1, weak.** Moving a pawn on a road map is fine, but the task is writing ordered step cards with endpoint labels and arrows and deleting out-and-back pairs. Adults must prepare and record every card, so the 5-year-old watches a letter-string procedure, with no surprise at the end.
- **2–3, weak.** Children build long routes as card rows and cancel reversals, which quickly becomes symbol manipulation. The tree results are predictable, and the one surprise, that order matters on two rings, comes late, after a lot of transcription.
- **4–5, workable.** Kids can reach the uniqueness question, the 'zero net loops but it won't disappear' commutator and the 16-versus-8 count themselves, which is real reasoning for strong 4-5 children. The minute-to-minute activity is still writing and reducing route strings.
- **Best moment:** Finding that going around left, right, left backwards, right backwards cannot be undone, even though every loop is cancelled out on net.
- **Biggest problem:** The concrete pawn quickly gives way to recording and cancelling ordered letter strings, which is bookkeeping without much payoff for the younger bands.
- **One change:** Make it a physical string or yarn game: children walk a yarn trail around posts (trees versus rings) and pull it tight to see what survives, saving the step-card reduction for 4-5.

### Week 40: Loop color certificates (knot tricoloring) (existing)

- **K–1, weak.** The cords are fun to handle, and the 3-by-3 crossing completion (P2) is a good marker puzzle. But counting arcs on a tangled figure-eight, reading the arc/underpass rule, coloring a thin channel and the end-dot move check (P6) are beyond most 5–6-year-olds, so the adult ends up doing the reading and checking.
- **2–3, workable.** Untangling cords A–D and then finding all nine trefoil colorings are real puzzles a 7–8-year-old can do with tracing paper and a partner referee. The two-crossing end-dot table (P5–6) is abstract bookkeeping with no clear reason to care at that age.
- **4–5, workable.** The arc is great: cord C refuses to come undone, and the coloring count (9 vs 3) proves it can never be done. It depends on a supplied theorem and a 27-case slide check that feels like a chore, and the cords need careful adult preparation (trefoil handedness, taped joins).
- **Best moment:** Three cords fall open into a plain loop but cord C will not, and then the coloring count shows it never can.
- **Biggest problem:** Most of the session is a rule-checking exercise on thin printed channels and end-dot tables, while the one exciting physical contrast (cords) is a single short problem.
- **One change:** Build the session around the cord race and a large trefoil to color with fat markers or colored string pieces, and keep the Reidemeister end-dot checks as a 4–5 return visit only.

### Week 41: Torus portals and lifts (existing)

- **K–1, workable.** Moving a pawn off the right edge and popping out on the left is a Pac-Man-like thrill, and 'reach every square in two steps' and 'can two pawns swap?' are concrete. On a tiny 3-by-3 map nearly every move wraps, so a 5-year-old will often lose the row or column and need the adult to say where the pawn goes.
- **2–3, workable.** Finding trips home in 3 and 6 steps is a good open search. Replaying trips on copy arrays and marking which copy you finish in, on 25 mm copies, is fiddly tracking that will feel like a chore for many 7–8-year-olds.
- **4–5, workable.** Winding pairs (which copy you end in) are an accessible and surprising invariant. Converting RRRUUU to UUURRR by nine square slides on tracing paper is rote, and the classification question (P6) is a very abstract finish that only a few children will own.
- **Best moment:** Two pawns given the same arrows can never trade places: the gap between them travels with them through every portal.
- **Biggest problem:** The good idea (winding = finishing copy) is buried under small-map wraparound confusion and long copy-tracking and slide sequences on paper.
- **One change:** Use a larger portal map (or a floor grid) with a target-chasing game, and let the repeated tiled map be built physically for every band before asking about copies or slides.

### Week 42: Fair results from a lopsided bag (existing)

- **K–1, weak.** Drawing counters and making color pairs is fun, but 'equal chances when a shape comes out', weighing 9/3/3/1 marked pictures and finding every fair rule are conditional-probability ideas a 5–6-year-old cannot hold. The adult would be doing the thinking.
- **2–3, workable.** Inventing a fair rule for a 3-red-1-blue bag is a real puzzle, and the 4-by-4 labeled grid makes the RB/BR symmetry checkable. Later questions (changing bags, six-pair promises) are wordy, and the random draws are explicitly set aside as only exploration, so hands-on time is short.
- **4–5, workable.** Discovering that a lopsided bag can still make a perfectly fair coin is a genuine aha, and the optimality and no-replacement questions give depth. The work quickly becomes reading and grid counting rather than drawing, so some children will drift.
- **Best moment:** Realizing that BR and RB are always equally likely, so even a 3-to-1 bag can produce a fair coin flip.
- **Biggest problem:** The concrete drawing gives way almost at once to reading-heavy exact-probability arguments on labeled grids, and K–1 cannot reach the core idea.
- **One change:** Make it a two-player game first: each child bets on square or circle under their invented rule and plays 20 rounds, so unfair rules lose visibly before the labeled grid is introduced to explain why.

### Week 43: Shuffling picture cards (fair shuffles) (existing)

- **K–1, workable.** Making all six rows of A, B, C with real cards is ideal K–1 work, and drawing from a cup is fun. The ticket-and-swap procedure with two ticket sets and resets is an adult-paced routine for 5–6-year-olds, so the later problems become follow-the-steps.
- **2–3, workable.** Matching the six ticket stories to the six rows is satisfying, and finding several stories that make the same row under the 'wrong' rule is a nice discovery. Juggling ticket sets and swap rules is a lot of procedure, and the 27-story fairness question needs adult help.
- **4–5, strong.** The natural-looking shuffle has 27 equally likely stories, which can't split evenly among 6 orders, so it must be unfair. That is a crisp, surprising proof that 10-year-olds can own, and designing a 4- and 5-card fair shuffle is a satisfying build.
- **Best moment:** Seeing that the obvious 'swap each slot with any slot' shuffle has 27 stories, and 27 can't be shared fairly among 6 orders.
- **Biggest problem:** Swap procedures with ticket-set resets are easy to misexecute and dominate the younger tables' time.
- **One change:** Give K–1 and 2–3 more time with direct card choosing and building all rows, and introduce the swap procedure only through an adult-led demonstration with children acting as slots.

### Week 44: The bag that copies (Pólya urn) (existing)

- **K–1, workable.** Draw, put back, add a copy is a simple physical action, and 'which bags can you make?' and 'can blue ever disappear?' are answerable by doing. Listing every four-draw color story (P3–4) is recording work an adult will carry, with little surprise for this age.
- **2–3, workable.** Seeing that color stories and marked histories count differently is real thinking, but tracking marked counters (R1, R2, B1…) through two draws and comparing chances exactly is heavy for 7–8-year-olds. The copy versus no-copy contrast is a good hook if an adult keeps the records.
- **4–5, workable.** The surprise that 0, 1, 2 or 3 red draws are all equally likely is striking, and predicting the pattern for 4 and 5 draws is a good conjecture task. Getting there requires enumerating 24 marked histories, which is bookkeeping-heavy.
- **Best moment:** After counting histories, every possible number of red draws comes out exactly equally likely, which nobody expects from a bag that 'favors' what it already has.
- **Biggest problem:** Most of the time goes into enumerating and labeling histories rather than playing with the bag, so the delightful uniformity result arrives late.
- **One change:** Open with a whole-group experiment: everyone runs 3 copying draws many times and stacks a class bar chart of red counts, so the flat result is seen first and the marked histories then explain it.

### Week 45: The visible side (Bertrand's box) (existing)

- **K–1, weak.** The behind-the-screen guessing round is fun, but the ticket-to-face mapping, filtering to 'red showing' and then comparing hidden colors, plus ticket-removal ties, needs more abstraction and working memory than most 5–6-year-olds have. The adult would run the sorting.
- **2–3, workable.** Sorting the six tickets and seeing that red showing hides red two ways out of three is a good surprise for 7–8-year-olds. The card, ticket, screen and cover setup is fiddly, and the later chooser comparisons are wordy.
- **4–5, workable.** Refuting the friend's 'only two cards remain so 50-50' argument is a classic paradox that 10-year-olds enjoy, and the extra-clue and fair-subset questions add depth. The game is barely played (no tally), so the surprise rests on argument rather than on experience.
- **Best moment:** Realizing the friend's 'two cards, so fifty-fifty' is wrong because the red-red card has two ways to show red.
- **Biggest problem:** The paradox is delivered through ticket bookkeeping with a fiddly screen-and-cover protocol instead of through a game where children feel the 2-to-1 odds.
- **One change:** Play a betting game: one child always bets the hidden side matches, another bets it differs, over 20–30 rounds. Let the lopsided score raise the question, then use the tickets to explain it.

### Week 46: Two boards forget their starts (existing)

- **K–1, workable.** Two three-counter boards and 'set this slot to blue on both' is easy to do and check, and drawing instruction cards from a cup adds a game feel. Once a child sees 'fix each different slot' there is little left to find, so engagement may fade.
- **2–3, workable.** Which stories guarantee a match, and the contrast that shared toggles can never merge two boards, are nice ideas. The minute-to-minute work is applying instructions to two boards and comparing, with modest surprise.
- **4–5, workable.** The mixed-story criterion and the 'last visit decides' argument for uniform final boards are real reasoning. The probability problem over 16 color stories is abstract, and much of the activity is applying instruction lists.
- **Best moment:** Toggles can never make two different boards match, however many you use, while one 'set' instruction per slot always can.
- **Biggest problem:** The core idea (matching takes one instruction per differing slot) is nearly obvious, so the activity offers little surprise or struggle before it turns abstract.
- **One change:** Turn it into a challenge game: one player secretly sets up two boards and the other must write the shortest blind instruction list guaranteed to make any pair match, with toggles added as a 'trap' card.

### Week 47: Gentle-step landscapes (existing)

- **K–1, strong.** Placing counters as mountain heights with the 'no big jumps' rule is concrete, quick to check, and full of small puzzles (highest and lowest star, impossible clues). Making a two-clue puzzle for a friend is very appealing at this age, though an adult must read the prompts.
- **2–3, strong.** Constraint puzzles with counters, impossible clue sets, smallest and largest total heights, and designing puzzles with one or many solutions for a partner give lots of independent play and real 'why it can't work' reasoning.
- **4–5, workable.** The first four pages repeat the easier 2–3 tasks. The later envelope and fillability questions (P5–7) are meaty but are pure reasoning with no game, so some 10-year-olds will find the start too easy and the end too abstract.
- **Best moment:** Discovering that clues 0 and 3 only two steps apart can never be joined, and then stumping a partner with your own forced-landscape puzzle.
- **Biggest problem:** For grades 4–5 the shared opening is too easy and the general question arrives without a playful hook.
- **One change:** Give grades 4–5 a puzzle-design challenge (clues that force exactly one landscape on the seven-site board with the fewest clues) as the bridge into the envelope argument.

### Week 48: Inside and outside covers (area bounds) (existing)

- **K–1, weak.** Marking whole squares and laying tiles over the triangle is fine. But choosing refinements to remove the most tiles, redrawing the diamond so small cells become 'partly gray' while keeping big-cell status, and drawing shapes with set areas are precise, abstract tasks beyond most 5–6-year-olds.
- **2–3, workable.** Trapping an area between inside and cover counts is understandable, and the 'same markings, very different areas' question is a good twist. Most of the time is counting cells and converting small squares to big-square units, with little surprise.
- **4–5, workable.** Optimizing which three squares to split and explaining why refining never worsens the bounds are real thinking, and finding the exact area is a satisfying close. The activity is still count-heavy, and cutting 64 tiles per pair is a big preparation load.
- **Best moment:** Finding that refining the trapezoid shrinks its uncertainty from 12 to 3, not just in half, so it pays to split the right squares.
- **Biggest problem:** It is mostly careful cell counting and recording, with the interesting estimation ideas left implicit, and the tile prep is heavy.
- **One change:** Frame it as a contest: each team gets a budget of splits to make the tightest trap around a blob, then compare. Drop pre-cut tiles in favor of shading on large printed grids.

### Week 49: Four towers and differences (Ducci) (existing)

- **K–1, workable.** Finding the gap between two cube towers by matching is a lovely concrete move, and 'make a start that lasts long' is a clear goal. Rebuilding four towers on a second mat each round with up to 40 cubes is slow and error-prone for 5–6-year-olds, so the adult will manage the simultaneous update.
- **2–3, strong.** Diffy-square rings are a proven favorite: quick subtraction, a clear race to make the longest-lasting start, and the shock that three stations can cycle forever while four always die. Predecessor puzzles add a good 'impossible' twist.
- **4–5, strong.** Hunting for a 7-move start, then explaining through parity and doubling why every four-station ring must end, gives a full arc from play to proof that 10-year-olds can follow.
- **Best moment:** The three-station ring 1,0,0 never reaches zero and cycles forever, unlike every four-station ring.
- **Biggest problem:** For the youngest children, the two-mat cube rebuild each round is a slow simulation that an adult has to police.
- **One change:** Let K–1 work with heights 0–3 and number cards or one-row cube records, and let older children switch from cubes to written numbers as soon as the rule is clear.

### Week 50: Staircases and lengths (existing)

- **K–1, weak.** A 5-year-old has to bend string along every corner of a ruled staircase on a blank page and tape it there, then compare two strings. It is fiddly, and 'the straight diagonal is 200 mm' and 'fewest turns' mean little to them, so the adult ends up doing the string work while the child watches.
- **2–3, workable.** Adding 160+120 and seeing that a zig-zag hugging the diagonal is still 280 mm is a real surprise. But ruling staircases inside a 30 mm strip on an ungridded page is slow, and explaining why 8 turns is the minimum is beyond most of them.
- **4–5, workable.** The paradox (it looks like the diagonal yet stays 280, never 200) is a good 'wait, what?' and the leftward-path variant is nice. Much of the hour is careful ruler drawing in narrow strips, and the turn-minimum proof needs an adult to steer.
- **Best moment:** Measuring a tiny-step staircase that almost sits on the diagonal and finding its string is still exactly as long as the big L-shaped route.
- **Biggest problem:** The core action is precise pencil-and-ruler drawing on blank paper, plus string taped along small corners, so effort goes into drafting rather than into the idea.
- **One change:** Print a fine square grid inside the rectangle, or use pipe cleaners or snap-cube trains, so children can build ever-finer staircases quickly and spend their time on the surprise that the length never shrinks.

### Week 51: Honest measurement ranges (existing)

- **K–1, weak.** 'A hidden end can be anywhere in its gray band' is an abstract, adult-language idea. Juggling two range cards, a strip set and a target with guarantee words is more than a 5-year-old can hold, so the parent reads everything and in practice runs it.
- **2–3, weak.** Picking strips and adding them is doable, and 'break my promise' gives a little adversarial fun. But the tightest guaranteed range and the shared-versus-separate A are interval arithmetic dressed up in strips, with no moment an 8-year-old would gasp at.
- **4–5, workable.** Older children can run the beat-the-claim game and the widest-safe-card design, and the 'remove the very same A' cancellation is a real insight. It is dry, mostly verbal reasoning about bounds, with lots of reading per page.
- **Best moment:** A partner picks the most awkward allowed strips and breaks the other child's 'it always ends between 8 and 9' promise.
- **Biggest problem:** Guaranteed ranges and dependency are abstract ideas with no natural surprise, and the strips only illustrate addition, so it feels like careful worksheet logic rather than play.
- **One change:** Rebuild it as a two-player bluffing game, with a hidden length in a bag that you must promise a range for and the opponent tries to beat, and drop the formal tight-bound wording for younger bands.

### Week 52: Hinged frames and braces (existing)

- **K–1, workable.** Pushing a wobbly square, then feeling it lock when a diagonal goes in, is immediately satisfying for small hands. But they cannot open and close brass fasteners to move braces, so an adult swaps every bar, and the drawing they are asked to do is a weak record.
- **2–3, strong.** Testing designs on a 2-by-2 frame and hunting for the fewest braces is a hands-on puzzle with an instant physical check. The surprise that 'a brace in every row' can still wobble is very engaging.
- **4–5, workable.** The physical 2-by-3 work is great. The jump to row/column dots and connectivity is beautiful but is introduced through an adult-led handoff, and the later problems are paper-only claims about 4-by-5 grids that many children will not own.
- **Best moment:** A frame with a brace in every row and every column still flops sideways when pushed.
- **Biggest problem:** The kit (108 bars, 35 braces, 90 pin fasteners, an estimated 70-90 minutes of cutting and punching, unrehearsed) is far beyond a busy parent's 30 minutes, and every brace change needs fiddly pin work.
- **One change:** Use a ready-made kit or a quick build (craft sticks or straws with pipe cleaners, braces that clip on without unpinning) so children can move braces themselves and prep fits in 30 minutes.

### Week 53: Connecting networks (existing)

- **K–1, workable.** Buying roads with counters and checking a pawn can reach every town is a playful frame, and the three-town maps are small enough. 'Find every cheapest purchase' is beyond them, so the adult reads and steers, and the fun is mostly in paying and tracing.
- **2–3, strong.** Spending counters to connect towns is a game with a clear goal and a quick check. The trap (buying the three cheapest roads leaves D stranded) gives a real 'oh!' Children can play with 4-5 town maps on their own.
- **4–5, workable.** Swaps, must-buy and never-buy links, and designing prices for unique optima are genuine puzzles. But pages 6-9 become wordy proof questions (Problem 8 asks three things at once) that will lose some children.
- **Best moment:** Grabbing the three cheapest roads, then realizing the traveler can't get to D.
- **Biggest problem:** Most maps are small, so the younger tables run out of challenge quickly, while the upper pages swing to reading-heavy proofs about every/some/none.
- **One change:** Add one or two bigger, juicier maps (8-10 towns) for a beat-the-adult's-cost challenge between the small catalogs and the proof pages.

### Week 54: Partitions and rebuilding (existing)

- **K–1, workable.** Snapping cubes into strips and hearing 'that's the same as before' is approachable, and joining nine 1s down to an 8 and a 1 is satisfying. But deciding whether two collections are the same takes more than they can hold, the parent records everything, and there is no packet of their own.
- **2–3, workable.** Building all the collections of 4, 5 or 6 cubes is concrete. Finding that the odd-only and all-different lists come out the same length is a nice coincidence. Complete catalogs are bookkeeping, and an unsystematic 8-year-old will miss and repeat cases.
- **4–5, strong.** Join-pairs and halve-evens as a reversible machine that matches the two lists is a gorgeous, physical aha. The row/column flip on drawings gives a second surprise they can check themselves.
- **Best moment:** Splitting all the evens to odds, then joining equal pairs back, and watching exactly the starting collection reappear.
- **Biggest problem:** Complete enumeration of partitions carries the early pages, and it leans on systematic listing that younger children find tedious and error-prone.
- **One change:** Let a table pool their collections on movable cards (one partition per card) so the count comparison emerges from sorting rather than each child listing everything.

### Week 55: Few sums and equal spacing (existing)

- **K–1, weak.** Every move is an addition fact up to 18, and the parent supplies sums when counting is slow. The question 'how many different places?' is a counting chore with no visible payoff for a 5-year-old.
- **2–3, workable.** Third graders can add the pairs and enjoy trying to make as few or as many totals as possible. Minute to minute, though, it is checking all pairs and placing counters, essentially addition practice until the pattern appears.
- **4–5, workable.** Designing card sets for the fewest totals and predicting m+n-1 is a real conjecture hunt, and the grid route argument is elegant. It is bookkeeping-heavy, and the equality-case proof (Problem 10) is adult-level.
- **Best moment:** Discovering that 0,1,2 with 0,1,2 gives only 5 totals while scattered cards give 9, and that equal spacing is the trick.
- **Biggest problem:** The core action is exhaustively adding every pair and marking repeats, which feels like arithmetic drill before any surprise arrives.
- **One change:** Open with the design challenge as a two-team contest (fewest totals wins) using a pre-made addition table to read sums, so effort goes to choosing sets rather than computing.

### Week 56: Corners of a solid (existing)

- **K–1, workable.** Holding models, closing triangle fans into points versus flat, and seeing eight quarter-circle gaps make two whole circles are lovely concrete moments. But edge counting on a cube is error-prone, cutting gap copies is fiddly, and the parent does most of the recording.
- **2–3, workable.** Counting faces, edges and corners and making fans is engaging, and both totals coming out the same is a pleasant surprise. Filling the four-row V/E/F tables and the degree arithmetic is bookkeeping, and counting edges reliably is hard.
- **4–5, workable.** Euler's formula and the total gap of 720 degrees are genuine surprises across different solids, and the cube-subdivision tests are nice. Much of the time goes into tables, and the tree-reduction explanation needs heavy adult help.
- **Best moment:** Gathering the cut-out gaps from every corner of a cube and a tetrahedron and finding both piles make exactly two full circles.
- **Biggest problem:** Prep is enormous: 15 tabbed paper polyhedra (72 closing seams), about 90 polygon pieces and 36 gap circles. Children then spend much of the hour filling count tables.
- **One change:** Use magnetic tiles or Polydron (already suggested as an option) as the default, and cut the tables down to a few solids so the gap-circle surprise comes sooner.

### Week 57: Area from dots (Pick's theorem) (existing)

- **K–1, weak.** The side route is building four-square shapes and counting outline dots while the parent traces outlines. The 'always 10 dots except the square' pattern is fine, but it is mostly counting dots with no real hook for a 5-year-old.
- **2–3, workable.** Finding the area of slanted shapes with squares, halves and cut-and-move tricks is a good puzzle for third graders. Keeping I, B and area records gets tedious, and the rule hunt will need support.
- **4–5, workable.** Pick's rule is a classic discovery, and building area-6 shapes with different dot counts is satisfying. But a three-variable formula from scattered records is hard to spot unaided, and Problems 7-10 are proof and holes work for a return visit.
- **Best moment:** Two very different-looking shapes with the same inside and boundary dot counts turn out to have exactly the same area.
- **Biggest problem:** The discovery depends on many accurate I/B/area records, so the aha arrives late and only for children who keep careful tallies.
- **One change:** Hold one variable fixed (all shapes with I=0, then I=1) and pool records on a shared board, so the pattern pops out within 15 minutes.

### Week 58: Fair division (existing)

- **K–1, weak.** Children must value trays using someone else's assigned dot card ('A values red at 3') rather than their own wants, which 5-year-olds will not hold. The parent reads the cards, and 'nobody wants to trade' is judged by counting dots.
- **2–3, workable.** 'I divide, you choose' is instantly understood and fun. Role-playing fixed preference cards, completing the Problem 2 catalog and measuring cuts in mm make it feel more like an exercise than a game.
- **4–5, workable.** Envy-free versus proportional, and the three-person case where everyone is 'fair' yet everyone envies someone, are genuinely interesting. The definitions take careful reading, and Problems 4 and 7 are verbal proofs.
- **Best moment:** With whole cards someone always wants to trade, but cutting the third square in half suddenly makes everyone happy.
- **Biggest problem:** Fairness is judged from artificial preference cards instead of children's real tastes, which drains the natural emotional pull of 'that's not fair!'
- **One change:** Use real treats or stickers the children actually prefer differently (or let each child write their own preference card) for the cut-and-choose and envy checks.

### Week 59: Constant width (existing)

- **K–1, workable.** Spinning shapes between taped rails and sorting them into stuck, wobbly and snug is hands-on, and the curved triangle spinning snug like a circle is a real surprise. Keeping rails parallel and card pieces from riding over them needs adult help.
- **2–3, workable.** The rail-spin test in Problem 2 is great. Problem 1 asks for millimetre width measurements with two parallel edges held perpendicular, which is fiddly for 8-year-olds and slow before the surprise.
- **4–5, strong.** Finding a non-circle that rolls like a circle, building one with a compass, and discovering its center bobs while its width stays fixed are memorable and hands-on. The Problem 4 proof can wait.
- **Best moment:** The curved triangle turns all the way round between the rails, touching both sides the whole time, just like the disk.
- **Biggest problem:** The opening problem is precise width measurement with improvised parallel guides, so younger children may tire before the spin surprise. Prep is an estimated 60-90 minutes for stiff-card pieces.
- **One change:** Lead with the rail-spin test (and a book rolling on Reuleaux rollers) and make measurement a later check, with pieces cut from thick foam board so they cannot slip under the rulers.

### Week 60: Take it or pass (existing)

- **K–1, weak.** Rolling the die and saying take or pass is fun for a few rounds, but inventing a fixed rule and the forced last take are beyond them. The tower comparison of card rows is an adult procedure that children carry out.
- **2–3, workable.** Playing rounds with the die and counters is a real game, and comparing take and pass on the nine two-offer cards is within reach. The opening rules paragraph is dense, though, and scoring 27 cards twice each is a chore.
- **4–5, workable.** The core surprise is that you take a 4 with two offers left but pass it with three. Getting there means scoring 54 card lines and comparing averages like 134/27, so the aha comes late and through bookkeeping.
- **Best moment:** Finding that the same 4 should be taken with two offers left but passed with three.
- **Biggest problem:** After a few minutes of genuine game play, the activity turns into scoring long printed card lists, and the averages behind the insight are fractional.
- **One change:** Keep it a game. Pit two rules against each other in a class tournament of many quick rolled rounds tallied with cubes, and keep the exhaustive card scoring as a short pooled check at the end.

### Week 61: Triangles on a ball (existing)

- **K–1, weak.** Holding strings taut on a ball while a partner pins the endpoints is hard for 5-year-olds, and checking right angles on a curved surface with a paper tab is fiddly. The three-square-corner triangle is a real wow, but the adult will end up making it.
- **2–3, workable.** Problems 1–3 are hands-on, and the three-right-angle triangle is a genuine surprise. String handling and drawing back-side arcs on paper will need a lot of adult steadying.
- **4–5, workable.** Lune fractions (Problem 4) are accessible. The Girard route through lune pairs and an eight-region count table (Problems 5–7) is a long abstract bookkeeping exercise done on paper views rather than on the ball.
- **Best moment:** Building a triangle with three right-angle corners on the ball, after seeing it is impossible with straws on the table.
- **Biggest problem:** Prep is far beyond a busy parent: globes with meridians, calibrated references and an untested 60–90 minute setup. The string-on-ball handling is fiddly too.
- **One change:** Use cheap balls and rubber bands, or a marked globe, for one big Problem 2–3 investigation (three right angles, growing the N corner). Drop the lune-pair counting to an optional return visit.

### Week 62: Conflict networks (graph coloring) (existing)

- **K–1, workable.** Putting coloured counters on circles so that no line joins two of the same colour is a simple, checkable puzzle that young children can do. The slot-header-and-card layer and the reading need an adult.
- **2–3, strong.** Small colouring puzzles with a clear goal, a partner checker and a 'why can't fewer work?' question are absorbing at this age. Problems 1–3 and the tree on page 6 give good variety.
- **4–5, strong.** Finding the odd-cycle rule and making the greedy first-slot rule waste slots with a bad order are satisfying discoveries with puzzle feel. Problem 9's counting is heavier but optional.
- **Best moment:** Finding an order that makes the first-slot rule use four slots on a network that needs only two.
- **Biggest problem:** The card-under-header plus counter-on-circle double representation adds handling and setup overhead to what is really a colouring puzzle.
- **One change:** Drop the activity cards and slot headers and just colour circles with counters or crayons, keeping 'slots' as story language.

### Week 63: Cards away from home (derangements) (existing)

- **K–1, workable.** Placing A, B, C picture cards so that none sits on its own home, and seeing that exactly two at home is impossible, is doable and has a small aha. The nine-row A–D catalog depends on the adult writing everything.
- **2–3, workable.** Problems 1 and 3 are a reasonable systematic-listing challenge. The 'repair this student's count' overlap tasks are abstract and lean on the adult.
- **4–5, workable.** Inclusion–exclusion and the two-family recurrence are real mathematics. The minute-to-minute work is listing and pooling up to 44 five-letter rows and correcting other people's subtractions, which is mostly bookkeeping with little play.
- **Best moment:** Realising that with three or four cards you can never have exactly one card out of place.
- **Biggest problem:** There is no story or game to make 'nobody gets their own' matter, so the work is cataloguing permutations and fixing arithmetic.
- **One change:** Frame it as a gift swap or hat mix-up. Have children actually shuffle and deal many times and guess how often nobody gets their own before cataloguing.

### Week 64: Straight paths on an octagon surface (existing)

- **K–1, skip.** Ruled parallel lines across slanted glued edges with tick matching are far beyond K–1 motor and reading skills. The guide itself points to another week's packet as the real fallback.
- **2–3, weak.** The packet is labelled grades 3–5. Third graders can enjoy the Pac-Man wrap idea, but keeping a constant heading with a ruler across slanted edges and matching fractional tick positions will need constant adult rescue.
- **4–5, workable.** Older children can trace trips and compare lengths, and cutting out corner sectors to find three full turns is a lovely concrete surprise. Precise drawing and the dense rules paragraph slow everything down.
- **Best moment:** Fitting the eight cut-out octagon corners around one point and finding they make three full turns.
- **Biggest problem:** Most of the activity is precise ruler drawing and transfer across slanted edges, so accuracy and fine motor control rather than ideas decide success.
- **One change:** Start with the L-shaped square model, or a square torus on grid paper where paths follow grid lines, and bring in the octagon only for the corner-sector surprise.

### Week 65: Hyperbolic octagon streets (existing)

- **K–1, weak.** Moving a 10 mm arrow and choosing turns on the square grid is doable with an adult. The octagon and bending roads only make sense if you accept 'these are straight', which a 5-year-old can't use.
- **2–3, weak.** The robot walking is accessible, but the key facts (rooms the same size, curved streets are straight) are only asserted. Walking around an octagon taking eight left turns to get home is unsurprising, since it has eight corners.
- **4–5, workable.** The two parallels through P and the turn-count comparison (two octagons vs two squares) give older children something to reason about. It still rests on trusting the map rather than experiencing the curvature.
- **Best moment:** Finding two straight streets through P that both miss street R, which is impossible on flat paper.
- **Biggest problem:** The hyperbolic geometry is told rather than felt: children walk on a picture whose strangeness they must take on faith.
- **One change:** Have children tape paper right-angled octagons four to a corner and watch the surface ruffle and refuse to lie flat, then walk the streets on that model.

### Week 66: Lamplighter streets (existing)

- **K–1, weak.** Children can build the lamp pictures with counters, but writing move words and comparing fewest moves would be done by the adult. Signed positions and the two-part state are too much.
- **2–3, workable.** A clear fewest-moves puzzle with a walker and lamps suits third graders, and the partner roles help. Negative positions and small counters on 19 mm spacing need care.
- **4–5, strong.** Shortest-route puzzles with a convincing lower-bound argument are engaging. The dead-end twist, where every possible move makes the target easier to reach, is a genuine surprise.
- **Best moment:** Discovering that from the seven-move target, every single move L, R or F lands somewhere reachable in six.
- **Biggest problem:** Small counters on a printed strip plus written move words make the state easy to disturb and the work feel like transcription.
- **One change:** Play it on the floor: a taped number line, cups or cards as lamps, and a child as the walker, with the partner calling and counting moves.

### Week 67: Meeting on shortest roads (existing)

- **K–1, weak.** Checking whether a dot is on some shortest route for each of three pairs is too much to hold at once. The adult draws every route while children move counters.
- **2–3, workable.** Third graders can count steps and find the meeting dot on a grid with an adult. Testing one candidate against three pair conditions taxes working memory, and the payoff ('always exactly one') is quiet.
- **4–5, workable.** Finding the middle-row, middle-column rule, the triangle with no meeting point and the cube majority rule are good reasoning tasks. The checking routine is heavy and the activity lacks game energy.
- **Best moment:** Trying to place three homes so that no meeting dot works on the grid and failing every time, then finding the triangle map where none works.
- **Biggest problem:** Each candidate needs three simultaneous shortest-route checks drawn in three colours, so the effort goes into verification rather than discovery.
- **One change:** Make it a 'where should three friends meet so nobody walks out of their way' game on a big floor or table grid with walking tokens, and let the coordinate pattern emerge from several trials.

### Week 68: How many ways out (ends of graphs) (existing)

- **K–1, weak.** Placing blockers and tracing with a finger is doable. Closed roads, components and 'forever beyond the page' are subtle, and 6–8 mm blockers on 12 mm spacing are fiddly for small hands.
- **2–3, workable.** The line problems are almost too easy, but the ladder split (the diagonal pair works) and the tree doubling 3, 6, 12 give real puzzles. An adult helps keep the 'forever' idea straight.
- **4–5, strong.** Trying and failing to split the endless grid, then seeing why, and watching the tree's forever pieces double are satisfying puzzle-and-argument moments with a nice infinity flavour.
- **Best moment:** Discovering that no finite wall can cut the endless grid into two forever pieces, while a two-dot diagonal cuts the ladder.
- **Biggest problem:** The opening line problems have a trivial answer (always two), and the tiny blockers on dense dot maps are fiddly.
- **One change:** Open with the ladder challenge on a large board with big blockers, and save the line as a quick warm-up comparison.

### Week 69: Thin and fat road triangles (existing)

- **K–1, skip.** Gap distances between colored sides are far beyond K–1. The suggested strip-laying route is adult-run and has no payoff for them.
- **2–3, weak.** Drawing three shortest routes on trees is fine, but the gap definition (distance to the nearer of two other sides using any road) is a hard multi-part idea to check.
- **4–5, workable.** The tree fact (every road used by exactly two routes) and building ever-fatter grid triangles to beat a partner's number are nice. Measuring gaps correctly is effortful and error-prone.
- **Best moment:** Beating any number your partner names with a bigger grid triangle.
- **Biggest problem:** Measuring gaps is a slow, abstract definition to apply, so the work is careful distance checking rather than play.
- **One change:** Make Problem 4 a 'name a number, I'll beat it' duel from the start, using the corner construction on big grid paper, and keep gap measurement to one or two examples.

### Week 70: Shields in a portal room (existing)

- **K–1, skip.** There are no K-1 pages and no K-1 route. Wraparound edges, exact-point shields and unfolded room maps are far beyond a 5-year-old.
- **2–3, weak.** The guide's untested 15-20 minute route needs an adult to trace the drawn portal shots through their edges and then lay a ruler to far target copies. The children mostly watch and mark crosses.
- **4–5, weak.** Problem 1 (the fewest crosses to block six drawn shots) is a genuine small puzzle. After that, the core move is drawing long ruler lines to target copies and judging whether a pencil line passes exactly through a pencil cross, then carrying shields between copies with tracing paper. That is a precision-drawing chore where measuring error decides the outcome. The midpoint 'aha' needs coordinates and odd/even halving that most kids will only hear from the adult.
- **Best moment:** In Problem 1, seeing that the four corner-to-centre diagonals can't share a shield, so at least four are needed, and then fitting in the two forced shields.
- **Biggest problem:** Whether a shot gets through depends on exact point-on-line judgments across unfolded copies, so the game turns into careful ruler work and tracing-paper transfers instead of reasoning.
- **One change:** Use only lattice-point shields and shots drawn on a coarse grid (or string on a pegboard), so a hit is obvious at a glance. Turn Problem 3 into a quick blocker-versus-shooter game.

### Week 71: Can you hear the room? (billiard bounce words) (existing)

- **K–1, skip.** There is no K-1 material, and reflected-copy unfolding plus wall-letter words is far beyond this age.
- **2–3, skip.** The packet is Grades 4-5 only with no younger route. Holding ruler lines through reflected copies while reading letters in order is too much for most 7-year-olds.
- **4–5, workable.** Drawing straight shots through the printed grid of copies and reading off three-letter words is something a 10-year-old can do alone. ABA being impossible in the square but possible in the rhombus is a real surprise. The rhombus unfolding and mirror checks are fiddly, though, and the secret-room game needs impossibility arguments that kids will replace with 'I couldn't find one' unless the organizer steers. The all-words stretch proof is adult-led.
- **Best moment:** Discovering that a shot can go A, B, A in the pointy rhombus (it bounces straight back off B) when that seemed impossible in the square.
- **Biggest problem:** Past Problem 1, progress depends on precise rhombus constructions, mirror alignment and proofs of impossibility. These stall children and push the adult into constructing shots.
- **One change:** Supply pre-drawn rhombus unfoldings with a few candidate shots to check, and play the secret-room guessing game only with already-checked words, so the game runs without new constructions.

### Week 72: A robot that remembers (signed area) (existing)

- **K–1, skip.** There is no K-1 route, and adding column numbers to a separate memory strip is beyond this age.
- **2–3, skip.** The packet is Grades 4-5 only. From Problem 2 on it needs adding and subtracting negative column numbers on a signed strip, which most 7-year-olds can't do yet.
- **4–5, workable.** The card routes in Problem 1 are concrete and finishable, and 'same place, different memory' is a nice surprise that links to counting squares left of the route. Kids juggle a robot counter, a move-card sequence and a memory marker with signed arithmetic, so one partner is mostly doing bookkeeping. Negative columns will need repeated adult help.
- **Best moment:** Realising that a route's memory is just the number of squares on one side of it, so a loop remembers its area.
- **Biggest problem:** Running three parallel records (position, card order, signed memory) makes the minute-to-minute activity bookkeeping, and the signed steps invite errors that hide the pattern.
- **One change:** Let children shade the squares left of the route as their 'memory' from the start, and bring in the strip and negative columns only after the area idea lands.

### Week 73: The gentlest stretch (rectangle to square) (existing)

- **K–1, skip.** There is nothing for K-1. Ratios of distances and whole-sheet maps don't fit this age.
- **2–3, skip.** The guide says there is no Grades 2-3 route. Stretch ratios and homeomorphism-style rules are out of reach.
- **4–5, weak.** The concrete part is ruler-and-paper-strip measuring of many dot pairs, where the key differences are below a millimetre (the guide admits this). The intended discoveries (every placement ties, the midpoint tests single out the centre, any legal map stretches some pair by 2) come from adult arguments, not from anything children can see. Inventing a 'rule for every point' is very abstract for a 10-year-old.
- **Best moment:** Noticing that the pair A-D always doubles no matter where O goes, so the score can never beat 2.
- **Biggest problem:** The hands-on activity is tedious measuring that can't reveal the intended distinctions, so the real mathematics stays with the adult.
- **One change:** Rebuild it around physically stretching a gridded rubber sheet or elastic onto the square and comparing a few dramatic pairs, and drop the near-centre midpoint precision task.

### Week 74: Doubling elevators (existing)

- **K–1, weak.** The adult-led route has a 5-year-old move a marker along tiny 5.8 mm dot spacings while the adult tallies, and the payoff is one-move savings (6 versus 5). There is a seed of 'going up is faster', but the adult carries the counting.
- **2–3, workable.** Problem 1 and target 8 need only adding 1, 2 and 4, and finding a shorter route than a partner is motivating. The small dots and the stride-strip procedure need adult steadying, but children make the real choices.
- **4–5, strong.** It's a clear game with a goal (fewest moves) and a challenge-your-partner structure, and the elevator shortcut and stepping past 23 and back are genuine surprises. Problems 3-4 turn naturally into 'can anyone beat 8?' arguments. The strip handling and small dot spacing are the main friction.
- **Best moment:** Finding that the fastest way to 23 is to go to 24 and step back left, beating every route that only moves right.
- **Biggest problem:** Dots 5.8 mm apart and a ruler-like stride strip make each move fiddly, which slows the game and invites miscounts.
- **One change:** Print a larger board where the higher levels have marked landing spots (or use a floor or number-line version with tape), so moves are instant and kids can focus on route choices.

### Week 75: Twists on a cylinder (winding) (existing)

- **K–1, skip.** There is no K-1 route. Signed seam crossings and fixed-endpoint yarn routes on a tube are beyond this age.
- **2–3, skip.** The packet is Grades 4-5 only, with signed counting, repeated-strip lifts and twist words, and there is no younger entry.
- **4–5, workable.** Wrapping yarn around a taped paper tube and counting signed seam crossings is tactile, and a 10-year-old can do it. The crossing puzzle in Problem 6 has a satisfying hidden rule. The guide admits the yarn slides toward a helix and won't hold a route, and the twist operation (shifting points by fractional turns per height) is a drawing chore. Twist words reduce to counting plus and minus signs, which is too easy.
- **Best moment:** Finding that two yarns with windings 0 and 3 can't avoid crossing twice, however you lay them, and then guessing the rule for 2 and 7.
- **Biggest problem:** The physical yarn routes are hard to hold in place on a paper tube, so the concrete model may fight the children exactly when they need it.
- **One change:** Use a cardboard tube with pegs or pins at A and B and a few anchor pins up the sides so yarn routes stay put, and cut Problems 4-5 down to a quick oral question.

### Week 76: Substitution strips (Thue-Morse) (existing)

- **K–1, workable.** With a parent reading, a 5-year-old can place AB under A and BA under B with big tiles and watch the row double. 'Can three of the same sit together?' is a question they can check by looking. The proofs and crops are beyond them, and the adult paces it.
- **2–3, workable.** Growing to 16 tiles, finding triples and spotting forged whole rows by undoing pairs suit third graders (the packet says 3-5). Second graders may find the 16-tile build and the reading load tiring. Crops and Problems 5-7 are beyond most.
- **4–5, strong.** Tiles keep it hands-on, and the forgery-detection framing (which rows were really grown? find the hidden seam) is a detective game with clear verdicts. The equal-neighbour seam trick is an aha kids can find themselves. Problem 7's proof needs adult support, but the first four problems carry a session.
- **Best moment:** Unmasking a fake row because undoing it leaves a pair like BB or AA, which no tile could have made.
- **Biggest problem:** Building and rebuilding long tile rows takes table space and time, and the crop and pairing rules in Problems 4-6 add enough conventions that some children lose the thread.
- **One change:** Supply pre-built 8- and 16-tile 'suspect' strips on card so children spend their time detecting and arguing, not re-laying tiles.

### Week 77: Persistent holes (existing)

- **K–1, weak.** In the adult-led route, the child lays strips and covers triangles while the adult reads and records. 'Is every triangle inside covered?' is easy, but there's nothing to puzzle over, and the saved-loop idea is invisible at this age.
- **2–3, weak.** The same adult-led route plus the DA-versus-AC ordering question. Children place pieces, but keeping a saved loop separate from the growing board and following stage schedules is adult-run.
- **4–5, weak.** The pieces are concrete, but the minute-to-minute work is copying edge tokens, cancelling pairs and replaying four-stage schedules under many rules (saved lists unchanged, batches, legal fillings). The interesting contrast (hole counts identical, loop lifetimes differ) arrives late and needs adult interpretation. Few 10-year-olds would ask to play again.
- **Best moment:** Seeing that one tile kills the triangle loop but the outer square loop survives either single tile and needs both.
- **Biggest problem:** Rules and token bookkeeping dominate, so children spend their time running a procedure the adult has to police instead of exploring holes.
- **One change:** Cut to the square and joined boards with a physical 'pour water in the loop' framing (does the filled region seal the rim?), and drop the token cancellation and stage cards.

### Week 78: Three-armed lines (tropical geometry) (existing)

- **K–1, weak.** The adult-led route has children slide a traced shape without turning it to touch dots. That's a small physical game, but with little to discover at 5, and keeping the shape unrotated is uncertain.
- **2–3, weak.** The same adult-led slide-the-shape route on two boards. Children can find 'one place' versus 'lots of places', but the adult reads everything and the session is short and thin.
- **4–5, workable.** Drawing three-armed lines from chosen junctions with a traced template is concrete, and 'these lines always meet, sometimes along a whole ray' is a real surprise against ordinary parallel lines. Problems 1-2 and 4 work independently. The 'least number is tied' definition and the general rules in 3, 6 and 7 lean on the adult's rectangle proof.
- **Best moment:** Trying hard to make two three-armed lines miss each other and discovering they never can.
- **Biggest problem:** The min-of-three definition up front is abstract and adds reading, and the general-rule problems turn into adult proof talk.
- **One change:** Launch purely with the tracing-paper shape as the definition and frame Problem 6 as a challenge: 'make two lines that never meet; your partner wins if they cross'.

### Week 79: Numbered-ball detectives (Ross-Littlewood) (existing)

- **K–1, weak.** There are no K-1 pages. In the adult-run route the child finds and moves the smallest card, which is doable, but it's a repetitive simulation with no surprise at this age.
- **2–3, workable.** Cards in bowls are concrete, and predicting card 20's days without running 20 days is a satisfying pattern find. Problem 4's choose-the-moves puzzle with an impossible row is a real challenge. The first problems are a repetitive enactment that can drag.
- **4–5, workable.** The simulations go quickly for 10-year-olds. Problem 5's paradox (every card eventually leaves A, yet A keeps growing) can produce a real 'whoa', but it's phrased abstractly and needs a skilled adult to land. Problem 4's stuck day is a good proof-of-impossibility moment.
- **Best moment:** Realising that every card eventually moves to B, yet bowl A holds more cards every day, and that under the other rule half the cards stay in A forever.
- **Biggest problem:** Problems 1-3 are rote day-by-day card moving before the interesting questions arrive, so some children tire before the paradox.
- **One change:** Shorten the enactment to three or four days, jump to the 'predict card 20' and 'when is A empty?' questions, and stage the paradox as a debate.

### Week 80: Midnight laboratory (lamp paradox) (existing)

- **K–1, weak.** The adult folds the strip and tells the story; the child only flips a card four times and says ON or OFF. 'Will there ever be a last fold?' is a nice question, but it gets a one-word answer and then the activity is over.
- **2–3, weak.** The hands-on part is four folds and four card flips, which takes about five minutes. After that it is talk about something nobody can do, and Problem 3 ('make up a rule that settles') needs abstract rule-writing, which these children will need an adult to scribe and steer.
- **4–5, workable.** Ten-year-olds can enjoy arguing about whether the light is on or off at midnight, and the halfway counter against the flipping card is a good contrast. But Problems 4-6 are worded as philosophy ('What, if anything, does the switching rule alone tell you'), and the discussion lives or dies on how well the adult runs it.
- **Best moment:** Children who were sure the light ends ON or ends OFF realize there is no last switch to decide it.
- **Biggest problem:** There is almost no concrete action: after a few folds and flips, the session is an abstract endpoint debate.
- **One change:** Make it a commit-and-defend debate game: each child bets ON or OFF at midnight and tries to convince the others, and pair it with a physical Zeno walk toward a wall to set up the contrast with the counter that converges.

### Week 81: Buckets of Fish (existing)

- **K–1, weak.** Five-year-olds can move counters in the simplified two-bucket game, but sorting nine cards by who can force a win is game-tree analysis. In practice the adult works out the answers while the children play aimless short games.
- **2–3, workable.** The capped game is quick to play with real counters, and partners can check each other's moves. The 'strictly left, at most one per bucket' rule takes practice, and deciding forced wins across 16 cards is heavy, so most pairs will play rather than analyse. Parity is unlikely to be found without hints.
- **4–5, strong.** 'Make the game last 10, then 30, then 100 moves' and 'can you make it go forever?' are hooks children push hard on. Realizing that one big refill makes the game as long as you like, yet it still always ends, is a real surprise, and the argument from the rightmost bucket is within reach with counters.
- **Best moment:** Finding that one huge refill makes the game as long as you want, then failing every attempt to make it last forever.
- **Biggest problem:** The capped game the younger bands get is the less surprising half; the delightful 'arbitrarily long but always finite' twist is reserved for 4-5.
- **One change:** Give grades 2-3 a small-number version of the 'make it last as long as you can / can it go forever?' challenge, instead of the 16-card forced-win sort.

### Week 82: Endless class lines (ordinals) (existing)

- **K–1, weak.** The adult-led route matches three red cards to three blue cards with yarn and finds six ways, which is fine finite matching. It has nothing to do with the endless lines, and 'which way has no crossing' runs out quickly.
- **2–3, weak.** The packet is labelled grades 3-5 and is reading-heavy. Children have to accept 'numbers continue forever' arrows and the 'after EVERY kid' panels as rules, and grasp the definition of 'keeps order'. Most 7-8-year-olds will hand the thinking to the adult once the lines become endless.
- **4–5, workable.** The star in front getting absorbed by everyone shifting one place is a Hilbert-hotel surprise that 10-year-olds enjoy, and contrasting it with a star at the very end is a real 'aha'. But the cards are only a schematic of infinite lines, Problem 3 and especially the open Problem 4 arrangements are abstract, and a strong adult is needed.
- **Best moment:** Everyone shuffles over one place and the extra star kid gets a partner after all; then the star at the end can't be fitted in that way.
- **Biggest problem:** After the finite warm-up there is no real concrete action: matching endless lines is reasoning about a drawing with an arrow, and the distinction between size and order is subtle.
- **One change:** Act it out with the children as a 'class line' that can't really end (an adult's 'and so on' card at the end), and cut Problem 4 to one guided pair of arrangements.

### Week 83: Hackenbush balances (existing)

- **K–1, workable.** Pulling cubes off snap-cube towers, so that everything above comes away, is satisfying and needs no reading. One-colour towers make the rule 'more cubes wins' findable. Keeping turns and starters straight needs an adult, but the children make every move.
- **2–3, workable.** The cube towers make the cut rule self-enforcing and the games are short and fun. Judging whether a board 'balances' needs best play from both starters, which 7-8-year-olds will often get wrong, so their conclusions may rest on lucky games unless an adult challenges them.
- **4–5, strong.** Playing to beat a partner, then discovering that two blue-red stalks exactly cancel one red cube (a stalk 'worth a half') and that two BR do not balance RB, is a genuine surprise. Building their own balanced boards is a creative follow-up. The surreal 'nursery' is optional and rightly deferred.
- **Best moment:** Realizing that two little blue-red towers exactly balance one red cube: a tower can be worth half.
- **Biggest problem:** Finding a balance needs near-optimal play from both starters, and younger children will judge from lucky games.
- **One change:** Give each board a referee child whose job is to find a better reply for the losing side, so that 'balances' is tested rather than inferred from one game.

### Week 84: Public knowledge (logic cafe and headbands) (existing)

- **K–1, weak.** Five-year-olds can say NO or NOT YET from their own card, but the point is reasoning about what others' answers reveal. That second-order inference is beyond most of them, so the adult does the reasoning.
- **2–3, weak.** This means keeping eight deal cards for possible worlds, tracking what each person privately knows, and following simultaneous-reveal rules about what may be removed when. That is too many rules and too much perspective-taking; the adult will end up making each elimination.
- **4–5, workable.** The cafe joke (the 'NOT YET' that proves YES) is a real click for 10-year-olds, and seeing the two blue dolls both prove blue in round 2 is a striking moment. The headband induction is fragile even for adults, though, and the card-elimination protocol is fussy, so only the quickest groups with a skilled adult will get there themselves.
- **Best moment:** The cafe: person 1's 'not yet' suddenly tells everyone that person 1 wants a cup.
- **Biggest problem:** The possible-worlds card protocol and the private-versus-public bookkeeping are so heavy that the adult, not the child, will usually be doing the inference.
- **One change:** Build the session around acting out the three-person cafe with real children holding hidden cards, and keep the headband induction as a short adult-led finale for 4-5.

### Week 85: Drawing machines (pantograph) (existing)

- **K–1, weak.** This is a one-child-at-a-time station with an adult steadying the machine, so the others wait. Steering T while watching P is hard fine-motor and attention work for 5-year-olds; they will enjoy seeing a big copy appear, but briefly.
- **2–3, workable.** If the machine works, tracing a shape and watching the other pencil draw it twice as big is genuinely magical, and steering P to the dots is a good puzzle. But the foam-board linkage has never been built. Prep is well over 30 minutes (craft-knife cutting, rehearsal), and wobbly joints can ruin the copies.
- **4–5, workable.** The doubled-length, four-times-area surprise with unit squares is a good aha, and reversing the machine or moving the anchor gives real questions. All of it depends on hardware that is fiddly and untested, and the bar-vector explanation in Upper Problem 1 is abstract.
- **Best moment:** Tracing a small house with one pencil and watching the other pencil draw a big house by itself.
- **Biggest problem:** It depends on a homemade linkage that has never been built, needs an hour or more of adult prep and rehearsal, and may wobble too much to give clean copies.
- **One change:** Buy one or two inexpensive commercial drawing pantographs and write the problems for those, rather than relying on an untested foam-board build.

### Week 86: Pursuit and escape (cops and robbers on graphs) (existing)

- **K–1, workable.** A chase game where you move one dot or stay is simple and appealing, and the triangle versus square contrast is visible. 5-year-olds may lose track of turns and stays, so the adult must manage the turn tile, but the children make the moves.
- **2–3, strong.** Chase games are instantly engaging, and the rules are tiny. Discovering that the cop always wins on paths and trees but the robber can run around a square forever is a real 'aha' they can find and demonstrate to a partner.
- **4–5, strong.** Beyond the chase, adding the fewest roads to trap the robber, designing a cop-win and a robber-win map, and coordinating two cops are puzzles 10-year-olds will want to keep testing against each other. Folding is a harder optional step.
- **Best moment:** The robber discovers it can circle the square forever, always staying opposite the cop.
- **Biggest problem:** Children will be tempted to take a long game as proof of escape; the 'works against every reply' standard needs adult questioning.
- **One change:** Start with a big floor-sized version (a path and a square of paper dots) where children are the cop and robber, before moving to tabletop boards.

### Week 87: Voting and agendas (existing)

- **K–1, weak.** The adult reads every ranking card aloud and the children place tokens and count to three. The voters are imaginary and the cycle is abstract, so the children are mostly operating an adult's procedure.
- **2–3, workable.** 'Make A win, now make B win, now C' is a good rigging challenge with a nice surprise: whoever waits wins. But voting on behalf of three imaginary cards, one pair at a time, is procedural, and the line packet's distance comparisons are beyond many of them.
- **4–5, workable.** Rigging the agenda and designing profiles where the order matters is a creative puzzle with a real twist. The line packet (five voters, comparing distances for many proposals) turns into tally bookkeeping before the median insight arrives. Upper Problem 2's impossibility argument is good but needs adult guidance.
- **Best moment:** Finding that whichever letter is made to wait wins the knockout, with the same voters and no one changing their mind.
- **Biggest problem:** The voters are imaginary cards, which drains the fun out of rigging an election and makes each vote a lookup chore.
- **One change:** Use the children's own real three-way preferences (snacks or games) for the cycle, and let one child secretly choose the agenda to 'rig' the outcome.

### Week 88: Packing and kissing circles (existing)

- **K–1, workable.** 'How many disks can touch this one?' is a perfect kindergarten question: they build it, count six, and can try a bigger middle disk. Sliding disks into a snug ring takes some motor care, and the later problems are well beyond them.
- **2–3, strong.** There is lots of hands-on building with a clear goal: it is always six around an equal disk, nine around a bigger one, only four big ones around a small one. Squeezing an extra disk into the tray by staggering rows is a tangible 'aha'.
- **4–5, strong.** Moving from building to proving (equilateral wedges show why a seventh can't fit, and why the neighbours must all touch) is a satisfying, concrete proof. The mixed-size rings and the general rule give real depth for return visits.
- **Best moment:** The staggered rows let eleven disks into a tray that held only eight in a square grid.
- **Biggest problem:** Preparation: about 95 card disks to cut (roughly 1.5 hours), and cutting errors of under a millimetre can make the tight tray problems give the wrong answer.
- **One change:** Use bought equal-size disks or coins (pennies and quarters, say) and resize the trays to match, so prep is minutes and the fits are exact.

### Week 89: Growing shapes and totals (differences and accumulators) (existing)

- **K–1, workable.** Growing squares and stairs with tiles and counting the new tiles suits 5-year-olds with an adult counting along. The tray and counter machines are mostly adult-operated, but the cube growth is fun.
- **2–3, workable.** The tile problems are strong: two staircases click into a rectangle, and a square peels into odd layers. The one-tray input problems are fine. The two-stage cascade is a step-by-step simulation where copying totals between trays becomes the main demand.
- **4–5, workable.** Maximizing the second tray by ordering inputs is an interesting puzzle, and the cube shells and corner piles are good hands-on encores. But much of the minute-to-minute work is running cascaded totals, and the 20-problem, 11-page packet sprawls.
- **Best moment:** Two copies of a staircase fit together into a perfect rectangle.
- **Biggest problem:** The accumulator machines turn into simulation and bookkeeping (keep, copy, add, repeat) that crowds out the delightful shape work.
- **One change:** Split it: make the tile and cube growing shapes the main week, and replace the cascade machines with a single puzzle such as 'order these cards for the biggest final total'.

### Week 90: Sliding number arrays (jeu de taquin) (existing)

- **K–1, skip.** No K-1 packet; the adult-read A-board route asks five-year-olds to track gray, dark and ring pieces plus a smaller-neighbor rule, and the only payoff is sorting finished shapes into two piles.
- **2–3, weak.** The single slide move (compare two neighbors, slide the smaller) is doable, but children juggle three mask types, a ring, reset cards and saved sketches, and the headline discovery is that nothing changes when you switch corners, which feels like a non-event at this age.
- **4–5, workable.** Upper children can run slides, design starts for target outlines (Problem 4 is the liveliest task) and argue order is preserved, but the 16-card catalog with two runs each is a long pooled simulation, and the order-independence theorem only lands if an adult frames it as surprising.
- **Best moment:** Problem 4: arranging 1-5 so the slide produces a chosen target outline, then testing it.
- **Biggest problem:** Most of the time goes on executing a multi-piece sliding procedure and resetting from cards, and the payoff is a confirmation that the result is the same both ways rather than a surprise children can feel.
- **One change:** Cut to one-hole A and D boards plus the design-a-start challenge, drop the dark/gray distinction where possible, and make the 'does the choice matter?' question a bet children commit to before running both orders.

### Week 91: Rotor-router machines (existing)

- **K–1, workable.** Pushing a counter along arrows and flipping cards is a hands-on, marble-run-like action five-year-olds can do, and 'does every exit get one?' is answerable by looking; an adult must read and keep the flip discipline, and 12 counters on one switch gets repetitive.
- **2–3, workable.** Operating the four-exit tree and programming it to hit target orders (and finding ones it can't make) is a real puzzle with a mild aha, but Problem 1's twelve-counter XYXY run is dull and writing arrival strings adds bookkeeping.
- **4–5, strong.** Programming the eight-exit tree, discovering bit-reversal order, spotting impossible orders and counting 128 programs gives upper children a machine they can both play with and reason about; 'every exit gets one before any gets two, whatever the start' is a satisfying surprise.
- **Best moment:** Discovering that four (or eight) counters always land on every exit exactly once no matter how the arrows start.
- **Biggest problem:** Preparation (cutting, folding and gluing 33 reversible cards, estimated at an hour) exceeds what a busy parent will do, and a missed flip silently corrupts every later result.
- **One change:** Replace fold-and-glue cards with something faster to make (coins or two-color counters as switch states) and shorten Problem 1 to four or six counters before moving to the tree.

### Week 92: Fold-and-stretch predictions (tent map) (existing)

- **K–1, weak.** Folding the track at 8 to see which numbers touch is a nice concrete moment, but hopping by counting the gap to the nearer end and laying it twice is a demanding procedure for five-year-olds and the adult will be operating it.
- **2–3, weak.** Point moves are a chain of measure-then-double steps read from a graph, and shading 'all possible positions' of a band is an abstraction most seven- and eight-year-olds won't hold; it becomes procedure-following with little visible payoff.
- **4–5, workable.** Children who can halve repeatedly can find markers that meet, bands that grow, and the 'how close must you start to stay predictable?' question, which carries real chaos ideas, but the work is pencil shading on number lines with no physical stretching and little play.
- **Best moment:** Folding the track and seeing 3 and 13 land on top of each other, so they go to the same place next move.
- **Biggest problem:** After the fold, the activity is repeated map-reading and shading of intervals; the striking idea (tiny differences blow up) is delivered as interval bookkeeping rather than a race children can watch.
- **One change:** Turn it into a two-marker race game where partners start close together and bet how many moves until they are far apart, saving band shading for upper return visits.

### Week 93: Squaring a rectangle (Babylonian square roots) (existing)

- **K–1, weak.** Only an adult-led side route: making every rectangle from 12 tiles is a decent K-1 task, but it is not what the week is about and the rest has nothing for this age.
- **2–3, weak.** Tile rectangles of 24 and the cut-and-fit squares work for some third graders, but the reshaping move needs division into fractions (3/2, 24/7) and comparing them, which second graders can't do and most third graders will need an adult to compute.
- **4–5, workable.** Tiles, cutting rectangles to fit inside a square, and watching the bracket close on the side of a 12-square are satisfying, but Problems 3-5 become fraction arithmetic (336/97) and decimal checking that many ten-year-olds will find a chore.
- **Best moment:** Cutting the 6-by-2 rectangle, fitting it into the 4-by-4 square and seeing exactly one small square left uncovered.
- **Biggest problem:** The engaging physical part ends after Problem 2; the convergence story runs on fraction calculations that slow children down and hide the idea.
- **One change:** Keep the reshaping on whole-number or tile-countable examples longer and let a calculator do the fraction steps so children focus on watching the bracket shrink.

### Week 94: Calibration lab (secret-extra machines) (existing)

- **K–1, workable.** Measuring strips on a ruler that doesn't start at 0 and playing a hidden 'adds 1, 2 or 3 cubes' tower machine behind a folder are concrete and game-like; Problems 5-6 (every pair that could have gone in) will need an adult to steer.
- **2–3, workable.** Being the secret machine is fun, but one known strip gives the extra away by subtraction, so the guessing game is over in one request; the 'could P be longer than Q?' and repair-the-box puzzles have some bite.
- **4–5, workable.** The copies-plus-extra game makes 'how few requests?' a real strategy puzzle, but the later stretch-and-shift and error-range pages (Problems 3-7) are linear-function word problems with fractions that feel like schoolwork.
- **Best moment:** Lifting the folder to check whether the partner guessed the machine's secret extra.
- **Biggest problem:** For the middle band the game is trivially solved by one subtraction, and the upper band's interesting game quickly gives way to abstract slope-and-error problems.
- **One change:** Give the middle band machines where one request is not enough (e.g. the copies-and-extra machine with small numbers) so the guessing game stays a strategy puzzle.

### Week 95: Count the unseen (capture-recapture) (existing)

- **K–1, skip.** No packet; the 15-minute adult-led route is a one-question demonstration, not a session.
- **2–3, workable.** Catching, marking and recatching counters to guess a hidden total has a game feel and kids will enjoy the reveal, but overlaps with catches of 4 are noisy, so guesses feel like luck, and the 'smallest possible bag' puzzles are dry next to it.
- **4–5, workable.** The proportion rule gives older children a real estimation method and the 'no matching total when overlap is 0' surprise is good, but Problems 6-8 on expected overlap and budgets are formula-driven and the erasable-mark materials are fiddly.
- **Best moment:** The keeper revealing the hidden total right after children commit to a guess from their overlap.
- **Biggest problem:** With small catches the overlap jumps around, so children may conclude the method is just guessing before they ever see why it works.
- **One change:** Pool every pair's rounds on one shared board so children see the guesses cluster around the true total before tackling the exact-bound puzzles.

### Week 96: Prime bags (factorization and divisors) (existing)

- **K–1, weak.** Only an adult-led route: building counter rectangles for 2 to 20 and sorting 'only one row' numbers is a reasonable activity for older first graders, but long for five-year-olds and not the week's material.
- **2–3, workable.** Third graders who know multiplication facts can split cards into prime tokens and list sub-bag values, and Problem 4's build-a-bag puzzle is a nice design task; second graders without fluent multiplication will depend on an adult or a times table.
- **4–5, workable.** Divisor counting, token patterns and 'least number with 12 divisors' are a solid puzzle sequence, but it reads close to accelerated school number theory and the moment-to-moment work is listing and multiplying.
- **Best moment:** Finding that 60 has more divisors than 64, or hunting for the smallest number with exactly 12 divisors.
- **Biggest problem:** The activity is mostly listing factors and products on paper, so it can feel like a worksheet rather than an investigation.
- **One change:** Frame the upper band as a contest to find the smallest number with N divisors, with a class record board, and open with that challenge rather than with routine factor trees.

### Week 97: Square remainders (quadratic residues) (existing)

- **K–1, skip.** The adult-led route is building squares and grouping by 3s or 4s to see leftovers; there is little for five-year-olds to decide and nothing for them to discover.
- **2–3, weak.** Only third graders are in range, and after the first few squares the work becomes dividing 36, 49, 64 by 7, 8, 9 to find remainders, which is arithmetic drill with an adult helping.
- **4–5, workable.** The secret-input partner game gives a little play and the pairing pattern for prime bundle sizes is a real discovery, but most of the time is computing remainders of printed squares and filling collections.
- **Best moment:** In the partner game, realizing an output always hides exactly two inputs with bundles of 7, except 0.
- **Biggest problem:** The concrete counter-square stage is short; the rest is remainder computation that crowds out the pattern-spotting.
- **One change:** Supply a remainder strip or wheel so children read outputs instantly and spend their time on the hiding game and on comparing prime versus composite bundle sizes.

### Week 98: Growing from a few seeds (bootstrap percolation) (existing)

- **K–1, workable.** Put counters down and add one wherever two neighbors are filled is a single rule five-year-olds can follow with a partner pointing, and 'did it fill or get stuck?' is visible; holding 'side not corner' and searching for fewer seeds will need adult help.
- **2–3, strong.** Designing a few seeds that fill the board, watching it spread, and chasing the fewest seeds is a self-checking puzzle children replay; the different-order question gives a gentle surprise.
- **4–5, strong.** The search for fewest seeds on 4x4, 5x5 and 10x10, then the perimeter-never-grows argument, is a classic aha that ten-year-olds can actually see with counters and edge counts.
- **Best moment:** Realizing the outline of the filled region never gets longer, which is why you can never fill an n-by-n board with fewer than n seeds.
- **Biggest problem:** Marking seeds and additions on small paper boards and redrawing for each attempt can slow the search, especially on 10x10.
- **One change:** Provide a big reusable grid and two colors of counters for all the searching, keeping drawing only for a final record of a best start.

### Week 99: Moving piles (least work / earth mover's distance) (existing)

- **K–1, weak.** Adult-led route only: moving two or three counters along bins and counting steps is doable, but the adult sets every start and target and counts aloud, and there is little decision-making for the child.
- **2–3, workable.** Matching a target with fewest moves is a clear puzzle and finding that 'shortest delivery first' can lose is a good surprise, but small cases are fairly obvious and writing each move adds recording.
- **4–5, workable.** The 'what must cross this gap?' lower-bound idea, the star-road version and the triangle-inequality question give real reasoning, though the activity is quieter and less playful than a game.
- **Best moment:** Showing that the greedy shortest-delivery-first plan costs 6 when a smarter plan costs 4.
- **Biggest problem:** For small piles the best plan is often obvious, so much of the time is counting and writing moves rather than puzzling.
- **One change:** Lead with the greedy-fails challenge and the partner game of building a start exactly N moves away, and drop the requirement to write each move.

### Week 100: Distance in nested worlds (ultrametric / 2-adic) (existing)

- **K–1, skip.** No packet; the 15-minute close/far loop route is a brief adult-led aside, not a session for this age.
- **2–3, weak.** Only third graders are in range, and the definition (smallest common group's label, labels increasing outward) is a dense paragraph to retain before any building; most will need an adult to decide each distance.
- **4–5, workable.** Building loop worlds with cord and testing which distance triples are possible is concrete, and the hidden-world guessing game (Problem 10) is genuinely game-like, but the reading load is high and the ball and 2-adic pages are abstract.
- **Best moment:** Problem 10: reconstructing a partner's secret world from as few distance questions as possible.
- **Biggest problem:** Children must absorb an unfamiliar, wordy distance definition before doing anything, and the surprising 'isosceles only' fact comes late.
- **One change:** Open with the secret-world game on three or four cards and a simple close/far/very-far vocabulary, letting the triangle surprise emerge from play before introducing balls.

### Week 101: Bead machines and the odd triangle (draft)

- **K–1, workable.** The same/different colour rule is a two-cell binary choice a 5-year-old can apply, and triangles appearing is a real reveal; but one wrong cell spoils every row below it, so an adult has to check each row, and 36 small hexagon cells take patience. Coin-flip beads with stacking cubes are fine but light.
- **2–3, workable.** Watching triangles inside triangles grow over 16 rows is genuinely satisfying and counting red cells per row gives a pattern to chase, but 136 cells is a long fill where errors spread, and the pooled 32-bead comparison is mostly waiting and tallying.
- **4–5, workable.** Matching the colour picture to odd entries and predicting row 13 from binary is a real aha, but filling numbered Pascal to row 15 means adding numbers into the thousands, which turns the first 20 minutes into arithmetic chore.
- **Best moment:** Upside-down white triangles of growing sizes suddenly appearing as the colour rule is applied row after row.
- **Biggest problem:** A single mistake propagates down the whole triangle, so long fills either need constant adult checking or end in a broken picture.
- **One change:** Give a self-check (pre-coloured cells every few rows, or a reference strip) so children can catch errors themselves, and skip the numbered Pascal fill for 4-5 in favour of the colour triangle plus a few spot numbers.

### Week 102: Domino diamonds (Aztec diamond) (draft)

- **K–1, workable.** Placing real dominoes on a small printed diamond and doing a flip is hands-on and easy to grasp, but orders 1 and 2 hold only 2 and 8 tilings, so the activity runs out quickly and 'a tiling no neighbour has' needs adult sorting.
- **2–3, workable.** Finding all 8 order-2 tilings and sorting by the top squares is a good complete-list puzzle, but the pooled order-3 sort (64 tilings) becomes drawing, duplicate-checking and bookkeeping.
- **4–5, workable.** Predicting from 2, 8, 64 and seeing the arctic-circle picture are nice, but children cannot check 64 or 1024 themselves, so the count pattern is handed to them, and the large random tiling does not exist yet.
- **Best moment:** Seeing the printed large random tiling with frozen brick-wall corners and a messy round middle.
- **Biggest problem:** The hands-on part (orders 1 and 2) is small, and the interesting growth (64, 1024) is beyond what children can verify, so the middle of the hour is recording tilings.
- **One change:** Supply printed half-filled order-3 boards with the top fixed so tables can each own a small, checkable sub-case, and generate the arctic-circle print before scheduling.

### Week 103: Tower maps and one-switch codes (draft)

- **K–1, weak.** Two-cup Hanoi is solved in three moves, and matching each arrangement to a picture card and joining the right cards on the floor is an abstract state-graph task an adult will mostly run; walking the taped map is fun but the child is following the adult's map.
- **2–3, workable.** Three-disc Hanoi in 7 moves is a reliably engaging puzzle, and the neighbour-pegs 26-move challenge is long but has a clear goal; building the 27-card class map with its 39 links is slow and logistics-heavy, though the triangle-of-triangles reveal is a payoff.
- **4–5, workable.** Proving 2^n-1, the self-similar map and matching disc moves to one-switch lamp patterns give real ahas, but many children already know Hanoi and the map build is a big class-wide logistics job.
- **Best moment:** Stepping back from the finished state map and seeing that it is a triangle made of three smaller triangles.
- **Biggest problem:** The new idea (the state map) requires finding and joining many cards, which is bookkeeping an adult ends up coordinating, while the familiar move-count puzzle is the part kids enjoy.
- **One change:** Give 2-3 and 4-5 a pre-printed map with blank dots to label by playing, instead of building a 27-card floor map, and drop the map for K-1 in favour of just the neighbour-pegs cup challenge.

### Week 104: The sixteen-card square (draft)

- **K–1, workable.** Nine coloured shape cards on a 3x3 mat is tactile and attractive, but two simultaneous conditions (colour and shape in every row and column) is a lot for a 5-year-old; many will manage one attribute and need adult help for the second.
- **2–3, workable.** Real playing cards and a clear goal make this a classic, tempting puzzle, but juggling rank and suit across rows and columns with 16 cards leads many 7-8 year-olds to get stuck without a 'ranks first' hint.
- **4–5, strong.** The card puzzle, the harder diagonal version, the 5x5 step rule and the 36-officers story with a 1959 surprise and a quantum twist give challenge and narrative children of this age enjoy.
- **Best moment:** Finally placing the sixteenth card so every row and column has one of each rank and each suit.
- **Biggest problem:** For younger bands the double constraint arrives all at once, so trial-and-error can turn to frustration before any pattern is seen.
- **One change:** Stage it: solve the rank-only (or colour-only) square first with the cards, then add the second attribute on top, for K-1 and 2-3.

### Week 105: Knight's tours on small boards (draft)

- **K–1, weak.** The L-shaped knight move is hard for 5-year-olds to execute reliably, and on 3x3 every move is forced, so the child is following the move card or an adult rather than making choices.
- **2–3, workable.** A 3x4 tour with numbered counters is a good trial-and-error puzzle with easy backtracking, and pooling start squares is a nice class find, but knight moves stay error-prone and 4x4 offers only failure.
- **4–5, strong.** Hunting a 5x5 tour, discovering that the 'fewest exits' rule usually works, and the colour argument for where tours must start give strategy, failure and explanation at the right level.
- **Best moment:** Trying Warnsdorff's 'go where there are fewest exits' rule on 5x5 and watching it carry the knight all the way round.
- **Biggest problem:** Younger children struggle to make legal knight jumps, so the core move is not theirs, and some boards produce only frustration with a 'computer says no' ending.
- **One change:** Print each board with the legal knight links drawn as lines (or use a jump template) for K-1 and 2-3, so children choose routes rather than struggle with the L move.

### Week 106: Colouring maps (draft)

- **K–1, workable.** Colouring is natural for this age and tracing round cups is easy, but ruler lines right across the page and small regions are hard for 5-year-olds, and the two-colour surprise is subtle for them.
- **2–3, strong.** Drawing their own maps, discovering two colours always work for line maps, and the open challenge to draw a map needing five colours gives a 'try to beat it' drive kids enjoy.
- **4–5, strong.** The parity explanation is within reach, the odd-ring obstruction is a clean find, and the four colour theorem's story is compelling; the torus seven-country map is a strong extension once it exists.
- **Best moment:** A child's elaborate 'impossible' map turns out to need only four colours again.
- **Biggest problem:** The torus station depends on a seven-country portal map that has not been made, and K-1 regions may be too small to colour well.
- **One change:** Provide prepared large-region line and circle maps for K-1 and build and hand-check the torus map before the session.

### Week 107: Mazes, walls and random trees (draft)

- **K–1, strong.** Solving and building mazes for a friend is something young children love, and walking a token with a hand on the wall is a concrete rule; consistent hand side and fiddly wall strips need adult help but do not spoil it.
- **2–3, strong.** Building mazes that defeat the hand rule is an adversarial challenge with a clear payoff (wall islands), and Trémaux marking gives a method that always works.
- **4–5, workable.** The 2-3 tasks suit them well, but the Wilson's-algorithm die walk wanders and is a long simulation, and the fair-versus-unfair comparison (5/84 vs 1/14) needs far more trials than a class can tally.
- **Best moment:** A partner's hand-on-wall walker circling an island forever while the exit sits just out of reach.
- **Biggest problem:** The 4-5 headline (fair random mazes) is a slow dice simulation whose statistical point cannot be seen in one session.
- **One change:** Make the 4-5 core 'design a maze that beats Trémaux or the hand rule' and keep Wilson's walk as a short 2-by-3 demonstration rather than a frequency experiment.

### Week 108: Hailstone numbers (draft)

- **K–1, weak.** Tripling a pile of counters and adding one quickly yields piles of 40-50 that a 5-year-old cannot count or pair reliably, so the adult ends up running the machine.
- **2–3, workable.** Racing starts up to 20 and watching numbers shoot up and crash has real drama, but 3n+1 on numbers like 35 or 53 and 20-step chains are an arithmetic chore for many 7-year-olds.
- **4–5, strong.** The shared run of 27 climbing to 9232 is a genuine gasp, and an unsolved problem they can test with their own arithmetic excites this age; the backward tree adds a proved fact.
- **Best moment:** The class's shared run of 27 climbing past 9000 before finally crashing to 1.
- **Biggest problem:** The whole activity is repeated arithmetic, too heavy for K-1 and borderline for 2-3.
- **One change:** Give K-1 and 2-3 a prepared hailstone number line or lookup chart so they can move a marker and watch the ups and downs without doing the multiplication.

### Week 109: Sharing loaves the Egyptian way (draft)

- **K–1, weak.** Folding and cutting thirds and sixths is beyond most 5-year-olds' motor control, so an adult cuts and the child just hands out pieces.
- **2–3, workable.** Building each twelfth from one of each strip is a nice puzzle, but 4 loaves for 5 and 9 for 10 need twentieths and fifteenths that the strip set does not contain, so the sharing tasks stall.
- **4–5, workable.** The 4/n challenge and the greedy-machine surprise are good for strong 10-year-olds, but the work is mostly written-fraction arithmetic and the 'why it stops' argument is abstract.
- **Best moment:** Discovering a share like 'half plus a third' really covers five-sixths of a loaf when the pieces are stacked on a whole.
- **Biggest problem:** The concrete materials do not support the tasks given (cutting accuracy for K-1, missing strip sizes for 2-3), so children drift into paper arithmetic.
- **One change:** Use pre-scored loaves or a fraction-strip set that actually covers each assigned share, and choose loaf-and-worker problems that fit that set.

### Week 110: Fibonacci coins (draft)

- **K–1, weak.** Paying amounts with coins is concrete, but the 'no neighbouring coins' rule is arbitrary to a 5-year-old, the uniqueness discovery needs a systematic search, and the Zeckendorf merging game has too many rules for this age.
- **2–3, workable.** Fibonacci Nim is a real game with a hidden secret and kids like hunting for an amount with two payments, but tracking the changing 'at most double' limit needs a marker card and steady attention.
- **4–5, strong.** A two-player game with a learnable winning strategy, a 'try to break it' uniqueness hunt and an argument with coin rows give competition, surprise and explanation.
- **Best moment:** Realising you should refuse to go first when the pile is 8, 13 or 21, and then beating an adult with 'take your smallest coin'.
- **Biggest problem:** The neighbour rule and the doubling limit are two unnatural rules to juggle, and Fibonacci themes have engaged this group poorly before.
- **One change:** Lead with Fibonacci Nim (with a limit marker card) and let the coin system arrive as the key to winning, dropping the Zeckendorf game for K-1.

### Week 111: Staircase numbers (draft)

- **K–1, workable.** Building two- and three-step staircases from cubes and posting them on a chart is concrete and within reach, though K-1 will mostly make two-step staircases and see the 'missing numbers' only with adult framing.
- **2–3, strong.** Filling a shared 1-30 chart by building, noticing that 1, 2, 4, 8, 16 resist everything, and testing 32 gives a clean conjecture they find themselves.
- **4–5, strong.** Evening out a staircase into a rectangle is an object proof, and matching staircases to odd divisors gives a satisfying deeper rule.
- **Best moment:** Predicting that 32 has no staircase and nobody at the table being able to build it.
- **Biggest problem:** Bigger targets need many cubes and the chart work can slide into listing sums rather than building.
- **One change:** Keep the chart shared across tables so each child builds a few numbers in several ways rather than everyone covering 1 to 30.

### Week 112: Spreading claps around a circle (draft)

- **K–1, strong.** Placing cups on plates and playing the rhythm as a group is physical, musical and joyful, and judging whether it 'sounds even' is a decision they can make by ear.
- **2–3, workable.** The cinquillo-is-the-tresillo's-rests surprise is lovely, but counting the different 3-on-8 patterns up to turning (7) is a fiddly necklace-sorting job for 7-year-olds.
- **4–5, workable.** Finding the most even placement and comparing gap lists is good work, but 'most even' is a subtle condition and x.xxx. versus xx.xx. needs careful adult framing to land.
- **Best moment:** Flipping cups and rests on 5-on-8 and hearing the tresillo come back.
- **Biggest problem:** The mathematical criterion of 'most even' is hard to state for children, so beyond K-1 the music is fun but the mathematical question can feel vague.
- **One change:** Give 2-3 and 4-5 a concrete test (every clap's next-clap and second-next-clap gaps) on the recording strip so they can check evenness themselves rather than by ear.

### Week 113: One magic square (draft)

- **K–1, weak.** Adding three numbers to 15 over and over is too much arithmetic for 5-year-olds, and Pick 15 requires tracking all triples in your hand, so the adult does the sums.
- **2–3, workable.** Hunting for a magic square with tiles is a classic, achievable puzzle and Pick 15 is fun, but it leans on repeated addition and the 'really different?' question needs adult prompting.
- **4–5, strong.** Proving there is only one square by counting triples is within reach, and finding out that Pick 15 is tic-tac-toe in disguise is a genuine gasp moment.
- **Best moment:** Laying the Pick-15 cards on the Lo Shu and seeing that every win was a tic-tac-toe line.
- **Biggest problem:** For younger children the activity is mostly addition practice, which the plan itself flags as the risk.
- **One change:** For K-1 replace the sum-to-15 task with a dot-card or rod version where totals are seen by length, or skip K-1.

### Week 114: Sunflower spirals (draft)

- **K–1, workable.** Sticking numbered seed dots like a dot-to-dot is enjoyable and the quarter-turn spokes are clear, but placing seed i on ray i at circle i on a crowded golden sheet is fiddly and pinecone spiral counting is adult-led.
- **2–3, workable.** Predicting spokes for 2/5 and 3/8 then seeing them appear is a good reveal, but placing 60 stickers per sheet is long, and pinecone spiral counting is unreliable without an adult marking a start.
- **4–5, workable.** Why p/q gives q spokes and the approaching Fibonacci fractions are good ideas, but the golden sheet's spirals only become visible after many stickers, and the approximation work is abstract.
- **Best moment:** Comparing a finished spoked sheet with the golden sheet and seeing straight spokes on one and crossing spirals on the other.
- **Biggest problem:** The payoff picture appears only after a long sticker-placing session on sheets that do not yet exist.
- **One change:** Split each sheet's seeds among a table so every sheet is finished in ten minutes, and show a pre-made 300-seed golden picture alongside.

### Week 115: Wallpaper patterns (draft)

- **K–1, weak.** Tracing a patch of a busy pattern, pinning it and turning it until it matches again is fine-motor work a 5-year-old can't do alone, so the adult does the turning. Stamping a quarter-turn pattern is the one part their hands can manage, but its result is just a sticker count.
- **2–3, weak.** Finding every kind of spin point and mirror line on every sample is hard for adults too, and stamping a pattern with a 3-spin but no mirror is hard to get right. The pentagon gap is a real aha, but it comes after a long, tiring hunt.
- **4–5, workable.** The bead-purse puzzle is a tidy find-all-ways problem, but the prices are arbitrary numbers to a child, so the link to spins is told to them rather than felt. The shortest-slide proof with arrows can land with an adult guiding it.
- **Best moment:** Three paper pentagons around a point leave a 36-degree gap, so no pentagon floor is possible.
- **Biggest problem:** The core action, tracing and spinning a patch of a dense printed pattern to find spin points, is fiddly and slow, and telling kinds of points apart is too subtle for most children.
- **One change:** Use a few bold, pre-made patterns with pre-cut transparent overlays, and centre the session on building and stamping patterns rather than classifying found ones.

### Week 116: Kaleidoscopes (draft)

- **K–1, strong.** Standing a mirror hinge on a wedge and counting copies, or choosing a wedge to make a 6- or 8-petal flower, is instant magic that small hands can do. No reading is needed.
- **2–3, strong.** Predicting copies from the angle and then checking is a satisfying guess-and-test loop, and the odd-angle seams that look wrong are a real puzzle. Sorting logos into spin-only and mirror sets gives a second task.
- **4–5, workable.** The mirrors still delight, and why there are 2n copies can be checked with an arrow. Leonardo's theorem argued with tracing paper and flip-tracing card triangles around a corner are fiddly and lean on an adult.
- **Best moment:** Closing the hinge and watching the flower gain petals, then seeing the 72-degree picture come out wrong at the back seam.
- **Biggest problem:** Material fit is unproven: mirrors may slip on the sheet, the odd-angle clash may be hard to see, and a class set of mirrors costs money and needs care.
- **One change:** Rehearse with real mirrors and pre-cut card triangles; make the triangle-closing test a guided table activity with templates rather than free flip-tracing.

### Week 117: Commutator puzzles (draft)

- **K–1, workable.** Bringing five animals home after a two- or three-turn scramble is a nice small puzzle. But sliding every token on a ring by hand is error-prone, and one slip spoils the result, so an adult will hover.
- **2–3, weak.** Each turn means moving five tokens one by one and writing it down, and finding a three-token move by search is long and error-prone. The can-you-swap-two question has no answer they can reach, so it frustrates rather than surprises.
- **4–5, workable.** Following each token through do-do-undo-undo, building conjugates and the parity argument are real mathematics with a good wall-you-can't-cross moment. Still, the physical turning is a simulation chore, and long turn words are easy to garble.
- **Best moment:** Doing L R l r on a scrambled-looking board and finding that only three tokens moved, every time.
- **Biggest problem:** On a printed board a turn is five separate token moves, so the activity becomes careful bookkeeping where one slip ruins the experiment.
- **One change:** Build a real turning device, such as two overlapping paper-plate wheels on brads or a token track in a cup, so that a turn is one hand motion.

### Week 118: Card magic (draft)

- **K–1, workable.** Performing the pairs trick and trying hard to break it suits this age, and taking a top card from either pile is easy for small hands. The column trick's pick-up procedure and checking pairs in order will need an adult's hands.
- **2–3, strong.** Performing a trick, then hunting for why it works (the two top cards always differ) and finding when a plain cut fails is a good puzzle loop. The 3-card warm-up code is a satisfying secret.
- **4–5, strong.** The 56 hands against 56 messages count, with 9 cards impossible, is a sharp aha, and performing the five-card trick is a strong motivator. Designing the 3-from-8 code may need a partial crib ready.
- **Best moment:** A child riffles the piles any way they like, flips the row in pairs, and every pair has one of each colour.
- **Biggest problem:** Designing the 3-from-8 code is open and may stall 4-5 without a crib, and performance time can crowd out the why questions.
- **One change:** Have a staged crib for the code design (a worked 3-from-5 example) and protect a fixed block of time for the why questions after each trick.

### Week 119: Juggling patterns (draft)

- **K–1, weak.** Laying colour-coded card arcs from every beat of a 20-beat strip is fiddly, and stacked arcs pile up and slide. Counting arcs crossing a pencil is mostly an adult-led procedure with little meaning for them; only the optional beanbag passing gives the juggling joy.
- **2–3, workable.** Testing patterns like 441 and 432 and noticing that the ball count is the average is a genuine discovery. But each test means laying many arcs, so it is slow, and the 7 two-number patterns turn into a long recording task.
- **4–5, workable.** The landing-remainder test and the average argument are good, and the 1, 3, 5, 7 table invites a formula guess. It works better if arcs are drawn on a printed ladder instead of placed as card pieces.
- **Best moment:** Laying 4 3 2 and watching two rainbows land on the same beat: a crash.
- **Biggest problem:** There is no actual juggling: the activity is laying many card arcs on a strip, which is fiddly and repetitive, and the throwing that would make it fun is optional.
- **One change:** Make passing beanbags to a clap for each pattern the core experience, and record patterns by drawing arcs on a printed beat ladder rather than laying cut card arcs.

### Week 120: Eight triangle gems (draft)

- **K–1, strong.** Building closed gems from magnetic triangles is absorbing and needs no reading, and a number line of what the table found is a fine shared record. The large gems may collapse, and counting faces on a 3D object needs adult help.
- **2–3, strong.** Hunting for new triangle counts, failing to make an odd one, and trying for 18 or more than 20 is a real challenge with a clear goal. Checking how many triangles meet at a corner is easy on a model.
- **4–5, strong.** The even-count and at-most-five-at-a-corner explanations are within reach with models in hand, and the 18 that counting allows but nobody can build is a good puzzle.
- **Best moment:** Trying to build an 18-face gem and finding it won't close, though every simple count says it should.
- **Biggest problem:** It needs many magnetic equilateral triangles (about 20 per pair), which few families own in that number, and the paper fold-and-tape fallback is much slower and fiddlier.
- **One change:** Secure a class set of Polydron or Magna-Tiles triangles before scheduling, with photo cards of the 12-, 14- and 16-face gems as optional targets.

### Week 121: Cube nets (draft)

- **K–1, workable.** Folding six-square shapes around a cube block and sorting them into box and not-a-box is a good hands-on guess-and-check. Cutting and taping paper squares is hard for them; magnetic squares make it work.
- **2–3, strong.** Predicting whether a shape folds, then testing it, is a satisfying loop, and pooling a class collection of the 11 gives a shared goal. Deciding when two nets are the same is a real reasoning task.
- **4–5, workable.** The 7-cuts-and-5-hinges question and an organised completeness search have substance, and the open Dürer problem is a nice story. Many children have already met cube nets in school, so the surprise is smaller.
- **Best moment:** The plus shape folding up into a box, and a near-identical shape that won't.
- **Biggest problem:** It is a familiar school topic, and with paper, scissors and tape, testing each candidate is slow for younger children.
- **One change:** Use magnetic squares for testing so each fold takes seconds, and keep paper only for the final favourite net.

### Week 122: Tangram shapes with no dents (draft)

- **K–1, weak.** Filling even a square outline with all seven tans is famously hard without piece lines, and tracing found shapes is fine-motor work. Most 5-year-olds will need an adult to place pieces.
- **2–3, workable.** Hunting for band-passing shapes and pooling them is a real challenge, but free search with all seven pieces often stalls, and duplicates are hard to recognise. The rubber-band test is a nice concrete check.
- **4–5, workable.** Corners of only 45, 90 or 135 degrees and at most 8 sides are reachable on the half-square grid, and checking the class list against the number 13 is satisfying. The search is long and may frustrate without silhouette cards held in reserve.
- **Best moment:** Stretching a rubber band around a shape and watching it skip over a dent.
- **Biggest problem:** Finding convex tangram shapes from scratch is hard, so many children spend the time stuck, and K-1 cannot fill the outlines alone.
- **One change:** Give K-1 outlines with piece lines, and keep a deck of silhouettes of the 13 to hand out one at a time when a table stalls.

### Week 123: Guards in a gallery (draft)

- **K–1, strong.** Hide-and-seek in a taped room is physical and fun, and moving the guard to fix a hiding place is something they can do themselves. The paper plans need adult help with sight lines.
- **2–3, strong.** Finding the fewest guards for each plan and designing rooms that need 2 or 3 guards are open puzzles with clear goals and a nice design-challenge feel.
- **4–5, strong.** Fisk's triangulate-colour-and-pick method is short and checkable, and seeing why n/3 is always enough is a real aha. Building a comb that needs that many is a satisfying construction.
- **Best moment:** A child finds a hiding spot in the taped room that the guard truly cannot see.
- **Biggest problem:** Sight-line disputes at corners and a 10-corner floor outline need space, prep time and a clear rule.
- **One change:** Fix a clear rule (string must not cross or touch a wall) and use large printed plans on 11x17 paper so string sight lines are easy to check.

### Week 124: One straight cut (draft)

- **K–1, strong.** Fold, cut once, predict and unfold is a natural delight at this age and needs no reading. The square-target trick shown by an adult is a good surprise.
- **2–3, strong.** One-cut targets like the square, triangle, plus sign and letters are clear challenges with an instant check, and finding the corner-bisector fold is a real discovery.
- **4–5, strong.** The fewest-folds table for regular shapes and the halving explanation give depth, and the five-point star is a memorable payoff. Accurate folding of 8- and 10-gons will need care.
- **Best moment:** Unfolding a single straight cut to find a perfect square or star dropping out.
- **Biggest problem:** Several layers of printer paper are hard to cut cleanly and fold accurately, especially for younger children and higher-sided shapes.
- **One change:** Use thin origami paper and pre-printed fold lines for the harder targets, and rehearse the star.

### Week 125: One tile that never repeats (draft)

- **K–1, weak.** Hats have 12 orientations and a complex outline; random building quickly leaves gaps that 5-year-olds can't fix, so the adult will end up placing tiles. The flipped-colour noticing is pleasant but thin.
- **2–3, weak.** The one-colour challenge and slide test are interesting ideas, but children get stuck early with free placement. The key fact, never periodic, cannot be seen in a patch and so must be told.
- **4–5, workable.** The patch-of-eight build and comparing patches can work as a guided construction, and the einstein story is exciting for this age. The discovery is still mostly told, and the Heesch task is unchosen.
- **Best moment:** Building a patch of hats and noticing that a few must be flipped over.
- **Biggest problem:** The theorem's payoff (no repeating slide) is invisible on any patch children can build, and a 13-sided hat can't be cut with a paper cutter, so preparing 160 of them is a heavy job.
- **One change:** Provide a printed kite-grid mat on which hats snap into outlines, and frame the session as building a growing floor together rather than discovering aperiodicity.

### Week 126: Cut and rearrange (draft)

- **K–1, workable.** Rearranging pre-cut pieces of a square into different shapes is easy and pleasant, but counting grid squares under each shape is tedious and the same-area point is mild.
- **2–3, workable.** Turning 5x8 into 4x10 and 3x3 plus 4x4 into 5x5 are good puzzles, but the staircase cut is hard to discover, and cutting on grid lines takes time.
- **4–5, strong.** The 3-4-5 squares challenge, chasing fewest pieces, and the triangle-to-rectangle-to-square recipe give a real sense of a general method, with a nice 3D contrast at the end.
- **Best moment:** Fitting a cut-up 3x3 square around a 4x4 to make a perfect 5x5.
- **Biggest problem:** The key moves, such as the staircase cut, are hard to find unaided, so younger children may just follow a shown cut.
- **One change:** Give 2-3 a hint card that shows a staircase on a smaller rectangle, and let them find the staircase for the 5x8 themselves.

### Week 127: How long is a coastline? (draft)

- **K–1, weak.** Comparing a straightened string from a wiggly edge with one from a straight edge is a quick, mild surprise. Walking strips and counting steps along a printed coast with stickers is slow and imprecise.
- **2–3, weak.** Walking a 1 cm strip around a coast or a stage-3 Koch curve means 64 or more careful steps, and then multiplying steps by strip length. The trend will be noisy, and counting dominates.
- **4–5, workable.** Why the Koch length grows by 4/3 each stage is a real aha, and box counting has a clear idea. But counting hundreds of touched boxes on a 1 cm grid is tedious, and coast results will wobble.
- **Best moment:** Realising the coast keeps getting longer every time you use a shorter ruler.
- **Biggest problem:** The minute-to-minute activity is counting many tiny steps or boxes, and the imprecision can hide the pattern the session depends on.
- **One change:** Have children draw Koch curves themselves (stages 0 to 3) and compute the lengths, and keep coast-walking to a single short demo comparison.

### Week 128: Splitting necklaces (draft)

- **K–1, workable.** Cutting a short paper strip and sharing pieces into two cups until they match is doable, but with 4 beads it is close to trivial, and matching two colours at once is the real demand.
- **2–3, workable.** Sorting strings into one cut and two cuts and trying to stump a partner works, but the never-needs-three result means the stump game always fails, and cutting uses up strips.
- **4–5, strong.** Three-colour splits, finding a string that needs all three cuts, and the sliding half-window argument give a real explanation they can hold in their hands.
- **Best moment:** Sliding a half-length window along the beads and watching the red count pass through exactly half.
- **Biggest problem:** Cutting paper strips uses up the material and makes retrying slow, and the younger versions are thin.
- **One change:** Use reusable beads on a string with clothes-peg cut markers, and give K-1 longer two-colour strings so there is a real search.

### Week 129: Wobbly table and crumpled map (draft)

- **K–1, workable.** Turning a rocking stool until it settles, and failing to make a three-legged stool rock, is hands-on and needs no reading; the map-on-map hunt is too abstract for this age and should be dropped for them.
- **2–3, workable.** The stool and the two-figure monk puzzle are good concrete puzzles, but recording which diagonal rocks at every eighth of a turn is fiddly to judge and turns play into bookkeeping.
- **4–5, workable.** The quarter-turn sign-swap argument and the shrinking map look-ups give real reasoning and an aha, but everything depends on a stool and sand tray that actually behave like the model, and pinning look-ups on two maps is fiddly.
- **Best moment:** Nobody can make the three-legged stool rock, however hard they try.
- **Biggest problem:** The core phenomenon rests on untested physical materials (worn stool legs, sand that gives way), and if the stool does not cooperate the session has nothing to stand on.
- **One change:** Replace the sand tray with a rigid, reusable bumpy board (e.g. a few glued wood shims) rehearsed in advance, and make the monk puzzle the main 2–3 task instead of the eighth-turn record.

### Week 130: Buffon's needle and noodle (draft)

- **K–1, workable.** Dropping handfuls of toothpicks and sorting into two cups is pleasant hands-on play, and the ring always touching twice is a noticeable fact; but there is little for a 5-year-old to wonder about beyond sorting.
- **2–3, weak.** Counting crossings per drop over 30 drops and comparing averages is tally work, average is not yet a meaningful idea, and the intended surprise (bent shapes cross the same on average) is a 'no difference' result buried in noise.
- **4–5, workable.** Estimating pi from a class tally of toothpick drops is a genuine wow, and cutting the wire into pieces is an argument they can follow; it needs many drops and careful pooling.
- **Best moment:** The class tally of toothpick drops comes out close to 3.14 and someone recognises pi.
- **Biggest problem:** The headline discovery for younger children (shape does not matter) is a null effect that small, noisy samples cannot show convincingly.
- **One change:** For 2–3, keep only the toothpick drop with totals compared across tables, and make the pi reveal the shared ending rather than asking younger children to detect equal averages for bent wires.

### Week 131: Collecting every sticker (draft)

- **K–1, workable.** Rolling a die and filling a sticker card is game-like and easy to do; the cube tower makes the run visible. Long runs of 25-plus rolls can drag, and the 'last one is slow' idea is felt more than understood.
- **2–3, workable.** Circling new faces on a written roll strip and comparing gaps is a reasonable record, but writing every roll is a chore and the pattern needs many pooled runs.
- **4–5, workable.** The stage-by-stage 6, 6/5, ... build to 14.7 matched against the class number line is a satisfying prediction-meets-data moment, though the math is mostly told and checked.
- **Best moment:** Everyone stares at the last empty square on their card while the die keeps giving faces they already have.
- **Biggest problem:** Repeated runs are dice-rolling with little decision-making, so after two or three runs the activity becomes waiting.
- **One change:** Turn it into a betting game: before each run every child bets a number of rolls on the class number line, and closest bet wins, so the long tail and the mean become things they care about.

### Week 132: Penney's coin-pattern races (draft)

- **K–1, workable.** Two-flip colour races with cubes for wins are simple and the 3-to-1 edge of blue-red over red-red can show up in ten races; spotting a two-box pattern on a track may need an adult eye.
- **2–3, strong.** Picking a reply that beats whatever a partner chooses is a trick kids love to play on each other and on adults; the class who-beats-whom chart is some bookkeeping and the 2/3 edges need pooled races.
- **4–5, strong.** The game plus the short 7/8 argument (HHH only wins if it comes first) is a real proof within reach, and waiting-time versus winning is a good second question.
- **Best moment:** A child realises they can beat the adult whichever card the adult picks, and does it again.
- **Biggest problem:** With only ten races per pair the 2/3 edges are often invisible, so 2–3 children may conclude there is no pattern.
- **One change:** Have each table race the same pairing and pool results onto one class chart before asking for the best reply.

### Week 133: Simpson's paradox with bags (draft)

- **K–1, weak.** Choosing between an all-red bag and a mostly-red bag is obvious, and the reversal only means something if a child remembers and compares the earlier choices; drawing adds nothing for them.
- **2–3, workable.** The pour-together reversal is a real surprise and building your own reversing set of bags is a good open challenge, though the main set (a one-counter bag) may feel like a trick.
- **4–5, workable.** Fraction comparisons in the gentler set and the hunt for an equal-size reversal that never works give substantive reasoning; it is closer to arithmetic than play.
- **Best moment:** After pouring, the side that won both pairs is suddenly the worse bag.
- **Biggest problem:** The paradox is a comparison of earlier judgments with a later one, which needs memory and fraction sense the youngest lack, and the drawing ritual is luck that does not bear on the question.
- **One change:** Drop drawing entirely and make it a building challenge: 'make A win both pairs but lose after pouring', with the spare counters, scaffolded by the given set as an example.

### Week 134: Peg solitaire and Conway's soldiers (draft)

- **K–1, workable.** Jumping counters to clear a row of 4 or 6 is a clear, satisfying puzzle; the 10-hole triangle is frustrating, and the colour-sticker chart means nothing to them.
- **2–3, strong.** The 15-hole triangle is hard but compelling, and getting soldiers 1, 2 and 3 rows past the line with as few as possible is a classic absorbing challenge.
- **4–5, strong.** The soldiers challenge plus the colour invariant and the weight argument for row 5 give real puzzles and a real impossibility proof; the infinite weight sum needs a good picture.
- **Best moment:** Someone gets a soldier three rows past the line using only 8 soldiers.
- **Biggest problem:** Counters on paper slide around and jumped counters are easy to confuse, so failed attempts are hard to retrace.
- **One change:** Use egg cartons or pegboards (or a hole-punched board) so pieces stay put and resets are fast.

### Week 135: Trust game (prisoner's dilemma) (draft)

- **K–1, weak.** Choosing share or keep for beans is playable, but 5-year-olds mostly choose at random or take 'keep' as being mean, and watching strategy cards play each other is an adult moving beans.
- **2–3, workable.** Discovering that keeping always pays more for you yet two keepers end poorer is a real aha, and the die ending is lively; social upset needs managing.
- **4–5, workable.** Writing strategies and running a round robin is exciting, and copycat topping the table while never beating anyone is a great surprise, but scoring a tournament by hand is slow without a prepared sheet.
- **Best moment:** Copycat wins the class tournament even though it never beat a single opponent.
- **Biggest problem:** The hand-run round robin is long bookkeeping that adults end up doing, and 'keep' can feel like betrayal to young children.
- **One change:** Precompute or quickly score pairings with a printed match grid so children spend their time inventing and predicting strategies, and give K–1 a short fixed-length bean game only.

### Week 136: Sealed-bid auctions (draft)

- **K–1, weak.** Value-minus-price with cube towers is abstract for 5-year-olds, who want to win the auction regardless of points, and an adult has to do the subtraction at each table.
- **2–3, workable.** Bidding games are lively and the 'never-worse bid' table is a good discovery, though the points-not-prizes framing needs care.
- **4–5, workable.** The case-by-case argument for bidding your value and the halve-your-bid puzzle are good reasoning; the payoff is clear once the rules land.
- **Best moment:** A volunteer wins the auction and the class realises they actually lost points.
- **Biggest problem:** Children instinctively play to win the auction, not to maximise value minus price, so the scoring has to be understood before any of the strategy makes sense.
- **One change:** Open with several quick demo rounds where winners visibly lose points, before any child bids, and leave K–1 out or give them only the tower-building comparison.

### Week 137: Game of Life (draft)

- **K–1, weak.** Counting eight neighbours including diagonals is the hard part for 5-year-olds, so an adult counts aloud while they place counters, and the floor routine is likely to need adults running it.
- **2–3, workable.** Small starts that blink, settle or vanish are fun to find and parent-finding is a good puzzle, but hand-updating larger shapes (the T for nine generations) is error-prone simulation.
- **4–5, workable.** The glider and the Rule 90 ring are within reach, and the Sierpinski triangle emerging row by row is a real gasp; enumerating ring patterns is heavy.
- **Best moment:** Rule 90 from a single coloured square draws the Sierpinski triangle on squared paper.
- **Biggest problem:** Updating a grid by hand is slow and mistake-prone, so a single error derails a pattern and the whole-room floor version risks collapsing into adults operating it.
- **One change:** Keep the floor grid as a short demo, and give children small patterns (3–5 counters) on transparent overlays or a 'neighbour window' card, saving long evolutions for an app.

### Week 138: Busy beaver (draft)

- **K–1, skip.** Following a two-state rule table needs a simultaneous lookup of colour and cup, so an adult reads and runs it while children move a toy; there is no surprise at this age.
- **2–3, weak.** Designing cards means many simultaneous choices, most random cards stop at once or obviously run forever, the record of 6 cannot be beaten, and the key insight is told by the facilitator.
- **4–5, workable.** Some 10-year-olds enjoy being the machine and writing short 'forever proofs', but the 21-step run is a long, error-prone simulation and the explosive growth is told, not felt.
- **Best moment:** A child notices their card is bouncing between the same two cups forever and explains why it will never stop.
- **Biggest problem:** The minute-to-minute activity is executing a rule table step by step, a simulation chore with an unbeatable record and a payoff that exists only as a story.
- **One change:** Reframe for 4–5 only as 'stops or forever?': hand out a deck of small ready-made cards to sort and prove, rather than long runs and record-chasing.

### Week 139: Secret messages and two padlocks (draft)

- **K–1, workable.** Handling real padlocks and acting out the four trips is fun and physical, though why it is clever may not register; symbol counting on a short message is fine.
- **2–3, strong.** Breaking a secret message with tallies and short words is a beloved activity, and the padlock trick is a genuine puzzle; the 183-letter tally needs splitting across a table.
- **4–5, workable.** Catching the shift-padlock leak as an eavesdropper is a good aha, but the clock-power arithmetic mod 11 may swamp the reasoning without a printed power table.
- **Best moment:** The class hands over the locked pencil case and works out how to get it there without ever sending a key.
- **Biggest problem:** The 2–3 cipher is long to tally by hand, and the 4–5 modular powers risk becoming arithmetic practice.
- **One change:** Split the cipher text into table strips with a pooled tally chart, and give 4–5 a printed powers-of-2 clock table.

### Week 140: Proving without telling (draft)

- **K–1, workable.** Running round a ring of chairs and seeing how long a bluffer survives is lively and the 'how many before you believe' idea is reachable; it needs two adults and much is luck.
- **2–3, workable.** Hiding colourings under cups and lifting one border is a good game, and playing the cheater on the five-petal flower is fun; re-colouring behind a folder correctly and quickly may need an adult.
- **4–5, workable.** The probability of a cheater surviving k rounds and the shuffle table make the ideas concrete; 'learns nothing' remains subtle and secret sharing is a separate topic.
- **Best moment:** The bluffer survives one round, then two, and the room cheers until the streak breaks.
- **Biggest problem:** The zero-knowledge part ('the verifier learns nothing') is the deep idea but is the hardest thing to feel, and the colour-swap step behind the folder is likely to break down.
- **One change:** Use a printed colour-swap card for re-colouring and make the cheater-on-five-petals game the centrepiece for 2–5, dropping secret sharing to the guide.

### Week 141: Leaning towers off the table (draft)

- **K–1, strong.** Sliding blocks out until the top one hangs completely past the edge is pure physical play with a visible surprise, and toppling is part of the fun.
- **2–3, strong.** Finding the fewest blocks to get past the edge is a clear, gripping goal; measuring the shrinking steps adds a pattern to notice.
- **4–5, strong.** Centres of mass, the harmonic steps and the side-by-side stack beating one-per-level give deep math anchored in something they built.
- **Best moment:** Four blocks: the top block hangs entirely beyond the table edge and doesn't fall.
- **Biggest problem:** Knife-edge stacks topple easily, so the four-block milestone may need patience and identical blocks.
- **One change:** Rehearse with the actual blocks and provide a pillow plus a five-block target so children reliably experience the milestone.

### Week 142: Space-filling curves (draft)

- **K–1, workable.** Walking a floor path and inventing one that steps on every square once is active and easy, but there is little surprise for this age.
- **2–3, workable.** Rotating four cups to join them into the next stage is a good spatial puzzle and drawing stage 3 is satisfying, though reflections are tricky and the 8 × 8 drawing is fine-motor work.
- **4–5, workable.** Numbering 64 cells is a chore before the payoff, and the limit argument is abstract; the cells-close-in-number-versus-close-in-space contrast is a good hook.
- **Best moment:** Four copies of the little cup snap together into one path that visits every square.
- **Biggest problem:** The real mathematics (the limit reaching every point) arrives after a long numbering task and may not land.
- **One change:** Give 4–5 a pre-numbered stage-3 board and spend the time on the quarter-of-time-in-a-quarter-of-space puzzle instead of numbering.

### Week 143: Domino computers (draft)

- **K–1, workable.** Knocking down domino lines, forks and merges is pure joy for this age, but five-year-olds knock lines over while setting them up and a reliable fork takes adult help; the truth-table card is incidental to the fun.
- **2–3, workable.** The 'make the cup fall only if both are pushed' challenge is a great hook but a domino AND is genuinely hard and may just end in rebuilds; the human-gate half adder is a fun skit that an adult choreographs while most children stand and wait.
- **4–5, workable.** Fewest-NAND-card puzzles are real puzzles a 10-year-old can own, but they are paper-and-rule-card work detached from the dominoes, and the domino gates beyond OR may not work reliably at table scale.
- **Best moment:** The cup toppling when two lines merge, and the moment someone gets a cup to fall only when both starts are pushed.
- **Biggest problem:** Most of the session risks going to resetting fallen dominoes and to gates (AND, XOR, NOT) that do not work reliably at table scale, so the gate ideas never get tested.
- **One change:** Rehearse and supply printed placement templates or simple jigs for wire, fork, merge and one working AND so children rebuild in a minute and spend their time testing and predicting.

### Week 144: The MU puzzle (draft)

- **K–1, workable.** Doubling a cube pile or taking away 3 is concrete, and seeing 3, 6, 9, 12 stay empty on the mat is a real noticing, but routes like 1-2-4-8-5-10-7 are long for a five-year-old and the adult will keep the goal in mind.
- **2–3, weak.** Juggling four conditional rewriting rules (ends in I, double after M, III to U, drop UU) while copying ever-longer tile strings is heavy, and the I-count-mod-3 insight is unlikely to emerge at this age, so it becomes aimless string-making with no aha.
- **4–5, workable.** Proving MU impossible by tracking the I count is a classic, satisfying invariant argument for 10-year-olds, though the letter game itself is dry and the converse route-building is fiddly tile bookkeeping.
- **Best moment:** Realising that no pile of 3, 6, 9 or 12 ever shows up no matter how you double and subtract.
- **Biggest problem:** The four letter rules plus string doubling overload grades 2-3 and the invariant pay-off arrives only after a long, unfocused search.
- **One change:** Lead every band with the cube-pile game (double or take 3) as the main puzzle and offer the MIU letter system only to grades 4-5 as the follow-up that has the same hidden invariant.

### Week 145: Fake coin and the balance (draft)

- **K–1, workable.** A real balance and a secret heavy egg is a hands-on detective game children love, and three eggs in one weighing is a lovely find; nine in two needs planning most five-year-olds will not do unaided, and a bucket balance may not tip clearly.
- **2–3, strong.** Faker-and-detective roles, the 'level means it's the one left off' trick, and the 3-9-27 pattern are concrete and surprising; a 7-year-old can plan and test a two-weighing strategy with real eggs, though drawing the tree may need an adult scribe.
- **4–5, workable.** The heavy-or-light 12-coin problem is notoriously hard and many 10-year-olds will not crack it in a session, and the 13-coin first-weighing argument is abstract; the heavy-only part is a strong entry if allowed.
- **Best moment:** Discovering that one weighing finds the heavy one among three because a level balance also gives an answer.
- **Biggest problem:** It depends on a balance sensitive enough to show one extra washer, and the 4-5 heavy-or-light challenge may be too hard to land in one hour.
- **One change:** Use a heavier fake (two or three extra washers) and rehearse the balance, and give 4-5 the heavy-or-light version with 3, then 4, then 12 containers as an explicit ladder rather than jumping to 12.

### Week 146: Easy to check, hard to find (draft)

- **K–1, workable.** Splitting cube sticks into two equal rows and checking by sliding them side by side is concrete, and being a puzzle maker who breaks a tower in half is fun; but the plan's example bag 1 to 6 totals 21 (odd) and has no split, and the check-versus-find idea is a meta point they won't feel.
- **2–3, workable.** Finding the one split of the 7-stick bag, beating the greedy rule and wrestling with a no-split bag are real puzzles; it can feel like addition practice and the no bag may frustrate without an adult ending.
- **4–5, workable.** Counting ways to share sticks, collecting reasons for 'no' and finding a no bag none of them explains is good reasoning, and the million-dollar open problem is a hook; the activity itself is subset-sum trial and error without a big gasp.
- **Best moment:** Lifting the folder to check a hidden split in two seconds after struggling to find it, or making a bag that a friend can't crack.
- **Biggest problem:** The core action is searching for equal-sum splits, which is mildly satisfying but has no strong surprise, and the K-1 example bag is unsolvable as written.
- **One change:** Turn it into a maker-versus-solver game: each child builds a secret solvable bag from a split tower and challenges a partner against a timer, so the check-is-fast, find-is-slow contrast is felt rather than told (and fix the K-1 bag to an even total).

### Week 147: Pairing strategies (draft)

- **K–1, workable.** The strip game is quick and replayable, and 'two in a row always wins' is easy to see, but finding or following a domino pairing plan is beyond most five-year-olds; they will play Breaker with dominoes an adult drew.
- **2–3, workable.** Tic-tac-toe variants are instantly appealing and 'Maker first always wins on 3 by 3' is a good discovery; the 5 by 5 domino plan is a hard puzzle and checking 12 lines on a clear sleeve is fiddly, so many children will need the diagonal hint.
- **4–5, strong.** Playing games, then proving Breaker always wins with a domino plan, plus the lovely counting argument that 4 by 4 (16 squares, 10 lines needing 20) has no plan, is exactly the game-to-proof arc 10-year-olds enjoy.
- **Best moment:** Watching a pre-drawn domino plan shut down every attempt at three in a row, then discovering you can beat it on a board where it can't exist.
- **Biggest problem:** The central pairing idea is a strategy someone else designs, so younger children mostly play a game whose clever part they don't see.
- **One change:** Give 2-3 a ladder of pairing puzzles on smaller boards (strips, 3 by 4 rectangles) before 5 by 5, so children design a working plan themselves before the hard one.

### Week 148: Guess two-thirds of the average (draft)

- **K–1, weak.** Levelling eleven secret towers to find an average is slow and adult-run, five-year-olds can't reason about what others will guess, so each round is effectively a lottery with one winner and some upset losers.
- **2–3, workable.** The class game with a chart of falling targets is lively and 'why would anyone guess over 67?' is reachable, but most 7-year-olds guess randomly and the adult does all the averaging.
- **4–5, strong.** Ten-year-olds reason about other players' reasoning about as well as adults, the falling targets round to round produce real laughter and argument, and the crossing-out staircase is a satisfying explanation.
- **Best moment:** Seeing the winning number drop sharply in round two as everyone tries to outthink everyone else.
- **Biggest problem:** Only the oldest children can play the reasoning game; for younger ones and at a kitchen table with two or three players it degenerates (with two players the lower guess always wins).
- **One change:** Run it as a whole-room game aimed at 4-5 with a quick visual average (calculator or number line) and give K-1 a different task, and add a kitchen-table version with imaginary extra players or past-class data so it works with three people.

### Week 149: Racetrack (draft)

- **K–1, workable.** Being the car on a floor road, hopping by a speed card and trying to stop exactly in the garage is physical and funny; tracking 'add 1, keep, take 1' while hopping needs a partner holding the card, and the planning is mostly adult-prompted.
- **2–3, workable.** Racetrack races are a game children replay happily, but the ghost-arrow rule is hard for 7-year-olds to execute on 1 cm squares and crashes from miscopied arrows may cause disputes.
- **4–5, strong.** Paper races in pairs with a real strategy (brake before the corner) are absorbing and replayable, and the 1-2-3-2-1 parking pattern and a why-no-faster argument give genuine mathematics.
- **Best moment:** Overshooting the garage or crashing into the wall at full speed, then realising you have to brake early to win.
- **Biggest problem:** For younger children the vector-copying rule on small squared paper is fiddly enough that adults end up checking or drawing moves.
- **One change:** Use a larger grid (2 cm squares or a printed dot board) and a transparent or cut-out 3-by-3 'steering card' placed at the tip of the copied arrow so younger children can execute moves without miscounting.

### Week 150: Same network or different (draft)

- **K–1, weak.** Bead-and-string networks tangle, five-year-olds struggle to lay them out to match a drawing, and 'same network' is an abstract judgment they cannot make by themselves.
- **2–3, workable.** Sorting a deck of drawings into families is a decent spot-the-same game and the pentagon-equals-star reveal is nice, but proving differences by counts gets dry and the equal-count different pair at 8 dots is likely too hard.
- **4–5, workable.** Finding all six trees on six beads and writing renamings is solid reasoning for 10-year-olds, but checking renamings is bookkeeping and there is little surprise after the first reveal.
- **Best moment:** Dropping the pentagon as a tangle and laying it out as a five-pointed star: it's the same network.
- **Biggest problem:** After the first 'it's the same!' moment the activity becomes counting degrees and checking renamings, which is careful bookkeeping more than discovery.
- **One change:** Make it a game: one child secretly re-lays a bead network, the other must decide same or different and challenge, so the counts become weapons in a contest rather than a checklist.

### Week 151: Instant Insanity (draft)

- **K–1, weak.** Folding paper cubes from nets is beyond five-year-old hands, and keeping four sides of a tower in mind while turning cubes overloads them; only the 'front shows four colours' goal is realistic.
- **2–3, workable.** The ladder of goals gives some progress and the broken cube with four red faces is a good impossibility argument, but the full puzzle by trial is famously frustrating and most children won't solve it.
- **4–5, workable.** The opposite-face graph is a beautiful trick, but drawing and reading it needs a long adult explanation and the pay-off arrives late, after children have likely spent their patience on trial and error.
- **Best moment:** Proving the broken set is hopeless: one cube with four red faces must show red on two sides.
- **Biggest problem:** The core puzzle is a mostly-blind search with a tiny solution set, so children face long frustration before the clever method appears.
- **One change:** Supply sturdy pre-made cubes (wooden with stickers), and introduce the 'only opposite pairs matter' idea early with a 2- or 3-cube version that kids can solve, so the graph method helps before patience runs out.

### Week 152: Who is most important? (draft)

- **K–1, weak.** Walking between chairs and dropping counters is fun for a few minutes, but it is a coin-driven walk with no decisions, one floor setup means waiting turns, and the point (A beats C) only appears after pooling many steps.
- **2–3, workable.** The vote-then-surprise is a good hook and the trap and die rule are memorable, but 26 coin-flip steps per pair and tallying are a simulation chore and results are noisy.
- **4–5, workable.** Checking that the 4, 2, 3, 2, 1, 1 counter split survives a sharing round is a crisp aha and explains why C loses to A, though it comes after a long random walk.
- **Best moment:** The class vote for C turning out wrong when the cups are lined up.
- **Biggest problem:** Most of the time goes to executing random steps and tallying, and the surprising result only emerges after pooling, by which point younger children have lost interest.
- **One change:** Lead with the counter-sharing round (everyone at a chair passes counters along arrows simultaneously) so all children act at once and see the piles settle, keeping the random walk as a short confirmation.

### Week 153: Soap-film shortcuts (draft)

- **K–1, strong.** Dipping a frame and seeing a soap network appear is magic for five-year-olds; drawing it and comparing string lengths is simple, even if the shortest-network idea stays light.
- **2–3, strong.** The soap's surprising square network (two junctions, not an X) and the string comparisons give a real gasp; measuring 120 degrees is fiddly but a three-armed template helps.
- **4–5, strong.** The sliding-junction argument for equal angles, predicting junctions then checking with soap, and catching soap in a worse network are rich and hands-on for 10-year-olds.
- **Best moment:** Lifting the square frame out of the soap and seeing two junctions joined by a bridge instead of the expected X.
- **Biggest problem:** Building reliable plate-and-peg frames is over the 30-minute prep budget for a parent volunteer and the frames may not work well first time.
- **One change:** Specify a no-drill frame design (e.g., two clear lids with pushpins or glued dowels) and rehearse it, with a fallback of printed photos of the soap networks if frames fail.

### Week 154: Bulgarian solitaire (draft)

- **K–1, workable.** With 6 counters the move is concrete and the staircase appears in a few moves, which is a little magic, but 'one from every pile' is easy to fumble and it's a procedure rather than a puzzle.
- **2–3, workable.** Discovering that some totals settle and some loop is a real surprise, but filling a class table for 3 to 10 is a simulation chore with careful recording.
- **4–5, workable.** Finding both cycles for 8 and the shapes no move makes is good, but the tipped-diagram proof is abstract and may need a return visit.
- **Best moment:** Every different start of 6 cards ending in the same 3-2-1 staircase.
- **Biggest problem:** Children spend most of their time executing a fixed move and recording piles rather than making choices.
- **One change:** Make it a challenge: 'find the start that takes longest to reach the staircase' or 'make a pile shape that can never appear', so children choose starts and hunt rather than just repeat the move.

### Week 155: Weird dice (draft)

- **K–1, workable.** Racing counters up a 2-to-12 track with dice is a game kids enjoy, but it's pure luck and the point (weird dice behave the same) is invisible to five-year-olds after a few rolls.
- **2–3, workable.** Filling two addition tables and finding identical counts is a genuine surprise and good arithmetic, but designing a matching die from scratch is a hard, open search that can stall.
- **4–5, workable.** Finding the four-sided weird pair is a nice puzzle, but the polynomial factoring is too abstract for most 10-year-olds without algebra.
- **Best moment:** Filling both addition tables and realising the strange dice give exactly the same sums counts.
- **Biggest problem:** The surprise lives in a table, not in play, and the deep explanation needs algebra beyond the band.
- **One change:** Make a game where knowing doubles matters (roll again on doubles), so children feel the one visible difference, and give 2-3 a guided search for the four-sided pair instead of the six-sided design.

### Week 156: Lining up by height (draft)

- **K–1, weak.** Picking people 'in order but skipping some' is a subtle idea for five-year-olds, and checking all triples in a line of 5 needs an adult to drive.
- **2–3, workable.** Building the longest line with no run of 3 or 4 is a good puzzle and patience sorting is a fun card game, but checking runs by hand is error-prone.
- **4–5, strong.** Finding 3 2 1 6 5 4 9 8 7, discovering 10 always fails, and the label-pair pigeonhole proof are rich and accessible for 10-year-olds.
- **Best moment:** Five volunteers trying every rearrangement and never escaping a run of three.
- **Biggest problem:** Spotting non-adjacent rising or falling runs is error-prone, so younger children rely on an adult to check.
- **One change:** Add a quick check method (patience piles or step-forward routine) introduced early so children can verify runs themselves.

### Week 157: Remainders that repeat (draft)

- **K–1, weak.** Dealing counters onto plates is fine for a round or two, but trading leftovers for ten smaller counters is a symbolic step a 5-year-old won't follow; the adult does the trading and recording while kids deal, and 'the cards repeat' after six rounds is mostly the adult's observation.
- **2–3, workable.** Dealing then switching to the wheel is doable and 'the leftover came back, so it must repeat forever' is a real aha, but six to twelve rounds of deal-trade-record is a long procedure and the shift from counters to wheel needs a strong adult; without decimals the payoff (the digits 142857) is muted.
- **4–5, workable.** The rotating digits of 142857 and 2/7 starting the same wheel at 2 are genuine surprises, but the route there is long division by hand and the period table for primes to 41 is bookkeeping shared across tables, with 17 and 19 needing 16-18 rounds.
- **Best moment:** Multiplying 142857 by 2, 3, 4, 5, 6 and seeing the same digits come back rotated, then times 7 giving 999999.
- **Biggest problem:** The concrete dealing is slow and repetitive and turns into a rote simulation before the interesting wheel and rotation patterns appear.
- **One change:** Move the counters to a 3-minute launch and have children work mainly on the remainder wheel (with the 'times 3 on the 7-wheel' shortcut available), saving time for the 142857 rotation hunt.

### Week 158: Squares from two squares (draft)

- **K–1, workable.** Building small squares from tiles and adding two of them with an adult is real hands-on work, and colouring a class chart is satisfying, but the totals quickly need counting past 20 and the 'never works' pattern is mostly adult-noticed.
- **2–3, workable.** A class hunt to fill a 1-50 chart is engaging and the leftover-after-fours sort is a concrete obstruction, but after the first 15 minutes it becomes mental addition of squares and chart bookkeeping; tiles help only for small cases.
- **4–5, strong.** Proving 'leaves 3 after fours is impossible' with tile groups is a real proof children can own, and the prime split (5, 13, 17 work; 3, 7, 11 don't) is a striking pattern; windmills are fiddly but a good challenge with printed outlines.
- **Best moment:** Discovering that every never-works number leaves exactly 3 when grouped in fours, so 43 and 47 can be ruled out without trying.
- **Biggest problem:** For younger bands the chart hunt drifts into arithmetic of squares with a light payoff, and windmill building needs 29 tiles and careful orientation.
- **One change:** Give 2-3 a pre-printed table of square numbers to pair up so the hunt focuses on the pattern of failures, and give 4-5 printed windmill outlines.

### Week 159: Rectangles of a number (draft)

- **K–1, workable.** Building every rectangle from 6, 7, 8 and 12 tiles is a good K-1 task and '7 only makes a line' is a small surprise; the tower comparison needs an adult to list sides, but kids can stack and compare towers.
- **2–3, workable.** Rectangle galleries and the short/level/tall sort are concrete and finding 28 as the second 'level' number is a satisfying hunt, but tracing every rectangle onto squared paper is busywork and the material repeats familiar factor-rectangle work.
- **4–5, strong.** Predicting 496 from the doubling sums and checking why 15 fails gives a real conjecture-and-test moment, and 'nobody knows if an odd one exists' lands well at this age.
- **Best moment:** A tower of 1+2+3 standing exactly level with a tower of 6, then hunting for the next number that does it.
- **Biggest problem:** Tracing galleries and stacking towers for many numbers is slow, and the rectangle gallery repeats Week 96-style material.
- **One change:** Drop the tracing; let tables share a wall list of side lengths and spend the time on the level-tower hunt and the doubling pattern.

### Week 160: Times tables on a circle (draft)

- **K–1, weak.** Hooking yarn round a notched plate while an adult reads pairs is fiddly, the adult is operating the rule, and on 10 notches no striking shape appears.
- **2–3, workable.** Watching a heart appear from straight lines is a real wow, but drawing 59 accurate chords with a ruler and computing 'times 2, keep the remainder past 60' is a long chore that many 7-8-year-olds won't finish; splitting dots within a table helps.
- **4–5, workable.** Cusp counting across times 2 to 5 and the parallel chords of times 23 are good conjectures, but each picture is 10-15 minutes of ruler work, so comparing four multipliers needs pre-printed help; the return-to-1 question is good mental work.
- **Best moment:** The cardioid emerging from a mess of straight chords on the 60-dot circle.
- **Biggest problem:** The payoff depends on dozens of precise ruler chords, which is slow, fine-motor and error-prone.
- **One change:** Print dot circles with each dot's target number already labelled (or faint chords for half the circle) so children draw quickly and spend time comparing pictures.

### Week 161: Flexagons (draft)

- **K–1, workable.** A pre-folded trihexaflexagon that magically shows a hidden colour delights young children and stickering new faces is easy, but the pinch flex itself is awkward for small hands and there is little to do after finding three faces.
- **2–3, strong.** Folding a trihexa with help and hunting all six faces of a pre-folded hexahexa is absorbing play with a built-in mystery (rare faces), and the face map is a natural record.
- **4–5, strong.** Folding the hexahexaflexagon is fiddly but doable at this age, and the traverse, the triangle map and predicting the hidden face from the strip give real reasoning tied to a toy kids want to keep playing with.
- **Best moment:** Pinching open the flexagon and a colour nobody had seen appears in the middle.
- **Biggest problem:** Folding, especially the hexahexa, is a known stumbling point and the face map depends on the printed strip matching the plan, which is untested on paper.
- **One change:** Rehearse and print a tested hexahexa strip and prepare enough pre-folded spares that no child waits on folding to start flexing.

### Week 162: Thirty coloured cubes (draft)

- **K–1, workable.** Stickering red/blue cubes is fun and 'same after turning' is a real idea at this age, but reliably deciding whether two cubes match by turning is hard for 5-year-olds, so the table count of 10 will need heavy adult checking.
- **2–3, workable.** Building a class museum is a motivating collective goal, but comparing six-colour cubes by turning is slow and error-prone, and duplicates or misses will creep in unless the sorting card system is given early.
- **4–5, workable.** The 5 x 6 and 720 / 24 arguments, mirror twins and MacMahon's double-size puzzle are rich, but the puzzle needs a complete, correct set of 30, which the museum may not deliver in one session.
- **Best moment:** Two cubes that look totally different turning slowly until they match, or a pair that can never be made to match (mirror twins).
- **Biggest problem:** Every stage rests on children correctly judging cube sameness by mental or physical rotation, which is slow and unreliable.
- **One change:** Give the 'red on top, which colour below, read the sides from a fixed colour' card from the start and have a pre-made checked set of 30 ready for the MacMahon puzzle.

### Week 163: Arrow multiplication (draft)

- **K–1, weak.** Quarter-turn floor games are fun movement but the mathematics is just counting turns, and naming a half turn 'minus 1' means nothing to children who haven't met negative numbers.
- **2–3, weak.** Multiplying by 1 + i means placing an arrow and its turned copy nose to tail and recording points like -2 + 2i; children execute a rule they can't connect to anything, and the spiral payoff needs accurate long arrows off a table mat.
- **4–5, workable.** Some 10-year-olds will enjoy that two tilted arrows multiply to land exactly on 5 and that 3 can never be made, but the nose-to-tail rule with backwards copies is abstract and needs a worked example and a strong adult.
- **Best moment:** The child-arrow on the floor turning twice to face backwards and the room realising 'times i times i' is 'minus 1'.
- **Biggest problem:** The concrete action (turning) is trivial while the real content (Gaussian multiplication) is an abstract rule pitched well above the bands.
- **One change:** Reserve it for 4-5 as a sequel to Week 158, built around one physical puzzle: which grid arrows can be combined to land exactly on 5, 13 or 3.

### Week 164: Borromean rings (draft)

- **K–1, workable.** Hooking pipe-cleaner chains is easy fun and untwisting one ring so the other two fall free is a great magic moment, but the adult will build the magic three for them.
- **2–3, strong.** Choosing who is on top at each crossing, lifting to test, and sorting 8 patterns into 'falls apart' and 'holds together' is a concrete, self-checking hunt with a surprise answer (only 2 hold).
- **4–5, workable.** The four-loop Brunnian chain is a good challenge but unrehearsed, and scoring crossings with a hand rule to get 0 is abstract bookkeeping whose point (0 does not mean unlinked) needs careful adult talk.
- **Best moment:** Three rings hang together from one hand, no two are hooked, and untwisting any one drops the other two.
- **Biggest problem:** Weaving the third ring and the four-loop chain are fiddly and unrehearsed, and the 4-5 linking number is an abstract scoring exercise.
- **One change:** Give 4-5 more physical challenges (build a four- or five-ring Brunnian chain with rubber bands, design one) and keep the crossing-score as a short demo.

### Week 165: Inside or outside? (draft)

- **K–1, workable.** Jumping in and out of rope loops and checking by walking without stepping over is joyful and physical, but the odd/even rule is something the adult tells them rather than something they find.
- **2–3, strong.** Deciding quickly for bugs on tangle sheets, checking by colouring, and designing a trick loop for a partner is game-like, independent and has a satisfying shortcut to discover.
- **4–5, workable.** Why each crossing switches and where the rule breaks (corners, edges, self-crossings, the star's centre) is good reasoning, but much of it is discussion, and it overlaps other self-crossing and winding drafts.
- **Best moment:** A toy deep in the rope spiral: the room votes, one child walks out counting rope crossings, and the count settles it.
- **Biggest problem:** The rope spiral needs floor space and rehearsal, and the 4-5 part leans on talk rather than doing.
- **One change:** Give 4-5 a concrete challenge, such as drawing a loop where some ray has to pass through a corner and fixing the count, or two-colouring a partner's self-crossing loop.

### Week 166: You can't comb a hairy ball (draft)

- **K–1, weak.** Covering a ball with arrow stickers so 'neighbours point almost the same way' is fiddly and vague for 5-year-olds, and they can't tell whether their calm spot is forced or just a sticker mistake; the combing launch is the only clear moment.
- **2–3, weak.** Trying for exactly one or two calm spots needs judging continuity of a hand-placed sticker field on a curved surface, which leads to disputes rather than discovery; the ring-versus-ball contrast is good but brief.
- **4–5, workable.** Indices and the 'total is always 2' pattern are a real discovery for 10-year-olds, but the pointer walk is new and abstract, and the cube net with springs, saddles and drains is adult-guided.
- **Best moment:** Combing a fluffy pompom and the tuft that always appears somewhere.
- **Biggest problem:** The core activity, a field of stickers on a beach ball, is too imprecise for children to see what forces a calm spot.
- **One change:** Use printed sphere and torus nets with pre-placed dots so children draw arrows on a grid, keeping the combing and the swim ring as the physical hook.

### Week 167: Walking a loop (draft)

- **K–1, workable.** Walking tape paths and dropping a peg on the left or right card at each turn is physical and kids can do it, but the 'always one full turn' comparison of piles needs adult help, and the turn dial is fiddly.
- **2–3, strong.** Drawing a wild grid loop for a partner and predicting 'left minus right is always 4' is a crisp, checkable surprise, and crossing loops making 0 or 8 is a good follow-up.
- **4–5, workable.** Turtle stars with 72, 144 and 135 degree turns are hard to draw by hand, so it becomes prediction on paper; the rule is good but the concrete action is thin without a turtle program or pre-printed paths.
- **Best moment:** However wiggly the loop, left turns minus right turns always come out the same.
- **Biggest problem:** Taping five floor paths is a lot of prep, and the 4-5 turtle part has little concrete action.
- **One change:** For 4-5, give angle cards for walking turtle stars on a big floor (or a simple Logo screen) so they act out the star before predicting.

### Week 168: Folding beats the compass (draft)

- **K–1, weak.** Halves and quarters are fine, but the 'magic fold' and the equilateral triangle are copied step by step after an adult and need precise folds that 5-year-olds can't make.
- **2–3, workable.** Haga's fold making exact thirds is a real trick and the pinch game converging to a third is satisfying, but folding accuracy limits what children see, and finding which fractions appear needs measuring.
- **4–5, workable.** Abe's trisection is a striking fold, but it needs a precise simultaneous placement that many 10-year-olds will botch, and the 'why' of the equilateral fold is the stronger task.
- **Best moment:** One fold makes exact thirds, checked by folding the paper so the pieces match one-to-two.
- **Biggest problem:** Most moves are procedures copied from an adult and judged by folding precision rather than reasoning.
- **One change:** Centre 2-3 and 4-5 on open exploration of Haga's fold (fold a corner to any edge point and find what fractions appear), with the trisection as an optional demonstration.

### Week 169: Stacking oranges (draft)

- **K–1, workable.** Stacking balls into pyramids is concrete and fun, and seeing a ball roll into a hollow is a good discovery, but ping-pong balls roll everywhere in a noisy room and need frames and non-slip mats.
- **2–3, workable.** Predicting pyramid counts before building is a good pattern task, but the box comparison (64 vs 66) shows almost no difference, and counting the 12 touching balls in a big stack is hard to see.
- **4–5, workable.** Finding triangular layers on the slanted face of a square pyramid is a nice 3D aha, but the cannonball part is a table lookup and the Kepler material is mostly story.
- **Best moment:** Spotting that the slanted face of the square pyramid is a triangle of balls, the same stack seen another way.
- **Biggest problem:** The headline comparison of stacking methods gives an unconvincing difference, and loose balls make building frustrating.
- **One change:** Use a taller box or count balls per layer area so the straight-up versus hollows difference is clear, and supply frames that keep balls from rolling.

### Week 170: Rep-tiles (draft)

- **K–1, strong.** Making a bigger copy of a pattern block from copies of itself is easy to understand, self-checking and quick, and the hexagon refusing to double is a real surprise.
- **2–3, strong.** Building the big L from four Ls and then from 16 is a satisfying puzzle with a countable pattern, and testing which tetrominoes double gives a clear yes/no hunt.
- **4–5, strong.** The sphinx double needing flips is a genuinely tricky puzzle, and folding A4 against letter paper gives a nice real-world aha about the square root of 2 ratio.
- **Best moment:** Four small sphinxes, three of them flipped, clicking into one big sphinx.
- **Biggest problem:** Cutting about 70 L-trominoes and the sphinxes per table is well over a parent's 30-minute prep.
- **One change:** Make Ls from square tiles or snap cubes (or buy polyomino sets) and pre-tape 16-blocks, so cutting is limited to the sphinxes.

### Week 171: Shared birthdays (draft)

- **K–1, workable.** Rolling a die for each teddy and seeing whether two land in the same box is easy and fun for a minute or two, and dropping cubes into two cups is a fine tally. But comparing the cup towers is a probability idea with no surprise for children who had no expectation in the first place, so after a few parties it turns into repetitive rolling.
- **2–3, workable.** Rolling parties of 3 to 6 guests on a 12-box calendar is quick and children can run it themselves, and 'why are 13 always enough?' is a real pigeonhole aha. But separating 4 guests (43%) from 5 (62%) needs about 30 parties per size, so most of the hour is rolling and tallying for a margin the pooled chart may not show clearly.
- **4–5, workable.** Counting pairs (10 in a party of 5, 253 in 23) and multiplying 11/12 x 10/12 x ... to get 38% is a real reason behind the data, and the 'someone shares MY birthday needs 253 people' contrast can produce a gasp. Multiplying fractions with a calculator is abstract, and the famous surprise lives on a 365-day calendar that the class never actually experiences.
- **Best moment:** A party where children bet 'no match' and the fifth roll lands on an occupied box, again and again, until the class chart shows that shared boxes are winning.
- **Biggest problem:** The surprise depends on a wrong intuition that young children don't have yet, and the evidence needs long repetitive rolling and pooling.
- **One change:** Open with a betting game in which each child stakes a counter on 'match' or 'no match' before each party, so the surprise is felt in their own wins and losses rather than read off a pooled tally.

### Week 172: First digits (Benford) (draft)

- **K–1, weak.** Sorting cards with big printed numbers by their first digit shape and building towers is something children can do, but the numbers mean nothing to them, the deck is simply handed over, and 'one deck makes a staircase' has no reason they can reach. It is a sorting chore with a modest visual payoff.
- **2–3, workable.** Doubling from a number they chose with a calculator and adding first-digit stickers to a class chart is quick, and the doubling map (anything starting with 5 to 9 doubles to a number starting with 1) is a genuine aha they can find themselves. Doubling by hand past 1000 turns into arithmetic practice, and the class chart needs many stickers before 1 clearly wins.
- **4–5, workable.** Listing the powers of 2 by digit length and noticing that each group has exactly one starting with 1 is a pattern they can find and explain, and the unit-change extension is a nice twist. The explanation (3 or 4 powers per digit length, a share between 1/4 and 1/3) is good but a little dry, and the real-data hook is unchecked.
- **Best moment:** Discovering that every number starting with 5, 6, 7, 8 or 9 doubles to a number starting with 1, so the 1 column has to win.
- **Biggest problem:** The core activity is generating and sorting long numbers, which feels like processing data more than playing, and the joy depends on an anticipation of 'all digits equal' that children may not have.
- **One change:** Build the session around the doubling-map arrows as a board game (a token moves along first digits as you double) so children feel why 1 keeps being visited, with the sticker chart as confirmation.

### Week 173: How long does Snakes and Ladders last? (draft)

- **K–1, strong.** Playing Snakes and Ladders on a short board and adding a cube for every roll is something young children love and can do alone; lining up towers from shortest to tallest makes the spread visible. The mathematical question is light (shortest game, snakes covered), but they will happily replay it.
- **2–3, workable.** Asking which square is best or worst and whether removing a snake helps is a real question, but games average about 7 rolls with a wide spread, so the few games a pair can play give noisy answers and the class may draw the wrong conclusion. It is a pure luck game with no decisions, so the thinking happens only in prediction.
- **4–5, workable.** Working backwards on the coin strip is a beautiful idea, and 'a ladder that makes the game longer' is a real surprise. But the computation is fractions like 9/4, 23/8 and 153/64 with no physical action, so many 10-year-olds will need an adult to carry it, and the classic-board surprises need a computer.
- **Best moment:** Finding that adding a ladder can make the game take longer.
- **Biggest problem:** The fun part (playing) and the mathematical part (working back with fractions) are disconnected, and noisy small samples can mislead the middle band.
- **One change:** Give 4-5 the backward computation in 'out of 16 games' whole numbers on the board itself, and choose a small board where a harmful ladder changes the class's own game lengths visibly.

### Week 174: Shrinking piles (draft)

- **K–1, workable.** Pouring a cup of two-colour counters, taking away the reds and building a tower of what is left is hands-on and gives a satisfying staircase. Counting and building a tower each round is slow for 5-year-olds, and comparing staircases with neighbours is a mild observation rather than a surprise.
- **2–3, workable.** Predicting what is left after each pour is engaging, and 'doubling the pile adds only about one pour' is a real idea. But time-to-empty varies a lot (a spread of nearly 2 rounds) while doubling adds only one, so the pooled sticky notes from a few pairs may not show the pattern.
- **4–5, strong.** The mystery cup (a partner pours 64 counters secretly and shows what is left, you guess how many pours) is a genuine guessing game with a reasoning payoff that children can replay, and the dice-sixes half-life extension gives a fresh twist. The radiocarbon story adds a real-world wow.
- **Best moment:** Guessing from a handful of counters left in the mystery cup that the partner poured exactly four times.
- **Biggest problem:** The 2-3 headline pattern (one extra pour per doubling) is statistically too noisy to emerge from the data one class can generate.
- **One change:** Lead 2-3 with the predict-the-pile and mystery-cup games, and keep 'how many pours does a doubled pile last?' as a whole-class pooled question with many trials or an app run.

### Week 175: The chaos game (draft)

- **K–1, weak.** Marking halfway points with a stretched rubber band, 10 to 15 times, needs fine-motor accuracy that 5-year-olds lack, and every dot depends on the last, so errors compound. The payoff (holes in a stack of transparencies) only arrives at the end and may not appear at all with imprecise dots.
- **2–3, weak.** Thirty halfway measurements with a ruler along slanted lines (halving non-whole centimetres) is a long, error-prone chore for 7- and 8-year-olds. The stacked reveal could be a real gasp, but it arrives late and depends on accuracy they are unlikely to keep.
- **4–5, workable.** Ten-year-olds can measure reasonably and will get absorbed in why a dot can never land in the middle triangle, which is a lovely argument. The measuring is still a slog, and the picture is only convincing if the class stack is accurate enough.
- **Best moment:** Stacking every table's transparencies on a window and watching the empty triangles appear.
- **Biggest problem:** The activity's success depends on many precise measured dots, which is exactly what children are worst at, and the payoff comes only at the end.
- **One change:** Have children do a handful of hand jumps to learn the rule, then reveal the full picture with an app or projector run, and spend the main time on 'why can't a dot land here?' with half-size triangle cut-outs.

### Week 176: Hide the bean (mixed strategies) (draft)

- **K–1, strong.** Hiding a bean under cups and trying to outguess a partner is a game young children will play happily for a long time, and noticing that 'always blue' gets caught is within reach. The die recipe will mostly be an adult's idea, but the core play is theirs.
- **2–3, workable.** Testing recipes such as 'red on 1 to 4' against a seeker who knows the recipe is a good question, but comparing pooled cube totals from noisy random play is slow and may not separate the recipes clearly. Professor Swindle adds a nice 'looks fair but isn't' moment.
- **4–5, workable.** The equalising argument (make the seeker's two guesses equally good) is something ten-year-olds can reach, and Morra's 7/12 deck plus the adult mind-reader round give real surprises. But mixed-strategy reasoning is abstract and the long-run claims rest on averages they can't see in a few rounds.
- **Best moment:** The adult 'mind reader' predicting a child's supposedly random hiding again and again, then failing against a die.
- **Biggest problem:** The mathematics (a best random mix) is only visible in long-run averages, which children's few noisy rounds won't reveal.
- **One change:** Make the mind-reader round the launch, so children feel why a die beats their own 'random' choices before they look for the best mix.

### Week 177: Pirates share the gold (draft)

- **K–1, weak.** Wearing rank cards and holding gold coins is fun, but the voting rule (thumbs up only for more than you'd get after the captain walks) needs backward reasoning that 5-year-olds can't hold, so the adult does all the logic and children just vote by feeling.
- **2–3, workable.** Building up from small ships on a strip and finding the 1, 0, 1, 0 pattern works with a capable adult, and the captain keeping almost everything is a real gasp. The tie-break preferences (enjoying a splash, the proposer's casting vote) are a lot of rules, and children acting as pirates will vote out of fairness or spite rather than by the logic.
- **4–5, strong.** This is a classic puzzle with a shocking answer that ten-year-olds can reach themselves by working up from small ships, and acting it out makes the argument concrete. The power-of-two survivors for few coins is a deep extension for keen children.
- **Best moment:** Realising that the five-pirate captain keeps 98 coins and everyone still votes yes.
- **Biggest problem:** Children playing the pirates bring real feelings about fairness, which clashes with the cold self-interest the logic assumes, and the tie-break rules are easy to lose.
- **One change:** Put the three preferences (survive, then coins, then enjoy a splash) on one picture card, and have children predict each pirate's vote from the ship strip rather than voting as themselves.

### Week 178: Bidding for turns (draft)

- **K–1, weak.** Hiding chips in a fist and opening together is fun, but the rule that the winner pays the loser is counterintuitive and the star tie rule is beyond 5-year-olds. They will bid at random, so the 'spending everything hands it over' idea will have to be pointed out by an adult.
- **2–3, workable.** The flag race with 10 chips gives a real puzzle (how many chips guarantee a win?), and bidding tic-tac-toe is a fresh game children like. The star rule is the hardest part and will need rehearsed adult help, and the analysis of splits needs careful record-keeping.
- **4–5, workable.** Finding that 1 chip out of 10 wins a 1-against-3 race and that this matches the coin-flip chance of 1/8 is a striking surprise. But it rests on working back probabilities and an averaging argument that most children will test rather than understand, and the discrete star rule complicates the clean picture.
- **Best moment:** Winning the bidding race with just 1 chip against 9.
- **Biggest problem:** The rules (hidden bids, paying the opponent, the star tie-break) take most of the attention before any strategy can develop.
- **One change:** Drop the star for younger bands with a simple 'tie means both bid again' rule, and save the star for 4-5 once the race is familiar.

### Week 179: Sharing the taxi fare (draft)

- **K–1, weak.** Driving a toy taxi and laying cubes is pleasant, but the stretch-sharing rule is given by the adult and children only carry it out, square by square. There is no puzzle or surprise for them to find.
- **2–3, workable.** Arguing about what's fair is engaging for this age, and testing rules (equal split, by distance, by stretch) on new trips gives them something to check. Without a sharp script, the 'fair' argument may stall in opinions, and the payoff is a quiet conclusion rather than an aha.
- **4–5, workable.** Playing all six arrival orders and finding that the average equals the stretch rule is a genuine surprise, and testing which rules break which condition is good reasoning. Shapley's conditions, especially additivity, are abstract, and averaging six orders is somewhat procedural.
- **Best moment:** Averaging the six arrival orders and finding that the far friend pays exactly 3, the same as the stretch rule.
- **Biggest problem:** Most of the activity is carrying out sharing rules, with little tension or game, so the joy depends on a fairness debate that may not take off.
- **One change:** Open with a case where an obvious rule (equal split) makes a near neighbour pay more than a taxi of their own, so the class has an injustice to fix before comparing rules.

### Week 180: Who holds the power? (draft)

- **K–1, workable.** Three voters with 4, 3 and 2 cubes snapping towers to reach a line, and finding that any two win, is concrete and gives a small surprise (unequal stacks, equal power). It works with adults acting it out, but the 'needed' idea will mostly be shown by an adult stepping away.
- **2–3, weak.** Four voters and four quota lines mean listing up to 15 teams per line and checking each member for criticality, which is heavy bookkeeping for 7- and 8-year-olds. The discoveries (a 2-cube voter as weak as a 1-cube voter) are good but buried under the listing.
- **4–5, strong.** The Nassau board, where the 7-vote member equals each 9 and three members have no power at all, is a surprise ten-year-olds can argue for without listing everything, and the 'hunt for a dummy' is a good puzzle. The link to Week 179's arrival order is a nice extra.
- **Best moment:** Discovering that a voter holding cubes can never change the result.
- **Biggest problem:** The core method (list every team, test each member) is exhaustive bookkeeping that overwhelms the middle band.
- **One change:** For 2-3, use three voters on two or three quota lines and frame the dummy hunt as a challenge ('make a vote where someone with cubes never matters') instead of complete team listings.

### Week 181: A new road makes traffic worse (draft)

- **K–1, workable.** Being a car on a taped floor map and seeing that the new road made everyone slower is physical and memorable. But the switching rule and adding up trip times will be run by the adult, so 5-year-olds mostly walk where they're told and hear the result.
- **2–3, strong.** Moving counters on a map for 2 to 5 cars, finding settled arrangements and discovering that the shortcut helps 3 cars and hurts 4, is a real surprise children can find with small sums. Several equilibria from 5 cars on may need adult care.
- **4–5, strong.** Explaining why nobody leaves the shortcut (9 minutes against 8) and why 2 and 2 is still better for the group gives a satisfying argument, and Braess's and Pigou's numbers extend it. The paradox is a genuine 'wait, what?' that ten-year-olds will want to retell.
- **Best moment:** Opening the free shortcut, everyone taking it, and everyone arriving later than before.
- **Biggest problem:** Acting out one-at-a-time selfish switching on the floor needs strict turn-taking, and children may cooperate instead of acting selfishly, blurring the equilibrium.
- **One change:** Give each driver a personal goal card ('get home fastest, you win a sticker if you beat your old time') and a clear one-at-a-time switch turn, so selfish switching is part of the game.

### Week 182: Passing secrets by phone (draft)

- **K–1, workable.** Acting out calls with coloured cubes is concrete, and beating the adult's 6-call plan with fewer calls for four animals is a nice challenge. Taking the right cubes from the tray and following a call list needs adult support, so K-1 will partly watch.
- **2–3, strong.** Finding 4 calls for 4 people is a satisfying puzzle with a clear aha, and pushing to 5 in 6 and 6 in 8, beating the hub plan, keeps them going. The cube exchange can get slow with 6 people, but the call list is a light record.
- **4–5, strong.** Generalising the 4-chief plan and proving that 3 calls can't work for 4 people gives real reasoning, and the honest open gap (7 vs 8 for six people) is a good end. It is puzzle-driven with little bookkeeping.
- **Best moment:** Finding the 4-call trick (AB, CD, AC, BD) after trying and failing with more calls.
- **Biggest problem:** Physical cube exchanges with many colours get slow and error-prone as groups grow.
- **One change:** Use a printed strip of colour boxes to tick for groups of 5 or more, keeping cubes only for the first acted-out calls.

### Week 183: Can everyone get a partner? (draft)

- **K–1, workable.** Placing clips on lines to pair faces with animals on small mats is a manageable puzzle, and pointing to 'these three only like these two' is a nice idea. Crowded mats and clips on lines may be fiddly, and the stuck-group idea will need an adult to bring out.
- **2–3, workable.** Sorting mats into 'works' and 'cannot' and fixing a pairing by swaps is good puzzle work, and designing a failing mat where everyone has two lines is a nice challenge. Finding the short group on 5-face mats without prompting is hard, and tangled lines make scanning tiring.
- **4–5, strong.** The rook grid, where the most rooks always matches the fewest covering lines, is a clean surprise that ten-year-olds can test and check themselves, and the cover as proof is satisfying. Low reading and no bookkeeping.
- **Best moment:** Finding that the most rooks and the fewest lines always match, so the cover proves you can't do better.
- **Biggest problem:** On crowded mats, finding the group that blocks a pairing is a visual search that middle-band children may not manage without adult hints.
- **One change:** Draw the mats with few, clearly separated lines and colour-coded animals so the short group stands out, and grow mat size gradually.

### Week 184: Your friends have more friends (draft)

- **K–1, weak.** Yarn between animals is fun to set up, but comparing one's own tower with a group of friends' towers is an averaging idea 5-year-olds can't handle, and an adult ties and runs everything.
- **2–3, workable.** Passing sticky notes along yarn is physical and fun, and inventing a town where the piles tie is a good challenge. But computing averages like 20/8 and each animal's friends' average is beyond many 7- and 8-year-olds, and tangled yarn slows the activity.
- **4–5, workable.** The 4-friend animal writing 16 notes, hence the sum of squares, is a nice reason children can explain, and the result is surprising. Averages and fractions dominate, and the yarn set-up takes time before any thinking starts.
- **Best moment:** Seeing that the notes pile has a bigger average than the animals pile and realising popular animals write the most notes.
- **Biggest problem:** The core comparison is between averages, which is arithmetic-heavy and abstract for the younger bands, and the yarn network is slow to set up.
- **One change:** Use a printed network board with tokens instead of yarn, and compare piles by levelling cube towers instead of computing averages.

### Week 185: One-way streets (draft)

- **K–1, workable.** Putting arrow cards on a ring and driving a toy car round is concrete and fun, and the dead-end lane that always traps the car is findable. Checking both 'reach every house' and 'get back to school' is a lot to hold in mind, so an adult will run the second check.
- **2–3, workable.** Finding a good plan on the 3-by-3 town is a real puzzle and the Manhattan rule failing at a corner is a nice surprise. Testing all 12 roads by driving the car from every crossing and back is slow, and errors are easy to miss without a systematic check.
- **4–5, strong.** Why one lifeline road ruins every plan is an argument they can make with the car, and building a plan loop by loop is a satisfying constructive idea. The even-streets rule for alternating grids gives a checkable conjecture.
- **Best moment:** Flipping one arrow on the ring and finding a house the car can leave but never get back to.
- **Biggest problem:** Checking that a plan works needs two full reachability sweeps, which turns into slow car-driving bookkeeping on the bigger maps.
- **One change:** Give the two-way test a physical shortcut, such as a 'leaving' car and a 'returning' car, or a single round-trip loop that has to pass every house, so checking a plan takes one quick drive.

### Week 186: Counting trees on numbered pegs (draft)

- **K–1, weak.** Building straw networks is fine for the hands, but deciding when two labelled trees are 'different' (a different pair joined, not just turned) is a subtle convention for 5-year-olds, and drawing each tree on a recording card is fiddly.
- **2–3, workable.** Hunting all 16 four-peg trees as a pooled class collection has a nice target and the 12-lines-4-stars split is satisfying. Spotting duplicates and recording accurately will take adult help.
- **4–5, workable.** Counting numberings of a shape as 4! or 5! divided by its symmetries and seeing the shapes add to 125 is a real aha. It overlaps heavily with existing AD-04 and draft 150, so it is a return visit rather than fresh joy.
- **Best moment:** Adding up the shape counts on 5 pegs (60 + 60 + 5) and landing exactly on 125 = 5 x 5 x 5.
- **Biggest problem:** The core activity is listing and deduplicating labelled trees, which is bookkeeping-heavy and depends on a sameness convention young children find arbitrary.
- **One change:** Drop it as a separate week and run the symmetry-counting hour as a 4-5 return visit to AD-04, giving K-1 only the 3-cup sort.

### Week 187: Coin forests (percolation) (draft)

- **K–1, weak.** Flipping 25 coins and placing 25 stickers is a long chore governed by luck, and a crossed-or-stuck pile has no decision in it. Finger-tracing the fire is fun but brief.
- **2–3, workable.** The class tally landing near a half, and the die rules shifting it sharply, can surprise them, and hex against square is a good question. Most of the time is spent flipping and stickering, and the payoff only appears once boards are pooled.
- **4–5, workable.** The exact-half argument via Hex (one crossing always happens, then colour swap) is a real aha if they have played Hex first. Filling 49- or 81-cell boards by coin is tedious; colouring boards by choice would be faster.
- **Best moment:** Trying to colour a hex board so that nobody crosses and finding it is impossible, while on squares it is easy.
- **Biggest problem:** Minute-to-minute work is coin flipping and sticker placing with no choices, and the interesting pattern only appears after a class tally.
- **One change:** Lead with the deliberate challenge (colour a board so neither side crosses, on hexes and squares), and fill the random boards fast with a die per row or a pre-printed random deck.

### Week 188: Small worlds and shortcuts (draft)

- **K–1, workable.** Standing in a yarn ring and passing a bean bag is lively, and seeing one shortcut cut the passes is easy to feel. Counting passes is all they do, and it needs a whole room of children, so it fails at a kitchen table.
- **2–3, workable.** Finding the farthest pair on a 16-dot ring, and discovering that a shortcut straight across leaves it unchanged, is a genuine surprise. Placing 2 shortcuts to minimise the farthest distance is a good puzzle, but average distance means a lot of tallying.
- **4–5, workable.** Comparing planned with random shortcuts and guessing the 1000-person distance is interesting. Computing distances on many pooled random rings is a bookkeeping chore, and the log2 n theorem can only be told, not found.
- **Best moment:** Adding a shortcut straight across the ring and finding the two people farthest apart are still exactly as far apart as before.
- **Biggest problem:** The physical ring needs many children, and the paper version quickly becomes distance-counting tables.
- **One change:** Centre the paper work on the 'farthest pair' optimisation puzzle (best spots for 1, 2, 3 shortcuts) and drop average distance to a guide-only note.

### Week 189: Guessing your own hat (draft)

- **K–1, weak.** Wearing headbands and revealing on three is fun, but the outcome is pure luck to them, and sorting the 8 hat-row cards under a rule is adult-led abstraction they will watch rather than do.
- **2–3, workable.** Hunting a three-player rule that wins as many of the 8 rows as possible is a crisp puzzle with a record (6 of 8). The bridge from the played game to the 8-card sort needs careful adult framing.
- **4–5, strong.** The pass-if-different rule winning 3 out of 4 when each guess is still a coin flip is a real surprise, and the dot-balance argument for why 7 of 8 is impossible is within reach with the cards.
- **Best moment:** Finding that a team can win 6 of 8 rows even though every single guess is still right only half the time.
- **Biggest problem:** For young children the game is all luck, and the counting tool that reveals the mathematics is abstract.
- **One change:** Make the 8-card deck the game board from the start (deal a row card, each player covers their own face and decides), so play and counting are the same action.

### Week 190: Follow the loop (prisoners and boxes) (draft)

- **K–1, workable.** Lifting a cup, reading the number and going to that cup until you find your own is a lovely, doable chase with numbers to 6. The team game with cup resets between players is slow and the win/lose rule may feel unfair.
- **2–3, workable.** The loop rule winning far more often than random lifting is a striking result. Shuffling 10 cups many times and recording the longest loop is repetitive simulation.
- **4–5, strong.** Counting the 24 orders of 4 cups by loop pattern to get 10 wins, why only one loop can be too long, and the helper's one-swap rescue are crisp, checkable arguments with a big payoff.
- **Best moment:** Realising that with the loop rule the whole team either all wins or all loses together, and wins about 4 times in 10 instead of almost never.
- **Biggest problem:** The team game needs an adult to reset hidden cups between players, and the 10-cup statistics turn into repeated simulation.
- **One change:** Play the team game with each player's lifts checked on one shared laid-out shuffle (look at the arrows, not the cups) so no reset is needed and kids see the loops directly.

### Week 191: Look-and-say (draft)

- **K–1, workable.** Saying a short row aloud and building it is a fun riddle for the first five rows, and discovering 22 never changes is delightful. Mixing count cards with colour cubes is a confusing double representation for 5-year-olds, and rows soon get too long.
- **2–3, workable.** Spotting 'only 1, 2, 3 ever appear' and 'every row ends in 1' is a real pattern hunt. Ten rows by hand means transcribing 20-plus digits with compounding errors.
- **4–5, strong.** Explaining why a 4 never appears, finding the row before 312211 and deciding that 1111 can never be a reading are short, satisfying puzzles. The backward game is checkable without long rows.
- **Best moment:** Cracking the 1, 11, 21, 1211 riddle and then finding that the start 22 just reads itself forever.
- **Biggest problem:** Rows grow fast, so after a few minutes the activity becomes error-prone copying of long digit strings.
- **One change:** Keep forward rows short (first six) and make the backward game, 'which strings can be readings', the main task for 2-3 as well as 4-5.

### Week 192: Short codes for common letters (draft)

- **K–1, workable.** Walking turn messages on a taped floor tree and calling out pictures is physical and fun. Comparing two trees by counting turns is fine with cubes, though 'jump back to the root' needs a clear marker.
- **2–3, workable.** Designing a tree that makes ABRACADABRA as short as possible with a class record is a good competitive puzzle. Counting 11 letters' worth of turns per attempt is tedious; a shorter message would help.
- **4–5, strong.** Discovering 'join the two rarest' and seeing it beat everyone's hand-made trees is a real aha. The tree-budget reason why lengths 1, 1, 2 are impossible is graspable.
- **Best moment:** Finding a gap-free message on a badly built code that can be read two different ways.
- **Biggest problem:** Counting the total message length for each candidate tree is arithmetic bookkeeping, and the topic largely duplicates atlas AP-29.
- **One change:** Use a shorter message with a 4-letter alphabet for 2-3 and have each letter's count printed on its card, so a tree's cost is count times depth summed quickly.

### Week 193: Langton's ant (draft)

- **K–1, weak.** Being the ant on a floor of plates is fun for a few steps, but left and right turns are unreliable at 5, one error ruins everything after it, and most children are waiting while one walks.
- **2–3, workable.** Running 50 to 100 steps by hand is a long error-prone procedure, but the computer showing chaos and then the highway near step 10,000 is a genuine gasp. The run-backward game is a nice puzzle.
- **4–5, workable.** Why moves alternate and why the rule can run backward are graspable, but the unboundedness proof is a facilitator story they follow rather than find. The honest 'nobody knows' open question is appealing.
- **Best moment:** Watching the computer ant scribble chaotically for 10,000 steps and then suddenly build a straight highway.
- **Biggest problem:** The hands-on part is a long rote simulation where one mistake spoils everything, and the real surprise only comes from watching a computer.
- **One change:** Keep hand simulation to about 20 steps with a partner checker, and give children the computer for experiments of their own (add one black square, predict, run).

### Week 194: Hilbert's hotel and the diagonal (draft)

- **K–1, weak.** With three rows of three, making a row that is not on the list is trivial by trial, and the diagonal recipe is handed to them as a procedure, so there is nothing to discover and no infinity.
- **2–3, workable.** The 'everyone move up a room' stories are fun to act out, and finding a method that beats any list a partner makes is a good two-player challenge. 'Same size' for endless collections is slippery at 7 or 8.
- **4–5, strong.** Ten-year-olds love infinity paradoxes, and the diagonal move that beats any list is a short, famous argument they can actually make with counters.
- **Best moment:** A full endless hotel fits a busload of endlessly many new guests when everyone moves to double their room number.
- **Biggest problem:** The concrete counter game is weak at small sizes, because any missing row is easy to find without the diagonal, so the power of the idea only shows abstractly.
- **One change:** Play the diagonal as a race on longer lists (6 or 8 rows of 6 or 8) where trial and error is hopeless and the diagonal wins instantly, and drop the K-1 version.

### Week 195: Ordering stones with a balance (draft)

- **K–1, workable.** A balance and mystery containers are irresistible, and a knockout to find the heaviest is easy to run. 'Sometimes 2 weighings, sometimes 3' is noticeable, but worst-case thinking is beyond most 5-year-olds.
- **2–3, workable.** Ordering 4 in the fewest weighings is a good challenge, but with real containers the outcomes are fixed, so a lucky child 'wins' in fewer and 'always works' stays abstract. Drawing a method as a branching tree will need an adult scribe.
- **4–5, workable.** The counting bound (64 endings are too few for 120 orders) is a nice argument, but the 5-in-7 plan is intricate and will mostly be fed through guide hints.
- **Best moment:** Realising that 6 weighings can never be enough for 5 stones, because there are more orders than possible weighing stories.
- **Biggest problem:** Fixed physical weights cannot play the tricky worst case, so the central idea of a method that always works is hard to experience, and the balance kit needs careful preparation.
- **One change:** Have a partner or adult secretly decide each weighing's answer as an adversary (or reshuffle contents between tries) so children face the worst case directly.

### Week 196: Change ringing (draft)

- **K–1, workable.** Children as bells swapping places with neighbours is lively and physical, and 6 line-ups of 3 is a manageable target. Spotting repeats and laying the ladder record will need an adult.
- **2–3, workable.** Plain hunt coming home after 8 rows instead of 24 is a real surprise, and flipping printed row cards on a wall chart makes repeats visible. A 24-row extent is long for bodies on the floor, so it moves to cards.
- **4–5, workable.** Building the 4-bell extent by letting bell 4 weave through the 3-bell rows is a satisfying construction. The coset reason why Plain Bob never repeats will mostly be adult explanation.
- **Best moment:** The plain-hunt dance on four bells unexpectedly arriving back home after only 8 of the 24 line-ups.
- **Biggest problem:** The 24-row extent is a long sequence where one slip spoils the record, so it risks becoming a procedure the group follows rather than a puzzle.
- **One change:** Make the 4-bell task a card puzzle on a 24-card wall chart with a ready-made partial ladder to complete or fix, keeping bodies for 3 bells and plain hunt.

### Week 197: Star patterns from crossing lines (draft)

- **K–1, weak.** Turning one paper square on another to make an eight-pointed star works, but most of the plan needs extending ruled lines on dot paper until they meet, which is beyond 5-year-old fine motor control.
- **2–3, workable.** Drawing X's and watching stars appear when the grid is erased is a real visual payoff, and comparing dot-step rules is a good question. Accurate ruler work across a whole grid is slow and error-prone.
- **4–5, workable.** Linking contact angle to joining midpoints and hunting the pattern's symmetry with tracing paper is rich. The 22.5- and 67.5-degree angle strips and the 'star has 8-fold but the pattern doesn't' argument need adult support.
- **Best moment:** Erasing the plain grid and seeing a field of stars appear from lines they drew themselves.
- **Biggest problem:** The core action is precise ruled drawing over many cells, so young children spend their energy on fine motor work rather than on noticing.
- **One change:** Provide printed sheets with all candidate lines drawn faintly so children choose and trace or colour lines, keeping the angle choice and the discovery without the precision drawing.

### Week 198: Nibble a tile (draft)

- **K–1, workable.** Cutting a nibble, taping it across and decorating a creature is a craft they will enjoy, and the flipped-nibble row that will not close is visible. Cutting and aligned tracing will need help.
- **2–3, strong.** On grid card, 'where can the nibble go so the floor still slides together' has clear, checkable answers and a surprise (anywhere along the bottom works, never a side). The pentomino sliding hunt is a good pooled task.
- **4–5, strong.** Matching opposite boundary pieces, the Conway half-turn spin, and which pentominoes need turning give real design-and-explain problems built on a hands-on craft.
- **Best moment:** Sticking the nibble somewhere else along the bottom edge and finding the floor still works, with the rows sliding sideways.
- **Biggest problem:** K-1 tracing and cutting accuracy may be too rough for a fit or a clash to show clearly.
- **One change:** Give K-1 pre-cut grid-square tiles with nibbles that snap to the grid, so whether the floor works is unambiguous.

### Week 199: Steering a card with perfect shuffles (draft)

- **K–1, weak.** Every shuffle means moving all eight cards at once along an arrow mat to a second mat. A five-year-old will lose cards or mix up arrows, so an adult ends up doing the shuffles. The mirror-colour observation means little at this age.
- **2–3, workable.** Hunting for the in/out word that sends the star card to each spot is a real puzzle with a pattern to notice (1, 2, 4). Counting places from 0 is unnatural, and every trial costs a full eight-card shuffle, so it needs a steady adult and patience.
- **4–5, workable.** The realisation that the steering word is the place written in binary is a genuine aha, and '8 of 24 orders with 4 cards' is a nice impossibility. Whole-deck shuffling is slow and error-prone, and the material overlaps Week 3 heavily for returning children.
- **Best moment:** A 4-5 child predicts 'in, out, in' for spot 5, shuffles, and the star card lands exactly there.
- **Biggest problem:** The core move, a whole-deck shuffle done by hand or by arrow mat, is slow and error-prone, so experiments get buried in card handling.
- **One change:** Let children track only the star card's position with the rules 'double' and 'double and add one' on a number strip, and save whole-deck shuffles for checking a prediction. Fold the week into a Week 3 return visit.

### Week 200: Kaprekar's sorting machine (draft)

- **K–1, weak.** The two-digit version hands children a gap chart that turns the gap into two mystery cards. They follow a lookup procedure without seeing why, so the loop they walk is an adult-made circuit rather than something they discover.
- **2–3, workable.** Landing on 495 from every start is a real surprise, but getting there takes several three-digit subtractions with regrouping, which can make the hour feel like arithmetic drill. Pooling the nine first answers is a good collective proof if a calculator or subtraction strip carries the arithmetic.
- **4–5, strong.** With a calculator every start mysteriously falls to 6174, children race to find a 7-step start, and the question of why 3524 and 5432 give the same answer leads to a proof by 54 shared cases they can actually finish.
- **Best moment:** A whole table discovers that everyone's different four-digit number ended at the same 6174.
- **Biggest problem:** Below grade 4 the machine is either long hand subtraction or an opaque lookup chart, so younger children run a procedure instead of exploring.
- **One change:** Allow calculators for 2–3 after one hand-worked step, and give K–1 a sorting and comparing task with digit cards rather than the gap-chart lookup.

### Week 201: Prime pairs (Goldbach) (draft)

- **K–1, workable.** Standing two ready-made towers beside a target to match its height is a clear, hands-on matching puzzle. Finding that 11 can't be made is a small surprise. The towers being 'prime' means nothing to them, so it's light number play.
- **2–3, workable.** Filling a chart of even numbers to 50 is mostly addition-fact listing. The questions about which numbers have the most ways, and why odd numbers need a 2, give it some point. Pooling keeps the load down, but the excitement is modest.
- **4–5, workable.** The odd-number proof and the 'nobody has proved it, but it's checked to 4 × 10¹⁸' story give older kids a thrill. Still, the minute-to-minute work is filling in a chart of sums up to 100.
- **Best moment:** Learning that a statement a child can check in a minute has defeated every mathematician for 280 years.
- **Biggest problem:** The hands-on work is listing prime sums, which gets repetitive. The interesting part, an open problem, is something to talk about rather than something to do.
- **One change:** Make it a hunt: teams race to find an even number with exactly one way, or the number below 100 with the most ways, rather than filling every row of a chart.

### Week 202: Halfway to the wall (draft)

- **K–1, workable.** The halfway walk is a fun body launch, and folding and colouring a strip is concrete. After four or five folds the pieces are too small to colour, and 'is there always white left?' needs an adult to make it land.
- **2–3, workable.** Shading one of four corners again and again and finding that the shaded part is one third is a real surprise. Cutting and stacking ever-smaller bands is fiddly, so pre-printed nested squares would help.
- **4–5, strong.** The 'three equal squares' picture proof, Achilles catching the tortoise, and 'is 0.999… really 1?' reliably spark argument and conviction at this age. Each child can draw and defend a proof.
- **Best moment:** The child walking halfway ends up shuffling heel-to-toe while the room shouts about whether they'll ever touch the wall.
- **Biggest problem:** After the first few folds or cuts the pieces are too small for small hands, so younger bands lose the concrete action just as the idea gets interesting.
- **One change:** Give K–3 large pre-printed strips and squares with the nested pieces already outlined, so they colour and compare rather than fold and cut tiny regions.

### Week 203: Press it again (draft)

- **K–1, workable.** Clips crowding together on the ribbon and then flipping it to find the hidden marks is a real magic moment. The two-step fold-and-move rule is a lot to repeat accurately, so an adult will often do the folding.
- **2–3, workable.** Pressing √ over and over is irresistible, and a million collapsing to 1 is a laugh. Children this age can't read the long decimals, though, so 'where does it settle' becomes 'when does the screen stop changing', and the extra machines need typed keystrokes each round.
- **4–5, strong.** Sorting machines into 'settles', 'flips' and 'runs away' by pressing buttons is fast, physical experimentation with surprises (cos always reaches 0.739). The race against averaging gives a vivid sense of speed, provided there are scientific calculators.
- **Best moment:** Flipping the ribbon over to find that every clip ended on the hidden one-third and two-thirds marks.
- **Biggest problem:** It depends on materials: cheap calculators lack cos and radian mode, and the ribbon fold rule needs careful repetition, so the experiment can fail for reasons that have nothing to do with the math.
- **One change:** Use machines on cards (halve and add 1, double and subtract 3, and so on) worked on a simple calculator or a number line, so 2–3 can sort machines without needing decimals or scientific keys.

### Week 204: The fastest slide (draft)

- **K–1, strong.** Marble races between a straight ramp and a bent one, with a vote first, are pure joy. Bending a track to beat the straight one is something a five-year-old can try again and again.
- **2–3, strong.** Changing only the shape and finding that the shortest ramp loses, and that a dip below the finish can still win, is a genuine 'wait, what?' backed by children's own races.
- **4–5, strong.** The same racing plus 'speed comes only from dropping' gives older kids a reason they can state. The tautochrone (different heights arriving together) is a showstopper if it works on homemade track.
- **Best moment:** The marble on the curved track that dips below the finish beats the straight one, against nearly every vote.
- **Biggest problem:** Homemade flexible track or cardboard channels may not hold a smooth curve or keep marbles on, and the time differences on a short course may be too small to see.
- **One change:** Rehearse and fix one reliable 1 m-wide course (for example foam pipe insulation cut in half on a cycloid template) before running the session.

### Week 205: Pi from polygons (draft)

- **K–1, workable.** Wrapping string round cans and marking off 'three and a bit' across-lengths is concrete, and fanning plate wedges into a strip is satisfying. Cutting and handling string accurately needs an adult, and the payoff is a mild observation.
- **2–3, workable.** Measuring several objects and finding the same 'three and a bit' every time is a nice constant to discover. Measurement error, comparing lengths and counting about 300 grid squares can make it feel like a measuring and counting chore.
- **4–5, workable.** Trapping π between hexagon and 12-gon perimeters and explaining the wedge rectangle is good reasoning. Most of the time goes to careful measuring, the gasp is limited, and some children will already 'know 3.14'.
- **Best moment:** A bucket, a coin and a plate all give 'three and a bit' when children lay out the across-lengths.
- **Biggest problem:** The core action is accurate measuring and counting, which is slow and error-prone, and the surprise that every circle gives the same number is a quiet one.
- **One change:** Drop the grid-square count and frame the string task as a challenge: find a round thing that is NOT three and a bit, using big hoops and buckets so measurement is reliable.

### Week 206: Folding the square root of two (draft)

- **K–1, weak.** Cutting the biggest square repeatedly from A-paper needs precise folds and cuts on ever-thinner strips. The 1, 2, 2, 2 versus 1, 3 counts mean nothing to a five-year-old, so an adult does the cutting.
- **2–3, workable.** Building two equal tile squares and trying to make one big square, then finding near-misses (5+5 against 7×7), is a concrete hunt with a surprise. The 12-and-17 case needs nearly 300 tiles and a lot of counting.
- **4–5, workable.** The overlap picture and the endless 'two again' square-cutting can give a real 'it can never stop' moment. Infinite descent is abstract, though, the fold argument involves an impossible square, and paper precision fails after a few rounds.
- **Best moment:** Laying 49 tiles beside two 5-by-5 squares and finding it is off by exactly one, then finding it happens again with 12 and 17.
- **Biggest problem:** The proof is the point, and it is abstract, while the physical square-cutting that should make it concrete breaks down from paper imprecision after three or four rounds.
- **One change:** Centre the hands-on work on the tile near-miss hunt with a grid sheet instead of loose tiles, and present square-cutting on a pre-drawn large diagram rather than real paper.

### Week 207: Random walks home (draft)

- **K–1, workable.** Flipping a coin and stepping on a floor number line is active and fun for a few walks. Some walks drag on for 30 or more flips with nothing to decide, and 'did everyone get home' is all they take away.
- **2–3, workable.** Odd-flip impossibility and listing the four-flip paths are good puzzles. The class average shifting as long walks arrive is interesting, but it takes many walks and a lot of recording.
- **4–5, weak.** The real ideas (a certain return with an infinite average, recurrence depending on dimension) can't be seen from a class chart, and the road argument assumes Week 91. Children mostly flip and wait while the punchline stays an adult's claim.
- **Best moment:** A walker who drifted out to +9 finally stumbles back to 0 and the room cheers.
- **Biggest problem:** The activity is long luck-driven simulation, and the surprising theorems (infinite average time, 3D transience) are not visible at the scale children can simulate.
- **One change:** Run short capped walks for the launch, then shift the main work to the four- and six-flip path-counting puzzle, and leave the infinite-average and dimension story to a brief adult demonstration or the app.

### Week 208: Long runs (draft)

- **K–1, workable.** Building a red-and-blue cube tower by coin flips is fun and easy. Many five-year-olds won't grasp making a 'pretend random' tower, so the detective contrast needs adult framing.
- **2–3, strong.** Making a real and a fake 20-flip strip and trying to fool another pair is a game kids want to replay. Spotting that real strips have surprisingly long runs is an aha they find themselves.
- **4–5, strong.** The detective game plus predicting the longest run in 100 flips, and the '1 in 64' explanation, give real reasoning on top of a fun hook. 100 flips is tedious unless shared or done with a cup of coins.
- **Best moment:** The detectives point at a strip with five heads in a row and declare it fake, and it turns out to be the real one.
- **Biggest problem:** The 100-flip recording for 4–5 can become a tedious transcription chore that eats time.
- **One change:** Use the tip-a-cup-of-10-coins method for the 100-flip grid, so recording takes minutes and the time goes to predicting and detecting.


