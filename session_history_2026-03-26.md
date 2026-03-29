# Session History: 2026-03-26 to 2026-03-27

## Overview
23 ChatGPT Extended Pro passes orchestrated by Claude Code via MathPipeProver pipeline (manual orchestration mode). Three fundamentally different proof architectures explored for Neyman's open problem (uniform equilibrium in finite stochastic games).

## Route B: Stationary Lexicographic (Passes 11-21)

### Passes
| # | Role | Key Result |
|---|------|-----------|
| 11 | Prover | One-step L4* FALSE — PD counterexample (eta >= 1/10) |
| 12 | Prover (block L4* W*) | Self-generation gap |
| 13 | Prover (block L4 full W) | Achievability != Equilibrium |
| 14 | Prover (APS bounded) | FALSE — additive recursion escapes |
| 15 | Prover (gain-bias discounted) | Lexicographic IC, not scalar |
| 16 | Prover (lexicographic) | **CONDITIONAL PROOF** |
| 17 | Reviewer + Literature | PATCH_SMALL + bias not known |
| 18 | Prover (patched + Puiseux) | Sharpened to H1+H2+H3 |
| 19 | Reviewer (self) | **PASS** |
| 20 | Prover (H3 via Mertens) | H3 NOT in literature |
| 21 | Prover (kappa counterexample) | **H3 FALSE** — concrete counterexample |

### Key Results
- **Conditional theorem (PASS)**: (H1+H2+H3) => uniform epsilon-equilibrium with O(1/T) regret
- **H3 counterexample**: 2-player absorbing game, unique analytic branch, kappa_1 = 1/4 > 0
- **Technique**: Novel lexicographic gain-bias decomposition
- **Conclusion**: Stationary limits of discounted Nash equilibria cannot close the theorem

## Route C: History-Dependent + Punishment (Passes 22-26)

### Passes
| # | Role | Key Result |
|---|------|-----------|
| 22 | Prover | Architecture identified: 4 deviation types, punishment + compensation |
| 23 | Prover | Absorbing subclass: compensation polytope empty without private signals |
| 24 | Prover | 4-player absorbing + public random: Kakutani fails, concrete counterexample |
| 25 | Prover | Autonomous correlation: public history insufficient for hidden roles |
| 26 | Prover | Embedded communication: cheap talk in public actions can't simulate private signals |

### Key Results
- **Deviation taxonomy**: gain-burning (auto), off-support (easy), within-support (D1), transition-tilting (D2)
- **Punishment architecture**: Fudenberg-Maskin phases + Vieille detection
- **4-player obstruction**: Blocked compensation polytope empty even with public randomization
- **Literature confirmed**: 4+ player absorbing Nash is smallest open class
- **Conclusion**: Punishment needs private communication channels

## Route D: Direct Topological (Pass 27)

### Key Results
- Raw strategy-space fixed-point refuted (wrong topology)
- **Route D'**: Work on compactified asymptotic state space
  - Quitting games: absorption paths (Ashkenazi-Golan)
  - Positive recursive absorbing: continuation-value orbits (Solan-Vieille 2025)
  - General stochastic games: correct compactification UNKNOWN
- **Conclusion**: Finding the right compact asymptotic object is the research frontier

## Publishable Results
1. Conditional theorem with PASS verdict (novel lexicographic gain-bias technique)
2. Three concrete counterexamples (L4*, bounded APS, H3)
3. Precise reduction to self-enforcing coalition punishment with private signals
4. Precise reduction to finding correct compact asymptotic state space
5. Literature survey confirming 4+ player absorbing Nash as smallest open class
