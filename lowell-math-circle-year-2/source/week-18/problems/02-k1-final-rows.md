+++
id = "w18.k1-final-rows"
title = "Which pictures could each final row mean?"
grades = ["K-1"]
route = "first"
kernel = "With 000 and 111 every final row means one picture; with 00 and 11 the rows 01 and 10 could mean either."
+++

## prompt
Draw every possible picture beside each final row. Which key lets the changer fool the receiver?

## figure
keyed(.35,2.8,'triangle','000')+keyed(9.7,2.8,'square','111')+''.join(strip(x,y,bits)+line(x+6.6,y+1.6,1.4) for x,y,bits in [(.45,6.05,'000'),(9.8,6.05,'101'),(.45,9.3,'010'),(9.8,9.3,'111')])+keyed(.35,13,'triangle','00')+keyed(9.7,13,'square','11')+''.join(strip(x,y,bits)+line(x+4.65,y+1.6,3.4) for x,y,bits in [(.45,16.25,'00'),(9.8,16.25,'01'),(.45,19.5,'10'),(9.8,19.5,'11')])
