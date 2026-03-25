# Prover Output

Generated: 2026-03-24T02:20:49.579519+00:00

[DERIVED] I keep the route explicitly **open/bootstrap**, and I preserve the exact theorem-side target: one behavioral profile (\sigma), one threshold (T_0), all sufficiently large horizons, every initial state, every player, and every unilateral deviation. That is the durable project status and the adopted formal claim.     

## Fixed-promise repair of the local invariant

[BREAKDOWN_AMEND] The downstream proof should use the **increment form** of the current breakdown’s local invariant and should stop citing the canceled-promise formulas from the superseded prover_07 setup. The current breakdown already has a fixed root promise (\rho^s) and a varying bias (b^s(h)):
[
\rho_i^s+b_i^s(h)
\le
\mathbb E!\left[u_i(s(h),a)+b_i^s(h,a,q)\right]+\eta_{|h|},
]
[
\rho_i^s+b_i^s(h)
\ge
\sup_{y_i}
\mathbb E!\left[u_i(s(h),(a_i,a_{-i}))+b_i^s(h,(a_i,a_{-i}),q)\right]-\eta_{|h|}.
]
Rearranging gives the exact fixed-promise local relations needed for telescoping:
[
\mathbb E!\left[u_i(s(h),a)+b_i^s(h,a,q)\right]-b_i^s(h)\ge \rho_i^s-\eta_{|h|},
\tag{Inc-E}
]
[
\sup_{y_i}
\mathbb E!\left[u_i(s(h),(a_i,a_{-i}))+b_i^s(h,(a_i,a_{-i}),q)\right]-b_i^s(h)\le \rho_i^s+\eta_{|h|}.
\tag{Inc-D}
]
This is algebraically equivalent to the displayed setup in the breakdown, and it is exactly the fixed-promise relation the reviewer patch set asks for.

[ASSUMPTION+] For the closed-graph clause in L3, equip (H^s=\bigsqcup_{t\ge 1}H_t^s) with the disjoint-union topology of its finite depth layers. Equivalently, (H^s) is a countable discrete space.

## L1

[ASSUMPTION+] (**ZU**) Every finite-state two-player zero-sum stochastic game with compact metric action sets and continuous payoff/transition data has a uniform value, and each player has uniformly (\delta)-optimal strategies.

[DERIVED] **L1**, conditional on [ASSUMPTION+] ZU.

Fix a public history (h) and a player (i). Let (q=s(h)) be the terminal state of (h). Define a two-player zero-sum continuation game (Z_{h,i}) as follows.

* The state space is (S), with initial state (q).
* Player Max is (i), with action set (A_i(s)) at state (s).
* Player Min is the coalition (N\setminus{i}), with action set
  [
  M_{-i}(s):=\prod_{j\ne i}\Delta(A_j(s)).
  ]
* The one-stage payoff to Max is
  [
  g_i(s,a_i,x_{-i})
  :=
  \sum_{a_{-i}}
  \Bigl(\prod_{j\ne i}x_j(a_j)\Bigr),
  u_i(s,(a_i,a_{-i})).
  ]
* The transition kernel is
  [
  Q(\cdot\mid s,a_i,x_{-i})
  :=
  \sum_{a_{-i}}
  \Bigl(\prod_{j\ne i}x_j(a_j)\Bigr),
  P(\cdot\mid s,(a_i,a_{-i})).
  ]

Justification of applicability of ZU: (S) is finite, each (A_i(s)) is finite, each (M_{-i}(s)) is a product of finite simplices and hence compact metric, and both (g_i) and (Q) are continuous and multilinear in the mixed actions.

By ZU, (Z_{h,i}) has a uniform value (m_i(h)\in[0,1]), and for every (\delta>0) player (i) has a strategy (\mu_i^{h,\delta}) in (Z_{h,i}) such that for all sufficiently large (T),
[
\inf_{\chi_{-i}}
\gamma_i^T(Z_{h,i},(\mu_i^{h,\delta},\chi_{-i}))
\ge m_i(h)-\delta.
]

Now let (\sigma_{-i}) be any opponent profile in the original continuation game (G_h). At each continuation history, (\sigma_{-i}) induces a coalition mixed action (x_{-i}\in M_{-i}(s)). Therefore the law of play in (G_h) under ((\mu_i^{h,\delta},\sigma_{-i})) is a special case of the law in (Z_{h,i}) under ((\mu_i^{h,\delta},\chi_{-i})). Hence the same lower bound holds:
[
\inf_{\sigma_{-i}}
\gamma_i^T(G_h,(\mu_i^{h,\delta},\sigma_{-i}))
\ge m_i(h)-\delta
]
for all sufficiently large (T). This is exactly L1.

## Gap on L2

