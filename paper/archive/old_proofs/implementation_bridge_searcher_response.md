# Implementation Bridge Searcher — Pass 58

**Pass**: 58
**Role**: Searcher
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 28m 30s

## Key Findings

**Requirement 3 (continuation weights): ~90% solved**
- Exit-tag augmentation (difficulty 3/10) makes it nearly automatic
- Section 5.1 with successor-labeled cemetery states already controls the right coordinates
- Remaining: normalization lemma or terminal-lottery gadget

**Requirement 4 (deviation-value preservation): THE real obstacle**
- Matching occupation does NOT pin down the deviator's MDP value
- Need a Bellman/LP certificate carried by gain-bias coordinates
- This is "the bridge plank most likely to creak"

## Strategies for Requirement 4
1. **Bellman certificate on deviator's MDP** — use gain-bias coordinates from Route D'
2. **LP certificate** — dual bound on deviation value from the occupation polytope
3. **Long stationary subblocks** — transport certificate through Caratheodory realization
4. **Prefix-robust mosaic** — make blocks deviation-safe even if terminated early

## Recommended Attack Order
1. Settle Req 3 with exit-tag augmentation (easy)
2. Attack Req 4 with Bellman/LP certificate on deviator's MDP
3. Use stationary subblocks to transport certificate through realization
4. Superexponential outer schedule only after local certificate exists

## Bottom Line
The last remaining obstacle: "can we make the abstract fixed-point package carry a unilateral-deviation certificate that survives public finite-memory implementation?"

This is the core mathematical question. It's what makes Neyman's conjecture hard for 40 years.
