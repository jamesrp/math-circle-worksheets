+++
id = "w11.order-proof"
title = "Why every order gives the same piles and counts"
grades = ["4-5"]
route = "return"
kernel = "No legal run can be the first to exceed a finished run's share quota at a circle, so every complete run has the same share counts and hence the same final piles."
+++

## prompt
Start with 8 chips at B and none at A or C. Find two different orders that finish. Explain why every order must give the same final piles and sharing counts, for this start and for any other start on this board.

## figure
order_proof_board()

## key
From $(0,8,0)$, the unique finish is $(1,0,1)$, with counts $(3,7,3)$ and 6 chips in the sink. Two full legal words are BBABBABCCBACB and BBCBBCBAABCAB. Each has 13 moves. They exchange A and C choices.

\textbf{Why the share counts must agree.} Fix one finished legal history, with $u_v$ shares at each circle $v$. Imagine another legal history, and suppose it is about to be the first to exceed one of those quotas, at $v$. So far, $v$ has shared exactly $u_v$ times, and every neighbor has shared no more than its quota. Thus $v$ has received no more chips than in the finished history and has sent exactly as many. Its present pile is at most its pile in that stable finish. It cannot legally share. This contradiction says no quota can be exceeded. If the other history also finishes, reverse the comparison; all quotas are equal. Equal counts determine equal final piles.

\textbf{Child-facing proof conversation.} Write the quotas 3,7,3 beside the sample board. Ask, ``Could a different run be the first to make A share a fourth time? Before that happens, could A have received more chips than in our finished run?'' Then discuss the same question for B and C. A careful explanation of that comparison is enough; symbolic notation is optional.
