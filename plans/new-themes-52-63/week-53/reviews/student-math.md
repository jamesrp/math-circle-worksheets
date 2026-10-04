# Week 53 independent mathematics review

Fresh math-review stage, October 4, 2026. **Targeted revision is required for Problem 8's final question.** All concrete printed answers, exchange lists, forced/forbidden classifications and inverse-price witnesses check out. No draft/source pages or guide were edited, and no subagents were used.

## Reviewed evidence

Read `AGENTS.md`, repository `README.md`, `REPUBLISHING.md`, `plans/new-themes-52-63/STAGE-ROUTING.md`, this run's complete `PROMPT.md` and `CRITIC-MATH.md`, research notes, adversarial `review.md`, and the editable student text, diagram builder, graph data and source notes. Direct stage routing authorizes this one combined packet and supersedes the harness's separate-band filenames and page quotas.

Reviewed the actual **nine-page `draft/students.pdf`**, SHA-256 `f12a42477b64ba4957740c7c4ef32eaa534081a9fc2c7acb429ee1e6331f5130`. Independently rendered and visually inspected every page at 108 dpi. Every page is US Letter, with Grades 2–5 on pages 1–4 and Grades 4–5 on pages 5–9. Problems are consecutive 1–9. The printed text, sites, prices, price dots, thick purchase membership, records and crossing conventions were audited.

The new `math-qa/independent_review.py` transcribes the graph edge/price lists from the reviewed rendered pages. It **does not import or execute the writer's verifiers, graph data or diagram code**. It tests every edge subset by a fresh connectivity closure, enumerates connected purchases and spanning trees, tests every legal strictly cheaper one-link exchange on every tree, and checks the path-price certificate. A separate routine reconstructs **all 27 printed graph instances** from actual PDF circle/line paths and price rectangles, including unpriced records and the six blank price fields on each inverse map. Every endpoint, site label, price numeral/dot and thick purchase matches the independently transcribed graphs. Full catalogs and checks are in `math-qa/independent-checks.json`; concise execution output is in `math-qa/independent-output.txt`. This stage did not perform a clean rebuild or physical rehearsal; the critic's rebuild evidence is separate.

## Located findings and smallest corrections

### M1 — Required: Problem 8's general question omits its decisive condition

**Location:** Grades 4–5, PDF p. 8, Problem 8: “Can a connected purchase with no loop get stuck above the least cost?”

The question is underdefined. If it asks whether a connected loop-free purchase can exceed the minimum, the answer is **yes**: the printed lower purchase is the tree `{AB,AC,BD,DE,DF}`, cost `1+3+5+1+4=14`; the unique minimum is `{AB,BC,CD,DE,EF}`, cost 8. If “get stuck” means **there is no legal cheaper one-link swap**, the answer is **no**, which is the intended theorem in `MATH-NOTES.md`. The first interpretation is not a child error: its counterexample is directly printed under the question.

**Smallest fix:** replace only the last sentence with an explicit open question such as “Can a connected purchase with no loop cost more than the cheapest one even though no one-link swap makes it cheaper?” Retain the two concrete inputs and the preceding loop question. A one-link swap means replacing one currently bought link by one currently unused printed link, with the **result** connecting every place. This precision fix preserves the arbitrary-map investigation without printing its answer or a search procedure.

Independent enumeration confirms the top tree (8) has no improving swap. The bottom tree (14) has exactly four:

| Return | Buy | New cost |
|---|---|---:|
| AC (3) | BC (2) | 13 |
| AC (3) | CD (2) | 13 |
| BD (5) | CD (2) | 11 |
| DF (4) | EF (2) | 12 |

This is independent evidence for the printed instances, not a proof for all graphs. The exact general theorem and proof are below.

### M2 — Minor domain precision: Problem 7's allowed prices

**Location:** Grades 4–5, PDF p. 7, Problem 7: “Put prices from 1 to 4 on each map.”

