# Prover Request: Section 3 — The Metastable Tree Object (Pass 47)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-28

## Instructions

You are the prover role. Write the complete Section 3 of our paper: "The Metastable Tree Object." The scope gatekeeper says this is 4-5 pages, DEFINITION + COMPACTNESS standard.

## What This Section Must Contain

1. **The tree structure**: Define the metastable tree T = (V, E, root) where each node C corresponds to a communicating class of the Markov chain under joint play, and the tree encodes the hierarchical decomposition of state space into metastable regions.

2. **Node data**: For each node C, define the local data tuple:
   - mu_C: stationary occupation measure within C
   - alpha_C: projective exit-rate vector
   - beta_C(e,b): boundary flux (unnormalized, from Section 4)
   - g_C: local payoff vector (one per player)
   - v_C: continuation value vector
   - Phase data: period, phase labeling

3. **Consistency equations (C1-C9)**: The 9 equations that the tree data must satisfy:
   - Flow conservation at each node
   - Exit-rate / occupation compatibility
   - Payoff recursion
   - Continuation-value recursion linking parent to children
   - Phase consistency across boundaries

4. **The relaxed tree space A_eta**: Define the eta-relaxed version where equalities become eta-approximate inequalities. This is the space where the fixed-point argument lives.

5. **Compactness theorem**: Prove that A_eta is compact (in the product topology). Key: each coordinate lives in a compact set, and the consistency constraints are closed.

## Notation (from v2 draft)

- xi for phase-states (not x)
- beta_C(e,b) = alpha_C(e) * q_C(e,b) — unnormalized flux (defined in Section 4)
- alpha_C — projective exit-rate vector
- Out(C) — exit set
- mu_C — occupation measure
- g_C — payoff vector
- v_C — continuation value

## Output Format

LaTeX-ready mathematical prose. Numbered definitions/propositions. ~4-5 pages. This is the central object definition section — it must be precise and complete.
