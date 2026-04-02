# VP3 Reformulation — Pass 56

**Pass**: 56
**Role**: Reviewer + Prover
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 23m 10s

## VERDICT: VP3 IS AUTOMATIC IN LIFTED FORMULATION

### Task 1: Counterexample Review — CONFIRMED
Pass 55 gadget is mathematically sound. Product VP3 genuinely fails (2/32 corners).

### Task 2: Lifted VP3 — PROVED

**Theorem**: J_C = {(mu, L(mu)) : mu in P_C}

**Proof sketch**:
- For each deterministic policy theta, flux(theta) = L(occ(theta)) for fixed linear L
- So J_C = conv{(mu_theta, L(mu_theta))} = {(mu, L(mu)) : mu in P_C} by linearity of L and convexity of P_C
- For any mu in P_C, the compatible flux is UNIQUELY DETERMINED: beta = L(mu)
- And (mu, L(mu)) is automatically in J_C

**Consequence**: The "compatibility gap" disappears completely when occupation and flux are treated jointly.

### Key Insight
- Product VP3 (J_C = P_C x B_C) is FALSE generically
- Graph VP3 (J_C = graph(L) restricted to P_C) is TRUE and AUTOMATIC
- The correct repair: rewrite the theorem using the joint occupation-exit polytope

### Caution
This is a convexified result. The conditional theorem uses Caratheodory decomposition into deterministic policies, so the convex hull property should suffice. But this needs verification that Section 6 (Kakutani argument) only requires the convexified version.

### Implication
If the conditional theorem only needs convexified compatibility (which Kakutani does), then:
**THE CONDITIONAL THEOREM BECOMES UNCONDITIONAL.**
Neyman's conjecture follows from the framework + the graph-VP3 theorem.

This is potentially a complete proof of Neyman's conjecture.
