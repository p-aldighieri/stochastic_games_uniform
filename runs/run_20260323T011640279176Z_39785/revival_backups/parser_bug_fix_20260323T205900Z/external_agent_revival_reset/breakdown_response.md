Fix a finite stochastic game (G) and (\varepsilon>0). The target is the exact strategy-existence statement
[
\exists \sigma\in \Sigma(G)\ \exists T_0\ \forall T\ge T_0\ \forall s_1\in S\ \forall i\in N\ \forall \tau_i\in \Sigma_i(G):
\gamma_i^T(G,s_1,\sigma)\ge \gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon,
]
with one public-history behavioral profile (\sigma) working for every sufficiently large horizon and every initial state. The project is still bootstrap/open, and the preferred route is the Martin-function bootstrap to a global Nash selector; the durable memo identifies the selector step as the main blocker.   

Let (H) be the rooted public-history tree, with root layer identified with (S), and let (s(h)) be the terminal state of a history (h). Fix a nonnegative depth schedule ((\eta_t)*{t\ge1}) with (\sum_t \eta_t<\infty), and write (\eta(h):=\eta*{|h|}). For a history (h), define
[
\operatorname{Succ}(h):={(h,a,s'):\ a\in A(s(h)),\ s'\in S,\ P(s'|s(h),a)>0}.
]
For a product mixed action (x\in \prod_j \Delta(A_j(s(h)))) and a successor assignment (\phi:\operatorname{Succ}(h)\to \mathbb R^N), define
[
\mathcal T_i(h;x,\phi)
:=
\sum_{a,s'} x(a),P(s'|s(h),a),\bigl(u_i(s(h),a)+\phi_i(h,a,s')\bigr),
]
and for a pure unilateral deviation (a_i'\in A_i(s(h))),
[
\mathcal T_i(h;a_i',x_{-i},\phi)
:=
\sum_{a_{-i},s'} x_{-i}(a_{-i}),P(s'|s(h),(a_i',a_{-i})),
\bigl(u_i(s(h),(a_i',a_{-i}))+\phi_i(h,(a_i',a_{-i}),s')\bigr).
]

**Dependency spine:** (L1 \to L2 \to L3 \to L4 \to L5 \to {L6,L7} \to L8).

### [BREAKDOWN_AMEND] L1. Safe promise correspondence

**Statement.** There exists a constant (B<\infty) and a correspondence (W) assigning to each public history (h) a compact set (W(h)\subset[-B,B]^N) of Martin-safe continuation promises, with closed graph on each depth layer, such that every (w\in W(h)) is minmax-safe for the rooted subgame at (h) in the sense intended by the route.

**Dependencies.** No internal dependencies; this is the imported continuation object.

**Technique hint.** Define (W(h)) as the closure of bounded continuation promises obtainable from the rooted subgame at (h) while preserving the subgame minmax safety constraints at descendants. Compactness comes from boundedness plus finite-dimensional closure; the bound (B) is the endpoint-normalization ingredient.

**Difficulty estimate.** Hard, but intended as imported machinery rather than the new theorem step.

---

### [BREAKDOWN_AMEND] L2. Historywise nonemptiness of (W)

**Statement.** For every public history (h), (W(h)\neq\varnothing). In particular, for every initial state (s\in S), there exists at least one root promise (w(s)\in W(s)).

**Dependencies.** L1.

**Technique hint.** Apply the root-bias nonemptiness input to each rooted subgame separately. Every public history defines another finite stochastic game of the same type, so a root theorem for one rooted subgame can be reapplied at every node.

**Difficulty estimate.** Hard.

---

### [BREAKDOWN_AMEND] L3. Compact local feasibility correspondence

**Statement.** For each pair ((h,w)) with (w\in W(h)), let (F(h,w)) be the set of all pairs ((x,\phi)) such that (x) is a product mixed action at (s(h)), (\phi(h')\in W(h')) for every (h'\in \operatorname{Succ}(h)), and for every player (i),
[
w_i \le \mathcal T_i(h;x,\phi)+\eta(h),
]
[
\mathcal T_i(h;a_i',x_{-i},\phi)\le w_i+\eta(h)\qquad\forall a_i'\in A_i(s(h)).
]
Whenever nonempty, (F(h,w)) is compact, and its graph is closed on each depth layer.

**Dependencies.** L1, L2.

**Technique hint.** The simplices of product mixed actions are compact, successor sets are finite, the map ((x,\phi)\mapsto \mathcal T_i) is continuous, and the defining inequalities are closed.

**Difficulty estimate.** Moderate.

---

### [BREAKDOWN_AMEND] L4. One-step uncorrelated Nash selector

**Statement.** For every public history (h) and every promise (w\in W(h)), the set (F(h,w)) is nonempty.

Equivalently, every safe promise can be decomposed at one step into:

1. an **uncorrelated** product mixed action (x(h)), and
2. successor promises (\phi(h')\in W(h')) for all (h'\in \operatorname{Succ}(h)),

such that the current promise is approximately delivered under compliance and no unilateral one-shot deviation can exceed that promise by more than (\eta(h)).

**Dependencies.** L1, L2, L3.

**Technique hint.** This is the missing selector theorem. It would have to upgrade currently available Martin-function outputs, which are known to give individually rational objects, correlated objects, or subgame-local objects, into a single product-mixed local selector that works at every node of the history tree.

**Difficulty estimate.** Extreme.

**Critical lemma.** This is the hardest step. It is exactly the place where the durable route memo says the route is still theorem-sized and unresolved; existing machinery stops short of the required uncorrelated selector. Everything after L4 is mainly tree assembly plus telescoping bookkeeping.  

---

### [BREAKDOWN_AMEND] L5. Global recursive assembly of a single whole-game profile

**Statement.** Choose one root promise (w(s)\in W(s)) for each (s\in S). Assuming L4, there exists a single family
[
{(x(h),w(h)) : h\in H}
]
such that (w(h)\in W(h)) for every history (h), and ((x(h),\phi_h)\in F(h,w(h))) for some successor assignment (\phi_h), with (w(h')=\phi_h(h')) for each successor (h'). Defining
[
\sigma(h):=x(h)
]
produces one behavioral profile on the full public-history tree, simultaneously covering every initial state.

**Dependencies.** L2, L4.

**Technique hint.** Recursion on the countable rooted public-history tree. Because the tree is countable and each node has finite branching, one can choose a witness from (F(h,w(h))) node by node; no sophisticated measurable-selection theorem is needed here. This is also the explicit repair of the statewise-to-global assembly issue.

**Difficulty estimate.** Hard. The durable memo treats this as salvageable once the selector exists. 

---

### [BREAKDOWN_AMEND] L6. Equilibrium-path delivery inequality

**Statement.** Let (\sigma) be the profile from L5. For every initial state (s), player (i), and horizon (T\ge1),
[
w_i(s)\le
\mathbb E_{s,\sigma}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t) + w_i(h_{T+1})
\right]
+\sum_{t=1}^{T}\eta_t.
]

**Dependencies.** L5.

**Technique hint.** Iterate the first inequality in the definition of (F(h,w)) along the realized play under (\sigma), condition on (h_t), and telescope the successor-promise terms.

**Difficulty estimate.** Moderate.

---

### [BREAKDOWN_AMEND] L7. Deviating-path upper bound

**Statement.** Let (\sigma) be the profile from L5. For every initial state (s), player (i), unilateral deviation strategy (\tau_i), and horizon (T\ge1),
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t) + w_i(h_{T+1})
\right]
\le
w_i(s)+\sum_{t=1}^{T}\eta_t.
]

**Dependencies.** L5.

**Technique hint.** Condition on the visited history (h_t). The second inequality in the definition of (F(h,w)) handles every pure one-shot deviation (a_i'); linearity then extends it to mixed actions chosen by (\tau_i(h_t)). Iterate this dynamic-programming inequality over time.

**Difficulty estimate.** Hard.

**Note.** This formulation avoids needing a separate “identify the deviator and enter punishment mode” lemma. If one insists on literal punishment phases, that becomes a stronger auxiliary lemma, not a weaker one.

---

### [BREAKDOWN_AMEND] L8. Telescoping comparison and uniformization

**Statement.** Under the hypotheses of L6 and L7, for every initial state (s), player (i), deviation (\tau_i), and horizon (T\ge1),
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2B}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]
Hence there exists (T_0) such that for all (T\ge T_0),
[
\gamma_i^T(s,\sigma)\ge \gamma_i^T(s,(\tau_i,\sigma_{-i}))-\varepsilon
]
for every (s\in S), every player (i), and every unilateral deviation (\tau_i).

**Dependencies.** L1, L6, L7.

**Technique hint.** Subtract the L6 lower bound from the L7 upper bound, control the two endpoint terms by (|w_i(h)|\le B), divide by (T), and use (\sum_t\eta_t<\infty). This is the telescoping and bookkeeping tail of the route.

**Difficulty estimate.** Moderate. The durable memo explicitly says the telescoping and nonnegative-(\eta_t) bookkeeping steps are fine once the selector exists. 

---

## [BREAKDOWN_AMEND] Glue steps to the final conclusion

**G1. Fix (G) and (\varepsilon).** Choose a summable nonnegative leakage schedule ((\eta_t)).

**G2. Build the tree object.** Use L1 and L2 to obtain (W(h)) and root promises (w(s)) for all (s\in S).

**G3. Assemble one global profile.** Apply L4 and then L5 to produce a single public-history behavioral profile (\sigma) on the entire game, not one profile per state.

**G4. Prove the uniform equilibrium inequality.** Apply L6, L7, and L8. This yields a threshold (T_0) such that for all (T\ge T_0),
[
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G):\
\gamma_i^T(G,s_1,\sigma)\ge \gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Since (G) and (\varepsilon) were arbitrary, this would prove (\operatorname{HasUniformEq}(G)) for all finite stochastic games, in exactly the adopted strategy-existence sense rather than the payoff-set sense. At present this remains conditional on L4, so the route is still a bootstrap plan rather than a proof.  

## [BREAKDOWN_AMEND] Bottleneck summary

The proof skeleton is structurally clean:

[
\text{safe promises} \Rightarrow \text{local feasible correspondence} \Rightarrow \text{uncorrelated selector} \Rightarrow \text{tree recursion} \Rightarrow \text{telescoping} \Rightarrow \text{uniform equilibrium}.
]

But the skeleton only starts walking once L4 exists. That lemma is not bookkeeping wearing a false mustache; it is the mathematical furnace at the center of the route. If L4 cannot be proved, the route has likely run directly into the open problem rather than around it.
