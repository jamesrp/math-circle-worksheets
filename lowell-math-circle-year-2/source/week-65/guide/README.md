# Adult guide

The seven-page guide is separate from the student drafting workflow. It opens with precise mathematical destinations and limits, then gives readiness, materials, a shared launch, first-visit choices, all student solutions, child-sized hints, proofs, return-visit options and source references.

Requires Python 3 and ordinary pdfLaTeX with Helvetica, geometry, amsmath/amssymb, TikZ, enumitem, fancyhdr and hyperref.

    python3 build.py --output facilitator.pdf
    python3 verify_geometry.py
    python3 verify_routes.py

`facilitator.tex` is directly editable. `verify_geometry.py` independently constructs the {8,4} tiling, checks both center and vertex-set deduplication, all 57 local rooms, complete-road separation, and the two-room/two-square boundary comparison. `verify_routes.py` independently enumerates the route answers from the printed four-room adjacency and checks square-grid examples. Neither script imports the student builder. The development mathematical review additionally used an independent Lorentzian reflection construction and audited the draft's actual TikZ circle parameters.

A missing diameter exception in the draft's technical explanation was corrected after independent review. Geodesics through the disk center are diameters and use ordinary line reflection; the finite-circle formulas apply otherwise. Final physical spacing is documented, but no actual print/counter rehearsal or classroom pilot has been performed.