The physical implementation and author's intended enumeration use six independently chosen whole-number prices in `{1,2,3,4}`, with repetition permitted. “From 1 to 4” can include fractions; it could also invite an unnecessary interpretation that all four numbers must occur. These readings do not make the inverse objective impossible, but change the verified domain and payment representation.

**Smallest fix:** “Give each link a price of 1, 2, 3 or 4.” No requirement to use every value is needed. Repetition is necessary/available across six links and should not be prohibited. Both uniqueness and multiple-optimum goals are feasible throughout the intended domain; exhaustive evidence is below.

### M3 — Minor convention precision: connectivity after a swap

**Location:** Grades 4–5, PDF p. 5, Problem 5: “returning one bought link and buying one unused link. All four places must stay connected.”

Both pictured inputs are trees. Removing any bought link **before** buying a replacement disconnects the network. Thus literal continuous connectivity during the listed return-then-buy procedure makes every operation impossible. The small worked example correctly buys first and returns second (cost 6 → 9 → 5), and standard simultaneous exchange interpretation makes the task correct. This is a wording ambiguity, not a wrong finite answer.

**Smallest fix if revising the sentence:** state that every **resulting** purchase must connect all four places. Retain “From each thick purchase” so every listed alternative starts from the unchanged pictured input, rather than from the previous row's result. The printed input is a fixed reference; a separate trace/removable record represents results. This handling belongs in the later guide.

### M4 — Source geometry figures need correction

**Location:** `draft/src/DESIGN-NOTES.md`, physical implementation paragraph: “On pages 1–6 and 9, nearest-place spacing is at least 52 mm” and “page-8 working cases have about 39 mm.”

Actual PDF circle centers give **51.001 mm on p. 6** and **37.500 mm on p. 8**. Page 7 is 40.251 mm. Correct those two source figures to 51 mm and 37.5 mm, so guide authors and physical pretests receive the actual geometry. This is a documentation correction; the smaller spacing is not evidence of failed physical fit.

## Independent finite results

Each count is for the complete available graph with every printed place retained, including connected purchases with extra links. Strictly positive prices ensure none of those extra-cycle purchases minimizes cost. All fixed graphs are connected. “Trees” below counts all spanning trees, not only optimal ones.

| Printed map / task | All subsets tested | Connected purchases | Trees | Minimum and complete optimum set |
|---|---:|---:|---:|---|
| p. 1 shared X/Y/Z example | 8 | 4 | 3 | 5: `{XY,XZ}`. Printed `{XY,YZ}` costs 6 and is connected, deliberately nonoptimal. |
| p. 1 / P1 left triangle | 8 | 4 | 3 | 3: `{AB,BC}` only. |
| p. 1 / P1 right triangle | 8 | 4 | 3 | 3: `{AB,BC}` and `{AB,AC}`. |
| p. 2 / P2 | 32 | 14 | 8 | 4: CD plus any two of AB, AC, BC; exactly three. |
| p. 3 / P3 | 32 | 14 | 8 | 7: `{AB,BC,CD}` only. The three cheapest links `{AB,BC,AC}` cost 6 and leave D isolated. |
| p. 4 / P4 | 256 | 134 | 45 | 6: CD and DE plus any two of AB, AC, BC; exactly three. |
| p. 5 swap convention U/V/W | 8 | 4 | 3 | 5: `{UV,UW}` only. Printed intermediate buys all three links for 9; before/after costs 6 and 5. |
| p. 5 / P5 available map (both inputs) | 32 | 14 | 8 | 6: `{AB,BC,CD}` only. Left input costs 10; right costs 6. |
| pp. 6/8 / P6/P8 six-place map | 512 | 164 | 55 | 8: `{AB,BC,CD,DE,EF}` only. |
| p. 7 / P7 underlying K4 | 64 | 38 | 16 | Depends on assigned prices; all 4,096 allowed assignments separately tested. |
| p. 9 / P9 distinct-price map | 64 | 38 | 16 | 6: `{AB,BC,CD}` only. |

