+++
id = "w10.k1-check-or-x"
title = "Can you pick up every counter?"
grades = ["K-1"]
route = "first"
page = "new"
+++

## prompt
Can you pick up every counter? Put a check in the box if you can and an X if you cannot.

## figure
figs([[k1_town(3, claw('k3a'), below='box'), k1_town(3, rotate(triple('k3b'), 90), below='box')]],
     [[k1_town(3, lollipop('k3c'), below='box')]],
     [[k1_town(3, theta_square('k3d'), below='side')]],
     [[k1_town(3, k4('k3e'), below='side')]], align='bottom')
