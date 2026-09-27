# AP2 maker QA

Status: **maker pass complete, 2026-09-26; ready for independent PDF-review closure.**

Current preview: `tmp/pdfs/atlas-remaining/ap2-preview-v3/`.

- Student: `atlas-ap2-student-worksheets.pdf`, 25 pages including contents; SHA-256 `0fb53e2b26089b81cc077ab06e7d76966a255cea4a7fde5a91d0818a102cd546`.
- Facilitator: `atlas-ap2-facilitator-guide.pdf`, 44 pages including contents; SHA-256 `e01589b13ea076557a67b5b63c0664ca6876f794827ccb5db70943aa283d12fa`.
- AP-11–AP-18: exactly eight investigations, 24 student body pages, 48 tracked prompts, all eight fully answered extensions.

## Coverage

I inspected all student pages 1–25 at full size from v1, all guide pages 1–44 on five contact sheets, and dense mathematics/figures on guide pages 5,8,9,10,15,16,20,21,24,25,26,27,29,30,31,32,33,35,36,37,38,39,41,42,43,44 at full size. The three additional changed guide pages 11,19,23 were inspected full size from fresh v3. This includes every worked figure and the sensitive inverse-design, entropy, quantum-update, conditional-sampling, boosted-event and bounded-error calculations.

After repairs I reopened **every changed student page** 3,4,6,8,11,12,13,14,19,22,24 and **every changed guide page** 11,19,23 under the new v3 path. PNG byte comparison against v1 confirmed exactly these 14 changed pages; the other 55 pages are byte-identical. Page counts and contents destinations did not change. No existing path was overwritten for repair review.

## Repairs made during visual review

- AP-11: separated the branch-plot caption from tick labels and redrew the tank outline after its fill, so the full tank has a visible base.
- AP-12: added arcs and unambiguous labels inside the two normal-angle sectors; marked the generic picture schematic. The worked crossing label now has a clear callout and leader away from both route lines and the boundary.
- AP-13: moved the horizontal-axis symbol away from the `2π` tick. The periodic phase scope already passed design review.
- AP-14: centered each heat label over its own arrow, keeping `Qc` clear of the cold reservoir box. Prompt 1 now says “Label” the supplied transfer arrows. The exact repeated guide prompt was updated with it.
- AP-15: explicitly printed `e1=(0,1)` alongside the other supplied state definitions. The design had this coordinate but the first render lacked its planned card. Guide preparation now accurately calls these printed definitions, not cutout cards. The extra introductory line leaves the probability trees usable.
- AP-16: put site numbers outside the ring's empty spin circles, leaving actual writing room for `+`/`−`. Kept all four physical links and did not disclose the parity condition or weighted totals on the exploratory page.
- AP-17: allocated more space for the metric-invariance argument without changing equal plot units or the legal coordinate window.
- AP-18: compacted the three common-scale mass axes and provided a genuine proof area below them for necessity and sufficiency.

The editor independently caught the same angle/heat-label concerns and requested the “Label” wording and crossing callout; all were included. The independent design reviewer was notified of the two supplied-object wording/definition repairs, which change no example or answer.

## Mathematical and mechanical checks

`ap2-checks.py` passes after the final data edits. The complete proofs were separately reviewed in `review-ap2-design.md`; that review includes an independently implemented checker. This maker pass rechecked actual plotted coordinates, equal units, proper-time versus Euclidean length, transfer directions, labels distinguishing measured and inferred quantities, and the exact locations of supplied and withheld information.

The v3 builder reports 25/44 pages, zero blank pages, zero out-of-page text characters and zero suspect glyphs. It also confirms the exact family set and once-only printing of all 48 prompt IDs. All 69 pages rendered at 100 dpi. Student body text remains 11.5 points; guide body remains 11 points. There is no shrink-to-fit substitution for the longer proofs.

Contents gates disclose calculus for AP-12, trigonometry for wave retrieval, vectors/probability for quantum measurement, and the supplied physical models. Two- or three-page investigations can be staged across meetings. No timing or learner engagement claim is classroom-tested.

## Candid first-pilot fit

AP-16 is the strongest concrete first-pilot candidate: freely chosen spin arrangements lead to a class-weight surprise, a bijection, an exact sampler, and a ring obstruction. AP-11 and AP-18 have similarly useful choices and nonuniqueness/extra-information payoffs once their model rules are understood. AP-12 retains its calculus gate and gives a full optimum/inverse-design arc. AP-14 and AP-15 require the most facilitator preparation: the supplied entropy and projection-update laws must be understood as hypotheses, and the activity should not be reduced to unaudited arithmetic with the formulas. They are serious advanced investigations, not elementary stand-ins.

Independent PDF closure and final assembly belong to the editor. This note does not claim a classroom pilot or a new visual pass over the later assembled combined books.
