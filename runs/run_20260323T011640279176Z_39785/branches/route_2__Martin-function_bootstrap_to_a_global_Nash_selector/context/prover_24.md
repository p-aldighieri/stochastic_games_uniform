# Prover Output (4-Player Absorbing Games with Public Randomization)

Generated: 2026-03-27T09:30:00.000000+00:00

## VERDICT: Kakutani on blocked correspondences FAILS in 4-player absorbing case

Concrete 4-player absorbing counterexample constructed where the blocked compensation polytope for punishing player 1 is EMPTY even with public randomization.

The issue: punitive half-space for player 1 and blocker half-spaces for players 2,3,4 do not intersect. Public randomization convexifies payoffs but cannot create informational asymmetry needed for compensation (unlike Solan-Vohra's private signals).

## Literature confirmed
- 2-player absorbing: solved (Solan)
- 3-player absorbing: solved
- 4+ player absorbing Nash: OPEN (this is confirmed by 2025 Solan-Vieille paper)
- Correlated/mediator devices: broader positive results exist but use private signals, not public randomization

## Next target
Characterize exactly when the blocked compensation LPs B_i^epsilon(alpha_i) ≠ empty. In absorbing games this is a finite-dimensional payoff-geometry problem.
