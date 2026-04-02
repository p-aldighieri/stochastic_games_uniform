# Paper v14 Fix — Pass 91

## All previous fixes confirmed working
- Degenerate terminal nodes: PASS
- Strategy-independent block boundaries: PASS (boundaries fixed, future path still action-dependent)
- Augmented kernel, convex domain, renewal-reward, restart-bias, depth boxes, prelude, Kakutani: ALL PASS

## TWO REMAINING FATAL ISSUES (from Pass 90 EP review, 26 min)

### Issue 1: Regret uses profile-dependent tau(B), not common |B|
The realization theorem uses E[tau_cmp], Bellman lemma uses E[tau_dev]. The subtraction leaves g*(E[tau_dev] - E[tau_cmp]) which is order |B|.

### Issue 2: Augmented payoff only covers live segment [0, tau(B)]
After cemetery hit, the remaining |B| - tau(B) stages are unaccounted. This gap can be Theta(|B|).

## THE CORRECT FIX: Full Scheduled-Block Payoff Identity

The key insight: after a cemetery hit at time tau within a launched block [t_k, t_k + L_k], the AUGMENTED strategy prescribes specific behavior for the remaining L_k - tau stages. This behavior must be explicitly modeled.

### The scheduled-block payoff decomposition

For ANY strategy profile sigma (compliant or deviating), define the FULL scheduled-block payoff on block B_k = [t_k, t_k + L_k]:

  U_i^{full}(B_k; sigma) = sum_{s=t_k}^{t_k+L_k-1} u_i(state_s, action_s)

This is the raw payoff over ALL L_k stages. Under the augmented kernel:

1. LIVE PHASE [t_k, t_k + tau - 1]: Play proceeds under the internal kernel P_C^0. Payoffs accumulate normally.

2. POST-CEMETERY PHASE [t_k + tau, t_k + L_k - 1]: After the first exit (cemetery hit), the state is absorbed in the cemetery. The EXECUTED strategy at the cemetery state yields a FIXED per-stage payoff. Under the compliant profile, this is the continuation value v(b) where b is the exit label. Under a deviator, this may differ.

3. CONTINUATION: At stage t_k + L_k, the routing automaton moves to the next node.

### The regret identity on full scheduled blocks

The block regret should be written as:

  U_i^{full}(B_k; sigma_dev) - U_i^{full}(B_k; sigma_comp)

Both sides sum over the SAME L_k stages. No tau appears in the normalization. The tau only determines WHEN the live/cemetery transition happens within the block.

### What to change in the LaTeX

1. DEFINE the full scheduled-block payoff U_i^{full}(B_k; sigma) as a sum over ALL L_k stages, splitting into live phase + cemetery phase.

2. REWRITE the realization theorem: lower-bound U_i^{full}(B_k; sigma_comp) using the full L_k stages. The live part uses the renewal-reward identity. The cemetery part contributes v(b) * (L_k - tau) per stage.

3. REWRITE the Bellman lemma: upper-bound U_i^{full}(B_k; sigma_dev) similarly. The live part gives the deviator's augmented payoff. The cemetery part gives continuation.

4. The SUBTRACTION now works on the same L_k stages for both sides. The tau-dependent terms cancel or are controlled because both sides pay v(b) per stage in the cemetery phase.

5. KEY: In the cemetery phase, the continuation value v(b) is the SAME for both compliant and deviating play (it's determined by the exit label b, which is a public signal). So the cemetery phases contribute identically, and the regret difference is concentrated on the live phase only — which is exactly what the renewal-reward identity controls.

6. The final regret bound then uses L_k in the denominator (not tau), and the sum over blocks telescopes correctly over the T-horizon.

Output the COMPLETE v14 LaTeX source.
