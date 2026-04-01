# Paper v12 Fix — Pass 87

## The terminal-label problem (failed 3 times)

Terminal exits stop the block schedule. The remaining T-t stages under the terminal profile are NOT covered by the block-by-block regret analysis. Previous attempts to patch this (one-shot w(b), per-stage w_avg, absorb into K_eta/T) all fail because they credit Theta(T) stages as O(1).

## The correct structural fix: DEGENERATE TERMINAL NODES

The block schedule should NEVER stop. Instead:

1. For each terminal label b with terminal profile sigma_b and per-stage average w_i(b), create a DEGENERATE TERMINAL NODE T_b in the metastable tree.

2. Node T_b has:
   - Internal state space: a single absorbing state xi_term
   - No exits (Out(T_b) = empty set, or self-loop)
   - Per-stage payoff under sigma_b: w_i(b)
   - Bookkeeping kernel: trivial (immediate return to xi_term)
   - Gain: g_{i,T_b} = w_i(b) (exact, no approximation)
   - Bias: h = 0 (constant gain, no fluctuation)

3. When the block schedule at node C exits to terminal label b, the schedule CONTINUES at degenerate node T_b. Blocks at T_b are trivial: each block stays at xi_term for L stages, collecting w_i(b) per stage.

4. The regret analysis at T_b: since sigma_b is a FIXED (non-optimized) profile, the deviator can't improve on w_i(b) beyond the eps-equilibrium guarantee already built into the fixed-point. The Bellman certificate at T_b is trivial: g = w(b), h = 0, sp(h) = 0.

5. This means: NO special terminal accounting needed. Terminal nodes are just leaf nodes of the tree that happen to have trivial internal dynamics. The general block-by-block regret analysis applies unchanged.

## What to change in the LaTeX

1. In the tree definition: terminal labels are replaced by degenerate terminal nodes T_b with single absorbing state and per-stage payoff w(b)

2. Remove ALL terminal-label special cases from routing, realization, and main proof

3. The fixed-point construction: terminal nodes contribute g_{T_b} = w(b) as continuation values to parent nodes, exactly like child nodes

4. The block schedule runs FOREVER (until T stages are used), including through terminal nodes

5. The regret bound: uniform over ALL nodes, including degenerate terminal ones (where the bound is trivially satisfied)

Output the COMPLETE v12 LaTeX source.
