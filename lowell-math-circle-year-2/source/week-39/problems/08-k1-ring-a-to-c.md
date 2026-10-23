+++
id = "w39.k1-ring-a-to-c"
title = "What six-step trips from A to C leave"
grades = ["K-1"]
route = "return"
kernel = "Six-step trips from A to C on the ring leave exactly four results: ABC, ADC, ABCDABC and ADCBADC."
+++

## prompt @27
Make every different trip from A to C that can remain after shortening a six-step trip. Can two of your remaining trips visit exactly the same roads in a different order?

## figure
graph(50, 76, 53, RING, REDGES) + blank(16, 203, 180, 49)

## key
Exactly four results: ABC, ADC, ABCDABC, and ADCBADC. Their lengths are 2, 2, 6, and 6. Six-step inputs for the short results include ABABABC and ABABADC. A nonreversing route from A to the opposite vertex C has length 2 modulo 4, so no other result of length at most 6 exists. Yes, the two six-step survivors both use all four roads, but in different orders. They do not have the same directed-edge multiset; the question only asks for the same roads.
