# Week 77 adversarial review

## Verdict

The draft passes the mathematical and digital-production checks. There is no demonstrated mathematical error, illegal prescribed schedule, clipped diagram, or missing page. It is a coherent four-page shared Grades 4–5 prototype, as required by the scope addendum. Do not create younger-band packets or add an adult guide in response to this review.

The strongest concern is the amount of independent work available after a quick child understands the cancellation rule. The packet has only two underlying two-face boards. Some nominally separate problems are very short consequences or constructions. This is a pacing risk to address or explicitly retain for piloting, not evidence that the topic is too advanced or that it requires wholesale redesign. Smaller revisions could remove repeated instructions and make preparation and simultaneous additions less dependent on adult interpretation.

## Findings, in priority order

### 1. Medium: the upper end of the workload is not convincingly forty minutes

**Locations:** page 3, Problem 3; page 4, Problem 5; the packet as a whole.

Problem 1 offers the three nonempty square cycles, Problem 2 has four edge/fill orders, Problem 3 asks for only two of four very simple orders, and Problem 4 offers four changes, two of which immediately violate the boundary rule. Once the child has established the cancellation mechanism, Problem 3 can be satisfied by closing the left triangle first and changing which triangle fills first. Its final yes/no question follows immediately from the two requested builds and the counts already printed. Problem 5 is worthwhile, but a child who remembers a successful cancelling set can answer it with a single invariant: those filled triangles remain available. It is not reliably a separate five-minute investigation.

This does not establish a measured completion time. Learning to retain an unchanged loop, finding and checking all three solutions to Problem 2, and explaining completeness may occupy much of a session. Nevertheless, the organizer specifically wants a quick child not to run out, and the draft has no substantial further construction after these small case sets.

**Recommended response:** strengthen one later child-controlled construction or repair problem, using a concrete specified board and a goal with genuinely contrasting cases. Alternatively, retain the current brief core deliberately and mark its fast-finisher provision as unresolved before classroom release. Do not lengthen it by adding repeated count tables, routine explanations, or barcode bookkeeping. Keep Problem 5's general argument; the concern is relying on it for much additional working time. This is an unpiloted judgment, not a proven classroom failure.

### 2. Low: duplicate schedule instructions add reading without adding a mathematical choice

**Location:** page 2, Problem 2 and the stage list; `students.tex` lines 61 and 64–68.

The paragraph gives all four scheduled actions and then the nearby stage list gives them again. This is a direct opportunity to follow the organizer's brevity standard more closely. The list is useful: it externalizes the changing state and leaves the child in control of the two choices. The prose could simply establish the goal, saving the first loop, and completeness, leaving the schedule to the legible printed list. Do not remove the list and require children to hold the whole schedule in working memory.

The page 1 shared rules also require a relatively long first read before the first action, but almost all of that text establishes genuinely necessary conventions. Preserve the non-task input/intermediate/output demonstration rather than treating it as an unwanted worked answer.

### 3. Low: make the distinction between physical placement and a completed simultaneous stage explicit

**Locations:** page 1 shared rule that all three edges are present “first”; page 4, Problem 4's simultaneous `AC` and filled `ABC`.

The intended mathematics is sound. The draft correctly says to check the board only after both additions. Still, a literal referee could interpret “first” as requiring a strictly earlier numbered stage, and reject the prescribed stage 4. Another child could momentarily place the edge, count two holes, and regard that as a recorded stage despite the later instruction.

A short clarification that an edge and its face may arrive in one numbered stage, with the boundary physically placed before its tile, would remove the possible conflict. It need not introduce a second recording system or show the repair solutions. The existing page 4 instruction already goes much of the way; this is a small operational clarification, not a mathematical blocker.

### 4. Low, preparation only: the demonstration's token labels are absent from the material inventory

**Locations:** page 1's `XYZ` demonstration; source README, “Print and materials.”

The inventory provides three copies of each task-edge label but none of `XY`, `YZ`, or `XZ`. If the short whole-group launch is to enact the exact printed example with tokens, it needs two `XY`, two `YZ`, and one `XZ` token, and a way to indicate that `XYZ` is already filled. The printed diagram is sufficient for visual reading, so this is not a missing student-page resource. Either add the small demonstration inventory to the README or state that this example is demonstrated directly on the printed figure.

## Mathematical audit

I independently followed the finite cases and ran the supplied `check_math.py`. All assertions passed. In particular:

