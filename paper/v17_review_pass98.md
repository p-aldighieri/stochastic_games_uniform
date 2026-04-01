# v17 Review — Pass 98

**Thinking**: 25 min 28s Extended Pro
**Verdict**: FAIL

## What PASSES
- SEPARATE TOTALS: Formally yes — no cross-profile per-visit comparison
- BELLMAN BOUND PER VISIT: Essentially correct — one-profile architecture
- ACTUAL PAYOFF MODEL: Yes — stays in [0,1]
- ALL PREVIOUS FIXES: Yes

## FATAL BREAK: Global assembly step
The conversion from nodewise visit-level estimates to root-level g_root*T benchmark is not justified.

The proof treats exit-rate-weighted child gains as if they controlled child TIME CONTRIBUTIONS. But:
- beta_C*(b) are stationary exit rates, not actual time fractions
- If g is not monotone down the tree, the telescoping fails
- No semi-Markov occupation relation is proved showing actual time fractions converge to stationary weights

## THE FIX NEEDED
A rigorous SEMI-MARKOV OCCUPATION MEASURE result:
- Under the compliant strategy, the process is a semi-Markov chain on the tree nodes
- The fraction of T stages spent at node C converges to pi(C) * E[tau_C] / sum_C' pi(C') * E[tau_C']
- This convergence, combined with the local visit-level estimates, gives the global bound
