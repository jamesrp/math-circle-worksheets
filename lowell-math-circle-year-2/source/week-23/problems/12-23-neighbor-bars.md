+++
id = "w23.23-neighbor-bars"
title = "Neighboring bars only"
grades = ["2-3"]
route = "return"          # save until children track four cards reliably
kernel = "With bars only between neighboring lanes, six bars are needed and enough: 4,3,2,1 has six out-of-order pairs and each neighboring swap fixes exactly one."
+++

## prompt
Build a four-lane machine that sorts every order of 1, 2, 3, 4. Every bar must join neighboring lanes: 1 and 2, 2 and 3, or 3 and 4. Use as few bars as you can, and explain why fewer cannot work.

## figure
network(4,[],y=4.3,gap=1.4)
+ network(4,[],y=14.4,gap=1.4)