L2 remains **imported/open** in this pass. I do not mark it as proved. I use only the properties explicitly stated in the breakdown: nonempty compact fibers (W^s(h)\subseteq[-B_s,B_s]^N), root nonemptiness, and the uniform bias bound. This is consistent with the route memo and the project proof-state, both of which keep the route conditional and bootstrap.

## L3

[DERIVED] **L3**.

Fix (s\in S), (h\in H^s), and (b\in W^s(h)). Let
[
X(h):=\prod_{i\in N}\Delta(A_i(s(h))).
]
Let (C(h)) be the finite set of one-step child histories (h'=(h,a,q)). Define the ambient product
[
K(h):=X(h)\times \prod_{h'\in C(h)} W^s(h').
]
By finiteness of actions and children, (X(h)) is a finite product of simplices, hence compact, and each (W^s(h')) is compact by L2. Therefore (K(h)) is compact.

For each player (i), define
[
\Phi_i(x,\beta)
:=
\mathbb E_{a\sim x,\ q\sim P(\cdot\mid s(h),a)}
\bigl[u_i(s(h),a)+\beta(h,a,q)_i\bigr].
]
This is continuous on (K(h)), because it is a finite multilinear expression in (x) and the child-bias coordinates.

Define also
[
\Psi_i(x,\beta)
:=
\sup_{y_i\in\Delta(A_i(s(h)))}
\mathbb E_{a_i\sim y_i,\ a_{-i}\sim x_{-i},\ q}
\bigl[u_i(s(h),(a_i,a_{-i}))+\beta(h,(a_i,a_{-i}),q)_i\bigr].
]
The inner expectation is affine in (y_i), so the supremum over the simplex equals the maximum over pure actions:
[
\Psi_i(x,\beta)
===============

\max_{a_i\in A_i(s(h))}
\mathbb E_{a_{-i}\sim x_{-i},\ q}
\bigl[u_i(s(h),(a_i,a_{-i}))+\beta(h,(a_i,a_{-i}),q)_i\bigr].
]
This is a finite maximum of continuous functions, hence continuous.

Therefore
[
\mathcal F^s(h,b)
=================

\Bigl{(x,\beta)\in K(h):
\rho_i^s+b_i\le \Phi_i(x,\beta)+\eta_{|h|},
\rho_i^s+b_i\ge \Psi_i(x,\beta)-\eta_{|h|}
\ \forall i
\Bigr}
]
is the intersection of finitely many closed subsets of the compact set (K(h)). Hence (\mathcal F^s(h,b)) is compact. The empty set case is harmless, since the empty set is compact.

For closed graph: let ((h_n,b_n,x_n,\beta_n)\to(h,b,x,\beta)) with ((x_n,\beta_n)\in\mathcal F^s(h_n,b_n)) for all (n). Since (H^s) is discrete, eventually (h_n=h). Since (b_n\to b) in the compact set (W^s(h)), continuity of (\Phi_i,\Psi_i) passes the defining inequalities to the limit, so ((x,\beta)\in\mathcal F^s(h,b)). Hence the graph is closed.

## L5

[BREAKDOWN_AMEND] The L5 proof does **not** need a Kőnig-style compactness limit once L4 is available on the full rooted tree. Direct recursion on depth is enough. Also, L5 must cite L2 for the root bias choice. This matches the accepted amendment and the stable route-memo takeaway.

[DERIVED] **L5**, conditional on L2 and L4.

Fix (s\in S). By L2 root nonemptiness, choose
[
b^s(s)\in W^s(s).
]
For each (n\ge 1), let (H_n^s) be the finite set of public histories of length (n) rooted at (s).

Inductively define (x^s(h)) and (b^s(h)) for all (h\in H_n^s).

* Base step (n=1): (b^s(s)) is already chosen.
* Induction step: assume (b^s(h)) is defined for every (h\in H_n^s). For each such (h), L4 gives a local package
  [
  \bigl(x_h,{c_{h'}}*{h'\text{ child of }h}\bigr)\in \mathcal F^s(h,b^s(h)).
  ]
  Set
  [
  x^s(h):=x_h,\qquad b^s(h'):=c*{h'}\ \text{for every child }h' \text{ of }h.
  ]

This is consistent because every child history (h') has a unique predecessor (h). Hence no two assignments conflict. By induction on (n), the functions
[
h\mapsto x^s(h),\qquad h\mapsto b^s(h)\in W^s(h)
]
are defined on all of (H^s), and for each (h) the chosen package lies in (\mathcal F^s(h,b^s(h))). This is exactly L5.

## L6

[BREAKDOWN_AMEND] Demote L6 to the **literal** statement that L5 defines a rooted behavioral profile. Do not cite L6 as a nonvacuous punishment-mode mechanism unless the public state is enlarged to remember punishment anchors. The route memo explicitly warns that the current stronger punishment reading is too weak / vacuous.

[DERIVED] **Literal L6.**

Given L5, define for each root (s) a behavioral profile (\widehat\sigma^s) on (H^s) by
[
\widehat\sigma_i^s(h):=x_i^s(h)\qquad(h\in H^s,\ i\in N).
]
Since (x^s(h)\in \prod_i\Delta(A_i(s(h)))), this is a well-defined public-history behavioral profile on the whole rooted tree (H^s).

No punishment-memory claim is used below.

## L7′

[BREAKDOWN_AMEND] Replace the current L7 by the following corrected lemma. Its proof uses only L2 and the full-tree L5 selector; L6 is not needed.

**Statement of L7′.** Assume L2 and L5. Then for every root (s), every player (i), every horizon (T\ge 1), and every unilateral deviation (\tau_i),
[
\mathbb E_{G,s,\widehat\sigma^s}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\ge
T\rho_i^s-2B_s-\sum_{t=1}^T\eta_t,
\tag{H_i^{T,\prime}}
]
and
[
\mathbb E_{G,s,(\tau_i,\widehat\sigma_{-i}^s)}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
T\rho_i^s+2B_s+\sum_{t=1}^T\eta_t.
\tag{D_i^{T,\prime}}
]

[DERIVED] **L7′**.

Fix (s,i,T). Under either honest play or unilateral deviation, let (H_t) be the random public history before the stage-(t) action, so (H_1=(s)), and let (H_{t+1}=(H_t,a_t,s_{t+1})). Because L5 is defined on the **full** tree (H^s), the bias (b^s(H_t)) is defined even on histories created by a deviation.

Write
[
B_t:=b_i^s(H_t).
]
By L2, (|B_t|\le B_s) almost surely for all (t).

### Honest play

At history (H_t), the action profile is drawn from (x^s(H_t)). Therefore ((E_{H_t}^i)), equivalently (Inc-E), gives
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}\mid H_t\right]-B_t
\ge \rho_i^s-\eta_t.
]
So
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]
\ge \rho_i^s-\eta_t.
]
Take expectations and sum from (t=1) to (T):
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
+
\mathbb E[B_{T+1}-B_1]
\ge
T\rho_i^s-\sum_{t=1}^T\eta_t.
]
Since (B_{T+1}-B_1\le 2B_s),
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\ge
T\rho_i^s-2B_s-\sum_{t=1}^T\eta_t.
]

