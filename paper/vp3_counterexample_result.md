# VP3 Counterexample — Pass 55

**Pass**: 55
**Role**: Prover (counterexample computation)
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 31m 19s

## VERDICT: VP3 IS FALSE (in literal product form)

On a 2-state, 2-exit, 2-player, 2-action gadget:
- Only 2 of 32 corners realized
- Support graph extremely sparse
- VP3 fails HARD

## Key Insight
beta(b) = sum_s sum_a x(s,a) * P(b|s,a)

Flux is a LINEAR FUNCTION of the occupation measure, not independent. The feasible (occ, flux) pairs lie on a thin rail (the graph of a linear map), not in the full product P_C x B_C.

## Missing Corner (explicit)
- x = occ(AA) = (9/10, 0, 0, 0; 1/10, 0, 0, 0)
- y = (1/100, 9/100) in ext(B_C)
- But x forces flux = (9/100, 1/100), the OPPOSITE of y
- Occupation at s1 forces exits through b1, not b2

## Implication for the Paper
The conditional theorem CANNOT use free product-form VP3. Instead:
1. **Option A**: Reformulate VP3 as a joint-germ theorem using the LIFTED occupation-exit polytope (Searcher Strategy 2)
2. **Option B**: The flux IS determined by the occupation measure — so VP3 is automatically satisfied in the lifted formulation, and the "gap" may not exist at all!

## Critical Realization
If beta = L(mu) for a linear map L, then knowing mu automatically determines beta. The "separate" decomposition problem was an artifact of treating them as independent. In the CORRECT formulation where we work with the joint occupation-exit polytope, VP3 may be trivially true.

This changes everything.
