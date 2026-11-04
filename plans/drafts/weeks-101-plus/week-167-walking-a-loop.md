# Week 167 (draft plan): Walking a loop

**Strand:** shape (Shapes and spaces). **Deep-math field:** differential topology of plane curves, turning number. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Walk once around any simple closed path (one that never crosses or touches itself) and you turn, in total, through exactly one full turn: left turns minus right turns equal 360°, or 4 quarter turns on a grid. This is Hopf's Umlaufsatz (theorem of turning tangents, Compositio Mathematica 1935): the tangent direction of a simple closed curve changes in total by exactly ±2π, with corners counted by their turning angles. Hopf credits the idea probably to Riemann and the first proof with suitable hypotheses to G. N. Watson (1916), and gave a short proof of his own. For loops that cross themselves the total can be any whole number of turns: a figure eight turns 0, a five-pointed star drawn in one stroke turns twice, a loop walked twice around turns twice. This whole number is the turning number (rotation number), and Whitney (Compositio 1937, on a suggestion of W. C. Graustein) proved that it is the only thing that matters: two smooth closed curves with no stops or cusps can be deformed into each other, without ever making a corner or a cusp, exactly when their turning numbers agree. So a figure eight can never be smoothly wiggled into a circle. Whitney also showed how to read the turning number from the crossings of a curve in general position. Turtle geometry (Papert's Logo) gives the classroom form: a turtle that repeats "forward, turn left by A degrees" comes home facing its starting direction after 360/gcd(A, 360) steps, having turned A/gcd(A, 360) full turns, and it is then also back at its starting point (the closing rule, because the steps form a balanced set of directions); A = 72 gives a pentagon (1 turn), 144 a star (2 turns), 135 an eight-point star (3 turns). Limits: the Umlaufsatz needs a simple loop; smoothness is needed for Whitney's theorem, while the turn count itself makes sense for polygons. Proved: both theorems. Checked here: the grid loops, the turtle table and the closing rule. What children can discover: every simple loop turns once; crossing loops can turn 0, 2 or more; a pattern that predicts when a repeating turtle closes and how many turns it makes.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Über die Drehung der Tangenten und Sehnen ebener Kurven](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hopfdreh.pdf), Heinz Hopf, Compositio Mathematica 2 (1935), 50–62 (bibliographic record at numdam) (read November 4, 2026). The Umlaufsatz for simple closed curves, its extension to curves with corners, and the history (Riemann, Watson 1916, other proofs).
- [On regular closed curves in the plane](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/whitcurv.pdf), Hassler Whitney, Compositio Mathematica 4 (1937), 276–284 (read November 4, 2026). Theorem 1: deformable exactly when the rotation numbers agree, suggested by Graustein; Theorem 2: the rotation number from signed crossings; the Umlaufsatz as a special case.
- [Exploring Turtle Geometry through Polygons and Spirals with TurtleArt](https://el.media.mit.edu/logo-foundation/services/pdf/Exploring%20Turtle%20Geometry%20through%20Polygons%20and%20Spirals.pdf), Cynthia Solomon, Logo Foundation (undated) (read November 4, 2026). The Total Turtle Trip Theorem, regular polygons turn 360°, stars more; "test the theorem out by being a turtle"; floor turtles in classrooms.
- Prior use with children: [Walking Round a Triangle](https://nrich.maths.org/8084), NRICH, ages 5 to 7 (read November 4, 2026). A ladybird walks round a triangle; how far has it turned when it gets back? A student's answer: a full 360°, for any triangle.

## A kid-friendly way in

Masking-tape paths on the floor (a rectangle, an L-shaped room, a wiggly loop, a figure eight, a five-point star), each with a start arrow; a "turn dial" per pair (a paper plate with a brass-fastener pointer; a partner turns the pointer each time the walker turns and makes a tally mark each time it passes the top); turtle cards (FORWARD 1, TURN LEFT and TURN RIGHT by quarter or eighth turns) and dot-grid paper. Prep about 25 minutes, mostly taping five paths. Launch (2–3 minutes): one child walks the tape rectangle while a partner turns the dial's pointer a quarter turn at each "left!" called by the group; back at the start, the pointer has made exactly one full turn. Ask: will a wigglier path turn more?

Suggested hour: 0–5 rectangle walk; 5–25 tape-path stations with dials; 25–40 grid loops drawn for a partner; 40–55 turtle repeats and stars (4–5); 55–60 share the figure eight and the star totals.

## By band

- **K–1:** Walk the tape paths with the dial and count left turns and right turns with clothes pegs on a "left" card and a "right" card; compare the piles at the end. Walk the figure eight: what happens to the dial?
- **2–3:** Draw grid loops for a partner and predict left minus right before walking them (the answer is always 4 quarter turns for loops that never cross). Make loops that cross themselves: which totals can you make (0, 8, ...)? Can a loop that crosses itself still total 4?
- **4–5:** Turtle repeats: "forward 1, turn left A" for A = 90, 120, 72, 60, 144, 135, 150. Predict how many steps until the turtle is home and how many full turns it made; find the rule (steps 360/gcd(A, 360)). Why does the turtle come home in position when it comes home in direction? Story: Whitney's theorem, and why no smooth wiggling turns a figure eight into a circle.

## Checked facts

In `check_shape_2.py`, `check_week_167()`: turtle repeats close after 4, 3, 5, 6, 5, 8, 12 and 9 steps for A = 90, 120, 72, 60, 144, 135, 150 and 160, with 1, 1, 1, 1, 2, 3, 5 and 4 full turns, and for every whole A from 1 to 359 the steps 360/gcd(A, 360) bring the turtle back to its start; all 20,144 closed self-avoiding grid walks of length up to 14 from a fixed start have left minus right equal to +4 or −4 quarter turns; a figure-eight grid walk totals 0 and a square walked twice 8; a notched rectangle has 5 left and 1 right turns. The theorems are cited.

## Nearest existing themes

Week 65 (Hyperbolic octagon streets) already uses "left minus right is 4 around squares" as the flat baseline for a discrete Gauss–Bonnet; this draft must not repeat that as its main event. Its new content is the self-crossing case (turning numbers 0, 2, 3), the turtle closing rule and Whitney's classification. Week 41 (Portals) and Week 75 (Twists on a cylinder) count windings of paths on surfaces by seam crossings; atlas GA-04 winds an arrow around a dial; Week 85 (Drawing machines) draws by machines. The Week 165 draft (inside or outside) uses the winding of a curve around a point, a different count. Draft 142 (space-filling curves) uses a turtle rule to draw the Hilbert curve.

## App connection

Shapes and spaces, near Octagon streets (Week 65), which already has a walking turtle. Board: a grid where the child builds a closed path from forward and turn tiles; a dial in the corner shows the running turning total. Puzzles: "Make a closed path that turns twice"; "Make a figure eight"; "Choose the turn angle so the turtle makes a star with 7 points"; "Which of these four loops can be wiggled into a circle without a sharp corner?" (by turning number).

## Open questions

- Overlap with Week 65: decide whether this week runs before it as preparation or is reshaped around turtle stars and the figure eight.
- Dial fidelity: can a K–1 partner keep the pointer in step with the walker, especially at the star's sharp corners (144°, between a quarter and a half turn)? Rehearse with two or three children.
- gcd is beyond grades 4–5 as notation; the guide should phrase the rule as "the first time A times the steps is a whole number of full turns".
