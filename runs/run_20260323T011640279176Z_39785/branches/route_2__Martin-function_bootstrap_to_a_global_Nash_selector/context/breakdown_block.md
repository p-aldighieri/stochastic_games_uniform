# Breakdown Output (Block Selector Amendment)

Generated: 2026-03-26T02:55:00.000000+00:00

[BREAKDOWN_AMEND] Route B amended backbone with block selectors

Status ledger:
- Imported / unchanged: L1, L2
- Proved from imported inputs: L3*-block
- Critical open lemma: L4*-block
- Conditional on L4*-block: L5*-block through L10
- Overall theorem status: still bootstrap/open

Dependency spine:
L1 -> L2 -> L3*-block -> L4*-block -> L5*-block -> L6*-block -> L7*-block -> L8*-block -> L9 -> L10

## Key change from previous breakdown

The falsified one-step Strong L4* is replaced by a block-selector lemma. The post-selector tail is moved to block boundaries. The theorem-side quantifiers stay exactly unchanged.

## L4*-block (Critical Open Lemma)

For every epsilon > 0, there exist a global block schedule (L_t) and nonneg errors (r_t) with sum r_t <= epsilon/8, such that at every boundary history h and every b in W*(h), the block-feasibility set F_t(h,b) is nonempty with leakage at most r_t.

Target schedule: L_t = ceil(L_1 * (1+rho)^{t-1}), r_t = 1/(4*L_t), with rho small.

The block version works because it asks for only one legal re-entry point at the end of a finite block, after incentive work has been done internally via grim-trigger-within-block strategies.
