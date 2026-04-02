# Deviation-Value Certificate Prover (Pass 59)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the PROVER role. Attack the LAST remaining gap to Neyman's conjecture: the deviation-value preservation certificate.

## The Problem

We have a public block controller that realizes a target occupation measure mu_C on a communicating class C (Section 5.1). The occupation measure determines the boundary flux beta = L(mu) automatically (graph-VP3). The continuation weights are handled by exit-tag augmentation.

BUT: a player who DEVIATES unilaterally from the block controller faces a one-player MDP against the fixed controller. The value of that MDP must be approximately the same as the value computed from the relaxed fixed-point package. This is NOT automatic from matching the occupation measure.

## Why it's hard

The occupation measure tells you what the compliant players DO. But a deviator faces different transitions — the deviator's MDP has:
- The same states (C's phase-states)
- The OTHER players' actions fixed by the controller
- The deviator's own actions FREE
- The deviator's value = sup over own actions of expected payoff

Matching mu_C pins down the joint behavior under compliance but NOT the deviator's one-player optimization landscape.

## What we need to prove

For the block controller u_C that realizes mu_C:
- The deviator's optimal value V_dev(u_C) satisfies |V_dev(u_C) - V_dev(relaxed)| < delta
- Where V_dev(relaxed) is the deviation value from the abstract fixed-point package
- This must hold for ALL players i and ALL deviations tau_i

## Possible approaches (from Pass 58 Searcher)

1. **Bellman certificate**: Show that the gain-bias pair (g_C, w_C) from the relaxed package also approximately solves the deviator's Bellman/Poisson equation under the realized controller
2. **LP dual bound**: Use the occupation-measure LP dual to bound the deviation value
3. **Continuity argument**: Show that as the controller's realized coordinates converge to the target, the deviator's value converges too (via continuity of the value function in the transition kernel)

## Key question

Is approach 3 (continuity) sufficient? If the block controller realizes mu_C within delta, and all the relevant coordinates (occupation, flux, gain, bias) are within delta of the target, does it follow that the deviation value is within f(delta) of the relaxed value, for some function f -> 0?

PROVE THIS if possible. If not, identify exactly what additional structure is needed.
