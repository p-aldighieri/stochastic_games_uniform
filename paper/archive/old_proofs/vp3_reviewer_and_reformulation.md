# VP3 Reviewer + Reformulation (Pass 56)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are BOTH a reviewer AND a prover in this pass. Two tasks:

### Task 1: REVIEW the counterexample (from Pass 55)
The prover computed a 2-state, 2-exit gadget and found VP3 false: only 2 of 32 corners realized. The key finding: flux is a LINEAR function of occupation, so treating them as independent variables is wrong.

Verify:
1. Is the gadget correctly set up?
2. Are the 16 policy computations correct?
3. Is the extreme-point identification correct?
4. Is the missing-corner argument valid?
5. Does this genuinely refute VP3 in product form?

### Task 2: REFORMULATE — does the lifted version resolve VP3?

The critical observation from Pass 55: beta(b) = sum_s sum_a x(s,a) * P(b|s,a). Flux is LINEAR in occupation.

This means: if we define the joint map F(theta) = (occ(theta), flux(theta)), then flux(theta) = L(occ(theta)) for some fixed linear map L. So:

conv{(occ(theta), flux(theta))} = conv{(occ(theta), L(occ(theta)))} = {(mu, L(mu)) : mu in conv{occ(theta)}} = graph(L) cap (P_C x R^d2)

This is NOT a product — it's the GRAPH of L restricted to P_C. And the "compatibility condition" becomes:

For any mu in P_C, is beta = L(mu) automatically in the feasible flux set?

If yes, VP3 is TRIVIALLY TRUE in the lifted formulation, because flux is determined by occupation.

PROVE OR DISPROVE: In the lifted (joint occupation-exit) formulation where beta = L(mu), is VP3 automatically satisfied? If so, the conditional theorem becomes UNCONDITIONAL.

This is potentially the most important mathematical step in the entire project.
