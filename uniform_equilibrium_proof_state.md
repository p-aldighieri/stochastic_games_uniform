# Uniform Equilibrium Proof State

- Project: Game Theory Proof (Neyman's Open Problem)
- Claim file: `uniform_equilibrium_stochastic_games_problem.md`
- Status: Route D' deep dive — 7 Extended Pro passes (28-34), proper pipeline discipline
- Theorem status: OPEN — reduced to ONE crisp item: finite boundary-flux/phase-reset witness existence
- Durable sources for ChatGPT project:
  - `uniform_equilibrium_stochastic_games_problem.md` (problem statement, unchanged)
  - `uniform_equilibrium_proof_state.md` (this file)
  - `uniform_equilibrium_route_memo.md` (route analysis)

## Prior Session Summary (2026-03-26 to 2026-03-27)

23 Extended Pro passes across 3 architectures. Full history in `session_history_2026-03-26.md`.

### Route B (Stationary Lexicographic) — EXHAUSTED
- Conditional theorem PASS: (H1+H2+H3) => uniform equilibrium, O(1/T) regret
- H3 is FALSE: concrete counterexample (2-player absorbing, kappa=1/4>0)
- Stationary limits of discounted Nash equilibria cannot close the theorem

### Route C (History-Dependent Punishment) — EXHAUSTED
- Correct architecture: gain supermartingale + bias-level punishment + Vieille detection
- Self-enforcing coalition punishment needs private signals
- Public actions/history/randomization insufficient for hidden role assignments
- 4+ player absorbing Nash confirmed as smallest open class

### Route D (Direct Topological) — RAW VERSION REFUTED, D' IDENTIFIED
- Raw Brouwer/Kakutani on strategy space fails (wrong topology)
- **Route D'**: Work on compactified asymptotic state space
  - Quitting games solved via absorption paths
  - Positive recursive absorbing solved via continuation-value orbits
  - General finite stochastic games: correct compactification UNKNOWN

## Current Direction: Route D' — Metastable Occupation-Flux Tree

### Route D' Passes (2026-03-27, continued session)

| Pass | Role | Result |
|------|------|--------|
| 28 | Searcher | 5 strategies identified; recommended Strategy 1 (Metastable Flux Tree) |
| 29 | Breakdown | 20-lemma sequence with critical path L4→L6→L8→L14→L16→L18→L19 |
| 30 | Prover (L14) | **CONDITIONAL** — D2 linear response needs finite exit jets (repair accepted) |
| 31 | Prover (L18) | **CONDITIONAL** — Implementability needs nodewise public realization certificates |

### What We Now Know

**The compact object is well-defined**: Phase-labeled metastable tree carrying (mu_C, P_C^0, J_C, alpha_C, q_C, g_C, v_C, b_C) per node, with 9 consistency equations (C1-C9). Compactness holds on relaxed tree space A_eta.

**Kakutani gives a fixed point**: Once deviation functionals are upper semicontinuous (via jet-enriched D2 data), the best-response correspondence has closed graph and Kakutani applies.

**The gap is implementation, not existence**: The abstract fixed point exists in A_eta. The missing theorem is a **nodewise public purification/realization** that converts each node's asymptotic data into an actual public block controller. This requires:
1. Uniform entry-state synchronization
2. Phase control for periodic classes
3. Mixing-vs-exit time-scale separation certificate

### Precise Reduction

The theorem (uniform epsilon-equilibrium in finite stochastic games) is now reduced to:

**For every node C in a jet-enriched metastable tree, every entry state, and every sufficiently large block length B, there exists a public block controller that realizes the node's occupation, exit, and phase data within eta, with reset cost o(B) and leakage density going to 0.**

### Options Forward

A. Attack the nodewise realization certificate directly (new prover pass)
B. Fold certificates into A_eta and reprove compactness on certified space
C. Pivot to Strategy 5 (recursive collapsing to quitting skeletons)
D. Accept as conditional theorem and write up the reduction as publishable

**References to exploit**:
- Ashkenazi-Golan et al.: absorption paths for quitting games
- Solan-Vieille 2025: continuation-value orbits for positive recursive absorbing
- Mertens-Neyman: algebraic approach to stochastic game limits
- Bewley-Kohlberg: Puiseux expansion / asymptotic structure
- Our conditional theorem: gain-bias decomposition is reusable infrastructure
