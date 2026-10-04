"""Independent finite-game checks for all printed starts. No third-party modules."""
from functools import cache
from functools import reduce
from operator import xor
import json
from pathlib import Path
import re

NIM = [(1,0),(1,1),(1,2),(2,2),(2,3),(3,3),(2,0),
       (1,1,1),(1,1,2),(1,2,2),(1,2,3),(2,3,4)]
COINS = [(1,2),(1,4),(4,5),(4,6),(7,8),(7,10),
         (1,2,3),(1,4,6),(2,3,5),(2,4,7),
         (3,4,7),(3,5,9),(4,7,11),(4,7,12)]
ROOKS = [(1,2,1,2),(1,1,2,2),(1,0,2,3),
         (1,3,2,2),(0,2,1,3),(0,1,1,3)]
COIN_EXAMPLE = [(4,10),(4,10),(2,10)]
ROOK_EXAMPLE = [(2,2,1,3),(0,2,1,3),(0,2,1,1)]

def check_source():
    """Keep every actual printed reference and worked example tied to the data."""
    source = Path(__file__).with_name("return-visit.tex").read_text()
    piles = re.findall(r"\\pilecard\{[^}]+\}\{[^}]+\}\{(\d+)\}\{([\d,]+)\}", source)
    coins = re.findall(r"\\coincard\{[^}]+\}\{[^}]+\}\{(\d+)\}\{([\d,]+)\}\{\}", source)
    rooks = re.findall(r"\\rookcard\{[^}]+\}\{[^}]+\}\{(\d+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}", source)
    assert [int(n) for n, _ in piles] == list(range(1,13))
    assert [tuple(map(int, s.split(","))) for _, s in piles] == NIM
    assert [int(n) for n, _ in coins] == list(range(1,15))
    assert [tuple(map(int, s.split(","))) for _, s in coins] == COINS
    assert [int(s[0]) for s in rooks] == list(range(1,7))
    assert [tuple(map(int, s[1:])) for s in rooks] == ROOKS
    examples = re.findall(r"\\coinrow\{[\d.]+\}\{[\d.]+\}\{[\d.]+\}\{([\d,]+)\}", source)
    assert [tuple(map(int, s.split(","))) for s in examples] == COIN_EXAMPLE
    examples = re.findall(r"\\rookpair\{[\d.]+\}\{[\d.]+\}\{[\d.]+\}\{(\d+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}\{\}", source)
    assert [tuple(map(int, s)) for s in examples] == ROOK_EXAMPLE
    assert "all two-pile starts with at least one counter" in source
    assert r"\foreach \i in {0,...,4}" in source
    assert r"\rookgrid{.85}{4.08}{.85}{-1}{-1}" in source
    assert r"\rookgrid{6.2}{4.08}{.85}{-1}{-1}" in source

@cache
def misere_win(state):
    # The game ends when the last counter is taken, and its mover loses.
    # Thus taking the last counter is never a winning candidate move.
    total = sum(state)
    assert total > 0
    for i, amount in enumerate(state):
        for removed in range(1, amount + 1):
            if removed == total:
                continue
            nxt = list(state)
            nxt[i] -= removed
            if not misere_win(tuple(nxt)):
                return True
    return False

def misere_formula(state):
    if max(state) <= 1:
        return sum(state) % 2 == 0
    return reduce(xor, state, 0) != 0

def coin_moves(state):
    for i, pos in enumerate(state):
        left = state[i-1] + 1 if i else 1
        for target in range(left, pos):
            nxt = list(state)
            nxt[i] = target
            yield tuple(nxt)

@cache
def coin_win(state):
    return any(not coin_win(nxt) for nxt in coin_moves(state))

def paired_gaps(state):
    gaps = [state[i]-state[i-1]-1 for i in range(len(state)-1,0,-2)]
    if len(state)%2:
        gaps.append(state[0]-1)
    return gaps

@cache
def rook_win(state):
    for i, amount in enumerate(state):
        for target in range(amount):
            nxt = list(state)
            nxt[i] = target
            if not rook_win(tuple(nxt)):
                return True
    return False

def winner(win):
    return "first" if win else "second"

def legal_rook_move(before, after):
    changes = [i for i, (old, new) in enumerate(zip(before, after)) if old != new]
    return len(changes) == 1 and 0 <= after[changes[0]] < before[changes[0]]

def main():
    from itertools import combinations, product
    check_source()
    # Complete small domains test the formulas, independently of selected cases.
    for size in (2,3):
        for state in product(range(13), repeat=size):
            if sum(state):
                assert misere_win(state) == misere_formula(state), state
    for size in (2,3,4):
        for state in combinations(range(1,13), size):
            assert coin_win(state) == (reduce(xor,paired_gaps(state),0) != 0), state
    for state in product(range(4), repeat=4):
        assert rook_win(state) == (reduce(xor,state,0) != 0), state
    assert [misere_win(s) for s in NIM] == [False,True,True,False,True,False,True,False,True,True,False,True]
    assert [coin_win(s) for s in COINS] == [False,True] * 7
    assert [rook_win(s) for s in ROOKS] == [False,False,False,True,False,True]
    assert COIN_EXAMPLE[-1] in list(coin_moves(COIN_EXAMPLE[0]))
    assert all(legal_rook_move(a,b) for a,b in zip(ROOK_EXAMPLE,ROOK_EXAMPLE[1:]))
    assert all(0 <= distance < 4 for state in ROOKS + ROOK_EXAMPLE for distance in state)
    invented = (0,3,1,2)
    assert rook_win(invented[:2]) and rook_win(invented[2:]) and not rook_win(invented)
    winning_components = [s for s in product(range(4), repeat=2) if rook_win(s)]
    cancellation_pairs = [(a,b) for a,b in combinations(winning_components,2) if not rook_win(a+b)]
    assert len(cancellation_pairs) == 18
    report = {
        "misere": [{"start":s,"winner":winner(misere_win(s))} for s in NIM],
        "coins": [{"start":s,"paired_gaps":paired_gaps(s),"winner":winner(coin_win(s))} for s in COINS],
        "rook_pairs": [{"start":s,"winner":winner(rook_win(s)),"component_nim_values":[s[0]^s[1],s[2]^s[3]]} for s in ROOKS],
        "worked_examples": {"coin":COIN_EXAMPLE,"rooks":ROOK_EXAMPLE,"legal":True},
        "example_new_cancellation": {"start":invented,"winner":winner(rook_win(invented))},
        "distinct_winning_component_cancellations":len(cancellation_pairs),
        "checks": {"misere":"all 168 nonempty two-pile and 2196 nonempty three-pile states with entries 0..12", "coins":"all 66 two-coin, 220 three-coin and 495 four-coin starts on squares 1..12", "rooks":"all 256 positions on two 4x4 boards", "source":"all 32 catalog starts and both worked examples agree with these checked data"}
    }
    print(json.dumps(report,indent=2))

if __name__ == "__main__":
    main()
