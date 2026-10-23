+++
id = "w100.number-world"
title = "The eight-number world"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "Cards 0-7 with distances 8, 4, 2 by parity and remainders mod 4 form a nested world (a scaled 2-adic distance)."
+++

## text
% Page 7: late number continuation; exact restricted 2-adic convention.

## prompt
Use the number cards 0--7. Each card has distance 0 from itself. The distances between different cards follow these rules:

## text
\txt{5}{18}{242}{$\bullet$ One card is even and the other is odd: distance 8.\\
$\bullet$ Both are even or both are odd, with different remainders after division by 4: distance 4.\\
$\bullet$ They have the same remainder after division by 4: distance 2.}
% Complete non-task convention conversion: input, remainder grouping, output.
\txt{0}{42}{250}{For cards 1 and 5, both leave remainder 1 when divided by 4. They belong to the same remainder group, so their distance is 2.}
\txt{0}{54}{250}{Build a world of loops with exactly these distances. Find every different ball of radius 3 and every different ball of radius 5.}
\draw[black!25,rounded corners=2mm] (0,65) rectangle (250,108);
