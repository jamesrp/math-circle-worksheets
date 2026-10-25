"""Pancake flip checks. Stacks are tuples read from the top; sorted = (1,2,...,n)."""
from collections import deque, Counter
from itertools import permutations

def flip(s, k):
    return tuple(reversed(s[:k])) + s[k:]

def bfs_unburnt(n):
    goal = tuple(range(1, n+1))
    dist = {goal: 0}
    q = deque([goal])
    while q:
        s = q.popleft()
        for k in range(2, n+1):
            t = flip(s, k)
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist

def bflip(s, k):
    # burnt: signed ints, positive = burnt side down
    return tuple(-x for x in reversed(s[:k])) + s[k:]

def bfs_burnt(n):
    goal = tuple(range(1, n+1))
    dist = {goal: 0}
    q = deque([goal])
    while q:
        s = q.popleft()
        for k in range(1, n+1):
            t = bflip(s, k)
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist

def breaks(s):
    n = len(s)
    t = list(s) + [n+1]
    return sum(1 for a, b in zip(t, t[1:]) if abs(a-b) != 1)

def method_flips(s):
    """Largest unsorted to top then down; skip useless flips."""
    s = list(s); n = len(s); c = 0
    for size in range(n, 1, -1):
        pos = s.index(size)  # 0-based
        if pos == size-1:
            continue
        if pos != 0:
            s = list(flip(tuple(s), pos+1)); c += 1
        s = list(flip(tuple(s), size)); c += 1
    assert s == sorted(s)
    return c

if __name__ == '__main__':
    for n in range(2, 8):
        d = bfs_unburnt(n)
        mx = max(d.values())
        dist = Counter(d.values())
        worst = sorted(s for s, v in d.items() if v == mx)
        assert all(breaks(s) <= v for s, v in d.items())
        assert all(method_flips(s) <= 2*n-3 for s in d)
        print(n, 'max', mx, 'distribution', sorted(dist.items()),
              'worst count', len(worst), worst if len(worst) <= 6 else worst[:6])
    for n in range(1, 6):
        d = bfs_burnt(n)
        mx = max(d.values())
        worst = sorted(s for s, v in d.items() if v == mx)
        print('burnt', n, 'max', mx, sorted(Counter(d.values()).items()), 'worst', worst[:8], len(worst))
