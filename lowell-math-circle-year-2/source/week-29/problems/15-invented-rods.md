+++
id = "w29.invented-rods"
title = "Invented rods with no common divisor"
grades = ["4-5"]
route = "return"
page = "same"
kernel = 'For coprime a and b, the multiples 0, b, ..., (a-1)b reach every remainder modulo a, so adding a-rods covers every long enough target.'
+++

## prompt @16
Invent paper rods of two different whole-number lengths a and b that have no common divisor larger than 1. Explain why some finite group of builds must settle every length from some point on.

## figure
draw(('ruled', 19, 4))

## key
\emph{Print guide, p. 4.} Many choices work. Example: 2/5 has builds 4 and 5, so all targets at least 4 work. In general, assume a,b are positive and coprime. The a numbers 0,b,2b,...,(a-1)b have different remainders modulo a: equal remainders would make a divide (j-k)b and hence j-k, impossible for distinct indices in 0,...,a-1. Each remainder therefore has a reachable starting value; add a-rods within each remainder class. This proves eventual coverage for any invented pair. If a=1, the conclusion is immediate.
