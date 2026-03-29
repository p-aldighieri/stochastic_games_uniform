# Breakdown Response: Strategy 1 — Metastable Occupation-Flux Tree

**Source**: ChatGPT Extended Pro, "Proof Breakdown Request" chat
**Date**: 2026-03-27
**Role**: Breakdown
**Pass**: 29 (second Route D' pass)
**Chat URL**: https://chatgpt.com/g/g-p-69b78396b3808191ad15bcc609e7ebf6-game-theory-proof/c/69c6dc3a-1f98-832c-b5b5-82280136f19d
**Length**: 33,307 characters

## Summary

Complete proof breakdown for the Metastable Occupation-Flux Tree strategy. Contains:

### Definitions (1.1-1.6)
- **1.1 Tree chart**: Finite rooted DAG of communicating classes with rank, phase partitions, macro-exits
- **1.2 Extended phase-state spaces**: Phase-labeled state-action spaces per node
- **1.3 Node coordinates**: 8 coordinates per node — mu_C, pi_C, x_C, P_C^0, Lambda_C, alpha_C, q_C, g_C, v_C, b_C
- **1.4 Consistency equations (C1-C9)**: Support/disintegration, flow balance, phase cyclicity, gain definition, exit-rate consistency, exit-law support, continuation recursion, bias normalization, local lexicographic Bellman
- **1.5 Global tree space**: Union over finite set of admissible charts
- **1.6 Relaxed tree space A_eta**: eta-approximate versions for Kakutani

### 20-Lemma Sequence
| # | Name | Status | Deviation Types |
|---|------|--------|-----------------|
| 1 | Periodic principal decomposition | KNOWN | Structural |
| 2 | Local gain-bias Poisson system | KNOWN | Gain-burning, within-support |
| 3 | Uniform boundedness of normalized bias | HARD | All (compactness) |
| 4 | Puiseux finite-scale lemma | HARD | D2 infrastructure |
| 5 | Finite-chart lemma | STRAIGHTFORWARD | Structural |
| 6 | Projective exit extraction | HARD | D2 representation |
| 7 | Sequential compactness of long-block profiles | HARD | Creates compact object |
| 8 | Split/merge closure of compactification | HARD | Compactness |
| 9 | Continuity of recursive payoff data | STRAIGHTFORWARD | None |
| 10 | Deviation reduction to nodewise Markov | STRAIGHTFORWARD | All 4 |
| 11 | Gain-burning lemma | KNOWN | Gain-burning |
| 12 | Off-support gap lemma | STRAIGHTFORWARD | Off-support |
| 13 | Within-support D1 continuity | HARD | D1 |
| 14 | Transition-tilting D2 linear-response | HARD | D2 |
| 15 | Full deviation functional upper semicontinuity | HARD | All 4 |
| 16 | Nonempty convex best-response on A_eta | HARD | All 4 |
| 17 | Kakutani fixed point | KNOWN (given L16) | All 4 |
| 18 | Implementability by growing blocks | HARD | All 4 |
| 19 | Tree-to-horizon transfer | HARD | All 4 |
| 20 | Fixed point implies uniform eps-equilibrium | STRAIGHTFORWARD | All 4 |

### Critical Path
Lemma 4 → Lemma 6 → Lemma 8 → Lemma 14 → Lemma 16 → Lemma 18 → Lemma 19

### Bottlenecks
- **Global bottleneck**: Lemma 18 (Implementability by growing blocks) — theorem-sized
- **Local algebraic bottleneck**: Lemma 14 (D2 transition-tilting linear response)

### Puiseux Engine Entry Points
- **Engine A** (Lemma 4): Finite Puiseux expansion for all local coordinates near lambda=0
- **Engine B** (Lemma 14): First-order exit coefficients define continuous tensor

### Bottom Line (from breakdown)
Route is coherent iff:
1. D2 deviations are fully captured by continuous exit-susceptibility data (L14)
2. Every relaxed fixed point can be implemented by one horizon-independent growing-block profile (L18)
