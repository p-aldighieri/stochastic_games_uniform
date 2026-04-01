# Paper v9 Fix — Pass 81

## Instructions

You are the REWRITER. A 43-minute Extended Pro review gave v8 a CONDITIONAL verdict — the first non-FAIL! Three patchable issues remain. Fix ALL THREE.

## Issue 1: Gain box [0,1] too small

The gain g*_{i,C} = sum mu*u + sum beta*v can exceed 1 (toy: u=1, exit prob=1, continuation=1 gives g=2). The ambient compact set constrains gains to [0,1], which is too small.

**FIX**: Replace [0,1] with [0, D] where D = depth of the tree (or max number of nodes on any root-to-leaf path). Since each node adds at most 1 to the gain via stage payoffs, and continuation values propagate through at most D levels, the correct box is [0, D]. Alternatively, normalize payoffs so that the per-stage payoff is in [0, 1/D], making gains fit in [0,1]. The cleanest fix: set the gain box to [0, ||u||_inf / (1-max exit rate)] or simply [-M, M] for some M depending only on game data.

## Issue 2: Prelude blocks

Block regret proved only for cap >= M*. Frozen prelude has finitely many smaller caps.

**FIX**: Add one sentence in the main proof: "The finitely many prelude blocks (before the superexponential schedule reaches cap M*) contribute at most K_eta to the total payoff, hence at most K_eta/T to the average. This is absorbed into the K_eta/T remainder term."

## Issue 3: Terminal label routing

Public routing doesn't specify behavior when C[b] is a terminal label.

**FIX**: Add: "If exit label b leads to a terminal label rather than a child node, the block terminates and play continues according to the terminal continuation profile w(b). Since terminal labels have no further tree structure, no additional blocks are scheduled at that label."

## Your task

Read the attached v8 tex. Apply ALL 3 fixes. Output the COMPLETE v9 LaTeX source.
