# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T04:00:00.000000+00:00

## Instructions

You are the prover role. This is the decisive proof attempt. Two prior attempts on L4 failed:
- One-step L4* with W* continuations: FALSE (PD counterexample, singleton face kills it).
- Block L4* with W* continuations: reduces to a self-generation theorem for W* that is not supplied by L1-L2.

Both failures share the SAME root cause: W*(h+) can be too thin (e.g., singletons) to support the needed continuation flexibility.

**The repair:** Replace W*(h+) with the FULL set W(h+) as the continuation domain. Then:
- W(h) is the set of all uniformly achievable individually-rational payoff vectors (nonempty, compact by L1)
- W(h) is inherently defined by long-run achievability, which IS a self-generation concept
- In the PD counterexample that killed W*-restricted L4*, using full W already restores an exact one-step selector

Your task: prove L4-block with continuations in W(h+) instead of W*(h+).

## The Exact Claim (L4-block-fullW)

For every finite stochastic game G and every epsilon > 0, there exist:
- a global block schedule (L_t) with L_t -> infinity
- root promises w^s in W(s) for each initial state s
- nonneg errors (r_t) with sum r_t <= epsilon/8

such that for every t >= 1, every level-(t-1) boundary history h, and every current bias b in W(h), there exist:
- a block policy pi_h (L_t-stage, product actions stagewise)
- block-end continuations beta_h(z) in W(z) for all z in Z_t(h)  [NOTE: full W, not W*]
- leakage r <= r_t

satisfying the block promise-tracking and block IC conditions.

Equivalently (by prover 12's reduction): there exists a continuation selector beta(z) in W(z) such that the finite block game B_t(h,b;beta) has a behavioral Nash equilibrium with payoff within r_t of w^s.

## Why Full W Should Work

**Self-generation of W**: Since W(h) is defined as the set of uniformly achievable payoff vectors from history h, it has an inherent self-generation property:

For every w in W(h) and every delta > 0, there exists a strategy sigma that achieves w within delta for all sufficiently large horizons. This strategy prescribes actions at each stage. Truncating it to L stages and looking at what happens after those L stages gives a continuation that is approximately achievable — i.e., approximately in W(z) for the realized block-end history z. Since W(z) is compact, and the approximation error goes to 0 as L grows, the block construction should work.

**Key argument sketch:**
1. Fix b in W(h). By definition of W, there exists sigma^h such that for all large T, the T-horizon average payoff from sigma^h is within delta of b, with individual rationality.
2. Truncate sigma^h to L stages. The first L stages contribute a block-averaged payoff close to b (with error O(1/L) from the truncation).
3. After L stages, at terminal history z, the continuation under sigma^h achieves payoffs close to some vector in W(z) (because sigma^h was achieving b uniformly from h, and the continuation subgame from z has its own achievable set W(z)).
4. Choose beta(z) in W(z) to be the closest point to the required continuation. The error from this projection is bounded because W(z) is compact and the continuation value is close to W(z).
5. The total leakage from (a) block truncation and (b) W-projection is O(1/L), matching r_t = 1/(4L_t).
6. Block IC: Use sigma^h's prescription as the block policy. Since sigma^h is a (near-)equilibrium strategy in the infinite game, deviations within the block are approximately controlled by the equilibrium structure. Formalize via the block game reduction from prover 12.

## What Needs to Be Made Rigorous

1. **The continuation value after L stages lies close to W(z):** This is the key step. Use the definition of W and the uniform achievability to show that the continuation strategy from z achieves payoffs in W(z), and the truncation error is O(1/L).

2. **The block policy from the truncated strategy satisfies block IC:** The truncated strategy is not an exact equilibrium of the block game, but the deviation gain is bounded by O(1/L) because the infinite-game equilibrium properties are preserved up to truncation effects.

3. **The W(z)-projection error is controlled:** Since W(z) is compact, the nearest-point projection is well-defined and introduces at most the distance between the continuation value and W(z).

4. **The recursion works with W instead of W*:** Without W*'s tie-breaking, there's no canonical choice at each node. But the recursion only needs compactness and nonemptiness of W(z), which L1 guarantees. The root bias w^s can be chosen as any element of W(s).

## What a Complete Answer Looks Like

Either a rigorous proof of L4-block-fullW, or a precise identification of where the argument breaks even with full W.

The key question is: does the self-generation property of W (defined by uniform long-run achievability) translate into the block decomposition required by L4-block?

Focus on making the argument sketch above rigorous. This is the most natural path to the theorem.
