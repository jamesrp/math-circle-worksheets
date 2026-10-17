# Mathematical notes for the eventual facilitator guide

These notes precede final student revision; align the final guide to the final pages.

## Certain compatibility versus inference

For a closed population of size N, first marked catch M, second distinct catch n and overlap R, the union has M+n−R distinct objects. Thus N≥M+n−R. Conversely any integer N at least this large can realize the record: build R shared objects, M−R first-only, n−R second-only, then arbitrarily many unseen objects. Also 0≤R≤min(M,n); for given N its lower limit is max(0,M+n−N). A finite toy-kit cap or an explicit prior is extra information, not a consequence of overlap.

## Uniform-subset sampling

Conditional on a fixed set of M marked objects, a second catch uniformly chosen among n-subsets gives each marked object chance n/N to appear. Summing M zero-or-one indicators gives E(R)=Mn/N without requiring those indicators to be independent. For exact finite checking, P(R=r)=choose(M,r)choose(N−M,n−r)/choose(N,n). Symmetry of uniform sample subsets explains the individual inclusion probability.

Matching sample marked proportion R/n to population proportion M/N gives the estimate Mn/R for R>0. This is neither an identity nor generally unbiased. Example N=6,M=4,n=3: R=1,2,3 with probabilities 1/5,3/5,1/5; resulting guesses 12,6,4 have expectation 34/5, not 6. R=0 leaves this ratio undefined, while all N≥M+n remain finitely possible. Repeated trials must return every object and erase every mark between complete rounds; keeping the total fixed is essential for comparing variability.

## Design objective

For fixed handling budget s=M+n≤N and positive integer catches, expected overlap is M(s−M)/N. If n≥M+2, moving one unit from n to M changes product by n−M−1>0. Repeating balances the sizes; ties arise only from swapping odd-budget floor/ceiling sizes. This proves maximal expected overlap, not minimal estimation error under every criterion. With N=24, budgets 12,13,20 give splits 6+6,6+7,10+10 and means 3/2,7/4,25/6 respectively.

## Illustrated lower repeat record

The invented six records R=2,1,3,1,2,0 at M=n=4 are all possible under N=8 and N=16. Ordered-record likelihoods under independent resets are 82944/1838265625 and 5635496592/70983656505125 respectively. The second is only about 1.76 times the first. The mean overlap 1.5 lies midway between the two model expectations 2 and 1; that mean alone is not a decisive comparison. Do not put likelihood arithmetic on lower student pages. A reasoned tentative choice of 16 from the pattern of smaller overlaps can be discussed, while recognizing that 8 remains possible; a forced certain answer would be false. The upper repeat record R=1,2,3,2,0 at M=n=6 is compatible with every N≥12, including 18, without any imposed prior.

## Mark loss and experimental controls

For the same second catch, removing marks can only reduce or preserve the observed overlap. A positive ratio estimate then increases or stays fixed; zero makes the ratio unavailable. A direct retention control marks a known count, uses the same handling, then examines the entire known population and counts surviving marks. An intact control on one occasion does not prove future retention or equal catchability; it is evidence about one potential model failure. Uniform mixing, no additions/losses, no tactile selection, retained visible marks, and no within-catch replacement all matter. Shaking a physical bag approximates the ideal uniform-subset assumption rather than proving it.
