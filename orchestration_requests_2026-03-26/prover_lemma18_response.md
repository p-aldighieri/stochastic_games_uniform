# Prover Response: Lemma 18 — Implementability by Growing Blocks

**Source**: ChatGPT Extended Pro, "Lemma 18 Implementability" chat
**Date**: 2026-03-27
**Role**: Prover
**Pass**: 31 (fourth Route D' pass)
**Chat URL**: https://chatgpt.com/g/g-p-69b78396b3808191ad15bcc609e7ebf6-game-theory-proof/c/69c6f0dd-8d00-832b-8e09-72cbe20f6936
**Length**: 6,908 characters

## VERDICT: CONDITIONAL

Lemma 18 is provable IF every node of the relaxed fixed point comes with a **uniform public local realization certificate** (synchronization, phase control, mixing-vs-exit separation). With only jet-enriched tree data (mu_C, alpha_C, q_C, J_C), Lemma 18 is NOT proved.

## What IS Proved (under the extra hypothesis)

Given nodewise public realization certificates, the global growing-block assembly is **standard**:
- Superexponential schedule L_{m+1} = L_m^2
- Public memory: current node, block index, phase label
- Exit detection is public (states and actions are public)
- Cumulative leakage density → 0
- One horizon-independent schedule works for all initial states and all large T

## What Is Missing (the exact obstruction)

Three certificates are needed but not provided by the tree data:

1. **Nodewise public realizability / purification**: Each local tree datum must be realizable uniformly from every entry state by a public block controller
2. **Time-scale separation certificate**: Internal equilibration must occur on scale o(B) while leading exits remain rare on the next scale
3. **Phase certificate**: Periodic classes need a finite public phase clock or explicit reset-to-canonical-phase map

## Key Insight

> "The jets describe the shadow, not the engine. Implementing every relaxed fixed point would amount to a dynamic purification theorem from convexified asymptotic data to one actual public profile, and that theorem is exactly the missing step."

The bottleneck doesn't vanish by folding certificates into A_eta — it merely migrates. Compactness and fixed-point arguments must be rebuilt on the stronger certified space.

## Statement Repairs Needed

1. "Public finite-memory" should mean public time-dependent strategy with finite local mode (not fixed finite automaton counting unbounded schedule)
2. Item 4 should use cumulative leakage density o(T), not absolute summability

## Satisfiability Assessment

- **Solved subclasses** (quitting, positive recursive absorbing, 2-player zero-sum): Hypothesis is believable and often already present in disguised form
- **General finite stochastic games**: NOT currently satisfiable from Route D' data alone — it is essentially another theorem-sized local realization theorem

## Impact on Route D'

The critical path now has TWO theorem-sized gaps:
1. **Lemma 14** (D2 linear response): CONDITIONAL — repaired by finite exit jets ✓
2. **Lemma 18** (Implementability): CONDITIONAL — needs nodewise public realization certificates ✗

The second gap is the deeper one. The tree object A is well-defined and compact, deviation functionals are (upper semi-)continuous, Kakutani gives a fixed point — but bridging from the abstract fixed point to an actual strategy profile requires a **local purification theorem** that is itself theorem-sized.

## Next Steps

Options:
A. Attack the nodewise public realization certificate directly (new prover pass)
B. Try to fold the certificates into A_eta and reprove compactness on the certified space
C. Pivot to Strategy 5 (recursive collapsing to quitting skeletons) where realization is easier
D. Accept this as a conditional theorem and write up the architecture as a publishable reduction
