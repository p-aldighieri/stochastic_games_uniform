# v11 Review — Pass 86

**Thinking**: 28 min 17s Extended Pro
**Verdict**: FAIL

## All previous fixes confirmed working
- Augmented kernel, convex domain, renewal-reward, restart-bias, depth boxes, prelude, exact coefficients: ALL PASS

## Persistent terminal-label issue (3rd attempt)

Terminal exits are NOT regenerative. Child exits restart the block schedule at the child node. Terminal exits STOP the schedule and play continues under the fixed terminal profile for all remaining T-t stages.

The per-stage average w(b) is correct, but the T-game accounting credits it as a single continuation value, not as (T-t) * w(b). This leaves a Theta(T) gap.

## The real fix needed

Option A: Make terminal exits regenerative. Define a "terminal node" for each terminal label that has a trivial bookkeeping kernel (immediate absorption), so the block schedule continues through it. The terminal profile IS the executed strategy at this degenerate node.

Option B: Redesign the global regret analysis to explicitly weight each segment by its actual duration. The T-game payoff = sum over all node-visit segments of (segment_length/T) * segment_avg_payoff. Terminal segments contribute (T-t)/T * w(b). Since the fixed-point already sets v(b) = w(b), this is absorbed naturally — BUT the proof must use this weighted decomposition instead of block-by-block summation.

Option B is cleaner and closer to what the proof already does. The key change: the global regret bound should decompose the T-horizon into SEGMENTS (node visits + terminal tails), not BLOCKS.
