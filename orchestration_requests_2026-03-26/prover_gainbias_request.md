# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T07:05:00.000000+00:00

## Instructions

You are the prover role. The previous APS attempt (Prover 14) failed because bounded payoff correspondences are the WRONG continuation object for undiscounted average-payoff stochastic games. The recursion is additive, not bounded — even the trivial all-ones game has empty bounded self-generating sets.

Prover 14 identified the exact repair: **gain-bias pairs**. This is the standard object in average-reward MDP/game theory:
- g(s) in [0,1]^N is the long-run average gain (bounded)
- b(s) in R^N is the bias/potential (unbounded but normalizable)
- Block equation: L·g_i(s) + b_i(s) >= E[sum_{t=1}^L u_i + b_i(s_{L+1})] - eta, for obedient play
- Block IC: L·g_i(s) + b_i(s) >= sup_{tau_i} E[sum u_i + b_i(s_{L+1})] - eta

Your task: prove uniform epsilon-equilibrium existence using gain-bias self-generation.

## The Theorem Target (unchanged)

For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist sigma and T_0 such that for all T >= T_0, all s, all i, all tau_i:
gamma_i^T(s, sigma) >= gamma_i^T(s, (tau_i, sigma_{-i})) - epsilon.

## The Gain-Bias Architecture

### Step 1: Define the gain-bias block decomposition

For a finite stochastic game G, a **gain-bias pair** is a pair (g, b) where:
- g: S -> [0,1]^N (the gain vector, one per state, bounded by payoff range)
- b: S -> R^N (the bias vector, normalized so that b(s_0) = 0 for a reference state s_0)

After normalization, b is bounded: since the game is finite with bounded payoffs, |b_i(s)| <= C for some game-dependent constant C (related to mixing time and diameter of the state space).

Fix a block length L. A gain-bias pair (g, b) is **L-block-feasible** at state s if there exists:
- A block policy pi (L stages, product actions, public-history contingent)
such that:
(a) **Gain tracking**: E_pi[sum_{t=1}^L u_i(s_t, a_t) + b_i(s_{L+1})] >= L·g_i(s) + b_i(s) - eta, for all i
(b) **Block IC**: For all i, all tau_i: E_{(tau_i, pi_{-i})}[sum_{t=1}^L u_i + b_i(s_{L+1})] <= L·g_i(s) + b_i(s) + eta

### Step 2: Construct feasible gain-bias pairs via discounted approximation

**Key idea**: For lambda-discounted stochastic games, stationary equilibria exist (Fink 1964, Takahashi 1964). These give discounted equilibrium payoffs v_lambda(s). As lambda -> 0:
- The gain g(s) = lim_{lambda->0} lambda·v_lambda(s) exists (Bewley-Kohlberg 1976)
- The bias b(s) = lim_{lambda->0} (v_lambda(s) - g(s)/lambda) exists after normalization (up to subsequences, by compactness)

The Bewley-Kohlberg algebraic theory shows these limits exist for all finite stochastic games and satisfy a system of inequalities related to the average-reward optimality equations.

**The question**: Do these limiting gain-bias pairs satisfy the block-feasibility conditions? Specifically:
1. Does the limiting gain-bias pair (g, b) from discounted equilibria satisfy block feasibility for large L?
2. Is the leakage eta controllable as O(1/L)?

### Step 3: From gain-bias pairs to uniform epsilon-equilibrium

If (g, b) is L-block-feasible at every state s:
1. At each block boundary, play the block policy pi_s that certifies feasibility
2. The gain tracking ensures: block-averaged payoff ≈ g_i(s) + (b_i(s) - E[b_i(s_{L+1})])/L
3. The bias terms telescope across blocks (this is the EXISTING verified L7*-block step!)
4. After K completed blocks: total payoff ≈ K·L·g_i + b_i(s_1) - E[b_i(s_{KL+1})]
5. Dividing by KL: average payoff ≈ g_i + O(1/(KL)) (bias terms are bounded)
6. Block IC ensures no player can gain more than eta per block
7. Take L large enough that eta = O(1/L), then summable across blocks

### Step 4: The critical new question

Does the discounted limit (g, b) from Step 2 actually satisfy the block-feasibility conditions from Step 1?

**Why it might work**:
- The discounted equilibrium sigma_lambda is approximately optimal for horizon ~1/lambda
- For a block of length L << 1/lambda, the discounted strategy plays "as if" the future is discounted, which approximates the block game equilibrium
- The bias terms capture the transient effects correctly
- As lambda -> 0 with L fixed but growing with the block index, the approximation tightens

**What needs to be proved**:
1. The gain-bias limit (g, b) exists (Bewley-Kohlberg — known)
2. The discounted equilibrium strategy, truncated to L stages, satisfies block feasibility with leakage O(1/L) + O(lambda·L) (this is the new claim)
3. Choose lambda and L jointly so that both error terms are small and the total leakage is summable

## Key References to Use

- **Bewley-Kohlberg (1976)**: Algebraic theory of the discounted limit in stochastic games. Gain and bias exist for all finite games.
- **Mertens-Neyman (1981)**: Two-player zero-sum stochastic games have uniform values (uses gain-bias).
- **Fink (1964), Takahashi (1964)**: Discounted stochastic games have stationary equilibria.
- **Solan-Vieille (various)**: Partial results on multiplayer uniform equilibrium in special classes.
- **Fudenberg-Yamamoto**: Return generation for stochastic game folk theorems.

## What a Complete Answer Looks Like

Either:
1. A rigorous proof that the discounted-limit gain-bias pair satisfies block feasibility, giving uniform epsilon-equilibrium, OR
2. A precise identification of where the discounted-to-undiscounted transfer breaks, with the exact gap.

The gain-bias framework is the RIGHT object (it handles the additive structure correctly). The question is whether discounted equilibria provide feasible gain-bias pairs for the undiscounted block construction.
