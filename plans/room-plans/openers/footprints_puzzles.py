# The route puzzles on the footprints sheet: towns, printed clues, and the checks behind them.
# Shared by footprints.py (drawing) and footprints_check.py (uniqueness). Edges are (u, v) or (u, v, colour).
# A walk is (islands, bridge indexes). Colours: G green, R red, B blue, Y yellow.

H1 = {"A": "G", "B": "R", "C": "B", "D": "B", "E": "R"}  # the house town, repeated colours
E1 = [("D", "E"), ("D", "B"), ("E", "C"), ("B", "C"), ("B", "A"), ("C", "A")]
H2 = {"A": "R", "B": "Y", "C": "B", "D": "B", "E": "R", "F": "Y"}  # two rows of three
E2 = [("A", "B"), ("B", "C"), ("D", "E"), ("E", "F"), ("A", "D"), ("B", "E"), ("C", "F")]
H3 = {k: "W" for k in "ABCDEF"}  # plain lettered islands, coloured bridges
E3 = [("A", "B", "R"), ("B", "C", "B"), ("D", "E", "B"), ("E", "F", "R"),
      ("A", "D", "B"), ("B", "E", "R"), ("C", "F", "B"), ("B", "F", "B")]


def steps(w, cols, a, b):
    return sum(cols[x] == a and cols[y] == b for x, y in zip(w[0], w[0][1:]))


PUZZLES = [
    {"n": 1, "islands": H1, "edges": E1, "answer": "A-B-D-E-C-A",
     "pos": {"A": (0.5, 1.24), "B": (0, 0.72), "C": (1, 0.72), "D": (0, 0), "E": (1, 0)},
     "clues": ["Pat started on the green island.",
               "Pat crossed 5 bridges.",
               "Pat walked from a blue island straight to a red island only once."],
     "checks": [("start green", lambda w: w[0][0] == "A"),
                ("5 bridges", lambda w: len(w[1]) == 5),
                ("blue to red once", lambda w: steps(w, H1, "B", "R") == 1)]},
    {"n": 2, "islands": H2, "edges": E2, "answer": "C-F-E-B-A-D",
     "pos": {"A": (0, 1), "B": (1, 1), "C": (2, 1), "D": (0, 0), "E": (1, 0), "F": (2, 0)},
     "clues": ["Pat started on a blue island.",
               "Pat visited every island.",
               "Pat never walked from a blue island straight to a red island."],
     "checks": [("start blue", lambda w: H2[w[0][0]] == "B"),
                ("every island", lambda w: set(w[0]) == set(H2)),
                ("never blue to red", lambda w: steps(w, H2, "B", "R") == 0)]},
    {"n": 3, "islands": H3, "edges": E3, "answer": "A-B-F-E-B-C",
     "pos": {"A": (0, 1), "B": (1, 1), "C": (2, 1), "D": (0, 0), "E": (1, 0), "F": (2, 0)},
     "clues": ["Pat started on A.",
               "Pat crossed 5 bridges.",
               "Pat never crossed two blue bridges in a row."],
     "checks": [("start A", lambda w: w[0][0] == "A"),
                ("5 bridges", lambda w: len(w[1]) == 5),
                ("no two blue in a row", lambda w: not any(
                    E3[i][2] == "B" == E3[j][2] for i, j in zip(w[1], w[1][1:])))]},
]
