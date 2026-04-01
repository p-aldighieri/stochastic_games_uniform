# Prover Output (APS endogenous self-generation)

Generated: 2026-03-26T07:00:00.000000+00:00

Verdict: No proof. Bounded payoff APS is the WRONG continuation object for undiscounted games.

## Key finding
The largest bounded block-self-generating correspondence V: S -> K([0,1]^N) can be EMPTY even in the trivial all-ones game. The recursion "block average + continuation" is additive, producing an unbounded tower that escapes any bounded set.

## Counterexample
One state, one action, payoff 1 forever. Block IC requires 1 + beta_i <= v_i + eta. Since beta_i >= v_i (from V(s)), we get 1 <= eta. So for any eta < 1, no nonempty V exists.

## The correct object: gain-bias pairs
The repair is to track (g(s), b(s)) where g is the long-run gain and b is the telescoping bias:
L·g_i(s) + b_i(s) >= sup_{tau_i} E[sum u_i + b_i(s_{L+1})] - eta_L

This matches the average-reward Bellman equation and the existing verified telescoping step.

## References identified
- Fudenberg-Yamamoto: "return generation" extends APS to stochastic games
- Solan: warns that lambda->0 limits can fail because state weights change
- Standard average-reward MDP theory uses gain-bias decomposition
