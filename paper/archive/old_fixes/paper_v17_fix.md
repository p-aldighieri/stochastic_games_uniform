# Paper v17 Fix — Pass 97

## What's confirmed working
- Expectation-based regret at visit level: YES
- Compliant E[U_act] = alpha * E[tau]: YES
- Deviator E[U_act] <= g*E[tau] + sp(h): YES
- Actual payoff model [0,1]: YES
- All structural fixes: YES

## TWO REMAINING BREAKS

### Break 1: Visit regret comparison uses same l(V) for both profiles
The corollary subtracts compliant from deviator using same l(V). But compliant and deviating visits have different stopping-time laws.

FIX: The regret comparison should be between E[U_dev(V)] and g* * E[l_dev(V)], where l_dev is the DEVIATOR's visit length. The deviator upper bound gives E[U_dev] <= g*E[l_dev] + sp(h). The compliant lower bound gives E[U_comp] >= alpha*E[l_comp]. These are SEPARATE bounds for SEPARATE visits. The regret is:
  (1/T) * sum_t u_i(dev) - (1/T) * sum_t u_i(comp) <= epsilon
NOT a per-visit comparison.

### Break 2: Routing telescoping: parent E[l] vs child E[l]
The telescoping multiplies the fixed-point identity by E[l(V_parent)], giving a child term g_child * beta * E[l_parent]. But the child visit has its own E[l_child].

FIX: The telescoping should sum over ALL visits across the T-horizon. Each visit contributes E[U(V)] to the total. The total compliant payoff is:
  E[sum_V U_comp(V)] = sum over visits V of alpha_C(V) * E[l(V)]
                     = (by fixed-point) g_root * sum_V E[l(V)] + error
                     = g_root * T + error

The key: the fixed-point ensures that the WEIGHTED average of alpha values (weighted by actual visit durations) equals g_root. The weights are the actual E[l(V)] for each visit, not borrowed from parent visits.

The routing balance should state: for the compliant profile,
  sum_{V at node C} E[l(V)] * alpha_C = sum_{V at node C} E[U(V)]
and the tree structure ensures
  sum_{all V} E[U(V)] = g_root * T + O(error terms)

This works because under the compliant profile, the sequence of visits IS the stationary process, and the occupation fractions converge to the tree-weighted values.

Output the COMPLETE v17 LaTeX source.
