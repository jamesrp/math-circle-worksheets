+++
id = "w87.knockout-rules"
title = "Knockout rules and the D/E/F knockout"
kind = "setup"
grades = ["2-5"]
route = "first"
+++

## text @18,29 size=11
A knockout starts with two letters. The winner faces the waiting letter; that vote chooses the final winner. Put each loser in Out. Reset all three letters before a new knockout.

## figure
cards(18, 58, ['DFE', 'EFD', 'FED'], 20, 38, 3) \
+ box(18, 105, 53, 31, r'D vs E: E wins\\D goes to Out', 10) + t(72, 114, r'$\longrightarrow$', 12, 14) \
+ box(86, 105, 47, 31, r'E stays in\\F was waiting', 10) + t(135, 114, r'$\longrightarrow$', 12, 14) \
+ box(148, 105, 50, 31, r'E vs F: F wins\\E goes to Out', 10)
