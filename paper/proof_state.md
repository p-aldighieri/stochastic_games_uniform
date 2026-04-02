# Proof State — Neyman's Conjecture Under Condition (a)

## The Open Problem

**Neyman's Conjecture (N-player):** Every finite N-player stochastic game satisfying condition (a) admits a uniform ε-equilibrium.

**Condition (a) [Neyman 2003]:** For every player i and every pure stationary strategy f_i: S → A_i, the Markov chain on S is irreducible regardless of the other players' strategies.

This is a UNILATERAL condition — no single player can break irreducibility. It does NOT require that ALL stationary profiles are irreducible (that's classical irreducibility, which is stronger).

## What Is Solved

**v28 (793 lines, PASS at Pass 120):** Under CLASSICAL IRREDUCIBILITY (every stationary mixed profile gives irreducible chain on S), uniform ε-equilibrium exists with O(1/T) regret.

Proof: Glicksberg fixed point on average-reward meta-game + supermartingale from Bellman optimality inequality. Prior art: Rogers (1969), Sobel (1971).

## What Remains Open — The Multichain Case

Under Neyman's actual condition (a), the game can have multiple strongly connected components. When players use mixed stationary strategies, the chain might NOT be irreducible — it can have multiple recurrent classes. The deviator's average reward then depends on WHICH recurrent class they reach.

### Why the tree approach failed (Passes 100-116)

The tree decomposition of the game's SCC structure was correct. Local Bellman certificates within each node were verified 10+ times. The failure was at the GLOBAL level:

1. **Terminal tree nodes create absorbing recurrent classes** in the expanded MDP
2. The expanded MDP is **multichain** — no single scalar g* bounds all deviations
3. The deviator can potentially choose WHICH recurrent class to enter
4. All 10+ bridge attempts failed because they tried to use a single benchmark

### The precise mathematical obstacle

In the multichain induced MDP:
- Different recurrent classes have different gains g_1, g_2, ..., g_k
- The deviator's average reward = Σ p_j(τ_i) g_j where p_j depends on the deviation
- The compliant's average reward = Σ p_j(σ_i) g_j where p_j depends on the compliant strategy
- The regret depends on how the deviator can SHIFT probability between classes

To bound regret, we need to show: the deviator cannot shift much probability toward higher-gain classes compared to the compliant.

## Verified Local Machinery (Available for Reuse)

These components were independently verified across 10+ EP reviews:

1. **Tree decomposition** of metastable SCCs
2. **Local Bellman certificates** (g_C, h_C) at each node — correct
3. **Stock Z** tracking transition jumps v_C(b) - h_D(entry) — correct
4. **Augmented potential Ψ = h + Z** with clean one-step drift — correct
5. **Kakutani fixed point** on tree packages — correct
6. **Realization theorem** for compliant payoff — correct

## Potential Attack Strategies for the Real Problem

### Strategy 1: LP Duality for Multichain MDPs
The Pass 118 reviewer noted: "a scalar dual bound might still upper-bound deviations without unichain." Explore LP formulations for multichain average-reward MDPs.

### Strategy 2: Recurrent-Class Selection Bound
Show that under condition (a), the deviator cannot significantly alter which recurrent classes are reached. The key: condition (a) prevents any single player from creating new absorbing subsets.

### Strategy 3: Blackwell Approachability / Discounted Limits
Approximate the average-reward game by discounted games (where equilibria are known to exist). Take limits as discount factor → 1. The challenge: controlling the limit.

### Strategy 4: Value-Based Tree Recycling
Modify the tree routing so terminal nodes restart from the root. Under condition (a), the game chain can return to any state, enabling restarts. This would make the expanded MDP irreducible.

### Strategy 5: Occupation Measure Approach
Work with occupation measures directly. The set of achievable occupation measures is a polytope. Condition (a) constrains which vertices are reachable. Bound regret via the polytope geometry.

## Key References to Investigate

- Neyman (2003): Original 2-player result
- Rogers (1969), Sobel (1971): Classical irreducible case
- Federgruen (1978): Average-reward MDPs
- Mertens-Neyman (1981): Value existence in stochastic games
- Vieille (2000): Two-player stochastic games
- Solan-Vieille (2002): Uniform equilibria
- Puterman (1994): MDP theory, multichain results
