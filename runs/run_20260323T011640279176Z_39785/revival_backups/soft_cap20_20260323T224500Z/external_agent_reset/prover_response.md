[BREAKDOWN_AMEND] I will use the typed reading
[
\sum_{a}x(a)\Bigl(u_i(s(h),a)+\sum_{s'}P(s'|s(h),a),b_i^{a,s'}\Bigr)-b_i\ge w_i-\eta_{|h|},
]
and
[
\sum_{a_{-i}}x_{-i}(a_{-i})\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i})),b_i^{(a_i',a_{-i}),s'}\Bigr)-b_i
\le w_i+\eta_{|h|},
]
for (Bal) and (Dev). As written in the packet, the displayed formulas have a comma where scalar multiplication is needed, so they are ill-typed until this repair is made. This is a notation repair only. 

## 1. L1

[DERIVED] **Lemma L1.** For every public history (h), the continuation game (G_h) is again a finite stochastic game of the same class. For every player (i), horizon (T), and opponents’ profile (\sigma_{-i}) on (G_h), the value
[
V_i^T(h,\sigma_{-i})=\sup_{\tau_i}\gamma_i^T(G_h,\mathrm{root}(h),(\tau_i,\sigma_{-i}))
]
is well defined.

**Proof.** Let (h) end at state (s(h)). The continuation game (G_h) keeps the same player set (N), state set (S), action sets (A_i(s)), stage payoffs (u_i(s,a)), and transition kernel (P(\cdot\mid s,a)), but starts from the continuation history rooted at (s(h)). Because (N,S), and every (A_i(s)) are finite, and (u,P) are unchanged, (G_h) is again a finite stochastic game of the same class as in the formal model. This is a direct unpacking of the model definition.  

Fix (i,T,\sigma_{-i}). Only the first (T) stages matter for (\gamma_i^T). Hence player (i)'s deviation problem depends only on the finitely many continuation public histories of lengths (1,\dots,T). For each such history (g), a truncated deviation strategy chooses one mixed action in the simplex (\Delta(A_i(s(g)))). Therefore the set of truncated deviation strategies is a finite product of nonempty compact simplices, hence itself nonempty and compact.

For fixed (\sigma_{-i}), the law of every (T)-stage play in (G_h) is a polynomial in those finitely many local mixing probabilities, because each play probability is obtained by multiplying stage-action probabilities and transition probabilities. Therefore
[
\tau_i\longmapsto \gamma_i^T(G_h,\mathrm{root}(h),(\tau_i,\sigma_{-i}))
]
is continuous on a compact set. By the extreme value theorem, the supremum is attained, hence finite and well defined. Equivalently, once (\sigma_{-i}) is fixed, player (i)'s problem is a finite-horizon controlled Markov problem with state variable equal to the current public history. ∎

## 2. L3

[DERIVED] **Lemma L3.** For fixed (h) and ((w,b)\in\mathcal C(h)), the local feasibility relation (\mathcal F(h,w,b)) is compact.

**Proof.** Let
[
X(h):=\prod_{j\in N}\Delta(A_j(s(h))).
]
Each (\Delta(A_j(s(h)))) is a compact simplex, so (X(h)) is compact.

