# Prover Output (Final Attack on Neyman — kappa_i counterexample)

Generated: 2026-03-27T05:00:00.000000+00:00

## VERDICT: (H3) IS FALSE IN GENERAL

Concrete counterexample: 2-player game, 1 nonabsorbing state, 3x2 actions, 6 absorbing states.
Unique analytic discounted Nash branch for all lambda. Player 1's action M is gain-neutral (d_1=0) but kappa_1(s,M) = 1/4 > 0.

All three angles fail:
1. Coupled first-order Nash: linearized system is fully explicit, still yields kappa > 0
2. Branch selection: equilibrium is UNIQUE, no alternative branch exists
3. Normalized Bellman order 1: branch is analytic with clean bias, kappa still wrong sign

## Consequence
- The conditional theorem (H1+H2+H3) is correct but H3 is genuinely false
- The lexicographic gain-bias route CANNOT close Neyman's problem
- H3 must be "replaced, weakened, or bypassed by a different route"
