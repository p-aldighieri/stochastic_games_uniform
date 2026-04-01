# Prover Output (Gain-Bias APS via Discounted Limits)

Generated: 2026-03-26T08:30:00.000000+00:00

Verdict: Gain-bias IS the right object, but discounted-limit transfer FAILS.

## Key findings
1. Gain-bias confirms as correct Bellman-shaped object for undiscounted games
2. Bewley-Kohlberg only works for 2-player zero-sum, not multiplayer
3. Discounted equilibria give LEXICOGRAPHIC control (gain-first, bias-second), not scalar block IC
4. Uncancelled storm-cloud term: (1/lambda - 1)(g_i(s) - E[g_i(s_{L+1})]) is O(1/lambda), not O(1/L)
5. Solan's Sorin absorbing-game example witnesses that discounted != uniform equilibrium payoffs

## The corrected object: lexicographic gain-bias self-generation
- On path: g_i is martingale, g_i + b_i satisfies average-reward Bellman equality
- Deviation: either lowers continuation gain, OR conditional on preserving gain, cannot improve bias-adjusted block payoff
- This is gain-first, bias-second — matching Mertens-Neyman structure

## Missing bridge
Control deviations that buy current payoff by burning future gain. The g/lambda term drowns the b-scale signal.
