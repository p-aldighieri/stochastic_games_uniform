# Paper v7 Fix — Pass 77

Provider: external_agent
Model hint: chatgpt-5.4-pro
Generated: 2026-03-31

## Instructions

You are the REWRITER. A 32-minute Pro review found ONE remaining blocker in v6 (3 of 4 previous blockers are fixed). Fix this blocker and output the COMPLETE corrected v7 LaTeX source.

## The blocker: bookkeeping kernel vs first-exit block mismatch

The paper mixes TWO different objects:
1. The **bookkeeping kernel** (with restart after exit): its invariant measure gives the occupation rates mu_bar*
2. The **first-exit block**: the actual realized segment that TERMINATES at first cemetery visit

The counterexample shows the problem:
- 1 internal state xi, 1 boundary b, certain exit lambda(b|xi)=1, restart rho(xi|b)=1
- Stage payoff u=0, continuation v(b)=1
- Bellman gives g*=1 (because the bookkeeping chain cycles: xi → exit → restart → xi → ...)
- But each scheduled block exits IMMEDIATELY, so realized block payoff = v(b)/L = 1/L → 0

The paper claims g* equals the normalized block payoff (1/L)*[stage payoffs + continuation], but this is wrong because L is the SCHEDULED block length, not the ACTUAL first-exit time.

## The fix: renewal-reward formulation

The correct relationship uses the RENEWAL REWARD THEOREM:

g* = E[total reward in one renewal cycle] / E[renewal cycle length]

where one renewal cycle = enter xi_0, play until first exit, collect continuation value.

In the block implementation:
- The block runs for a RANDOM time tau (first exit time), tau <= L
- Total block reward = sum_{t=0}^{tau-1} u(xi_t, a_t) + v(b) at exit
- The renewal reward theorem gives: g* = E[total block reward] / E[tau]

The block's contribution to the T-game payoff is:
- NOT (1/L) * total block reward
- BUT rather the total block reward itself (counted over tau steps out of T total)

In the regret analysis, the correct accounting is:
- T-game payoff = sum over blocks of (total block reward)
- Total time = T
- Average payoff = (1/T) * sum of block rewards
- Each block contributes approximately E[tau_block]/T * g* to this average

The key identity that makes this work:
sum over blocks of tau_block = T (up to the last incomplete block)
So (1/T) * sum of block rewards ≈ g* (by renewal reward applied to each node)

## What needs to change in the LaTeX

1. **Theorem 6.1 (Local Controller Lemma)**: Replace the claim that (1/L)*block_payoff ≈ g* with the correct renewal-reward formulation. The claim should be: E[total augmented block reward] / E[first-exit time] ≈ g* to within O(delta).

2. **The regret bound (Section 7)**: Account for the actual first-exit times, not scheduled block lengths. The key is that the SUM of first-exit times across all blocks at node C approximately equals the total time spent at C, so the renewal reward applies.

3. **Fix Lemma 7.5** (minor): The displayed proof of kappa(P) uses n-step transitions incorrectly. Fix to: for each (x,y), there exists n <= |X|-1 such that P^n(y|x) >= kappa(P). The conclusion (hitting time bound) still follows.

## Additional context from the reviewer

Three fixes that PASS and should be kept:
- Bias normalization h(xi_0)=0 ✓
- Block termination at first cemetery ✓
- Condition (a) on augmented kernel ✓

## Your task

Read the attached v6 tex. Fix the bookkeeping/first-exit mismatch using renewal-reward. Fix Lemma 7.5. Output the COMPLETE v7 LaTeX source.
