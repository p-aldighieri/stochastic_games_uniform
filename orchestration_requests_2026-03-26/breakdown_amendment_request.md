# External Agent Request (breakdown)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T02:00:00.000000+00:00

## Instructions

You are the breakdown role. Your task is to produce a **clean, amended breakdown** for Route B that replaces the falsified one-step L4* with a block selector version. The post-selector tail (L5*-L10) must be adapted to the block architecture but should preserve its verified logical structure wherever possible.

**Context:** Prover 11 proved that Strong L4* (one-step, W*-restricted) is false via a concrete Prisoner's Dilemma counterexample where leakage eta >= 1/10 at every depth. The key insight is that when W*(h+) is a singleton, the selector has no continuation freedom and collapses to an approximate Nash problem. The proposed repair is a block selector where L_t-stage block policies replace one-step selectors, and "grim trigger within block" strategies make r_t = 1/(4*L_t) with geometric L_t giving summable leakage.

## What You Must Produce

A complete amended breakdown with:

1. **L1-L2**: Keep as imported (unchanged from current breakdown).

2. **L3*-block (compactness)**: Reformulate the local feasibility set for block selectors. At each node h and current bias b in W*(h), a block feasibility tuple is (pi_h, beta_h, r) where:
   - pi_h is an L_t-stage public-history block policy (product actions at each stage within the block)
   - beta_h(z) in W*(z) for each block-end terminal history z
   - r >= 0 is the per-block leakage
   - Promise-tracking and incentive-compatibility hold in averaged form over the block

3. **L4*-block (nonemptiness with summable leakage)**: The central claim. For every epsilon > 0, there exists a sequence of block lengths L_t and per-block errors r_t with sum_t r_t <= epsilon/8, such that at every node the block feasibility set is nonempty with leakage at most r_t. Include the key proof idea: within a block of length L_t, play the target action profile and use deviation-contingent punishment within the block to suppress gain to O(1/L_t).

4. **L5*-block through L10**: Adapt the post-selector tail to the block recursion. The recursion now proceeds over block boundaries rather than single steps. The telescoping, threshold extraction, global assembly, and synthesis should carry over with appropriate modifications.

## Constraints

- Keep the theorem-side target EXACTLY as before: one whole-game behavioral profile, one threshold, all sufficiently large horizons, every initial state.
- Keep the proof labeled as bootstrap/open until L4*-block is actually proved.
- Mark which lemmas are proved, which are conditional, and which are open.
- The amended breakdown should be self-contained — a reader should understand the full proof architecture from this document alone.
- Tag breakdown amendments with [BREAKDOWN_AMEND] and mark the critical lemma clearly.
- Do not include old/superseded numbering. This is a clean rewrite of the backbone.
