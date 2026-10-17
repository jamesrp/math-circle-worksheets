#!/usr/bin/env python3
"""Independent exact finite checks; this is not a proof of physical sampling uniformity."""
from math import comb
from fractions import Fraction as F

def main():
    checks = 0
    for N in range(1,25):
        for M in range(1,N+1):
            for n in range(1,N+1):
                dist = {r:F(comb(M,r)*comb(N-M,n-r),comb(N,n)) for r in range(max(0,M+n-N),min(M,n)+1)}
                assert sum(dist.values()) == 1
                assert sum(r*p for r,p in dist.items()) == F(M*n,N)
                assert min(dist) == max(0,M+n-N)
                checks += 1
    for s in range(2,20):
        for N in range(s,25):
            zero = {M:F(comb(N-M,s-M),comb(N,s-M)) for M in range(1,s)}
            expected = {M:F(M*(s-M),N) for M in range(1,s)}
            assert {M for M,p in zero.items() if p==min(zero.values())} == {s//2,(s+1)//2}
            assert {M for M,p in expected.items() if p==max(expected.values())} == {s//2,(s+1)//2}
            checks += 1
    print(f'{checks} exact distribution and design checks passed')
if __name__ == '__main__':main()
