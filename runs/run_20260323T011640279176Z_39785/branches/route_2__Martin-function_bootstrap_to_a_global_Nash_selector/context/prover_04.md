# Prover Output

Generated: 2026-03-23T18:06:44.304832+00:00

The theorem remains bootstrap/open, and the exact target stays the one-profile strategy-existence statement for every sufficiently large horizon and every initial state. I therefore prove only the post-L4 tail and record the remaining gap explicitly.    

[BREAKDOWN_AMEND] Use the corrected post-L4 backbone
[
L1 \to L2 \to L3 \to L4 \to \text{strengthened }L5 \to {L6,L7'}\to L8',
]
with the following repairs.

First, strengthen L5 so that it quantifies over the full public-history tree (H), not merely histories reachable under compliance. This is necessary because deviation paths in L7′ may visit arbitrary public histories.

Second, replace the old L7 citation pattern by a direct telescoping lemma (L7') whose proof uses the second inequality in the definition of (F(h,w)) pointwise at every visited history. This proof does not use L6.

Third, replace L8 by (L8'), identical in substance but explicitly citing the standing hypothesis (\eta_t\ge 0).

Fourth, sharpen L3 slightly: (F(h,w)) is compact even when empty, because the empty set is compact.

[DERIVED] **Sublemma A.** For each depth (t\ge 1), the layer (H_t) of public histories of length (t) is finite. Hence (H=\bigcup_{t\ge1}H_t) is countable.

**Proof.** For (t=1), (H_1=S), which is finite by the standing game data. Assume (H_t) finite. For each (h\in H_t), the terminal state (s(h)) has finitely many action profiles (A(s(h))=\prod_j A_j(s(h))), because (N) is finite and each (A_j(s(h))) is finite. For each (a\in A(s(h))), the next-state set ({s'\in S:P(s'|s(h),a)>0}) is finite because (S) is finite. Therefore (\operatorname{Succ}(h)) is finite. Since
[
H_{t+1}=\bigcup_{h\in H_t}\operatorname{Succ}(h),
]
(H_{t+1}) is a finite union of finite sets, hence finite. By induction, every (H_t) is finite. Therefore (H) is a countable union of finite sets, hence countable. (\square)

[DERIVED] **L3, sharpened.** For every public history (h) and every (w\in W(h)), the set (F(h,w)) is compact, possibly empty. Its graph is closed on each depth layer.

**Proof.** Fix (h) and (w\in W(h)). Write
[
X(h):=\prod_{j\in N}\Delta(A_j(s(h))),
\qquad
Y(h):=\prod_{h'\in\operatorname{Succ}(h)} W(h').
]
By finiteness of every action set, each simplex (\Delta(A_j(s(h)))) is compact in a finite-dimensional Euclidean space. Hence (X(h)) is compact as a finite product of compact sets. By L1, each (W(h')) is compact. Since (\operatorname{Succ}(h)) is finite, (Y(h)) is compact. Therefore
[
D(h):=X(h)\times Y(h)
]
is compact.

For fixed (h), the map
[
(x,\phi)\longmapsto \mathcal T_i(h;x,\phi)
]
is continuous for each player (i): it is a finite sum of terms of the form
[
x(a),P(s'|s(h),a),\bigl(u_i(s(h),a)+\phi_i(h,a,s')\bigr),
]
where (x(a)=\prod_j x_j(a_j)) is a polynomial in the mixed-action coordinates, hence continuous, and (\phi_i(h,a,s')) enters linearly. Likewise, for each pure deviation (a_i'),
[
(x_{-i},\phi)\longmapsto \mathcal T_i(h;a_i',x_{-i},\phi)
]
is continuous by the same direct computation.

Now (F(h,w)\subset D(h)) is defined by the finitely many weak inequalities
[
w_i-\mathcal T_i(h;x,\phi)-\eta(h)\le 0
]
for all (i), and
[
\mathcal T_i(h;a_i',x_{-i},\phi)-w_i-\eta(h)\le 0
]
for all (i) and all (a_i'\in A_i(s(h))). Each inequality cuts out a closed subset of (D(h)) because the defining function is continuous. Hence (F(h,w)) is a closed subset of the compact set (D(h)), so (F(h,w)) is compact. This remains true if (F(h,w)=\varnothing), since the empty set is compact.

For the graph statement, fix a depth (t). By Sublemma A, (H_t) is finite. For each fixed (h\in H_t), the graph
[
\operatorname{Gr}(F_h):=
{(w,x,\phi)\in W(h)\times D(h):(x,\phi)\in F(h,w)}
]
is closed, because (W(h)\times D(h)) is compact and the defining inequalities are continuous in ((w,x,\phi)). The full graph on depth (t) is the finite union over (h\in H_t) of these closed pieces, so it is closed in the natural finite disjoint-union topology on that layer. (\square)

[DERIVED] **L5, strengthened full-tree form, conditional on L4.** Assume L4. Choose one root promise (w(s)\in W(s)) for each root (s\in S), which is possible by L2. Then there exists a single family
[
{(x(h),w(h)):h\in H}
]
such that (w(h)\in W(h)) for every history (h), and for every (h) there exists a successor assignment (\phi_h) with
[
(x(h),\phi_h)\in F(h,w(h)),
\qquad
w(h')=\phi_h(h')\ \text{ for every }h'\in\operatorname{Succ}(h).
]
Consequently, defining each player’s behavioral strategy by the coordinates of (x(h)) produces one whole-game behavioral profile (\sigma) on all of (H).

**Proof.** By Sublemma A, (H) is countable. Choose an enumeration
[
H={h^1,h^2,h^3,\dots}
]
such that
[
|h^m|\le |h^n| \quad\text{whenever } m<n.
]
Thus every predecessor of a history appears earlier in the enumeration.

We recursively define (w(h)), (x(h)), and (\phi_h).

At depth (1), i.e. for roots (h=s\in S), (w(s)\in W(s)) is already chosen.

Now suppose inductively that for all histories appearing before (h^m), the corresponding objects have been chosen. Let (h=h^m).

If (h) is a root, (w(h)) is already fixed.

If (h) is non-root, then (h) has a unique immediate predecessor (\bar h): if
[
h=(s_1,a_1,\dots,s_{t-1},a_{t-1},s_t),
]
then
[
\bar h=(s_1,a_1,\dots,s_{t-1}),
]
and (h=(\bar h,a_{t-1},s_t)\in \operatorname{Succ}(\bar h)). Because (|\bar h|<|h|), the predecessor (\bar h) appears earlier in the enumeration. When (\bar h) was processed, we chose (\phi_{\bar h}). Define
[
w(h):=\phi_{\bar h}(h).
]
This is well-defined because the predecessor is unique. Since ((x(\bar h),\phi_{\bar h})\in F(\bar h,w(\bar h))), the definition of (F) gives (\phi_{\bar h}(h)\in W(h)). Hence (w(h)\in W(h)).

Now (w(h)\in W(h)). By L4, (F(h,w(h))\neq\varnothing). Choose one witness
[
(x(h),\phi_h)\in F(h,w(h)).
]
For every successor (h'\in\operatorname{Succ}(h)), define
[
w(h'):=\phi_h(h').
]
Again this is consistent because every non-root history has a unique predecessor, so each history receives its promise exactly once, namely when its predecessor is processed.

This finishes the recursion over all (h\in H).

Finally, because (x(h)\in \prod_j \Delta(A_j(s(h)))), write (x(h)=(x_1(h),\dots,x_n(h))) and define
[
\sigma_i(h):=x_i(h)\in \Delta(A_i(s(h))).
]
Then (\sigma=(\sigma_i)_{i\in N}) is a behavioral public-history profile on the full tree (H). (\square)

[DERIVED] **Explicit global assembly corollary.** If one first runs the same construction separately on each rooted subtree with initial state (s), obtaining rooted profiles (\sigma^s), then one global whole-game profile is
[
\sigma(h):=\sigma^{\operatorname{root}(h)}(h),
]
where (\operatorname{root}(h)) is the first state in the history (h). This is well-defined because every history has a unique root. So the reviewer-requested statewise-to-global glue step is entirely explicit.

[DERIVED] **L6.** Let (\sigma) be the profile from strengthened L5. Then for every initial state (s), player (i), and horizon (T\ge1),
[
w_i(s)\le
\mathbb E_{s,\sigma}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t) + w_i(h_{T+1})
\right]
+\sum_{t=1}^{T}\eta_t.
]

**Proof.** Fix (s,i,T). For (t\ge1), define
[
U_t:=u_i(s_t,a_t),\qquad W_t:=w_i(h_t).
]
By L1, (|W_t|\le B) almost surely. By the base model, (0\le U_t\le 1). Hence all expectations below are finite.

Fix (t\in{1,\dots,T}). Under (\sigma), conditional on the public history (h_t), the current action profile is distributed according to (x(h_t)), and then the next state is distributed according to (P(\cdot\mid s(h_t),a)). Also, by the L5 construction,
[
w(h_{t+1})=\phi_{h_t}(h_{t+1}).
]
Therefore, by direct comparison with the definition of (\mathcal T_i),
[
\mathbb E_{s,\sigma}[U_t+W_{t+1}\mid h_t]
=========================================

\mathcal T_i(h_t;x(h_t),\phi_{h_t}).
]
Since ((x(h_t),\phi_{h_t})\in F(h_t,w(h_t))), the first defining inequality of (F) gives
[
W_t
\le
\mathbb E_{s,\sigma}[U_t+W_{t+1}\mid h_t]+\eta(h_t)
===================================================

\mathbb E_{s,\sigma}[U_t+W_{t+1}\mid h_t]+\eta_t.
]
Taking expectations yields
[
\mathbb E_{s,\sigma}[W_t]
\le
\mathbb E_{s,\sigma}[U_t+W_{t+1}]+\eta_t.
]
Summing over (t=1,\dots,T),
[
\sum_{t=1}^T \mathbb E[W_t]
\le
\sum_{t=1}^T \mathbb E[U_t]
+
\sum_{t=1}^T \mathbb E[W_{t+1}]
+
\sum_{t=1}^T \eta_t.
]
The terms (\mathbb E[W_2],\dots,\mathbb E[W_T]) cancel, leaving
[
\mathbb E[W_1]
\le
\mathbb E!\left[\sum_{t=1}^T U_t + W_{T+1}\right]
+
\sum_{t=1}^T \eta_t.
]
Because (h_1=s) is deterministic, (W_1=w_i(s)). This is the claimed inequality. (\square)

[BREAKDOWN_AMEND] The proof above establishes only the literal displayed statement of L6. It does **not** build a non-vacuous punishment-mode mechanism. Any stronger “switch to a punishment plan anchored at a remembered history” reading remains unproved unless the public state is enriched to remember that anchor.

[BREAKDOWN_AMEND] Replace the old L7 by the following corrected version.

**L7′.** Assume L1, L2, and strengthened L5. Let (\sigma) be the global profile from L5. Then for every initial state (s), player (i), unilateral deviation strategy (\tau_i), and horizon (T\ge1),
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t) + w_i(h_{T+1})
\right]
\le
w_i(s)+\sum_{t=1}^{T}\eta_t.
]

**Proof.** Fix (s,i,\tau_i,T). Again write
[
U_t:=u_i(s_t,a_t),\qquad W_t:=w_i(h_t).
]
As above, these random variables are integrable because (0\le U_t\le 1) and (|W_t|\le B).

The key point is that strengthened L5 provides (x(h)) and (w(h)) on the **full** tree (H), so every history that may be visited under the deviating law ((\tau_i,\sigma_{-i})) is covered.

Fix (t\in{1,\dots,T}), and condition on the currently visited public history (h_t). Let
[
\mu_t(\cdot):=\tau_i(h_t)\in \Delta(A_i(s(h_t)))
]
be the deviator’s mixed action at (h_t). For each pure action (a_i'\in A_i(s(h_t))), because ((x(h_t),\phi_{h_t})\in F(h_t,w(h_t))), the second defining inequality of (F) gives
[
\mathcal T_i(h_t;a_i',x_{-i}(h_t),\phi_{h_t})
\le
w_i(h_t)+\eta(h_t)
==================

W_t+\eta_t.
]
Multiply by (\mu_t(a_i')) and sum over (a_i'). By direct computation, the left-hand side becomes the conditional expectation of (U_t+W_{t+1}) under the law ((\tau_i,\sigma_{-i})): indeed, linearity of finite sums gives
[
\sum_{a_i'}\mu_t(a_i')\mathcal T_i(h_t;a_i',x_{-i}(h_t),\phi_{h_t})
===================================================================

\mathbb E_{s,(\tau_i,\sigma_{-i})}[U_t+W_{t+1}\mid h_t].
]
Hence
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}[U_t+W_{t+1}\mid h_t]
\le
W_t+\eta_t.
]
Taking expectations gives
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}[U_t+W_{t+1}]
\le
\mathbb E_{s,(\tau_i,\sigma_{-i})}[W_t]+\eta_t.
]
Summing over (t=1,\dots,T),
[
\mathbb E!\left[\sum_{t=1}^T U_t\right]
+
\sum_{t=1}^T \mathbb E[W_{t+1}]
\le
\sum_{t=1}^T \mathbb E[W_t]+\sum_{t=1}^T\eta_t.
]
Telescoping cancels (\mathbb E[W_2],\dots,\mathbb E[W_T]), so
[
\mathbb E!\left[\sum_{t=1}^T U_t + W_{T+1}\right]
\le
\mathbb E[W_1]+\sum_{t=1}^T\eta_t.
]
Since (h_1=s), (W_1=w_i(s)). This proves L7′. (\square)

[BREAKDOWN_AMEND] Replace L8 by the following corrected version, which explicitly cites the standing hypothesis (\eta_t\ge0).

[DERIVED] **L8′.** Under L1, L6, and L7′, for every initial state (s), player (i), deviation (\tau_i), and horizon (T\ge1),
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2B}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]
Consequently, if
[
M:=\sum_{t=1}^\infty \eta_t<\infty,
]
then
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le \frac{2(B+M)}{T},
]
and therefore any integer
[
T_0\ge \left\lceil \frac{2(B+M)}{\varepsilon}\right\rceil
]
suffices to ensure
[
\gamma_i^T(s,\sigma)\ge \gamma_i^T(s,(\tau_i,\sigma_{-i}))-\varepsilon
\qquad\forall T\ge T_0.
]

