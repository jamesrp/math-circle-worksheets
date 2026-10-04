"""Adult-only prose, written separately from the tested student workflow."""
GUIDES={
11:{'topic':'Chip-firing return visits',
'overview':r'''\textbf{Facts and limits.} On a finite undirected sink graph with finite nonnegative chip piles, each legal firing sends one chip along every incident edge. With every working vertex connected to an absorbing sink, every legal run continued until no move is available terminates, with the same finish and firing counts. Without a sink, termination may fail. If a start does admit legal stabilization, its complete legal runs still have unique finish and firing counts, even without a sink. On a closed triangle, total chips are conserved: a stable placement holds at most three. Even at that total, some starts stabilize and others cycle.

A one-chip addition to a stable state can start a cascade. On the four-cycle \(S-A-B-C-S\), all working thresholds are two. The largest avalanche from a stable start has four firings, not three: the middle vertex can fire twice. This maximum is specific to this board and the one-chip perturbation.

A finish does not determine its past. On the sink triangle each firing loses one chip to the sink. Finishing at \((1,1)\) after four firings fixes the initial total at six, but leaves three possible starts and eight legal histories. Formal balance alone does not guarantee a proposed word is legal.

\textbf{Children's destination.} Separate the reason a run stops from experiments where it happens to stop; notice propagation through occupied neighbors; reconstruct and check legal histories rather than assuming a unique past.

\textbf{Entry map.} Problem 1: K--1 with oral rules, small counting and an adult recording the run. Problem 2: grades 2--3 and up, distinguish a stable start from its one-chip perturbation. Problem 3: grades 4--5, small arithmetic and backwards reasoning; a counter reconstruction is sufficient, without algebra.

\textbf{What is new.} The base tests sink-board order independence, staged additions and repeated addition cycles. Problem 1 expands the sink-free cycle seed already suggested in the base adult guide's optional closed-board continuation (p. 12 as read October 4, 2026) into contrasting stabilization, cycle and capacity work. Problem 2 optimizes cascade length from stable starts. Problem 3 reuses the six-chip starts from base grades 2--3 Problem 3, but its new target is every legal firing history and the missing orders. They are three investigations within one chip-firing theme.''',
'materials':'For each working pair, 12 counters no wider than 20 mm, one board, pencil and spare paper/whiteboard. For the current five pairs plus upper-table third child, reserve 72 counters so each table can compare two starts. Printed working circles should be at least 42 mm and sinks at least 55 mm; stack piles rather than spread chips across lines. No exact fit or existing stock has been physically checked.',
'launch':'Let children handle chips freely. On a sink board, place a small legal pile and ask a child to send one chip along every touching line. Show that extras remain and the sink never sends chips back. Write the fired circle’s letter after each move; a second letter is appended, not substituted. Then cover the sink label with C and show that the sink-free triangle is a separate board with a different rule, not a continuation of the old trial. A partner touches all recipient lines before the chips move.',
'route':'Start Problem 1 with three chips; offer the four-chip impossibility question after a real run. Start Problem 2 with an empty stable board and a single addition, then a board with some ones. Save Problem 3 for children who can restart a trial reliably and keep a four-letter move record. If they completed base grades 2--3 Problem 3, start from their known three starting states and investigate all legal histories rather than repeat that search.',
'solutions':[
r'''\textbf{Problem 1: removing the escape.} On the closed triangle every vertex has degree two. From \((3,0,0)\), firing A gives \((1,1,1)\), which is stable. From \((2,1,0)\), the forced run is
\[
(2,1,0)\xrightarrow{A}(0,2,1)\xrightarrow{B}(1,0,2)\xrightarrow{C}(2,1,0).
\]
The same three legal moves can repeat forever. This is a certificate of nontermination, not just a long unfinished experiment.

With four chips, no stable state exists: each of three circles must hold at most one, while firing never changes the total. Therefore every continued legal run is infinite. There are only finitely many placements of four chips, so an earlier arrangement must repeat. For the printed start, AABC reaches (2,1,1), which was already reached after the first A; ABC can then repeat. With three chips the same capacity argument does not decide the outcome; the contrasting starts above are essential.

\textbf{If needed.} Keep a photograph or drawing of the start beside the board. Once the arrangement repeats, ask what the same next move will do. To show the capacity obstruction, put one chip in each circle and ask where the fourth could remain without a legal move.

\textbf{Return question.} Which three-chip starts stabilize? Up to permuting the circles, the only types are \((3,0,0)\), \((2,1,0)\), and \((1,1,1)\). The first reaches \((1,1,1)\), the second cycles, and the third is already stable. Children can give the proof with piles; ordered notation is adult support.

\textbf{Observe.} Can the child identify a repeated whole arrangement, or merely repeat a preferred move? Record that distinction before changing the activity.''',
r'''\textbf{Problem 2: the biggest one-chip avalanche.} Stable starts have zero or one chip at each of A, B and C. Add exactly one chip, then finish all legal sharing. The maximum number of firings is \textbf{four}, attained only by starting at \((1,1,1)\) and adding at B. Its two legal words are BACB and BCAB, each with counts \((1,2,1)\); the finish is \((1,0,1)\), and two chips have escaped.

Adding at A to the all-one start gives ABC and finish \((1,1,0)\). Adding at C gives CBA and finish \((0,1,1)\). Each has three firings. Every other stable start gives at most two. An addition to an empty circle gives none.

\textbf{Why the bound is complete.} There are eight stable starts and three addition sites, hence 24 trials. The independent check explores every legal order for each. A child can also reason locally: from an occupied endpoint, a wave can advance across occupied circles, but a missing one stops it. From B, each occupied neighbor can send one chip back; B fires again only when both neighbors initially held one. That is the all-one start, and after B's second firing both endpoints have just one chip.

\textbf{Light record.} Write the move word while moving, then count letters afterwards. A partner handles the counters or reads the next legal choice; do not require a concurrent tally.

\textbf{If needed.} Offer a start with a single empty neighbor. Ask where a second chip must come from before that neighbor can fire. Keep the starting board unchanged as a reference.

\textbf{Return question.} How does the maximum change on a longer path with a sink at both ends? Do not transfer the four-firing bound to a new board; this is a fresh conjecture to test.''',
r'''\textbf{Problem 3: all legal four-move histories.} The page uses the three known starts from base grades 2--3 Problem 3. The complete history answer is:
\begin{center}\begin{tabular}{c|l}
Start (A,B)&Legal four-letter histories\\\hline
(0,6)&BBAB, BBBA\\
(3,3)&ABAB, ABBA, BAAB, BABA\\
(6,0)&AAAB, AABA
\end{tabular}\end{center}
Every history ends \((1,1)\), with four chips in the initially empty sink.

\textbf{Completeness for the printed task.} For each supplied start, try all four-letter A/B words, rejecting a word at its first illegal firing. The table lists every surviving word that stops at the required finish. A pair can organize the attempts by their first letter, keeping just the word and final board.

\textbf{Readiness-dependent inverse continuation.} If the starts were not supplied, could they be recovered? Four moves lose four chips, so the start has six. Let A fire \(a\) times and B fire \(b\) times; \(a+b=4\). Reversing the changes gives starting piles \(1+2a-b\) and \(1+2b-a\). Counts \((0,4)\) and \((4,0)\) require a negative start, so only \((a,b)=(1,3),(2,2),(3,1)\) remain. These give the three starts in the table. Replay each multiset of letters, discarding a word immediately when its next firing is illegal. This leaves exactly the eight listed words.

A child need not use the formulas: reverse a firing by taking one chip from the other working circle and one from the sink and returning both to the named circle. Four reverse moves consume the four sink chips. A reverse move with an empty recipient is forbidden. Restore a copy after each branch; adult recording can support the tree of attempts.

\textbf{If needed.} Begin with a known forward four-move run, cover its start, then reconstruct it. The discovery task still concerns all possible pasts.

\textbf{Extension.} Change the known finish or run length. Keep the same exact information in every trial. A finish and a run length can determine the initial total without determining the initial arrangement.

\textbf{Checks.} Independent exhaustive firing checks are included in the source package. The algebra and reverse-counter explanation supply the reason for arbitrary order; code verifies this finite answer.''']},
12:{'topic':'Pairing and path return visits',
'overview':r'''\textbf{Facts and limits.} Noncrossing perfect pairings of six fixed circle positions may be restricted to unlike labels. For cyclic words RBRBRB, RRRBBB and RRBRBB the counts are respectively 5, 1 and 2. A cyclic R/B word admits an unlike noncrossing pairing exactly when its two label counts agree: remove an adjacent unlike pair, then continue.

A path with \(n\) up and \(n\) down steps that stays on or above its starting line is a Dyck path. Restricting its height to at most two leaves \(2^{n-1}\) paths for \(n\geq1\): each return-to-ground block is \(U(UD)^kD\), and block sizes are a composition of \(n\). For four pairs, height ceilings 1, 2, 3 and 4 allow 1, 8, 13 and 14 paths.

A legal adjacent swap DU to UD raises one valley by two height units. Repeated raising reaches the mountain \(U^nD^n\). Half the sum of intermediate-height differences from that mountain is the exact minimum number of swaps needed; every swap changes this score by one. Equal counts of steps alone do not permit a swap that goes below ground.

\textbf{Children's destination.} Distinguish existence from counting under a restriction, organize paths around their ground returns, and pair an actual shortest route with a lower bound.

\textbf{Entry map.} Problem 1 (student pp. 1--2): K--1 and up, oral rules, labels and pairing. Problems 2--3 (student p. 3): grades 2--3 and up, reading U/D or arrow cards and keeping height nonnegative. Problem 4 (student p. 4): grades 4--5, local changes and a picture-based optimality argument; no formula is required.

\textbf{New versus base.} Base pages enumerate ordinary pairings and paths and translate trees/codes. These visits add label compatibility, a height ceiling, and a move-distance question.''',
'materials':'For each pair, three R and three B lettered counters, pencil and eraser; short strings are optional because pencil chords make crossings visible. Provide five U and five D step cards, ruler and spare grid paper. Reserve six sets for eleven children (upper third child rotates as checker). A pairing circle should be 3–4 inches across; path grids use equal horizontal and vertical scale. Neither counting task requires exact tile fit.',
'launch':'After free handling, put four labeled dots around a circle and join one unlike pair with string or pencil. Let another child check whether the remaining unlike pair crosses it. On a separate short walk, demonstrate one U and one D card from ground level and show the matching intermediate point. The pairing and step representations are familiar if the base packet was used; otherwise give its ordinary board demonstration before the page.',
'route':'Begin with unlike-color pairing attempts. Offer the ceiling-two path page only once children can act out a walk. Keep local swaps for a later visit if choosing and preserving a legal path still takes adult control.',
'solutions':[
r'''\textbf{Problem 1: unlike partners.} Using fixed positions 1–6, the complete unlike-color pairings are:

RBRBRB: \(12|34|56,\ 12|36|45,\ 14|23|56,\ 16|23|45,\ 16|25|34\).

RRRBBB: \(16|25|34\).

RRBRBB: \(16|23|45,\ 16|25|34\).

Here \(16\) means join dots 1 and 6; bars separate pairs. These are adult compact records, not a new notation required of children. Draw the actual chords when checking their collection.

\textbf{Why a pairing always exists when counts agree.} Unless no dots remain, a balanced cyclic word has both labels and therefore two adjacent unlike dots. Join that pair near the boundary, remove it, and pair the remaining cyclic word. Removing one R and one B preserves equality; the new chord cannot cross any later chord. Reinsert the removed adjacent pairs in reverse order. Conversely, every unlike pair consumes one of each label, so unequal counts make a complete pairing impossible.

\textbf{Completeness of the small lists.} A chord from dot 1 divides the remaining dots into two sides, each containing a balanced number of labels and an even number of dots. Check all possible partners of 1, then pair each side independently. This is an optional hint after genuine attempts.

\textbf{Extension.} Invent a balanced label arrangement with as few pairings as possible and one with many. Treat maximum counts on larger circles as a new question, not a theorem inferred from the six-dot trials.''',
r'''\textbf{Problems 2--3: a low ceiling.} With four U and four D cards, the eight paths staying at height at most two are
\[
\begin{array}{ll}
UDUDUDUD&UUDDUDUD\\
UDUUDDUD&UDUDUUDD\\
UUDDUUDD&UUDUDDUD\\
UDUUDUDD&UUDUDUDD.
\end{array}
\]
Problem 3 has \textbf{sixteen} five-pair paths under the same ceiling: the four possible gaps between pair tokens may each be a block break or not. This continues the same bounded-height investigation rather than adding a fourth investigation.

A ceiling of one allows only UDUDUDUD. A ceiling of three permits every ordinary four-pair path except UUUUDDDD, giving 13; a ceiling of four permits all 14.

\textbf{Why eight.} Between consecutive ground returns, a ceiling-two path must begin U, remain at height one or two by repeated UD, then end D. A block of size \(r\) is therefore \(U(UD)^{r-1}D\). Divide four pairs into an ordered list of positive block sizes: \(1111,211,121,112,22,31,13,4\). Each gives exactly one path. For \(n\) pairs there are \(n-1\) gaps between pair tokens; choose independently whether each gap separates blocks, giving \(2^{n-1}\). This is a deeper adult continuation, not a printed procedure.

\textbf{If needed.} Use a pawn to follow one path before asking for a collection. Put a ruler at the ceiling; stop attempts immediately when they cross it. Children may organize their own list before an adult suggests ground returns.

\textbf{Return question.} What happens at a ceiling of three with more pairs? Concrete enumeration is welcome; the simple ceiling-two formula should not be transferred.''',
r'''\textbf{Problem 4: raise the path.} A swap DU to UD changes only the height at their intermediate vertex, raising it by two. It always preserves legality. The reverse swap is legal only if its new intermediate height is nonnegative.

The four-pair alternating path reaches UUUUDDDD in six moves. One shortest route is
\[
\begin{array}{l}
UDUDUDUD\to UUDDUDUD\to UUDUDDUD\to UUUDDDUD\\
\to UUUDDUDD\to UUUDUDDD\to UUUUDDDD.
\end{array}
\]
Each arrow swaps adjacent unlike letters and leaves a legal path. The other printed starts UUDDUUDD and UUUDUDDD need respectively four moves and one. A shortest route from UUDDUUDD is UUDDUUDD $\to$ UUDUDUDD $\to$ UUUDDUDD $\to$ UUUDUDDD $\to$ UUUUDDDD. UUUDUDDD becomes the target by swapping its middle DU.

\textbf{Why no shorter route.} Above the alternating path and below the mountain, there are six elementary height-increment diamonds. Equivalently, intermediate-height differences sum to twelve, and one swap can change that sum by only two. Therefore at least six swaps are necessary. Draw the two paths on the same grid and let children account for the six raised pieces; avoid demanding a concurrent area tally during the route.

\textbf{General reason.} Any nonmountain Dyck path has a valley: some D occurs before a later U, so an adjacent DU exists. Raise it. Half the total height gap to the mountain falls by one and stays nonnegative. Thus raising terminates precisely at the mountain, with the lower-bound number of moves. This proves both connectivity and optimality to that target.

\textbf{If needed.} Supply a shorter legal path and demonstrate a single swap on separate cards. Keep the target question open. A score alone does not give the distance between two arbitrary paths; that extension requires a new argument.

\textbf{Check limit.} Exhaustive enumeration verifies all four-pair paths, ceilings and legal swaps. The finite test is separate from the general valley and height-gap proof.''']},
13:{'topic':'Route-sharing return visits',
'overview':r'''\textbf{Facts and limits.} A packing of edge-disjoint routes can share internal dots. If internal dots instead have capacity one, the maximum can drop. The central-hub board has two edge-disjoint routes and only one internally vertex-disjoint route; adding the bypass A\(\to\)C permits two of the latter. Edge cuts and vertex cuts answer different questions.

Two routes with specified endpoints need not fit even when the same network carries two routes after reassigning the endpoints. On the P,Q,X,Y board, P\(\to\)Y and Q\(\to\)X both require the single arrow C\(\to\)D, whereas P\(\to\)X and Q\(\to\)Y fit. The single-start max-flow theorem does not promise simultaneous routes for prescribed pairs.

On a finite directed network with one start and one finish and nonnegative integer arrow capacities, an arrow holds that many simultaneous routes. Replacing capacity \(c\) by \(c\) separate lanes gives integral packing; the maximum equals the minimum sum of cut capacities. The printed capacity board supports four routes, and increasing C\(\to\)T from three to four permits five. Length and sequential travel do not represent capacity here.

\textbf{Children's destination.} Identify exactly what is occupied, distinguish endpoint assignment from route choice, and prove an optimum by exhibiting routes and a matching obstruction.

\textbf{Entry map.} Problem 1: K--1 and up with oral rules and occupied-dot counters. Problem 2: grades 2--3 and up, preserve both endpoint obligations simultaneously. Problem 3: grades 4--5, small totals, lane counts and cut certificates. No flow algebra is required.

\textbf{New versus base.} The base uses one start/finish and unit edge capacity, including rerouting and cuts. These visits alter vertex sharing, impose two endpoint pairs, and introduce integer lanes.''',
'materials':'For each pair, pencil/eraser, two route colors or two clear line styles, and 16 markers no wider than 15 mm. Reserve six boards/marker sets for eleven children. For vertex exclusion use a marker on every occupied internal dot; for capacities place one short tick or token in each reserved lane slot. Provide spare paper. Keep arrowheads visible and distinguish crossings without dots from junctions.',
'launch':'Let pairs trace one route. Reserve its whole path before tracing another. Demonstrate an unused arrow entering an already occupied dot: under edge-sharing rules this can be legal; under the new dot rule it is blocked. Put a marker on that dot so a partner enforces the rule. On a spare arrow with two lane boxes, put one reservation in each and show that a third cannot fit.',
'route':'Begin with the hub board and physical dot reservations. The two-pair page needs a child who can retain the pair obligations while rerouting; the reader or adult may restate them. Offer capacity bookkeeping only after simultaneous reservation is secure.',
'solutions':[
r'''\textbf{Problem 1: roads versus junctions.} On the hub board use S-A-H-C-T and S-B-H-D-T. They share H but no arrow, so two edge-disjoint routes fit. Three are impossible because only two arrows leave S.

When no internal dot may be shared, only one fits: every S-to-T route contains H. Closing H stops all routes, giving the matching one-dot obstruction. Closing one arrow cannot do the same on this board, since the exhibited two routes have no common arrow.

Add A\(\to\)C. Now S-A-C-T and S-B-H-D-T share no internal dot and fit together. Again two is maximal because each route needs a distinct first arrow from S.

\textbf{If needed.} Put a counter on H after the first route. Ask whether the second route needs that exact dot. Do not model these as pawns taking successive journeys: successive routes could reuse both roads and dots and would change the question.

\textbf{Extension.} Invent a board where deleting one internal dot stops all travel but at least three arrows must be closed. A three-branch hub supplies an example; the child should demonstrate three disjoint arrow routes and show that every route meets the hub.

\textbf{Limits.} Internally vertex-disjoint routes may share S and T. If a direct S-to-T edge exists, removing internal vertices alone cannot block it; a general vertex-cut formulation must handle that case separately.''',
r'''\textbf{Problem 2: two assigned deliveries.} The direct assignments fit: P-A-X and Q-B-Y use no common arrow. Each crossed assignment exists alone: P-A-C-D-Y and Q-B-C-D-X.

They cannot both be reserved simultaneously. A crossed route leaving A must go to C, because A-X reaches the wrong terminal and terminates there. A crossed route leaving B likewise must go to C. Both then must use C-D. This arrow has capacity one, so the pair cannot fit. This checks all possible crossed routes, rather than merely rejecting the drawn attempts.

If the endpoints can be reassigned, two routes fit again. There is no contradiction with max-flow/min-cut: that theorem joins a single source to a single sink (or handles unassigned aggregate supplies), not specified source-to-terminal pairings.

\textbf{If needed.} Keep a card P\(\to\)Y beside one marker and Q\(\to\)X beside the other. Ask a child to check the finish before reserving the route. Never update which terminal is required during a run.

\textbf{Extension.} What one-arrow addition permits both crossed deliveries? A\(\to\)Y suffices: P-A-Y and Q-B-C-D-X. B\(\to\)X works symmetrically. The new arrow is a changed network, not an unmarked jump allowed on the original.

\textbf{Observe.} Routine adult reading is helpful; if the adult must choose and reroute both paths, delay the simultaneous-pair investigation and return to the first page.''',
r'''\textbf{Problem 3: several lanes on one road.} Capacities are S-A:3, S-B:2, A-C:2, B-C:2, C-T:3, A-T:1. One route S-A-T, two copies of S-A-C-T and one S-B-C-T give four. Copies are separate units using distinct available lanes.

Only four units can enter T, through capacities three and one. This cut proves that five cannot fit and certifies that the displayed four are optimal. A maximum collection could distribute the three C-T units differently; it need not use every outgoing lane of S.

Increasing C-T by one permits five: one S-A-T, two S-A-C-T and two S-B-C-T. All lane capacities are respected. The old T-entry cut now has capacity five; the S-exit cut also has five, proving optimality. Zero changes cannot suffice, so one lane increase is minimal.

\textbf{If needed.} Draw distinct lane slots beside an arrow. A partner crosses out a slot when a whole route reserves it. Keep just a route list and the slots, not several simultaneous cumulative tables.

\textbf{General continuation.} Replace every c-lane arrow by c separate parallel one-lane arrows. The base unit-capacity theorem then applies; minimum cut size becomes the sum of the original capacities. This argument requires nonnegative integer capacities and one start and one finish. It does not repair the prescribed-pair obstruction from Problem 2.

\textbf{Checks.} The source audit independently enumerates simple routes and their multiplicities, plus all start-side cuts. It confirms capacities four and five and the dot/endpoint obstructions.''']},
14:{'topic':'Triangulation return visits',
'overview':r'''\textbf{Facts and limits.} For a triangulated convex n-gon using only original corners and noncrossing diagonals, the graph connecting triangles across shared diagonals is a tree: it is connected, with n-2 triangle nodes and n-3 edges. For n\(\geq\)4 it has at least two leaves. Each leaf is an ear, a triangle with two boundary sides. There may be more than two ears.

The corners admit a three-coloring with all three labels on every triangle, unique up to permuting labels. Remove ears to a single triangle, color it, then insert ears in reverse order: the new ear corner gets the third label opposite its two already colored neighbors. The smallest color class touches every triangle and contains at most \(\lfloor n/3\rfloor\) corners. This is a combinatorial cover, not physical visibility in a room.

Of the 14 triangulations of a regular labeled hexagon, six have half-turn symmetry, two have one-third-turn symmetry and none have one-sixth-turn symmetry. Labels remain fixed when counting different drawings; symmetry tests whether a rotation carries a diagonal set back to itself.

\textbf{Children's destination.} Peel a structural object into smaller pieces; use a coloring to certify a triangle cover; find a complete symmetry collection by orbit constraints rather than guesswork.

\textbf{Entry map.} Problem 1 (student pp. 1--2): K--1 and up, recognize two outside sides and erase a corner with adult demonstration. Problem 2 (student pp. 3--4): grades 2--3 and up, label corners and check every triangle. Problem 3 (student pp. 5--6): grades 4--5, turning/tracing, fractions of a turn and accounting for all possibilities. Formal tree or group language is optional.

\textbf{New versus base.} The base counts triangulations and studies flips and fans. These pages add ears/adjacency, corner coloring/coverage, and geometric symmetry.''',
'materials':'For each pair, pencil/eraser, ruler, three R/B/Y pencils or letter labels and two tracing sheets. Reserve six sets for eleven children and at least twelve spare sheets. Main polygons are about four inches across, with fixed corner labels and equal x/y scaling. No tile fit is required. A turn must keep the outline fixed; tracing lets children check the geometric symmetry while preserving the corner names.',
'launch':'Let children draw a triangle division on spare paper. Point to a triangle with two outline sides and cover it with a small paper flap; then show how erasing its middle corner and the two short outline sides leaves a smaller polygon bounded by the third side. Demonstrate a turn on a square diagonal as a non-task example. At the rotation table, one, two and three corner steps on an empty regular hexagon show one-sixth, one-third and one-half turns if needed. Do not announce the minimum number of ears or the hexagon symmetry counts.',
'route':'Supply the two-page pair for the chosen investigation together: pp. 1--2, 3--4 or 5--6. Start with finding and removing ears. Offer corner coloring after children can reliably identify every triangle. Return for rotation symmetry when a child can compare two diagonal sets with fixed corners; tracing or adult label reading may help without making the choices.',
'solutions':[
r'''\textbf{Problem 1: ears and the triangle tree.} An ear has two polygon boundary sides. In a hexagon triangulated by the alternating central triangle, the three outside triangles are all ears. A fan has exactly two ears. Thus ``at least two'' is sharp, but ``exactly two'' is false.

The printed task asks whether different choices leave different last triangles. Yes: on the fan, peel B,C,D to leave AEF, or F,E,D to leave ABC. On the central drawing, peel B,D,F to leave ACE, or D,F,E to leave ABC. Every original triangle can be the last one: retain its node in the adjacency tree and repeatedly remove a leaf away from it. The fan has eight complete corner-removal words, and the central drawing twelve; these are adult checks, not required child catalogs.

Put one point in every triangle and connect points across every shared inside diagonal. This graph is connected: adjacent cells can be reached by crossing successive diagonals inside the polygon. It has n-2 nodes and n-3 edges, so it is a tree. A finite tree with at least two nodes has at least two leaves; otherwise a longest simple path could be extended at an endpoint. A leaf triangle has only one neighboring triangle and therefore two boundary sides: it is an ear.

\textbf{A direct peeling entry.} Remove an ear by erasing its middle polygon corner. Its third side becomes boundary, leaving a triangulated convex (n-1)-gon. Continue until one triangle remains. Children can record just the corner names erased; the original drawing lets them rebuild in reverse.

\textbf{If needed.} Trace the outline sides of one candidate triangle. A triangle with only one outside side is not an ear, even if it is narrow or near an edge.

\textbf{Extension.} What is the greatest number of ears an n-gon can have? No two ear middle corners can be adjacent when n\(\geq\)5, so at most \(\lfloor n/2\rfloor\); alternating ear constructions attain it. Treat the quadrilateral separately: its two ears have nonadjacent middle corners. A new drawing and bound are a worthwhile return task.''',
r'''\textbf{Problem 2: a corner cover from three labels.} Color a final triangle R,B,Y. Reinsert ears in reverse deletion order. Each added corner is adjacent to the two ends of its ear diagonal, which already have different labels; the third label is forced. This proves existence and uniqueness up to the initial label permutation without assuming an arbitrary traversal always encounters an uncolored corner.

Every triangle has all three labels, so choosing every R corner, or every B corner, or every Y corner touches every triangle. The smallest class has at most \(\lfloor n/3\rfloor\) members, because the three class sizes sum to n.

For the hexagon with central triangle ACE and ears ABC,CDE,EFA, one possible cyclic labeling is R,Y,B,R,Y,B. Each label has two corners, and two corners suffice to touch every triangle. One corner cannot suffice: no corner belongs to all three outside ears. The six minimum pairs are \(AC,AD,AE,BE,CE,CF\); mixed-color selections are valid too. For a fan at A, the unique minimum is A alone, and its color class has just that one corner; it touches every triangle. Coloring supplies a reliable upper bound; an arbitrary chosen class need not be a minimum cover.

\textbf{If needed.} Cover all but one already labeled triangle. Ask which label its remaining corner needs. Let children choose their covering corners and test each triangle before offering the smallest-color-class idea.

\textbf{Extension.} Build a triangulation requiring more than one chosen corner, then seek a cover smaller than the most obvious color class. Keep ``touch a triangle at a vertex'' explicit; covering the drawing with a big physical counter is not the rule.''',
r'''\textbf{Problem 3: turn-symmetric fillings.} Using the printed corner names A–F cyclically, the six half-turn-symmetric diagonal sets are
\[
\begin{array}{ll}
AC,AD,DF&AC,CF,DF\\
AD,BD,AE&BD,BE,AE\\
BE,BF,CE&BF,CE,CF.
\end{array}
\]
(These use compact adult endpoint notation; check drawings rather than teach it as an extra convention.) The two one-third-turn sets are \(AC,CE,AE\) and \(BD,DF,BF\). No one-sixth-turn filling exists.

\textbf{Why the half-turn list is complete.} A triangulation has three diagonals. Under a half-turn, nonfixed diagonals occur in pairs, so at least one diagonal is fixed. Such a diagonal must be a diameter. Two diameters would cross, so there is exactly one. Choose its three possible positions, then triangulate one of its two quadrilaterals in either of two ways. The other half is forced: \(3\cdot2=6\).

\textbf{One-third and one-sixth turns.} A one-third-turn orbit of a diameter consists of three crossing diameters and is forbidden. The other possible diagonal orbits are the two alternating central triangles, both legal. A one-sixth turn would require either all three diameters (crossing) or an orbit of six short diagonals (more than the available three); neither works.

\textbf{If needed.} Give a tracing copy. Turn the diagonals, keep the outline aligned and compare each line, rather than rotating the labels and deciding that every picture is automatically ``the same.''

\textbf{Checks.} The independent source audit enumerates noncrossing three-diagonal sets, all triangle cells, ears, valid colorings, corner covers and rotation-fixed sets. It confirms 14 total, six half-turn, two one-third, zero one-sixth.''']},
15:{'topic':'Site-map return visits',
'overview':r'''\textbf{Facts and limits.} Taxi distance permits horizontal/vertical travel from any point, including inside a cell; fractional edges count as fractional steps. It uses \(|\Delta x|+|\Delta y|\), rather than a straight string. Between (0,0) and (2,2), ties occupy whole opposite quadrants, not only a line. The closed nearest region can fail convexity: (4,0) and (0,4) tie, while their midpoint (2,2) belongs strictly to the second site.

For greatest straight-line distance, each pairwise comparison is still a half-plane, so each farthest-site region is convex, but some sites have no region. For four square corners (\(\pm2,\pm2\)) plus center E, E is never farthest. Corner cells are opposite their corners. In contrast, every distinct site owns itself under nearest-distance rules.

In the bounded square with its four corner sites, the largest distance to the nearest site occurs uniquely at the center, distance \(\sqrt8\). Once that center is also a site, the new optimum is distance 2, attained only at the four edge midpoints. Exact quadrant arguments establish these facts; a sampled map alone cannot prove a continuum maximum.

\textbf{Children's destination.} Identify how the metric changes a map, see an empty cell under a reversed comparison, and optimize the worst nearby distance with a construction and a bound.

\textbf{Entry map.} Problem 1 (page 1): K--1 and up with string and oral ``farthest'' rules. Problem 2 (page 2): grades 2--3 and up, whole grid steps first, fractional lengths and midpoint later. Problems 3--4 (pages 3--4): grades 4--5, concrete candidate locations and a picture-based all-points bound; square roots and coordinate algebra are adult notation.

\textbf{New versus base.} Base pages make straight-line nearest cells, ties, insertions and prescribed regions. These visits change the distance, reverse nearest to farthest, and ask for maximum clearance.''',
'materials':'For each pair, pencil/eraser, ruler, about 12 inches of nonstretch string, and spare grid/tracing paper. Reserve six sets for eleven children. All four printed frames are 4.5 inches square with equal x/y scale. Measurements are to dot centers. A printed frame bounds the clearance task but only displays part of the plane in the whole-region questions. Exact ties use symmetry; stock sizes and string procedure have not been rehearsed.',
'launch':'Let children stretch strings between dots. For the taxi page use its printed non-task route: P=(0.5,0.5), Q=(3,1), two and a half steps across plus half a step up, total three. P starts inside a cell; fractions measure length. Show input, route and total in one unchanged reference. Then compare two string lengths from a trial point to sites and ask which is greatest. Announce the relevant comparison rule at each table/page; do not silently carry grid steps into a straight-line task.',
'route':'Begin with whichever physical comparison is familiar. Problem 1 is the youngest table entry. Grid-step classification requires keeping steps aligned with the grid. Save a proof of the whole-square clearance optimum for a return visit after genuine candidate testing.',
'solutions':[
r'''\textbf{Problem 1: farthest ownership.} With square corners A=(-2,-2), B=(2,-2), C=(2,2), D=(-2,2), the farthest cells are: A owns x\(\geq\)0,y\(\geq\)0; B owns x\(\leq\)0,y\(\geq\)0; C owns x\(\leq\)0,y\(\leq\)0; D owns x\(\geq\)0,y\(\leq\)0. Axis boundaries are shared; all four tie at the center.

Every point is farthest from the corner opposite its quadrant. Moving the corner away horizontally increases the squared horizontal distance, and moving it away vertically increases the squared vertical distance. The two comparisons are independent.

\textbf{Why E has no cell.} Average the four squared corner distances from any point (x,y). The average is \(x^2+y^2+8\), while the squared distance to E=(0,0) is \(x^2+y^2\). At least one corner distance is therefore strictly larger than E's. This is a proof for every point in the plane. An elementary drawing argument can split into quadrants and compare E with the opposite corner, whose horizontal and vertical separations are both greater.

\textbf{If needed.} Ask where a point very near one corner should belong under ``farthest.'' Keep the rule card visibly reversed. String experiments suggest the opposite corner; the quadrant comparison explains the whole region.

\textbf{Return question.} Which added points can have empty farthest regions? Interior points of a convex hull cannot be uniquely farthest; do not claim the precise all-case classification without a new argument.''',
r'''\textbf{Problem 2: taxi ties.} For A=(0,0), B=(2,2), within the small square \([0,2]^2\), the grid distances are x+y and 4-x-y. Thus their tie line there is x+y=2. But outside that square, the same line description fails: for every x\(\geq\)2, y\(\leq\)0, both distances are x-y; the opposite quadrant x\(\leq\)0, y\(\geq\)2 is tied as well.

A precise whole-plane test is
\[
f(x)+f(y)\leq0\quad\hbox{for A's closed region},\qquad
f(t)=|t|-|t-2|.
\]
Here f is -2 below 0, rises linearly from -2 to 2 between 0 and 2, and stays 2 above 2. Equality means tie. On the printed frame \([-2,6]^2\), the 81 crossings comprise 15 strict A, 35 strict B and 31 tied AB. Sixteen entire unit cells are tied. This is adult compact notation; children can compare routes across the nine strips made by x=0,2 and y=0,2.

\textbf{The convexity surprise.} Both (4,0) and (0,4) have distance four to A and B. Their straight joining segment contains B=(2,2), where distance to B is zero and to A is four. Thus a closed nearest region under taxi distance need not contain the whole segment between two of its points.

\textbf{If needed.} Put a small token on each counted grid step, then collect the tokens to compare distances. Any shortest grid route has the same horizontal and vertical step counts; wandering routes do not define the distance.

\textbf{Extension.} Move the second site onto the same horizontal grid line. Its tie set returns to a vertical line. The large tie regions arise from the alignment of two changing coordinate contributions, not an imprecision in measurement.''',
r'''\textbf{Problems 3--4: the clearest place.} With only the four square corners as sites, choose the center. Its nearest-site distance is \(\sqrt{2^2+2^2}=\sqrt8\). Every point lies in a quadrant where its distances horizontally and vertically from that quadrant's corner are at most two. Its distance to that corner is therefore at most \(\sqrt8\); equality in both coordinates forces the center. This proves uniqueness and optimality.

Problem 4 adds a center site; the four side midpoints each have nearest-site distance two, to the center and the adjacent corners. To prove no better point exists, work in the upper-right quarter \(0\leq x,y\leq2\). If x+y\(\leq\)2, distance to the center is at most x+y, hence at most two. If x+y\(\geq\)2, the horizontal and vertical separations from the corner (2,2) sum to \(4-x-y\leq2\), so distance to that corner is at most two. Equality of Euclidean length with the sum of nonnegative horizontal/vertical lengths requires one separation to vanish. These conditions give only (2,0) and (0,2). Reflect into the other quadrants to obtain all four edge midpoints.

\textbf{Units and domain.} In the adult coordinate normalization the square has side four. On the printed 4.5-inch square, the first optimum distance is \(4.5/\sqrt2\approx3.182\) inches and the second is 2.25 inches. Only the candidate point must lie in or on the square; its clearance circle need not fit inside the frame.

\textbf{If needed.} Give children string circles centered on candidate points, or compare the nearest of five lengths. Suggest testing the center and side midpoints only after their own candidates. The proof is a return question; a good candidate search alone can be a satisfying first visit.

\textbf{Extension.} Where should a second new site go after choosing the center? This is a different optimization because the existing reference state has changed. Keep it explicit and allow multiple plausible experiments.

\textbf{Checks.} Exact arguments above settle the continuum claims; a 0.05-unit grid audit confirms the examples and finds the same optimum locations. Sampling is supporting evidence, not the proof.''']},
16:{'topic':'Three-color return visits',
'overview':r'''\textbf{Facts and limits.} Count mesh cells: individual triangles with no mesh line inside them. Ordinary Sperner labeling uses only R/B/Y, fixes those three outer corners, and permits only the two endpoint labels along each side. Allowing G only at interior vertices defeats the guarantee of a specifically RBY cell. Nevertheless, if no RBY cell exists, at least three cells have three different labels: one each of RBG, RYG and BYG. Temporarily replace every G by R, B or Y in three separate copies of the unchanged original and apply ordinary Sperner; the forced rainbow in each copy identifies one of those three original types. On the three-step mesh the minimum three is attainable. All 256 legal four-label fillings include 27 with no RBY: 18 have three any-three cells and nine have five. These finite counts describe this mesh, not every triangulation.

For an edge-to-edge triangulated disk with arbitrary R/B/Y boundary labels, rainbow count has the parity of the number of boundary R-B edges. Interior doors count twice. A square can force even or odd counts; its boundary does not fix the count itself. Problems 3--4 use only R/B/Y, resetting Problem 1's four-label rule.

With outer corners R,B,Y counterclockwise and usual endpoint-label side restrictions, positive R-B-Y cells (up to cyclic reading) minus negative R-Y-B cells is exactly one. Oriented interior edges cancel, leaving the signed outer R-to-B changes. Reversing the outer corner orientation gives minus one. These statements require no holes or dangling subdivisions.

\textbf{Children's destination.} Change an interior-label assumption while preserving the boundary; distinguish RBY from any three different labels; investigate general boundary parity and opposite-sign pairs with one net positive.

\textbf{Entry map.} Problems 1--2 (pages 1--2), one investigation: oral K--1 star entry on page 1; grades 2--3 free mesh and separate counts on page 2; grades 4--5 minimum proof using restored copies. Problem 3 (page 3): grades 2--3 and up, boundary changes and even/odd pairing. Problem 4 (page 4): grades 4--5, a stable counterclockwise convention and two cyclic orders. Formal topology is unnecessary.

\textbf{New versus base.} Base K--1 Problem 4 already inserts centers and classifies local refinements; that is not a new investigation. These visits permit a fourth interior label, change the domain/boundary pattern, and count signs.''',
'materials':'For each pair, four lettered/color pencils are the simplest preparation. For movable labels instead, supply sixteen each R/B/Y and two G; ruler, eraser and spare/tracing paper. Reserve six sets for eleven children. Counters should be at most 12 mm across with vertex spacing at least 18 mm. A three-step mesh has ten vertices, only one interior; all four square boards together have sixteen corners, which sets the movable-label maximum. Labels mark vertices, not faces. Save the original before recoloring and restore it before each replacement. G is allowed only at interior dots in Problems 1–2; remove it for Problems 3–4. Offer pages 1–2 together so page 1’s shared rules remain visible beside the free mesh. Printed dot rings are about 7.1 mm across; pencils or small labels can cover them, with counter centers aligned to the vertices. Material fit and orientation procedure are untested physically.',
'launch':'Let children handle labels. Show how to label a dot and identify one cell’s three corner letters. Contrast a non-task RBG cell with an RBY cell: both have three different letters, only the second is specifically RBY. Use one count at a time. For signs trace counterclockwise around a separate R-Y-B triangle and show the intermediate read order and negative record. Turning that example preserves its sign. Do not reveal the minimum or signed theorem before exploration.',
'route':'Start with the small star under spoken rules, then offer the free mesh to children ready to choose boundary labels and preserve a filling. Seek zero RBY first; count any-three cells in a second pass. Save the recoloring proof for children who retain the unchanged reference. The square is a separate return direction. Introduce signs after rainbow recognition and a stable counterclockwise convention.',
'solutions':[
r'''\textbf{Problems 1--2: a fourth interior label.} A star with R/B/Y outer corners and G at its center has zero RBY cells and three any-three cells, one each RBG, RYG and BYG. On the three-step mesh, read rows from the bottom R-to-B edge upwards: RRBB / RGB / YY / Y. Its nine cells comprise three monochrome, three using two labels, and one each RBG, RYG, BYG. Thus zero RBY and three any-three are attained on the larger mesh.

\textbf{Why three is the minimum.} Preserve the original no-RBY filling. In a copy replace every G by R. Ordinary Sperner forces an RBY cell. It was not originally RBY, so its original labels were G,B,Y. Restore the original and replace every G by B; this forces an original R,G,Y cell. Restore again and replace G by Y; this forces an original R,B,G cell. These three types are different, so at least three any-three cells exist. The general lower bound uses an argument, not numerical search.

\textbf{Conditions and limits.} The triangle is triangulated edge to edge, with usual R/B/Y corners and side restrictions and G only inside. A boundary G would invalidate the recolorings’ Sperner hypotheses. The star is an entry; the free mesh and minimum question supply the substantial investigation. Repeated star choices are not separate investigations.

\textbf{If needed.} Check one cell at a time and distinguish ``exactly RBY'' from ``any three different.'' Mark RBY first, then make a fresh pass for any-three. Adults may read and record while children choose. Three tracing copies or reversible cards support the proof without changing the original between tests.

\textbf{Deeper continuation.} Each of RBG, RYG and BYG occurs oddly if RBY is absent. For RB doors, RBG cells contribute one, RB-only cells two, and interior doors twice. The RB outer side has an odd number of changes. Repeat with RY and BY. The independent three-step enumeration checks 256 fillings: 27 have zero RBY, 18 of those have three any-three cells and nine have five.''',
r'''\textbf{Problem 3: a square boundary.} The student squares are unlabeled. For these adult examples number corners 1=lower left, 2=lower right, 3=upper right, 4=upper left. The left square has diagonal 1--3; the right has 2--4. For a square with diagonal 1--3, use cells 123 and 134; the other diagonal gives cells 124 and 234. With boundary RBRB there are four R-B doors and zero rainbows. With RBY Y there is one door and one rainbow under either diagonal. With RBRY there are two doors: diagonal 1--3 gives zero rainbows, while 2--4 gives two. Spaces in the boundary word only aid reading; the four corner order is fixed.

\textbf{General parity reason.} A rainbow cell has one R-B door. A cell using R and B only has two doors. Other cells have none. Count cell-door incidences: the rainbow count plus twice the two-door-cell count equals the boundary-door count plus twice the interior-door count. Therefore rainbow count and boundary-door count have the same odd/even parity. This works for any triangulated disk, even when the domain is a square or its boundary lacks the usual side restrictions.

A child can pair the two incidences of every inside door, leaving the outside doors unpaired. The remaining parity is easier to see physically than to state symbolically.

\textbf{If needed.} Trace only the boundary once and mark its R-B changes. Keep the chosen diagonal or refinement fixed while filling labels. Supply a pattern with two doors after children have discovered an odd case.

\textbf{Extension.} Find two fillings with the same boundary and different totals. RBRY on the two diagonal choices supplies zero and two; refining a two-label cell gives another construction. Same boundary fixes parity, not exact count.''',
r'''\textbf{Problem 4: positive and negative rainbows.} On the standard three-step triangle, all 192 legal fillings have signed counts \((1,0),(2,1)\) or \((3,2)\). The respective numbers of fillings are 108, 72 and 12. In each, positive minus negative is one. These finite counts are examples; the theorem applies to every edge-to-edge Sperner triangulation with the stated boundary orientation.

\textbf{Why the signed count is one.} Traverse each cell counterclockwise. Give an R-to-B edge contribution +1, a B-to-R edge -1, and every other edge zero. A positive rainbow contributes +1 and a negative one -1. A two-label R/B cell has one edge in each direction and contributes zero; every other nonrainbow also contributes zero.

When adding cell contributions, each interior edge occurs in both directions and cancels. Along the outer R-to-B side only R/B labels occur: +1 changes and -1 changes alternate, beginning with R and ending with B, so their net is +1. The other two sides have no R-B edge. Thus the whole boundary sum is +1, which equals positive count minus negative count.

\textbf{Conventions.} RBY, BYR and YRB are the same positive cyclic order; RYB, YBR and BRY are negative. Turning the page preserves counterclockwise orientation; reflecting it reverses signs. Fixed outer corners must be R,B,Y counterclockwise for the +1 statement. Reversing that order gives -1.

\textbf{If needed.} Put a small curved arrow inside each candidate rainbow and read around it aloud. Let the child classify one triangle at a time; adults may record the plus/minus marks. If the adult must operate every orientation, return to the four-label or square page.

\textbf{Extension.} Apply a missing-color refinement inside a two-label triangle. It creates one positive and one negative rainbow, directly illustrating preservation of the signed difference.''']},
17:{'topic':'Machine-memory return visits',
'overview':r'''\textbf{Facts and limits.} A deterministic machine reads one R/B symbol at a time, has one outgoing arrow for each symbol at every state, and gives a fixed YES/NO when stopped. Its current state is its whole memory. Histories ending in the same state can never be separated by the same continuation.

Detecting RR anywhere requires exactly three states: no pending R, one pending R, and already seen RR. R moves 0\(\to\)1\(\to\)2\(\to\)2; B resets states 0 and 1 to 0 and leaves 2 fixed. Empty, R and RR are pairwise distinguishable, proving three is minimal.

Accepting exactly when both R and B counts are even needs four states, the four parity pairs. R toggles its coordinate and B toggles its coordinate; only even/even accepts. Empty, R, B and RB are pairwise distinguishable, proving four is minimal.

No fixed finite-state machine recognizes equal R/B counts for arbitrary row length. An m-state machine sends two of the m+1 histories empty,R,\(\ldots\),\(R^m\) to the same state. A common run of blue cards then balances one and not the other, a contradiction. A machine can pass many finite tests without settling the all-length question.

\textbf{Children's destination.} Remember an event after it happens, combine independent memories, and expose a limitation through concrete histories and one shared ending.

\textbf{Entry map.} Problem 1 (page 1): K--1/2--3 with a partner operating and an adult reading/drawing arrows. Problem 2 (page 2): grades 2--3/4--5, two odd/even conditions. Problem 3 (page 3): grades 4--5, compare histories and reason about a proposed finite number of circles. No formal-language notation is required.

\textbf{New versus base.} Base tasks track red remainders, last-card/suffix conditions and distinguish histories. These visits detect an occurrence with persistent memory, combine two counts, and show an unbounded-memory obstruction.''',
'materials':'For each pair, twelve R and twelve B lettered cards, one marker, at least eight blank state discs about 4 cm wide, pencil and spare paper. Reserve six sets for eleven children. The upper third child can read inputs or referee, rotating. Used cards must be hidden; no remembered count, card piles, marker orientation or extra counters can act as additional machine memory. Both outgoing arrows must remain legible. Separate 4 cm discs are working materials; printed rectangles record machine drawings. Twelve cards of each label support ordinary tests and red-history collision trials for proposals with at most eight states. Use extra cards or prepared written input rows for larger trials; the all-length theorem has no twelve-card limit.',
'launch':'Let children choose and arrange cards. Use the printed non-task two-circle machine: start X (NO), read R to X, then B to Y, then B to Y, hiding each used card. Its RBB input ends YES. Show input, intermediate states and output together. A partner supplies only the next symbol and the stop signal. Then let every child operate one legal run. The reader may correct an illegal arrow, but cannot communicate past symbols.',
'route':'Act out the page 1 rules instead of reading them in one uninterrupted block; let every child run the marker before designing. Keep page 1’s rules/example beside any selected later page. Begin with the occurrence detector and partner-generated tests; a young child can seek fewer states through trials, leaving the all-rows minimality proof for later. Before the two-even task, check evenness by pairing cards outside the machine run, then hide them. Move to combined parities when separate parity tracking is familiar. Save the equal-count challenge for a return visit where children can propose a complete machine and understand continuation versus restart.',
'solutions':[
r'''\textbf{Problem 1: RR has happened.} Use three states N (no pending R), P (last card R, no RR yet), and F (RR already seen). N is the NO start; P is NO; F is YES.
\begin{center}\begin{tabular}{c|cc|c}
State&R&B&Stop\\\hline
N&P&N&NO\\
P&F&N&NO\\
F&F&F&YES
\end{tabular}\end{center}
The state meanings are preserved by every arrow. In particular, after reaching F, a later B must not erase the already observed event. The printed test rows RRBB, RBR and BRRB should say YES, NO, YES respectively; later B cards do not erase the occurrence.

\textbf{Minimality.} Consider histories empty, R, RR. Stopping distinguishes RR from each of the other two. Appending R distinguishes empty from R: the first becomes R (NO), the second RR (YES). If any pair had shared a state, that common continuation would give the same answer, so three separate states are necessary. This proves the minimum for arbitrary inputs, not just the sample rows.

\textbf{If needed.} Give a child one pending-R disc and one seen-RR disc and ask what a B should do in each situation. Adult drawing is routine help; children still choose the memory meanings and test rows.

\textbf{Return question.} Detect RBR anywhere. Use states empty-suffix, R-suffix, RB-suffix and found. Their R/B destinations are respectively (R-suffix, empty-suffix), (R-suffix, RB-suffix), (found, empty-suffix), (found, found); only found says YES. Empty, R, RB and RBR need different states: stopping separates found; endings BR and R separate the first three. This is an optional return question, not part of the three-state answer.''',
r'''\textbf{Problem 2: two even counts.} Put four circles at the corners of a square, labeled EE, OE, EO, OO; first coordinate is red parity. EE is the YES start, every other circle NO. R switches EE\(\leftrightarrow\)OE and EO\(\leftrightarrow\)OO; B switches EE\(\leftrightarrow\)EO and OE\(\leftrightarrow\)OO. Each card changes only its own count's parity, so the marker always tracks exactly the pair. Printed rows no cards, R, RB, RRBB, BBR, BRBR should say YES, NO, NO, YES, NO, YES respectively.

\textbf{Four are necessary.} Empty, R, B and RB end in the four parity pairs. For any two distinct pairs, append the cards that make the first pair even/even: none, R, B or RB respectively. Those cards toggle both histories in the same way, so the second pair stays different and says NO. Thus every pair of the four histories is distinguishable and must reach a different state.

\textbf{If needed.} Place two ordinary parity boards side by side and operate them together once; then replace the two markers with one marker on the four-pair square. This is a bridge for adults to use after the child has encountered the two conditions, not a printed recipe.

\textbf{Extension.} What if red count is even and the last card is blue? A literal two-by-two memory grid can be compressed to three states because the two odd-red last-card states have identical futures. An exact three-state construction uses E (even red, last card not blue), F (even red, last card blue) and O (odd red). Start E; only F says YES. R sends E/F to O and O to E; B sends E/F to F and O to O. Empty, B and R need distinct states: stopping separates B, and appending B separates empty from R. Combining memories gives an upper bound, not automatically a minimum.''',
r'''\textbf{Problem 3: can finitely many circles remember balance?} Printed rows RRBB, RBRB, BRR require YES, YES, NO. These are only sample tests, not certification. Any proposed m-circle machine fails on some input if its only memory is its current circle. Run the m+1 histories with 0,1,\(\ldots\),m red cards, starting fresh each time, and record each final circle. Two histories must finish at the same circle; call their red counts i and j with i\(<\)j.

Now append the same i blue cards to both histories, \emph{continuing} from those final circles. The first row has i reds and i blues and must say YES; the second has j reds and i blues and must say NO. Starting at the same circle and following the same added cards cannot produce different final circles, so the machine is wrong on at least one row. Adding no cards is allowed when i=0.

\textbf{The mathematical limit.} This argument works for every fixed finite m, regardless of how arrows are drawn. It does not say a machine with a finite bound on the allowed input length is impossible. Nor does it rule out an unbounded counter or stack, which is additional memory outside this model.

\textbf{If needed.} For a proposed three-circle machine, make four red histories physically. Keep a small final-circle record outside the machine, used by the experimenters rather than the operator. Pick a collision and append matching blue cards without restarting. The experimenter's record does not become machine memory.

\textbf{Stop meaningfully.} A concrete failed machine, a collision witness, or the arbitrary-m proof can each finish a visit. Do not make a young child build increasingly large diagrams while an adult controls the investigation.

\textbf{Checks.} Independent enumeration tests both finite constructions on every row of length 0–9, and explicit continuation witnesses prove minimality. The equal-count impossibility rests on the all-m argument above, not the finite audit.''']}
}
