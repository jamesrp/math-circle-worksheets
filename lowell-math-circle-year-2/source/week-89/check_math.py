#!/usr/bin/env python3
"""Independent Week 89 numerical and finite geometric checks (Python stdlib).

This file was written by a fresh mathematics reviewer, independently of the
writer's checker. It checks mathematical models, not the layout or physical
operation of the printable artifacts. General proofs and assumptions are in
the facilitator guide and review-math.md. Finite tests are not universal proofs.
"""
from itertools import permutations, product, combinations
from math import comb, factorial
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def run_machine(inputs, starts):
    state = list(starts)
    history = []
    for incoming in inputs:
        for stage in range(len(state)):
            state[stage] += incoming
            incoming = state[stage]  # NEW total is copied; old stage retained.
        history.append(tuple(state))
    return history


def square(n):
    return set(product(range(n), repeat=2))


def stair(n):
    return {(x, y) for x in range(n) for y in range(n) if x + y < n}


def rectangle(n):
    return set(product(range(n + 1), range(n)))


def cube(n):
    return set(product(range(n), repeat=3))


def pile(n):
    return {(x, y, z) for x, y, z in product(range(n), repeat=3)
            if x + y + z < n}


def differences(row):
    return [b - a for a, b in zip(row, row[1:])]


def check():
    report = {}
    # Independent lattice-cell models, including disjoint coverage assertions.
    for n in range(1, 21):
        require(len(square(n + 1) - square(n)) == 2*n + 1, 'square layer')
        require(len(stair(n)) == n*(n+1)//2, 'stair total')
        require(len(stair(n + 1)) - len(stair(n)) == n + 1, 'stair growth')
        rotated = {(n-x, n-1-y) for x, y in stair(n)}
        require(not stair(n) & rotated, 'paired stairs overlap')
        require(stair(n) | rotated == rectangle(n), 'paired stairs coverage')
        require(len(rectangle(n+1) - rectangle(n)) == 2*n+2, 'rectangle layer')
        shell = cube(n+1) - cube(n)
        top = {(x,y,n) for x,y in product(range(n+1), repeat=2)}
        side = {(n,y,z) for y in range(n+1) for z in range(n)}
        last = {(x,n,z) for x,z in product(range(n), repeat=2)}
        require(not (top & side or top & last or side & last), 'slabs overlap')
        require(top | side | last == shell, 'slabs cover shell')
        require(tuple(map(len,(top,side,last))) == ((n+1)**2,n*(n+1),n*n), 'slab counts')
        require(len(shell) == 3*n*n+3*n+1, 'shell total')
        old_pile_raised = {(x,y,z+1) for x,y,z in pile(n-1)}
        new_base = {(x,y,0) for x,y in stair(n)}
        require(not old_pile_raised & new_base, 'pile layers overlap')
        require(old_pile_raised | new_base == pile(n), 'recursive pile geometry')
        triples = {(x+1,x+y+2,x+y+z+3) for x,y,z in pile(n)}
        require(triples == set(combinations(range(1,n+3),3)), 'pile bijection')
        require(len(pile(n)) == n*(n+1)*(n+2)//6, 'pile total')
    report['P1'] = [len(square(n+1)-square(n)) for n in range(1,5)]
    report['P2'] = [{'side': n, 'kept': n*n, 'removed':25-n*n} for n in range(1,5)]
    report['P3'] = [len(stair(n)) for n in range(2,7)]
    report['P4'] = [len(rectangle(n)) for n in range(2,7)]
    report['P5'] = [len(rectangle(n)) for n in range(1,7)]
    report['P6'] = {name: differences([len(fn(n)) for n in range(1,7)])
                    for name,fn in [('squares',square),('stairs',stair),('rectangles',rectangle)]}
    require(report['P6'] == {'squares':[3,5,7,9,11], 'stairs':[2,3,4,5,6], 'rectangles':[4,6,8,10,12]}, 'P6')
    for name, second in [('squares',2),('stairs',1),('rectangles',2)]:
        require(set(differences(report['P6'][name])) == {second}, 'second differences')
    orders = set(permutations((0,1,2,3,4)))
    require(len(orders)==120, 'P7 orders')
    for initial in (0,3):
        require({run_machine(row,(initial,))[-1][0] for row in orders} == {initial+10}, 'P7 invariant')
    report['P7'] = {'orders':len(orders), 'final_from_0':10,'final_from_3':13}
    report['P8'] = differences([2,5,5,9,12])
    require(report['P8']==[3,0,4,3], 'P8 inputs')
    hidden = []
    # No start >4 can lead to first total4 using nonnegative inputs.
    for start in range(5):
        for row in product(range(6), repeat=4):
            if run_machine(row,(start,)) == [(4,),(7,),(7,),(12,)]:
                hidden.append((start,)+row)
    require(hidden == [(b,4-b,3,0,5) for b in range(5)], 'P9 complete list')
    report['P9'] = hidden
    both = [run_machine((2,0,3,1),(start,)) for start in (1,4)]
    require([b[0]-a[0] for a,b in zip(*both)] == [3]*4, 'P10 gap')
    report['P10'] = both
    orders = set(permutations((2,2,1,0,0)))
    outcomes = {row:run_machine(row,(0,0))[-1][1] for row in orders}
    require(len(outcomes)==30 and min(outcomes.values())==9 and max(outcomes.values())==21, 'P11 bounds')
    require([row for row,val in outcomes.items() if val==21] == [(2,2,1,0,0)], 'P11 unique value order max')
    require([row for row,val in outcomes.items() if val==9] == [(0,0,1,2,2)], 'P11 unique value order min')
    report['P11'] = {'distinct_orders':30,'minimum':9,'maximum':21,
                     'max_history':run_machine((2,2,1,0,0),(0,0)),
                     'min_history':run_machine((0,0,1,2,2),(0,0))}
    zero_orders = sorted(row for row in set(permutations((0,0,1,3))) if row.index(1)<row.index(3))
    report['P12'] = [{'inputs':row,'final_second':run_machine(row,(0,0))[-1][1]} for row in zero_orders]
    require(len(zero_orders)==6, 'P12 orders')
    require({tuple(d['inputs']): d['final_second'] for d in report['P12']} ==
            {(1,3,0,0):13,(1,0,3,0):10,(1,0,0,3):7,(0,1,3,0):9,(0,1,0,3):6,(0,0,1,3):5}, 'P12 results')
    # Small-domain exhaustive checks complement, and do not replace, exchange proof.
    count = 0
    for length in range(1,7):
        for row in product(range(4),repeat=length):
            result = run_machine(row,(0,0))[-1][1]
            require(result==sum((length-i)*u for i,u in enumerate(row)), 'weighted recurrence')
            require(run_machine(sorted(row),(0,0))[-1][1] <= result <=
                    run_machine(sorted(row,reverse=True),(0,0))[-1][1], 'sorting bounds')
            for i in range(length-1):
                swap = list(row);swap[i],swap[i+1] = swap[i+1],swap[i]
                require(run_machine(swap,(0,0))[-1][1]-result == row[i+1]-row[i], 'adjacent exchange')
            count += 1
    report['P13'] = {'finite_input_rows_checked':count, 'universal_argument':'contribution weights and adjacent exchange; see guide'}
    rule_a = lambda n:n*n
    rule_b = lambda n:n*n+max(0,n-4)
    rule_c = lambda n:n*n+2*max(0,n-4)
    require(all(rule_a(n)==rule_b(n)==rule_c(n) for n in range(1,5)), 'matching four rules')
    require(len({rule_a(5),rule_b(5),rule_c(5)})==3, 'different fifth pictures')
    report['P14'] = {'A':[rule_a(5),rule_a(6)], 'B':[rule_b(5),rule_b(6)]}
    report['P15_example'] = [rule_c(5),rule_c(6)]
    report['P16'] = [len(cube(n+1)-cube(n)) for n in range(1,4)]
    require(report['P16']==[7,19,37], 'P16')
    report['P17'] = [[(n+1)**2,n*(n+1),n*n] for n in range(1,4)]
    history = run_machine([1]*30,(0,0,0))
    for n, state in enumerate(history,1):
        require(state == (n,n*(n+1)//2,n*(n+1)*(n+2)//6), 'P18 closed forms')
    report['P18'] = history[5]
    require(report['P18']==(6,21,56), 'P18 sixth')
    report['P19'] = [len(pile(n)) for n in (3,4,5)]
    report['P20'] = len(pile(10))
    require(report['P19']==[10,20,35] and report['P20']==220, 'P19/P20')
    # Worked visuals: input stays fixed inside the operation.
    old={(0,0),(1,0)}; added={(2,0),(0,1),(1,1),(2,1)}
    require(not old & added and old | added == set(product(range(3),range(2))), 'growth bridge')
    require(run_machine([3],(2,)) == [(5,)], 'single bridge')
    require(run_machine([2],(1,1)) == [(3,4)], 'two-stage bridge')
    require(run_machine([1],(2,3,4)) == [(3,6,10)], 'three-stage bridge')
    require(pile(2)=={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}, 'pile bridge')
    # Pascal uses forward differences: f(n+1)-f(n).
    for n in range(1,31):
        for k in range(1,n+1):
            require(comb(n+1,k)-comb(n,k)==comb(n,k-1), 'Pascal forward difference')
    for degree in range(9):
        row = [n**degree for n in range(20)]
        for unused in range(degree): row=differences(row)
        require(set(row)=={factorial(degree)}, 'monomial highest difference')
        require(set(differences(row))=={0}, 'next difference zero')
    report['verification_limits'] = 'Finite model checks; general arguments are documented separately. No PDF rendering or physical rehearsal is implied.'
    return {'status':'PASS','week':89,'problem_count':20,'results':report}


if __name__ == '__main__':
    print(json.dumps(check(),indent=2))
