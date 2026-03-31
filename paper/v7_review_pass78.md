# v7 Review — Pass 78

**Thinking**: 27 min 54s Extended Pro
**Verdict**: FAIL (but first-exit fix confirmed working)

## What PASSES
- Block payoff uses actual tau_B: CONFIRMED FIXED
- Convex domain, augmented kernel, routing: all preserved
- Bibliography: complete

## Remaining blocker: restart-bias term

When integrating Bellman equalities against bookkeeping occupation, extra term appears:
g* = sum mu* u + sum beta* v - sum (R_C beta*)(xi') h*(xi')

The last term vanishes ONLY if rho_C restarts at zero-bias state.

## Fix
Since h(xi_0)=0 (reference-coordinate normalization) and rho_C is a FREE bookkeeping choice (not part of executed dynamics), DEFINE rho_C = delta_{xi_0} (point mass at reference state). Then (R_C beta*)(xi') h*(xi') = beta_total * h*(xi_0) = 0.
