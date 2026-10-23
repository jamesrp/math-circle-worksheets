+++
id = "w49.parity"
title = "Even and odd rings"
grades = ["4-5"]
route = "return"
kernel = "Under the even/odd rule every one of the 16 letter rings becomes all E within four moves, so after four moves every height is even."
+++

## prompt @0
Replace even heights by E and odd heights by O. Use this two-letter gap rule. Which letter rings are possible after four moves? Explain why you have checked every kind of start.

## text @5,34 size=12
E and E give E.     O and O give E.\\[\dimexpr10mm-15pt\relax]E and O give O.     O and E give O.

## figure
ring(25,72,['E','O','E','E'],39,8)+line(81,92,104,92,'-{Stealth[length=3mm]}')+ring(123,72,['O','O','E','E'],39,8)+ring(25,170,None,42,9)+ring(123,170,None,42,9)
