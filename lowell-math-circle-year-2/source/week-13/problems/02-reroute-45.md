+++
id = "w13.reroute-45"
title = "Replace stuck reserved routes"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "Reserved routes that leave no room can be replaced by a larger collection; on the double-trap board two reservations must be undone at once."
+++

## prompt
The thick arrows form reserved routes. No more routes fit beside them. Replace them with a largest collection on each board.

## figure
reroute_boards('0.05in')

## key
First board: replace the reserved s-A-B-t by s-A-t and s-B-t. The change-walk s-B-A-t uses unused sB and At and cancels AB by traversing it backward. Two Start arrows certify the optimum of 2.

Second board is the revised coupled network, with the reserved route s-A-B-C-D-E-t shown thick above. Its maximum is 2, not 3. Two final collections are \{s-A-C-D-t, s-B-C-E-t\} and \{s-A-C-E-t, s-B-C-D-t\}. No third can leave Start.

## hints
First ask whether both arrows leaving Start could be used. Then ask which reservation prevents the other approach from continuing. If that repair still leaves only one route, inspect the other half. Do not call a backward change-step a legal final route arrow.
