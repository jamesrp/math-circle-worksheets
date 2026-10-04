# Independent review of the Week 18 draft

## Verdict

**Small, targeted revisions recommended.** The packet is mathematically sound, visually clean, and substantially faithful to the organizer's register. I found no false mathematical premise, impossible task mistakenly presented as possible, clipping, overlap, or counter-size failure. The principal weaknesses are the depth of two K–1 problems and the mismatch between an exhaustive search and the recording space supplied in grades 2–3. These do not call for a replacement packet.

I read `PROMPT.md`, independently rendered all three delivered PDFs at 100 dpi, and inspected every one of their 18 pages. Each PDF has six US Letter pages. I also read `draft/src/build_packets.py`, checked relevant generated source, independently enumerated the finite cases, checked the compilation warnings, and verified font embedding. I did not edit the draft or run its authoring script.

## Findings to address

### 1. Two K–1 problems are too slight as separately numbered investigations

**Location:** K–1 p. 2, Problem 2; p. 5, Problem 6. Source: `build_packets.py`, lines 71–74 and 88–90.

The standard requires every numbered problem to offer at least five minutes of real experimenting and thinking without another instruction. These two are unlikely to meet that requirement for a quick child in the stated sequence:

- **Problem 2** supplies the same repetition key that Problem 1 has just explored. Once a child has found that the more numerous counter face identifies the picture, all eight cases are routine classifications. The cases correctly include the two unchanged rows and all six one-change rows, but there is no new choice, ambiguity, or search. Eight recordings are not necessarily eight mathematical decisions.
- **Problem 6** asks for only one mixed four-counter key. Immediately after finding three-counter keys, a child can make a complementary mixed pair such as `0011 / 1100` and finish. “Can you make it always work?” does not require additional contrasting cases or another substantial mathematical product. The second printed pair of blank rows does not itself assign another task.

**Revision direction:** Consolidate the short decoding task with the contrasting two-counter ambiguity task, or give it a genuinely different mathematical decision. Make the four-counter task require a substantive family of cases or a new constraint that cannot be disposed of by one immediate complementary pair. Preserve the short oral wording; do not solve the problem by adding hints, a prescribed testing procedure, or a routine “explain your thinking.”

This is a per-problem depth issue, **not** a claim that the whole K–1 packet is too short. Problems 4, 5, and 7 provide real impossibility and enumeration work, and the six-page packet could readily occupy the group for forty minutes with discussion.

### 2. The grades 2–3 exhaustive search has fewer recording positions than answers

**Location:** Grades 2–3 p. 4, Problem 4. Source: `build_packets.py`, lines 115–117.

The task explicitly asks for **every** working key and says swapping the pictures counts as different. There are six such keys, but the page contains only four pairs of blank strips. A child who successfully completes the search cannot record it all in the provided strip diagrams. This is especially awkward because the page's four repeated pairs visually suggest a four-answer task.

The six ordered solutions, written here only to substantiate the review, are:

- `0011 / 1100`
- `0101 / 1010`
- `0110 / 1001`
- `1001 / 0110`
- `1010 / 0101`
- `1100 / 0011`

**Revision direction:** Provide open overflow space or a reusable continuation sheet and make the continuation route clear. Keep the counter cells at least 2 cm. Do not cure the shortage by shrinking the cells or by creating an exact-answer-count template that gives away the enumeration. The brief already supplies blank paper, so this is readily fixable and is not a session-level materials blocker.

### 3. The corresponding K–1 search needs a clear convention and practical overflow

**Location:** K–1 p. 4, Problem 5. Source: `build_packets.py`, lines 84–86.

There are eight ordered three-counter keys, but six printed pairs. If exchanging the triangle and square counts as a new key, a complete search overflows the page. If it does not, there are four complementary pairs, so the meaning of “different” changes the result. Unlike grades 2–3 Problem 4, this task does not state the convention.

This is lower severity than finding 2: “Find every key you can” does not unambiguously demand a completed exhaustive list, and extra blank paper is available. Nevertheless, it is a foreseeable source of an adult having to supply an additional instruction. It matters because the organizer explicitly wants the task, objects, and recording to be self-contained.

