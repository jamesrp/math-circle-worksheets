+++
id = "w09.rules"
kind = "setup"
title = "Rules: the ball, its bounces and a 7 by 3 table"
grades = ["2-3", "4-5"]
route = ["first", "return"]
+++

## figure [2-3]
rules_block("""The ball starts at the dot in the bottom left corner of a table and rolls up and to the right, crossing each square from corner to corner. It bounces off every wall it hits and stops when it reaches a corner of the table. Each time the ball hits a wall counts as one bounce; reaching the corner at the end does not count. A 7 by 3 table is 7 squares wide and 3 squares high.

Partners take turns: one predicts where the ball will stop, and the other traces the path.""",
            rule_picture(), textwidth="0.56\\textwidth", picwidth="0.4\\textwidth") + vspace(0.05)

## figure [4-5]
rules_block("""The ball starts at the dot in the bottom left corner of a table and rolls up and to the right, crossing each square from corner to corner. It bounces off every wall it hits and stops when it reaches a corner of the table. Each time the ball hits a wall counts as one bounce; reaching the corner at the end does not count. A 7 by 3 table is 7 squares wide and 3 squares high.

Before one of you traces a path, the others predict where the ball will stop. Then they check the tracing.""",
            rule_picture(), textwidth="0.56\\textwidth", picwidth="0.4\\textwidth") + vspace(0.05)
