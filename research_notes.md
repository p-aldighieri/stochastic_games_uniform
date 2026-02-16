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

