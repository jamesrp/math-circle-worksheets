# Historical student-draft review

The two required wording changes below were applied in the included final student packets. This is the original project review record, retained for design context. The original renders and draft PDFs are omitted from this compact source bundle. See `release-validation.md` for the completed release checks.

# Independent adversarial review: Week 15

## Verdict

**Approve after two narrow wording fixes.** The draft is mathematically sound, unusually close to the organizer's requested register, and adequately substantial in all three bands. I found no incorrect site arrangement, impossible construction presented as possible, clipped content, overlapping labels, or broken PDF rendering. The two requested changes concern recording multiple nearest sites in K–1 and the meaning of a shared boundary in grades 2–3. Neither requires rebuilding the mathematical sequence.

I read `PROMPT.md` first, independently rendered the three delivered PDFs at 90 dpi into `review-render/`, and looked at **all 24 pages individually**. Each PDF has eight US Letter pages. I also inspected the generator and exact geometry checks, ran the author's checks, and independently recomputed relevant distances, half-plane inequalities, and vertices with rational arithmetic. I did not edit the draft.

## Changes to make

### 1. K–1, page 4, Problem 4: explicitly permit every nearest letter

The instruction is “Write the nearest dot's letter beside each cross.” This diagram has ordinary two-way nearest ties **and a three-way nearest tie**. Page 1's more specific recording instruction is “Use both letters for a tie,” which is appropriate there, with two sites, but does not tell a child how to record the new three-site case. The general opening rule allows multiple owners, so this is a local wording defect rather than an incorrect mathematical definition. It is still avoidable friction for children receiving instructions aloud.

At the central cross, all three letters A, B, and C are required. At the two high corner crosses the answers are AC and BC; the two lower central crosses require AB. The cross above the center belongs only to C, although its distances to A and B agree. The contrast is excellent and should not be muddied by a singular response instruction.

**Minimal repair:** “Write every nearest dot's letter beside each cross. Divide the sheet among A, B, and C.” This preserves the two-sentence limit and adds neither a hint nor a solution.

### 2. Grades 2–3, page 7, Problem 7: settle whether touching at one point counts

The instruction asks for D's region to share “a boundary” with A and B, but “no boundary” with C. In a packet that explicitly retains shared ties and has just explored a four-way meeting, this needs an unambiguous meaning. “Share a boundary” can mean sharing any boundary point or sharing a positive-length edge. These meanings produce different judgments of a natural student placement.

For the printed sites A = (−2,0), B = (2,0), C = (0,2), put D at (0,−2). D has positive-length shared edges with A and B, and D and C meet only at the four-way tie (0,0). This succeeds under an edge-adjacency reading but fails under a no-shared-points reading. An adult should not have to decide what the question meant after a child produces it.

**Minimal repair, if no contact with C is intended:** “Put D in the frame so its region shares places with A's and B's regions, but no places with C's region. Draw all four regions.” If only positive-length edges are intended, say so instead. Do not forbid point contacts implicitly.

The task is feasible even under the stronger no-contact requirement: D = (0,−5/2) works. This is a wording issue, not an impossible problem.

## Lower-priority considerations

- **“Keep the dots fixed” versus placement problems.** The opening rule is defensible as “do not move sites within a map,” but “Keep the printed dots fixed” would be clearer when later problems ask children to choose new dots. This is optional; the existing instructions can be understood correctly.
- **Individual problem duration.** Eight full working maps give each band enough total material, including genuine inverse and impossibility tasks. A quick older child may nevertheless finish the square map in grades 2–3 Problem 4 or grades 4–5 Problem 4 in less than the requested five minutes after understanding the earlier maps. That is a modest per-problem pacing risk, not a shortage of work for the hour. Avoid adding routine explanations or mechanical extra dots merely to fill time. The adjacent insertion problems provide substantial continuation.
- **The grades 4–5 convexity question is initially about one region.** Problem 3 correctly asks about every pair of points in the pictured D region; it does not, by itself, ask for a statement about all possible nearest-site regions. Problem 8 usefully requires that broader reasoning in a concrete case. This is a reasonable progression. If a general convexity result is considered essential before children may stop, the current ordering should be considered deliberately rather than treating Problem 3 as already having asked for that result.

