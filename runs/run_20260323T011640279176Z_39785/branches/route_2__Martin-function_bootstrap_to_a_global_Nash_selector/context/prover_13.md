# Prover Output (L4-block with full W attempt)

Generated: 2026-03-26T04:55:00.000000+00:00

Verdict: Cannot certify a proof. Full W removes the W*-thinness pathology but does NOT make W self-generating under equilibrium incentives.

## Two precise breaks

### Break 1: "tail close to W(z)" does not follow from b in W(h)
Even though the average of continuation tails is close to b, individual tails at specific terminal histories z can be far from W(z). The definition of W only controls averages, not pointwise continuation values. Compactness of W(z) is "an address book, not a teleportation device."

### Break 2 (fatal): Achievability ≠ Equilibrium
W(h) gives a strategy that ACHIEVES b uniformly, but L4 needs a strategy that is an APPROXIMATE EQUILIBRIUM of the block game. These are "different planets." Truncating an achieving witness does not turn it into a block-game equilibrium. This is worse on deviation histories: achievability gives no incentive control there.

## The missing lemma (precisely stated)
For every h, b in W(h), eta > 0, there exists L_0 such that for L >= L_0:
1. A profile sigma achieving b within eta on L-horizon
2. A selector beta(z) in W(z) for all terminal z, with continuation close to beta(z)
3. The first L stages form an eta-equilibrium of the L-block game with terminal payoffs beta

This is precisely "W is self-generating under equilibrium incentives" — which is Neyman's open problem reformulated.
