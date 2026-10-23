+++
id = "w31.every-blocker"
title = "Why the rule finds every blocker"
grades = ["4-5"]
route = "return"
kernel = 'With u = a/d and v = b/d coprime, every lattice point on the ray is an integer multiple of (u, v), so the d - 1 multiples are all the blockers.'
+++

## prompt
Explain why your Problem 3 rule finds every blocker: why can no other dot lie on the thread between O and the target?

## figure
draw(('ruled', 3.2, 8))

## key
\emph{Print guide, p. 4.} Put u=a/d, v=b/d; then gcd(u,v)=1. The d-1 points k(u,v), $1\leq k<d$, are blockers. Any lattice point on that ray is t(u,v). For a positive coordinate, t is rational; write it in lowest terms. Its denominator must divide both u and v, hence is 1. Therefore t is an integer, so no extra points fit between consecutive listed points. This also covers axes: the primitive coordinate pair is (1,0) or (0,1).
