# Independent AD2 PDF review

Reviewer: expand_ga1. Date: September 26, 2026. **Closed: approved for assembly from `tmp/pdfs/atlas-remaining/ad2-preview-r5/`.** One custom guide-caption finding was repaired and reinspected. No open findings remain. This is a PDF review, separate from the independently closed design review. The activities are unpiloted.

## Preview identity and actual coverage

- Student PDF: 26 pages, contents plus 25 bodies. SHA-256 `ee798c22c0197a5c1d85ecc63b876ccb9d0361bfe262ea7c1994087b507b28f9`.
- Guide PDF: 36 pages including contents. SHA-256 `193aa2d05a07b213b95df368378d32166df13be3f81affee1cc24eae3b47906a`.

I read `ad2-maker-qa.md`, the current data's prompts, keys and extensions, and inspected **every student page 1–26 individually at full size in r4**. I inspected **every guide page 1–36 on all four r4 contact sheets**. Full-size guide inspection covered pages **1,4,5,7,8,9,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,29,30,31,33,34,35,36**. This includes all dense algebra, optional extension arguments and the worked staircase diagrams.

After the repair I independently opened guide page 22 at full size under the fresh r5 path. I compared every PNG byte-for-byte between r4 and r5: all 26 student PNGs and all other 35 guide PNGs are unchanged. These identity checks connect the full inspection to the current preview; I do not claim an additional full pass of unchanged pages or the future assembled books.

## Findings and closure

**AD-13 / guide page 22, custom worked-figure caption.** The sentence “Distinct surviving monomials have distinct nonzero images under either coordinate multiplication” was too broad: for example y³ survives in the quotient but both its coordinate products are zero. The main key already made the correct distinction. I requested that distinctness be restricted to images that survive. The author changed the caption to “Among monomials whose shifted images survive, those images are distinct. Thus cancellation cannot add other joint-kernel elements.” This is correct, reads cleanly and preserves the full argument. Closed on the fresh r5 page. No mathematical data or student task changed.

## Family fidelity and use

- **AD-09:** Four- and six-clock labels, ordered report coordinates and the 4×6 record agree. Repair ledgers are open and do not reveal the number of successful repairs. The printed key gives first times 5,11,10,6; the gcd/Bézout construction includes existence, period uniqueness and nonnegative reduction.
- **AD-10:** Counter workspaces allow real arrangement choices, then the forward/reverse machines are supplied at their intended stages. The printed recurrence preserves x²−2y²; the inequalities 4y/3<x<3y/2 establish positive descent for y>2. The first-over-million and next totals match the recurrence. The source/guide distinguish production of examples from completeness.
- **AD-11:** Four coefficient cards correctly encode 0,1,t,u. Both product tables are blank and separately labeled by their actual reduction rule. Inverse, collision, field and two-report decoding arguments are consistent, including equal-output constant machines and the rule-A no-solution example. No row count leaks an unknown answer inventory.
- **AD-12:** The copyable unit segment and semicircle with diameter split 1:√2 are geometrically faithful. The unknown height is an offered square-root construction, not a false cube-root construction. The necessary degree theorem is visibly supplied, irreducibility is explicitly required, and positive integer volume scope is stated. The printed rational brackets, fourth-root construction and 20° obstruction agree with their algebra.
- **AD-13:** Corners are correctly located and axes continue beyond the page. Original student diagrams reveal no survivor set. I independently read the eight-move classification and checked the guide's original eight versus repaired ten survivors. Both added points (2,1),(2,2) and common-kernel points (0,3),(1,2),(2,0) match the exact coordinates. Spanning and independence are explained, with no total-degree cutoff substituted for ideal membership.
- **AD-14:** Every dependency in the program flow is present, including separate z² and z²+1 boxes. Ordinary and ε columns are blank, arrows follow the operations, and the output 16 is withheld until its proper later task. The guide evaluates 3+bε as 10+16bε and gives exact polynomial product/chain rules, not an argument based on a small real ε. The second-order extension's 8+12ε+42ε² agrees with direct expansion.
- **AD-15:** Both ellipse figures have equal axis units and vertical semiaxis 1/√2. Only the basepoint is marked; the learner supplies secants and second intersections. All printed point examples, inverse slope, omitted point, homogeneous triples and gcd cases agree. The cubic counterexample correctly limits the line-through-point strategy instead of claiming a general nonparametrization theorem.
- **AD-16:** The residue grids have exactly the labels 0–4 and no misleading smooth curve. The finite inventory, single projective point O, discriminant 4, generator orbit and congruence-equation keys agree with the formulas. The group theorem is explicitly supplied before cyclic-law conclusions. The orbit record is open, and the final four answer areas correspond to four explicitly requested equations rather than a hidden solution count.

The student pages provide generous working room, staging and actual prerequisite gates. Sources and solved examples remain in the guide. Contents entries and starts match the body families: student 2,5,8,11,14,17,20,23; guide 2,6,10,14,19,24,28,32. The advanced algebra/calculus sections are not marketed as completed by the entry manipulatives.

## Mechanical support and scope

I independently compared all 49 rendered prompt records with the current JSON: exact text matches, each family/prompt pair appears exactly once. Both current build reports have no blank pages, out-of-page characters or suspect glyphs; all 62 pages render. I independently calculated or followed the printed identities above while checking mathematical fidelity, rather than treating a clean report as mathematical proof.

This review did not mutate the author's data, renderer or previews. The author made the caption repair. Classroom preparation, engagement and timing remain untested. The editor still owns final assembly, contents/link checks and proof that final page bodies match these reviewed previews.