For P5 the complete cheaper-swap list from the cost-10 left input is **AC→BC (7), AC→CD (8), AD→CD (9)**. The right input has none. AD→BC is cheaper arithmetically but isolates D and is excluded. Each row uses the same input, and the supplied table has enough rows.

For P6 every cheapest purchase must contain **AB, BC, CD, DE, EF**, and none contains **AC, DF, BD, CE**. Independent unique-cheapest cut certificates are:

| Cut side | Crossing links/prices | Forced link |
|---|---|---|
| `{A}` | AB=1, AC=3 | AB |
| `{A,B}` | BC=2, AC=3, BD=5 | BC |
| `{A,B,C}` | CD=2, BD=5, CE=6 | CD |
| `{E}` | DE=1, EF=2, CE=6 | DE |
| `{F}` | EF=2, DF=4 | EF |

The excluded links are uniquely heaviest on actual cycles: AC on ABC (1,2,3); DF on DEF (1,2,4); BD on BCD (2,2,5); CE on CDE (2,1,6). These certificates cover every competing tree; positivity rules out adding extra links to the unique optimum. The repeated prices do **not** imply several optima.

For P7, independently checking the author's two witnesses in edge order **AB,BC,AC,AD,BD,CD** gives:

- `(1,1,3,2,3,4)`: unique cost-4 optimum `{AB,BC,AD}`.
- `(1,2,2,1,4,4)`: exactly two cost-4 optima `{AB,AD,BC}` and `{AB,AD,AC}`.

The full 4,096-assignment enumeration finds **1,956 unique** and **2,140 multiple** cases. Numbers of cheapest purchases and assignment counts are `1:1956, 2:936, 3:768, 4:144, 5:96, 6:96, 8:72, 9:24, 16:4`. The four all-equal assignments have all 16 spanning trees optimal. These are adult verification data, not proposed student instructions.

For all fixed maps, every nonoptimal tree has an improving legal single swap; the only local minima are the enumerated global optima. The independent test covers **152 spanning trees** across the ten fixed weighted graph types, and separately certifies every unused-edge path inequality. This finite check supports but does not replace the general proof.

## Exact general claims and valid domains

**P8 loop-removal claim.** Assume a finite undirected available graph, fixed vertices, a connected purchase using whole links, and strictly positive price paid once for each bought link. A loop is a nonempty closed trail with no link repeated (a simple cycle also suffices). Removing any link on that loop preserves connectivity, since its endpoints remain connected through the rest of the loop, and strictly reduces cost. Therefore a cheapest connecting purchase has no loop and is a spanning tree. Positive prices matter: on a triangle with all prices zero, the three-link loop is cheapest; a negative-price cycle can make extra links preferable. No printed task uses those prices.

**P8 intended local-to-global theorem.** For a connected acyclic purchase T, “no improving one-link swap” means that no unused available link can replace a bought link while preserving final connectivity and strictly lowering total cost. T is cheapest **if and only if** it has this property.

Adding any unused link f to a tree creates one cycle, consisting of f and the unique tree path between its endpoints. Exactly the links on that path can be removed while restoring a tree. Therefore no improving swap is equivalent to `price(f) ≥ price(e)` for every e on that path. Necessity follows immediately if T is cheapest.

For sufficiency, remove any candidate edge e from T, obtaining two sides. Every available link f crossing those sides costs at least e: for f outside T, the T-path for f contains e; e is the only T-edge crossing the cut. Take any competing spanning tree S that lacks e. Add e to S; the resulting cycle contains some other crossing link f, necessarily outside T. Replace f by e. Cost cannot increase, and the number of edges shared with T strictly increases. Repeat until S becomes T. Thus T costs no more than every competing tree. Every competing connected purchase can first have cycles deleted without increasing cost (strictly decreasing it under these positive prices), so T also minimizes over connected purchases. This proves the intended “cannot get stuck” conclusion on arbitrary finite connected maps, including tied prices.

