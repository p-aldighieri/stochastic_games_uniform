# Paper v18 Fix — Pass 99

## What's confirmed working
- Separate total bounds (no cross-profile comparison): YES
- Bellman bound per visit (one-profile): YES
- Actual payoff model [0,1]: YES
- Expectation-based estimates: YES
- All structural fixes: YES

## THE ONE REMAINING FATAL BREAK: Global assembly

The proof cannot convert local visit-level estimates into a root-level g_root*T bound because it uses stationary exit rates as if they control time fractions. No semi-Markov occupation relation is proved.

## THE FIX: Prove a semi-Markov occupation theorem

Under the compliant profile, the sequence of node visits forms a SEMI-MARKOV CHAIN on the tree nodes:
- The embedded chain has transition probabilities p(C -> C[b]) = beta_C*(b) (normalized exit rates)
- The sojourn times are E[tau_C] at each node C
- The stationary distribution of the embedded chain is pi(C)
- The SEMI-MARKOV STATIONARY MEASURE gives fraction of time at C as: pi(C)*E[tau_C] / sum_C' pi(C')*E[tau_C']

KEY THEOREM TO ADD: For the compliant profile sigma_eta operating on the metastable tree under condition (a):

(1) The embedded chain (sequence of visited nodes) is an irreducible positive-recurrent Markov chain on the finite tree nodes (irreducibility follows from condition (a)).

(2) By the semi-Markov ergodic theorem, as T -> infinity:
    (1/T) * sum_{t: stage t at node C} 1 -> pi(C)*E[tau_C] / sum_C' pi(C')*E[tau_C']

(3) Therefore:
    (1/T) * sum_t u_i(s_t, a_t) = sum_C (fraction at C) * (avg payoff at C)
    -> sum_C [pi(C)*E[tau_C] / Z] * alpha_C*
    = g_root* (by the fixed-point identity, since the fixed-point was constructed so that the weighted average of alpha values equals g_root)

(4) For the DEVIATOR: the Bellman bound gives E[U_tilde(V)] <= g_C* * E[l(V)] + sp(h) per visit. Summing over all visits and dividing by T:
    (1/T) * E[total deviator payoff] <= (1/T) * sum_V [g_C(V)* * E[l(V)] + sp(h)]
    The sum_V g_C(V)*E[l(V)] involves a WEIGHTED average of g values with weights being actual visit durations. By the tree structure and the fixed-point g = alpha + sum_b beta*g_child, this weighted average equals g_root* regardless of the deviator's routing, because the gains are CONSISTENT across the tree.

CRITICAL: The gains g_C* are consistent because of the fixed-point equation. For ANY probability distribution over nodes (any routing), the weighted average of g values equals g_root. This is because the fixed-point makes g constant across the tree (up to eta errors): g_root = g_C + O(eta) for all C. Under condition (a), the metastable tree has bounded depth, so g_C = g_root + O(D*eta) for all nodes.

So the global assembly becomes trivial: all g_C* values are within O(D*eta) of g_root*, and sum_V E[l(V)] = T. Therefore:
    sum_V g_C(V)* * E[l(V)] = g_root* * T + O(D*eta*T)

This eliminates the need for a semi-Markov occupation theorem for the deviator. Only the compliant profile needs it, and the deviator bound follows from the near-constancy of g across the tree.

Output the COMPLETE v18 LaTeX source.
