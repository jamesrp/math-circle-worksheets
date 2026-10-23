+++
id = "w30.third-weight"
title = "A third weight for 1 and 3"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = 'Adding 9 to 1 and 3 balances every target from 1 to 13: 8 leaves a repeat and stops at 12, 10 leaves a gap at 5.'
+++

## prompt @0 [K-1]
You have weights 1 and 3; choose one more weight from 8, 9 and 10. Which choice balances every target from 5 through 13?

## prompt @0 [2-3]
You have weights 1 and 3. Choose one more whole-number weight so that the kit balances every target from 1 through 13. Test your choice.

## prompt @0 [4-5]
Add one weight to 1 and 3. Which choice balances the longest unbroken run of targets starting at 1? Explain why a smaller or larger choice cannot do better.

## figure [K-1]
draw(('weights', [1, 3], 2.1), ('weights', [8, 9, 10], 5.1), ('targets', range(5, 14), 8.1, 5), ('blanks', [5, 13], 12.3), ('ruled', 22, 2))

## figure [2-3]
draw(('weights', [1, 3], 2), ('targets', range(1, 14), 5, 7), ('blanks', [5, 8, 13], 9))

## figure [4-5]
draw(('targets', range(1, 16), 3, 8), ('blanks', [5, 7], 8), ('ruled', 20, 3))
