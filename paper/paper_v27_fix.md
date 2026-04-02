# Paper v27 Fix — Pass 117

## Pass 116 FAIL: The unichain claim is FALSE

The reviewer proved that the paper's NODEWISE condition (a) does NOT imply the global induced MDP is unichain. Counterexample: terminal tree nodes create absorbing recurrent classes. The tree routing itself breaks irreducibility — even if each node's internal chain is locally irreducible, the expanded state space (game state × tree node × controller memory) has multiple recurrent classes.

This is the ROOT CAUSE of all 10+ failed local-to-global bridge attempts (passes 100-116). The tree structure inherently creates a multichain MDP. No amount of stitching, telescoping, or gain-comparison can fix this.

## THE FIX: Use Neyman's GAME-LEVEL condition (a) and DROP THE TREE

### Key realization

The paper uses a NODEWISE reformulation of condition (a) (irreducibility within each tree node). This is WEAKER than Neyman's original GAME-LEVEL condition:

**Condition (a) [Neyman 2003, game-level]**: For every player i, for every pure stationary strategy f_i: S → A_i of player i, and for every mixed stationary profile σ_{-i} of the other players, the Markov chain on S under (f_i, σ_{-i}) is irreducible.

Under the game-level condition (a):
- The game has NO proper absorbing subsets for any unilateral pure deviation
- The SCC decomposition under any deviation is trivial (the whole S is one SCC)
- **There is no need for a tree decomposition** — the entire game is one "node"
- Player i's induced MDP on S is UNICHAIN by definition

### The correct proof (5 steps)

**Step 1: The average-reward meta-game**

Define a normal-form game G_avg where each player i chooses a mixed stationary strategy σ_i ∈ Δ(A_i(s))_{s ∈ S} and receives payoff g_i(σ) = the ergodic average reward under the Markov chain induced by σ = (σ_1, ..., σ_N) on S.

Under condition (a), the chain is irreducible for every profile σ (since every pure profile gives irreducibility, and the mixed chain's support includes all transitions from any pure component). Therefore the ergodic average g_i(σ) is well-defined for every σ.

**Step 2: Existence of Nash equilibrium (Glicksberg)**

The strategy space Δ(A_i(s))_{s ∈ S} is compact and convex for each player. The payoff g_i(σ) is continuous in σ (because the stationary distribution π(σ) is continuous in the transition matrix, which is linear in σ, and the chain stays irreducible by condition (a) — no bifurcation of stationary distributions).

By Glicksberg's theorem (= Fan's fixed-point theorem for N-player games with compact strategy spaces and continuous payoffs), there exists a Nash equilibrium σ* of G_avg.

At σ*: for every player i, σ_i* maximizes g_i(σ_i, σ_{-i}*) over mixed stationary σ_i. So g_i(σ*) = g_i*(σ_{-i}*) = the optimal gain of player i's MDP under σ_{-i}*.

**Step 3: Unichain MDP theory (standard)**

Fix player i and σ_{-i} = σ_{-i}*. Player i faces a finite-state unichain MDP on S (unichain by condition (a)). Standard theory gives:
- Unique optimal gain g_i* = g_i(σ*)
- Optimal bias h_i*: S → R satisfying g_i* + h_i*(s) = max_{a_i} [r_i(s, a_i, σ_{-i}*) + Σ P(s'|s, a_i, σ_{-i}*) h_i*(s')]
- sp(h_i*) = max h_i* - min h_i* < ∞ (bounded by game parameters)

**Step 4: Deviator upper bound (supermartingale)**

For ANY deviation τ_i (including history-dependent behavioral strategies):

Define N_t = h_i*(s_t). The Bellman inequality gives:
E[N_{t+1} | F_t] ≤ g_i* + N_t - r_t (where r_t = u_i(s_t, a_t))

Summing: E[N_T] - N_0 ≤ g_i* T - Σ E[r_t]
Therefore: (1/T) Σ E[r_t] ≤ g_i* + [N_0 - E[N_T]]/T ≤ g_i* + sp(h_i*)/T

This holds for ALL T ≥ 1 and ALL deviations τ_i.

**Step 5: Compliant lower bound (ergodic theorem)**

Under σ* (the Nash equilibrium), player i plays σ_i* which achieves the optimal gain g_i* in the MDP. The chain under σ* is irreducible (condition (a)), so by the ergodic theorem:

(1/T) Σ_{t=1}^T u_i(s_t; σ*) → g_i(σ*) = g_i* almost surely

Therefore for T ≥ T_1: (1/T) E[Σ u_i] ≥ g_i* - O(1/T)

**Conclusion: Uniform ε-equilibrium**

Regret = deviator payoff - compliant payoff ≤ [g_i* + sp(h_i*)/T] - [g_i* - O(1/T)] = O(sp(h_i*)/T)

For T ≥ T_0 = max_i 2 sp(h_i*)/ε, regret ≤ ε for all players i and all deviations.

The strategy σ* does NOT depend on T. Therefore σ* is a UNIFORM ε-equilibrium for T ≥ T_0. ∎

### What changes in the paper

**DELETE** (no longer needed):
- Tree decomposition (T_η, nodes, routing, depth, schedule)
- Local Bellman certificates (g_C, h_C, v_C per node)
- Stock Z and augmented potential Ψ
- Local controllers and visit-level analysis
- Realization theorem
- All bridging attempts (gain comparison, tree telescoping, etc.)
- Kakutani on tree packages (replaced by Glicksberg on stationary strategies)

**KEEP** (in simpler form):
- Introduction and motivation
- Stochastic game definition
- Condition (a) — but state at GAME LEVEL, not nodewise
- MDP average-reward theory (gain, bias, supermartingale) — a short appendix
- The 5-step proof above

**ADD**:
- Glicksberg's theorem and its application to the average-reward meta-game
- Continuity proof for g_i(σ) under condition (a)
- The LP formulation showing η-best-response sets are convex (for those wanting a Kakutani alternative)

### Paper structure

The v27 paper should be MUCH shorter — approximately 20-30 pages instead of 60+.

1. Introduction (3 pages): state the theorem, history, significance
2. Stochastic games and condition (a) (3 pages): definitions, examples
3. Average-reward MDP theory (5 pages): unichain, gain, bias, supermartingale bound
4. The average-reward meta-game (5 pages): define G_avg, continuity of g_i, Glicksberg equilibrium
5. Proof of the main theorem (5 pages): the 5-step argument
6. Discussion (2 pages)

### Why this is correct

Under condition (a) at the game level:
1. Every player's induced MDP is unichain ← DEFINITION of condition (a) for pure deviations, plus the fact that mixed deviations don't break irreducibility
2. g_i is continuous ← standard perturbation theory for irreducible Markov chains
3. Glicksberg gives Nash equilibrium ← compact strategy spaces + continuous payoffs
4. Supermartingale bounds deviator ← standard Bellman inequality argument, works for all policies
5. Ergodic theorem gives compliant lower bound ← irreducible finite Markov chain

Each step is well-established in MDP/game theory. The contribution is recognizing that condition (a) at the game level makes the tree decomposition unnecessary and reduces the proof to standard techniques.

### Important note on condition (a)

The game-level condition (a) is equivalent to the nodewise condition when the game has only ONE strongly connected component (which IS the case under the game-level condition). So there is no loss of generality for Neyman's conjecture — the conjecture IS about the game-level condition.

Output the COMPLETE v27 LaTeX source as a downloadable .tex file.
