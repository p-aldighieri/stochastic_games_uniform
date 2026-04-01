# Prover Output (H3 via Mertens / Homotopy Investigation)

Generated: 2026-03-27T00:00:00.000000+00:00

## Verdict: (H3) NOT established in existing literature

Mertens' known non-zero-sum results do NOT yield (H3). The homotopy literature does NOT repair the gap.

## Key finding: kappa_i is the precise obstruction

For gain-neutral actions (d_i = 0), the Bellman inequality gives:
phi_i(s, a_i) <= kappa_i(s, a_i)

where kappa_i = lim_{lambda->0} [g_i(s) - sum P^{a_i,lambda}(s,s') g_i(s')] / lambda

(H3) requires kappa_i <= 0. Smoothness of the branch makes kappa_i FINITE but does NOT force it <= 0.

## Literature check
- Mertens-Parthasarathy: existence of discounted subgame-perfect equilibria only
- Mertens Handbook chapter: zero-sum value theory, "approaches" non-zero-sum
- Sorin 1986: only that discounted equilibrium payoffs have limit points
- Herings-Peeters: differentiable homotopy gives local regularity, not sign control
- Doraszelski-Escobar: generic regularity, but kappa_i sign still unresolved

## What would close the gap
Either:
1. Mertens-type theorem for multiplayer: discounted limit is lexicographically optimal at level 2
2. Branch theorem: first-order flatness d_lambda = o(lambda) on gain-neutral actions

Both remain open.