### Unilateral deviation

Now fix a deviation (\tau_i). At history (H_t), the deviator uses the mixed action
[
y_t:=\tau_i(H_t)\in\Delta(A_i(s(H_t))).
]
The opponents still use (x^s_{-i}(H_t)). Therefore ((D_{H_t}^i)), equivalently (Inc-D), applied with (y_i=y_t), gives
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}\mid H_t\right]-B_t
\le \rho_i^s+\eta_t.
]
Hence
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]
\le \rho_i^s+\eta_t.
]
Taking expectations and summing,
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
+
\mathbb E[B_{T+1}-B_1]
\le
T\rho_i^s+\sum_{t=1}^T\eta_t.
]
Since (B_{T+1}-B_1\ge -2B_s),
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
T\rho_i^s+2B_s+\sum_{t=1}^T\eta_t.
]

This proves L7′.

## L8′

[BREAKDOWN_AMEND] Replace the current L8 by the corrected bookkeeping lemma below, with explicit use of (\eta_t\ge 0).

[DERIVED] **L8′**.

Assume L7′ and
[
\sum_{t\ge 1}\eta_t\le \frac{\varepsilon}{4},
\qquad
\eta_t\ge 0.
]
Divide the two inequalities of L7′ by (T):
[
\gamma_i^T(G,s,\widehat\sigma^s)
\ge
\rho_i^s-\frac{2B_s}{T}-\frac{1}{T}\sum_{t=1}^T\eta_t,
]
[
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))
\le
\rho_i^s+\frac{2B_s}{T}+\frac{1}{T}\sum_{t=1}^T\eta_t.
]
Subtracting,
[
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))
----------------------------------------------

\gamma_i^T(G,s,\widehat\sigma^s)
\le
\frac{4B_s}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Since the (\eta_t) are nonnegative,
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
\frac{2}{T}\sum_{t\ge 1}\eta_t
\le
\frac{\varepsilon}{2T}
\le
\frac{\varepsilon}{2}.
]
Thus any
[
T_0(s)\in\mathbb N_{>0}
\quad\text{with}\quad
\frac{4B_s}{T_0(s)}\le \frac{\varepsilon}{2}
]
works. For example,
[
T_0(s):=\max!\left(1,\left\lceil \frac{8B_s}{\varepsilon}\right\rceil\right).
]
Then for all (T\ge T_0(s)),
[
\gamma_i^T(G,s,\widehat\sigma^s)
\ge
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))-\varepsilon.
]
This is exactly the rooted uniform (\varepsilon)-equilibrium statement.

