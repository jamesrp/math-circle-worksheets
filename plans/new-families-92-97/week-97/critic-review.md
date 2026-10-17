# Week 97 adversarial review

## Scope and verdict

Reviewed the complete six-page `draft/students.pdf`, rendered every page at 1.3× with PyMuPDF, inspected all six images, and read `draft/src/students.tex` and the full writer/critic instructions. This is the accepted single Grades 3–5 packet; no younger-band packet or facilitator guide is required. No draft files were edited.

**Revise narrowly before acceptance.** The mathematics and problem sequence are sound, and the opening now passes the same-fixed-input operation audit. The remaining introduction-audit gap is the reading convention for grouped input collections. Also make the removal stopping rule explicit in the shared rules. Retain the six substantial investigations and their upper-level depth.

## Required revisions

### R1 — Demonstrate the collection-reading convention before comparing collections (pages 1–3; introduction-audit requirement)

The worked visual establishes only one forward calculation: input 3 → nine counters → two complete bundles of 4 plus one counter → output 1. Problem 1 then asks for pairs of inputs with one output; Problem 2 asks for every input hidden by an output and for largest/smallest collections; Problem 3 compares those collections across bundle sizes. Problem 6 eventually counts different outputs, which is a different count from the number of inputs producing an output.

There is no example of reading one output as a collection of possible inputs, or distinguishing “how many inputs?” from “how many different outputs?”. A child may follow the physical operation perfectly and still interpret a larger output number as hiding more inputs. This is a representation transition, not a missing mathematical hint. It falls under the explicit run-specific instruction to demonstrate the necessary whole-collection reading convention before variations.

Add a compact non-task example before its first use, keeping the existing complete input-3/bundle-4 operation intact. One suitable scope is a small explicitly bounded collection of inputs for bundle size 4, with their outputs and one grouped reading shown. Make clear which numbers are input labels, which are output labels, and what a collection's size means. Do not supply the mod-5/mod-7 task inventory, prescribe opposite pairing, or turn the investigation into a required table-filling algorithm. A brief worked convention is enough; children should still choose how to organize their own investigation.

### R2 — State when removing bundles stops (page 1 shared rules)

“Remove complete bundles of the given size. The number left is the output” omits “all” or an equivalent stopping condition. The diagram correctly removes both available bundles, but the general words would also allow stopping early. Unique remainder outputs underlie every task.

Use a concise shared rule such as “Remove complete bundles until fewer than one bundle's worth of counters remain.” Keep it once at the opening; do not repeat it in every problem. The essential mathematical requirement is output in `0,…,m−1` after every complete bundle has been removed.

## Mathematical verification

I independently enumerated `x*x % m` for every specified input, with these results. Braces below contain input labels, not output counts.

| Bundle size | Output → all possible inputs | Number of outputs |
|---|---|---:|
| 3 | 0 → {0}; 1 → {1,2} | 2 |
| 5 | 0 → {0}; 1 → {1,4}; 4 → {2,3} | 3 |
| 7 | 0 → {0}; 1 → {1,6}; 2 → {3,4}; 4 → {2,5} | 4 |
| 8 | 0 → {0,4}; 1 → {1,3,5,7}; 4 → {2,6} | 3 |
| 9 | 0 → {0,3,6}; 1 → {1,8}; 4 → {2,7}; 7 → {4,5} | 4 |
| 11 | 0 → {0}; 1 → {1,10}; 3 → {5,6}; 4 → {2,9}; 5 → {4,7}; 9 → {3,8} | 6 |
| 15 | 0 → {0}; 1 → {1,4,11,14}; 4 → {2,7,8,13}; 6 → {6,9}; 9 → {3,12}; 10 → {5,10} | 6 |

- Problem 1: the two different-input pairs are {1,4} and {2,3}; outputs 2 and 3 cannot occur. Input 0 and output 0 are included.
- Problem 2: outputs 1, 2, 4 each hide two possible inputs; output 0 hides one. “Among outputs that occur” correctly prevents absent outputs from being counted as the minimum.
- Problem 3: mod 7 maxima are outputs 1, 2, 4 with two inputs each; mod 8 maximum is output 1 with four inputs; mod 9 maximum is output 0 with three inputs. Thus bundle size 8 hides the most possibilities among those compared. Zero hides multiple inputs for both 8 and 9.
- Problem 4: output 1 has inputs 1, 4, 11, 14; no output hides more than four. Output 4 ties it. The 0–14 domain is finite and appropriate.
- Problem 5: for `n=7q+r`, `n²−r²=7q(7q+2r)`, so the remainder agrees with the square of an input 0–6. A geometric explanation can remove seven-wide strips from a large square. Testing the printed examples suggests this fact but does not prove the universal claim; the prompt explicitly asks for an explanation covering arbitrarily large squares.
- Problem 6: for odd prime `p`, equal square remainders imply `p` divides `(x−y)(x+y)`; primality gives `x=y` or `x+y=p` within the stated domain. Zero is alone and nonzero inputs pair, giving `(p+1)/2` distinct outputs. The qualifier “odd” excludes the exceptional pairing behavior at 2. The composite counts 3, 4, 6 for 8, 9, 15 do not satisfy that formula; finite tables alone do not justify the prime theorem. The worksheet asks for, rather than asserts, generalization and explanation. No false universal two-root rule is printed.
- All printed square facts through `15×15=225` are correct. The optional multiplicative square/nonsquare extension from the outline is not included; its omission is permitted.

