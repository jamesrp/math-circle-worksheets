# Checks the footprint puzzles on footprints.pdf (built by footprints.py): each must have one answer.
# The town is the Week 10 house town and the floor town:
#   green A (top), purple B (upper left), yellow C (upper right), blue D (bottom left), red E (bottom right),
#   bridges D-E, D-B, E-C, B-C, B-A, C-A.
# Rule: crossing a bridge picks up its note, and a bridge with no note is closed, so Pat crosses each
# held bridge exactly once and no other bridge. A puzzle gives the notes Pat holds and either where Pat
# started or where Pat is now; the answer is the other end of the walk.
# Run: python3 footprints_check.py
WORD = {"A": "green", "B": "purple", "C": "yellow", "D": "blue", "E": "red"}
BRIDGES = {frozenset(b) for b in ["DE", "DB", "EC", "BC", "BA", "CA"]}


def walks(held):
    """Every walk that crosses each held bridge exactly once and nothing else: (start, end) pairs."""
    held = [frozenset(b) for b in held]
    assert all(b in BRIDGES for b in held), held
    ends = set()

    def go(here, start, left):
        if not left:
            ends.add((start, here))
            return
        for b in left:
            if here in b:
                (there,) = b - {here}
                go(there, start, left - {b})

    for start in "ABCDE":
        go(start, start, frozenset(held))
    return ends


def solve(held, start=None, now=None):
    pairs = walks(held)
    if start:
        return sorted({e for s, e in pairs if s == start})
    return sorted({s for s, e in pairs if e == now})


PUZZLES = [
    # (label, held notes, known start, known position now, expected answer)
    ("Problem 1: started on blue; where now?", ["DE", "EC"], "D", None, "C"),
    ("Problem 2: on green now; where did Pat start?", ["DB", "BC", "CA"], None, "A", "D"),
    ("Problem 3: on purple now; where did Pat start?", ["BC", "CA", "AB"], None, "B", "B"),
    ("Problem 4: started on green; where now?", ["AB", "BD", "DE", "EC", "CB"], "A", None, "B"),
]

for label, held, start, now, want in PUZZLES:
    got = solve(held, start, now)
    print(f"{label} -> {[WORD[g] for g in got]}")
    assert got == [want], (label, got)
print("All four puzzles have exactly one answer.")
