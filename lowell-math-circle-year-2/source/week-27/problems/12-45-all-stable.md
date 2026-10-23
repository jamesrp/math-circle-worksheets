+++
id = "w27.45-all-stable"
title = "All stable pairings"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "The two-pair lists have two stable pairings, one giving the circles their first choices and one giving the squares theirs; the three-pair lists have exactly one, AY / BZ / CX."
+++

## prompt @1.79
Find all stable pairings for each set of lists.

## figure
strips(2.56,*get('k_two_stable'),n=2,step=.58,d=.43,size=16)
+ board(1.18,4.18,'AB','XY',w=1.9,step=.56,d=.42)+board(4.94,4.18,'AB','XY',w=1.9,step=.56,d=.42)
+ ln(.6,5.13,7.9,5.13)+strips(5.63,*get('middle_unique'),step=.56,d=.43,size=16)
+ ''.join(board(.70+col*2.55,8.13,step=.56) for col in range(3))
