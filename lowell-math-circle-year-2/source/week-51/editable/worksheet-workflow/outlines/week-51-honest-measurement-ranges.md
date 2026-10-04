Week 51: Measuring with honest ranges

Mathematical kernels

1. If an unknown length a is guaranteed to lie between L and U and another independent-in-the-logical-sense length b between V and W, then a+b lies between L+V and U+W, and a−b lies between L−W and U−V. Independence of probability is not assumed; these are deterministic bounds on all admissible values. For freely variable inputs, each endpoint is attainable. Example: strips of lengths 4–6 units and 3–4 units have an end-to-end length in 7–10 units. A long strip 13–15 units minus a shorter one 10–12 units leaves a gap in 1–5 units. The interval width exposes lost precision, not a chance distribution.

2. Repeated use of the same unknown quantity is different from two separately varying quantities. If a ribbon has length 4–6, its length minus itself is exactly zero, although treating the two appearances as unrelated gives the safe but loose bound −2 to 2. This dependency issue is central in interval arithmetic. Children can model it by aligning or removing shared physical pieces; no negative-number arithmetic is required for the entry. A needed visual example shows a shaded allowed-length band, a single hidden endpoint somewhere in it, and the resulting range for joined strips. Never claim every position in a range is equally likely, or infer a guaranteed measurement error solely from a ruler's tick spacing.

Sources: NIST Digital Library of Mathematical Functions, §3.1(v), interval arithmetic: https://dlmf.nist.gov/3.1. Vladik Kreinovich, UTEP Interval Computations course description, bounded-error interpretation: https://www.cs.utep.edu/vladik/cs5351.21/syllabus.html. The integer strip cases are independently derived. This is distinct from atlas AP-05's random confidence-coverage mechanism and GA-13's minimax curve fit.

Suggested emphasis by level:

K–1: compare hidden strip ends within pictured ranges and build shortest/longest possibilities physically.
Grades 2–3: design guaranteed reach/fit claims for joined strips and give examples that defeat stronger claims.
Grades 4–5: propagate sum/difference bounds and investigate why using the same uncertain piece twice changes the answer.

Materials

Each child: a 0–16 number-line board at 10 mm per unit, at least four sliding paper strips in opaque sleeves with exposed start marks, movable lower/upper endpoint clips, and blank range cards. Ten kits; sleeved strips can be reusable cardstock. For exact mathematical tasks the sleeve card states a guaranteed range; real ruler measurements are only motivation unless an error bound is explicitly given. Pairwise end-to-end joining must mean no overlap. Large printed interval bands should be manipulable without formal bracket notation. Avoid turning this into repeated endpoint arithmetic; retain construction, adversarial counterexamples and shared-piece dependency as the play.
