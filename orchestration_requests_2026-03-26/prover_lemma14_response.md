# Prover Response: Lemma 14 — D2 Transition-Tilting Linear Response

**Source**: ChatGPT Extended Pro, "Proof of Lemma 14" chat
**Date**: 2026-03-27
**Role**: Prover
**Pass**: 30 (third Route D' pass)
**Chat URL**: https://chatgpt.com/g/g-p-69b78396b3808191ad15bcc609e7ebf6-game-theory-proof/c/69c6ea1f-0520-8329-a83c-33e2c351c022
**Length**: 9,364 characters

## VERDICT: CONDITIONAL

Lemma 14 is valid on a Puiseux branch **under a first-active-order nondegeneracy/separation hypothesis**. Without that hypothesis, the first-order susceptibility tensor Lambda_C is NOT enough.

## Key Findings

### 1. Conditional Proof (VALID under hypothesis)
- On a fixed Puiseux branch, if all exit probabilities share a common first active order q_C(x) and the first coefficients separate D2 directions, the linear-response formula holds exactly
- The affine map Theta_{C,i} correctly captures the leading-order exit effect
- The continuation shift formula sum_e Theta(tau_i)(e) * v_{C,i}(e) is correct at leading order

### 2. Why the Unrestricted Lemma Fails
- **Concrete algebraic obstruction**: When two exits have matching first-order coefficients (Lambda = (1,1) for both actions), the D2 effect lives in the SECOND Puiseux jet, not the first
- First-order data cannot distinguish the deviation from the nominal action
- The continuation-dependent term t*lambda^2 only appears at second order

### 3. Exact Repair: Finite Exit Jet
Replace Lambda_C by a finite exit jet:
```
J_C(x) = ((q_1, Lambda^(1)), (q_2, Lambda^(2)), ..., (q_m, Lambda^(m)))
```
where q_1 < q_2 < ... < q_m are the distinct Puiseux exponents. The first continuation-separating order is the smallest r such that the sum of delta*Lambda^(r) * v_{C,i}(e) is nonzero.

A finite m suffices branchwise (finitely many players, states, actions, finite Puiseux expansions).

### 4. Likelihood Assessment
- For **generic branches**: first-order condition likely holds (ties are codimension phenomena)
- For **all finite stochastic games**: hypothesis likely FALSE — semialgebraic Puiseux geometry naturally allows first-order ties and continuation-weighted cancellations
- **Route D' needs an all-games object**, so the repair is necessary

## Impact on Route D'
- The tree object needs MORE coordinates than originally specified
- Replace Lambda_C with finite exit jet J_C at each node
- Compactness still holds (finite jet, bounded coefficients)
- The breakdown's Lemma 8 (split/merge closure) and Lemma 7 (sequential compactness) need updating to use jets
- Critical path unchanged but Lemma 14 is now RESOLVED modulo jet enlargement

## Next Step Recommendation
- Accept the jet repair and update the tree definition (Def 1.3)
- Move to Lemma 18 (Implementability) — the theorem-sized bottleneck
- The jet enlargement is a coordinate enlargement, not a structural change; compactness should survive
