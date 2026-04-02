# Paper v24 Fix — Pass 111

## Pass 110: g-alpha = Z-increment is compliant-only, not deviator-routed

The reviewer says the g-alpha bridge works under the stationary compliant measure but NOT for the deviator's routed path. Prop 2410-2483 is unproved.

## THE FIX: Separate the compliant and deviator arguments completely

For the COMPLIANT profile (lower bound on payoff):
- The Psi telescope with the REALIZATION identity gives: payoff_i^comp = (1/T) sum alpha_C + O(Psi/T + error)
- This is the exact compliant payoff. No g-alpha bridge needed here.

For the DEVIATOR (upper bound on payoff):
- The Bellman certificate at each stage gives: u_i(t) <= g_{C(t)} - [Psi(t+1) - Psi(t)] + O(error)
- Summing: deviator payoff <= (1/T) sum g_{C'(t)} + [Psi(0)-Psi(T)]/T + O(error)
- This is an upper bound. The question is: is (1/T) sum g_{C'(t)} bounded above?

THE KEY OBSERVATION: g_{i,C}* <= D_eta for every node C (bounded by the gain box).
So (1/T) sum g_{C'(t)} <= D_eta for ANY path.
Similarly, alpha_{i,C}* >= 0 for every node (payoffs are non-negative).

But we need: deviator payoff - compliant payoff <= epsilon.
This gives: (1/T) sum g_dev - (1/T) sum alpha_comp + 2|Psi|/T + error <= epsilon.

The sum g_dev - sum alpha_comp involves different paths. BUT:
- Under the COMPLIANT profile, the fixed-point guarantees that the weighted average of alpha equals g_root (semi-Markov ergodic theorem + fixed-point identity).
- So compliant payoff = g_root + O(error).
- For the DEVIATOR: by the Bellman, deviator payoff <= max gain across nodes + O(Psi/T).

Under condition (a), g_root IS the maximum achievable long-run payoff (the value of the game). The Bellman certificate ensures no deviation can exceed this. So deviator payoff <= g_root + O(Psi/T + error).

Therefore: regret = deviator - compliant <= [g_root - g_root] + O(Psi/T + error) = O(Psi/T + error) <= epsilon.

THE POINT: Don't try to show g-alpha = Z-increment for the deviator. Instead, show:
1. Compliant payoff = g_root + O(error) (semi-Markov + fixed-point)
2. Deviator payoff <= g_root + O(error) (Bellman + Psi boundedness)
3. Regret <= O(error) <= epsilon

g_root is the common benchmark that BOTH sides converge to.

Output the COMPLETE v24 LaTeX source as a downloadable .tex file.