**Revision direction:** Settle what counts as a different key in concise child-facing language or in the task's construction, and allow the search to continue without treating the six printed pairs as its endpoint. Avoid adding an answer-sized set of eight bins.

## Lower-priority usability and sequencing observations

- **K–1 pp. 2–3, Problems 2–3:** “Put its picture” / “Put every possible picture” can mean place a physical message card. The materials provide one of each of four distinct picture cards, not enough copies to leave all answers in place. If the intent is a written record on the short answer lines, “draw” is the unambiguous verb. Sequential card placement is also possible, so this is a wording ambiguity rather than a mathematical defect.
- **Grades 2–3 p. 5 and grades 4–5 p. 2:** Inventing four length-five words is a substantial jump from two-message examples. It is a valid investigation, and the instruction not to give methods should be respected. In an unpiloted session, watch for a group committing to `00000` and `11111`: no third word can be at distance at least three from both, so that natural starting pair is a dead end. This is a pacing risk, not a reason to print a construction or a hint. If revision changes the order, do so through contrasting tasks rather than adult commentary on the page.
- **Grades 4–5 p. 5:** The shortest-length problem deliberately leaves the child to connect neighborhood sizes with the size of the whole binary universe. That is legitimate mathematical work. Do not “fix” the open space by supplying twenty bins, the `20 > 16` comparison, or the counting proof. The page has adequate room to enumerate sixteen strips and explain the obstruction.
- **Grades 4–5 p. 6:** This is a good final investigation, but it requires a different obstruction: three neighborhoods of size five would occupy fifteen of sixteen strips, so the previous counting bound alone cannot rule it out. The task is correctly phrased as “find one, or explain why every choice fails.” Keep that distinction intact in any revision.

## Page-by-page audit

| Packet/page | Mathematical and task audit | Visual/production audit |
| --- | --- | --- |
| K–1 / 1 | Repetition key `000 / 111` is reliable. Hidden zero-or-one-change play is preserved. | Clear key and six unlabelled working strips; left-end markers and 2.05 cm cells. No collision between rules and problem. |
| K–1 / 2 | All eight length-three received rows occur once and decode uniquely. Depth concern in finding 1. | All rows and answer lines fit; message symbols are distinct. |
| K–1 / 3 | `00` and `11` decode uniquely; `01` and `10` admit both pictures. No reliable two-counter key exists. | The two problems are clearly separated. Four received rows include unchanged possibilities. |
| K–1 / 4 | Reliable keys are exactly complementary length-three pairs. Convention/overflow concern in finding 3. | Six blank keys fit, including the bottom pair; footer remains clear. |
| K–1 / 5 | Mixed four-counter keys exist. Depth concern in finding 1. | Both construction areas are large and usable; no overlap. |
| K–1 / 6 | Three pictures cannot be reliably encoded in length three. This is genuine age-scaled impossibility work. | Two complete candidate keys and ample open space; new star symbol is visually clear. |
| Grades 2–3 / 1 | First key works; second key's words differ in one position and are ambiguous even when one is received unchanged. | Two keys are clearly separated; working cells are 2 cm. |
| Grades 2–3 / 2 | The four cases have distances 1, 2, 3, and 4: the first two fail and the latter two work. Strong contrasting cases. | All four keys fit with intervening recording space; no right-edge clipping. |
| Grades 2–3 / 3 | Exact minimum for two messages is three. Cases of lengths 1–3 are supplied. | Clearly paired rows and useful workspace. |
| Grades 2–3 / 4 | Exactly six ordered solutions. Recording shortage in finding 2. | Four attractive, full-size recording pairs, but not enough to hold the full result. |
| Grades 2–3 / 5 | Four messages at length five are possible; explaining the guarantee is substantive. | All four rows are five cells of 2 cm; remaining page is open for testing/explanation. |
| Grades 2–3 / 6 | Rule explicitly changes to at most two flipped counters. Minimum length for two messages is five. | Open lines accommodate a chosen length and spare attempt without revealing the answer through cell count. |
| Grades 4–5 / 1 | Distances 2, 3, and 2 give two failing keys and one working key. Listing includes the no-change possibilities under the global rule. | Binary numbers are legible, with generous space for lists. |
| Grades 4–5 / 2 | Valid four-message construction problem. No solution is given away. | Four rows and substantial working space. |
| Grades 4–5 / 3 | Displayed pairs have distances 2 and 3. Required general threshold is three. | Six positions align correctly in both pairs; plentiful argument space. |
| Grades 4–5 / 4 | Neighborhood sizes are 4, 5, 6, and 11 for the requested lengths. | No answer-sized bins; room for lists and the completeness explanation. |
| Grades 4–5 / 5 | Exact shortest length is five; both construction and exclusion of all shorter lengths are requested. | Full open workspace. Nothing supplies the counting proof visually. |
| Grades 4–5 / 6 | No three-word, length-four, one-error-correcting code exists. | Three clear four-cell rows and adequate space for a structural argument. |

