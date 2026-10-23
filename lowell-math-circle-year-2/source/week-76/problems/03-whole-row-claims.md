+++
id = "w76.whole-row-claims"
title = "Which claimed whole rows are right?"
grades = ["3-5"]
route = "first"
page = "new"
kernel = "Undoing a whole row must reach a single A; a pair AA or BB at any level rules the claim out."
+++

## text
\promptat{0}

## prompt
Undo a replacement by turning each pair AB into A and each pair BA into B.

## text
\Label{25}{28}{new row}
\Label{92}{28}{pairs}
\Label{157}{28}{old row}
\Strip{4}{32}{B,A,A,B,B,A}{7}
\Arrow{50}{35.5}{59}{35.5}
\Strip{64}{32}{B,A}{8}
\Strip{84}{32}{A,B}{8}
\Strip{104}{32}{B,A}{8}
\Arrow{126}{36}{138}{36}
\Strip{145}{32}{B,A,B}{8}
\Text{0}{54}{182}{Each row below claims to be a whole row grown from a single A. Which claims can be right? Keep a record that settles each decision.}
\Strip{5}{83}{A,B,B,A,B,A,A,B}{8}
\Strip{5}{122}{A,B,B,A,A,B,B,A}{8}
\Strip{5}{161}{A,B,B,A,B,B,A,B}{8}
\Strip{5}{200}{A,B,B,A,B,A,A,B,A,B,B,A,B,A,A,B}{8}
