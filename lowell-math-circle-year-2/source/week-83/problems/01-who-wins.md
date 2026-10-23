+++
id = "w83.who-wins"
title = "Play each board with each starter"
grades = ["2-5"]
route = "first"
page = "same"
kernel = "Some boards are won by one colour whoever starts, and some by whoever moves second."
+++

## text
\renewcommand{\prompty}{98}

## prompt
Play each board with Blue starting, then with Red starting. On which boards can one color always win?

## text
\case{1}{77}{A}\ground{1}{18}{38}\stalk{15}{18}{B}
\case{47}{77}{B}\ground{47}{18}{38}\stalk{61}{18}{R}
\case{93}{77}{C}\ground{93}{18}{38}\stalk{101}{18}{B}\stalk{120}{18}{R}
\case{139}{77}{D}\ground{139}{18}{38}\stalk{147}{18}{B,B}\stalk{166}{18}{R}
\end{sheet}
