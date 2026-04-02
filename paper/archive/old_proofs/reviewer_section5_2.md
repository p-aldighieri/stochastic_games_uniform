# Reviewer Request: Section 5.2 — Boundary-Flux Witness (Pass 44)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-28

## Instructions

You are the REVIEWER for Pass 43 (Section 5.2 — Boundary-Flux Witness). The prover wrote a complete proof of Proposition 5.2. Your job is a line-by-line mathematical review.

## What the prover was asked to write

The complete proof of Proposition 5.2 (Boundary-Flux Witness) — a subordinate result to the Ergodic Occupation Realization (Theorem 5.1). The proof defines an augmented state space with cemetery states, establishes the occupation polytope P_C, proves the affine map L_C, uses L(conv V) = conv(L(V)), and applies Caratheodory. Uses flux coordinates beta = alpha*q throughout.

## Review Checklist

For each item, give PASS / CONDITIONAL / FAIL with a one-line reason:

1. **Augmented state space**: Is the augmented state space with cemetery states correctly defined? Are transitions properly redirected?
2. **Occupation polytope P_C**: Is P_C correctly characterized as the set of feasible occupation measures?
3. **Affine map L_C**: Is L_C correctly shown to be affine? Is the map from occupation measures to (alpha, beta) data correct?
4. **Flux coordinate argument**: Is the key insight correct — that beta is linear in occupation measure m, while normalized q = beta/alpha introduces a discontinuous division?
5. **L(conv V) = conv(L(V))**: Is this identity correctly applied? Does L need to be affine (not just linear) for this?
6. **Caratheodory**: Is Caratheodory correctly applied? Is the dimension bound correct?
7. **Notation**: Does the proof use our notation (xi for phase-states, beta for flux, Out(C), etc.)?
8. **Scope**: Is this a clean subordinate result that correctly supports Theorem 5.1?

## Verdict

After the checklist, give one of:
- **PASS** — ready for the paper as-is
- **UPGRADE** — correct and exceeds expectations
- **CONDITIONAL** — mostly correct but needs specific fixes (list them)
- **FAIL** — fundamental errors (list them)

## The Proof Text

The full proof follows in the attached file `section5_2_flux_witness_proof.md`.
