+++
id = "w12.legal-pairing-codes"
title = "Which letter strings are pairing codes?"
grades = ["2-3"]
route = ["first", "return"]
kernel = "A U/D string is a pairing code exactly when its height never goes below zero and ends at zero; the two failures are a D with no open U and U's left open."
+++

## prompt
Which strings of letters can be codes for pairings of eight dots? Draw the pairing whenever it is possible, and explain what goes wrong whenever it is impossible.

## figure
pairing_codes()

## key
\emph{Print guide, p. 5.} UUUDDUDD is valid: 18|25|34|67. UDDUUDUD is invalid: after its third letter the height is -1, so a closing endpoint has no opening partner. UUDUDUDD is valid: 18|23|45|67. UUUUDDUD is invalid: five U and three D leave height 2 and two unmatched openings.
