# Paper v16 Fix — Pass 95

## What's confirmed working (from v15 review)
- Actual payoff model: PASS — no fake post-exit payoffs
- Node-visit decomposition: PASS — segment boundaries well-defined
- All previous fixes: PASS

## TWO FATAL BREAKS to fix

### Break 1: E[U/tau] != E[U]/E[tau]
The local controller bounds U/tau pathwise, then "takes expectations" to get E[U]/E[tau]. This is invalid.

THE FIX: Use the RENEWAL-REWARD THEOREM properly. The renewal-reward theorem says:
  lim_{n->inf} (sum of rewards in n cycles) / (sum of durations in n cycles) = E[reward per cycle] / E[cycle duration]

For a SINGLE visit (one cycle), this doesn't apply directly. Instead use:
- For the COMPLIANT profile: the controller ensures E[U_act(V)] >= (alpha - error) * E[l(V)] directly from the stationary measure characterization. The occupation measure mu satisfies sum_xi mu(xi,a)*u_i(xi,a) = alpha and sum_xi mu(xi,a) = 1/E[tau]. So E[U_act] = alpha * E[tau] exactly for the compliant stationary profile.
- For the DEVIATOR: the Bellman upper bound gives E[U_act(V)] <= (g* + sp(h)/E[tau]) * E[tau] + |h|_inf from the optional stopping identity. The key is using E[U] directly, not E[U/tau].

The point: work with E[U] and E[tau] separately, never with ratios. The renewal-reward identity gives E[U_act] = alpha * E[tau] for the compliant, and the Bellman optional stopping gives E[U_act] <= g*E[tau] + sp(h) for the deviator.

### Break 2: Stationary beta vs actual exit indicators
The routing-balance uses beta_C*(b) (stationary rates) instead of actual exit counts.

THE FIX: Use EXPECTED exit counts E[I_V(b)] instead of stationary weights.
- For the compliant profile: by the occupation measure, E[I_V(b)] = beta_C*(b) * E[tau_V] exactly (this is the definition of beta as the exit rate per unit time).
- So the routing-balance should be written as: E[l_V * alpha_C] = E[U_act(V)] = alpha_C * E[l_V], and E[I_V(b)] = beta_C * E[l_V], making the telescoping work with EXPECTED values, not pathwise.
- The key insight: everything telescopes in EXPECTATION. The fixed-point identity g = alpha + sum_b beta(b)*g_child is an EXPECTED identity, not a pathwise one.

### Summary of approach
1. All regret estimates should be in EXPECTATION form: E[U], E[tau], E[I(b)]
2. Compliant profile: E[U_act] = alpha * E[tau] from occupation measure
3. Deviator: E[U_act] <= g*E[tau] + sp(h) from optional stopping / Bellman
4. Routing balance: uses E[I_V(b)] = beta * E[tau], telescoping in expectation
5. Total regret bound: sum over visits of (g* * E[l_V] - E[U_act(V)]) <= error terms

Output the COMPLETE v16 LaTeX source.