- **Demonstration:** `XY + YZ + boundary(XYZ)` leaves `XZ` after matching pairs cancel. This is a non-loop input, appropriately introduced only as a token-operation example. It neither gives away the target square loop nor incorrectly claims that a remaining token proves a loop survives every possible test.
- **Problem 1:** the square with diagonal `AC` has exactly three nonempty mod-2 cycles: triangle `ABC`, triangle `ACD`, and the outer rim. Either triangular loop can disappear with one matching filling. The outer rim survives either single filling and disappears after both. The child may need to add the diagonal to make a chosen face legal; the shared build rules permit that addition. Nothing tells the child to remove pieces during a build.
- **Problem 2:** all four schedules are legal and have counts `0, 1, 2, 1, 0`. Exactly three keep the first saved loop until stage 8: `(DA, AC; ABC, ACD)`, `(DA, AC; ACD, ABC)`, and `(AC, DA; ACD, ABC)`, listing edges at 2/4 and faces at 5/8. The excluded schedule `(AC, DA; ABC, ACD)` kills its first loop at 5. This is a genuine choice of construction order, not an arbitrary naming of visible cavities.
- **Problem 3:** the two triangles share only the explicitly marked vertex `C`. Closing either triangle first and filling that same triangle at 5 kills the old loop at 5. Filling the other triangle at 5 preserves the old loop until 8. There are two schedules of each kind. Their stagewise hole counts agree. The supplied checker also verifies the distinct persistence histories through inclusion-map ranks, not merely through those counts.
- **Problem 4:** the original finished stages have at most one hole. Moving `AC` to 3 or moving filled `ABC` to 5 produces a genuine two-hole stage. Moving `AC` to 5 or filled `ABC` to 3 is illegal. The simultaneous original addition correctly contributes no lasting second feature. The text does not ask children to record an internal placement order as a new numbered stage.
- **Problem 5:** once a set of filled-triangle boundaries cancels the saved loop, that same set remains available at every later stage. Hence the saved loop cannot become nonzero again. The finite checker tests all nested face subsets on both printed boards. Those finite tests alone are not a proof for every legal board; the persistent cancelling-set argument supplies the general proof.

The enclosed-unfilled-region convention is valid for these particular noncrossing planar boards. The draft does not introduce an unjustified general cycle-count formula, equate visible graph cycles with holes after filling, attach arbitrary identities to child cavities, introduce matrix algebra, or make unsupported claims about noise, signal, or stability.

## Visual and practical audit

I rendered and inspected **all four pages** at 110 dpi.

- All pages are US Letter with consistent headers, footer identifiers, and page numbers. The only prominent headings are the required problem labels. The response labels function as short answer prompts rather than separate activity titles.
- Text, vertex labels, arrows, tokens, rules, and diagrams are legible. No clipping, collisions, missing glyphs, overflowing lines, or accidental extra pages were found.
- The dashed/solid distinction survives grayscale. The triangle example has a visible filled interior. The square has 6.2 cm sides; the joined-triangle board is 11.6 cm by 5.8 cm. These dimensions agree with the README.
- The joined-board intersection is an actual labeled vertex, not a silently identified crossing. The task triangles do not overlap in their interiors.
- The cancelled pairs in the non-task example are visibly crossed out, and the remaining token is shown. This satisfies the special requirement for an explicit input/intermediate/output convention example.
- There is useful writing space on every page. Problem 2 can accommodate the three schedules and a short completeness explanation, though children writing each stage on a separate line may need another sheet. It does not force simultaneous count, barcode, and saved-loop records.
- Matching tiles are prepared from extra copies, not supplied as a separate cutout sheet. This is disclosed in the README. Tracing/cutting, marker placement, tile coverage of edges, three-child role rotation, and actual readability/handling at print size remain untested. Rendering does not establish those properties.

## Build and source audit

The portable source folder contains exactly the expected original source, builder, verifier, and README. It contains no downloaded paper, borrowed pictures, workflow prompts, or generated TeX runtime files.

I rebuilt the unchanged source with the supplied `build.py --out` interface, using the separately provided cloud TeX runtime configuration. The build succeeded with no TeX warnings or overfull/underfull-box notices. The extracted text of the rebuilt PDF matches the delivered draft. The supplied draft has four pages and is **58,314 bytes**, comfortably below the practical 200 KB target. The builder is standard-library Python, runs the mathematical checks, uses a temporary compilation directory, and does not require a network call.

The README states prerequisites, materials, build commands, prototype status, and physical/classroom limits. Its provenance statement points outside the portable source to the run's research note; I did not review another workflow stage or treat an external paper as necessary to validate these small independently specified examples.

## Revision boundary

Preserve the central design: saved loop lists remain fixed, cancellation happens only on disposable test tokens, a partner checks legal face additions, and children choose construction orders. The current mathematical model and all explicit answers are correct. Any changes should primarily improve the amount of child-owned experimentation and trim or clarify instructions. Re-run the finite verifier and visually inspect all pages after revisions; keep any new example in the verifier. Do not claim physical or classroom validation without a separate rehearsal.
