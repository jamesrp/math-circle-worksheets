+++
id = "w62.first-slot-path"
title = "First-slot orders on a path"
grades = ["shared"]
route = "return"
kernel = 'On the 4-path the first-slot rule uses 2 or 3 slots depending on the order, and moving cards afterwards always reaches 2.'
+++

## prompt
Find orders that make the rule use as few slots and as many slots as possible on this network. After an order is finished, you may move cards. Can you use fewer slots?

## figure
center(graph("p7-path",P4,P4e))
+r"\recordline{Order:}\vspace{0.25cm}"
+"\n"
+center(graph("p7-path-extra",P4,P4e))
+r"\recordline{Order:}"
+notespace(1)
