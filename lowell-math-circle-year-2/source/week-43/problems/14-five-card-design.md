+++
id = "w43.five-card-design"
title = "Design a fair five-card shuffle"
grades = ["4-5"]
route = "return"
page = "same"
kernel = 'Ticket sets \{1,2,3,4,5\}, \{2,3,4,5\}, \{3,4,5\}, \{4,5\} give 120 equally likely stories, one per order.'
+++

## prompt @13
Design a fair five-card version on paper with exactly one story for each final order. Specify the ticket sets and resets; how many equally likely stories does your rule have?

## figure
five_card_design()

## key
Use sets \{1,2,3,4,5\}, \{2,3,4,5\}, \{3,4,5\}, \{4,5\} for swaps of slots 1, 2, 3, 4 respectively, then leave slot 5. Reset the cup to the prescribed set before each choice and reset the full procedure for each new shuffle. With uniform fresh choices, $5 \times 4 \times 3 \times 2 = 120$ histories have equal probability. The same unique-target construction proves one story per order, hence probability 1/120 for each.
