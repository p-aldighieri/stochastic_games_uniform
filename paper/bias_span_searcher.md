# Bias-Span Boundedness Searcher (Pass 61)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## The Last Obstacle

The enriched tree needs a uniform bias-span bound for the deviator's MDP. Specifically:

For each node C, each player i, the deviator faces an MDP with kernel Q_i and reward r_i (both determined by compliant data). The Bellman equation T_i* w = g + w has solutions, but the bias w_i^dev may have unbounded span across the relaxed tree space.

## Why this matters

Without a bound on ||w||_span, the enriched tree space is noncompact, Kakutani fails, and the proof breaks.

## What is known about bias-span bounds in finite MDPs

- For IRREDUCIBLE chains: bias span is bounded by |S|^2 * max|r| / min(P) (classical)
- For COMMUNICATING MDPs: span(h*) ≤ D * max|r| where D is the diameter
- For MULTICHAIN MDPs: bias is defined only relative to each recurrent class; transient states can have unbounded relative bias

## The key question

In our metastable tree, the deviator's MDP is defined on a FINITE state-action space (the augmented phase-states of node C). So:

1. Is the deviator's MDP always communicating? (If yes, bias span is bounded by game constants.)
2. If not communicating, can the deviator create multichain structure by choosing actions?
3. Does the metastability assumption (C is a communicating class under compliance) help?
4. Can we use the occupation-measure structure to bound bias span indirectly?

## Find strategies for proving a uniform bias-span bound, or explain why it cannot hold.
