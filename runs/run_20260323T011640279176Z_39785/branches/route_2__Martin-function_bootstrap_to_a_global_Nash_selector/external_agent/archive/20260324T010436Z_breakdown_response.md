# Route B breakdown: Martin-function bootstrap to a global Nash selector

This breakdown keeps the theorem-side target exactly as fixed in the packet and durable sources: for every finite stochastic game (G) and every (\varepsilon>0), produce one public-history behavioral profile (\sigma) and one threshold (T_0) such that (\sigma) is an (\varepsilon)-equilibrium for every (T\ge T_0) and every initial state. The theorem remains open; this is a bootstrap decomposition of the preferred current route, not a completed proof.    

## Setup

Let (h) be a public history, and let (s(h)) be its terminal state. Fix a nonnegative leakage schedule ((\eta_t)*{t\ge1}), with (\eta(h):=\eta*{|h|}), to be chosen later so that the cumulative leakage is at most the target (\varepsilon).

Because the later telescoping step needs explicit bounded bias terms, work with a bias-refined continuation correspondence (Z(h)). An element of (Z(h)) is a pair
[
z_h=(w_h,b_h),
]
where (w_h\in[0,1]^N) is the continuation payoff promise and (b_h\in\mathbb R^N) is a bounded Martin bias vector. Let
[
W(h):={w_h:\exists b_h\text{ with }(w_h,b_h)\in Z(h)}.
]

For (z_h=(w_h,b_h)\in Z(h)), define the one-step feasibility set (F(h,z_h)) to consist of pairs ((x_h,\zeta_h)) such that:

* (x_h=\bigotimes_{i\in N}x_{h,i}) is a product mixed action at state (s(h)),
* for every child history (h'=(h,a,s')), (\zeta_h(h')=z_{h'}=(w_{h'},b_{h'})\in Z(h')),
* and for every player (i) and every pure one-step deviation (a_i'\in A_i(s(h))), the Martin one-step equilibrium inequalities hold:
  [
  w_{h,i}+b_{h,i}
  \le
  \mathbb E_{x_h,P}!\left[u_i(s(h),a)+w_{H'}+b_{H'}\right]+\eta(h),
  ]
  [
  \mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+w_{H'^{a_i'}}+b_{H'^{a_i'}}\right]
  \le
  w_{h,i}+b_{h,i}+\eta(h).
  ]

This is the schematic local self-generation condition for the route. If the exact Martin normalization later changes, the dependency graph below should stay the same and only the local formulas need amendment.

## Lemmas

### L1. Subgame reduction from histories to terminal states

**Statement.**
For every public history (h), the continuation game after (h) is canonically identified with the original stochastic game started from state (s(h)). Hence any state-indexed object, such as a maxmin value, punishment strategy, Martin correspondence, or continuation selector, can be pulled back to every history ending in that state.

**Dependencies.**
Only the model definition.

**Technique hint.**
Use the shift-of-history identification: after (h), future law and payoffs depend only on the current state and future actions.

**Difficulty estimate.**
Easy.

---

### L2. Nonempty bounded continuation correspondence

**Statement.**
There exists a constant (B<\infty) and, for every public history (h), a nonempty compact set
[
Z(h)\subseteq [0,1]^N\times [-B,B]^N
]
such that every (z_h=(w_h,b_h)\in Z(h)) satisfies the minmax safety bounds
[
w_{h,i}\ge m_i(s(h)) \qquad \forall i\in N,
]
where (m_i(s)) is player (i)'s statewise uniform maxmin value. In particular, for each initial state (s\in S), there exists at least one root label
[
z^s_\varnothing=(w^s,b^s)\in Z(s).
]

This is the root-bias nonemptiness input needed for the tree recursion.

**Dependencies.**
L1, plus the imported Martin-function / uniform maxmin machinery.

**Technique hint.**
Start from statewise subgame (\varepsilon)-maxmin or minmax-safe continuations already supplied by the Martin framework, then package the guaranteed payoff and bounded bias into a label (z_h).

**Difficulty estimate.**
Hard, but intended as source-backed input rather than the novel step.

---

### L3. Compactness and heredity of the local feasibility problem

