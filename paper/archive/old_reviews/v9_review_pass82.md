# v9 Review — Pass 82

**Thinking**: 26 min 35s Extended Pro
**Verdict**: CONDITIONAL

## What PASSES
- Depth-sensitive gain boxes [0,D]: CONFIRMED
- Prelude blocks peeled off: CONFIRMED
- Renewal-reward normalization: CLEAN
- All structural proof elements: SOUND

## Remaining issue: terminal-label leaf

Terminal labels have continuation profile w(b) and payoff vector, but:
- The realization theorem and main proof treat post-terminal-label play as an O(1) fragment
- They only charge the one-shot cemetery bonus
- But terminal labels can lead to continued play under a different profile
- The accounting of stages consumed by terminal-continuation play is incomplete

## Fix needed
Either: (a) define terminal labels as absorbing (game ends, payoff = w(b)), or (b) explicitly account for stages consumed by terminal-continuation play in the regret bound. Option (a) is cleaner — terminal labels ARE the end of the metastable tree, and the continuation profile w(b) IS the final payoff.
