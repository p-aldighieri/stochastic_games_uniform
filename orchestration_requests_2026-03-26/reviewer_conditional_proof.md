# External Agent Request (reviewer + prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T09:35:00.000000+00:00

## Instructions

You have TWO tasks in this request:

### Task 1: REVIEW the conditional proof

A conditional theorem was proved in the previous pass (Prover 16). Verify every step:

**Claim**: If discounted Nash equilibria x_{lambda_n} converge to x* with bounded bias expansion v_i^{lambda_n}(s) = g_i(s)/lambda_n + b_i(s) + o(1), then x* is a uniform epsilon-equilibrium with regret O(1/T).

**Proof steps to verify**:
1. Gain inequality: g(s) >= Q*(s,a_i)g for all deviations (from discounted Nash, limit)
2. Bias inequality on gain-preserving actions (when gain drop = 0)
3. Support equality (actions in support of x* satisfy both as equalities)
4. Combined one-step: u_i + Qb <= g + b + C_i*(g - Qg)
5. Summing: deviation payoff <= Tg(s1) + osc(b) + C_i*osc(g)
6. On-path: payoff = Tg(s1) + b(s1) - E[b(s_{T+1})] >= Tg(s1) - osc(b)
7. Final regret bound: O(1/T)

Issue a VERDICT: PASS, PATCH_SMALL, PATCH_BIG, or REDO.

### Task 2: INVESTIGATE bias boundedness

The exact remaining question: does the discounted equilibrium branch have bounded bias?

**What is known**:
- Fink-Takahashi: stationary discounted Nash equilibria exist for all lambda
- Semi-algebraic selection: x_lambda can be chosen along a semi-algebraic branch
- Puiseux series: v_i^lambda(s) has a Puiseux expansion in lambda near 0
- Bewley-Kohlberg (1976): for 2-player zero-sum, the expansion has the form g/lambda + b + o(1) with bounded b

**The question for multiplayer**:
- Does the Puiseux expansion of v_i^lambda(s) along a discounted Nash equilibrium branch have a bounded second term?
- Is this known in the literature? Check recent work by Oliu-Barton, Vigeral, Solan, Ziliotto.
- If the Puiseux expansion is v^lambda = c_{-1}/lambda + c_0 + c_1*lambda^{1/k} + ..., is c_0 necessarily bounded?

This is the ONLY remaining question for the full theorem. If the bias is bounded, the theorem is proved. Search the literature and determine if this is already known.
