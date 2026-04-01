# Prover Output (Lexicographic Gain-Bias — CONDITIONAL PROOF)

Generated: 2026-03-26T09:30:00.000000+00:00

## CONDITIONAL THEOREM (PROVED)

If there exists a sequence lambda_n -> 0 and stationary discounted Nash equilibria x_{lambda_n} such that:
1. x_{lambda_n}(s) -> x*(s) for every state s
2. v_i^{lambda_n}(s) = g_i(s)/lambda_n + b_i(s) + r_{i,n}(s) with r_{i,n} -> 0

Then x* is a stationary uniform epsilon-equilibrium for every epsilon > 0, with regret:

regret_i^T <= (2*osc(b_i) + C_i*osc(g_i)) / T

where C_i = max over gain-burning actions of the bias-to-gain-drop ratio.

## Proof structure
1. Gain inequality: g(s) >= Q*(s,a_i)g — supermartingale under deviation
2. Bias inequality for gain-preserving actions: g(s) + b(s) >= u_i + Q*b
3. Combined one-step: u_i + Qb <= g + b + C_i*(g - Qg)
4. Sum over T: deviation payoff <= Tg(s1) + osc(b) + C_i*osc(g) 
5. On-path: payoff = Tg(s1) + b(s1) - E[b(s_{T+1})] >= Tg(s1) - osc(b)
6. Regret = O(1/T) — DONE

## EXACT REMAINING OBSTRUCTION

Does the discounted equilibrium branch have BOUNDED BIAS? Specifically:
- v_i^lambda(s) - g_i(s)/lambda must remain bounded as lambda -> 0
- Semi-algebraicity alone does not force this
- For 2-player zero-sum: Bewley-Kohlberg (1976) proves it — YES
- For multiplayer: NOT YET CERTIFIED

This is the sharpest possible reduction of Neyman's problem:
OPEN PROBLEM = "Is the bias bounded in the multiplayer discounted limit?"
