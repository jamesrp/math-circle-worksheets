Week NN: Train-yard sorting

Mathematical kernels

1. What one siding can sort. Cars numbered 1 to n arrive one at a time along the main line, in some order. Each arriving car drives into a dead-end siding; the car nearest the siding's exit may leave onto the departure track. The cars must depart in the order 1, 2, …, n. Because the last car into the siding is the first out, a car stuck above a smaller car blocks it for good. An arrival order can be sorted exactly when no three cars arrive in the pattern middle, largest, smallest (no 2-3-1 pattern): with three cars only the order 2, 3, 1 fails. The method that never fails when sorting is possible: send a car out whenever the next car needed is at the siding's exit, and otherwise bring in the next arriving car (computer check of both facts for every order of up to 8 cars).

2. Counting the orders that work. The sortable arrival orders number 1, 2, 5, 14, 42, 132, 429, 1,430 for 1 to 8 cars, the Catalan numbers (computer). Writing each car's entry into the siding as an up-step and each departure as a down-step turns a sorting run into a mountain path of n ups and n downs that never dips below the start, and each such path gives exactly one sortable arrival order. This is Week 12's mountain path reached from a machine.

3. More sidings (extension). With two sidings one after the other, every arrival order of up to six cars can be sorted, and 22 of the 5,040 seven-car orders cannot (computer). The general description of what two sidings can sort is hard (Knuth posed it; it remains a research topic), so this stays an open-ended continuation.

Sources: Donald E. Knuth, The Art of Computer Programming, vol. 1, 3rd ed. (1997), §2.2.1, exercises 2–5 (the railway with a siding); Robert E. Tarjan, "Sorting using networks of queues and stacks", Journal of the ACM 19 (1972), 341–346. Library: Week 12 counts the Catalan families (noncrossing pairings, mountain paths, trees), Week 23 sorts with fixed comparator bars, and Week 3 treats orders as permutations. New here: a physical last-in, first-out device, the 2-3-1 obstruction found by trying, and a new route to the Catalan numbers for children who met Week 12.

Suggested emphasis by level: K–1 drives three numbered cars through the siding so that they leave 1, 2, 3, and finds which of the six arrival orders work; no reading, numbers to 5. Grades 2–3 sort four and five cars, describe what makes an order impossible, and pool all 24 four-car orders. Grades 4–5 explain the 2-3-1 rule, count the sortable orders, connect each sorting run to a mountain path, and try two sidings.

Materials

A printed track mat per pair at 100%: an arrival track on the right, a departure track on the left, and a dead-end siding below the junction exactly one car wide and five cars long, drawn with walls so that cars sit in a single line. Cars: cubes or 25 mm card squares numbered 1 to 5, one set per pair (five sets; number the cubes with a marker, about 10 minutes). Cars slide along the table and may not be lifted over one another; the partner watches the siding's exit. Arrival-order cards (a row of numbers per card) for problems that give orders, and blank cards for pooling. The launch runs one non-task arrival order of three cars (for example 1, 3, 2) through the siding with the whole group.
