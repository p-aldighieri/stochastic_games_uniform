# v26 Review — Pass 116

**Thinking**: ~30 min Extended Pro
**Verdict**: FAIL

## PASSES (Items 1, 6, 7)
- Induced MDP formulation: PASS — correctly defines finite MDP when others frozen
- Local machinery (Z, Psi, Bellman): PASS — no longer misused as global benchmark
- Fixed-point (Kakutani): PASS — legitimate fixed-point argument

## FAILS (Items 2, 3, 4, 5, 8)

### Gap 1: UNICHAIN CLAIM IS FALSE (Proposition 2402)
Condition (a) is LOCAL: inside a fixed node C, internal states remain irreducible.
The paper leaps to GLOBAL: the full routed induced MDP is unichain. This is false.

**Counterexample**: Game with s_0 and two absorbing states s_1, s_2. From s_0,
next state is s_1 or s_2 with prob 1/2 each. Root node has one internal state,
two exit labels to degenerate terminals. Condition (a) holds trivially (one state).
But induced MDP has two absorbing recurrent classes. NOT unichain.

Also: condition (a) quantifies over LOCAL selectors a_i(·) on Ξ_C, not over
arbitrary stationary policies on the full public-memory state space.

### Gap 2: COMPLIANT O(eta+delta)-OPTIMALITY NOT PROVED (Proposition 2435)
The claim that the fixed-point construction produces a policy whose average reward
is O(eta+delta)-optimal in the induced MDP is inserted as an undeclared extra theorem.
The fixed-point only gives LOCAL stationary Nash packages at each node, not GLOBAL
optimality. This is "not just unproved, it is generally false in multichain situations."

### Gap 3: Parameter bookkeeping
A_eta * eta → 0 assumed but never established.

## KEY INSIGHT FROM REVIEWER
"The local Bellman, Z/Psi, and Kakutani pieces survive. The new direct global
induced-MDP comparison does not."

The failure is because the tree routing creates an expanded MDP with terminal
absorbing nodes, even though the underlying game state space might be communicating
under condition (a). The tree structure introduces artificial non-irreducibility.
