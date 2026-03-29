# Proof Breakdown Request (breakdown role)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-27T14:30:00.000000+00:00

## Instructions

You are the breakdown role. Your task is to take the selected proof strategy and produce a **detailed proof breakdown** — a sequence of lemmas, propositions, and constructions that, if each is proved, yields the theorem.

## Theorem Target (unchanged)

For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist a strategy profile sigma and threshold T_0 such that for all T >= T_0, all initial states s, all players i, all unilateral deviations tau_i:

gamma_i^T(s, sigma) >= gamma_i^T(s, (tau_i, sigma_{-i})) - epsilon.

## Selected Strategy: Metastable Occupation-Flux Tree (Strategy 1 from Searcher)

### The Compact Object
A finite rooted DAG of communicating classes; for each node C, store:
- **Phase-labeled occupation measure** mu_C on state-action pairs inside C
- **Projective exit-rate vector** alpha_C over outgoing macro-exits
- **Exit law** q_C
- **Continuation values** on successor nodes
- **Normalized bias vector** b_C

The phase label matters because periodic transition structure can be essential, so invariant measures alone are too coarse.

### The Proof Sketch (from Searcher)
1. Define consistency equations for these coordinates
2. Prove every sequence of long-block profiles has a convergent asymptotic-tree subsequence (sequential compactness)
3. Prove payoffs and unilateral deviation values are continuous on the tree by renewal equations
4. Apply Kakutani on the relaxed tree space
5. Realize fixed points by growing blocks (implementability)

### Known Obstacles
- Implementability must stay closed when classes split, merge, or differ only at smaller rare-transition scales
- Transition-tilting deviations must be readable continuously from exit coordinates
- The searcher recommends using Puiseux-branch analysis (Strategy 3) as a lemma engine for the algebraic structure near lambda=0

### Reusable Infrastructure (from 23 prior passes)
- **Gain-bias decomposition**: Lexicographic gain-bias structure from the conditional theorem (Route B, Pass 16-19)
- **Deviation taxonomy**: 4 types — gain-burning (auto), off-support (easy), within-support (D1), transition-tilting (D2)
- **Block structure**: Growing blocks with summable leakage from the block-selector work
- **H3 counterexample**: Shows stationary limits fail at bias level — the flux tree must carry more than just x*

### What Works in Solved Subclasses
| Subclass | Compact Object | Key Technique |
|----------|---------------|---------------|
| Quitting games | Absorption paths | Continuous payoff on path space |
| Positive recursive absorbing | Continuation-value orbits | Self-map on value domain + finite orbits |
| 2-player zero-sum | Algebraic value structure | Puiseux expansion / operator theory |

## Your Task

Produce a **complete proof breakdown** for Strategy 1 consisting of:

1. **Definitions**: Precisely define the metastable occupation-flux tree space A for a general finite stochastic game. Include all coordinates, the topology, and the consistency equations.

2. **Lemma sequence**: A numbered sequence of lemmas/propositions that build toward the theorem. For each lemma:
   - State it precisely
   - Identify the key technique or known result it relies on
   - Flag whether it is KNOWN (follows from literature), STRAIGHTFORWARD (routine given the setup), or HARD (requires new ideas)
   - Estimate which of the 4 deviation types it handles

3. **Critical path**: Identify which lemma is the theorem-sized bottleneck — the one that, if proved, essentially closes the argument.

4. **Puiseux lemma engine**: Where in the sequence does Strategy 3 (Puiseux-branch analysis of discounted Nash correspondences) enter as a supporting lemma? State the specific algebraic lemma needed.

5. **Risk assessment**: For each HARD lemma, describe what could go wrong and what fallback exists.

Be concrete and precise. Each lemma should be stated formally enough that a prover role can attempt it in a single pass.
