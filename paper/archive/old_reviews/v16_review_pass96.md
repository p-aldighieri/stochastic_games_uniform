# v16 Review — Pass 96

**Thinking**: 26 min 15s Extended Pro
**Verdict**: FAIL

## What PASSES (significant progress)
- Expectation-based regret: MOSTLY YES — ratio-of-expectations fixed
- Compliant lower bound: YES — E[U_act] = alpha * E[tau]
- Deviator upper bound: YES at single-visit level
- Actual payoff model: YES — no fake payoffs
- All previous fixes: YES — no regressions

## TWO REMAINING BREAKS

### Break 1: Per-visit regret corollary (lines 1992-1995)
- Subtracts compliant benchmark using same l(V) as deviator
- But compliant and deviating visits have DIFFERENT stopping-time laws
- The clean single-visit upper bound is fine, but regret comparison isn't justified

### Break 2: Routing balance telescoping (lines 1868-1889)
- E[I_V(b)] = beta*E[l(V)] is justified
- But telescoping multiplies g = alpha + sum_b beta(b)*g_child by E[l(V)]
- Child term becomes g_child * beta * E[l(V_parent)]
- This should match child visit's E[l(V_child)], not parent's
- Different nodes have different expected visit lengths

## KEY INSIGHT FOR FIX
The telescoping needs to account for the RATIO E[l(V_child)]/E[l(V_parent)] = beta(b) * E[l(V_parent)] / E[l(V_child)] and show these match. Under the stationary package, E[l(V_child)] is determined by the child's local dynamics, not the parent's.
