# Paper v21 Fix — Pass 105

## Pass 104 FAIL: Potential Phi not continuous across node boundaries

Phi(t) = h_{C(t)}(X_t) jumps when play transitions from node C to child D because h_C and h_D are different functions. The paper admits a "carried stock Z_t" is needed but suppresses it.

## THE FIX: Define the stock-augmented potential Psi explicitly

Define the AUGMENTED POTENTIAL:
  Psi_i(t) = h_{i,C(t)}(X_t) + Z_i(t)

where Z_i(t) is the ACCUMULATED TRANSITION STOCK:
  Z_i(0) = 0
  At each node transition (exit from C to child D at stage t):
    Z_i(t) := Z_i(t-1) + [v_{i,C}(b) - h_{i,D}(X_entry^D)]

The transition stock Z compensates for the jump in h across node boundaries. Specifically:
- When exiting C via boundary label b: the Bellman at C credits v_C(b) as exit value
- When entering D: the Bellman at D starts with h_D(X_entry)
- The difference v_C(b) - h_D(X_entry) is absorbed into Z

Now the ONE-STEP DRIFT of Psi is:
- Inside a node (no transition): Psi(t+1) - Psi(t) = h(X_{t+1}) - h(X_t) = g_C - u_i(t) + O(error) (by local Bellman)
- At a node transition: Psi jumps by [v_C(b) - h_D(X_entry)] in Z, and h jumps from h_C to h_D. The net change in Psi is: [h_D(X_entry) + v_C(b) - h_D(X_entry)] - h_C(X_exit) = v_C(b) - h_C(X_exit). By the Bellman at exit: this equals g_C - u_i(t) + O(error).

So Psi has a CLEAN one-step drift everywhere:
  E[Psi(t+1) - Psi(t) | F_t] = g_{C(t)} - u_i(t) + O(error)

Summing: sum u_i(t) = sum g_{C(t)} + Psi(0) - Psi(T) + O(error*T)

Psi is bounded: |Psi(t)| <= ||h||_inf + |Z(t)|. And |Z| grows by at most |v_C(b)| + |h_D| per transition, with at most T/L transitions. By the superexponential schedule, this is controlled.

Output the COMPLETE v21 LaTeX source as a downloadable .tex file.
