# Week 33 final independent mathematical audit

**Pass.** Audited actual `final/bonus.pdf` (five pages), every rendered page, and actual `final/src/bonus.tex`. All seven tasks, all supplied necklaces/cards, and the wraparound example are valid. No correction remains.

The final P1 now says “ring labels,” correctly naming the objects grouped. The window rules now require a fresh complete deck for each test, removal of one available card at every start, and failure if that card is already gone. This exactly enforces unique window coverage. Independent simulation accepts all four fixed-position pair-ring solutions and all sixteen triple-ring solutions, and rejects AAABBBAA when AAA repeats. Printed code sets remain complete. The added two P7 recording rings each have eight equally spaced spots, equal scaling and no overlap.

The full computations remain: turn groups {a,c},{b},{d,f},{e}; flip groups {a,b,c},{d,e,f}; six proper named-three-kind five-ring classes; one shortest pair-window class AABB; two shortest triple-window classes AAABABBB and AAABBBAB that exchange under reflection. Clockwise indices 4→0→1 in the example correctly produce BAB.

`independent-check.py` uses only final source/PDF paths, recomputes all word/orbit/window enumerations and geometry, checks actual PDF task numbers and final deck rules, and binds the inspected source by hash. No draft is required. Final source SHA-256: `f64b946a50b22c9f746045aee4daeb966b03449c506b638b2818e20972373eb8`. Final PDF SHA-256: `2ff16dccb1db5ff2b63b9bd56dd5c62a51fd4a88f13e622216d7da1d55838a91`.

Physical card/counter fit, overlay/viewer use, and classroom pacing remain untested. This is a mathematical audit, not a classroom-pilot claim.
