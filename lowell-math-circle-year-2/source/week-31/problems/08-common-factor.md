+++
id = "w31.common-factor"
title = "Common factors and blockers, both directions"
grades = ["4-5"]
route = "return"
kernel = 'A common factor q > 1 gives the blocker (a/q, b/q); conversely a blocker t(a, b) with t = r/s in lowest terms forces s > 1 to divide both coordinates.'
+++

## prompt
A target is (a, b), with a and b positive whole numbers. Explain why a common factor larger than 1 always produces a blocker. Does every blocker produce a common factor?

## figure
draw(('ruled', 3, 16))

## key
\emph{Print guide, p. 4.} If $q>1$ divides a and b, then (a/q,b/q) is a lattice point strictly between O and (a,b). Conversely, a blocker (u,v)=t(a,b) has $0<t<1$. Write t=r/s in lowest terms. Since ra/s and rb/s are integers and gcd(r,s)=1, s divides both a and b; also $s>1$. Thus every blocker certifies a nontrivial common divisor. Do not assume every blocker is the first one or that its coordinates divide the target coordinates.
