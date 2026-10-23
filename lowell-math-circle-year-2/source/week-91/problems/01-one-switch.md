+++
id = "w91.one-switch"
title = "One switch: arrival orders"
grades = ["2-5"]
route = "first"
page = "same"
kernel = "Every departure flips the next one, so a single switch alternates: XYXY... or YXYX..., never two of one exit in a row."
+++

## prompt @15,123
Use the one-switch board. Choose its first arrow. Send 12 counters through and keep their arrival order. Then start a new trial with the other first arrow.

## figure
strip(15,163,12,15)+strip(15,201,12,15)

## text @15,234 w=186 size=14
Which arrival strings can this switch make: XYXY, XXYY, YXYX, XYYX?
