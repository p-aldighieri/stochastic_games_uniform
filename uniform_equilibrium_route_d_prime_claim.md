# Route D' Claim: Uniform Equilibrium via Compact Asymptotic State Space

## The Theorem Target (unchanged)
For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist a strategy profile sigma and threshold T_0 such that for all T >= T_0, all initial states s, all players i, all unilateral deviations tau_i:
gamma_i^T(s, sigma) >= gamma_i^T(s, (tau_i, sigma_{-i})) - epsilon.

## The Approach: Route D'
Construct a compact asymptotic state space A for general finite stochastic games, with continuous payoff and deviation functionals, and prove existence of uniform equilibrium via fixed-point theorem on A.

## What We Know (from 23 prior Extended Pro passes)

### What DOESN'T work
1. **Stationary limits** (Route B): H3 (bias-level optimality) is provably false — concrete counterexample
2. **History-dependent punishment** (Route C): Self-enforcing coalition punishment needs private signals unavailable from public actions
3. **Raw strategy-space fixed-point** (Route D): Wrong topology — payoff not continuous, space not compact

### What DOES work in solved subclasses
- **Quitting games**: Absorption paths as the compact space (Ashkenazi-Golan et al.)
- **Positive recursive absorbing**: Continuation-value orbits (Solan-Vieille 2025)
- **2-player zero-sum**: Algebraic value structure (Mertens-Neyman, Bewley-Kohlberg)

### Reusable infrastructure from our work
- **Gain-bias decomposition**: The lexicographic gain-bias structure from the conditional theorem gives the right payoff decomposition
- **Deviation taxonomy**: 4 types of deviations (gain-burning, off-support, within-support, transition-tilting) from Route C
- **Block structure**: Growing blocks with summable leakage from the block-selector work

## What Route D' Must Do
1. **Define A** for general finite stochastic games — encoding occupation measures, exit intensities, continuation values, and gain-bias structure for each communicating set of states
2. **Prove compactness** with continuous payoff and deviation functionals
3. **Prove fixed-point existence** via Kakutani on a self-map of A
4. **Prove implementability** — each fixed point yields an actual strategy profile that is a uniform epsilon-equilibrium
