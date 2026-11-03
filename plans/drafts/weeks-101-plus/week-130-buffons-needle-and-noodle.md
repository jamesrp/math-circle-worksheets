# Week 130 (draft plan): Dropping sticks and noodles on lines

**Strand:** chance, with shape (app region "Chance and machines"). **Deep-math field:** geometric probability, expectation, integral geometry. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Buffon's needle (posed by Buffon, published 1777): a needle of length L dropped at random on a floor of parallel lines spaced d apart, with L ≤ d, crosses a line with probability 2L/(πd). For a toothpick as long as the spacing that is 2/π ≈ 0.637. Barbier (1860) changed the question from "does it cross?" to "how many crossings on average?", and then the answer holds with no restriction: the expected number of crossings of any rigid wire of length L, straight, bent, zigzag or closed, is 2L/(πd), whatever its shape. The proof is short and does not need calculus. Expected crossings add over the pieces of a wire (linearity of expectation, which holds even though the pieces' crossings are not independent), and every short piece behaves like every other piece of the same length, so the average is c·L for one constant c. A ring of diameter d always meets exactly one line, and meets it twice, so 2 = c·πd and c = 2/(πd). For L ≤ d a straight needle crosses at most once, so its expected count equals its crossing probability, which recovers Buffon's formula. Limits: the drop must be uniform in position and angle (real throws on a small sheet are close to this, not exactly), and the formula is an average, so a class of 500 drops estimates π only to about ±0.1. Barbier's theorem from Week 59 (every shape of constant width w has perimeter πw) follows from the same argument, since such a shape also always crosses twice. Children can discover that bending a wire does not change its average crossings, that a ring of the right size always crosses exactly twice, and that the same wire straightened still averages 2.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Buffon's noodle (talk slides)](https://www.math.miami.edu/~armstrong/Talks/buffons_noodle.pdf). Drew Armstrong, University of Miami, undated talk. Buffon's 1777 question, Barbier's 1860 shift to the average number of crossings, the noodle ("rigid or floppy, as long as it lies in the plane"), and estimating a perimeter from crossings (read November 3, 2026).
- [Math Surprises: An Example](https://www.cut-the-knot.org/ctk/August2001.shtml). Alexander Bogomolny, Cut-the-Knot, August 2001. The formula 2L/(πD), additivity over pieces of a wire, the circle-of-diameter-D argument giving the constant, and the link to Barbier's constant-width theorem (read November 3, 2026).
- Prior use with children: [Celebrating Pi Day? Try this activity by a UF mathematician](https://news.ufl.edu/2023/03/pi-day-toothpick-activity-/). University of Florida News, March 2023. A family activity with posterboard, lines one toothpick apart and about 1,000 drops shared among friends or kids (read November 3, 2026). No K–5 math-circle handout on the noodle version was found (searched NRICH, math circle and toothpick activity pages).

## A kid-friendly way in

Materials per table: a poster sheet ruled with lines 6.5 cm apart (one flat toothpick length; measure the toothpicks first), 50 toothpicks, three pipe cleaners, a cup, and a tally strip. One pipe cleaner is bent into a ring and the sheet's spacing is set to match its width (a 20.4 cm wire makes a 6.5 cm ring); a second identical wire stays straight; a third is cut in half and bent into a V. Prep: rule lines with a meter stick, cut pipe cleaners to length, about 20 minutes. Launch (3 minutes): drop three toothpicks from a fixed height above the sheet, sort them into "touches a line" and "touches no line", and put a tally mark for each; then drop the ring a few times and ask everyone to watch how many times it touches.

Suggested hour: 0–5 launch; 5–30 toothpick drops pooled per table, then ring and straight wire; 30–45 bent wires and short toothpicks; 45–60 pool the class tallies and compare tables.

## By band

- **K–1:** Drop toothpicks in handfuls of ten and sort into two cups (touching, not touching); line the cups' contents up to see which is longer. Then try half toothpicks. Drop the ring many times: does it ever touch a line other than twice?
- **2–3:** Count crossings per drop for the straight wire as long as the ring. It crosses 0 to 4 times; what does it do on average over 30 drops? Then compare a straight wire, a V and a zigzag of the same length. Which shape crosses most?
- **4–5:** Explain why bending cannot matter (cut the wire into short pieces; each piece's crossings add up), use the ring to find the constant, and use the class's toothpick tally to estimate π from drops ÷ crossings × 2. How close should we expect to get with 500 drops?

## Checked facts

- `check_week_130()`: numerical integration confirms the crossing probability 2L/(πd) for L = d/4, d/2, d, giving 0.6366 for L = d and 0.3183 for L = d/2; for L = 2d and 3d the expected number of crossings is still 2L/(πd).
- `check_week_130()`: a ring of diameter d always meets exactly one line, twice (1,000 random placements); seeded simulations of 40,000 drops give about 2/π crossings for a straight toothpick, a V and a zigzag, each of length d.
- `check_week_130()`: a straight wire of length πd crosses 0 to 4 times and averages 2 (about 10% zero, 22% one, 28% two, 39% three, 2% four in one seeded run); a wire of length 2d averages 4/π ≈ 1.27.
- `check_week_130()`: 500 toothpick drops at L = d give about 318 crossings with a standard deviation of about 10.7, so a ±1 standard deviation spread of π estimates runs from about 3.04 to 3.25.
- The dates 1777 and 1860 and the noodle theorem are cited from Armstrong and Bogomolny.

## Nearest existing themes

Week 59 (Constant-width shapes) proves that a Reuleaux triangle's perimeter is π times its width; Bogomolny's column connects that theorem to the crossing argument, so this week can return to Week 59's shapes as "noodles that always cross twice". Week 50 (Staircases and lengths) treats lengths of curves. Chance weeks 42, 43 and 44 use equally likely draws from bags; atlas AP-01 uses coin-toss walks. New here: continuous geometric probability, expectation as the right question, and linearity of expectation used as a proof. No existing week estimates π or uses expected crossings.

## App connection

Region "Chance and machines", possible family "Drop zone": a board of parallel lines where a child drops (taps) sticks, bent wires or a ring and the machine keeps the running average of crossings. Puzzle 1: "Make a wire that crosses more often on average than this one" (only longer wires work). Puzzle 2: "Bend this wire into a shape that always crosses the same number of times" (a ring of the spacing's diameter; a Reuleaux shape also works). An existing simulation family could carry it if one exists for repeated random trials with a running tally.

## Open questions

- Material fit: do pipe cleaners lie flat enough for crossings to be unambiguous, and does dropping from a fixed height give near-uniform angles on a small sheet? Rehearse before use.
- Age fit: is "average number per drop" meaningful to 2–3 children, or should they compare totals over the same number of drops?
- Counting rule: a wire touching a line exactly at an end, or lying along it, needs a stated convention.
- Whether to show the π estimate at all for K–3, or keep it as a 4–5 reveal.
