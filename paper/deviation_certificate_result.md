# Deviation Certificate — Pass 59

**Pass**: 59
**Role**: Prover
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 27m 32s

## VERDICT: Bare continuity NOT sufficient; Bellman-stability version IS sufficient with enriched package

### What works
A corrected Bellman-stability argument gives explicit modulus:
|g_C^{m,dev}(u_C;x) - g*| ≤ eta_r + H/2 * eta_Q + H/m

where eta_r = reward convergence, eta_Q = transition convergence, m = block length.

### What the current package lacks
(mu_C, L(mu_C), g_C, w_C) is TOO SMALL to certify incentives. Must add:

1. **Full unilateral reward-kernel family**: (r_i(x,a_i), Q_i(·|x,a_i)) for each player i, each state x, each action a_i — on the exit-tag augmented phase-state space

2. **Bounded-span Bellman pair**: (g*, w*) for each deviator's MDP with ||w*||_span bounded

3. **Uniform realization of unilateral kernels**: not just aggregate compliant occupation

### What this means
- The metastable tree object (Section 3) needs to carry MORE data per node
- The compactification must include deviator-specific transition data
- This is a DESIGN change, not just a proof gap
- Once the enriched package is in place, the deviation certificate is a telescoping argument

### Precise remaining gap
"Can we build a compact tree space that carries enough deviator data to run the Bellman certificate, while remaining compact and supporting the Kakutani argument?"

This is the sharpest formulation of the remaining obstacle to Neyman's conjecture achieved in this project.
