"""Map data shared by verify.py and build.py.

Coordinates are in map units; build.py scales them.  Each link is
(u, v, price).  Places listed in "optional" are drawn as squares.
"""

GRID = {"A": (0, 1), "C": (1, 1), "E": (2, 1), "B": (0, 0), "D": (1, 0), "F": (2, 0)}
STRIP = {"A": (0, 1), "C": (1, 1), "E": (2, 1), "B": (0.5, 0), "D": (1.5, 0), "F": (2.5, 0)}

MAPS = {
    # K-1 Problem 1 (four-place tie map, redrawn as a diamond)
    "tie4": {
        "places": ["A", "B", "C", "D"],
        "pos": {"B": (0, 0), "A": (1, 0.72), "C": (1, -0.72), "D": (2, 0)},
        "links": [("A", "B", 1), ("B", "C", 1), ("A", "C", 1), ("C", "D", 2), ("A", "D", 3)],
    },
    # K-1 Problems 2-3: groups 4, 2, 1 after the 1-, 2-, 3-dot links
    "kmap": {
        "places": list("ABCDEF"),
        "pos": GRID,
        "links": [("A", "B", 1), ("A", "C", 2), ("B", "C", 2), ("C", "D", 3), ("B", "D", 4),
                  ("C", "E", 4), ("D", "E", 2), ("E", "F", 1), ("D", "F", 4)],
    },
    # 2-3 Problems 1-3, 4-5 Problems 1-3: six cheapest networks, groups 6,3,2,2,1,1.
    # Drawn as a strip of triangles so it cannot be confused with the
    # six-place map (grid layout) later in the same packets.
    "vmap": {
        "places": list("ABCDEF"),
        "pos": STRIP,
        "links": [("A", "B", 1), ("A", "C", 1), ("B", "C", 1), ("C", "D", 2), ("B", "D", 3),
                  ("C", "E", 4), ("D", "E", 4), ("E", "F", 1), ("D", "F", 5)],
    },
    # 4-5 Problem 4: the base week's five-place tie map (three cheapest
    # networks of different shapes, all with prices 1, 1, 2, 2)
    "tie5": {
        "places": list("ABCDE"),
        "pos": {"A": (0, 1), "B": (0, 0), "C": (1, 0.5), "D": (2, 1), "E": (2, 0)},
        "links": [("A", "B", 1), ("A", "C", 1), ("B", "C", 1), ("C", "D", 2), ("C", "E", 3),
                  ("D", "E", 2), ("A", "D", 5), ("B", "E", 6)],
    },
    # 4-5 Problem 5 (outline's limit example)
    "samsq": {
        "places": list("ABCD"),
        "pos": {"A": (0, 1), "B": (1, 1), "C": (1, 0), "D": (0, 0)},
        "links": [("A", "B", 1), ("B", "C", 3), ("C", "D", 3), ("D", "A", 3)],
    },
    # 2-3 Problem 4, 4-5 Problem 7
    "cycle4": {
        "places": list("ABCD"),
        "pos": {"A": (0, 1), "B": (1, 1), "C": (1, 0), "D": (0, 0)},
        "links": [("A", "B", 1), ("B", "C", 1), ("C", "D", 1), ("D", "A", 4)],
    },
    # base week's six-place map
    "sixmap": {
        "places": list("ABCDEF"),
        "pos": GRID,
        "links": [("A", "B", 1), ("B", "C", 2), ("A", "C", 3), ("C", "D", 2), ("D", "E", 1),
                  ("E", "F", 2), ("D", "F", 4), ("B", "D", 5), ("C", "E", 6)],
    },
    # six-place map with only A and F required (4-5 Problem 9)
    "sixAF": {
        "places": list("ABCDEF"),
        "optional": list("BCDE"),
        "pos": GRID,
        "links": [("A", "B", 1), ("B", "C", 2), ("A", "C", 3), ("C", "D", 2), ("D", "E", 1),
                  ("E", "F", 2), ("D", "F", 4), ("B", "D", 5), ("C", "E", 6)],
    },
    "star": {
        "places": ["A", "B", "C", "S"], "optional": ["S"],
        "pos": {"A": (0, 1.0), "B": (-0.866, -0.5), "C": (0.866, -0.5), "S": (0, 0)},
        "links": [("A", "B", 4), ("B", "C", 4), ("A", "C", 4), ("S", "A", 2), ("S", "B", 2), ("S", "C", 2)],
    },
    "star3": {
        "places": ["A", "B", "C", "S"], "optional": ["S"],
        "pos": {"A": (0, 1.0), "B": (-0.866, -0.5), "C": (0.866, -0.5), "S": (0, 0)},
        "links": [("A", "B", 4), ("B", "C", 4), ("A", "C", 4), ("S", "A", 3), ("S", "B", 3), ("S", "C", 3)],
    },
    "star224": {
        "places": ["A", "B", "C", "S"], "optional": ["S"],
        "pos": {"A": (0, 1.0), "B": (-0.866, -0.5), "C": (0.866, -0.5), "S": (0, 0)},
        "links": [("A", "B", 4), ("B", "C", 4), ("A", "C", 4), ("S", "A", 2), ("S", "B", 2), ("S", "C", 4)],
    },
    # K-1 Problem 5: four circled corners of a diamond, optional centre X
    "diamondx": {
        "places": ["A", "B", "C", "D", "X"], "optional": ["X"],
        "pos": {"A": (0, 0.9), "B": (1.15, 0), "C": (0, -0.9), "D": (-1.15, 0), "X": (0, 0)},
        "links": [("A", "B", 4), ("B", "C", 4), ("C", "D", 4), ("D", "A", 4),
                  ("X", "A", 2), ("X", "B", 2), ("X", "C", 2), ("X", "D", 2)],
    },
    # K-1 Problem 6, 4-5 Problem 11: two optional places, each with three links
    "twosq": {
        "places": ["A", "B", "C", "D", "S", "T"], "optional": ["S", "T"],
        "pos": {"A": (0, 1), "B": (0, 0), "S": (1, 0.5), "T": (2, 0.5), "C": (3, 1), "D": (3, 0)},
        "links": [("A", "S", 1), ("B", "S", 1), ("S", "T", 2), ("T", "C", 1), ("T", "D", 1),
                  ("A", "B", 3), ("C", "D", 3), ("A", "C", 4)],
    },
    # convention example for opening links by price (non-task)
    "openex": {
        "places": list("ABCD"),
        "pos": {"A": (0, 1), "B": (1, 1), "C": (1, 0), "D": (0, 0)},
        "links": [("A", "B", 1), ("B", "C", 2), ("C", "D", 3), ("D", "A", 2)],
    },
    # convention example for buying (K-1) and for trips (2-3, 4-5), non-task
    "pathex": {
        "places": list("ABC"),
        "pos": {"A": (0, 0), "B": (1, 0), "C": (2, 0)},
        "links": [("A", "B", 2), ("B", "C", 1)],
    },
    # 2-3 Problem 6: triangle with prices to choose
    "tri": {
        "places": list("ABC"),
        "pos": {"A": (0, 0), "B": (1, 0.8), "C": (2, 0)},
        "links": [("A", "B", 0), ("B", "C", 0), ("A", "C", 0)],
    },
    # convention example for optional places (non-task)
    "optex": {
        "places": ["A", "B", "S"], "optional": ["S"],
        "pos": {"A": (0, 1), "B": (2, 1), "S": (1, 0)},
        "links": [("A", "B", 3), ("A", "S", 2), ("S", "B", 2)],
    },
}
