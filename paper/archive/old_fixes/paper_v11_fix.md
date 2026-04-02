# Paper v11 Fix — Pass 85

## The issue

Post-terminal horizon can be Theta(T). One-shot w(b) recording misses this.

## The correct treatment

After reaching terminal label b at stage t, the strategy plays the FIXED terminal continuation profile for the remaining T-t stages. The correct accounting:

1. The terminal continuation profile has a well-defined per-stage average payoff w_avg_i(b) for each player i.

2. At the fixed point x*, the continuation value v_{i,C}^{x*}(b) at a terminal label b is SET EQUAL TO w_avg_i(b) — not a one-shot payoff, but the per-stage average under the terminal profile. This is a DEFINITION choice in the fixed-point construction.

3. When a block at node C exits to terminal b, the remaining game plays under the fixed terminal profile. The contribution of this segment to the T-game average is:
   (T-t)/T * w_avg_i(b)

4. The regret from terminal segments: since v_{i,C}^{x*}(b) = w_avg_i(b) is built into the fixed-point, the Bellman certificate ALREADY accounts for the terminal continuation correctly. The node's local gain g* includes the contribution from terminal exits weighted by their exit rates.

5. Therefore NO separate terminal-regret term is needed. The terminal continuation is fully internalized in the fixed-point construction. The only remaining issue is the O(1/T) boundary effect from the last incomplete block or terminal segment, which is absorbed into K_eta/T.

The key change: stop treating terminal labels as special. They are just exit labels whose continuation values happen to be FIXED (not determined by descendant nodes). The fixed-point construction handles them exactly like any other continuation value.

## What to change in LaTeX

1. Remove the special terminal-label accounting remark (lines ~1287-1298)
2. In the node data, clarify that v_{i,C}(b) = w_avg_i(b) is the per-stage average under the terminal profile (not a one-shot value)
3. In the fixed-point construction, terminal labels contribute their w_avg values as continuation, just like child nodes contribute their gains
4. The regret bound handles terminals the same as internal exits — no separate D*||u||/T term needed

Output the COMPLETE v11 LaTeX source.