**Proof.** L7′ gives
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[\sum_{t=1}^T u_i(s_t,a_t)+w_i(h_{T+1})\right]
\le
w_i(s)+\sum_{t=1}^T\eta_t.
]
L6 gives
[
w_i(s)\le
\mathbb E_{s,\sigma}!\left[\sum_{t=1}^T u_i(s_t,a_t)+w_i(h_{T+1})\right]
+\sum_{t=1}^T\eta_t.
]
Subtract the second inequality from the first:
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
-------------------------------------------------------------------------

\mathbb E_{s,\sigma}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
\mathbb E_{s,\sigma}[w_i(h_{T+1})]
----------------------------------

\mathbb E_{s,(\tau_i,\sigma_{-i})}[w_i(h_{T+1})]
+
2\sum_{t=1}^T\eta_t.
]
By L1, (|w_i(h)|\le B) for every history (h). Hence
[
\mathbb E_{s,\sigma}[w_i(h_{T+1})]
----------------------------------

\mathbb E_{s,(\tau_i,\sigma_{-i})}[w_i(h_{T+1})]
\le 2B.
]
Therefore
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
-------------------------------------------------------------------------

\mathbb E_{s,\sigma}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
2B+2\sum_{t=1}^T\eta_t.
]
Divide by (T), and use the definition of (\gamma_i^T):
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2B}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]
Now use the standing hypothesis (\eta_t\ge0). Then each partial sum satisfies
[
0\le \sum_{t=1}^T\eta_t\le M:=\sum_{t=1}^\infty\eta_t,
]
so
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le \frac{2(B+M)}{T}.
]
Choosing any integer (T_0\ge \lceil 2(B+M)/\varepsilon\rceil) gives the desired (\varepsilon)-bound for all (T\ge T_0). (\square)

