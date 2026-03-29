# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T22:30:00.000000+00:00

## Instructions

You are the prover role. The conditional theorem (H1+H2+H3 => uniform equilibrium) is now PASS-verified. The remaining upstream gaps are (H2) bounded bias and (H3) neutral-action flatness. This pass focuses on (H3).

## The Exact Condition (H3)

For every player i, state s, and pure action a_i:
- d_i(s,a_i) := g_i(s) - sum_{s'} P^{a_i,*}(s,s') g_i(s') >= 0 (gain drop, proved from discounted Nash)
- phi_i(s,a_i) := u_i^{a_i,*}(s) + sum_{s'} P^{a_i,*}(s,s') b_i(s') - b_i(s) - g_i(s) (bias surplus)

(H3) says: if d_i(s,a_i) = 0, then phi_i(s,a_i) <= 0. If a_i in supp(x_i*(s)), then phi_i(s,a_i) = 0.

## Why (H3) Doesn't Follow from (H1)+(H2)

The reviewer confirmed: from (H1)+(H2), we get d_{i,n}(s,a_i) -> 0 but NOT d_{i,n}/lambda_n -> 0. Without the o(lambda) rate, phi_i's sign is uncontrolled.

## What Would Suffice

ANY of the following would establish (H3):

**Approach A: Show d_{i,n}(s,a_i) = o(lambda_n) for gain-neutral actions.**
If the discounted gain-drop converges to 0 faster than lambda_n, then the bias surplus inequality follows from the discounted Bellman inequality by division. This is an asymptotic rate question about the Puiseux expansion.

**Approach B: Use the structure of Nash equilibrium at lambda = 0.**
At the limit, x* is a Nash equilibrium of a "gain game" (where payoffs are g_i). The bias inequality phi_i <= 0 on gain-neutral actions would follow if x* is also an equilibrium of a "bias game" on the gain-neutral subgraph. This is related to the lexicographic equilibrium theory of Mertens (1987).

**Approach C: Differentiable homotopy / regular branch selection.**
Herings-Peeters (2004) and Li-Dang-Herings (2023) construct differentiable paths of stationary equilibria. On a differentiable branch, the Puiseux expansion has only integer powers, so:
- v_i^lambda = g_i/lambda + b_i + c_i*lambda + O(lambda^2)  [no fractional exponents]
- This gives d_{i,n} = O(lambda_n) and phi_i = lim (d_{i,n}/lambda_n - Psi_{i,n}) which is well-defined
- The sign of phi_i is then determined by the derivative of the Bellman operator

**Approach D: Mertens' (1987) algebraic approach to stochastic game limits.**
Mertens showed that limits of discounted equilibria in finite stochastic games satisfy a "lexicographic" optimality condition at multiple levels. If the limit x* satisfies Mertens' lexicographic equilibrium conditions, then (H3) follows by definition of the second-level optimality.

## Key Question

Does the Mertens (1987) lexicographic equilibrium theory, applied to multiplayer finite stochastic games, directly give (H3)?

Specifically: Mertens defines a hierarchy of optimality conditions for the limit of discounted equilibria. The first level is gain optimality (d_i >= 0, which we have). The second level is bias optimality conditional on gain neutrality — which IS (H3).

If Mertens' theory applies to multiplayer Nash equilibria (not just zero-sum), then (H3) is already known to hold for limit points of discounted equilibria. Check whether this is the case.

## What to Produce

1. Determine whether Mertens (1987) or subsequent work (Solan, Neyman, Bewley-Kohlberg) establishes that multiplayer discounted Nash equilibrium limits satisfy the second-level lexicographic optimality (= our H3)

2. If yes: state the precise theorem and show it gives (H3). This would close the gap between (H1)+(H2) and the full conditional theorem.

3. If no: identify the exact obstruction and what additional conditions would be needed.
