# Week 77 revision record

Reviser stage only, 2026-10-07. Checkout: `frontier-stages/week-77-reviser`, branch `dot/week-77-reviser`; origin verified as `https://github.com/jamesrp/math-circle-worksheets.git`. The coordinator's published claim was in place. Read the local project instructions, complete author prompt and scope addendum, both reviews, and the PDF skill. Copied `draft/src/` to `final/src/`; the draft is unchanged. No other stage, guide, delegation, commit, or push was performed.

## Review decisions

1. **Adopted the substantive pacing/depth concern.** Added an earned fifth page, Problem 6, using an exactly specified square with a center vertex and four triangular faces. Children choose two fixed, distinct, initially surviving loops with a shared guaranteed fate from a partly filled start, then seek the same pair with either strict death order from a fresh start with no fillings. The two contrasting situations concern equivalence created by already-filled boundaries, rather than merely increasing the number of schedules. The child chooses the loops and filling orders; the recording consists of two saved edge lists and two replayable face orders. There are no barcode tables, simultaneous count logs, or mandated full enumeration on the student page.
2. **Adopted the brevity finding.** Problem 2's paragraph no longer repeats all four scheduled actions. Its visible stage list remains, so children need not remember the schedule.
3. **Adopted the simultaneous-stage clarification.** The shared boundary rule now says edges must be in place when a triangle is filled, removing the possibly temporal word “first.” Problem 4 explicitly makes stage 4 one step: place the edge, then the tile, and check only when both are in place. This does not reveal either repair or create a separately recorded internal stage.
4. **Adopted the preparation finding.** The README now includes two XY, two YZ, and one XZ token for the exact printed demonstration. It also specifies the new board's four tiles, four radial-edge token labels, 8 cm dimensions, and a movable O label in case a tile hides the printed center label. The board remains unshaded so removing tiles for a new build genuinely returns it to the stated unfilled start.
5. **Retained the mathematical review's conclusions for Problems 1–5.** No correctness repair was necessary. Their precise saved-loop mechanism, partner check, non-task cancellation example, and general no-resurrection question remain.

No actionable review finding was rejected. I declined the alternative of leaving fast-finisher provision unresolved without adding a substantive construction. I did not pad Problems 2–4 with repeated schedules or add formal persistence notation. The new task is a design response, not evidence that the packet takes forty minutes: physical preparation, handling, and classroom pacing remain untested.

## New finite mathematics and exact witnesses

The new board has vertices A=(0,0), B=(8,0), C=(8,8), D=(0,8), and O=(4,4), in centimetres. Its eight edges are AB, BC, CD, AD, AO, BO, CO, DO. Its four nonoverlapping faces are ABO, BCO, CDO, ADO. All edges are present initially; only ABO and BCO are filled in the first build. The point where the diagonals meet is explicitly a vertex, O.

Writing a face name for its mod-2 boundary, the four eligible loop supports are:

- CDO + ADO
- ABO + CDO + ADO
- BCO + CDO + ADO
- ABO + BCO + CDO + ADO

Each is initially nonzero and stays nonzero after either one of CDO or ADO is filled; each becomes zero once both are filled. These are four different edge sets. Of their six unordered pairs, exactly one permits either strict death order when starting with no filled faces:

- L: AB, BO, CO, CD, AD, which is the boundary of ABO + CDO + ADO
- M: AO, BO, BC, CD, AD, which is the boundary of BCO + CDO + ADO

Both are simple closed loops: every used vertex has degree two. Their difference is the boundary of ABO + BCO. Thus, in the partly filled starting board, their difference already cancels, and both reduce to the nonzero boundary of CDO + ADO. This proves the universal first-part claim without assigning identities to visible cavities.

For the fresh board, filling CDO, ADO, ABO, BCO kills L at the third filling and M at the fourth. Filling CDO, ADO, BCO, ABO reverses that order. Among all 24 orders, six kill L first, six kill M first, and twelve tie. The other five pairs among the four eligible loops have nested face supports, so both strict orders cannot occur. Already-filled faces may be removed only when resetting to the separately requested new build, never within either growing build.

## Verification performed

- Extended and ran `final/src/check_math.py`. All original cycle, cancellation, schedule, inclusion-map rank, and simultaneous-stage checks pass.
- Added exhaustive edge-set cancellation checks for the new board: 16 cycle chains, 12 initially nonzero chains, four loops surviving either possible first remaining filling, all six candidate pairs, and all 24 filling orders per pair.
- Independently checked the new finite claims with a separate integer-bitmask model in the verifier. Its triangle boundary masks are explicitly specified over the eight listed edge positions. It enumerates graph cycles by vertex parity and tests every permitted subset of filled boundaries, without calling the earlier cycle/span/death routines. Both models agree on the four eligible loops, unique reversible pair, and 6/12/6 outcome counts.
- Added the four-face board to the finite nested-boundary-space check for Problem 5. The general explanation still rests on the same cancelling set remaining available, rather than claiming finite tests prove an unlimited theorem.
- Built the final PDF with the portable `build.py --out DIRECTORY` interface. The cloud-only runtime configuration was supplied externally: `TEXMF='{/usr/share/texmf,/usr/share/texlive/texmf-dist}'` and `TEXFORMATS=<run>/tex-runtime:.`. No runtime files were added to the portable source.
- Packaged the four source files into a temporary ZIP, extracted them to `revised-clean-rebuild/src/`, and rebuilt successfully. Extracted text and all five 110 dpi rendered PNGs are byte-identical to those of the final output. The builder uses only the Python standard library plus the documented TeX installation.
- Inspected every page of the final rebuilt PDF at 110 dpi, including the final wording change on page 5. No clipping, overlaps, missing glyphs, or malformed diagrams were found. Dashed and solid edges, token cancellations, center vertices, labels, headers, footers, and answer spaces are legible. The fifth-page board has equal x/y scaling and all eight edge segments.
- Both final and extracted-source builds have no TeX warning, overfull, underfull, or error notices. The final PDF has five US Letter pages and is 60,534 bytes, below the practical 200 KB target.
- The final source directory contains only `students.tex`, `build.py`, `check_math.py`, and `README.md`. No borrowed text, images, reference paper, workflow prompt, or generated environment file is packaged.

## Deliverable and limits

`final/students.pdf`: five pages, shared Grades 4–5 prototype. SHA-256: `e27735de07fee5b65d5f8ea1be06e260f4724a12ca039e10bd8b8d704a4d4787`.

There are no separate K–1 or Grades 2–3 editions under this run's scope. No adult guide was created. Matching paper tiles are prepared from extra copies; they are not a supplied cutout sheet. The README discloses untested physical fit, tile/edge handling, pacing, and children's command of the representation. Added digital checks and one deeper problem do not establish classroom readiness.
