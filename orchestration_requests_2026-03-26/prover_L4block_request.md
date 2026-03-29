# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T02:58:00.000000+00:00

## Instructions

You are the prover role. Your task is a **single, sharply focused proof attempt** on L4*-block: the block-selector nonemptiness lemma with summable leakage. This is the ONLY remaining theorem-sized step in Route B.

**Do not re-derive L1-L2 or the post-selector tail (L5*-block through L10).** These are verified. Focus all effort on proving L4*-block.

Tag results with [DERIVED], assumptions with [ASSUMPTION+], gaps with [GAP], scope changes with [SCOPE].

## The Exact Claim (L4*-block)

For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, there exist:
- a global block schedule (L_t)_{t>=1} with L_t -> infinity
- nonneg per-block errors (r_t)_{t>=1} with sum_{t>=1} r_t <= epsilon/8

such that for every t >= 1, every level-(t-1) boundary history h, and every current bias b in W*(h), the block-feasibility set F_t(h,b) is nonempty and contains a triple (pi_h, beta_h, r) with r <= r_t.

## What F_t(h,b) Contains

A triple (pi_h, beta_h, r) where:

1. **pi_h** is an L_t-stage public-history block policy: at each within-block public history xi extending h, it specifies a product mixed action profile for the current state.

2. **beta_h(z) in W*(z)** for every block-end history z in Z_t(h).

3. **r >= 0** is the per-block leakage.

4. **Promise-tracking**: The block-averaged payoff under pi_h, plus the expected block-end continuation bias, minus the current bias, is within r of the root promise w^s for all players i.

5. **Block IC**: For every player i and every unilateral deviation tau_i confined to the L_t stages of the block, the analogous block-averaged deviation payoff plus expected block-end continuation minus current bias does not exceed w^s + r.

## What Is Available

- **W(h)** is nonempty, compact (L1, imported) — set of uniformly achievable, individually-rational payoffs.
- **W*(h)** is nonempty, compact (L2, imported) — tie-broken exposed face of W(h).
- **The game is finite**: finitely many players, states, actions, and successor states.
- **Block length L_t is a free parameter**: you can choose it as large as needed.
- **The target leakage r_t = 1/(4*L_t)**: decreasing with block length, geometrically summable.

## The Core Proof Idea (To Be Made Rigorous)

At a boundary history h with current bias b in W*(h):

1. **Choose an intended on-path prescription**: Since b in W*(h) subset W(h), there exists a strategy sigma^h that approximately achieves b uniformly in the continuation game from h. Use sigma^h's prescription for the next L_t stages as the "intended" block policy.

2. **Add within-block punishment**: If player i deviates at some within-block stage k, switch to a punishment mode for the remaining L_t - k stages. Since the game is finite, each player's minimax value is well-defined. Use minimax play against the deviator for the rest of the block (grim trigger within block).

3. **Choose block-end continuations**: At each block-end history z, choose beta_h(z) in W*(z) to match the bias drift required by the promise-tracking equation.

4. **Bound the leakage**: The one-shot gain from deviating is O(1) (bounded stage payoffs). The punishment cost is O(L_t - k) * (gap between target payoff and minimax). After block averaging, the net deviation gain is at most O(1/L_t).

## Key Technical Challenges

**Challenge A**: The "intended" block policy must use PRODUCT (uncorrelated) mixed actions at each within-block stage. The witness strategy sigma^h achieves b in the limit, but its one-step prescriptions may not exactly match the block-averaged target. Show that the block averaging absorbs this error.

**Challenge B**: The punishment must be implementable with product actions and public-history detection. In a multiplayer game, deviations may not be perfectly detectable from public history alone. Show that the punishment can be organized so that the deviator's expected continuation is sufficiently below the target. The standard approach is to punish using the minmax strategy against the worst-case deviator, which is detectable from public history in a stochastic game with observed actions.

**Challenge C**: The block-end continuation beta_h(z) in W*(z) must exist for every possible block-end state z. This follows from L2 (W*(z) is nonempty for all z), but the CHOICE of beta_h(z) must be consistent with the promise-tracking equation. Show that the freedom to choose beta_h(z) anywhere in the compact set W*(z) is enough to close the promise-tracking gap.

**Challenge D**: Uniformity over all boundary histories h and all current biases b in W*(h). The block construction must work regardless of the current state and bias. Since the game is finite, there are only finitely many states, and W*(h) depends only on the current state s(h). So there are only finitely many distinct block-feasibility problems per block level.

## What a Complete Answer Looks Like

A rigorous proof of L4*-block. The proof should:
1. Define the block policy pi_h explicitly (intended play + grim trigger)
2. Define the block-end continuation table beta_h
3. Verify promise-tracking (block-averaged form)
4. Verify block IC for all players and all within-block deviations
5. Show that the leakage r is at most r_t = 1/(4*L_t)
6. Confirm that the construction works uniformly over all histories and biases

If you cannot prove L4*-block in full generality, identify the EXACT point where the proof breaks and state the strongest partial result you can establish.