The **tree condition is essential** if the move permits only one-for-one swaps: buying all three price-1 links of a triangle has no unused link and hence no improving swap, but costs 3 instead of 2. Connectivity, fixed available links/sites and final connectivity of a swap are also essential. For comparison among spanning trees alone, the exchange theorem holds for arbitrary real prices; strict positivity is required for this packet's stronger claims about all cheapest connected purchases being trees. Strictly decreasing swaps terminate because the graph has finitely many trees. A tied-price swap may preserve cost; “cheaper” here is strict, as printed.

**P9 distinct-price uniqueness.** On a finite connected undirected available graph with a different strictly positive price on every edge, there is exactly one cheapest connected purchase. Positivity first makes every optimum a tree. If optimal trees T1 and T2 differ, let e be the cheapest edge in their symmetric difference, say in T1. Adding e to T2 makes a cycle. At least one edge f on it is in T2 but not T1, or T1 would contain the cycle. Distinct prices and e's choice give `price(e)<price(f)`. Exchanging f for e makes T2 cheaper, a contradiction. A disconnected available graph has no all-place connecting purchase. Distinct prices are sufficient, not necessary: P6 has repeated prices and a unique optimum; P1/P7 give multiple-optimum cases.

## Actual diagram and material audit

All 27 printed graph instances preserve their complete topology, including the compact records. The worked X/Y/Z and U/V/W visuals show meaningful input, paid intermediate and connected output before the relevant procedure is used. Dot counts agree with every dot-price numeral. P7 has six price fields on each K4, one for every link. All place circles have equal horizontal/vertical diameters. The P9 square has four equal 98.601-mm sides and two 139.443-mm diagonals; its unmarked crossing is not a place, as the shared circled-place rule specifies.

**No missing-bridge correction is required.** In P6/P8, CD=2 is visibly printed between C and D. BD=5 goes directly from B to D without turning at C, and CE=6 goes directly from C to E without turning at D. Actual perpendicular center separation from each bypass to the nearby unrelated place is 12.393 mm on p. 6 and 9.112 mm on p. 8; the 5.2-mm place radius leaves about 7.19 mm and 3.91 mm clearance respectively. The available six-place graph has **no graph bridges**: deleting any one link leaves it connected. CD is forced by its price, not because it is the only connection. Deleting CD by misreading the diagram would change the unique minimum to 11 (`AB,BC,BD,DE,EF`), so retaining that visible link and both bypasses is mathematically consequential. The actual PDF and independently reconstructed graph retain all three.

Nearest site-center spacing on main working maps is 56.776 mm (p. 1), 67.501 mm (pp. 2–4), 64.600 mm (p. 5), 51.001 mm (p. 6), 40.251 mm (p. 7), 37.500 mm (p. 8), and 98.601 mm (p. 9). Main circles are approximately 10.4 mm across. Compact examples/records have 5.6-mm circles and 22.5–27-mm nearest spacing; those are pen records, not pawn boards.

Fixed available-price sums are 5–26 (including 9 for each convention example); the highest is 26 on the six-place map. Fixed maps have at most nine links. Each inverse K4 costs at most 24 when every link is bought. Thus **30 counters and ten markers suffice** for every allowed whole purchase and buy-first swap intermediate; no printed task has an additional numerical budget. Every stated minimum is feasible within the kit. Prices are paid once, so repeated travel changes no cost. No exact material fit, refund handling, volunteer operation, timing or classroom piloting was tested here, and no remote copy was checked or changed.

**Band disposition:** All concrete Grades 2–5 tasks on pp. 1–4 check completely. All concrete Grades 4–5 tasks on pp. 5–9 check completely; M1 is the required general-question repair, M2/M3 clarify conventions, and M4 corrects source geometry. There is no separate K–1 packet under the authorized routing. The supported younger entry and arbitrary-map proof continuations remain unpiloted, with their prerequisites described separately in source notes. This review does not author the later facilitator guide.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
