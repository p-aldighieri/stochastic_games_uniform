# VP3 Searcher — Pass 54

**Pass**: 54
**Role**: Searcher
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 28m 29s

## Key Insight
**VP3 (literal product form) is likely FALSE.** The searcher's blunt verdict: "if your feasible target really means the full product P_C x B_C, then VP3 is probably false and a two-state rare-exit missing-corner gadget should exist."

## Equivalence Found
VP3 is equivalent to EXTREME-CORNER COMPLETION: every extreme occupation point can be paired with every extreme flux point by some deterministic stationary policy. I.e., the bipartite support graph between ext(P) and ext(B) must be complete bipartite.

## 7 Strategies Identified
1. **Extreme-corner completion** (6/10) — prove bipartite completeness
2. **Lift to joint occupation-exit polytope** (6/10) — RECOMMENDED as most promising
3. **Farkas-dual obstruction killing** (7/10) — show no separator exists
4. **Fiberwise flux polytope** (8/10) — strengthen Section 5.2 to fiberwise feasibility
5. **Two-time-scale policy surgery** (8/10) — exploit metastability separation
6. **Augment boundary flux into occupation** (6/10) — absorbing-state trick
7. **Discounted branch alignment** (7/10) — prove at delta<1, pass to limit

## Recommended Next Move
Compute K_{2,2} support graph for smallest 2-state rare-exit node. This determines whether VP3 holds or needs reformulation.

## If VP3 Fails
Replace with joint-germ theorem using Strategy 2 (lift to joint object). This dovetails with Route D'.