Let
[
\mathrm{Succ}(h):={,h[a,s'] : a\in A(s(h)),\ s'\in S,}.
]
This set is finite because (A(s(h))) and (S) are finite. By L2, for each (g\in\mathrm{Succ}(h)), the set (\mathcal C(g)\subseteq [0,1]^N\times[-C,C]^N) is compact. Hence
[
Y(h):=\prod_{g\in\mathrm{Succ}(h)}\mathcal C(g)
]
is compact. Therefore
[
D(h,w,b):=X(h)\times Y(h)
]
is compact.

Now write a generic element of (D(h,w,b)) as
[
\Bigl(x,\bigl((w^g,b^g)\bigr)*{g\in\mathrm{Succ}(h)}\Bigr).
]
For each player (i), define
[
\Phi_i(x,(w^g,b^g)*g)
:=
\sum_a x(a)\Bigl(u_i(s(h),a)+\sum*{s'}P(s'|s(h),a),b_i^{h[a,s']}\Bigr)-b_i-(w_i-\eta*{|h|}),
]
and for each pure deviation (a_i'\in A_i(s(h))),
[
\Psi_{i,a_i'}(x,(w^g,b^g)*g)
:=
(w_i+\eta*{|h|})-\Bigl[\sum_{a_{-i}}x_{-i}(a_{-i})
\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i})),b_i^{h[(a_i',a_{-i}),s']}\Bigr)-b_i\Bigr].
]
Because (x(a)=\prod_j x_j(a_j)) and (x_{-i}(a_{-i})=\prod_{j\neq i}x_j(a_j)), each (\Phi_i) and (\Psi_{i,a_i'}) is continuous on (D(h,w,b)).

By definition,
[
\mathcal F(h,w,b)
=================

D(h,w,b)\cap\bigcap_{i}{\Phi_i\ge 0}\cap\bigcap_{i,a_i'}{\Psi_{i,a_i'}\ge 0}.
]
This is an intersection of finitely many closed subsets of the compact set (D(h,w,b)). Hence (\mathcal F(h,w,b)) is closed in a compact set, therefore compact. The empty set is also compact, so no separate nonemptiness argument is needed here. ∎

## 3. L5 and L6, conditional on L4

[DERIVED] **Lemma L5.** Assuming L2 and L4, the rooted recursion statement holds as written.

**Proof.** Fix an initial state (s) and a chosen root pair ((w^s,b^s)\in\mathcal C(s)). Let (H_t^s) be the finite set of rooted public histories of length (t) whose first state is (s).

We construct by induction on (t) a pair assignment
[
h\mapsto (w(h),b(h))\in\mathcal C(h)
]
for all (h\in H_t^s), together with local product mixed actions (x(h)\in\prod_j\Delta(A_j(s(h)))).

Base step (t=1): the only history is the root (s), and we set
[
(w(s),b(s))=(w^s,b^s).
]

Induction step: assume the assignment is already defined for all histories in (H_t^s). Fix (h\in H_t^s). Since ((w(h),b(h))\in\mathcal C(h)), L4 gives one element of (\mathcal F(h,w(h),b(h))). Write that chosen element as
[
\Bigl(x(h),\bigl((w(h[a,s']),b(h[a,s']))\bigr)*{a,s'}\Bigr).
]
This defines a product mixed action at (h) and defines successor pairs for every one-step successor (h[a,s']\in H*{t+1}^s). A rooted history has a unique predecessor, so there is no ambiguity in the successor pair assigned to (h[a,s']).

Perform this construction for every (h\in H_t^s). Then all pairs on (H_{t+1}^s) are defined. By induction, the assignment exists on every rooted history.

Finally define the rooted behavioral profile (\sigma^s) by
[
\sigma_i^s(h):=x_i(h)\in\Delta(A_i(s(h)))\qquad(h\text{ rooted at }s).
]
This is a behavioral strategy because its value at (h) lies in the correct simplex. By construction, at every rooted history (h), the mixed action prescribed by (\sigma^s) together with the successor-pair assignment is an element of (\mathcal F(h,w(h),b(h))). That is exactly L5. ∎

[DERIVED] **Lemma L6.** Assuming the rooted objects of L5 for every initial state, the global assembly statement holds in its literal disjoint-union form.

**Proof.** Every public history (h=(s_1,a_1,s_2,\dots,s_t)) has a unique initial state (s_1). Therefore the full public-history tree is the disjoint union of the rooted trees ({H^s:s\in S}).

For each history (h), define
[
\sigma(h):=\sigma^{s_1}(h),\qquad (w(h),b(h)):=(w^{s_1}(h),b^{s_1}(h)),
]
where (s_1) is the initial state appearing in (h). This is well defined because (h) belongs to exactly one rooted tree.

Since each (\sigma^{s_1}) is behavioral on its rooted tree, (\sigma) is behavioral on the whole history space. Since local feasibility at a history (h) was already verified inside the rooted tree indexed by its initial state (s_1), the same local feasibility property holds for the assembled global objects. Thus L6 is proved.

This proves only the literal assembly lemma. It does **not** produce any nonvacuous punishment-mode mechanism. That stronger reading should not be claimed downstream.  

## 4. What the current local data actually telescope to

[DERIVED] **Weak telescope under the current L5-L6 data.** Assume L2, L5, and L6 as currently written. Fix an initial state (s), player (i), a horizon (T), and a unilateral deviation (\tau_i). Let (H_t) denote the random public history at stage (t).

Then
[
\gamma_i^T(G,s,\sigma)\ge
\frac1T\sum_{t=1}^T \mathbb E_{G,s,\sigma}[,w_i(H_t),]
-\frac{2C}{T}
-\frac1T\sum_{t=1}^T\eta_t,
\tag{WT-ob}
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))\le
\frac1T\sum_{t=1}^T \mathbb E_{G,s,(\tau_i,\sigma_{-i})}[,w_i(H_t),]
+\frac{2C}{T}
+\frac1T\sum_{t=1}^T\eta_t.
\tag{WT-dev}
]

**Proof.** Under obedient play, condition on (H_t=h). Because the action at (h) is distributed according to the product mixed action (x(h)) chosen in L5, and the next state follows (P(\cdot\mid s(h),a)),
[
\mathbb E!\left[u_i(s_t,a_t)+b_i(H_{t+1})-b_i(H_t)\mid H_t=h\right]
===================================================================

\sum_a x(h)(a)\Bigl(u_i(s(h),a)+\sum_{s'}P(s'|s(h),a)b_i(h[a,s'])\Bigr)-b_i(h).
]
By (Bal), this is at least (w_i(h)-\eta_{|h|}). Since (|H_t|=t), we obtain
[
\mathbb E!\left[u_i(s_t,a_t)+b_i(H_{t+1})-b_i(H_t)\mid H_t\right]
\ge w_i(H_t)-\eta_t.
]
Take expectations and sum from (t=1) to (T):
[
\mathbb E\sum_{t=1}^T u_i(s_t,a_t)
+
\mathbb E[b_i(H_{T+1})]-b_i(s)
\ge
\sum_{t=1}^T \mathbb E[w_i(H_t)]-\sum_{t=1}^T \eta_t.
]
Divide by (T). Because every admissible bias lies in ([-C,C]), both (|b_i(s)|\le C) and (|\mathbb E[b_i(H_{T+1})]|\le C). Hence
[
\gamma_i^T(G,s,\sigma)\ge
\frac1T\sum_{t=1}^T \mathbb E[w_i(H_t)]-\frac{2C}{T}-\frac1T\sum_{t=1}^T\eta_t.
]
This is (WT-ob).

Now consider deviating play ((\tau_i,\sigma_{-i})). Condition again on (H_t=h). Let (q_h:=\tau_i(h)\in \Delta(A_i(s(h)))). Then
[
\mathbb E!\left[u_i(s_t,a_t)+b_i(H_{t+1})-b_i(H_t)\mid H_t=h\right]
]
equals
[
\sum_{a_i'} q_h(a_i')
\sum_{a_{-i}}x_{-i}(h)(a_{-i})
\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i})),b_i(h[(a_i',a_{-i}),s'])\Bigr)-b_i(h).
]
For each pure (a_i'), the inner term is at most (w_i(h)+\eta_t) by (Dev). Averaging over (q_h) preserves that upper bound. Therefore
[
\mathbb E!\left[u_i(s_t,a_t)+b_i(H_{t+1})-b_i(H_t)\mid H_t\right]
\le w_i(H_t)+\eta_t.
]
Summing and dividing by (T), with the same (2C/T) bias bound, gives (WT-dev). ∎

[BREAKDOWN_AMEND] The weak telescope is the exact output of the current L3-L6 data. It does **not** imply the displayed L7' in the packet, because the right-hand sides contain the visited promise process (w_i(H_t)), not the root promise (w_i^s). Also, the expectation in (WT-ob) is taken under obedient play and the expectation in (WT-dev) under deviating play, so the promise averages do not cancel. The current local relation uses successor **biases** but never successor **promises**, so no fixed-promise invariant is propagated. Therefore the current L7' requires a genuine amendment upstream, at L3-L4, exactly where the route memo says amendments should be made first.  

## 5. Corrected fixed-promise fiber version

[BREAKDOWN_AMEND] For each history (h) and promise vector (w\in[0,1]^N), define the bias fiber
[
B(h,w):={,b\in[-C,C]^N : (w,b)\in\mathcal C(h),}.
]

Replace current L3-L5 by the following fixed-promise versions.

**L3*.** Fix (h) and ((w,b)\in\mathcal C(h)). Let (\mathcal F^\ast(h,w,b)) be the set of all data consisting of

1. a product mixed action (x=\prod_j x_j\in \prod_j \Delta(A_j(s(h)))), and
2. for every one-step successor (h[a,s']), a successor bias (b^{a,s'}\in B(h[a,s'],w)),

such that for every player (i),
[
\sum_a x(a)\Bigl(u_i(s(h),a)+\sum_{s'}P(s'|s(h),a)b_i^{a,s'}\Bigr)-b_i\ge w_i-\eta_{|h|},
]
and for every pure unilateral deviation (a_i'\in A_i(s(h))),
[
\sum_{a_{-i}}x_{-i}(a_{-i})\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i}))b_i^{(a_i',a_{-i}),s'}\Bigr)-b_i
\le w_i+\eta_{|h|}.
]

**L4*.** For every (h) and every ((w,b)\in\mathcal C(h)), one has (\mathcal F^\ast(h,w,b)\neq\varnothing).

**L5*.** Assume L4*. For every initial state (s) and every chosen root pair ((w^s,b^s)\in\mathcal C(s)), there exist

1. a rooted behavioral profile (\sigma^s), and
2. a rooted bias assignment (h\mapsto \beta^s(h)\in[-C,C]^N),

such that (\beta^s(s)=b^s), ((w^s,\beta^s(h))\in \mathcal C(h)) for every rooted history (h), and at every rooted history (h) the prescribed mixed action together with the successor biases belongs to (\mathcal F^\ast(h,w^s,\beta^s(h))).

[DERIVED] **L3* is compact.**

**Proof.** Fix (h) and ((w,b)\in\mathcal C(h)). For each successor (g=h[a,s']), the fiber
[
B(g,w)={b' : (w,b')\in \mathcal C(g)}
]
is compact, because (\mathcal C(g)) is compact by L2 and (B(g,w)) is its section at the fixed first coordinate (w). Thus the ambient space
[
\Bigl(\prod_j \Delta(A_j(s(h)))\Bigr)\times \prod_{g\in\mathrm{Succ}(h)} B(g,w)
]
is compact. The defining inequalities are continuous in the same way as in L3. Therefore (\mathcal F^\ast(h,w,b)) is a closed subset of a compact set, hence compact. ∎

[DERIVED] **L5* follows by the same depth recursion as L5.**

**Proof.** Fix (s) and ((w^s,b^s)\in\mathcal C(s)). At the root set (\beta^s(s)=b^s). If (\beta^s(h)) is defined and ((w^s,\beta^s(h))\in\mathcal C(h)), then L4* gives one element of (\mathcal F^\ast(h,w^s,\beta^s(h))), consisting of a product mixed action (x(h)) and successor biases (\beta^s(h[a,s'])\in B(h[a,s'],w^s)). Because a rooted successor has a unique predecessor, the assignment is unambiguous. Induction on depth defines (\beta^s) and (x(h)) on the whole rooted tree. Set (\sigma_i^s(h):=x_i(h)). Then ((w^s,\beta^s(h))\in\mathcal C(h)) at every rooted history, and the local fixed-promise feasibility condition holds by construction. ∎

[DERIVED] **The literal assembly lemma L6 also works for the corrected L5*.**

**Proof.** If (h) starts at state (s_1), define
[
\sigma(h):=\sigma^{s_1}(h),\qquad w(h):=w^{s_1},\qquad b(h):=\beta^{s_1}(h).
]
The rooted trees are disjoint, so this is well defined. Since any play beginning at initial state (s) remains inside the rooted tree (H^s), the global profile restricts to the rooted one relevant for that initial state. ∎

## 6. Corrected L7'

[DERIVED] **Corrected L7'.** Assume L2, corrected L5*, and the literal assembly lemma L6. Then for every initial state (s), every player (i), every unilateral deviation (\tau_i), and every horizon (T),
[
\gamma_i^T(G,s,\sigma)\ge w_i^s-\frac{2C}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))\le w_i^s+\frac{2C}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Hence
[
\gamma_i^T(G,s,\sigma)\ge
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))
-\frac{4C}{T}
-\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]

**Proof.** Fix (s,i,T). Because the play starts from (s), both the obedient law and every unilateral-deviation law stay inside the rooted tree (H^s). Hence along either law the promise coordinate is the fixed vector (w^s), while the bias at history (h) is (\beta^s(h)).

Let (H_t) be the stage-(t) public history and abbreviate
[
B_t:=\beta_i^s(H_t).
]

### Obedient play

Condition on (H_t=h). By the same computation used in the weak telescope, but now with the corrected local data,
[
\mathbb E_{G,s,\sigma}!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t=h\right]
======================================================================

\sum_a x(h)(a)\Bigl(u_i(s(h),a)+\sum_{s'}P(s'|s(h),a)\beta_i^s(h[a,s'])\Bigr)-\beta_i^s(h).
]
Because ((x(h),(\beta^s(h[a,s']))*{a,s'})\in \mathcal F^\ast(h,w^s,\beta^s(h))), the (Bal) inequality gives
[
\mathbb E*{G,s,\sigma}!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]\ge w_i^s-\eta_t.
]
Take expectations, sum from (t=1) to (T), and telescope:
[
\mathbb E_{G,s,\sigma}\sum_{t=1}^T u_i(s_t,a_t)
\ge
T w_i^s-\sum_{t=1}^T\eta_t-\mathbb E[B_{T+1}]+B_1.
]
Since every admissible bias lies in ([-C,C]), we have (|B_1|\le C) and (|\mathbb E[B_{T+1}]|\le C). Divide by (T):
[
\gamma_i^T(G,s,\sigma)\ge w_i^s-\frac{2C}{T}-\frac1T\sum_{t=1}^T\eta_t.
]

### Deviating play

Now condition on (H_t=h) under the law ((\tau_i,\sigma_{-i})). Let (q_h:=\tau_i(h)). Then
[
\mathbb E_{G,s,(\tau_i,\sigma_{-i})}!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t=h\right]
]
equals
[
\sum_{a_i'} q_h(a_i')
\sum_{a_{-i}}x_{-i}(h)(a_{-i})
\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i})),\beta_i^s(h[(a_i',a_{-i}),s'])\Bigr)-\beta_i^s(h).
]
For each pure (a_i'), the inner term is at most (w_i^s+\eta_t) by (Dev), because the promise vector has been frozen at (w^s). Averaging over (q_h) preserves that upper bound. Therefore
[
\mathbb E_{G,s,(\tau_i,\sigma_{-i})}!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]\le w_i^s+\eta_t.
]
Again sum from (t=1) to (T), telescope, and use (|B_t|\le C):
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))\le
w_i^s+\frac{2C}{T}+\frac1T\sum_{t=1}^T\eta_t.
]

Subtracting the two displayed bounds gives the incentive inequality. ∎

## 7. L8'

[DERIVED] **Lemma L8'.** Assume (\eta_t\ge 0) for all (t) and (\sum_{t\ge1}\eta_t\le \varepsilon/4). Then there exists (T_0) such that for all (T\ge T_0),
[
\frac{4C}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t\le \varepsilon.
]
Consequently, the global profile (\sigma) from L6 is a uniform (\varepsilon)-equilibrium.

**Proof.** Set
[
M:=4C+2\sum_{t\ge1}\eta_t.
]
Because (\eta_t\ge0),
[
4C+;2\sum_{t=1}^T\eta_t\le 4C+2\sum_{t\ge1}\eta_t=M.
]
Hence
[
\frac{4C}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t\le \frac{M}{T}.
]
Choose (T_0\in\mathbb N) with (M/T_0\le \varepsilon), for instance (T_0=\lceil M/\varepsilon\rceil). Then for every (T\ge T_0),
[
\frac{4C}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t\le \varepsilon.
]

Now apply corrected L7'. For every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)\ge \gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]
This is exactly the uniform (\varepsilon)-equilibrium property in the adopted theorem-side formulation.  ∎

## 8. Conditional closure of the repaired route

[DERIVED] **Conditional theorem for the repaired post-L4 tail.** Suppose L2 is available as imported Martin-function input, and suppose the strengthened fixed-promise selector L4* holds. Then for every finite stochastic game (G) and every (\varepsilon>0), the repaired Route B yields one global public-history behavioral profile (\sigma) and one threshold (T_0) such that for every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)\ge \gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]

