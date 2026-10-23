+++
id = "w13.no-change-walk"
title = "No change-walk means largest"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "If no change-walk reaches Finish, the arrows leaving the reachable set are all reserved and number exactly k, so closing them proves the k routes are largest (max-flow min-cut)."
+++

## prompt
On any finite board with these rules, suppose no change-walk from Start can reach Finish. Must the reserved route collection already be largest? Explain why, or draw a board where it is not.

## key
Answer: yes. Suppose a collection of k routes has no change-walk to Finish. Mark S, all vertices reachable from Start by unused forward arrows and used backward arrows. Start is in S and Finish is outside. Every original arrow leaving S is reserved, or its unused forward direction would reach another dot. Every original arrow entering S is unreserved, or its backward direction would reach a dot outside S.

At every internal dot, the number of reserved arrows coming in equals the number going out. Add this balance over all dots of S. Internal arrows cancel in pairs. The only surplus is k at Start, since Finish is outside. Hence k equals the number of reserved outward arrows minus the number of reserved inward arrows. The latter is zero; all outward arrows are reserved. There are therefore exactly k outward arrows, and closing them blocks every route. Page 4’s certificate proves the current collection is largest.
