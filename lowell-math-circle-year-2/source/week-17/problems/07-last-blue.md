+++
id = "w17.last-blue"
title = "Is the last card blue?"
grades = ["K-1", "2-3"]
route = { "K-1" = "return", "2-3" = "first" }
page = { "K-1" = "new", "2-3" = "same" }
kernel = "Two circles: each card resets the answer, so only the last card matters."
+++

## prompt size=17 [K-1]
Use two circles to make a machine that says \Y\ exactly when the last card is blue. With no cards, it must say \N.

## prompt @5.4 size=15 [2-3]
Draw a machine that says YES exactly when its last card is blue. It must say NO if there are no cards. Use as few circles as you can.

## figure [K-1]
state('e0',2.2,3.3,False,True,True)+state('e1',6.15,3.3,False,True,True)+start_arrow(1.2,'e0',3.3)
