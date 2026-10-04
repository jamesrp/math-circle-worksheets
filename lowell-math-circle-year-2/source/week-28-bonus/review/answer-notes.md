# Week 28 revised answers and assumptions

Three investigations: one-fold inverse alignment (P1), connected-strip layer orders (P2–P3), reflected punch-pattern orbits (P4–P5). One shared Grades K–5 companion. P1/P2/actual unfoldings offer supported concrete entry; P3 completeness is a readiness-dependent static-model task. No physical folding, four-panel sequential reachability, eight-layer punch capacity, material accuracy or hole clearance has been rehearsed. All material is unpiloted. The student page explicitly describes P3 as an ideal thin-paper side view and does not claim a noncrossing drawing supplies a physical folding motion.

## Problem 1

Coordinates below are adult checking coordinates relative to each diagram's 6×6 square. Marks and creases are ideal exact points/lines; approximate copying/folding is an experiment, not proof.

1. P=(1,1), Q=(5,1), R=(2,4), S=(4,4): possible, crease x=3, the middle vertical line.
2. P=(1,1), Q=(5,1), R=(1,4), S=(4,4): impossible. P→Q forces x=3; R→S forces x=2.5.
3. Same as case1 with T=(3,5): possible, x=3 fixes T.
4. Same as case1 with T=(2,5): impossible under the requested P-side-folds-onto-Q-side action; T is on the moving P side, so x=3 moves it to (4,5).

The unique straight crease reflecting distinct P to Q is the perpendicular bisector of segment PQ. Simultaneously aligning two ordered pairs requires their bisectors to coincide. A point fixed by the reflection lies on the crease. For a physical half-sheet fold, marks on the stationary half also stay put without lying on the crease: do not apply the last statement indiscriminately. This packet's T off-crease case deliberately lies on the moving P side, so the intended impossibility is valid. A squared-distance calculation gives 2(Q−P)·X=|Q|²−|P|²; no coordinates needed for a child's distance/drawing explanation. Physical alignment tolerances do not establish exact coincidence.

## Problem 2

Non-task convention: X folds under Y; side view has Y above X; output word YX reads top to bottom. Read the three-panel stack with B's original front facing up; this canonical orientation removes reversal by turning over the completed stack. Mark original fronts before trying three-panel stacks; labels must be visible on both sides and the strip stays connected, with only its two joins creased.

The ideal three-panel orders are ABC, ACB, BAC, BCA, CAB, CBA. In the language of original-front-directed outer-panel folds:

- Both outer panels toward the original front of B: ACB or CAB; B is bottom. Order of folding selects the top outer panel.
- Both away from the front of B: BAC or BCA; B is top.
- A toward front and C toward back: ABC.
- A toward back and C toward front: CBA.

This is an ideal expected classification, not a completed physical rehearsal or guarantee about stiff/creased material. Child experiments should record actual witnesses. The directions comparison is the mathematical question, so its second table column is purposeful rather than incidental simultaneous transcription. Mountain/valley labels are not required; do not use Maekawa's interior-vertex rule on these boundary strip joins.

## Problem 3

Static zero-thickness model only. AB and CD bends attach at one end, BC at the other. All four labeled layer permutations are tested by the interleaving condition: if the positions of A/B and C/D alternate, their same-end arcs cross. If their intervals are disjoint or nested, they can be drawn noncrossing; BC's arc lives at the other end and meets no other bend there. These noncrossing arcs supply a static embedding, not a rigid motion.

Sixteen valid orders:
ABCD, ABDC, ACDB, ADCB, BACD, BADC, BCDA, BDCA, CABD, CBAD, CDAB, CDBA, DABC, DBAC, DCAB, DCBA.

Eight excluded interleavings:
ACBD, ADBC, BCAD, BDAC, CADB, CBDA, DACB, DBCA.

The excluded count is 2 choices of first pair ×2 orientations of AB ×2 orientations of CD =8. Thus 24−8=16. The diagram depicts one possible static side view ABCD to establish joins/ends; the child still finds the complete classification. A drawing or enumeration establishes the stated model; actual folding witnesses must be separately tested. No extra crease or tearing is allowed in the physical strip branch.

## Problem 4

Use separate square sheets about15cm; fold both midlines onto the top-right quarter. Printed diagrams are pattern records, not cutting/punch templates. Folded-quarter records show the two folded edges on left/bottom; their lower-left corner is the original sheet center. An off-fold/off-edge point (p,q), p,q>0, unfolds to (±p,±q), four distinct centered-rectangle vertices. Fold-order reversal gives the same set. Pattern counts alone do not establish attainability.

Coordinates in diagram units (full square [-3,3]²): pattern1 uses p=1.7,q=.9, and is possible; pattern2 p=q=1.2, also possible with four holes; pattern3 moves (-1.7,-.9) to (-1.2,-.9), so breaks the vertical reflection and is impossible. Suggested records: put the point (p,q) measured from lower-left on each folded-quarter record. Any reflected representative of the same orbit is equivalent before the quarter is selected.

## Problem 5

Additionally fold the quarter along its diagonal onto the shown lower-right triangle (0≤q≤p≤3). Away from all folds, p>q>0. The image set is (±p,±q) together with (±q,±p), eight distinct centers. Patterns1 and2 are possible, with (p,q)=(1.7,.9) and (1.8,.7). Pattern3 is the union of midline orbits (1.7,.8) and (.7,1.4); it is midline-symmetric but not diagonal-symmetric, e.g. (1.7,.8) would require (.8,1.7), which is absent. Thus it cannot arise from the stated one punch. Reversing the horizontal/vertical fold order leaves the orbit unchanged.

Off-axis and away-from-diagonal restrictions matter: p=q after the diagonal fold gives four rather than eight centers, and fold-line punches have smaller orbits. The questions exclude these. Distinct point-centers do not certify separate real circular holes. On a15cm square the suggested target centers scale by2.5cm per diagram unit; the valid targets are geometrically more than10mm from each relevant crease/edge, but actual punch diameter, registration and capacity remain untested. Adults must rehearse before classroom use. If a punch cannot handle the stack, children may draw reflected centers as a labeled model; that is not a punched witness.

## Sources and QA

`src/check.py` independently enumerates writer-side 24 stack orders and reflects every hole target, with alignment equations. `writer-checks.json` records these digital checks, not physical rehearsal and not separate math review. Portable standalone LaTeX build accepts optional output directory. Every page was rendered and visually inspected after repairs. Rozhkovskaya Lesson12 supplies related reflection activities and classroom reports about the need for actual mirrors/physical figures, not these exact questions or counts; physical folding/punching here is an adaptation/inference. No external source claim for the new16-count or orbit examples.

## Added punch convention example and representation checks

The non-task example uses a 4×4 square, one vertical midline x=2, and a folded-right-half punch at original-sheet point (3.2,1.1). The second layer reflects it to (0.8,1.1); these are the two shown unfolded centers. Both are strictly away from the crease/edge. The folded-stack local coordinate is (1.2,1.1), translated to the diagram location (8.2,1.1). This is an ideal point-center example, not a physical hole-clearance or punch-capacity claim. All target pattern positions were retained while square drawings increased to 4.68 cm. The alignment instructions now use exact tracing rather than freehand dot copying.
