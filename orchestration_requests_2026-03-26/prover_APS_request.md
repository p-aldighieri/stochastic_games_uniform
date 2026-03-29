# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T06:00:00.000000+00:00

## Instructions

You are the prover role. This is a FUNDAMENTALLY NEW proof architecture for Neyman's open problem (uniform equilibrium in finite stochastic games). The previous Route B approach failed because it imported continuation sets W(h) and tried to show they are self-generating under equilibrium incentives — but achievability does not imply equilibrium.

The new approach: **endogenous self-generation via APS (Abreu-Pearce-Stacchetti) methods**, adapted from repeated games to stochastic games with block decomposition.

Instead of importing W, DEFINE the continuation correspondence as the largest bounded self-generating set, and prove it is nonempty. This is how equilibrium payoff sets are characterized in the repeated game folk theorem literature.

## The Theorem Target (unchanged)

For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist a strategy profile sigma and threshold T_0 such that for all T >= T_0, all initial states s, all players i, all unilateral deviations tau_i:
gamma_i^T(s, sigma) >= gamma_i^T(s, (tau_i, sigma_{-i})) - epsilon.

## The New Proof Architecture

### Step 1: Define block-self-generation

Fix a block length L. A state-indexed correspondence V: S -> compact subsets of [0,1]^N is called **L-block-self-generating** if for every state s and every v in V(s), there exist:
- An L-stage block policy pi (product actions at each stage, public-history contingent)
- Block-end continuation selectors beta(z) in V(s(z)) for every L-stage terminal history z starting from s

such that:
(a) **Promise-tracking**: The block-averaged expected payoff under pi, plus the expected continuation, equals v (up to small error).
(b) **Block IC**: For every player i and every unilateral deviation tau_i within the block, the deviator's block-averaged payoff plus expected continuation does not exceed v_i (up to small error).

Key difference from imported W: here V is defined BY the self-generation property, not imported from an external source.

### Step 2: Prove the largest L-block-self-generating correspondence exists and is nonempty

**Approach A (Kakutani/fixed-point):** Define a correspondence Phi_L that maps a state-indexed family V to the set of all payoff vectors v that can be block-decomposed using continuations in V. Show Phi_L is upper-hemicontinuous with compact convex values on the lattice of compact correspondences. Then the largest fixed point of Phi_L exists by Tarski's theorem or direct construction.

**Approach B (Direct construction):** Start with V^0(s) = [0,1]^N (all bounded payoffs). Define V^{k+1}(s) = Phi_L(V^k)(s). Show V^k is a decreasing sequence of compact sets, so V^* = intersection is compact and is an L-block-self-generating correspondence. The key is to show V^*(s) is nonempty for every s.

**Why nonemptiness should hold:** In any finite stochastic game, for any state s, there exist Nash equilibria of the L-stage truncated game. These equilibria give payoff vectors that can be decomposed using continuations in [0,1]^N. As we iterate the Phi_L operator, we're refining the set. The question is whether the refinement stabilizes at a nonempty set.

For DISCOUNTED stochastic games, this is known to work (the discounted game has a value, and the equilibrium payoff correspondence is nonempty). For the UNDISCOUNTED/uniform case, the key insight is that the block structure with L -> infinity approximates the discounted case as the effective discount factor approaches 1.

### Step 3: From self-generating correspondence to uniform epsilon-equilibrium

If V^*(s) is nonempty for every s:
1. Choose v^s in V^*(s) for each state s
2. Recursively construct a block policy at each block boundary using the self-generation property
3. The block IC guarantees deviation control within each block
4. Telescope across blocks (this is the verified L7*-block step)
5. Take L large enough that block leakage is summable
6. Assembly into one whole-game profile (verified L9 step)

This is essentially the same post-L4 tail, but now L4 is replaced by the self-generation fixed-point theorem.

### Step 4: Handle the block-length growth for summability

For summable leakage, use growing block lengths L_1 < L_2 < ... with:
- V_{L_t}^*(s) may depend on t
- But since the game is finite, the block-self-generation property with L_t large enough should give leakage O(1/L_t)
- Choose L_t geometrically to make sum_t (1/L_t) < epsilon/8

## Key Technical Questions to Resolve

1. **Is V^*(s) nonempty?** This is the central question. The argument must show that the iterated refinement doesn't collapse to the empty set. Use the fact that Nash equilibria of finite truncated games exist (Nash's theorem) and provide candidate vectors at each iteration.

2. **Does the block IC hold with small leakage?** In the self-generating set, the IC is part of the definition. The question is whether the self-generating set contains vectors that are close to useful payoff targets (like the mutual cooperation payoff in PD).

3. **Does the state-dependence cause problems?** In repeated games (single state), APS works cleanly. In stochastic games, the continuation sets V(s') depend on the successor state. Show that finiteness of the state space keeps the correspondence compact and the fixed-point argument valid.

4. **Relation to discounted results:** For lambda-discounted stochastic games, the equilibrium payoff correspondence E_lambda(s) is known to be nonempty. Can the undiscounted block construction be related to E_lambda as lambda -> 0?

## What a Complete Answer Looks Like

A rigorous proof that:
1. The largest L-block-self-generating correspondence V_L^*(s) exists and is nonempty for every state s
2. Elements of V_L^*(s) can be used to construct uniform epsilon-equilibria via the block recursion
3. The construction works for every finite stochastic game

OR a precise identification of where this approach also fails, with the exact obstruction.

This is the most natural path to the theorem. The APS approach is the standard tool for equilibrium payoff characterization, and adapting it to stochastic games with block decomposition directly addresses the self-generation gap that killed the previous approaches.
