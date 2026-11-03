# Week 108 (draft plan): Hailstone numbers

**Strand:** number (Numbers). **Deep-math field:** dynamical systems on the integers, number theory. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The Collatz map sends an even n to n/2 and an odd n to 3n + 1. The Collatz conjecture (Lothar Collatz, 1937) says every positive start eventually reaches 1, after which it cycles 4, 2, 1. It is open. What is known falls into three kinds. Proved: Terence Tao (arXiv 2019, revised 2022) showed that for any function f(N) that grows to infinity, almost all starts N (in the sense of logarithmic density) have an orbit whose least value is at most f(N); so almost every orbit comes down to "almost bounded" values, but this does not rule out a single orbit that climbs forever or a second cycle. Checked by computer: every start up to 2^71 reaches 1 (Bařina, Journal of Supercomputing, 2025). Checked by hand or small program: 27 takes 111 steps and climbs to 9232 before falling; below 100, 97 is the slowest at 118 steps. Children can discover two provable facts. First, a start only has to drop below itself: if every smaller number reaches 1, so does it, which is why computer checks run fast. Second, running the machine backward from 1 grows a tree: every m has the even parent 2m, and has an odd parent (m − 1)/3 exactly when m leaves remainder 4 on division by 6 (apart from m = 4, whose odd parent is 1 itself). The conjecture says this tree eventually contains every whole number; nobody can prove it does. A side machine with a proved answer is Kaprekar's routine (sort a four-digit number's digits high-to-low and low-to-high, subtract): every four-digit string whose digits are not all equal reaches 6174 in at most 7 steps, a finite fact checked by trying all cases.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Almost all orbits of the Collatz map attain almost bounded values](https://arxiv.org/abs/1909.03562v5) — Terence Tao, arXiv 1909.03562, 2019 (v5 2022). The theorem quoted above, and its logarithmic-density meaning (read November 3, 2026).
- [Improved verification limit for the convergence of the Collatz conjecture](https://www.fit.vut.cz/research/publication/c197809) — David Bařina, Journal of Supercomputing 81 (2025). Computer verification to 2^71 (read November 3, 2026).
- [Mysterious number 6174](https://plus.maths.org/issue38/features/nishiyama/feat.pdf) — Yutaka Nishiyama, Plus Magazine, March 2006. Kaprekar's routine and the seven-step bound (read November 3, 2026).
- Prior use with children: [youcubed "Oh Hail the Elephant!"](https://www.youcubed.org/wp-content/uploads/2017/03/WIM2-Day-4-3-5.pdf) — youcubed Week of Inspirational Math lesson; the file sits under a "3-5" filename but prints no grade. Students generate hailstone sequences, conjecture and are told the problem is unsolved (read November 3, 2026). Also the [UCLA Olga Radko Math Circle session](https://circles.math.ucla.edu/circles/events.shtml?id=4444) "Intro to the Collatz conjecture and iterated functions," September 29, 2024, Intermediate 2B; no handout posted (read November 3, 2026).

## A kid-friendly way in

The hailstone machine with counters: a child holds a pile, pairs the counters up; if every counter has a partner, they keep one of each pair (halving); if one is left over, the pile is tripled (two more copies of the pile) and one counter is added. Piles stay small for starts like 6, 7, 10, 12. In parallel, the class grows a "hailstone tree" backward from 1 on a long roll of paper or sticky notes on a wall: each note gets a "double" child and, when it applies, a "subtract 1 then share into 3" child. Prep: 100 counters per table, sticky notes, a paper roll; about 15 minutes. Launch (2–3 minutes): run 6 together on the board (6, 3, 10, 5, 16, 8, 4, 2, 1), then ask everyone to pick a start and see where it goes.

## By band

- **K–1:** the counter machine with starts up to 12, pairing counters physically; record each pile on a strip of number cards. Question: does your pile always get to 1?
- **2–3:** race starts 1 to 20 (18 and 19 are the slowest, 20 steps each); find the highest point of each; then the "tree from 1" task: which numbers are exactly 7 steps from 1? (3, 20, 21, 128.)
- **4–5:** 27 as a shared class project (111 steps, top 9232), split into chunks; why it is enough to show a start drops below itself; when does a number have two parents in the tree (remainder 4 on division by 6)? Kaprekar 6174 as a contrast: a machine where checking every case finishes the proof.

## Checked facts

Computed in `check_number.py`, `check_week_108()`:

- the orbit of 6 (6, 3, 10, 5, 16, 8, 4, 2, 1); 7 takes 16 steps and peaks at 52; 9 takes 19 steps;
- 27 takes 111 steps with peak 9232; among 1–20 the slowest are 18 and 19 (20 steps each); below 100 the slowest is 97 (118 steps);
- the backward tree's levels 0–8 from 1 (level 5 is 5 and 32; level 7 is 3, 20, 21, 128; level 8 is 6, 40, 42, 256);
- the odd-parent rule (m has an odd parent other than 1 exactly when m leaves remainder 4 on division by 6, m ≠ 4);
- every start from 2 to 99999 drops below itself;
- Kaprekar: all four-digit strings with two different digits reach 6174 within 7 steps, and 7 is needed; the chain 3524, 3087, 8352, 6174.

Cited, not computed: Tao's theorem and the 2^71 verification bound.

## Nearest existing themes

Week 92 (fold-and-stretch predictions) also iterates a map, but on a continuous track with proved behaviour; Weeks 79 and 80 (numbered balls, midnight laboratory) treat infinite processes. Week 74 (doubling elevators) uses halving and doubling as moves. None states an open problem as its centre. New here: an iterated integer map whose behaviour is unknown, the backward tree as the representation, and the honest distinction between "checked to 2^71" and "proved".

## App connection

Numbers region, a new family "hailstone machine": the child steps a number through the machine and predicts the next value; puzzles ask "find a start that takes exactly 10 steps" or "fill in the missing parents on this branch of the tree". A Kaprekar puzzle ("reach 6174 in the fewest steps from this start") could share the family's machine frame.

## Open questions

- Counter piles grow fast after tripling (7 climbs to 52); a pilot should check whether K–1 children cope with tripling physically or need a number line instead.
- Whether "nobody knows" lands as exciting or as unsatisfying for younger children; the guide should pair it with a proved fact (the tree's parent rule).
- Kaprekar may be a separate short station rather than part of the same hour.
