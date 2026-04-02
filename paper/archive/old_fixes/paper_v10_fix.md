# Paper v10 Fix — Pass 83

## Instructions

A 27-minute Extended Pro review gave v9 CONDITIONAL. ONE issue remains: terminal-label leaf accounting.

## The issue

Terminal labels have continuation w(b), but realization theorem treats post-terminal play as O(1) fragment and only charges one-shot cemetery bonus. The accounting of stages consumed by terminal-continuation play is incomplete.

## The fix

Terminal labels ARE the boundary of the metastable tree. After a block exits to a terminal label b:
1. The continuation value w(b) is paid as a one-shot terminal payoff
2. No further blocks are scheduled — the remaining T-game stages at that terminal are played under the fixed terminal profile
3. The terminal profile is a FIXED strategy (not optimized), so its average payoff converges to some fixed value
4. The total number of stages spent at terminal labels is bounded by T, so the contribution is absorbed into the regret bound

Specifically, add: "After an exit to a terminal label b, the strategy prescribes the fixed terminal continuation profile for all remaining stages. Because terminal labels are leaves of the metastable tree with no further tree structure, the expected number of stages spent at terminal labels before the next node entry is at most the tree depth D. The terminal contribution to the T-game regret is therefore at most D*||u||_inf/T per terminal visit, which is absorbed into K_eta/T."

Apply this fix. Output the COMPLETE v10 LaTeX source.
