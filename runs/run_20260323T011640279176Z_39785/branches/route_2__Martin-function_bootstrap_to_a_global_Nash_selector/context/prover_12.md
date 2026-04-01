# Prover Output (L4*-block attempt)

Generated: 2026-03-26T03:55:00.000000+00:00

Cannot certify a full proof of L4*-block from the imported hypotheses.

## Key results

[DERIVED] Summable leakage schedule is easy (not the issue).

[DERIVED] Challenge A (product actions) is not the fatal point — behavioral strategies are automatically product-mixed stagewise.

[DERIVED] Clean reduction: L4*-block is equivalent to finding a selector beta(z) in W*(z) such that the finite block game B_t(h,b;beta) has a behavioral equilibrium with payoff within 1/(4L_t) of w^s.

Block IC follows automatically from Nash equilibrium of the block game.

[GAP] The whole content of L4*-block reduces to:
For every (t,h,b), there exists beta(z) in W*(z) such that d_infinity(w^s, E_t(h,b)) <= 1/(4L_t),
where E_t(h,b) = union over all admissible beta of {equilibrium payoffs of B_t(h,b;beta)}.

This is a SELF-GENERATION theorem for W* under block decomposition, and it is not supplied by L1-L2.

[GAP] The "intended play + grim trigger" proof does not close because:
1. Long-run achievability of b does not imply that truncating to L stages yields a selector beta(z) in W*(z) matching the bias drift
2. Grim-trigger punishment requires continuation vectors (e.g., minimax) to lie in W*(z), which is not guaranteed

[SCOPE] The exact obstruction is the absence of a theorem that turns the static compact family W*(·) into a dynamically self-generating continuation selector for the block game.
