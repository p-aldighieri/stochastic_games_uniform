# Paper v25 Fix — Pass 113

## Pass 112: Common g_root scalar benchmark appears FALSE

The reviewer says g_root as a single scalar benchmark for both compliant and deviator is wrong under current definitions. 112 EP passes with local machinery fully verified but global benchmark failing repeatedly.

## FUNDAMENTAL REFRAMING: Single-player MDP for the deviator

When player i considers deviating from sigma_eta, the OTHER players continue playing sigma_{-i}^eta. So player i faces a FIXED Markov environment — it's a SINGLE-PLAYER MDP.

In this MDP:
- States: (node C, internal state xi) in the metastable tree
- Player i's actions: any action a_i
- Transition: determined by (a_i, sigma_{-i}^eta(xi))
- Payoff: u_i(xi, (a_i, sigma_{-i}^eta(xi)))

The Bellman certificates (g_C, h_C) were constructed as an APPROXIMATE solution to this MDP's average-reward Bellman equation. Specifically, the fixed-point construction ensures that for each node C:
  g_{i,C}* is an approximate optimal gain for this MDP restricted to node C
  h_{i,C}* is the corresponding bias

The Psi process is a SUPERMARTINGALE for the deviator in this MDP:
  E[Psi(t+1) | F_t] <= Psi(t) + g_{i,C(t)}* - u_i(t) + O(error)

This means: u_i(t) <= g_{i,C(t)}* + Psi(t) - E[Psi(t+1)] + O(error)

Now THE KEY: in a single-player MDP with the Psi supermartingale, the OPTIMAL GAIN is characterized by the Bellman equation. The fixed-point was constructed so that the gain values g_C are CONSISTENT across the tree — the fixed-point equation makes g_C the value of continuing optimally from node C.

For the DEVIATOR: Psi is a supermartingale, so E[Psi(T)] <= Psi(0). Therefore:
  sum u_i(t) <= sum g_{C(t)} + Psi(0) - E[Psi(T)] + error*T
              <= sum g_{C(t)} + 2*||Psi||_inf + error*T

For the COMPLIANT: Psi is approximately a martingale (exact realization), so:
  sum u_i(t) = sum alpha_{C(t)} + Psi(0) - E[Psi(T)] + error*T
             = sum alpha_{C(t)} + O(||Psi||_inf) + error*T

The regret = deviator - compliant = sum(g_dev - alpha_comp) + O(Psi_bound)

Now: the compliant profile IS the approximately optimal policy in the single-player MDP. The fixed-point ensures this. So sum alpha_{C(t)} / T is approximately the OPTIMAL average reward of the MDP. And sum g_{C(t)} / T for ANY policy (including the deviator) is at most the optimal average reward + O(eta).

This follows because:
1. Under the compliant, the process is ergodic (condition (a)), so (1/T) sum alpha = ergodic_average + O(1/T)
2. The fixed-point makes ergodic_average = g_root (the MDP value)
3. For any deviating policy, the Bellman supermartingale gives (1/T) sum u_i <= g_root + O(Psi/T + error)

The point: g_root is the value of the SINGLE-PLAYER MDP that player i faces, not a property of the multi-player game. It IS the correct benchmark because the other players' strategies are fixed.

Output the COMPLETE v25 LaTeX source as a downloadable .tex file.
