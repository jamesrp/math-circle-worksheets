"""Answer check for every board printed in the three revised packets.
Bites are (row, column) counted from the poison corner; positions are row
lengths, bottom row first.  W = the player to move can make sure to win."""
from chomp import win, winning_moves, positions_in_box


def show(label, boards):
    print(label)
    for b in boards:
        wm = winning_moves(b)
        print(f"   {b}: {'W' if win(b) else 'L'}  winning bites {[m for m, _ in wm]}  leaving {[q for _, q in wm]}")


show("K-1 P1 (X on W boards, circle L boards)", [(2, 1), (2, 2), (3, 1)])
show("K-1 P2", [(3, 3), (4, 4)])
show("K-1 P3 (circle the L ones)", [(3, 1, 1), (4, 1, 1)])
show("K-1 P4", [(3, 3, 3), (4, 4, 4, 4)])
show("K-1 P5", [(6, 6)])
print("K-1 P6: second-player wins reachable by bites from 4x4:")
print("   ", [p for p in positions_in_box(4, 4) if not win(p)])
show("2-3 P1", [(3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (3, 1, 1)])
show("2-3 P2", [(3, 3), (4, 4), (6, 6)])
show("2-3 P3", [(5, 4), (5, 2), (5, 3), (4, 1), (6, 5), (6, 3)])
show("2-3 P4", [(3, 3, 3), (4, 4, 4, 4)])
show("2-3 P6 / 4-5 P5", [(4, 4, 4)])
print("2-3 P7: three-row second-player wins reachable by bites from 3x5:")
print("   ", [p for p in positions_in_box(3, 5) if not win(p) and len(p) == 3])
show("4-5 P1", [(4, 4), (6, 6), (3, 3, 3), (4, 4, 4, 4)])
ps = sorted(positions_in_box(3, 3), key=lambda p: (-sum(p), [-x for x in p]))
show("4-5 P2 (page order)", ps)
show("4-5 P3", [(5, 4), (6, 3), (4, 1), (6, 5), (5, 2), (6, 4)])
show("4-5 P6 boards: after the top-right bite on 3x4; the L board", [(4, 4, 3), (3, 1, 1)])
show("4-5 P7", [(5, 5, 5), (6, 6, 6)])
