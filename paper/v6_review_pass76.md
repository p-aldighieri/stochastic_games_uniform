# v6 Review — Pass 76

**Thinking**: 32 min 43s Extended Pro
**Verdict**: FAIL (but narrowing — 3 of 4 blockers fixed)

## What PASSES
1. Bias normalization h(xi_0)=0: PASS — domain genuinely convex
2. Block termination at first cemetery: PASS — routing precise
3. Condition (a) on augmented kernel: Mostly repaired (minor Lemma 7.5 bug)

## Remaining blocker: bookkeeping vs first-exit mismatch

The paper mixes a RESTARTED bookkeeping object with a TERMINATED first-exit block.

Counterexample: 1 internal state, 1 boundary, certain exit (lambda=1), restart, continuation v(b)=1, stage payoff u=0.
- Bellman gives g*=1
- But every block exits immediately, so realized block payoff = 1/L → 0
- Therefore Theorem 6.1 is FALSE under present definitions

The fix: the block payoff normalization is wrong. Should use renewal-reward:
E[sum of payoffs + continuation] / E[first exit time] = g*

The bookkeeping occupation measure (from invariant law of restart kernel) gives the correct RATES, but the block payoff must account for the random stopping time, not normalize by scheduled block length L.

## Fix needed
Rewrite Theorem 6.1 to use renewal-reward normalization. The block's contribution to the T-game is not (1/L)*sum, but rather weighted by the actual first-exit time relative to the total game length.
