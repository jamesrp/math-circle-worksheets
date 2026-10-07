# Adversarial review: Week 78, Three-armed lines

## Verdict

Acceptable four-page Grades 4–5 prototype, with targeted nonblocking improvements recommended below. I found no incorrect printed mathematics, missing solution to a prescribed construction, rendering defect, source-portability failure, or mandatory scope violation. The run-local single-packet addendum controls; the absent K–1 and Grades 2–3 files and absent facilitator guide are correct.

The strongest weakness is in the concrete preparation for the final all-case argument: the prescribed intersection examples guarantee only one of the two genuinely different nonaligned configurations. The other can arise in the open first problem, but its appearance depends on a child's choices. This is a teaching-sequence risk, not a counterexample to the packet's mathematics.

## Prioritized recommendations

### 1. Medium, nonblocking: guarantee a nonaligned southwest/northeast intersection example before Problem 6

Location: Problems 1–2 and the transition to Problem 6.

Problem 2 supplies junction pairs `(2,5)/(6,2)`, `(3,2)/(3,6)`, `(2,4)/(6,4)`, and `(2,2)/(6,6)`. These cover the northwest/southeast singleton and all three shared-ray directions. The last pair has equal horizontal and vertical separation and is an overlap, so it does not supply the unequal-width/height southwest/northeast singleton case. Problem 4 uses such a configuration for the inverse problem, which is a different construction.

A child could choose four aligned or northwest/southeast trials in Problem 1 and reach “Can two lines ever miss each other?” without having confronted the other singleton mechanism. A false rule such as “the meeting is always the northeast corner of the junction rectangle” is then insufficiently challenged by the mandatory examples.

Recommended revision: guarantee one unequal-width/height southwest/northeast pair somewhere before Problem 6, while retaining meaningful choice and the three overlap cases. For example, junctions `(2,2)` and `(6,5)` meet at `(3,2)`; swapping their relative width and height gives the complementary north-arm case. A single added contrasting case is more valuable than extra explanation. Do not print the rectangle method or classification as a hint. Preserve the current generous grid scale and roughly four-page length.

This is recommended rather than a publication blocker because the brief leaves case selection to the writer, the open exploration can produce the missing case, and the adult can support the final argument.

### 2. Low, nonblocking: make continuation beyond the window something children can test

Location: first-page rules and Problem 6.

The continuation rule and the inclusion of points between grid dots are both stated correctly. However, all prescribed junction pairs are inside the same printed square. Their intersections are inside their junction rectangles, so none can actually look disjoint merely because the meeting was cropped away. All prescribed finite coordinates are integral as well. The broad final question therefore asks children to move beyond the page largely on verbal instruction.

If there is room when revising the preceding cases, one concrete off-window construction or counterexample would give this demand more substance. For example, the lines with junctions `(2,7)` and `(10,5)` meet at `(10,7)`, outside a `0`–`8` window. The necessary junction information must be explicitly supplied; an unexplained cropped picture would be unfair. This is an optional strengthening, not a reason to append an extra page or turn the packet into coordinate arithmetic.

### 3. Low, technical: make the finite-example checker fail if a case is added without an expectation

Location: `draft/src/check_math.py`, the `zip(...)` loops for printed examples.

The current expectation lists match the current data and every printed finite example passes. Nevertheless, ordinary `zip` silently truncates. Appending a new `INTERSECTION_PAIRS`, `INVERSE_GENERAL`, `INVERSE_ALIGNED`, or `EXAMPLE_POINTS` item can leave it unchecked while the script still reports “every printed finite example.” This is particularly relevant if recommendation 1 is adopted.

Add explicit length assertions, or use a compatible strict pairing mechanism, before those loops. When adding an example, update both its diagram data and exact expected result. This is a future-edit coverage weakness, not evidence that today's example results are wrong.

## Mathematical audit

The opening graph is the corner locus of `min(x,y,2)`, with junction `(2,2)`. Its east and north arms and slope-one southwest arm are correct. The marked example `(4,2)` has the repeated minimum `2` and lies on the east arm; `(4,4)` has two equal larger values and is correctly excluded. The explanatory example is allowed by the outline's explicit non-task-visual-example exception to the usual prohibition on worked answers.

All translations preserve orientation. The packet never permits a rotated arbitrary three-way road, imports ordinary Euclidean-line uniqueness, or substitutes a stable intersection for an overlapping set. Its instructions to trace shared stretches and to count points between grid dots are important safeguards.

Exact prescribed results:

