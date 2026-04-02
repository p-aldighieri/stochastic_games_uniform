# v8 Review — Pass 80

**Thinking**: 43 min 9s Extended Pro
**Verdict**: CONDITIONAL (first non-FAIL from EP!)

## What PASSES
- Renewal-reward identity: CONFIRMED FIXED (restart-bias gone)
- Local controller theorem: PASS (best part of rewrite)
- Frozen-memory lemma: PASS
- Bookkeeping, polytope, graph theorem, coefficient-affinity: PASS
- Within-block Bellman: PASS (exact coefficients, no perturbation)
- Bibliography: complete

## Remaining issues (all likely patchable)

### 1. Gain box too small [MAIN BLOCKER]
Local gain constrained to [0,1] but renewal-reward formula gives g = sum mu*u + sum beta*v which can exceed 1. Toy: u=1, exit prob=1, continuation=1 gives g=2. Need depth-dependent box or different normalization.

### 2. Prelude blocks not peeled off
Block regret proved only for complete blocks with cap >= M*. Frozen prelude has smaller caps. Need to absorb finitely many prelude blocks into K_eta/T remainder.

### 3. Terminal label routing
Public routing doesn't specify what happens when C[b] is a terminal label (not a child node). Under-specified.

## Assessment
These are all PATCHABLE — no structural rewrites needed. The gain-box is a constant/normalization fix. The prelude and terminal issues are bookkeeping. One more fix pass should close this.
