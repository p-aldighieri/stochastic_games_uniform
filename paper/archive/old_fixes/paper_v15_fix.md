# Paper v15 Fix — Pass 93

## All previous fixes confirmed working
- Degenerate terminal nodes, strategy-independent block partition, augmented kernel, convex domain, renewal-reward, restart-bias, depth boxes, prelude, Kakutani: ALL PASS

## THE DEEP BARRIER: Cemetery payoff is not actual game payoff

The Pass 92 reviewer (23 min EP) identified two fatal issues:
1. v(b) can exceed [0,1] so it's not a real stage payoff — the cemetery construction left the original payoff model
2. Exit label b is strategy-dependent — cemetery terms don't cancel across profiles

## THE CORRECT FIX: Abandon cemetery-phase payoff. Use COUPLING instead.

The cemetery phase was an attempt to account for post-exit stages within a launched block. But this approach fundamentally cannot work because:
- The actual game continues with real state transitions after an exit, not with artificial v(b) payoffs
- The routing automaton moves to the next node, and actual play resumes there

The right approach: DO NOT try to attribute payoff to post-exit stages within the current block. Instead:

### Approach: Regret via OCCUPATION MEASURE decomposition

The T-game average payoff decomposes as:
  (1/T) sum_{t=1}^T u_i(s_t, a_t) = sum over nodes C of (fraction of time at C) * (average payoff at C)

The compliant strategy sigma_eta plays blocks at each node. For each node C:
- The FRACTION of T stages spent at node C converges (by the block schedule and routing)
- The AVERAGE PAYOFF at node C during those stages is controlled by the local controller lemma

The deviator can change:
- Which stages are spent at which node (routing changes)
- The payoff during stages at each node

But the KEY INSIGHT from the fixed-point construction is:
- The gain g*_C is the AVERAGE payoff per stage at node C under the compliant profile
- The GLOBAL gain g*_root equals the weighted average of node gains
- Under ANY deviation, the total T-horizon payoff is at most g*_root * T + lower-order terms

This is because:
1. Within each node visit, the deviator's payoff is bounded by the Bellman certificate (local regret control via augmented kernel and renewal-reward)
2. The routing between nodes is controlled by the tree structure and the fixed-point
3. The SUM of local regret bounds TELESCOPES because the fixed-point equates node gains with routing-weighted continuation values

### What to change in the LaTeX

1. REMOVE the cemetery-phase payoff construction entirely. No U_i^cem, no post-exit payoff attribution within blocks.

2. DEFINE the T-game payoff decomposition as a SUM OVER NODE VISITS, not over launched blocks. Each node visit is a contiguous segment of stages at node C.

3. For each node visit segment [t_enter, t_exit], the average payoff is controlled by the local controller (Bellman certificate + renewal-reward). The local regret is O(sp(h)/L) per stage.

4. The TOTAL regret = sum over all node visits of (segment_length * local_regret_per_stage). By the fixed-point, the gains at different nodes are consistent, so the weighted sum gives the global regret bound.

5. The block schedule ensures that node visits are long enough for the local regret to be small. The superexponential schedule ensures switching errors are negligible.

6. The prelude (first few blocks) contributes O(K_eta/T). The remaining blocks have small local regret. The sum telescopes to O(epsilon) for large T.

This approach stays entirely within the actual game payoff model. No cemetery. No artificial per-stage v(b). Just actual stage payoffs decomposed by which node the play is visiting.

Output the COMPLETE v15 LaTeX source.
