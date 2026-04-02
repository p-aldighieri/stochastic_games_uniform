# Paper v23 Fix — Pass 109

## Pass 108: Psi telescope correct, gain comparison fails

The gain-level routed comparison (Lemma 6.6 / Prop 8.3) doesn't prove the step from sum g_{C(t)} to regret. Different node sequences for compliant vs deviator.

## THE FIX: Use Psi DIRECTLY for epsilon-equilibrium, no gain comparison needed

The epsilon-equilibrium definition: for player i, under sigma_eta, no unilateral deviation tau_i improves payoff by more than epsilon.

The Psi telescope gives, for ANY strategy profile sigma:
  (1/T) sum_t u_i(t; sigma) = (1/T) sum_t g_{i,C(t)}(sigma) + [Psi_i(0) - Psi_i(T)]/T + O(error)

Now consider: player i deviates from sigma_eta to (tau_i, sigma_{-i}^eta).

STEP 1 (Compliant lower bound): Under sigma_eta, the Psi telescope with the REALIZATION identity gives:
  (1/T) sum_t u_i(t; sigma_eta) = (1/T) sum_t alpha_{i,C(t)} + O(Psi_bound/T + error)
  where alpha is the exact per-stage payoff rate from the controller.

STEP 2 (Deviator upper bound): Under (tau_i, sigma_{-i}^eta), the Psi telescope with the BELLMAN upper bound gives:
  (1/T) sum_t u_i(t; tau_i, sigma_{-i}) <= (1/T) sum_t g_{i,C'(t)} + O(Psi_bound/T + error)
  where g is the Bellman gain (upper bound) and C'(t) is the deviator's node sequence.

STEP 3 (The bridge): The compliant gains g_{i,C}* and alphas alpha_{i,C}* satisfy:
  g_{i,C}* = alpha_{i,C}* + sum_b beta_{C}*(b) * v_{i,C}*(b) + O(eta)

The continuation terms sum_b beta*v are EXACTLY what the stock Z tracks! So:
  sum_t g_{i,C'(t)} = sum_t alpha_{i,C'(t)} + Z-contributions + O(eta*T)

And the Z-contributions are absorbed into Psi(T). Therefore:
  Deviator payoff <= (1/T) sum_t alpha_{i,C'(t)} + O(Psi_bound/T + eta + error)

But alpha_{i,C}* <= g_{i,C}* for every node, and g_{i,C}* is the MAX payoff player i can get at node C. The compliant achieves alpha; the deviator gets at most g. The difference g - alpha at each node is the continuation term, which is absorbed by Z/Psi.

THEREFORE: Deviator payoff - Compliant payoff <= 2*Psi_bound/T + O(eta + delta + 1/T)

With eta, delta chosen so this is <= epsilon, the epsilon-equilibrium follows.

THE KEY: Don't compare sum g_dev vs sum alpha_comp across different node sequences. Instead, recognize that the Psi process ALREADY encodes the full routing and continuation value information. The regret bound comes from |Psi(T)|/T being small, which is guaranteed by Psi boundedness.

Output the COMPLETE v23 LaTeX source as a downloadable .tex file.