- Problem 1: the only fixed coordinate is junction `A=(4,4)`; `B` is deliberately chosen by the child. Coinciding junctions are not prohibited here, so identical whole lines remain an available exploration.
- Problem 2, upper left: one point, `(6,5)`.
- Problem 2, upper right: the north ray starting at `(3,6)`.
- Problem 2, lower left: the east ray starting at `(6,4)`.
- Problem 2, lower right: the southwest ray starting at `(2,2)`.
- Problem 3: exactly two shared points are impossible. For distinct junctions the intersection is either a singleton or an entire shared ray.
- Problem 4, left: unique junction `(2,2)`.
- Problem 4, right: unique junction `(5,5)`.
- Problem 5, left: all junctions `(t,4)` with `t <= 2`.
- Problem 5, middle: all junctions `(3,t)` with `t <= 2`.
- Problem 5, right: all junctions `(t,t)` with `t >= 5`.

The open final tasks have valid all-real answers. For northwest/southeast junctions the northeast rectangle corner lies on both lines. For southwest/northeast junctions, moving southwest from the northeast junction by the smaller of the horizontal and vertical separations reaches the other line; unequal separations produce a singleton and equal separations produce a shared southwest ray. Equal x or y coordinates give the stated north or east overlap. Equal junctions produce identical whole lines. Thus no pair misses and no pair has exactly two shared points.

For the inverse problem, the possible junctions through one fixed point form the reversed fan with west, south, and northeast rays. Intersecting two such fans gives one junction for nonaligned distinct points and a whole ray of junctions in each of the three aligned cases. This independently explains the expected inverse results and supports Problem 7 without importing a Euclidean theorem.

## Student-page and visual audit

I freshly rendered and inspected every page at 130 dpi, rather than relying on extracted text or the writer's screenshots.

- Page 1: compact non-task rule example, then four substantial child-chosen trials. The distinction between a least tie and an irrelevant tie is visually and verbally clear. The “junction” label does not obscure the essential three-arm meeting. Text, grids, and footer fit.
- Page 2: four readable contrasting diagrams followed by the exactly-two-points question. Labels do not collide with dots. There is adequate blank space for the final explanation or sketch.
- Page 3: genuine inverse constructions followed by three complete-locus tasks. Open circles distinguish given points from the filled junction markers on earlier pages. Even the smaller three-column boards retain about 6.6 mm grid spacing. The current diagrams are usable with pencil at 100% size.
- Page 4: the general arguments come last, after experimentation and constructions. Blank grids and open space to their right permit a drawing plus explanation. The page does not give away a proof method.

Every page has the requested one-line header and footer, packet ID, and page number. Problem labels follow the required form. There are no extra activity headings, slogans, cute framing, unrequested adult notes, small lettered method steps, or automatic explanation prompts after every exercise. The seven problems collectively provide substantial work and an appropriate late extension for quick children. That timing judgment remains provisional because classroom use has not been tested.

No clipping, overlap, missing glyph, malformed arrow, unequal x/y scale, or visible page-break problem was found. Light-gray grid lines are legible in the digital render; their reproduction on the actual printer remains untested, as the README correctly discloses.

## Source, build, and verification audit

- The submitted PDF is four US Letter pages and 137,868 bytes, comfortably below 200 KB.
- The portable source folder contains only `README.md`, `build.py`, `check_math.py`, `data.py`, and `students.tex`. There are no downloaded diagrams, source papers, workflow prompts, or hidden asset dependencies in it.
- `python3 draft/src/check_math.py` passed the printed examples, 2,401 exact rational ray-intersection regressions, inverse constructions, minimum-tie tests, and common-shift tests.
- A fresh `--out` build passed. Its extracted text matched the submitted PDF exactly, and its LaTeX log had no overfull/underfull boxes, warnings, missing characters, or errors.
- I copied only those five portable source files to an isolated review directory and rebuilt there. All four rebuilt page PNGs matched the freshly inspected draft page PNGs byte for byte at 130 dpi. This confirms the portable source reproduces the reviewed appearance in this environment.
- The build script uses Python's standard library and invokes the declared TeX dependencies. Build products are confined to the chosen output folder. The README provides prerequisites, build commands, source attribution, and clear printing/manipulation/timing/classroom limitations.
- I checked the linked primary source, [Speyer and Sturmfels, *Tropical Mathematics*](https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf). Printed page 6 gives the repeated-minimum definition, page 7 gives the three-ray orientation, and pages 7–8 state generic intersection and interpolation. The README correctly separates these source facts from the prototype's independently derived exact ray classifications and examples.
- Finite regression is not an all-real proof; the README explicitly says so and makes no classroom-readiness claim.

The draft and its sources were not edited. All review, render, and rebuild artifacts remain in this run folder. No other workflow stage was started, and nothing was committed or pushed.
