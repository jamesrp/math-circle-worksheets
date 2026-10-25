#!/usr/bin/env python3
"""Checks for the train-yard sorting packets.

Model: cars arrive in the given order (first car = leftmost in the drawing).
A move pushes the front arriving car into the siding (a stack) or pops the
top car of the siding onto the departure track. The train "works" when the
departures are 1, 2, ..., n.
"""
from itertools import permutations
from collections import deque
import sys


def sortable_bfs(train, cap=None):
    """Exhaustive search over all move sequences (single siding)."""
    n = len(train)
    start = (0, (), 0)  # next arrival index, stack (bottom..top), next needed
    seen = {start}
    q = deque([start])
    while q:
        i, st, need = q.popleft()
        if need == n:
            return True
        if st and st[-1] == need + 1:
            s = (i, st[:-1], need + 1)
            if s not in seen:
                seen.add(s); q.append(s)
        if i < n and (cap is None or len(st) < cap):
            s = (i + 1, st + (train[i],), need)
            if s not in seen:
                seen.add(s); q.append(s)
    return False


def greedy(train):
    """Pop when the needed car is on top, else push. Returns moves or None."""
    st, need, i, moves = [], 1, 0, []
    n = len(train)
    while need <= n:
        if st and st[-1] == need:
            st.pop(); need += 1; moves.append('D')
        elif i < n:
            st.append(train[i]); i += 1; moves.append('U')
        else:
            return None
    return ''.join(moves)


def has231(p):
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[j] > p[i]:
                for k in range(j + 1, n):
                    if p[k] < p[i]:
                        return True
    return False


def two_sidings(train, cap=None):
    """Two sidings in series. Cars leaving siding A go straight into siding B
    (waiting on the middle track adds nothing; see the notes)."""
    n = len(train)
    start = (0, (), (), 0)
    seen = {start}
    q = deque([start])
    while q:
        i, a, b, need = q.popleft()
        if need == n:
            return True
        nxt = []
        if b and b[-1] == need + 1:
            nxt.append((i, a, b[:-1], need + 1))
        if a and (cap is None or len(b) < cap):
            nxt.append((i, a[:-1], b + (a[-1],), need))
        if i < n and (cap is None or len(a) < cap):
            nxt.append((i + 1, a + (train[i],), b, need))
        for s in nxt:
            if s not in seen:
                seen.add(s); q.append(s)
    return False


def two_sidings_queue(train, cap):
    """Two sidings with an unlimited waiting line between them (the middle
    track of two mats laid side by side)."""
    n = len(train)
    start = (0, (), (), (), 0)
    seen = {start}
    q = deque([start])
    while q:
        i, a, mid, b, need = q.popleft()
        if need == n:
            return True
        nxt = []
        if b and b[-1] == need + 1:
            nxt.append((i, a, mid, b[:-1], need + 1))
        if mid and len(b) < cap:
            nxt.append((i, a, mid[1:], b + (mid[0],), need))
        if a:
            nxt.append((i, a[:-1], mid + (a[-1],), b, need))
        if i < n and len(a) < cap:
            nxt.append((i + 1, a + (train[i],), mid, b, need))
        for s in nxt:
            if s not in seen:
                seen.add(s); q.append(s)
    return False


def path_to_train(word):
    """Up = car in, down = car out. Departures are 1..n in order."""
    stack, labels, out = [], {}, 0
    order = []  # indices of up-steps in arrival order
    for idx, c in enumerate(word):
        if c == 'U':
            stack.append(idx); order.append(idx)
        else:
            out += 1
            labels[stack.pop()] = out
    return tuple(labels[i] for i in order)


def is_mountain(word):
    h = 0
    for c in word:
        h += 1 if c == 'U' else -1
        if h < 0:
            return False
    return h == 0


def main():
    ok = True
    print('Single siding: BFS vs greedy vs no-231, and counts')
    for n in range(1, 9):
        cnt = 0
        for p in permutations(range(1, n + 1)):
            b = sortable_bfs(p)
            g = greedy(p) is not None
            a = not has231(p)
            if not (b == g == a):
                ok = False
                print('MISMATCH', p, b, g, a)
            cnt += b
        print(f'  n={n}: {cnt} sortable')
    # capacity 5 does not matter for n <= 5
    for n in range(1, 6):
        for p in permutations(range(1, n + 1)):
            assert sortable_bfs(p, cap=5) == sortable_bfs(p)
    print('  siding of length 5 suffices for n <= 5')

    print('Mountain paths <-> sortable trains')
    for n in range(1, 8):
        words = set()
        from itertools import product
        trains = {}
        for w in product('UD', repeat=2 * n):
            w = ''.join(w)
            if w.count('U') == n and is_mountain(w):
                t = path_to_train(w)
                assert greedy(t) == w, (w, t, greedy(t))
                trains[t] = w
                words.add(w)
        assert len(trains) == len(words)
        sortable = [p for p in permutations(range(1, n + 1)) if greedy(p)]
        assert set(trains) == set(sortable)
        print(f'  n={n}: {len(words)} paths, bijection checked')

    print('Two sidings in series')
    for n in range(1, 8):
        perms = list(permutations(range(1, n + 1)))
        bad_unl = [p for p in perms if not two_sidings(p)]
        bad_c5 = [p for p in perms if not two_sidings(p, cap=5)]
        print(f'  n={n}: unlimited unsortable {len(bad_unl)}, '
              f'capacity-5 unsortable {len(bad_c5)}')
        if n <= 6:
            assert not bad_unl and not bad_c5
        if n == 7:
            # Unlimited sidings (or sidings 6 cars long): 22 orders fail.
            # The printed mat's siding holds 5 cars: then 51 orders fail.
            assert len(bad_unl) == 22 and len(bad_c5) == 51
            assert set(bad_unl) <= set(bad_c5)
            print('    fail even with long sidings:', bad_unl)
            # Cars waiting on the track between the two mats change nothing.
            for p in perms:
                assert two_sidings_queue(p, 5) == two_sidings(p, 5)
            print('    waiting line between mats: same answers for all 7-car orders')
    return ok


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
