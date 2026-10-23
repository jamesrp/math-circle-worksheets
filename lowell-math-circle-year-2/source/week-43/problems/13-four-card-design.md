+++
id = "w43.four-card-design"
title = "Design a fair four-card shuffle"
grades = ["4-5"]
route = "return"
kernel = 'Ticket sets \{1,2,3,4\}, \{2,3,4\}, \{3,4\} give $4 \times 3 \times 2 = 24$ equally likely stories, exactly one per order.'
+++

## prompt @0
Design a four-card ticket-and-swap shuffle on paper that gives every order the same chance, with exactly one choice story per order. Explain why it meets both goals.

## figure
four_card_design()

## key
For ABCD, swap slot 1 with a uniform ticket from \{1,2,3,4\}; swap slot 2 with a uniform ticket from \{2,3,4\}; swap slot 3 with a uniform ticket from \{3,4\}. Leave slot 4. Permit self-swaps. At each stage empty the cup and use exactly the indicated ticket set; for a new full shuffle reset the starting row and all ticket sets. There are $4 \times 3 \times 2 = 24$ equally likely stories.

## key
A target order uniquely specifies the ticket at each step: locate the target first card, swap it into slot 1, then locate the target second card in the suffix, then the third. Later steps cannot disturb a settled slot. Consequently each of the 24 orders has exactly one story, of probability 1/24.

## key
Other designs pass too. Keeping the swaps of slot 1, then 2, then 3, exactly six choices of ticket sets give one story per order, one for each order of the set sizes 4, 3, 2; for example \{1,4\}, \{1,2,4\}, \{1,2,3,4\}.