# Prover Output (Patched Conditional Proof + Puiseux Investigation)

Generated: 2026-03-26T13:30:00.000000+00:00

## Part 1: Sharpened Conditional Theorem

The original (H1)+(H2) are NOT sufficient. Need additional hypothesis:

(H3) If d_i(s,a_i) = 0 (gain-neutral), then phi_i(s,a_i) <= 0.
     If a_i in supp(x_i*(s)), then phi_i(s,a_i) = 0.

Where:
- d_i(s,a_i) = g_i(s) - sum P(s') g_i(s')  [gain drop]
- phi_i(s,a_i) = u_i + sum P(s') b_i(s') - b_i(s) - g_i(s)  [bias surplus]

With (H1)+(H2)+(H3): x* is uniform epsilon-equilibrium with regret O(1/T).
Explicit bound: T_0(epsilon) = max_i ceil((2*B_i + C_i*G_i)/epsilon)

Proof is fully rigorous with all three PATCH_SMALL fixes applied:
(a) One-step deviation inequality from discounted Nash ✓
(b) Finite-gap lemma for C_i with explicit formula ✓  
(c) Multi-step supermartingale via telescoping ✓

## Part 2: Puiseux Investigation

- Datta universality: Nash equilibria realize any algebraic variety → no automatic ban on fractional exponents
- Regular branches: analytic in lambda, bounded bias → (H2) holds generically
- BUT analyticity alone doesn't give (H3): first-order opponent drift can leak into neutral-action inequality

## The PRECISE remaining gap (final refinement):

Find a stationary equilibrium selector near lambda=0 whose neutral one-step deviation gaps are o(lambda), yielding (H3) automatically.

This is sharper than "ban fractional exponents" or "bounded bias."
