# Week 174 (draft plan): Shrinking piles

**Strand:** chance, with analysis (app region "Chance and machines"). **Deep-math field:** exponential decay, logarithms, the maximum of random waiting times. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Start with n coins. Each round, flip every coin still in the pile and remove the heads. Each coin survives a round with chance 1/2 independently, so after r rounds the pile size is binomial with mean n/2^r (proved, by adding each coin's survival chance): the pile halves on average every round whatever its size, which is what "half-life" means. Each coin's lifetime is a geometric waiting time with mean 2 rounds, and the pile is empty when the longest-lived coin goes, so the time to empty is the maximum of n independent waits. Its average is exactly E(n) = Σ_{j ≥ 0} [1 − (1 − 2^(−j))^n]: 2 rounds for one coin, 8/3 for two, 22/7 for three, 368/105 for four, about 4.73 for 10 coins, 6.36 for 32 and 7.98 for 100. It grows like log₂ n: E(n) = log₂ n + 1/2 + γ/ln 2 + (a periodic term of tiny amplitude) + (a term that tends to 0), where 1/2 + γ/ln 2 ≈ 1.333 (Szpankowski and Rego, as presented by Finch, 2019). So doubling the pile adds about one round (64 coins take 0.989 rounds longer than 32), and the periodic wobble means E(n) − log₂ n never settles to a limit, though the wobble is far too small to see. The spread does not grow with the pile (the variance is about 3.3 rounds² for 10 coins and about 3.5 for 10,000, computed here), so relative to its length a big pile empties at a more predictable time. Radioactive atoms behave the same way in continuous time: each nucleus has the same chance of decaying in any interval, regardless of its age, so a sample halves every half-life (5730 years for carbon-14 by later measurement; laboratories still report ages with Libby's 5568 years by convention). Reading a fraction left as a time is radiocarbon dating; after 50,000 years only about 0.24% (roughly 1/423) remains, which is about the method's practical limit. Children can discover the halving staircase, that the last coin lingers, that a pile twice as large lasts only about one more round, and that what is left tells how many rounds have passed.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Resolving Conflicts and Electing Leaders](https://arxiv.org/pdf/1912.06545). Steven Finch, arXiv, December 9, 2019. Section 3 treats repeated tossing of all coins showing tails until only heads remain; the expected number of rounds is log₂ n + 1/2 + γ/ln 2 + a periodic fluctuation of tiny amplitude, attributed to Szpankowski and Rego (read November 4, 2026).
- [On A Roll Again: Analysis of a Dice Removal Game](https://journals.calstate.edu/pump/article/view/6774). F. Camellini, W. Ghantous, A. M. Lanocita, L. E. Mangiapanello, S. J. Miller, G. Tresch and E. Z. Yildirim, The PUMP Journal of Undergraduate Research 9 (2026), 145–157. A related removal game whose length is modelled as the maximum of independent geometric waiting times (read November 4, 2026).
- [Radiocarbon Dating Principles](https://canadianarchaeology.ca/dating). Richard Morlan, Canadian Archaeological Radiocarbon Database. Libby's half-life 5568 ± 30 years used by convention, the later 5730 ± 40, and an effective limit of about 50,000 years (read November 4, 2026).
- Prior use with students: [Decaying Dice](https://tasks.illustrativemathematics.org/content-standards/tasks/2130). Illustrative Mathematics, Algebra 1 (F-LE.A.2): pairs roll 30 dice, remove the 1s, and fit 30(5/6)^x (read November 4, 2026). Also [Half-life with pennies](https://www.scienceteacherprogram.org/chemistry/stevens03.html), Ben Stevens, Summer Research Program for Science Teachers, 2003, high school chemistry: 100 pennies shaken in a container, tails removed each round (read November 4, 2026). No K–5 version was found (searched NRICH and circle pages for coin and dice decay activities).

## A kid-friendly way in

Materials per pair: a cup and 32 two-colour counters (red on one side, yellow on the other; coins work too), a tray, linking cubes, and squared paper. For the class: a chart with columns for starting piles of 1, 2, 4, 8, 16 and 32, where each pair adds a sticky note with the number of rounds its pile lasted. Prep: count counters into cups, about 10 minutes.

Launch (3 minutes): pour a cup of 16 counters onto a tray at the front, take away every red one, and build a cube tower as tall as the pile that is left; repeat until the cup is empty, standing the towers in a row. Ask: "How many pours would 32 counters last?"

## By band

- **K–1:** Start with 10 or 16 counters. After each pour, build a tower the size of what is left and put it next to the last one: a staircase going down. How many pours until the cup is empty? Compare staircases with neighbours: same number of steps?
- **2–3:** Before each pour, predict the pile that will be left. Then the class question: piles of 1, 2, 4, 8, 16 and 32 counters; how many pours does each last? Pool the sticky notes. What happens to the number of pours each time the pile doubles?
- **4–5:** Mystery cup: a partner secretly starts with 64 counters and pours some number of times, then shows only what is left. Guess how many pours happened, and say how sure you are. Extensions: why does one counter last 2 pours on average (list what can happen)? Use dice and remove only the sixes: how many rolls does it take for a pile to halve (about 4)? Why is "time to empty" so much less predictable for a small pile?

## Checked facts

- `check_week_174()`: E(1) = 2, E(2) = 8/3, E(3) = 22/7, E(4) = 368/105 by the recursion over how many coins survive, matching the sum formula; E(10) ≈ 4.73, E(32) ≈ 6.36, E(100) ≈ 7.98.
- `check_week_174()`: 1/2 + γ/ln 2 ≈ 1.3327461772; the gap E(n) − (log₂ n + 1.333) is about 0.07 at n = 10, about 0.02 at n = 32 and under 0.01 at n = 100 and 128; E(64) − E(32) ≈ 0.989 and E(128) − E(64) ≈ 0.994.
- `check_week_174()`: expected piles 32, 16, 8, 4, 2, 1; a pile of 20 is empty after 5 rounds with chance (31/32)^20 ≈ 0.53; removing sixes from dice gives a half-life of ln 2/ln(6/5) ≈ 3.80 rolls; with half-life 5730 years, a quarter remains after 11,460 years and about 0.24% (1/423) after 50,000; a seeded 5,000-run simulation of 32 coins agrees with E(32).
- `check_week_174()`: variance of the time to empty ≈ 3.31, 3.44, 3.49 and 3.51 for 10, 32, 100 and 10,000 coins; the app comparison: 64 beads at chance 1/2 average about 7.34 ticks, 32 beads at chance 1/3 about 10.51.

## Nearest existing themes

Weeks 79 and 80 (Numbered-ball detectives, Midnight laboratory) are about infinite processes and halving distances deterministically; here the halving is random and the process always ends. Atlas AP-27 hides two halving amounts behind a total and asks what readings can reveal, a close cousin of the 4–5 mystery cup. Draft 131 (collecting every sticker) waits for the *last* of several events in a different way (new faces), and draft 141 meets harmonic numbers; atlas GA-34 marks doubling times of fast growth. Week 74 (Doubling elevators) shows exponential reach. New here: a random pile that halves on average, logarithmic time to empty as the maximum of waiting times, and dating from what remains.

## App connection

Region "Chance and machines", possible family "Fading lights": a jar of lit beads, each going dark with chance 1/2 each tick. Puzzle 1: "Bet on how many ticks until the jar is dark; the machine runs 100 jars." Puzzle 2: "This jar started with 80 and now shows 5 lit beads. How many ticks ago did it start?" Puzzle 3: "Which jar goes dark sooner on average, one jar of 64 beads or a jar of 32 beads whose beads go dark with chance 1/3 each tick?" (the 64-bead jar: about 7.3 ticks against 10.5).

## Open questions

- Pouring and sorting 32 counters each round takes time; is one round per minute realistic for K–1, and is 16 a better start?
- Whether children will accept "remove the reds" as fair when a counter lands on its edge; a rule for re-pouring is needed.
- The radiocarbon story: how much to say, and whether "the method's practical limit" needs a gentler explanation.
- Whether the bounded spread (about 3.5 rounds²) should reach children at all, or stay an adult note behind the 4–5 question about small piles.
