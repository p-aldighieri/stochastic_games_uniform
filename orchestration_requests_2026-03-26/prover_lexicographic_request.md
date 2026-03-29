# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T08:35:00.000000+00:00

## Instructions

You are the prover role. This is the deepest attempt yet on Neyman's open problem. The previous 7 prover passes have progressively identified the EXACT mathematical structure needed:

1. One-step W* selector: FALSE (PD counterexample)
2. Block W* selector: self-generation gap
3. Block full-W selector: achievability != equilibrium
4. Bounded APS: FALSE (additive recursion escapes bounded sets)
5. Gain-bias APS via discounted limits: discounted equilibria give LEXICOGRAPHIC control, not scalar block IC

The key insight from Prover 15: discounted equilibria naturally provide lexicographic gain-bias control:
- Gain level: deviations cannot increase expected continuation gain (g is a supermartingale under deviation)
- Bias level: CONDITIONAL on gain being preserved, deviations cannot improve bias-adjusted block payoff

This is the Mertens-Neyman structure. Your task: prove uniform epsilon-equilibrium existence using LEXICOGRAPHIC gain-bias block construction.

## The Theorem Target (unchanged)

For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist sigma and T_0 such that sigma is a uniform epsilon-equilibrium for all T >= T_0.

## The Lexicographic Architecture

### The discounted input (known)

For every lambda in (0,1), there exists a stationary Nash equilibrium x_lambda of the lambda-discounted game. The discounted payoff v_i^lambda(s) satisfies:

v_i^lambda(s) >= u_i(s, y_i, x_{-i}^lambda(s)) + (1-lambda) E[v_i^lambda(s')] for all deviations y_i.

As lambda -> 0 along a semi-algebraic branch:
- g_i(s) = lambda * v_i^lambda(s) -> limit (the gain)
- b_i(s) = v_i^lambda(s) - g_i(s)/lambda -> limit (the bias, after normalization)

### The lexicographic block IC (from Prover 15's calculation)

For an L-stage block starting at state s under discounted equilibrium play:

**Gain level**: g_i(s) >= E[g_i(s_{L+1})] under any within-block deviation (g is a supermartingale)

**Bias level**: When g_i(s) = E[g_i(s_{L+1})] (gain-preserving deviation):
L*g_i(s) + b_i(s) >= E[sum u_i + b_i(s_{L+1})] - eta_L

The storm-cloud term (1/lambda - 1)(g_i(s) - E[g_i(s_{L+1})]) VANISHES for gain-preserving deviations.

### Why this should close the theorem

**Key insight**: A deviation that burns future gain is ALREADY punished by the gain-supermartingale property. Over T stages, the total gain lost is at most g_i(s_1) - E[g_i(s_{T+1})] <= max g - min g = O(1). So gain-burning deviations contribute at most O(1/T) to the average regret, which vanishes.

The only "dangerous" deviations are gain-PRESERVING ones. For those, the bias-level block IC applies, and the leakage is O(1/L) — summable.

### Proof sketch

1. **Discounted equilibria exist** (Fink-Takahashi): stationary x_lambda for each lambda.

2. **Gain-bias limits exist**: Along a semi-algebraic branch, g(s) and b(s) are well-defined for all states.

3. **Gain supermartingale under deviation**: From discounted Nash, g_i(s) >= E_deviation[g_i(s')] in the limit. This means any deviation either preserves or lowers continuation gain.

4. **Bias-level block IC for gain-preserving deviations**: For deviations with g_i(s) = E[g_i(s_{L+1})], the storm-cloud term vanishes and the bias inequality holds with leakage O(1/L) + o(1).

5. **Construct the block policy**: Use x_lambda(s) (the discounted stationary strategy) as the within-block policy. This is product (uncorrelated) by construction.

6. **Decompose T-horizon regret**: Split any deviation tau_i into:
   - Gain-burning component: contributes <= O(1/T) to average regret (bounded total gain loss)
   - Gain-preserving component: controlled by bias-level block IC with summable leakage

7. **Choose lambda = lambda(L) jointly**: Set lambda ~ 1/L^2 so that both the discounted approximation error and the block leakage are O(1/L).

8. **Telescope across blocks**: The bias terms telescope as before (verified conditional tail). The gain terms are bounded.

## What Needs to Be Made Rigorous

A. **Does the gain supermartingale property hold in the limit?** The discounted game gives g_i(s) >= (1-lambda) E[g_i(s')] under deviation, which converges to g_i(s) >= E[g_i(s')] as lambda -> 0. But does this limit hold uniformly over deviations?

B. **Is the gain-preserving deviation set well-structured?** Can we decompose an arbitrary deviation into gain-burning and gain-preserving components? Or is this decomposition only meaningful at the one-step level?

C. **Does the stationary discounted strategy work as a block policy?** Using x_lambda as the block policy requires that it approximately satisfies the block equations for the undiscounted game. This is where the lambda = lambda(L) choice matters.

D. **Multiplayer coordination**: With multiple players, the gain supermartingale must hold simultaneously for all players. Are there deviations where one player's gain drops but another's rises?

## What a Complete Answer Looks Like

A rigorous proof that the lexicographic decomposition (gain supermartingale + bias block IC for gain-preserving deviations) yields uniform epsilon-equilibria. OR the exact point where even this decomposition fails, with a concrete obstruction.

This is the most promising approach yet. The lexicographic structure naturally matches what discounted equilibria provide, and the gain-burning/gain-preserving decomposition of deviations is the key new idea.
