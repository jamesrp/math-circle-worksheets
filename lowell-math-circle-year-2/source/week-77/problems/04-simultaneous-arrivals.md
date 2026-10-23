+++
id = "w77.simultaneous-arrivals"
title = "Move one addition to see two holes"
grades = ["4-5"]
route = "first"
page = "new"
kernel = "An edge and a tile added at one stage can hide a moment with two holes; exactly two legal one-item moves reveal it."
+++

## text
\promptat{0}

## prompt
Build this schedule. Stage 4 is one step: place its edge, then its tile, and check only after both are in place. Does it ever have two holes at a finished stage? Move exactly one of those two additions to stage 3 or 5 so that it does. Find every legal change. Keep all other additions at their original stages.

## text
\squareboard{10.6}{5.3}{1}
\smallat{0.5}{5.15}{7.8}{Stage 0: AB, BC, CD}
\smallat{0.5}{6.55}{7.8}{Stage 2: DA}
\smallat{0.5}{7.95}{7.8}{Stage 4: AC and filled ABC}
\smallat{0.5}{9.35}{7.8}{Stage 8: filled ACD}
\lineat{0}{12.9}{18.2}\lineat{0}{14.2}{18.2}
