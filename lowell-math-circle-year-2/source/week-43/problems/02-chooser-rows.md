+++
id = "w43.chooser-rows"
title = "Every row the chooser can make"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "Each order has exactly one first-two draw story, of probability (1/3)(1/2) = 1/6, so the chooser is fair."
+++

## prompt @6 [K-1]
Each row starts with the card drawn first. Find every row that can still happen. Could two different first-two draws make the same row?

## prompt @6 [2-3]
Find every possible final row. Could the chooser give any row more chance than another? Use the possible choices to decide.

## prompt @6 [4-5]
Does this chooser give every order of A, B, C the same chance? Settle the question using every possible choice story.

## figure [K-1]
k1_first_card_rows()

## figure [2-3]
chooser_answer_rows(2.6)

## figure [4-5]
chooser_answer_rows(2.5)

## key [K-1]
Each displayed card is the card drawn first. If \textbf{A} is first, the rows are ABC and ACB; if \textbf{B} is first, BAC and BCA; if \textbf{C} is first, CAB and CBA. Two different first-two draws cannot make the same row because that row displays both draws in its first two positions.

## key [2-3]
ABC, ACB, BAC, BCA, CAB, CBA each has one first-two draw story: AB, AC, BA, BC, CA, CB respectively. Every story has probability $1/3 \times 1/2 = 1/6$. Therefore none is favored. This proof is about all possible choices, not six observed runs.

## key [4-5]
Direct-choice stories AB, AC, BA, BC, CA, CB produce ABC, ACB, BAC, BCA, CAB, CBA. Each story has probability 1/6.
