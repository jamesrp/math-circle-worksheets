# Card-stage checks for the App fit section (week 89). Standard library only.
from itertools import permutations

def run(inputs, stages):
    t = [0]*stages
    for u in inputs:
        t[0] += u
        for s in range(1, stages):
            t[s] += t[s-1]   # copy the NEW total of the previous stage
    return t

def reach(cards, stages):
    return sorted({run(p, stages)[-1] for p in set(permutations(cards))})

def weights(n, stages):
    return [run([1 if j == i else 0 for j in range(n)], stages)[-1] for i in range(n)]

for cards, st in [((2,2,1,0,0),2), ((4,1,0,0,0),2), ((3,0,0,0,0),2), ((2,2,0,0,0),2),
                  ((2,2,1,0,0),3), ((3,2,2,1,0,0),2), ((3,2,2,1,0,0),3)]:
    r = reach(cards, st)
    orders = len(set(permutations(cards)))
    gaps = [v for v in range(r[0], r[-1]+1) if v not in r]
    print(f"cards {cards} stages {st}: orders {orders}, min {r[0]}, max {r[-1]}, "
          f"reachable {len(r)}, gaps {gaps}")
print("weights, 5 inputs, 2 stages:", weights(5, 2))
print("weights, 5 inputs, 3 stages:", weights(5, 3))
# P18 example vs the task path
path = []
t = [0,0,0]
for k in range(6):
    t[0] += 1; t[1] += t[0]; t[2] += t[1]; path.append(tuple(t))
print("P18 all-ones path:", path)
