# Research Notes: Uniform Equilibrium in Finite Stochastic Games

## 1. Repository Structure Analysis

### Files and Directories

| Path | Type | Purpose |
|------|------|---------|
| `uniform_equilibrium_stochastic_games_problem.md` | Markdown | **Primary problem statement document.** Contains the full formalization of Neyman's open problem on uniform equilibrium in finite stochastic games, including: formal model (Section 2), payoff criteria and equilibrium definitions (Section 3), solution criteria (Section 4), attack strategies (Section 5), computational workflow (Section 6), research roadmap (Section 7), and a Lean formalization blueprint (Section 8). |
| `234153_uniform_equilibrium_resolution_criterion.pdf` | PDF | **Resolution criteria document.** Specifies what constitutes a valid solution (positive or negative) to the open problem. Contains Lean 4 code skeletons for formal verification. |
| `research_rubric.json` | JSON | **Research execution plan.** Contains 27 items across 5 phases, tracking progress of the computational research effort. Managed by the orchestrator/researcher agent pipeline. |
| `.gitignore` | Config | Excludes build artifacts, secrets (.env, .key, .pem), agent logs (TASK_*.md), and orchestration infrastructure (.claude/, .codex/, .archivara/). |
| `.gitattributes` | Config | **Git LFS configuration.** Tracks large binary files (*.zip, *.tar.gz, *.csv, *.hdf5, *.feather, *.npz, *.pickle, *.parquet, *.npy, *.pkl, *.gz, *.obj, *.stl, *.h5) via Git Large File Storage. Relevant for storing large experimental output datasets. |
| `sources.bib` | BibTeX | **Bibliography file.** Created for this research effort; will accumulate citations to all consulted papers, tools, and implementations. |
| `figures/` | Directory | **Output directory for visualizations.** Will contain publication-quality PNG and PDF figures from experiments (regret trajectories, convergence plots, heatmaps, etc.). Currently empty. |
| `results/` | Directory | **Output directory for experimental data.** Will contain JSON files with numerical results from all computational experiments. Currently empty. |
| `stoch_game/` | Directory | **Python package directory.** Will contain the core implementation: game data structures, payoff computation, MDP solver, regret analysis, and equilibrium solvers. Currently empty. |
| `.archivara/logs/` | Directory | Agent orchestration logs (excluded from commits by .gitignore). |
| `TASK_researcher_attempt_1.md` | Markdown | Task specification for the researcher agent (excluded from commits by .gitignore). |

### Current State of the Repository

- **No code exists yet.** The `stoch_game/` directory is empty; all computational infrastructure must be built from scratch.
- **No experimental results exist yet.** The `results/` and `figures/` directories are empty.
- **No bibliography entries yet.** `sources.bib` contains only a header comment.
- **Problem statement is complete and well-formalized.** The `.md` file provides a thorough, proof-oriented formulation of Neyman's open problem with explicit quantifiers, formal definitions, and both positive and negative solution criteria.
- **Resolution criteria PDF is available** for reference on what constitutes a valid solution, including Lean formalization targets.

### Connection to the Research Problem

The repository is set up as a fresh computational research project for investigating Neyman's open problem on uniform equilibrium existence in finite stochastic games. The problem statement document provides the mathematical foundation; the research rubric provides the execution plan. All computational work (game implementations, solvers, experiments, analysis) will be built in this repo during the research phase.

---

## 2. Formal Problem Statement

### Neyman's Open Problem (Full Quantified Form)

**Conjecture (Uniform Equilibrium Existence).** For every finite stochastic game G = (N, S, (A_i)_{i in N}, u, P) and every epsilon > 0, there exists a strategy profile sigma = (sigma_1, ..., sigma_n) and a horizon threshold T_0 in N such that for all T >= T_0, for all players i in N, for all initial states s_1 in S, and for all deviation strategies tau_i:

gamma_i^T(s_1, sigma) >= gamma_i^T(s_1, (tau_i, sigma_{-i})) - epsilon

where gamma_i^T(s_1, sigma) = E_{s_1, sigma}[(1/T) sum_{t=1}^{T} u_i(s_t, a_t)] is the expected T-stage average payoff.

**Equivalently:** For all G, for all epsilon > 0, there exists sigma such that sigma is a uniform epsilon-equilibrium.

### Distinctions from Related Notions

| Notion | Definition | Status |
|--------|-----------|--------|
| **Uniform epsilon-equilibrium** (target) | Single sigma works for ALL T >= T_0 simultaneously | OPEN for n >= 3 |
| **Horizon-dependent equilibrium** | For each T, there exists sigma^T that is epsilon-NE for that T | Known to exist (backward induction) |
| **Discounted equilibrium** | NE of the delta-discounted game | Exists for all delta < 1 (Fink 1964) |
| **Uniform correlated equilibrium** | Uniform epsilon-CE (correlated deviations) | Exists (Solan-Vieille 2002) |
| **Restricted-deviation equilibrium** | Only certain strategy classes can deviate | Various partial results |

The key distinction: uniform epsilon-equilibrium requires a SINGLE strategy profile that simultaneously works for all sufficiently long horizons, using Nash (unilateral) deviations. This is strictly stronger than horizon-dependent existence and is not implied by correlated equilibrium existence.

---

## 3. Computational Tools Survey

