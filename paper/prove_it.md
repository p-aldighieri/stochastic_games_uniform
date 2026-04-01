# PROVE IT (Pass 62)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the PROVER. Stop mapping obstacles. PROVE THE THEOREM.

## The situation

We have everything except a uniform bias-span bound. The searcher says it fails "in general" because the deviator can break connectivity. Fine. Then RESTRICT THE CLASS and prove an unconditional theorem for that class.

## Your job

Write a COMPLETE PROOF of the following theorem (or the strongest version you can prove):

**Theorem**: Every finite stochastic game in which [FILL IN THE WEAKEST SUFFICIENT CONDITION] has a uniform epsilon-equilibrium.

The proof should use:
1. The metastable tree compactification (Section 3)
2. The flux coordinate repair (Section 4)
3. The ergodic occupation realization (Section 5.1)
4. Graph-VP3 (automatic)
5. The Bellman deviation certificate with the bias-span bound

## Candidate restrictions (try the WEAKEST one that works)

(a) **All nodes have a communicating deviator MDP** — i.e., no player can unilaterally break connectivity of the chain on any node. This is weaker than irreducibility of the game itself.

(b) **Bounded exit ratio** — the ratio max(alpha)/min(alpha) over exit rates is uniformly bounded. This prevents the degenerate rare-exit case.

(c) **All games with at most K players and M states** — for fixed K, M, prove it unconditionally. The bias span is bounded by a function of K, M, and the game parameters. Since the game is FINITE, isn't this automatic?

(d) **Absorbing games** — games where at least one state is absorbing.

(e) **No restriction at all** — maybe the bias-span problem is actually solvable if we use the RIGHT normalization. The searcher said the bias span is 1/p where p is the connector probability. But in the RELAXED tree space, p comes from the compliant occupation measure. If we project out the degenerate p->0 face (which is already handled by the flux repair), maybe the bias span IS bounded on the relevant part of A_eta.

## IMPORTANT

Option (e) is the most important to investigate. The relaxed tree space A_eta already has eta-approximate consistency. Does this constrain the connector probabilities away from zero? If the compliant kernel M_C has a mixing time bounded by a function of eta, then the deviator's bias span may be bounded by f(|C|, eta) — which is EXACTLY what we need, since eta is fixed throughout the Kakutani argument.

PROVE THIS. Write the actual proof. If it works, we have Neyman's conjecture unconditionally.

Do not just analyze. PROVE.
