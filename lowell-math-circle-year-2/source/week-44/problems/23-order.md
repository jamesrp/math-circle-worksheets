+++
id = "w44.order"
title = "Does order change the chance?"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "RRB, RBR and BRR each have chance $1/12$: the same factors in a different order, though the draws are dependent."
+++

## prompt @13
Return to copying. Compare the color stories RRB, RBR, and BRR. Does their order change their chance? Give an exact reason for your answer.

## figure
order_boxes()

## key
RRB, RBR, BRR each has probability 1/12. Their products are (1/2)(2/3)(1/4), (1/2)(1/3)(2/4), and (1/2)(1/3)(2/4). Reordering does not change the product of the red factors and blue factors. The draws remain dependent despite this equality.
