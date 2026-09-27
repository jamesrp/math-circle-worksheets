# Independent PDF review: GA-11, AP-26 and AP-07

September 25, 2026. Reviewer: decision/probability author, reviewing the systems author's PDFs read-only. Preview root: `tmp/pdfs/atlas-random-ten/systems-preview/`. This follows the independent mathematical/design review in `decisions-review-of-systems.md`.

**Result: pass, no open findings.** Student preview has 12 pages including its cover (11 investigation pages); guide has 19 pages including its cover. All 32 guide solutions match `systems-data.json` after normalizing whitespace and the renderer's dash convention. Reports show no blank pages, out-of-page characters or suspect glyphs. This is a checked printable prototype, not classroom evidence.

## Pages visually inspected

- **Every student investigation page at full size:** PDF pp. 2–4, GA-11; pp. 5–8, AP-26; pp. 9–12, AP-07.
- **Every guide page through the three contact sheets:** PDF pp. 1–19. Additionally inspected guide pp. 10 and 18 at full size to check dense algebra, signs, subscripts/powers represented in plain text, the all-start period proof and the unequal-schedule accuracy bound.
- Confirmed the student cover/contents and per-family page ranges against the build manifest.

## Content and figure checks

**GA-11, student pp. 2–4.** The four claim cards are correct and do not preprint their verdicts. Their paired routes leave room for actual certificates. The rational proof asks for signed and zero cases. The expansion to exactly `a+b√2` is explicit, and the formula remains blank until the learner builds the two machines. The domain is not silently all real numbers. Optional continuity wording distinguishes one close numerical pair from arbitrary rational approximation. All relevant glyphs are legible; the general addition proof has its own substantial space.

**AP-26, student pp. 5–8.** The simultaneous two-card update is unambiguous. The initial current-state sequence is blank beyond its supplied starting value. The pair-state graph is blank, so the learner discovers the cycle. The algebra slots and exact-period question preserve the zero exception and require explanation of shorter periods. The triangular grid points OLD right and CURRENT up-left with equal unit lengths; no orbit is preplotted, and the origin is clear. Its embedding supports the intended regular hexagons. The half-gain page is visibly optional and has space for the arbitrary-pair calculation, all-residue convergence explanation, and a permanent tolerance certificate.

The first displayed image of AP-26 p. 7 appeared to have a shallow D8 panel. After coordination with the author, I inspected a uniquely named copy of the current PNG (`ap26-d8-review-current.png`): the panel is **102 pt high**, with ample space below all three case labels. The apparent workspace finding is closed; no additional author edit was needed.

**AP-07, student pp. 9–12.** The calculus prerequisite is prominent. The exact cooling graph has the required time range through 3 and vertical range down to −16, so every requested tangent endpoint fits. Tangents and chosen endpoints remain blank; the exact curve is the intentionally supplied comparison. Relative temperature and actual elapsed time are clearly labeled. The classification table leaves parameter intervals blank, including boundary cases. Two-update optimization has a large proof area and does not print the optimal half-step split. The accuracy-budget title and C11 wording now withhold the six-update minimum. Unequal durations are allowed, the product-maximization theorem is openly supplied, and the backward-Euler repair remains an optional separate question.

**Guide.** Every student prompt has a corresponding solution and separately labeled delayed hints. Positive-rate and domain restrictions, equilibrium terminology, full-state memory, zero exceptions and numerical accuracy distinctions survive rendering. The sources and prior-use distinctions are included; no unsupported claim of a classroom pilot appears. Text is readable, with no clipped lines or crowded figures. A few short source/continuation pages are acceptable; they are not blank or misleading.

## Evidence and limits

The mathematical review independently solved all 32 prompts before this PDF check. In this pass, normalized extraction confirms every full keyed solution is present, rather than merely searching for labels. The rendered checks supplement that verification: they do not substitute for either mathematics or image inspection.

Manifest hashes at review:

- Student PDF: `eac1adcec5688a106025178e2f556f9089752df5a9422c609e360524df3e9a30`.
- Guide PDF: `a1bb03825157d672abd2686ba9e55551fe95960c42f376df1bae849b16909a2b`.

Final combined-book pagination will differ. The root should rerender/check the assembled outputs and retain the same module content. Student engagement, prerequisite fit for particular children, and actual timing remain untested.
