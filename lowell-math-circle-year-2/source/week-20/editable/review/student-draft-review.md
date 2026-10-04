# Independent adversarial review

## Verdict

The packet is mathematically sound and visually clean. It is close to ready, with two concrete clarity fixes recommended before use and a smaller K–1 pacing/recording concern. I found no incorrect displayed numerical instance, accidental integer-only impossibility, broken diagram, clipped text, or false claim of existence. The strongest parts are the simultaneous-rule emphasis, the examples where an interior value really can equal a boundary extreme, and the progression to a general maximum principle in grades 4–5.

I read the brief first, independently rendered the three delivered PDFs at 90 dpi, and visually inspected all 20 pages: 7 K–1, 6 grades 2–3, and 7 grades 4–5. I then checked the graph data against the source and independently solved every fixed-value graph using exact arithmetic. I also exhaustively enumerated the bounded all-ways problems. I did not edit the draft or run its authoring workflow.

## Recommended revisions, in priority order

### 1. Make an empty neighboring place count explicitly in the K–1 rule

**Location:** K–1, page 1, packet-wide rule; immediately relevant to Problem 1 and especially Problem 3.

The rule says to share into “as many piles as there are joined stacks.” A zero-valued square has no physical stack. A young child hearing this once can quite reasonably count only the nonempty stacks. On the first board, that means sharing the 2 cubes into one pile rather than two; on the first star in Problem 3, it means sharing 3 cubes into one pile rather than three. These are exactly the boards chosen to introduce the action, so the ambiguity affects the foundation of the packet.

**Revision:** Count joined **shapes** or joined **places**, including an empty place, rather than physical stacks. Keep the instruction to use spare cubes so a check does not change the reference arrangement. This is a rule clarification, not a hint or a worked example. The intended mathematics is correct; the concern is how the physical instruction can be heard and enacted.

### 2. Visually identify the two disconnected pieces as one lower board

**Location:** Grades 4–5, page 6, Problem 6.

The problem refers to an upper board and a lower board, but the picture looks like a triangle and two separate two-circle boards. Every earlier group of disconnected diagrams has represented separate boards. Here, the intended new idea is apparently that the two lower pieces together make one board: that board has 25 fillings, whereas each separate piece has 5. A child who treats the two lower drawings as two boards is following the packet's earlier visual convention, not necessarily misunderstanding the mathematics.

**Revision:** Give the entire lower pair a shared visual boundary or another unmistakable grouping that does not resemble a graph edge. Do not add a line connecting the components, since that changes the answer from 25 to 5. This small change preserves the intended component-wise freedom without adding a method suggestion or a sentence that merely narrates the diagram.

### 3. Strengthen the weakest K–1 work unit; make the all-ways work easier to retain

**Locations:** K–1, especially page 3; secondarily pages 4 and 7.

Seven pages provide a respectable amount of material, and the all-ways/impossibility problems are genuine mathematics. Nevertheless, some early page counts overstate the amount of independent thinking. Page 3 contains just two three-neighbor stars, and the second is the first with 1 added everywhere. After making the two center stacks, the requested change has the same answer both times: add 3 cubes to any one square. A quick child can finish this well short of the organizer's five-minute target. This is a pacing risk, not a demonstrated failure of the whole forty-minute packet; physical handling and first encounters with the rule can take longer.

Pages 4 and 7 are the most substantial continuations, but each gives only one working diagram per board. Page 4 has eight position-specific arrangements; page 7 has six arrangements per board. There is blank paper space, but retaining multiple physical arrangements or recording them as a non-reader becomes an extra burden. The adult can help, but the current page does little to support that independence.

**Revision:** Give Problem 3 a genuinely contrasting or bounded inverse-construction case rather than only a translated repeat. Consider adding unobtrusive recordable diagram copies for the all-ways tasks in the available space, while keeping the main manipulatives diagrams at their current size. Do not add hints, solution steps, automatic explanation prompts, or headings. Recording copies are an enhancement rather than a rendering defect.

## Mathematical audit

Values below are reviewer checks, not proposed material for the student pages. Left-to-right/top-to-bottom order follows the rendered diagrams unless noted.

### K–1

