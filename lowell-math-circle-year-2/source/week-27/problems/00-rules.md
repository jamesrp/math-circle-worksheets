+++
id = "w27.rules"
kind = "setup"            # unnumbered shared rules; K-1 and 2-3 add the P-U worked example and have page 1 to themselves
title = "Pairings, strips and blocking pairs"
grades = ["K-1", "2-3", "4-5"]
route = ["first", "return"]
+++

## text @0.6,0.9 size=13.7 [K-1]
Pair each circle with a different square. Each strip uses both choices once, with its first choice on the left. A pairing can stay if no two pieces in different pairs both want each other more than their partners.

## text @0.6,0.9 size=13.7 [2-3]
Pair each circle with one square, using every letter once. Each strip runs from first choice to last. A pairing can stay if no two letters in different pairs both prefer each other to their current partners.

## text @0.6,0.87 size=13 [4-5]
Pair each circle with one square, using every letter once. Each list runs from first choice to last, with no ties. A pairing is stable if no two letters in different pairs both prefer one another to their current partners.

## figure [K-1, 2-3]
blocking_example('Example: check P with U. First choice is on the left.', 'Current pairs',
                 'P prefers U to V: yes', 'U prefers P to Q: ',
                 'Both yes: P and U block.', 'P and U do not block.',
                 'Shaded choice = current partner. This check is only for P and U.')
