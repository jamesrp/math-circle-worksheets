# Week 204 (draft plan): The fastest slide

**Strand:** analysis, with shape (app region "Shapes and spaces"). **Deep-math field:** calculus of variations, optimisation of travel time, the cycloid. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A bead slides without friction from rest at A down to a lower point B, not directly below. Which track gets it there soonest? Not the straight line, which is shortest: the bead gains speed only by dropping (its speed at depth y is √(2gy)), so a track that falls steeply first and spends the long middle stretch moving fast wins. The fastest track is an arc of a cycloid, the curve traced by a point on the rim of a rolling wheel, turned upside down. Johann Bernoulli posed this "brachistochrone" problem in Acta Eruditorum in June 1696; at Leibniz's urging the deadline was extended, and solutions came from Johann, his brother Jacob, Leibniz, Newton (anonymously, in the Philosophical Transactions, January 1697) and de l'Hôpital (whose solution was printed only in 1988). Johann's solution treats the track as light crossing many layers of glass of increasing speed: Fermat's least-time principle gives the sine law at every layer, and in the limit that law with v = √(2gy) is the cycloid. Galileo (1638) had correctly shown that a two-segment path through a point on a circle beats the straight chord, then wrongly concluded that a circle arc is fastest. Jacob's follow-up questions started the calculus of variations. The cycloid also has the tautochrone property, found by Huygens (1659): released from rest anywhere on the arc, the bead reaches the bottom in the same time, π√(a/g) for a wheel of radius a. Concrete numbers (computed): for a 30 cm drop over 47.1 cm, where the cycloid ends at its lowest point, the straight ramp takes 0.461 s, a circle arc 0.393 s and the cycloid 0.388 s. Over 1 m with the same drop the cycloid dips about 10 cm below the finish and still wins clearly: 0.861 s straight, 0.691 s circle, 0.594 s cycloid. A rolling solid ball has v² = (10/7)gy rather than 2gy, which stretches every time by the same factor √(7/5), so the ranking does not change, but real marbles also lose to friction and bumps, which these numbers ignore. Proved: the cycloid minimises time among smooth tracks (calculus of variations) and is tautochronous. Checked here: the race times by numerical integration. Children can discover that the shortest track is not the fastest, that a track that dips below the finish can still win, and, on a cycloid, that marbles released at different heights arrive together.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The brachistochrone problem](https://mathshistory.st-andrews.ac.uk/HistTopics/Brachistochrone/). J. J. O'Connor and E. F. Robertson, MacTutor History of Mathematics, St Andrews, 2002. Galileo's 1638 error, Johann Bernoulli's June 1696 challenge, the solvers, Newton's anonymous solution (January 1697), publication in May 1697, Johann's refraction method, Huygens' tautochrone (1659) and the start of the calculus of variations (read November 4, 2026).
- [Cycloid Experiment for freshmen physics labs](https://arxiv.org/pdf/1702.06597). R. Akoglu, S. Habib Mazharimousavi and M. Halilsoy, arXiv 1702.06597, 2017. A billiard ball on a 2 m grooved flexible track over eight paths: straight 0.740 s, cycloid 0.652 s (the minimum), deeper curves slower again; the rolling factor 10/7; the tautochrone as a proposed extension (read November 4, 2026).
- [Brachistochrone](https://sciencedemonstrations.fas.harvard.edu/presentations/brachistochrone). Harvard Natural Sciences Lecture Demonstrations. A straight and a cycloidal track; the cycloid ball always arrives first (read November 4, 2026).
- Prior use with children: [Which ball will reach the bottom first?](https://thekidshouldseethis.com/post/which-ball-will-reach-the-bottom-first). The Kid Should See This, with a video from T. Ross Kelly's Gravitational Illusions: a straight ramp against a ramp with dips, posed as "pause and predict" for families and classrooms (read November 4, 2026). No K–5 math-circle handout was found; searches for brachistochrone lessons with marbles, toy-car track and elementary classes found science-fair projects and university demonstrations.

## A kid-friendly way in

Materials per table: two lengths of flexible toy-car track or 1 m strips of cardboard folded into a V channel (about 3 cm), two identical marbles or steel balls, masking tape, a stack of books for the start (about 30 cm high), a printed cycloid template (a large paper sheet with the curve, made by rolling a can with a pen taped to its rim along a ruler, or printed). Prep: about 25 minutes (cut and fold channels, print or trace one cycloid per table). Launch (3 minutes): an adult holds two tracks from the same start to the same finish, one straight and one bent into the cycloid template; the group votes, then a ruler held across both start points releases the marbles together. Then roll a can with a pen on its rim so children see where the curve comes from.

Suggested hour: 0–5 launch race; 5–25 free design: bend the flexible track into any shape and race it against the straight one; 25–45 band questions; 45–60 tautochrone surprise on the cycloid board and the Bernoulli story.

## By band

- **K–1:** Race the straight ramp against a bent one, guessing first each time. Can you bend a ramp that wins? A ramp that loses? Draw a winning shape.
- **2–3:** Keep the start and finish fixed and change only the shape: steep first, shallow first, a dip below the finish. Which shapes win, and is the shortest ramp ever the winner? Record each race with a winner sticker on a drawing of the track.
- **4–5:** Explain why steep-first can win though the track is longer (speed comes only from dropping). Release two marbles at once from different heights on the cycloid board: who arrives first? Compare with the same test on a circle arc. Then the light story: how Johann Bernoulli turned a sliding bead into bending light.

## Checked facts

- `check_week_204()`: for a 30 cm drop over 47.1 cm (cycloid with a = 15 cm ending at its bottom), straight 0.4605 s, circle arc 0.3931 s, cycloid 0.3885 s = π√(a/g); the straight time equals √(π² + 4)·√(a/g), 1.185 times the cycloid's.
- `check_week_204()`: Galileo's square case (30 cm down, 30 cm across): straight 0.3497 s, quarter circle 0.3242 s, cycloid 0.3193 s.
- `check_week_204()`: 1 m across, 30 cm down: the cycloid dips about 9.7 cm below the finish; straight 0.861 s, circle 0.691 s, cycloid 0.594 s.
- `check_week_204()`: released from rest at five different points of the cycloid, the time to the bottom is the same 0.3885 s to within 10⁻⁷ s.
- `check_week_204()`: rolling multiplies every time by √(7/5) ≈ 1.183. Friction, track joins and the groove's contact geometry are not modelled.
- The optimality of the cycloid is cited, not computed.

## Nearest existing themes

No week or draft uses the brachistochrone or the cycloid. Atlas AP-12 (fastest crossing between two speeds, the sine law) is the one-boundary version of Johann Bernoulli's argument and could be the 4–5 bridge. Week 21 (shortest route touching a line) and atlas GA-21 optimise length; this week optimises time, where the shortest route loses. Week 59 (constant-width shapes) rolls shapes and meets π; draft 160 meets epicycloids as envelopes. New here: travel time as the quantity to minimise, a curve found by a variational principle, the tautochrone, and a famous public challenge from 1696.

## App connection

Region "Shapes and spaces", possible family "Fastest slide": the child drags four or five control points to shape a track between fixed ends; pressing Go races a bead on their track against a ghost on the straight line, with a timer computed from v = √(2gy) (no physics engine needed, only the integral). Puzzle 1: "Beat the straight track." Puzzle 2: "Beat the circle-arc ghost" (very close; needs a near-cycloid). A tautochrone level releases three beads at once.

## Open questions

- Material fit: do flexible tracks or cardboard channels keep the cycloid shape well enough, and is the 0.07 s difference at 30 cm visible? A longer, shallower course (1 m across) gives a bigger gap; rehearse before choosing.
- Fair release: a ruler gate across both starts, or a two-child countdown? Untested.
- The circle arc and cycloid differ by about 1% in the first race, too close to see; use it only as an adult note or in the app.
- Whether the tautochrone works with real rolling marbles on a homemade track is untested.
