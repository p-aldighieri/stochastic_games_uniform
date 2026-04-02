# v15 Review — Pass 94

**Thinking**: 30 min 17s Extended Pro
**Verdict**: FAIL

## What PASSES (real progress)
- Actual payoff model: PASS — cemetery bug gone, stays in u_i in [0,1]
- Node-visit decomposition: PASS — segment boundaries well-defined
- Previous fixes: mostly PASS

## TWO FATAL BREAKS

### Break 1: Ratio-of-expectations step (local controller)
- Proof bounds E[U/tau] pathwise, then claims E[U]/E[tau] follows by "taking expectations"
- But E[U/tau] != E[U]/E[tau] in general
- The realization theorem's core lower bounds E[U_i^act(V)] >= (alpha - C*eta*delta)*E[l(V)] are unsupported
- Need rigorous bridge from empirical visit-rate control to expected total actual payoff

### Break 2: Routing-balance proposition (global telescoping)
- Claims weighted sum of alpha - g_root over visits is bounded
- Proof uses nodewise identity g = alpha + sum_b beta(b)*g_child + O(eta)
- But beta_C*(b) are stationary exit rates per unit time, NOT actual exit indicators I_V(b)
- Actual routing is driven by realized boundary hits, not deterministic stationary weights
- The telescoping argument uses the wrong currency

## REVIEWER'S SUGGESTED FIX
1. Replace ratio-of-expectations with genuinely usable estimate for expected visit totals
2. Rewrite routing-balance in terms of actual exit indicators or expected exit counts, not stationary rates beta_C*
