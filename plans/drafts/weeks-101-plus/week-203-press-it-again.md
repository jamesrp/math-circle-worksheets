# Week 203 (draft plan): Press it again

**Strand:** analysis, with number (app region "Chance and machines"). **Deep-math field:** iteration, fixed points, contraction mappings, speed of convergence. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Feed a machine's output back in as its next input and watch where the numbers go. Banach's fixed-point theorem (his thesis, 1920, published 1922): if a machine f on a complete space shrinks every distance by at least a fixed factor c < 1, then f has exactly one fixed point (an input with f(p) = p), every start converges to it, and after n presses the error is at most cⁿ/(1 − c) times the first step. On a calculator: pressing cos (radians) from any start settles at the Dottie number p ≈ 0.739085, the only real solution of cos x = x (named by Kaplan in Mathematics Magazine, 2007; it is transcendental). The theorem applies because any start lands in [cos 1, 1] ⊂ [0, 1] after two presses, and on [0, 1] cos shrinks distances by at least sin 1 ≈ 0.84. Near p each press multiplies the error by about sin p ≈ 0.674, so a new correct digit costs about six presses (35 presses from 0 for six decimals). The square-root key settles at 1 from any positive start; on [1, ∞) it halves distances at least, and near 1 it halves them almost exactly (√(1 + s) ≈ 1 + s/2), so about 24 presses from 100. Contraction is a sufficient reason, not a necessary one: from 0.01 the √ key also reaches 1 although it stretches distances near 0, and sin creeps to its fixed point 0 with no fixed shrinking factor (after n presses from 1 it is about √(3/n)). Machines can also fail to settle: 1/x swaps 2 and 1/2 forever, and x² sends 1.1 off to infinity and 0.9 down to 0, so its fixed point 1 repels. The slope at the fixed point decides, in the smooth case: below 1 in size it attracts, above 1 it repels. Averaging a guess for √2 (x → (x + 2/x)/2, Heron's Metrica I 8; a mathematically equivalent Old Babylonian procedure is attested, though there is no evidence the Babylonians iterated it) is a contraction whose slope at √2 is 0, so the error is squared each time (error_new = error²/(2x)) and correct decimals roughly double: 3/2, 17/12, 577/408, 665857/470832, with 0, 2, 5, 11 correct decimals. A physical version: on a ribbon, alternately move a clip halfway to the left end and halfway to the right end; the clip settles on the one-third and two-thirds marks from any start, because one round is x → x/4 + 45 on a 90 cm ribbon, a contraction by 1/4 (James Tanton's folding, used in a teachers' circle). Children can discover that very different starts end at the same place, that some machines settle, some flip and some run away, and, in grades 4–5, why a machine that halves gaps must settle, and why averaging is so much faster than pressing cos.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The contraction mapping theorem](https://kconrad.math.uconn.edu/blurbs/analysis/contraction.pdf). Keith Conrad, expository notes, University of Connecticut. Banach's theorem (thesis 1920, published 1922), a priori and a posteriori error bounds, cos on [0, 1] with constant sin 1 ≈ 0.8415 and fixed point ≈ 0.7390, Newton's method for √3 and "doubling the number of correct digits" (read November 4, 2026).
- [Dottie Number](https://mathworld.wolfram.com/DottieNumber.html). MathWorld (Wolfram Research). Value 0.739085…, named by Kaplan (Mathematics Magazine 80, 2007) after a professor who kept pressing the cosine key; universal attracting fixed point; transcendental by Lindemann–Weierstrass (read November 4, 2026).
- [Square Root Approximations in Old Babylonian Mathematics: YBC 7289 in Context](https://www.ux1.eiu.edu/~cidelman/Classes/4900/Class%20Notes/Babylonian%20Approximations.pdf). David Fowler and Eleanor Robson, Historia Mathematica 25 (1998). YBC 7289's √2 = 1;24 51 10; the Old Babylonian procedure equivalent to Heron's averaging (Metrica I 8, √720); no direct evidence the Babylonians iterated it (read November 4, 2026).
- Prior use with children: [Iterated Functions](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2009_2010/lectures/0910lecturespdf/iterated_tom_davis.pdf). Tom Davis, Berkeley Math Circle archive, November 5, 2009. Pressing cosine to reach about .739085133215, fixed points as crossings with y = x, the slope-below-1 rule, and averaging for square roots (read November 4, 2026).
- Prior use with adults: [Fun with Folding and Pouring](https://archive.mathteacherscircle.org/assets/session-materials/DunbarSchmidtFoldingPouring.pdf). Steve Dunbar and Anne Schmidt, Math Teachers' Circle session, October 10, 2013, after Tanton, Mathematics Galore! ch. 9. Alternating left and right folds whose creases converge to two positions from any start (read November 4, 2026). No K–5 handout was found for calculator iteration.

## A kid-friendly way in

Materials per table: two or three cheap calculators with √ and (for 4–5) cos keys set to radians; a 90 cm ribbon or adding-machine tape with a clothespin and 30/60 cm marks hidden on the back; a "machine card" deck (√, cos, 1 + 1/x, 1/x, x², half-and-add-1); recording strips. Prep: about 20 minutes (set calculators to radians, cut tape, write cards). Launch (3 minutes): put a clip anywhere on the ribbon; the rule is "fold the left end up to the clip and move the clip to the fold, then fold the right end to the clip and move the clip to the fold". Three volunteers start at different places; the group watches the clips crowd together, then flips the ribbon to see the marks.

Suggested hour: 0–5 ribbon launch; 5–20 ribbon (K–1) or √ key from many starts (2–3, 4–5); 20–40 sort the machine cards into "settles", "flips" and "runs away"; 40–55 band questions; 55–60 share the fastest settling machine.

## By band

- **K–1:** The ribbon game in pairs, each child choosing a secret start; do the clips end up in the same places? Then try a ribbon twice as long: do the clips settle at the same fraction of the way along?
- **2–3:** Press √ again and again starting from 5, 100, a million and 0.2. Where does it go, and how many presses until the screen stops changing? Then "half and add 1": what number does it settle on, and can you find it before pressing?
- **4–5:** Sort the machine cards and explain which settle; press cos (radians) from different starts and count presses for each new correct digit; then race cos against averaging a guess for √2 and compare how many digits each press gives. Why must a machine that halves every gap settle, and settle in one place only?

## Checked facts

- `check_week_203()`: cos p = p for p = 0.7390851332…; 35 presses from 0 and 34 from 1 reach six decimals; the error factor sin p ≈ 0.6736 gives about six presses per digit; any start lies in [cos 1, 1] after two presses; sin 1 ≈ 0.8415.
- `check_week_203()`: the √ key reaches 1 to six decimals in 22 presses from 5, 24 from 100, 25 from a million and 24 from 0.01; near 1 the distance to 1 halves each press; on [1, ∞) √ halves distances at least.
- `check_week_203()`: 1 + 1/x reaches the golden ratio in 15 presses; 1/x swaps 2 and 1/2; x² from 1.1 exceeds 400 in six presses and from 0.9 falls below 0.002; sin from 1 is within 3% of √(3/n) at n = 100 and 1000.
- `check_week_203()`: averaging from 1 gives 3/2, 17/12, 577/408, 665857/470832 with errors about 0.086, 0.0025, 2.1 × 10⁻⁶, 1.6 × 10⁻¹², and each new error equals error²/(2x).
- `check_week_203()`: the ribbon rule settles on 30 and 60 cm from five starts; one round is x → x/4 + 45, with gaps 60, 15, 3.75, 0.9375, 0.234375 from 0.
- Banach's theorem and the transcendence of the Dottie number are cited, not computed.

## Nearest existing themes

This topic substantially overlaps the library, so it needs a distinct angle. Week 93 (Squaring a rectangle) is exactly the averaging method for square roots, done geometrically with the same fractions 3/2, 17/12, 577/408; atlas AP-06 and GA-28 cover Newton's method and its cycles; atlas GA-36 already feeds a machine's output back and contrasts a contraction ((x + 1)/3) with 1 − x flipping around 1/2; AD-17 shrinks a gap by a fixed factor; draft 129 finds a map's fixed point by repeated lookup; draft 175 (chaos game) uses halving contractions with random choices; draft 168's "pinch game" is the same alternating-halves ribbon rule used here for K–1; Week 80 moves halfway to END. Week 20 (Averaging) is about a discrete harmonic function, a different averaging idea; Week 49 (Ducci) reaches zero by a different mechanism. What is new: the calculator as a cheap experimental machine, a sorting task over many machines (settle, flip, run away), the slope rule as the classifier, the Dottie number, and speed of convergence as a measured quantity (six presses per digit, one press doubling the digits). Proposal: present Heron's method only as a callback to Week 93, and keep the ribbon game shared with draft 168 rather than claiming it for both; if only one of 168 and 203 goes forward, the ribbon belongs with whichever is chosen.

## App connection

Region "Chance and machines", possible family "Press again": the child picks a machine card and a start, presses a big button and watches a dot hop on a number line, with a trail of earlier dots; a side panel draws the staircase or spiral against the diagonal line. Puzzle 1: "Find a start for x² that neither runs away nor falls to 0" (only ±1). Puzzle 2: "Build a machine from 'halve' and 'add a number' that settles at 7." The existing "Missing square in Tile gardens" family (Week 93) already carries averaging; this family would carry the other machines.

## Open questions

- Calculators: cos needs radian mode, and cheap four-function calculators have only √. Is √ plus hand-made machines enough for 2–3?
- Is sorting six machine cards too abstract for 2–3 without a picture? The staircase picture may be adult-only.
- The ribbon game is shared with draft 168; decide which plan owns it.
- How much of Week 93 do returning children remember? If a lot, the averaging race can be short.