**Statement.**
For every history (h) and every label (z_h\in Z(h)), the set (F(h,z_h)) is a closed subset of
[
\left(\prod_{i\in N}\Delta(A_i(s(h)))\right)\times \left(\prod_{h'\text{ child of }h} Z(h')\right).
]
Since the domain is compact, (F(h,z_h)) is compact whenever it is nonempty. Also, if ((x_h,\zeta_h)\in F(h,z_h)), then every child label (\zeta_h(h')) lies in (Z(h')), so the same construction may be iterated at descendants.

**Dependencies.**
L2.

**Technique hint.**
The immediate-child set is finite because states and actions are finite. The constraints are finitely many linear or polynomial inequalities in (x_h) and the child labels. Pure one-step deviations suffice, since mixed one-step deviations are convex combinations.

**Difficulty estimate.**
Moderate.

---

### L4. One-step uncorrelated self-generation at every history

**Statement.**
For every public history (h) and every label (z_h\in Z(h)), the local feasibility set (F(h,z_h)) is nonempty.

Equivalently, every Martin-admissible promise can be implemented at that history by:

1. a product mixed action (x_h=\bigotimes_i x_{h,i}), and
2. a choice of child labels (z_{h'}\in Z(h')) for all immediate descendants,

so that no player can gain more than (\eta(h)) from a one-step unilateral deviation.

This is the uncorrelated one-step Nash selector.

**Dependencies.**
L2 and L3, plus any new selector theorem strong enough to upgrade correlated or state-by-state admissibility to a product-mixed selector on the full public-history tree.

**Technique hint.**
This is where the gears actually bite. The likely route is to show that the Martin continuation correspondence admits a Nash-feasible product slice at every node, perhaps via a Kakutani-type fixed-point argument inside the local feasibility region, or via a new projection theorem taking a correlated self-generating witness to an uncorrelated one without losing the incentive inequalities.

**Difficulty estimate.**
Extreme. This is theorem-sized.

---

### L5. Recursive assembly of a single whole-game profile

**Statement.**
Assume L4. For each initial state (s), choose one root label (z^s_\varnothing\in Z(s)). Then there exists:

* a single behavioral strategy profile (\sigma) defined on the union of all public histories of the game, and
* a label (z_h\in Z(h)) for every public history (h),

such that for every (h), the mixed action prescribed by (\sigma) at (h) and the descendant labels chosen at the children of (h) form one witness in (F(h,z_h)).

In particular, this yields one whole-game profile (\sigma), not a separate family ((\sigma^s)_{s\in S}).

**Dependencies.**
L2 and L4.

**Technique hint.**
Recursion on the finitely branching public-history forest rooted at the finitely many initial states. Once every node has a feasible local witness and every root has a label, the global profile is assembled by dependent choice on a countable tree.

**Difficulty estimate.**
Moderate once L4 exists.

---

### L6. Strong reduction from arbitrary deviations to stagewise deviations

**Statement.**
Assume L5. Let (i\in N), let (h) be any public history, and let (\tau_i) be any behavioral deviation from (h) onward. Then the deviation gain admits a recursive upper bound of the form
[
\Delta_i(h,\tau_i)
\le
\eta(h)+
\mathbb E_{(\tau_i,\sigma_{-i})}!\left[\Delta_i(H_{+},\tau_i^{H_{+}})\mid H=h\right],
]
where (H_{+}) is the realized child history and (\tau_i^{H_{+}}) is the continuation deviation after that child history.

Consequently, controlling every pure one-step deviation at every node is enough to control every full behavioral deviation.

**Dependencies.**
L5.

**Technique hint.**
Use a one-shot deviation principle on the promise-labeled history tree. Public monitoring matters here because the realized action profile and next state are public, so the continuation label after every realized child history is common knowledge and already fixed by the tree construction.

**Difficulty estimate.**
Hard. This lemma must be kept in this strong recursive form; a weaker “there exists a punishment mode” statement is not enough.

---

### L7. Telescoping bound over finite horizons

**Statement.**
Assume L5 and L6. Then there exists a universal constant (c), depending only on the adopted Martin normalization, such that for every initial state (s), every horizon (T), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))
------------------------------------

\gamma_i^T(G,s,\sigma)
\le
\frac{cB}{T}+\sum_{t=1}^{T}\eta_t.
]