## Independent mathematical verification

I computed the received sets directly from all binary strings within the allowed number of changes, separately from the draft's saved JSON checks.

- For grades 2–3 Problem 2, the intersections of the two received sets are respectively `{0000, 0001}`, `{0100, 0111}`, empty, and empty.
- For grades 4–5 Problem 1, the ambiguous received rows are `{01, 10}` for the first key and `{0000, 0110}` for the third. The middle key has no ambiguity.
- For grades 4–5 Problem 3, the first pair shares `{010000, 100000}`; the second pair shares no received row.
- A valid length-five four-message example is `{01001, 01110, 10000, 10111}`. Its six pairwise distances are `3, 3, 4, 4, 3, 3`, and its neighborhoods contain 24 distinct received rows.
- Length four cannot accommodate four disjoint neighborhoods of five received rows: twenty distinct rows would be required, but there are only sixteen. Padding a hypothetical shorter code with fixed entries rules out all shorter lengths too. This validates the requested exact minimum; the worksheet does not falsely claim that fitting the count guarantees existence.
- No three length-four binary words have all pairwise distances at least three. An elementary independent reason is that each coordinate contributes either zero or two to the sum of the three pairwise distances, so four coordinates give a sum at most eight, whereas three distances of at least three require a sum at least nine. Thus the last grades 4–5 task is genuinely impossible even though the neighborhood count permits fifteen out of sixteen.
- The two-change variant needs pairwise distance at least five; two words of length at most four cannot meet that, and `00000 / 11111` does. This confirms the grades 2–3 final task.

## Standards and production that pass

- Six pages per band satisfy the requested amount of material; later tasks provide meaningful stretch. The K–1 packet is not merely arithmetic or a token shorter version of the older work.
- Every page uses the required one-line week/topic/level header, a valid one-line Bellingham footer with packet ID, and its page number.
- Only the header and `Problem N:` labels serve as headings. There are no mascots, manufactured excitement, praise, solution boxes, activity commentary, lettered substeps, or decorative titles.
- All K–1 problem statements are one or two sentences. The longer global protocol is separate and can be supplied orally as the brief permits.
- The receiver's original message and original strip are hidden; the final strip is the information transmitted. The rule allows no change. All illustrated operative strips have a left-end mark, and rows are not distinguished by color alone.
- K–1 cells are 2.05 cm; grades 2–3 cells are 2 cm. The grades 4–5 pages explicitly use written binary notation, so their smaller cells are appropriate.
- No page has clipped text, overlapping diagrams, an obscured footer, or unreadable symbols. All PDF fonts are embedded. The logs' `pdftex.map` warning has not resulted in a visible or embedding failure in the delivered PDFs.
- The source and diagram choices preserve the distinction between error correction and mere detection. The draft does not decode outside the promise, replace hidden errors with visible erasures, or assert a general maximum-code theorem from the counting bound.

**Bottom line:** Keep the mathematical content and the restrained page design. Address the two short K–1 tasks and the exhaustive-search recording/convention issues before treating the draft as fully compliant with the organizer's standard.