## Page-by-page evaluation

| Page | Finding |
|---|---|
| 1 | Complete worked operation uses the same fixed input 3 and bundle size 4 in all panels. Left panel has nine dots in a 3×3 array; middle has two boxes of four plus one dot; right has one dot. Labels and arrows match. This is a non-task instance. Five starting arrays include explicit zero and leave substantial work: two collisions and two missing outputs. The new collection-reading example should remain compact enough to preserve working space. |
| 2 | Partner secrecy gives the inverse problem a concrete purpose, and the global max/min question adds mathematical substance beyond isolated guesses. Squares require at most 36 counters. Keep the partner game; do not replace it with a completed catalog. |
| 3 | Purposeful contrast between prime 7, composite 8, and prime-square 9. The bounded domains avoid ambiguity about infinite input classes. At most 64 counters per individual square matches the supplied material limit. Three investigations plus comparison are substantial and can take more than one work period. |
| 4 | Mod 15 shows four-input collisions for a different composite structure. Square products are supplied, so no one must build 196 counters. Finding all candidates and testing whether another output has more is a substantial finite classification. |
| 5 | Universal explanation is a legitimate deep continuation; testing examples is explicitly distinguished from settling every input. This is more demanding than the concrete entry, but it should remain as a readiness-dependent return visit. |
| 6 | Conjecture and prime explanation connect the earlier catalogs; zero is expressly counted. Primes are defined in ordinary language and the composite check limits the rule. The proof can require adult mathematical conversation, but its presence is warranted by the accepted scope. |

## Independence, materials, and age fit

The first two pages support doing and checking with counters. Page 1 uses at most 16 counters per square and page 2 at most 36. Page 3 reaches the 64-counter limit only for input 8. The word “build” appears only at the concrete opening; later large-square tasks provide multiplication values rather than demand impossible materials. The blank areas give ample room for sketches, grouping records, and children's chosen organization.

Prerequisites increase sensibly: recognizing square arrays and making equal bundles at entry; comparing several finite collections on pages 2–4; eventually divisibility and universal argument on pages 5–6. Reading a problem aloud is ordinary support; it need not mean adults operate the investigation. The shared three-person upper group will need a role rotation in live facilitation, but no printed role-management instructions are required here.

**Unpiloted concerns, not blockers:** computing remainders of 169 and 196 with bundles of 15 may still consume substantial arithmetic effort despite supplied square products; repeated multiplication support fills space but is useful. Observe whether children can use repeated addition/subtraction or drawings without adult operation of the entire investigation. A supplied multiples strip could be considered if actual experience shows a bottleneck. Do not preemptively remove mod 15 or add a prescribed method. No requirement says all six pages must fit one hour.

The packet leaves organizational and proof choices open. The maxima/comparison questions are mathematically connected, not disconnected small subparts. No generic encouragement, Name/Date fields, extra section titles, or obligatory explanation after every small action is present. Essential explanations occur where universal claims are the problem itself.

## Visual and technical audit

All six rendered pages were inspected. US Letter, one numbered problem per page, continuous Problems 1–6, consistent Week 97 / Square remainders / Grades 3–5 headers, packet footers, and page numbers are present. Text extraction additionally confirms header/footer strings on all six pages. No clipped text, overlapping panels, missing characters, or accidental blank pages were found. Array dots and arithmetic cards are legible. The square arrays use equal x/y scaling. Blank working areas are generous and stay inside the page margins.

The source contains `\pdfinfoomitdate=1` and `\pdftrailerid{}` as requested. This review did not run an independent portable rebuild or inspect a source ZIP; those are revision/integration verification work, not evidence established here. The source and PDF agree on the six tasks and printed arithmetic support. The physical activity has not been rehearsed with children; all operational age-fit comments remain hypotheses rather than classroom findings.