- **Page 1:** Center stacks are 1, 3, 2, and 4. All are achievable with whole cubes.
- **Page 2:** Interior pairs are (1, 2), (2, 1), (2, 4), and (4, 2). The reversed paths offer a simple symmetry opportunity, although they are not four fundamentally different cases.
- **Page 3:** Centers are 1 and 2. Increasing either center by 1 requires adding 3 cubes to whichever single square is changed.
- **Page 4:** With entries ordered left square, circle, right square, the eight arrangements are (0,1,2), (0,2,4), (1,2,3), (2,1,0), (2,3,4), (3,2,1), (4,2,0), and (4,3,2). This is a sound all-ways question. Reversals are distinct positions on the printed board; no numerical count is demanded by the wording.
- **Page 5:** The interior pairs are (1,2) and (2,3), so neither board can contain a 5-cube circle while every circle works. This is a real impossibility task, not a missing-fraction accident.
- **Page 6:** The triangle's circles are both 2; all three circles on the lower cycle are 3. The fixed square need not itself average its neighbors.
- **Page 7:** Each connected board has exactly six fillings: every circle has the same value, chosen from 0 through 5. The absence of fixed squares is intentional and meaningful.

### Grades 2–3

- **Page 1:** Centers are 4, 4, 5, and 5. To increase a center by 2, a single square must increase by 4 on a two-neighbor board and by 6 on a three-neighbor board. This is a useful contrast.
- **Page 2:** Interior values are (3,6), (5,8), (3,3), and, on the tree, (4,6). All constraints hold simultaneously.
- **Page 3:** The path has (3,5,7); the tied diamond has (5,5). Neither admits the requested hidden peak. Asking for an impossibility explanation is appropriate here.
- **Page 4:** Top row: (3,6,6). Bottom row: (0,0,3). These correctly prevent an overstatement of the theorem as strict inequality. A fixed vertex in the middle legitimately separates a constant-valued branch from the other boundary value.
- **Page 5:** Fillings are (6,9), (5,7), and (7,7). None has a second filling with the same square values. This is a substantial later question; it does not falsely claim that uniqueness alone provides existence.
- **Page 6:** Each connected board has exactly six constant fillings, with common value 0 through 5. The finite integer restriction is deliberate and does not create an accidental impossibility.

### Grades 4–5

- **Page 1:** Fillings are (5,10), (5,7), and (8,8). The failed search for a second filling prepares the later uniqueness question without printing its proof method.
- **Page 2:** In the upper graph, the successive circle values are 3 and 6 across the top, then 7 and 8 across the lower pair. The diamond has (6,6). A value of 13 or more is impossible on both.
- **Page 3:** The statement is correct: the board is finite and every vertex can reach a fixed square. The bound is phrased using reachable squares, so it also handles multiple components. The illustrative graph has horizontal circle values (4,6,8) and top value 6. No proof is supplied to the children, which follows the organizer's standard.
- **Page 4:** Both boards have circle values (4,8,8), but only the top board has circles equal to its maximum square value. The contrasting role of a fixed interior square versus an unfixed branch point is mathematically worthwhile.
- **Page 5:** Both copies have left circle 6, upper circle 10, and lower circle 8. The universal uniqueness question is correct under its stated finite/reachability assumptions. It is a serious stretch beyond the concrete maximum principle, appropriate as later work with an adult; it does not need a printed signed-difference hint.
- **Page 6:** The upper triangle has 5 fillings. The whole disconnected lower board has 25, independently choosing a common value from 0 through 4 for each pair. See the grouping concern above.
- **Page 7:** The required circle values are 1/2; (1,2); 1; and (1/3,2/3). All required fractions are supplied with area representations. Whole-number existence is correctly treated as a separate issue.

## Visual and brief-compliance audit

- All three PDFs are US Letter. Every page has the required one-line week/topic/level header and one-line organization/week/packet footer, plus the correct page number.
- I inspected every rendered page individually. All task text, diagram edges, numbers, fraction labels, and footers are legible and contained within the page. I found no text/diagram collisions or ambiguous graph crossings. The source logs also contain no overfull/underfull or error warnings.
- The K–1 node diameter/side is 1.19 inches, approximately 3.02 cm, meeting the explicit minimum for standing stacks. The older packets use smaller writing nodes, approximately 1.73 cm, and their tasks ask children to fill numbers rather than stand stacks on them; this is not a violation of the conditional size requirement.
- Squares and circles are distinguishable without color. Fraction cards remain readable in grayscale.
- The K–1 numbered problems use one or two sentences and concrete small counts. The opening rule is more linguistically demanding than the individual problems, which makes the zero-place clarification especially valuable.
- The sheets avoid extra titles, mascots, praise, activity narration, worked solutions, little lettered substeps, and habitual explanation requests. Explanations are generally requested where impossibility, completeness, or uniqueness is the actual goal.
- The amount of older-band work is substantial, and the sequence reaches the local-to-global theorem rather than stopping at an arithmetic drill. The K–1 packet also reaches meaningful impossibility and completeness questions; retain these in any revision.

## Suggested disposition

Make the two small clarity fixes first. Review the K–1 pacing/recording suggestion against the organizer's unusually strict five-minute-per-problem standard. No wholesale rewrite, mathematical replacement, or layout repair is warranted by this review.
