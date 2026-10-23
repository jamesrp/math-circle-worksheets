+++
id = "w13.fit-routes"
title = "Fit as many routes as you can"
grades = ["K-1", "2-3"]
route = "first"
page = "same"
kernel = "A stuck collection need not be largest: on the greedy board the route through the middle arrow blocks both others, and two routes fit."
+++

## prompt [K-1]
Fit as many routes as you can on each board. Find another way to fit that many routes, if you can.

## prompt [2-3]
On each board, fit as many routes as possible. Find the fewest arrows you can close to stop every route.

## figure [K-1]
k1_fit_routes()

## figure [2-3]
fit_and_close_23()

## key [K-1]
Upper greedy board: maximum 2, uniquely the collection s-A-t and s-B-t. The route s-A-B-t alone is stuck but not largest. Lower bowtie: maximum 2, with exactly two collections: \{s-A-C-D-t, s-B-C-E-t\} or \{s-A-C-E-t, s-B-C-D-t\}. Both may meet at C. Closing sA and sB blocks all travel and certifies 2.

## key [2-3]
Both boards have 2 routes and require 2 closures. Upper bowtie: take s-A-C-D-t and s-B-C-E-t; close \{sA,sB\}. Lower greedy: take s-A-t and s-B-t; close \{sA,sB\}. Page 4 explains the certificate; shared C does not consume capacity.

## hints [K-1]
Hint: can each arrow out of Start serve a different route? If a chosen route blocks another, try changing the first.

## hints [2-3]
Hint: distinguish a dot that is shared from an arrow that is shared.