Equivalently, once the recursive one-step inequalities are summed along the realized path, all interior promise/bias terms cancel, leaving only an endpoint bias error of order (O(1/T)) and the cumulative leakage.

**Dependencies.**
L2, L5, and L6.

**Technique hint.**
Take the recursive inequality from L6, iterate it along the path, then telescope. The bounded bias terms are the only endpoint residue. This is the “promise bookkeeping collapses to a boundary term” step.

**Difficulty estimate.**
Moderate once the selector and recursive deviation bound are in place.

---

### L8. Uniform (\varepsilon)-equilibrium conclusion

**Statement.**
Choose the leakage schedule so that
[
\sum_{t\ge1}\eta_t \le \frac{\varepsilon}{2}.
]
Let (T_0) be large enough that
[
\frac{cB}{T_0}\le \frac{\varepsilon}{2},
]
where (B) and (c) are from L2 and L7. Then for every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Hence (\sigma) is a uniform (\varepsilon)-equilibrium of (G).

**Dependencies.**
L7 and the explicit nonnegativity of (\eta_t).

**Technique hint.**
Pure bookkeeping.

**Difficulty estimate.**
Easy.

## Critical lemma

**L4 is the critical lemma.** It is the hardest step because existing Martin-function tools appear to deliver individually rational objects, correlated objects, or subgame-specific objects, but not yet a single product-mixed one-step selector at every public history. Solving L4 would amount to the missing bridge from statewise or correlated continuation admissibility to one global Nash-feasible selector on the full history tree. The durable route memo explicitly flags this as the theorem-sized unresolved bottleneck, while L5, L7, and L8 are viewed as conditionally repairable once L4 exists. 

## Glue steps to the final conclusion

### G1. Fix the theorem inputs exactly once

Take an arbitrary finite stochastic game (G) and arbitrary (\varepsilon>0). Choose a nonnegative leakage schedule ((\eta_t)) with total mass at most (\varepsilon/2).

### G2. Seed all initial states

Use L2 to pick one root label (z^s_\varnothing\in Z(s)) for every initial state (s\in S).

### G3. Build one whole-game profile

Assuming L4, apply L5 to recursively define a single public-history behavioral profile (\sigma) on the entire history forest, together with a consistent label (z_h) at every node.

### G4. Convert local incentives into full no-profitable-deviation bounds

Apply L6 to reduce arbitrary behavioral deviations to recursive one-step deviations, then apply L7 to telescope the resulting inequality over (T) stages.

### G5. Uniformize in the horizon

Use L8 to choose (T_0) so that the endpoint bias term is at most (\varepsilon/2). Since the leakage sum is also at most (\varepsilon/2), (\sigma) is a uniform (\varepsilon)-equilibrium for every initial state.

### G6. Quantify back out

Because (G) and (\varepsilon) were arbitrary, proving L1 through L8 would prove
[
\forall G\in\mathfrak G,\ \forall \varepsilon>0,\ \exists \sigma,\exists T_0,\ \forall T\ge T_0,\ \forall s_1,\forall i,\forall \tau_i:
\gamma_i^T(G,s_1,\sigma)\ge \gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]

## Current status of the breakdown

* L1 is formal scaffolding.
* L2 is the imported Martin/maxmin seed layer.
* L3 is compactness and local well-posedness.
* L4 is the genuine research bottleneck.
* L5 is a recursion lemma once L4 and root nonemptiness are available.
* L6 must stay strong enough to propagate incentives for arbitrary behavioral deviations.
* L7 and L8 are telescoping and bookkeeping once the earlier structure exists.

So the route is coherent as a dependency graph, but it does **not** currently close the open theorem because L4 remains unresolved.  

## [BREAKDOWN_AMEND]

Use the following patch format to edit the plan without rewriting the whole document:

```text
[BREAKDOWN_AMEND]
Target: L4
Replace statement: <new lemma statement>
New dependencies: <comma-separated IDs>
Technique update: <new proof idea or warning>
Downstream changes: <which later lemmas must be edited>
Reason: <why the change is necessary>
[/BREAKDOWN_AMEND]
```

Valid targets are `Setup`, `L1` through `L8`, and `G1` through `G6`.