**Proof.** Choose a nonnegative summable leakage schedule with (\sum_t\eta_t\le \varepsilon/4). Use L2 for root pairs, L5* for rooted recursion, the literal L6 for global assembly, corrected L7' for the finite-horizon incentive bound, and L8' for bookkeeping. This yields exactly the one-profile, all-large-(T), every-initial-state quantifier pattern of the target theorem.  ∎

## Status summary

[DERIVED] **Proved in this pass.**

* L1.
* L3 as stated.
* L5 and the literal disjoint-union L6, conditional on L4 and L2.
* The weak telescope that the current L3-L6 data actually imply.
* The corrected fixed-promise compactness lemma L3*.
* The corrected fixed-promise recursion lemma L5*.
* The corrected telescoping lemma L7', conditional on L2 and the strengthened selector L4*.
* L8' from corrected L7'.

[BREAKDOWN_AMEND] **Required packet repair.**

* The current downstream tail cannot use the variable-promise formulation of L3-L5 if it wants the root-promise bound in L7'. The promise coordinate must be frozen along each rooted tree, or else the local inequalities must be changed so successor promises enter the telescope.
* Thus the real bottleneck is a strengthened fixed-promise selector L4*, not the looser current L4.
* L6 should be cited only as literal global assembly, not as a nonvacuous punishment-mode construction.

[DERIVED] **What remains open.**

* L2 is still imported, not proved here.
* L4* is still the theorem-sized unresolved selector step.
* Therefore the full theorem remains bootstrap/open. That is also the current durable project status, and the route memo still identifies the selector step as the central research bottleneck.