## Page-by-page audit

### K–1

1. **Problem 1:** Sixteen well-spaced comparison crosses, including three two-way ties, provide concrete length comparison. The two site centers are clear. The instruction is short, and letter responses have room. It appropriately samples points before later problems request entire regions.
2. **Problem 2:** The oblique two-site arrangement is a purposeful contrast with page 1. It requests the continuous division and shared places without telling children a construction. The boundary is 3x + 2y = 0 in the generator's coordinates.
3. **Problem 3:** Three collinear, equally spaced sites give two parallel boundaries and a middle strip. The outer-site tie line is beaten by the middle site, so the task contains meaningful competition rather than three independent bisectors. No site or label overlaps.
4. **Problem 4:** The intended triangle arrangement is exact, and the probes include all relevant phenomena: sole winner, genuine pairwise nearest tie, three-way nearest tie, and an A/B equality beaten by C. Apply finding 1.
5. **Problem 5:** The square is genuinely symmetric and gives a four-way tie at its center. The question avoids the false claim that only three regions may meet.
6. **Problem 6:** The added center is correctly positioned. Its nearest region is the intended diamond. The old sites and labels stay in exactly the same positions as page 5.
7. **Problem 7:** A valid inverse-placement task with a concrete two-site start. Adding a site at the midpoint gives it places formerly nearer each old site. The subsequent full map makes this more substantial than simply locating one point.
8. **Problem 8:** The exact target strip is visible with dashed sides as well as gray fill. Two sites reflected across its vertical edges produce it. “Inside the frame” properly limits the target comparison; the strip is not incorrectly treated as a bounded whole-plane cell.

### Grades 2–3

1. **Problem 1:** The diagonal site arrangement and fourteen crosses have correct ties on x + y = 0. Asking for the boundary after labeling crosses moves beyond the sampled points. The text and diagram fit comfortably.
2. **Problem 2:** P is nearer C alone; Q is tied between A and B. Asking for all three regions makes the distinction matter for the whole map. The P/Q labels are clear and distinct from site symbols.
3. **Problem 3:** Unequal collinear spacing avoids merely repeating the K–1 symmetric strip. The two live boundaries are x = −5/4 and x = 3/4; no point is nearest to all three. The requested explanation has a genuine mathematical purpose.
4. **Problem 4:** The four closed quadrants and every shared point are well posed. All four sites share the origin. Potentially quick, as noted above.
5. **Problem 5:** The perturbed-square diagram is nondegenerate and has a short but workable interior edge. It contrasts usefully with page 4. The adjacent pairs are AB, AD, BC, BD, and CD; AC has no shared point. Both triple vertices fall comfortably inside the map.
6. **Problem 6:** The printed sites match Problem 4, and the center insertion gives the intended diamond. The referenced old map is available two pages earlier. Asking which old boundaries disappear focuses directly on the second kernel.
7. **Problem 7:** The construction is feasible, but clarify point contact versus edge-sharing as in finding 2.
8. **Problem 8:** The shaded bottom-left portion is a correct clipped target for an unbounded region. Sites at (2,0) and (0,2), with their labels interchangeable, give A exactly x ≤ 1 and y ≤ 1. The words “part of the frame” correctly avoid claiming the whole region is a square.

### Grades 4–5

