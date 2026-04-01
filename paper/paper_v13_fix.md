# Paper v13 Fix — Pass 89

## All previous fixes confirmed working
- Degenerate terminal nodes: PASS
- Block schedule continuity: PASS
- Fixed-point construction: PASS
- Augmented kernel, convex domain, renewal-reward, restart-bias, depth boxes, prelude: ALL PASS

## NEW FATAL GAP: Global regret comparison (block partition is strategy-dependent)

The "Augmented block regret" corollary (lines 1789-1825) and main proof (lines 1879-1916) subtract a compliant block payoff from a deviating block payoff AS IF both live on the same block B with the same duration |B|.

Problem: Once player i deviates, block exit times, successor nodes, and the block partition itself change. The compliant block and deviating block are NOT the same object. The realization estimate for the compliant profile does not apply to the deviator's block B'.

## The correct structural fix: COMPLIANT BLOCK PARTITION AS REFERENCE

The standard approach in the stochastic games literature (Mertens-Neyman, Vieille, etc.) is:

1. The COMPLIANT PLAY defines the block partition. Blocks are defined by the COMPLIANT strategy's switching schedule, NOT by the deviator's play.

2. Under the compliant strategy sigma_eta, the block boundaries are deterministic functions of the routing schedule — they do NOT depend on which actions the players actually choose. The block schedule is: "at stage t_k, start block k at node C_k with length L_k." This schedule is fixed a priori.

3. The deviator plays inside the SAME block partition. On block B_k (stages t_k to t_k + L_k), the deviator may take different actions, but the block boundaries are still t_k and t_k + L_k. The block does NOT end early because the deviator causes a different exit.

4. Key insight: The bookkeeping kernel WITHIN a block already accounts for exits. An exit from node C during block B_k means the INTERNAL bookkeeping restarts, but the block boundary is still at t_k + L_k. The augmented kernel treats exits as transitions to cemetery/restart states WITHIN the block.

5. Therefore: Both compliant and deviating payoffs ARE computed on the same block B_k = [t_k, t_k + L_k]. The augmented kernel handles exits within the block. The payoff comparison U_i^dev(B_k) - U_i^comp(B_k) is valid because both use the same time interval.

## What to change in the LaTeX

1. In the block schedule definition: Make EXPLICIT that block boundaries are deterministic and strategy-independent. They are set by the routing schedule a priori, not by the realized play.

2. In the augmented block regret corollary (lines ~1789-1825): Clarify that BOTH the compliant and deviating payoffs are computed over the same block interval [t_k, t_k + L_k]. The augmented kernel handles within-block exits via cemetery states.

3. In the main proof (lines ~1879-1916): The summation over blocks uses the FIXED compliant block partition. Each block's regret bound applies because the block interval is the same for both strategies.

4. Add a remark explaining why the block partition is strategy-independent: "The block schedule {(t_k, C_k, L_k)} is determined by the routing automaton, which observes only the PUBLIC routing signal (which node is currently active), not the players' private actions. Therefore block boundaries are identical under any strategy profile."

5. If the routing signal IS affected by the deviator's actions (because exits depend on actions), then the fix must use the SCHEDULED block length L_k as the reference, with the augmented kernel absorbing any early/late exits within the block. The renewal-reward decomposition already handles this via the augmented first-exit time.

Output the COMPLETE v13 LaTeX source.
