# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T01:10:00.000000+00:00

## Instructions

You are the prover role. Your task is a **single, sharply focused proof attempt**: prove or disprove that the fixed-promise selector can be chosen with controlled (depth-summable) leakage. This is the theorem-sized bottleneck L4* in Route B of the uniform equilibrium proof.

**Do not re-derive the post-selector tail.** L5*-L10 are already verified and conditionally correct. Do not discuss Route A. Focus all effort on L4*.

Tag new results with [DERIVED], new assumptions with [ASSUMPTION+], and scope changes with [SCOPE]. If you identify a genuine obstruction to L4*, state it precisely with [GAP] and propose the most promising alternative formulation or workaround.

## Mathematical Context

### The Theorem Target
For every finite stochastic game G = (N, S, (A_i), u, P) and every epsilon > 0, prove the existence of a strategy profile sigma and threshold T_0 such that sigma is a uniform epsilon-equilibrium for all T >= T_0, all initial states, all players, all unilateral deviations.

### What Is Already Proved (Do Not Re-derive)
- **L3* compactness half**: The local feasibility set F_s*(h,b) is compact for every valid input.
- **L5*-L10**: The entire post-selector tail (rooted recursion, literal assembly, telescoping, threshold extraction, global assembly, conditional synthesis) is verified as correct by multiple reviewer passes.
- **Trivial nonemptiness**: F_s*(h,b) is trivially nonempty when eta = 2 (both promise-tracking and incentive constraints become vacuous). So basic L4* is not the issue.

### The Actual Open Problem: Controlled Leakage (Strong L4*)

The feasibility set F_s*(h,b) is defined for initial state s, history h in the rooted tree H^s, and current bias b in W*(h). It consists of tuples (x, beta, eta) where:

1. x in X(h) := prod_j Delta(A_j(s(h)))  [uncorrelated mixed action profile]
2. beta(h+) in W*(h+) for every child h+ in C(h)  [continuation biases in the compact tie-broken set]
3. eta in [0, 2]
4. Promise-tracking (E_h^i): u_i(s(h), x) + E_{x,P}[beta_i(H') | h] - b_i >= w_i^s - eta,  for all i
5. Incentive-compatibility (D_h^{i,a_i'}): u_i(s(h), a_i', x_{-i}) + E_{a_i',x_{-i},P}[beta_i(H') | h] - b_i <= w_i^s + eta,  for all i, a_i'

Here w^s in W*((s)) is the fixed root promise chosen at the start, and b is the current bias inherited from the parent node.

**Strong L4* (what needs to be proved):** For every epsilon > 0, there exists a depth-based budget r_t >= 0 with sum_{t>=1} r_t <= epsilon/8, and a full-tree selector choosing (x(h), beta(h), eta(h)) in F_s*(h, b(h)) at each node with eta(h) <= r_{|h|}.

Equivalently: the leakage at each depth level can be made to decrease fast enough (e.g., r_t ~ epsilon * 2^{-t}) that the total leakage is finite.

### Why This Is Hard

The difficulty is the **uncorrelatedness** constraint (x must be a product distribution, not a correlated action) combined with the requirement that eta vanishes with depth. If correlated actions were allowed, the problem would reduce to a linear feasibility problem (always solvable by the minimax theorem). With uncorrelated actions, we need a Nash equilibrium of an auxiliary one-shot game at each node, and the gap between Nash and correlated equilibrium payoffs is the source of leakage.

### Key Structural Facts Available

1. **W(h) is nonempty and compact** (L1, imported). It is the set of uniformly achievable, individually-rational payoff vectors at history h.
2. **W*(h) = argmax_{w in W(h)} b(h) . w** is nonempty and compact (L2, imported). The bias is a deterministic tie-breaker.
3. **The game is finite**: at each state, there are finitely many players, finitely many actions per player, and finitely many successor states.
4. **Nash's theorem**: every finite normal-form game has a Nash equilibrium in mixed strategies.
5. **The continuation biases beta(h+) can be freely chosen from W*(h+)**: this is a large degree of freedom. The prover can exploit the full richness of the continuation set.

### Suggested Proof Strategies (Non-Exhaustive)

**Strategy A: Approximate self-generation via Nash existence.** At each node h with bias b, construct an auxiliary finite game where player i's payoff from action profile a is V_i(a) = u_i(s(h), a) + sum_{s'} P(s'|s(h),a) * beta_i(h,a,s'). Choose beta to make b (or something close to it) a Nash equilibrium payoff of this auxiliary game. Then eta measures the gap between the Nash payoff and the target w^s. Show this gap can be made small by careful choice of beta from the compact set W*.

**Strategy B: Block construction.** Divide the tree into finite blocks. Within each block, play an approximate equilibrium of the block-game. Show that inter-block transitions contribute only a bounded correction, and the total leakage is geometrically decreasing because block length grows.

**Strategy C: Kakutani fixed-point on a controlled-leakage correspondence.** Define a correspondence from (b, r) to the set of (x, beta, eta) satisfying F_s* constraints with eta <= r. Show this correspondence is upper-hemicontinuous with nonempty convex values (in an appropriate product space), and apply Kakutani. The challenge is ensuring nonemptiness for small r.

**Strategy D: Exploit the definition of W(h).** Since b in W*(h) subset W(h), there exists a strategy sigma^h that approximately achieves b uniformly. This strategy's one-step prescription at h gives a mixed action and continuation. Show that this "witness" strategy provides a valid (x, beta, eta) with small eta. The key is that the witness strategy already achieves b in the limit, so the one-step gap should be controllable.

**Strategy E: Disproof / counterexample.** If the controlled leakage version is false, construct a finite stochastic game where the uncorrelated leakage at every node is bounded below by some constant delta > 0. This would imply that the entire Route B cannot work and the theorem (if true) requires a fundamentally different proof architecture.

### What a Complete Answer Looks Like

Either:
1. A proof of Strong L4* (or an equivalent reformulation that plugs into the existing L5*-L10 tail), OR
2. A precise identification of the obstruction, with a concrete counterexample or impossibility argument, and a proposed alternative formulation that might circumvent it.

Do not produce a generic survey of difficulties. Produce a mathematical argument.
