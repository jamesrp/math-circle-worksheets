+++
id = "w30.fourth-weight"
title = "A fourth weight for 1, 3 and 9"
grades = ["2-3", "4-5"]
route = "return"
page = { "2-3" = "same", "4-5" = "new" }
kernel = 'Adding 27 to 1, 3, 9 balances every target from 1 to 40, each in exactly one way: the new weight is twice the old total plus 1.'
+++

## prompt @13 [2-3]
Choose a fourth weight to add to 1, 3 and 9. Make the longest possible unbroken run of targets starting at 1, and explain why your kit reaches all of them.

## prompt @0 [4-5]
Use the kit 1, 3 and 9. Add one weight so that the new kit balances every target in the longest possible run starting at 1, each in exactly one way. Explain why there are neither gaps nor repeated answers.

## figure [2-3]
draw(('ruled', 16, 7))

## figure [4-5]
draw(('ruled', 3.5, 7))
