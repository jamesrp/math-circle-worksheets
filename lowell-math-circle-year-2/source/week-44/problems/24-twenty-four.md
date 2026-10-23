+++
id = "w44.twenty-four"
title = "Twenty-four marked histories"
grades = ["4-5"]
route = "return"
kernel = "After three draws each red total 0, 1, 2, 3 has six of the 24 marked histories."
+++

## prompt @0
Three copying draws have 24 equally likely marked histories. How many give zero, one, two, or three red draws? Explain how you know your counts cover every possibility.

## figure
total_boxes()

## key
There are six marked histories for each total 0, 1, 2, 3. BBB and RRR each have 1 $\times$ 2 $\times$ 3 = 6 identity histories. For one red, the three words RBB, BRB, BBR have two histories each, hence six. The three words with two reds also have two each. These four groups cover all eight possible color words and all 24 marked histories.
