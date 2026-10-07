# Week 71 adversarial student-packet review

## Verdict

**Mathematically sound; retain, with small operational revisions and a required physical rehearsal before classroom use.** The packet gives children genuine choices of rays, a checkable obstruction, an information game and a substantial final indistinguishability question. I found no wrong bounce word, invalid reflection example, distorted candidate shape or page overflow. The main risk is that the free-choice game moves beyond the supplied exact tracing apparatus, so adults may end up operating the geometric checking rather than merely supporting it.

Reviewed the authorized shared Grades 4–5 `draft/students.pdf`, four pages. I read `PROMPT.md`, its scope addendum, `CRITIC.md`, repository `AGENTS.md` and `README.md`, the LaTeX, reflected-window generator and mathematical checker. Fresh 105-dpi renders of every page are in `critic-render/`; all were visually inspected. Draft SHA-256: `19d89ad17938fa693231bb251374a43efaa4a8335836c4a243267ef9479bf4fd`. The draft and its sources were not edited.

## Revision priorities

### 1. Page 3: preserve a usable way to make and check a secret shot

The shared rules use reflected copies to check a bounce. Pages 1 and 2 supply them. Problem 3 then permits any candidate room and any checked shot of at least three bounces, but supplies only single-room outlines. The square can reuse Page 1, and the rhombus can reuse the ABA construction on Page 2. A new rhombus word or wide-rectangle shot requires constructing new reflected copies, or correctly handling the mirror at successive wall hits. That demand is appreciably higher than simply choosing a line in the earlier windows.

This is a **usability risk, not a claim that the task is impossible**: a small mirror is among the authorized materials, and Page 2 describes a mirror check. Make access to a viable checking route explicit and available to both partners. A minimal revision could permit reuse of the earlier checked shots, provide an appropriately labeled scratch/reflection sheet for new attempts, and place the rectangle window where children can use it during the game. Do not require each child to invent a rhombus unfolding before they can play. Keep the choice of word and the elimination reasoning with the children.

The adult guide should include a one-shot mirror rehearsal using the actual printed room sizes. The Page 3 square and rectangle are only about 3.2 cm high; they are legible, but precision with a ruler and mirror at this scale is untested. If a normal rehearsal repeatedly needs adult line construction, enlarge the working rooms or use separate larger reusable copies. Do not call this a proven age mismatch before that rehearsal.

### 2. Page 4: say how substantial the sample shots should be

“Draw three shots” does not specify a bounce length or require encountering both wall directions. Under the shared stop-when-you-want convention, three one-letter or axis-aligned shots satisfy the concrete part but barely test transfer to a wide rectangle. The final universal question remains deep, so this is not a mathematical failure; the example selection can nevertheless leave a poor bridge to it.

A short requirement such as three distinct words with at least three bounces, including a shot that meets both a horizontal and a vertical wall, would supply purposeful concrete evidence without prescribing the coordinate-stretch solution. Reusing words already found on Page 1 is also sufficient. Keep the general explanation late, and do not print a scaling recipe.

## Page-by-page findings

- **Page 1 / Problem 1:** The AD example is correct in both folded and unfolded views. It shows a start, the two intermediate wall crossings and the resulting word before the three-letter task. Corner hits are explicitly excluded. The alternating labels in the reflected square tiling are correct, and the start dot is inside the bold square. Six distinct words are feasible in this exact finite window; see the check below. Six lines from one point may become cluttered, so the adult should have spare copies or allow erasing after recording the word. This is a material-preparation note, not a demand for more student instructions.
- **Page 2 / Problem 2:** Both ABA windows are correct chains of reflected rooms. The square's first and third A edges are collinear; the rhombus chain allows a line crossing the specified open edges. The shaded start room, labels and 60-degree corner are consistent with the corresponding single rooms. The visible geometry supports a reason for rectangle impossibility rather than mere failed aiming. The single-room transfer and mirror check are meaningful use of the same successful shot, not gratuitous follow-ups. No solution ray is printed in the task window.
- **Page 3 / Problem 3:** Asking for rooms not yet ruled out, rather than demanding a unique guess, is an excellent logical distinction. The sentence rejecting failed search as evidence is an essential rule of this game. It prevents the main mathematical misconception. Three rows allow repeated play. The free-shot checking concern is detailed above. Do not replace the game with a memorized answer table.
- **Page 4 / Problem 4:** The square and rectangle tilings have corresponding labels and an exact horizontal scale factor of two. Their heights are unchanged, so the picture is suitable for the intended all-word comparison. There is enough writing room. Three experimental transfers cannot prove that every word transfers; the final explanation must supply a general mapping in both directions. That belongs in the adult key, with hints discretionary.

## Mathematical audit

The supplied checker passes the non-task AD example, a non-corner ABA rhombus trajectory and thirty twelve-bounce rectangle comparisons. The worked AD path hits `(3,0)` and `(4,1)` in the 4-by-4 square, with the correct reflected directions.

For the rhombus with vertices `(0,0),(4,0),(6,2√3),(2,2√3)`, the checker's start `(1,1/2)` and initial direction `(-1,-1)` hit A at `(1/2,0)`, B at `((√3−1)/4,(3−√3)/4)`, and A at `((√3+1)/2,0)`. All hits lie strictly inside their sides. The reflected windows use the same side conventions.

I independently enumerated exact rational crossings from the printed square start `(1,1)` through its displayed window `[-4,6]²`. Twenty distinct three-letter words were witnessed without a corner hit before the third crossing, comfortably exceeding the six requested. Examples include `ABC`, `ACA`, `ADC`, `BAD`, `BDB` and `CAB`. This is an existence check, not a claim that the sample enumerates every possible word.

The independent kernel report supplies the universal arguments: after bouncing at the rectangle's A side, a bounce at adjacent B cannot reverse the vertical direction, so ABA is impossible. A positive coordinate stretch between labeled rectangles preserves horizontal/vertical reflection rules, straightness, crossing order and corner avoidance; its inverse gives the converse transfer. It does not preserve every Euclidean angle between arbitrary directions, and no such assertion is needed. All rectangles therefore share the same word language under corresponding labels. No finite observation is represented as a general unique room identifier.

## Visual, scope and readiness checks

All four pages have consistent headers, footers, page numbers and consecutive problem numbers. Every reflection-window edge and room label is legible at print size; no clipped text, overlapping answer areas, missing glyphs or skewed regular geometry was found. Diagram captions name objects rather than adding decorative activity headings. The shared four-page Grades 4–5 output is the authorized scope; no younger-band packet or adult guide is required from this stage.

The source README appropriately identifies ruler use and matching reflected pictures as entry prerequisites and the final general explanation as readiness-dependent. The packet is unpiloted. The follow-on guide should distinguish ray experiments, impossibility arguments and language equivalence, and explicitly prepare the mirror/reflection materials needed for Page 3. A digital reflection calculation does not verify children's physical control of a small mirror.

## Independent exact-instance cross-check

Before closing this review I read the completed independent `draft-instance-review.md`. Its Week 71 result is PASS for all four problems. I verified that its PDF and student-source SHA-256 fingerprints match this reviewed draft (including `windows.tex`). Its findings agree with this review; the proposed revisions above concern task selection, conventions or physical usability rather than a failed mathematical instance.