## L9′

[BREAKDOWN_AMEND] The present L9 asks for a stronger current-state re-rooting compatibility:
the continuation from a history ending at (q) should agree with the separately constructed rooted profile for (q). That is stronger than what independent rooted constructions provide. It is also **not needed** for the formal theorem target, which quantifies over initial states only. So replace L9 by the weaker and sufficient disjoint-union assembly below. This keeps theorem-side scope unchanged.

**Statement of L9′.** Assume L8′ for every initial state (s\in S). Define a whole-game behavioral profile (\sigma) by
[
\sigma(h):=\widehat\sigma^{s_1(h)}(h),
]
where (s_1(h)) is the first state of the public history (h). Then (\sigma\in\Sigma(G)), and for every initial state (s), every horizon (T\ge T_0(s)), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Because (S) is finite, one may set
[
T_0:=\max_{s\in S}T_0(s).
]

[DERIVED] **L9′**.

Every public history (h) has a unique first state (s_1(h)). Therefore the definition
[
\sigma(h):=\widehat\sigma^{s_1(h)}(h)
]
is well-defined on the full history space
[
H=\bigsqcup_{s\in S}H^s.
]
Since each (\widehat\sigma^{s}) is behavioral on (H^s), the assembled (\sigma) is behavioral on (H).

Now fix an initial state (s). Any play started from (s) only visits histories in (H^s). On that entire subset,
[
\sigma(h)=\widehat\sigma^s(h)
\qquad(h\in H^s).
]
Therefore the law of play under (\sigma) from initial state (s) is exactly the same as the law of play under (\widehat\sigma^s) from root (s). The same is true after replacing player (i)’s component by a deviation (\tau_i). Hence the rooted L8′ inequalities transfer verbatim from (\widehat\sigma^s) to (\sigma) at initial state (s). Taking (T_0=\max_s T_0(s)) is valid because (S) is finite.

## L10

[BREAKDOWN_AMEND] Replace the downstream backbone by
[
L1\to \text{imported }L2\to L3\to L4\to L5\to L7'\to L8'\to L9'\to L10,
]
with literal L6 optional and not used in the incentive proof. This is exactly the stable post-L4 route indicated by the route memo: recursion, telescoping, bookkeeping, and explicit global assembly, with L4 as the unresolved bottleneck.

[DERIVED] **Conditional L10.**

Assume L1, imported L2, and L4. Then L5 constructs, for each root state (s), a full-tree selector ((x^s,b^s)). Literal L6 turns (x^s) into a rooted behavioral profile (\widehat\sigma^s). L7′ and L8′ show that (\widehat\sigma^s) is a uniform (\varepsilon)-equilibrium from root (s). L9′ assembles the rooted family into a single whole-game behavioral profile (\sigma\in\Sigma(G)) and a common threshold
[
T_0=\max_{s\in S}T_0(s).
]
Therefore, for every (T\ge T_0), every initial state (s_1\in S), every player (i\in N), and every unilateral deviation (\tau_i\in\Sigma_i(G)),
[
\gamma_i^T(G,s_1,\sigma)
\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
This is exactly the formal theorem-side quantifier pattern.

Because L2 remains imported and L4 remains open, this is a **conditional theorem synthesis**, not a completed proof of the open problem. That is the correct project-level status.

## Status summary

[DERIVED] In this pass I have advanced the route as follows.

* **Proved conditionally from an explicit external zero-sum input:** L1.
* **Proved:** L3.
* **Proved conditionally on L2 and L4:** L5.
* **Proved in literal form only:** L6.
* **Proved and corrected:** L7′ and L8′.
* **Proved with a statement repair:** L9′, using disjoint-union whole-game assembly.
* **Proved conditionally:** L10.

Open gaps that remain explicit:

* **L2** is still imported/open and needs exact source-to-statement citation.
* **L4** is still the theorem-sized unresolved selector step.
* The stronger punishment-memory reading of **L6** is not proved.
* The stronger current-state re-rooting version of **L9** is not used.

So the coherent current proof object is:

[
\boxed{
L1\ (\text{conditional on ZU})\ \to\ \text{imported }L2\ \to\ L3\ \to\ \text{open }L4\ \to\ L5\ \to\ L7'\ \to\ L8'\ \to\ L9'\ \to\ L10
}
]

This preserves the exact theorem-side scope while honestly localizing the remaining obstruction at L2/L4, exactly as the durable proof-state and route memo require.
