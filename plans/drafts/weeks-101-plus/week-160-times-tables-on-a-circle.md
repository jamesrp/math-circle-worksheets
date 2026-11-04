# Week 160 (draft plan): Times tables on a circle

**Strand:** number, with shape (Numbers). **Deep-math field:** modular multiplication, envelopes of lines, epicycloids. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Put the numbers 0 to n − 1 round a circle and join each number i to k × i, keeping only the remainder after dividing by n. Two different theorems live in the picture. The curve: as n grows, the chord from the point at angle t to the point at angle k t always touches the curve P(t) = (k e^{it} + e^{ikt}) / (k + 1), which is an epicycloid with k − 1 cusps, the path of a point on a small wheel rolling round a fixed one. So times 2 outlines a cardioid (one cusp), times 3 a nephroid (two cusps), times 4 three cusps, and the lines appear to draw a curve none of them lies on (an envelope). Beardon and Beardon (1989) treat the general rule i to k i + c and show the envelopes are epicycloids for positive k and hypocycloids for negative k. Times n − 1 joins i to its mirror image, so all chords are parallel, and times n + 1 draws nothing, because only the remainder matters. The numbers: the rule is a function on the n remainders, so following strings from 1 (1, k, k², …) must eventually loop. When k shares no factor with n the rule is a reshuffle and 1 returns after the multiplicative order of k mod n; otherwise the path falls into a loop that misses 1 (times 2 on 10: 1, 2, 4, 8, 6, 2). On 24 nails every multiplier sharing no factor with 24 returns to 1 after just two steps, and 24 is the largest n with that property (true exactly for the divisors of 24; checked here to 2000, a classical fact not taken from a source read). On a finite circle the curve is only suggested: with 24 nails, times 2 gives 22 distinct strings (8 to 16 is drawn twice) and times 3 gives 19. Everything stated is proved; nothing is open at this level. The Mathologer video "Times Tables, Mandelbrot and the Heart of Mathematics" connects the cardioid to the main bulb of the Mandelbrot set, a link to mention, not to teach.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Circles, chords and epicycloids](https://core-prod.cambridgecore.org/core/journals/mathematical-gazette/article/circles-chords-and-epicycloids/521CED898E8D77088183D4F8B2B888BA) — A. F. Beardon and L. A. Beardon, The Mathematical Gazette, 1989. Abstract: N points, chords by a rule such as n to 5n + 8 mod N; envelopes are epicycloids for positive k (simplest a cardioid), hypocycloids for negative k. Only the abstract was read; the cusp count k − 1 is checked numerically here, not quoted from the paper (read November 4, 2026).
- [Mathologer modulo circle](https://redblobgames.com/x/1847-mathologer-modulo-circle) — Red Blob Games, November 2018. An interactive version with N points and multiplier M, inspired by the Mathologer video, showing the cardioid (read November 4, 2026).
- [Coding Challenge 133: Times Tables Cardioid Visualization](https://thecodingtrain.com/challenges/133-time-tables-cardioid-visualization) — The Coding Train. Lists the Mathologer video by title in its references and starts from the 2-times table and the cardioid (read November 4, 2026).
- Prior use with children: [Round and round the circle](https://nrich.maths.org/86) — NRICH, ages 7–11: join clock numbers 0–11 by counting on in steps of 2, 5, 6, 7 and relate step to the number of sides (read November 4, 2026). This is the additive picture (Week 4), not the multiplying one. Also [Mary Boole, String Art, and Modular Arithmetic](https://uen.pressbooks.pub/sentry2023/chapter/part-1-mary-boole-string-art-and-modular-arithmetic/) — Brown, Buell and Marr, a classroom string-art module with yarn on dot templates, again joining i to i + k (read November 4, 2026). No source found where children draw the multiplying rule i to k i; I searched NRICH, string-art and "multiplication circles" pages.

## A kid-friendly way in

String art. Paper plates with 10 notches (K–1) and printed circles of 24 and 60 dots (2–5). With yarn on the plate, each child hooks string from 1 to 2, 2 to 4, 3 to 6, …, 5 to 10, which is back at 0, then 6 to 12, which is 2: the plate's numbers run out and the rule "keep going round" appears naturally. On paper, children draw times 2 on 60 dots with a ruler (59 chords is long; tables can split the dots) and watch the heart shape grow. Prep: 10-notch plates with numbers written on, yarn and tape; printed 24- and 60-dot circles (one template, printed many times); rulers; about 25 minutes, mostly plates. Launch (2–3 minutes): on a big 10-dot circle on the board, draw 1 to 2, 2 to 4, 3 to 6, 4 to 8 together, then ask where 6 should go and agree "count round past 10 and keep going".

## By band

- **K–1:** yarn plates with 10 notches, times 2 (an adult reads out the pairs); notice that every string ends on an even notch and that the even notches 2, 4, 6, 8 each get two strings.
- **2–3:** times 2 and times 3 on 24 dots, then on 60 dots shared within the table; what shape appears? Which multipliers draw the same picture on 24 dots (times 25 is times 1, so nothing; times 23 gives parallel lines)? Follow one string after another from 1 and find when you get back.
- **4–5:** compare times 2, 3, 4, 5 on 60 dots and count the cusps; conjecture "k − 1 points" and test times 6. On 24 dots follow the path from 1 for every multiplier: why do 5, 7, 11, 13 all come back in two steps, while 2 never comes back? Explain with remainders why times 23 makes parallel chords.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_160()`:

- on 10 dots times 2 sends 0 to 9 to 0, 2, 4, 6, 8, 0, 2, 4, 6, 8 (9 distinct chords); paths from 1: times 3 gives 1, 3, 9, 7, 1; times 9 gives 1, 9, 1; times 2 gives 1, 2, 4, 8, 6 then 2; times 3 and times 7 return in exactly 4 steps; times 2 on 60 dots draws 59 strings;
- on 24 dots times 2 gives 22 distinct chords (8 to 16 twice) and times 3 gives 19 (fixed dots 0 and 12; 3 to 9, 6 to 18, 15 to 21 twice); times 25 draws nothing; times 23 gives chords all parallel;
- the multipliers 1, 5, 7, 11, 13, 17, 19, 23 all square to 1 mod 24, and the n up to 2000 where every such multiplier squares to 1 are 2, 3, 4, 6, 8, 12, 24;
- for k = 2 to 5, P(t) = (k e^{it} + e^{ikt})/(k + 1) lies on every chord from t to k t and moves along it (tangency), and P stops (a cusp) at exactly k − 1 angles per turn.

## Nearest existing themes

Week 4 (stars and wheels) hops by adding k round n dots; NRICH's clock task and Boole string art are that additive picture. Here each dot has its own string determined by multiplying, so the picture is not a star and some dots get two strings while others get none. The order of k mod n links to Week 157 draft (remainders that repeat), where multiplying by 10 mod p is the same move. Week 47's "envelopes" are a different idea (bounds on values). No week draws a curve as an envelope of lines; that and the epicycloid are new.

## App connection

Shapes and spaces or Numbers region, a "times-table loom" family: choose n and k, the board strings the chords one by one; puzzles ask the child to predict before drawing, "on 24 nails, which multiplier makes all strings parallel?", "which multiplier makes 2 cusps?", or "start at 1 and follow strings: which multiplier brings you back in 4 steps on 10 nails?" (3 or 7).

## Open questions

- Whether 60 dots can be drawn accurately with a ruler by grades 2–3 in the time, or whether a printed 60-dot sheet with every chord drawn faintly is needed for the shape to show. Rehearsal needed.
- Yarn plates take time to notch; a parent volunteer may prefer pegboards or pencil drawing only.
- The Beardon paper was read only as an abstract; the guide should check the full paper or another source for the cusp statement before quoting it.
