# Paper v19 Fix — Pass 101

## What's confirmed working
- Bellman per-visit bound: correct
- Separate totals: correct architecture
- Actual payoff model [0,1]: clean
- All structural fixes: verified

## THE FATAL ERROR IN v18: Gain near-constancy is FALSE
Counterexample: root with u=1, terminal child with w=0 → g_root=1, g_child=0.
g values CAN vary by O(1) across nodes. Cannot assume they're constant.

## THE CORRECT FIX: U_tilde telescoping across visits

The Bellman per-visit bound gives: E[U_tilde_i(V)] <= g_C* * E[l(V)] + sp(h)

where U_tilde_i(V) = U_i^act(V) + sum_b I_V(b) * v_i,C*(b)

The KEY INSIGHT: U_tilde ALREADY includes continuation values v(b) at the exit boundary. When the next visit starts at the child node C[b], the Bellman bound at that visit also starts with the SAME continuation value. So the U_tilde values CHAIN TOGETHER across consecutive visits:

Total U_tilde over visits = sum_V [U_act(V) + sum_b I_V(b)*v(b)]
                          = sum_V U_act(V) + sum_V sum_b I_V(b)*v(b)

The second sum telescopes: each exit's v(b) approximately equals g_child * E[l_child] / E[l_child] when divided by visit length. But more precisely:

For the COMPLIANT profile: the telescoping works because the fixed-point equation g_C = alpha_C + sum_b beta_C*v_C(b) + O(eta) means that U_tilde telescopes through the tree. Specifically:

sum over all visits V of E[U_tilde(V)]
= sum_V E[U_act(V)] + sum_V sum_b E[I_V(b)] * v_C(V)(b)
= Total actual payoff + sum of boundary values

The boundary values from one visit become the STARTING VALUES of the next visit. At the root, there's no incoming boundary value. At terminal nodes, the process stays forever. So the chain of U_tilde values telescopes to:

E[U_tilde(first visit)] + E[U_tilde(second visit)] + ... = g_root * T + O(boundary terms)

This telescoping works because U_tilde(V) = g_C*E[l(V)] + O(sp(h)) by Bellman, AND the continuation values v(b) in U_tilde match the g values at the next node (by the fixed-point construction).

For the DEVIATOR: the same U_tilde telescoping applies because the Bellman UPPER bound on E[U_tilde(V)] is g_C*E[l(V)] + sp(h), and the continuation values still chain together regardless of which strategy the deviator plays.

The actual payoff is: U_act = U_tilde - sum_b I(b)*v(b)
So: total U_act = total U_tilde - total boundary values
And: total U_tilde <= g_root*T + O(error) by telescoping
And: total boundary values = total U_tilde - total U_act (accounting identity)

The key is that the boundary values from the LAST visit in the chain are O(D*||v||) = O(D^2) per terminal event, and the number of such events is bounded.

Output the COMPLETE v19 LaTeX source as a downloadable .tex file.