[DERIVED] **Conditional close of the route.** Assume L1, L2, and L4. Fix (G) and (\varepsilon>0), and choose any summable nonnegative leakage schedule ((\eta_t)). By L2 choose root promises (w(s)\in W(s)). By strengthened L5, construct one global public-history behavioral profile (\sigma) on all of (H). By L6 and L7′ compare equilibrium and deviating path values with terminal promise corrections. By L8′ choose (T_0) so that for every (T\ge T_0),
[
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G):
\quad
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Thus the route closes **conditionally on L4**.

[BREAKDOWN_AMEND] The remaining gap is now cleanly localized. L1 and L2 remain imported. L4 remains the unresolved selector theorem. Everything after L4 is tree recursion plus telescoping bookkeeping.

### Status summary

* [DERIVED] Sublemma A: every finite depth layer of (H) is finite; hence (H) is countable.
* [DERIVED] L3 proved, in a sharpened form: (F(h,w)) is compact even when empty, and its graph is closed on each depth layer.
* [DERIVED] L5 proved conditionally on L4, with the required full-tree repair and explicit whole-game assembly.
* [DERIVED] L6 proved in its literal displayed form.
* [DERIVED] L7′ proved conditionally on L1, L2, and strengthened L5.
* [DERIVED] L8′ proved conditionally on L1, L6, and L7′, explicitly using the standing nonnegativity of (\eta_t).
* [BREAKDOWN_AMEND] Old L7 should not be cited as proved with its original dependency list.
* [BREAKDOWN_AMEND] Any stronger punishment-mode reading of L6 remains unproved without enlarging the public state to remember the punishment anchor history.
* **Gap:** L4 is still unresolved, and therefore the full theorem remains bootstrap/open rather than solved.
