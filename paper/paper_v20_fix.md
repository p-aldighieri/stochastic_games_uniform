# Paper v20 Fix — Pass 103

## THE ISSUE (Pass 102): U_tilde exit credit has no matching entry debit

U_tilde(V) = U_act(V) + sum_b I_V(b)*v_C(b) credits exits but doesn't debit entries. The child visit starts with bias h_D(X_in), not -v_C(b). No cross-visit cancellation.

## THE FIX: Entry-exit corrected functional W_i(V)

Define: W_i(V) = U_act(V) + sum_b I_V(b)*v_C(b) - h_C(X_entry)

This SUBTRACTS the bias at entry. Then:
- Bellman optional stopping gives: E[W_i(V)] = E[U_act(V)] + E[sum_b I_V(b)*v_C(b)] - h_C(X_entry)
- By the Bellman identity: E[W_i(V)] <= g_C*E[l(V)] + [h at exit - h at entry] = g_C*E[l(V)] (the h terms cancel within the visit by optional stopping)

Now chain across visits:
- Visit k at node C exits with credit sum_b I(b)*v_C(b)
- Visit k+1 at node D=C[b] starts with debit -h_D(X_entry)
- At the fixed point: v_C(b) = g_D*E[tau_D] + h_D(xi_0^D) + O(eta) (from the Bellman certificate at D)
- With restart rho_D = delta_{xi_0^D}, the entry state IS xi_0^D, so h_D(X_entry) = h_D(xi_0^D) = 0 (by normalization h(xi_0)=0)

So the exit credit v_C(b) from visit k chains to: g_D*E[tau_D] + 0 + O(eta)
And the entry debit of visit k+1 is: -h_D(xi_0^D) = 0

The net chain: v_C(b) - 0 = v_C(b) ≈ g_D*E[tau_D]/E[tau_D] per stage...

Actually, the CLEANEST approach: use the POTENTIAL FUNCTION h directly.

Define the POTENTIAL TELESCOPE:
  Phi(t) = h_{C(t)}(X_t) where C(t) is the current node at stage t

At each stage: E[Phi(t+1) - Phi(t)] = g_{C(t)} - u_i(s_t, a_t) + O(error) (by the Bellman equation)

Summing over T stages:
  E[Phi(T) - Phi(0)] = sum_t [g_{C(t)} - u_i(s_t, a_t)] + O(error*T)

Therefore:
  (1/T) sum_t u_i(s_t, a_t) = (1/T) sum_t g_{C(t)} - (1/T)[Phi(T)-Phi(0)] + O(error)

Since |Phi| <= ||h||_inf = O(sp(h)), the boundary term is O(sp(h)/T).

And sum_t g_{C(t)} = sum over visits V of g_{C(V)}*l(V), which by the fixed-point...

Wait — this is EXACTLY the standard Markov-chain potential argument. The potential h is the bias function. The one-step Bellman equation gives the drift. The telescope over T stages gives the payoff bound.

THE KEY: The Bellman equation h(x) + g = r(x) + P*h(x) + O(error) holds for EACH state x at EACH node. So:
  u_i(s_t, a_t) = g_{C(t)} + h_{C(t)}(X_t) - E[h_{C(t+1)}(X_{t+1}) | X_t] + O(error)

Summing: sum_t u_i = sum_t g_{C(t)} + h(X_0) - h(X_T) + O(error*T)

This works STAGE BY STAGE, not visit by visit. No need for visit-level telescoping at all!

Output the COMPLETE v20 LaTeX source as a downloadable .tex file.
