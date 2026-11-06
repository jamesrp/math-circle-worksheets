+++
id = "w22.shared-location"
title = "Two labels at one point"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "With A and D at one point, four splits work (A | BCD, AB | CD, AC | BD, ABC | D); a split always exists, since the shared point alone against the rest meets it."
+++

## prompt
A and D share a location. Find every split whose regions meet. Does a successful split always exist when two of four labels share a location? Explain.

## figure
board([('A, D',3,3,'below=6pt'),('B',10,4.5,'right=6pt'),('C',5.5,10,'above=6pt')])

## text
\recordlines{2}

\newpage

## prompt
A and D share a location. Find every split whose regions meet. Does a successful split always exist when two of four labels share a location? Explain.

## figure
repeated([('A, D',3,3,'below=6pt'),('B',10,4.5,'right=6pt'),('C',5.5,10,'above=6pt')])
