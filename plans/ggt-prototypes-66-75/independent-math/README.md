# Independent checks for ten geometric-group-theory prototypes

Reviewed Weeks 66–75, 2026-10-06. All kernels and all final writer-stage draft instances pass with the stated assumptions. Two consequential clarifications: the cylinder citation supports related torus shearing, not the independently derived arc-intersection formula; the fan-map center must be strictly interior (now explicit in the reviewed draft).

## Run

From this directory, using Python 3 and its standard library:

    python3 verify_kernels.py
    python3 verify_draft_instances.py

The second command reads the adjacent small `bounce-unfolding-instance.json` coordinate snapshot. No writer code, TeX installation or downloaded reference is required. It checks the recorded instances; it does not silently certify future versions. To add fingerprints of current writer inputs, pass `--writer-root /path/to/the/parent/of/ggt-writer-a`.

## Files

- `review-math.md`: assumptions and human proofs of all universal claims, including the fan-map extension and the elevator lower bound for destination 23.
- `sources.md`: actual checked source locations and attribution caveats.
- `source-fingerprints.json`: hashes and byte counts of checked reference versions; no references are included.
- `verify_kernels.py`, `kernel-check-results.json`: independent exact finite kernel checks and results.
- `verify_draft_instances.py`, `bounce-unfolding-instance.json`, `draft-instance-check-results.json`, `reviewed-input-fingerprints.json`: exact draft-instance checks, recorded geometry, answers, and source/PDF fingerprints.
- `draft-instance-review.md`: problem-by-problem findings and audit limits.

All mathematical diagrams and numerical data retained here are authored prototype data. No whole source reference, copied source page or reference figure is part of this deliverable. Physical/classroom rehearsal and comprehensive final-output visual review are separate.
