+++
id = "w27.45-asking-rules"
title = "The asking rules, from both sides"
grades = ["4-5"]
route = "first"
kernel = "Deferred acceptance ends in a stable pairing, and the asking side can change it: circles asking give AW / BY / CZ / DX in 8 requests, squares asking give AZ / BY / CW / DX in 7."
+++

## prompt @0.91 size=13.5
Use these rules with A, B, C, D asking. Show or record the requests and final pairs. Run them again with W, X, Y, Z asking. Does changing the asking side change the final pairing?

## text @0.6,1.94 size=12.7
Begin with everyone free. A free asker asks its highest choice that it has not asked before. A free receiver holds its asker. A receiver already holding someone keeps whichever of the two it prefers and releases the other. Holds are temporary. Stop when every asker is held.

## figure
hold_release_example('One step with other letters: U ranks Q ahead of P. Free Q asks U.', 'Before: P held; Q free.', 'After: Q held; P released.')
+ strips(4.56,*get('older_four'),n=4,step=.56,d=.41,size=15)
+ box(.65,7.24,3.35,.75)+box(4.5,7.24,3.35,.75)
+ board(1.10,8.43,'ABCD','WXYZ',w=1.9,step=.48,d=.38,size=14)+board(4.85,8.43,'ABCD','WXYZ',w=1.9,step=.48,d=.38,size=14)
