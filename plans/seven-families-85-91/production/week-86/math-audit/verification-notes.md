# Independent mathematical evidence: Week 86

Reviewed the actual current `draft/shared.pdf` (4 pages), `draft/upper.pdf` (6 pages), and `draft/materials.pdf` (3 pages). The outline explicitly replaces the generic three-band output list; there is no K–1 packet to review. No draft files were changed. `results.json` records SHA-256 hashes of the reviewed PDFs. This is mathematical/digital review, not classroom piloting or a physical printing/procedure rehearsal.

## Independent method

`independent_check.py` was written without importing, executing, or reading the author's `verify.py`. It implements the finite game directly with ordered cop locations, robber location, and whose turn it is. Captured states are terminal. Both players' legal move sets include staying. Each cop independently moves or stays during one joint cop turn. Cop placements precede the robber placement; the objective is the minimum over cop placements of the maximum over robber placements.

Finite-horizon sets are grown to a fixed point: C can win within h future cop turns exactly when some joint move leads to an R state winnable within h−1 turns; R states belong when every legal robber reply leads to a C state winnable within h turns. These monotone sets exhaust finite capture strategies. Outside the fixed point, every C action has an R reply outside it, certifying perpetual evasion. First-entry horizon yields optimal capture times. All assertions passed.

`check_pdf_graphs.py` independently extracts circles, roads, and adjacent printed vertex labels from the final PDF drawing/text objects. It checked all **29 printed graph instances**, including both copies of each fold map and every example panel. Each actual edge set and label set matches the hand-transcribed mathematical graph. Working dots are 22 mm except P7's allowed 20 mm; minimum working center spacing is at least 28 mm (P7), all other working graphs at least 32 mm. Demonstration diagrams are 8 mm reference dots. All pages are 612 × 792 PDF points. Every page was rendered and visually inspected, with individual images retained here. No unintended graph intersection or omitted/extra road was found. Cutout tile/counter assembly has not been physically rehearsed.

## Coverage and independently verified outcomes

| Packet / location | Question and verified result |
|---|---|
| Shared p1 / P1; upper p1 / P1 | Choose fastest guaranteed starting point on P5 and P7. P5 uniquely starts at c, taking at most 2 cop moves; P7 uniquely at d, at most 3. All-start worst cases are respectively 4,3,2,3,4 and 6,5,4,3,4,5,6. |
| Shared p2 / P2 | Find forced cop strategies on T1 and T2. Both are trees, both optimally start at c and catch in at most 2 cop moves. Unique-path pursuit wins from every starting vertex, even if not optimal. T1 has 7 vertices/6 edges, T2 has 8/7, exactly as printed. |
| Shared p3 / P3 | Classify R3 and R4. R3 permits capture in one cop move from any cop placement. R4 permits indefinite evasion with a correctly chosen robber start. |
| Shared p4 / P4 | Find perpetual escape on R5/R6. Both permit evasion, and every cop placement admits an escaping robber start. An invariant strategy was exhaustively checked for every separated position and every cop reply. |
| Upper p2 / P2 | Add the fewest roads to E4/E5. C4 needs exactly one diagonal, either ac or bd. C5 needs exactly two chords; exactly five of its ten two-chord choices win: {ac,ad}, {ac,ce}, {ad,bd}, {bd,be}, {be,ce}. Each pair shares an endpoint and makes it universal, giving immediate capture from that endpoint. All five disjoint pairs fail. All 4 subsets of C4 diagonals and all 32 subsets of C5 diagonals were solved. Parallel roads, if allowed by the wording, cannot improve adjacency and therefore cannot alter the minimum. Crossings are explicitly not dots. |
| Upper p3 / P3 | Design two connected six-dot maps with at least six roads, one cop-win and one evasive. A valid cop-win example is ab,bc,ca,cd,de,af (triangle with tails, 6 vertices/6 edges); it is playable in the supplied layout using curved roads where necessary. A valid evasive example is the six-cycle ab,bc,cd,de,ef,fa. Both satisfy all constraints. |
| Upper p4 / P4 and materials pp1–2 | Fold F1/F2 to one dot or to a map with no fold. F1 always dismantles to one dot under exhaustive branching over every available legal fold. F2 has just b→a or b→c initially; either leaves the same square a–c–d–e–a with no legal fold, and F2 is independently robber-win. See explicit neighborhoods below. |
| Upper p5 / P5 | Find a two-cop plan on Q6. The claim is true; optimal free starting placement is opposite dots a,d (or b,e / c,f), yielding capture in 1 joint cop turn. This is the located shortcut reported in `review-math.md`. If both start at a, the optimal guarantee is 3 turns, and the general blocker/sweep plan also wins. |
| Upper p6 / P6 | Find a two-cop plan on Q8 and explain extension to any ring. Two cops suffice; optimum with free placement is 2 joint cop turns. A stationary blocker plus moving sweeper proves the general statement for every finite ring. No upper bound on ring size is required by the argument. |

The three-panel T demonstration is a valid non-task instance: edges wx, xy, xz; first C=w,R=y, then C=x,R=y, then R stays at y. No capture occurs. Turns progress C, R, C. Every counter and label agrees across panels.

