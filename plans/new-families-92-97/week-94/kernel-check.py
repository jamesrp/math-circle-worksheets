#!/usr/bin/env python3
"""Exact checks of the independent affine calibration derivation."""
from fractions import Fraction as F

def main():
    checks = 0
    for a in range(-4,5):
        for b in [F(1,2),F(1),F(2),F(3)]:
            for x1 in range(0,8):
                for x2 in range(x1+1,9):
                    y1,y2 = a+b*x1,a+b*x2
                    recovered_b = (y2-y1)/(x2-x1)
                    recovered_a = y1-recovered_b*x1
                    assert (recovered_a,recovered_b)==(a,b)
                    for e in [F(0),F(1,2),F(1)]:
                        lo,hi=(y2-y1-2*e)/(x2-x1),(y2-y1+2*e)/(x2-x1)
                        assert hi-lo==4*e/(x2-x1)
                        for slope,err1,err2 in [(lo,-e,e),(hi,e,-e)]:
                            intercept=y1-slope*x1-err1
                            assert intercept+slope*x2+err2==y2
                        checks += 1
    print(f'{checks} exact affine identification and interval-endpoint checks passed')
if __name__ == '__main__':main()