1. **Problem 1:** A whole-region task with a useful demand to explain why the boundary works for every point. It asks for certification rather than more measurement. The oblique configuration discourages reading off a vertical center line.
2. **Problem 2:** Correct P/Q contrast and exact triangle arrangement. The task does not suggest retaining every pairwise bisector.
3. **Problem 3:** D's whole region is bounded, triangular, and entirely visible. The straight-segment question is correct and has room for drawing or a written explanation below the map. It avoids introducing algebra as a prerequisite.
4. **Problem 4:** The square arrangement supplies the intended counterexample to “exactly three meet.” There is exactly one point shared by three or more nearest sites, and it is shared by all four.
5. **Problem 5:** The map correctly repeats the prior four sites and inserts E. Shrinkage of old regions and disappearance of old boundary portions are both well posed. Endpoints where three regions still tie should remain in the boundary; the prompt does not tell students otherwise.
6. **Problem 6:** A sound minimum question: two new sites suffice to bound B's original vertical strip inside the frame, and one cannot eliminate both directions of its vertical unboundedness. “Entire region” explicitly distinguishes the plane from the displayed window.
7. **Problem 7:** The inverse triangle is achievable with precisely three reflected sites, all fitting in the displayed frame. The site A lies strictly inside the target triangle. Dashed edges keep the task usable without relying on fill color.
8. **Problem 8:** Correct possible/impossible contrast. R cannot be removed while P and Q remain in A's region, including the shared-tie convention. S can. The marked P, Q, R, and S are probe crosses, not accidentally styled as competing sites.

## Mathematical verification details

These are reviewer checks, not text to add to the student pages.

- For A = (−2,0), B = (2,0), C = (0,2), comparison gives A: x ≤ 0 and y ≤ −x; B: x ≥ 0 and y ≤ x; C: y ≥ |x|. Thus the A/B boundary is only x = 0, y ≤ 0. P = (0,1) belongs only to C, Q = (0,−1) belongs to A and B, and the origin belongs to all three.
- For the four square-corner sites, the cells are closed quadrants. Inserting the origin yields the diamond with vertices (−2,0), (0,−2), (2,0), (0,2). On each old axis boundary, points with distance strictly less than 2 from the origin cease to be shared by the old nearest sites. The four diamond vertices retain ties.
- The irregular grades 2–3 Problem 5 has triple vertices (0,−1/2) for ABD and (3/8,0) for BCD. The interior BD edge joins them, with length 5/8 coordinate unit, about 0.60 inch on the page. This is visibly nonzero, not a misleading almost-four-way junction.
- Grades 4–5 Problem 3 gives D the triangle with vertices (−7/4,1), (7/4,1), and (0,−5/2). It is the intersection of the three winning half-planes; a segment between two allowed points remains in each half-plane.
- For grades 4–5 Problem 6, new sites at (0,2) and (0,−2) give B the square [−1,1] × [−1,1]. Any one new site's winning half-plane intersects the original strip in a set still unbounded in at least one vertical direction, so one does not suffice.
- For the inverse triangle in grades 4–5 Problem 7, new sites at (0,−2), (24/13,16/13), and (−24/13,16/13) give exactly the three pictured edges and vertices. There is no hidden requirement to place a site outside the map.
- For grades 4–5 Problem 8, adding a site at (0,−5/2) leaves P, Q, and R strictly nearer A but makes S nearer the new site. R's impossibility follows from the segment PQ lying in every half-plane that retains both endpoints.

## Production and style checks

- All three delivered PDFs are eight pages, with 612 × 792 point media boxes and equal horizontal/vertical map scales.
- Every map is 5.8 inches square, within the brief's 5–6 inch range. All sites have visible centers; crossings, labels, and target outlines remain legible in grayscale.
- Every page has the required one-line week/topic/level header, the correct packet footer, and its page number. The only other headings are the numbered “Problem N:” labels.
- No clipping, overflow, unwanted blank pages, overlapping task text, broken glyphs, or obscured diagram elements appeared in the independent renders.
- All K–1 problems use one or two sentences. The youngest band has eight pages of genuine region, tie, insertion, and inverse-placement mathematics; it is neither a shortened consolation packet nor an arithmetic worksheet.
- There are no mascots, promotional titles, exclamation marks, automatic “what do you notice?” follow-ups, lettered procedural steps, or printed solution methods. Explanation requests are attached to actual certification, impossibility, or minimum questions.
- The sources contain a font-map warning, but the resulting PDFs have embedded Latin Modern fonts and rendered normally. This is not an observed delivery defect.
- Preserve the large work areas and restrained wording. Do not repair the two clarity issues by adding worked boundaries, general-position terminology, coordinate formulas, or a student-facing facilitator guide.
