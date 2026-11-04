# Week 144 (draft plan): The MU puzzle

**Strand:** logic (Codes and logic). **Deep-math field:** formal systems, invariants, decidability. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Douglas Hofstadter's MIU system (*Gödel, Escher, Bach*, 1979) is a formal system: one starting string, MI, and four rules for making new strings. (1) A string ending in I may get a U on the end (MI → MIU). (2) Everything after the M may be doubled (MIU → MIUIU). (3) Any III may be replaced by U. (4) Any UU may be removed. The strings you can make are the system's "theorems". Hofstadter asks: is MU a theorem? Theorem: no. Rules 1 and 4 do not change the number of I's, rule 3 lowers it by 3, and rule 2 doubles it; starting from 1, a number that is not a multiple of 3 stays not a multiple of 3 under doubling and under taking away 3, so the number of I's is never a multiple of 3, while MU has none. More is true and proved (constructive argument on both pages cited below): a string is a theorem exactly when it is an M followed by I's and U's and its number of I's is not a multiple of 3. So for MIU there is a mechanical test for theoremhood. Two lessons sit around that fact. First, generating theorems never tells you that MU is missing: a search that only builds strings runs forever, and even a search that caps the length can miss real theorems (with strings capped at 12 letters, MIUUUI is never reached, although it is a theorem; with a cap of 16, every short theorem appears). You need an argument from outside the system, here an invariant. Second, "theorem" (made by the rules) and "true" (a fact about the strings) are different notions; Hofstadter uses MIU to prepare for Gödel's 1931 incompleteness theorem, where for arithmetic there are true statements the rules can never produce. The arithmetic core is small enough for kindergarten: start with 1 cube; you may double the pile or take away 3. You can make exactly the piles that are not multiples of 3 (checked up to 30). Proved: the invariant and the characterisation. Checked here: reachability for all strings up to 6 letters, shortest derivations, and the cube version. Children can discover that some targets never appear, find the quantity that explains why, and meet the idea that a reason can settle what no amount of trying can.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [MU puzzle](https://en.wikipedia.org/wiki/MU_puzzle) — Wikipedia, secondary pointer (read November 4, 2026). The four rules, the I-count invariant, the characterisation of theorems with a constructive proof, and Hofstadter's arithmetic recoding of MIU (M = 3, I = 1, U = 0) from GEB chapter XIX.
- [On Decidability and the MU puzzle](https://3fx.ch/blog/2020/12/13/on-decidability-and-the-mu-puzzle/) — Ben Fiedler, blog, December 13, 2020 (read November 4, 2026). A decision procedure for MIU via the value invariant (counting each U as three I's), with both directions of the characterisation.
- Prior use with older students: [Formal Systems](https://www.math.utah.edu/mathcircle/notes/albin1.pdf) — Nathan Albin, University of Utah Math Circle notes, October 26, 2005 (read November 4, 2026). MIU as a toy problem worked in groups, then recast as "Is MU a theorem?", with a link to Gödel and Principia Mathematica. Also [A formal system](https://mathweb.ucsd.edu/~dmeyer/teaching/elementary/20170920formal.pdf) — D. Meyer, UCSD class worksheet, undated (read November 4, 2026): students generate strings from MI, state a true fact about them and decide whether MU can be reached. No K–5 use was found (searched "MU puzzle children elementary classroom", "MIU math circle handout").

## A kid-friendly way in

Letter tiles and picture rule cards. Each pair gets one M tile, about 20 I tiles and 12 U tiles (cut from card, or letter beads), and four rule cards that show a before-and-after picture of each rule. The K–1 kit is a cup of cubes and two arrow cards ("double it", "take away 3"). Prep: print and cut tile sheets and rule cards; about 20 minutes. Launch (3 minutes): start with MI on a large demonstration strip and apply each rule once on a non-task string (MI → MIU, MI → MII, MIIII → MUI, MUUI → MI), then set the challenge: make MU.

## By band

- **K–1:** Cube piles. Start with one cube; double or take away 3. Which piles from 1 to 12 can you make? Put each made pile on a number mat. Children notice 3, 6, 9 and 12 stay empty, and can check a friend's claimed route by redoing it. No reading.
- **2–3:** Letter tiles. Try to make MU; collect every string you make on a class chart; then try targets such as MUI, MIIU and MIUUUI. Which targets never appear, and what do all the made strings have in common? Sorting chart strings by their number of I's is the natural move; leave that discovery to them.
- **4–5:** Explain why MU is impossible (the I count under each rule). Then the converse: show that every target with a good I count can be made, and write a route for MIUUUI. Invent a new rule that would make MU possible, or a new system with its own invariant. Discuss "theorem" and "true", and why searching cannot settle "never".

## Checked facts

All in `check_logic_games_2.py`, function `check_week_144()`:
- No string reachable from MI (strings capped at 16 letters) has an I count divisible by 3; MU is never reached.
- Every string M plus 1 to 5 letters is reached exactly when its I count is not a multiple of 3.
- With a cap of 12 letters MIUUUI is not reached; with 16 it is.
- Fewest steps: MIU 1, MII 1, MIIU 2, MIIII 2, MIUIU 2, MUI 3, MUIU 4 (the same with a cap of 22).
- Cube piles from 1 by doubling or taking away 3: exactly the piles 1 to 30 that are not multiples of 3; 5 takes 4 moves (1, 2, 4, 8, 5) and 7 takes 6 (1, 2, 4, 8, 5, 10, 7).
- Cited, not computed: Hofstadter's framing and the link to Gödel (Wikipedia, Albin).

## Nearest existing themes

Atlas AP-25 (trades whose weighted totals never change) and Week 2 (parity decides which lamp targets are reachable) already teach "find what never changes to prove a target unreachable"; this is the same reasoning move, so the cube entry is close to AP-25. Week 76 (Substitution strips) rewrites every letter at once by a fixed rule; here the player chooses one rule at a time, as in a proof. Week 17 machines read strings rather than produce them. Draft 134 (Conway's soldiers) uses a colouring invariant. New: a formal system with theorems, the idea that a missing string needs an outside argument, and a complete description of the theorems.

## App connection

Codes and logic region, possible family "Rule cards": a strip of letter tiles and four rule buttons that light when they apply; the child taps where to apply them. Puzzles: "Make MUI in 3 moves"; "Make MIUUUI"; "Can you make MU?" with a "never" answer the child must justify by picking the quantity that never changes. A cube-pile level (double, take 3) gives K–1 the same idea. Shrink strips (Week 76) could share the tile art.

## Open questions

- Age fit for 2–3: rule 2 doubles a long string; is copying tiles a burden that crowds out the mathematics? Pairs sharing one strip and a doubling "mirror card" may help.
- How many tiles a pair needs before strings get unwieldy (MIUUUI needs a detour through longer strings).
- Whether the overlap with AP-25 and Week 2 makes this better as a return visit to the invariant theme than a new week; its new content is the formal-system framing.
- Whether to say "theorem" to children at all, or "made by the rules".
