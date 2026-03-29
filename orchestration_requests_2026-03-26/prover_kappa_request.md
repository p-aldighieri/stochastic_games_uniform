# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-27T00:30:00.000000+00:00

## Instructions

You are the prover role. This is the FINAL ATTACK on Neyman's open problem. The conditional theorem (H1+H2+H3 => uniform equilibrium) has PASS from the reviewer. The remaining gap is (H3): proving kappa_i(s,a_i) <= 0 for gain-neutral actions.

Previous investigation (Prover 20) showed:
- Mertens' known results don't give (H3) for multiplayer
- Smoothness of the branch makes kappa_i finite but doesn't control its sign
- phi_i <= kappa_i is all the Bellman expansion gives

## The Exact Remaining Question

For a convergent analytic branch of discounted Nash equilibria x_lambda -> x*, with normalized payoffs w_i^lambda(s) = lambda * v_i^lambda(s) = g_i(s) + lambda * b_i(s) + O(lambda^2):

kappa_i(s, a_i) = lim_{lambda->0} [g_i(s) - sum_{s'} P^{a_i,lambda}(s,s') g_i(s')] / lambda

Must we have kappa_i(s, a_i) <= 0 when d_i(s, a_i) = 0?

## THREE NEW ANGLES TO TRY

### Angle 1: Coupled First-Order Nash System

Previous passes treated each player's kappa_i in isolation. But kappa_i depends on how the OPPONENTS' strategies x_{-i}^lambda change at first order. In Nash equilibrium, ALL players' first-order strategy changes are simultaneously determined by the coupled system of Bellman equations.

Write x_i^lambda(s) = x_i*(s) + lambda * y_i(s) + O(lambda^2) for the first-order perturbation. Then kappa_i depends on y_{-i} (the opponents' perturbation vectors). But y_{-i} are determined by the OTHER players' Bellman equalities on THEIR support actions.

Question: Does the coupled system of first-order Nash conditions force kappa_i <= 0? This is a LINEAR ALGEBRA question about the first-order perturbation system.

### Angle 2: Branch Selection Freedom

Semi-algebraic selection gives multiple possible branches. Maybe (H3) fails on some branches but holds on others. If we can SELECT a branch where kappa_i <= 0, that suffices.

The equilibrium correspondence E_lambda is semi-algebraic. As lambda -> 0, there may be multiple limit points x*. Perhaps the ones that satisfy (H3) are precisely the ones that arise as limits of "well-behaved" branches (e.g., interior equilibria that stay totally mixed, or equilibria selected by trembling-hand perfection).

### Angle 3: Normalized Bellman at Order 1

On an ANALYTIC branch, expand the normalized Bellman equation w^lambda = T_lambda(w^lambda) to first order in lambda. At order 0: g = T_0(g) gives the gain. At order 1: b = T_0'(g,b) + T_1(g) where T_0' is the derivative of the gain-level operator and T_1 is the direct lambda-correction.

For the Nash case, T_lambda involves the opponents' mixed actions. The order-1 expansion gives a LINEAR system for the biases b_i(s). If this linear system has a unique solution (generically true), then phi_i = 0 on support and phi_i <= 0 off support — i.e., (H3) — follows from the expansion being consistent with Nash optimality at second order.

This is the most promising angle: the STRUCTURE of the first-order expansion of the Nash Bellman system may force (H3) automatically on analytic branches.

## What to Produce

A rigorous proof that (H3) holds on analytic discounted Nash equilibrium branches, OR a precise counterexample showing it can fail.

If the proof works on analytic branches, note that:
- Analytic branches exist generically (Herings-Peeters, implicit function theorem at regular points)
- The game is finite, so there are only finitely many branches
- At least one branch must have a limit point (compactness)
- If ALL analytic branches satisfy (H3), combined with (H1) and (H2) on analytic branches, the theorem follows

This is the endgame. Give it everything.
