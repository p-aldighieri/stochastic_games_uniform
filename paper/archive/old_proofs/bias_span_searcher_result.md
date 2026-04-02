# Bias-Span Searcher — Pass 61

**Pass**: 61
**Role**: Searcher
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 28m 56s

## VERDICT: Uniform bias-span bound does NOT hold in general

The deviator's MDP is NOT always communicating — the deviator can create multichain structure by choosing actions that break connectivity. When this happens, the bias span depends on the inverse of the minimum transition probability on connector edges, which can be arbitrarily small in the relaxed tree space.

### Key example
Two-state MDP with probability p of transitioning between states. The optimal bias span is 1/p, which is unbounded as p -> 0. Same recurrent occupation, wildly different transient bonus.

### Three rescue routes
1. **Uniform connector bound**: Prove every metastable node has a strongly connected phase graph with edge probability ≥ eta > 0. Then bias span ≤ f(|C|, eta).
2. **Interior support floor**: Restrict A_eta so mixing weights never approach zero on connector actions. Changes the compactification.
3. **Richer compact object**: Track transient navigation data (entry laws, exit intensities, transient navigation bound), not just steady-state occupation.

### Implication
The current Route D' framework stores only recurrent occupation data. Bias remembers the transient trip BEFORE the recurrent regime is reached. This is the missing piece.

## Final State of Neyman's Conjecture (after 61 passes)

**PROVED unconditionally:**
- Compact metastable tree space (Section 3)
- Flux coordinate repair (Section 4)
- Ergodic occupation realization (Section 5.1)
- Boundary-flux witness (Section 5.2)
- Graph-VP3 automatic (flux = L(occupation))
- Deviator kernels Q_i, r_i automatic (affine in compliant data)

**CONDITIONAL on:**
- Bounded bias span for deviator MDPs on metastable nodes
- Equivalently: a "robust metastability" lemma ensuring uniform transient navigation bounds

This is the precise mathematical frontier of Neyman's open problem.
