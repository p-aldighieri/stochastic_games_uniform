# v25 Review — Pass 114

**Thinking**: 22 min 13s Extended Pro
**Verdict**: FAIL

## PASSES
- Single-player MDP reframing: YES — correct. When player i deviates, others play sigma_{-i}^eta, creating a well-defined MDP for player i.
- Psi supermartingale: Mostly yes — local drift certificate works
- Local machinery (Z, Bellman, bias, routing): intact from previous passes

## FAILS: g_root as MDP value
"the local gain g_{i,C}* is a restarted-node average, not the value of the global routed MDP"

The per-node gain g_{i,C}* is the average reward of the MDP RESTRICTED to node C with restarts. It is NOT the optimal gain of the global MDP that spans all nodes. The child-gain lump sum v_C(b) ≈ g_{C[b]}* conflates the local restarted average with the global continuation value.

## FIX NEEDED
"replace the child-gain lump sum v_C(b) ≈ g_{C[b]}* by a true global continuation or relative-value object for the routed MDP"

## BOTTOM LINE
"v25 is a genuine conceptual improvement (single-player MDP reframing is correct). But the proof still fails at the same mountain pass, now in a cleaner form."

## STATUS AFTER 114 EP PASSES
Local machinery: FULLY VERIFIED (10+ independent reviews)
Global benchmark: STILL FAILING (10+ different approaches, all disproved or unproved)
The gap: converting local per-node Bellman bounds into a T-horizon epsilon-equilibrium
