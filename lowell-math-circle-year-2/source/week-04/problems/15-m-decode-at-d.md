+++
id = "w04.m-decode-at-d"
title = "The wheel: decode five codes at D"
grades = ["2-3", "2-5"]
route = "first"
page = "new"
+++

## prompt
Cut out the two wheels on the last two pages and join them through the middle dots with a brass fastener. Setting the wheel to D means turning it until the inner A is next to the outer D. Each letter of a message on the inner wheel goes into code as the outer letter next to it, so with the wheel set to D, CAT goes into code as FDW. Set your wheel to D and find what each of these codes came from.

## prompt [2-5]
Cut out the two wheels on the last two pages, put the small wheel on top of the big one, and join them through the middle dots with a brass fastener. Setting the wheel to D means turning it until the inner A is next to the outer D, so every letter moves 3 places. With the wheel set to D, CAT goes into code as FDW, and FDW comes back to CAT. Set your wheel to D and find what each of these codes came from.

## figure
parts(*[code_block(enc(w, 3), before='0.25in' if w == "STAR" else '0.2in')
        for w in ["STAR", "FOX", "WHEEL", "PENCIL", "I CAN DRAW A STAR"]])

## text
\vspace{0.4in}
