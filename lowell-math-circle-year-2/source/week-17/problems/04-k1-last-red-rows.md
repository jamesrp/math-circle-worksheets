+++
id = "w17.k1-last-red-rows"
title = "Every four-card row that finishes at yes"
grades = ["K-1"]
route = "first"
kernel = "This machine says yes exactly when the last card is red: 8 of the 16 four-card rows."
+++

## prompt size=17
Make every four-card row that finishes at \Y. Show each row once.

## figure
two('lastR',2.6,5.9,2.58,True)+blank_rows([1.05,4.75],[3.9,4.95,6.0,7.05,8.1,9.15],4,.48,.65)