## Proofs and hypotheses

**Paths/trees.** Finite, connected, undirected graph; visible positions; alternation, one edge or stay; capture at any shared vertex. In a tree there is a unique path from C to R. C moves one step along it. Unless captured, R is trapped in one component after deleting the new cop vertex, strictly contained in its previous possible component. R cannot cross the cop to regain the removed part. The component shrinks until capture. On a path, start at a central vertex and sweep toward R, who cannot pass. The farthest endpoint gives the matching lower bound by staying, so the optimal worst time is floor(n/2); checked independently for n=1,…,15. The one-vertex case is immediate capture at placement.

**Bare rings.** On C3 each cop start is adjacent to every other vertex. On each Cn, n≥4, R initially chooses outside C's closed neighborhood. Before every cop turn keep distance at least 2. A cop move cannot capture from that position. Afterward, at least one of R's stay/two-neighbor choices remains outside the new cop's closed neighborhood; otherwise a cycle of length ≥4 would have that local three-vertex set contained in the cop's three-vertex set with the old cop at distance at least 2, which is impossible. This was also checked directly at every state for C4,…,C8. Staying is essential to allow responses when C stays or moves away. A long sampled game alone is not the proof; the printed P4 correctly says so.

**Added roads.** One chord of C5 gives, up to rotation, F2. Its nonchord-endpoint triangle vertex folds away to C4, so one chord cannot win. With two chords sharing an endpoint, that endpoint is adjacent to all four other vertices, which is a winning placement. The other five two-chord pairs leave an evasive square after a fold. This provides lower bounds and complete minimum-choice coverage, not merely example solutions. In this convention adding an edge may help either player in general: a four-vertex path is cop-win, adding its missing end-to-end edge gives robber-win C4; a diagonal then makes it cop-win again.

**Folds.** The printed rule means closed-neighborhood inclusion N[v]⊆N[u] in the *current* graph, with v≠u adjacent, and deletion of v with every incident road. All stays/self-memberships are included. Its worked input has N[w]={w,x}⊆N[x]={w,x,y}; deleting w leaves x–y–z. The blue rings and original/output diagrams match those sets.

A legal fold preserves cop-win status, not necessarily capture time. The retraction sends v to u and fixes all other vertices; it maps every legal move or stay to a legal move or stay. A strategy in G projects to G−v when R remains there. Conversely, use a strategy in G−v against the projected robber in G. At projected capture, either actual capture has occurred or C is at u and R at v. In the latter case every next robber position is in N[v]⊆N[u], so the cop captures on its next move. Thus the fold direction is correct and requires the current neighborhoods. No necessity theorem for dismantling is needed for these tasks.

F1 exact initial neighborhoods:

- N[a]={a,b,c,f}; N[b]={a,b,c}; N[c]={a,b,c,d}.
- N[d]={c,d,e}; N[e]={d,e}; N[f]={a,f}.

A checked full sequence, recomputing after each deletion:

1. f→a: {a,f}⊆{a,b,c,f}.
2. e→d: {d,e}⊆{c,d,e}.
3. d→c: {c,d}⊆{a,b,c,d}.
4. a→b: {a,b,c}={a,b,c}.
5. b→c: {b,c}={b,c}; c remains.

F2 exact initial neighborhoods:

- N[a]={a,b,c,e}; N[b]={a,b,c}; N[c]={a,b,c,d}; N[d]={c,d,e}; N[e]={a,d,e}.
- Only b→a and b→c are legal. Deleting b gives N[a]={a,c,e}, N[c]={a,c,d}, N[d]={c,d,e}, N[e]={a,d,e}. No one is contained in any other's set.

**Two cops.** Both cops are placed before R; each cop can independently move/stay on a joint cop turn; R replies once; shared-dot capture is immediate, including placement or moving onto a cop; cops may share a vertex. These printed conventions agree with the solver. For any finite ring, start both cops at vertex 0. Keep C1 there and advance C2 one vertex clockwise each cop turn. R cannot pass C1 through 0 or pass C2 through its occupied vertex. After sweep step s any uncaptured R lies strictly ahead of C2 before the blocker, among s+1,…,n−1. This set decreases to empty by step n−1. This is a general proof, with every robber response separately enumerated as a cross-check for n=3,…,12. Sequential execution of the two cops' chosen moves does not affect the result because there is no interleaved robber move and capture is immediate. The two-cop claim concerns finite simple rings (at least three vertices); even a degenerate one-/two-vertex interpretation is trivially catchable.

## Reproduction

Run both scripts with a Python environment containing PyMuPDF (only the PDF extraction script needs that package):

```
python independent_check.py
python check_pdf_graphs.py
```

Expected summaries: `All independent assertions passed.` and `29 printed graph instances ... verified directly from final PDF drawing objects.` JSON result files hold full finite-state outcomes and every extracted board's labels, edges and dimensions. `Infinity` in the solver JSON means no finite guaranteed capture (Python JSON's nonstandard infinity literal, intentionally retained for inspection).