| Tool | Language | Capabilities | Limitations | Relevance |
|------|----------|-------------|-------------|-----------|
| **Gambit** (v16.5) | C++/Python | Compute Nash equilibria in extensive and strategic form games; support enumeration, Lemke-Howson, iterated polymatrix approximation, linear complementarity | No native stochastic game support; focused on one-shot games; limited scalability for large state spaces | Useful for computing stage-game Nash equilibria and static equilibrium benchmarks |
| **Nashpy** (v0.0.43) | Python | 2-player Nash equilibria via support enumeration, vertex enumeration, Lemke-Howson; also fictitious play, replicator dynamics | 2-player only; no stochastic game dynamics; no discounted/average payoff computation | Useful as a subroutine for 2-player stage-game equilibria within our framework |
| **PRISM-games** (v3.0) | Java | Model checking for stochastic multi-player games; Nash equilibria synthesis; supports concurrent and turn-based games with omega-regular objectives | Focused on verification/synthesis with qualitative/quantitative temporal logic properties; not designed for average-payoff uniform equilibrium analysis | Could verify properties of specific game instances; supports Nash equilibria in concurrent stochastic games |
| **sgamesolver** | Python | Compute stationary/Markov-perfect equilibria of stochastic games via homotopy continuation (QRE and LogTracing methods) | Computes stationary (discounted) equilibria, not uniform equilibria; may struggle with large state spaces | **Most directly relevant tool.** Can compute discounted equilibria as delta -> 1, providing candidate uniform equilibrium payoffs |
| **MarkovGameSolvers** | Python | Zero-sum and general-sum Markov game solvers; Nash, Stackelberg, minimax via LP (PuLP) | Limited to simple game structures; research prototype quality | Useful for zero-sum benchmarking; LP-based approach is fast |
| **QuantEcon** | Python | Markov perfect equilibrium in linear-quadratic games; educational tutorials | Restricted to LQ structure; not for general finite stochastic games | Educational reference; not directly applicable |

### Decision for This Project
We will build our own framework (in `stoch_game/`) because:
1. No existing tool directly computes or verifies **uniform** epsilon-equilibria
2. We need exact control over: horizon-dependent payoff computation, best-response MDP solving, regret trajectory analysis
3. We can use **sgamesolver** as a reference for discounted equilibria and **Nashpy** for 2-player stage-game subroutines
4. Custom implementation allows phase-based strategy construction and counterexample search

---

## 4. Taxonomy of Known Results and Open Frontier

### Solved Classes (Uniform Equilibrium Existence Proved)

| Class | Players | Structure | Result | Reference |
|-------|---------|-----------|--------|-----------|
| **(a) 2-player zero-sum** | 2 | Arbitrary finite | Uniform value exists; epsilon-optimal strategies exist | Mertens-Neyman 1981 |
| **(b) 2-player general-sum** | 2 | Arbitrary finite | Uniform equilibrium payoff exists | Vieille 2000 I & II |
| **(c) 3-player absorbing** | 3 | At most one state change (absorbing) | Uniform equilibrium exists | Solan 1999 |
| **(d) 3-player quitting** | 3 | Single non-absorbing state | Equilibrium exists | Solan-Vieille 2001 |
| **(e) n-player correlated** | Any n | Arbitrary finite | Uniform correlated equilibrium exists (autonomous device) | Solan-Vieille 2002 |
| **(f) n-player recursive positive** | Any n | Positive recursive, non-rectangular absorption | Undiscounted equilibrium exists | Ashkenazi-Golan et al. 2025 |
| **(g) 2-player shift-invariant** | 2 | Arbitrary finite, shift-invariant payoffs | epsilon-equilibrium exists | Flesch-Solan 2023 |
| **(h) n-player product-state** | Any n | Each player controls one state component | Uniform equilibrium exists | Flesch et al. (product games) |

### Open Cases (Uniform Nash Equilibrium NOT Yet Proved)

| Class | Players | Structure | Status | Notes |
|-------|---------|-----------|--------|-------|
| **(i) n-player general Nash** | n >= 3 | Arbitrary finite stochastic game | **OPEN** | This is Neyman's open problem |
| **(j) 4+ player absorbing** | n >= 4 | Absorbing games | **OPEN** | Not known whether 4-player absorbing games always have uniform NE |
| **(k) 4+ player quitting** | n >= 4 | Quitting games | **OPEN** | Simplest open case for multiplayer |
| **(l) 3-player general** | 3 | Non-absorbing, general finite | **OPEN** | Known only for absorbing subclass |

### The Exact Frontier

The gap is specifically:
- **Nash (not correlated) uniform equilibrium** for **n >= 3 players** in **general finite stochastic games**
- The correlated version is solved for all n (Solan-Vieille 2002)
- The Nash version is solved for n = 2 (Vieille 2000)
- For n = 3, only special subclasses are solved (absorbing: Solan 1999; quitting: Solan-Vieille 2001)
- For n >= 4, even absorbing and quitting games remain open
- The simplest completely open case: **3-player non-absorbing stochastic games with >= 2 states**
- Recent progress (2025): Recursive absorbing with non-rectangular absorption solved; with public correlation device, all positive recursive games solved

### Key Structural Observations
1. The difficulty is fundamentally about **Nash** vs. **correlated**: correlation devices allow information sharing that resolves coordination problems
2. In multiplayer games, cyclic equilibria (Flesch-Thuijsman-Vrieze 1997) show that equilibrium structure can be qualitatively different from 2-player case
3. Memory requirements matter: in the Big Match, bounded memory strategies fail (Hansen-Ibsen-Jensen-Neyman 2025), but O(log n) memory suffices for zero-sum uniform value
4. Computational complexity: finding Nash equilibria in stochastic multiplayer games can be undecidable with payoff constraints (Ummels-Wojtczak 2011)

