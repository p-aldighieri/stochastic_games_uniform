# External Agent Request (searcher)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-27T13:00:00.000000+00:00

## Instructions

You are the searcher role. Your task is to find **proof strategies** for proving uniform epsilon-equilibrium existence in finite stochastic games via a compact asymptotic state space (Route D').

The theorem target is unchanged: for every finite stochastic game G and every epsilon > 0, there exist sigma and T_0 such that sigma is a uniform epsilon-equilibrium for all T >= T_0.

## What Has Been Tried and Failed (from 23 prior passes)

### Route B (Stationary): DEAD
- Limit of discounted Nash equilibria fails bias-level optimality (H3 provably false)
- Concrete counterexample: kappa_1 = 1/4 > 0 on gain-neutral action

### Route C (History-Dependent Punishment): DEAD
- Self-enforcing coalition punishment needs private signals
- Public actions/history/randomization insufficient for hidden role assignments
- 4+ player absorbing Nash is smallest open class

### Route D (Raw Fixed-Point): DEAD
- Strategy space not compact in the right topology
- Payoff functionals not continuous

## What Works in Solved Subclasses

| Subclass | Compact Object | Key Technique | Reference |
|----------|---------------|---------------|-----------|
| Quitting games | Absorption paths | Continuous payoff on path space | Ashkenazi-Golan et al. |
| Positive recursive absorbing | Continuation-value orbits | Self-map on value domain + finite orbits | Solan-Vieille 2025 |
| 2-player zero-sum | Algebraic value structure | Puiseux expansion / operator theory | Mertens-Neyman, Bewley-Kohlberg |
| 2-player non-zero-sum | Communicating sets + punishment | State-by-state construction | Vieille 2000 |
| 3-player absorbing | Special structure | Solan |

## What Route D' Must Find

A compact asymptotic state space A for general finite stochastic games, encoding:
- **Occupation measures**: time spent in each state
- **Exit intensities**: transition rates between communicating sets
- **Continuation values**: expected payoffs after exit
- **Gain-bias structure**: lexicographic decomposition (from our conditional theorem)

Plus an implementability map A → Σ and deviation functionals that are continuous on A.

## Your Task

Search for **3-5 distinct proof strategies** for constructing A and proving it works. For each strategy:

1. **Name** the strategy concisely
2. **Describe** the compact object and the key topological/algebraic ingredient
3. **Identify** the main technical obstacle
4. **Assess** feasibility (high/medium/low) based on what's known
5. **Cite** relevant literature that supports or constrains the approach

Consider approaches from:
- Occupation measure compactification (ergodic theory)
- Operator-theoretic methods (Shapley operator, nonlinear Perron-Frobenius)
- Algebraic geometry of Nash correspondences (semi-algebraic sets, o-minimal structures)
- Viability theory / differential inclusions on payoff correspondences
- Category-theoretic / coalgebraic methods for infinite-horizon games
- Approximation by solved subclasses (quitting → absorbing → recursive → general)

Be concrete. Each strategy should be specific enough to serve as a proof breakdown target.
