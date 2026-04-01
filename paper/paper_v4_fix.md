# Paper v4 Fix (Pass 70)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the FIXER. A reviewer found three issues in the v4 manuscript. Fix ALL THREE in the LaTeX source. The attached `neyman_route_d_prime_v4.tex` is the current manuscript (2008 lines).

## Issue 1: Kakutani global nonemptiness (Section 3)

The reviewer says: local nonemptiness of N_C(x) does not imply nonemptiness of BR_eta(x) intersected with A_eta. Need to prove mutual consistency.

**How to fix**: The tree packages in A_eta are ALREADY defined as globally consistent collections. The local Nash sets N_C(x) are defined against the environment x which encodes the descendant values. The global correspondence BR_eta maps x to {y in A_eta : y_C in N_C(x) for all C}. Nonemptiness follows because:
- Each A_eta(C) (the local feasible set at node C) is compact and nonempty
- The local Nash set N_C(x) is nonempty (finite game has Nash eq)
- The constraints defining A_eta are LINEAR consistency conditions (flux = L(occupation))
- So the product of local Nash sets intersected with the linear consistency conditions is nonempty (the consistency is automatic by graph-VP3!)

This is EXACTLY the payoff of graph-VP3: the joint feasibility set is the graph of a linear map, so there's no separate compatibility to check. Make this argument explicit in the proof.

## Issue 2: Blockwise Bellman certificate (Section 6) — CRITICAL

The reviewer says: compliant occupation closeness doesn't imply deviation value closeness.

**How to fix**: Under condition (a), the deviator's MDP on node C has a BOUNDED bias span: sp(h) <= (|Xi_C|-1)/kappa_eta. This was proved in Pass 62 (46 min thinking). The key argument:
- Under condition (a), kappa_eta > 0 (minimum connector probability)
- The deviator's MDP has a unique invariant measure (irreducibility under condition (a))
- The bias function h satisfies ||h||_span <= (|Xi_C|-1)/kappa_eta
- Therefore the deviation value is LIPSCHITZ in the occupation measure with Lipschitz constant = bias span
- So |V_dev(mu_hat) - V_dev(mu)| <= sp(h) * ||mu_hat - mu||_1

This gives the needed continuity. Write this as a proper lemma with proof.

## Issue 3: Bias-span cardinality (minor)

Replace |S| with max_C |Xi_C| everywhere in the bias-span bound. The phase-state set Xi_C = ⊔_k {k} × S_C^k can be larger than |S|, but max_C |Xi_C| is still finite and depends only on the game.

## Your task

Read the attached v4 tex file. Apply all three fixes. Output the COMPLETE fixed LaTeX source (the full file, not just patches). Make the fixes mathematically rigorous — add new lemmas with proofs where needed.
