# Final Proof Report: Martin-Function Bootstrap to a Global Nash Selector

## Formal statement

Fix a finite stochastic game
[
G=(N,S,(A_i)_{i\in N},u,P)
]
with perfect public monitoring, finite action sets, behavioral public-history strategies, and finite-horizon average payoff
[
\gamma_i^T(G,s_1,\sigma)
========================

\mathbb E_{G,s_1,\sigma}!\left[\frac1T\sum_{t=1}^T u_i(s_t,a_t)\right].
]

The target theorem is the exact one-profile strategy-existence statement:
[
\forall G\ \forall \varepsilon>0\ \exists \sigma\in\Sigma(G)\ \exists T_0\in\mathbb N_{>0}\ \forall T\ge T_0
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G):
\quad
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Equivalently, every finite stochastic game should admit a uniform (\varepsilon)-equilibrium for every (\varepsilon>0), with one fixed public-history behavioral profile working for all sufficiently large horizons and all initial states. This remains the adopted theorem-side target, and the durable proof state still classifies the project as bootstrap rather than solved.   

## Strategy used

The selected route is the Martin-function bootstrap to a global Nash selector. The idea is to work directly on the public-history tree rather than through discounted asymptotics. One tries to construct, at every public history (h), a safe continuation promise (w(h)), a product mixed action (x(h)), and successor promises for all one-step continuations, such that current promises are approximately delivered under compliance and no unilateral one-shot deviation can improve by more than a small leakage term (\eta(h)). If such a local uncorrelated selector exists at every node, the rest is explicit recursion on the history tree plus telescoping estimates. The packet and durable memo agree that the selector step is the theorem-sized bottleneck.  

## Core definitions

Let (H) be the public-history tree, with root layer identified with (S), and let (s(h)) be the terminal state of a history (h). Fix a nonnegative summable leakage schedule ((\eta_t)*{t\ge 1}) and write (\eta(h):=\eta*{|h|}).

For a history (h), define its successor set
[
\operatorname{Succ}(h)
:=
{(h,a,s') : a\in A(s(h)),\ s'\in S,\ P(s' \mid s(h),a)>0}.
]

Given a product mixed action (x\in \prod_j \Delta(A_j(s(h)))) and a successor assignment (\phi:\operatorname{Succ}(h)\to\mathbb R^N), define
[
\mathcal T_i(h;x,\phi)
======================

\sum_{a,s'} x(a)P(s'\mid s(h),a)\bigl(u_i(s(h),a)+\phi_i(h,a,s')\bigr),
]
and for a pure unilateral deviation (a_i'\in A_i(s(h))),
[
\mathcal T_i(h;a_i',x_{-i},\phi)
================================

\sum_{a_{-i},s'} x_{-i}(a_{-i})P(s'\mid s(h),(a_i',a_{-i}))
\bigl(u_i(s(h),(a_i',a_{-i}))+\phi_i(h,(a_i',a_{-i}),s')\bigr).
]

The route is built around a bounded safe-promise correspondence (W(h)\subset[-B,B]^N) and the local feasibility correspondence
[
F(h,w)
]
consisting of all pairs ((x,\phi)) such that (x) is a product mixed action at (h), every successor promise (\phi(h')) lies in (W(h')), and for each player (i),
[
w_i \le \mathcal T_i(h;x,\phi)+\eta(h),
]
[
\mathcal T_i(h;a_i',x_{-i},\phi)\le w_i+\eta(h)
\qquad
\forall a_i'\in A_i(s(h)).
]

I normalize the report in the (W(h)), (w(h)), (F(h,w)) language. Earlier packet fragments written in (B_\delta), (v^s), (\beta) notation are treated as superseded intermediate phrasing.

## Corrected canonical backbone

The coherent repaired spine is
[
L1 \to L2 \to L3 \to L4 \to \widetilde L5 \to {L6,L7'}\to L8' \to \text{Theorem},
]
where:

* (L1) and (L2) are imported continuation inputs.
* (\widetilde L5) is the strengthened full-tree version of L5, already including the explicit whole-game assembly step.
* (L7') replaces the old L7 as the main deviation lemma.
* (L8') replaces the old L8 as the closing bookkeeping step.
* (L6) is retained only in its literal displayed form; it is **not** taken as a proved nonvacuous punishment-mode construction.

This is the version consistent with the repaired tail in `prover_04` and the reviewer diagnoses. 

## Ordered lemma record and proofs

### L1. Safe promise correspondence

**Statement.** There exists (B<\infty) and a correspondence (W) assigning to each public history (h) a compact set (W(h)\subset[-B,B]^N) of Martin-safe continuation promises, with closed graph on each depth layer.

**Status.** Imported, not proved in-packet.

**Role.** Supplies the bounded continuation object used everywhere else: compactness in L3, bounded terminal corrections in L8′, and the safe-promise domain for the selector theorem L4.

### L2. Historywise nonemptiness

**Statement.** For every public history (h), (W(h)\neq\varnothing).

**Status.** Imported, not proved in-packet.

**Role.** Starts the recursion at the roots and supports choosing one root promise (w(s)\in W(s)) for each initial state (s).

### L3. Compact local feasibility correspondence

**Statement.** For every public history (h) and every (w\in W(h)), the set (F(h,w)) is compact, possibly empty, and its graph is closed on each depth layer.

**Proof.** Fix (h) and (w\in W(h)). Let
[
X(h):=\prod_{j\in N}\Delta(A_j(s(h))),
\qquad
Y(h):=\prod_{h'\in\operatorname{Succ}(h)} W(h').
]
Each simplex (\Delta(A_j(s(h)))) is compact because the action set is finite, hence (X(h)) is compact. By L1, every (W(h')) is compact, and (\operatorname{Succ}(h)) is finite, so (Y(h)) is compact. Thus
[
D(h):=X(h)\times Y(h)
]
is compact.

The maps ((x,\phi)\mapsto \mathcal T_i(h;x,\phi)) and ((x_{-i},\phi)\mapsto \mathcal T_i(h;a_i',x_{-i},\phi)) are continuous because they are finite sums of polynomial expressions in mixed-action coordinates and linear expressions in successor-promise coordinates. Therefore the inequalities defining (F(h,w)) cut out closed subsets of (D(h)). So (F(h,w)) is a closed subset of a compact set, hence compact. This includes the empty case.

For the graph claim, each depth layer (H_t) is finite, so the depth-(t) graph is a finite union of closed graphs for fixed histories (h\in H_t). Hence it is closed on each depth layer. (\square)

### L4. One-step uncorrelated Nash selector

**Statement.** For every public history (h) and promise (w\in W(h)), the set (F(h,w)) is nonempty.

**Status.** Unresolved.

**Role.** This is the central missing theorem. It must produce, for every safe promise, an **uncorrelated** product mixed action and successor promises that jointly satisfy the compliance and deviation inequalities. The packet consistently identifies this as the place where the route could collapse back into the open problem itself.

### Sublemma A. Countability of the public-history tree

For each depth (t), the layer (H_t) is finite. Hence
[
H=\bigcup_{t\ge1} H_t
]
is countable.

**Proof.** (H_1=S) is finite. If (H_t) is finite, then each (h\in H_t) has finitely many action profiles and finitely many successor states, so (\operatorname{Succ}(h)) is finite. Therefore (H_{t+1}=\bigcup_{h\in H_t}\operatorname{Succ}(h)) is finite. Induction finishes the claim. (\square)

### (\widetilde L5). Global recursive assembly on the full tree

**Statement.** Assume L2 and L4. Choose one root promise (w(s)\in W(s)) for each (s\in S). Then there exists a single family
[
{(x(h),w(h)):h\in H}
]
such that (w(h)\in W(h)) for every history (h), and for every (h) there exists a successor assignment (\phi_h) with
[
(x(h),\phi_h)\in F(h,w(h)),
\qquad
w(h')=\phi_h(h')\quad\forall h'\in\operatorname{Succ}(h).
]
Defining
[
\sigma_i(h):=x_i(h)
]
produces one behavioral profile on the **full** public-history tree, hence one whole-game profile covering all initial states and all deviation-generated histories.

**Proof.** By Sublemma A, enumerate (H={h^1,h^2,\dots}) by nondecreasing depth. Root promises are already chosen using L2.

Proceed recursively. If (h) is a root, (w(h)) is fixed. If (h) is nonroot, it has a unique immediate predecessor (\bar h). When (\bar h) was processed, a witness ((x(\bar h),\phi_{\bar h})\in F(\bar h,w(\bar h))) was chosen, so define
[
w(h):=\phi_{\bar h}(h).
]
This is well-defined because predecessors are unique. Since (\phi_{\bar h}(h)\in W(h)), we have (w(h)\in W(h)).

Now apply L4 to ((h,w(h))): (F(h,w(h))\neq\varnothing). Choose one witness
[
(x(h),\phi_h)\in F(h,w(h)).
]
For each successor (h'\in\operatorname{Succ}(h)), define (w(h'):=\phi_h(h')). Again uniqueness of predecessors gives consistency.

After finishing the recursion, each (x(h)) is a product mixed action at (s(h)). Writing (x(h)=(x_i(h))_{i\in N}) and setting (\sigma_i(h):=x_i(h)) gives a behavioral public-history profile on all of (H). (\square)

**Assembly remark.** Equivalently, if one first builds rooted profiles (\sigma^s) separately, then the whole-game profile is
[
\sigma(h):=\sigma^{\operatorname{root}(h)}(h).
]
So the statewise-to-global glue is explicit and no longer hidden.

### L6. Equilibrium-path delivery inequality

**Statement.** Let (\sigma) be the profile from (\widetilde L5). For every initial state (s), player (i), and horizon (T\ge1),
[
w_i(s)\le
\mathbb E_{s,\sigma}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t)+w_i(h_{T+1})
\right]
+\sum_{t=1}^{T}\eta_t.
]

**Proof.** Fix (s,i,T). Write
[
U_t:=u_i(s_t,a_t),\qquad W_t:=w_i(h_t).
]
Under (\sigma), conditional on the current history (h_t), the action profile is distributed as (x(h_t)), and the next promise is (\phi_{h_t}(h_{t+1})). Hence
[
\mathbb E_{s,\sigma}[U_t+W_{t+1}\mid h_t]
=========================================

\mathcal T_i(h_t;x(h_t),\phi_{h_t}).
]
Since ((x(h_t),\phi_{h_t})\in F(h_t,w(h_t))), the first defining inequality of (F) gives
[
W_t\le \mathbb E_{s,\sigma}[U_t+W_{t+1}\mid h_t]+\eta_t.
]
Take expectations and sum over (t=1,\dots,T). The intermediate promise terms telescope, leaving
[
w_i(s)=\mathbb E[W_1]
\le
\mathbb E!\left[\sum_{t=1}^{T}U_t+W_{T+1}\right]+\sum_{t=1}^{T}\eta_t.
]
This is the stated inequality. (\square)

**Scope note.** This proves only the displayed delivery inequality. It does **not** prove a substantive punishment-mode mechanism.

### L7′. Deviating-path upper bound

**Statement.** Let (\sigma) be the profile from (\widetilde L5). For every initial state (s), player (i), unilateral deviation strategy (\tau_i), and horizon (T\ge1),
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[
\sum_{t=1}^{T} u_i(s_t,a_t)+w_i(h_{T+1})
\right]
\le
w_i(s)+\sum_{t=1}^{T}\eta_t.
]

**Proof.** Fix (s,i,\tau_i,T), and again write
[
U_t:=u_i(s_t,a_t),\qquad W_t:=w_i(h_t).
]
Because (\widetilde L5) defines (x(h)), (w(h)), and (\phi_h) on the full tree (H), every history visited under the deviating law is covered.

Condition on the visited history (h_t), and let
[
\mu_t:=\tau_i(h_t)\in \Delta(A_i(s(h_t)))
]
be the deviator’s mixed action. For each pure action (a_i'), the second defining inequality of (F(h_t,w(h_t))) gives
[
\mathcal T_i(h_t;a_i',x_{-i}(h_t),\phi_{h_t})
\le
w_i(h_t)+\eta_t
===============

W_t+\eta_t.
]
Average this inequality with respect to (\mu_t). By linearity, the left-hand side becomes the conditional expectation of (U_t+W_{t+1}) under ((\tau_i,\sigma_{-i})). Thus
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}[U_t+W_{t+1}\mid h_t]
\le
W_t+\eta_t.
]
Take expectations and sum over (t=1,\dots,T). Telescoping yields
[
\mathbb E!\left[\sum_{t=1}^{T}U_t+W_{T+1}\right]
\le
w_i(s)+\sum_{t=1}^{T}\eta_t.
]
This is the claim. (\square)

### L8′. Telescoping comparison and uniformization

**Statement.** Assume L1, L6, L7′, and (\eta_t\ge0). Then for every initial state (s), player (i), deviation (\tau_i), and horizon (T\ge1),
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2B}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]
If
[
M:=\sum_{t=1}^{\infty}\eta_t<\infty,
]
then
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2(B+M)}{T},
]
so any
[
T_0\ge \left\lceil \frac{2(B+M)}{\varepsilon}\right\rceil
]
ensures
[
\gamma_i^T(s,\sigma)\ge
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\varepsilon
\qquad \forall T\ge T_0.
]

**Proof.** L7′ gives
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[\sum_{t=1}^{T}u_i(s_t,a_t)+w_i(h_{T+1})\right]
\le
w_i(s)+\sum_{t=1}^{T}\eta_t.
]
L6 gives
[
w_i(s)\le
\mathbb E_{s,\sigma}!\left[\sum_{t=1}^{T}u_i(s_t,a_t)+w_i(h_{T+1})\right]
+\sum_{t=1}^{T}\eta_t.
]
Subtracting the second inequality from the first yields
[
\mathbb E_{s,(\tau_i,\sigma_{-i})}!\left[\sum_{t=1}^{T}u_i(s_t,a_t)\right]
--------------------------------------------------------------------------

\mathbb E_{s,\sigma}!\left[\sum_{t=1}^{T}u_i(s_t,a_t)\right]
\le
\mathbb E_{s,\sigma}[w_i(h_{T+1})]
----------------------------------

\mathbb E_{s,(\tau_i,\sigma_{-i})}[w_i(h_{T+1})]
+
2\sum_{t=1}^{T}\eta_t.
]
By L1, (|w_i(h)|\le B) for every history, so the terminal-promise difference is at most (2B). Divide by (T) to obtain
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)
\le
\frac{2B}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]
Since (\eta_t\ge0) and (\sum_t \eta_t=M<\infty),
[
\sum_{t=1}^{T}\eta_t\le M,
]
hence the sharper bound
[
\gamma_i^T(s,(\tau_i,\sigma_{-i}))-\gamma_i^T(s,\sigma)\le \frac{2(B+M)}{T}.
]
Choosing (T_0\ge \lceil 2(B+M)/\varepsilon\rceil) gives the uniform (\varepsilon)-equilibrium inequality for all (T\ge T_0). (\square)

## Main result assembly

Assume L1, L2, and L4. Fix a finite stochastic game (G) and (\varepsilon>0). Choose any summable nonnegative leakage schedule ((\eta_t)), with total mass (M=\sum_t\eta_t).

By L2, choose one root promise (w(s)\in W(s)) for each initial state (s\in S). By (\widetilde L5), recursively assemble one whole-game public-history behavioral profile (\sigma) on the full tree (H). By L6 and L7′, compliant and deviating path values satisfy complementary telescoping inequalities with terminal promise corrections. By L8′,
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\gamma_i^T(G,s,\sigma)
\le
\frac{2(B+M)}{T}.
]
Hence any
[
T_0\ge \left\lceil \frac{2(B+M)}{\varepsilon}\right\rceil
]
suffices to ensure
[
\gamma_i^T(G,s,\sigma)\ge
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon
]
for all (T\ge T_0), all initial states (s), all players (i), and all unilateral deviations (\tau_i).

Therefore, **if** L1, L2, and especially L4 are available, the route closes and proves the desired one-profile uniform (\varepsilon)-equilibrium statement for the fixed game (G). Since (G) and (\varepsilon) were arbitrary, this would establish the universal theorem. The current packet does **not** prove those missing inputs, so this is a conditional closure only. 

## Proof status

The correct overall status is:

* **Global theorem:** not proved.
* **Project status:** bootstrap/open.
* **What is proved in the packet, after repair:** Sublemma A, sharpened L3, strengthened full-tree L5 conditional on L4, literal L6, L7′, and L8′.
* **What remains missing:** L4 outright, plus packet-level grounding for imported L1 and L2.
* **Net conclusion:** this is a **partial/conditional** proof report. The post-L4 tail is essentially cleared. The universal existence theorem remains open because the uncorrelated selector theorem L4 is still unresolved and the continuation inputs L1-L2 are not proved in-packet.   

## Assumptions used

1. Finite stochastic game data: finitely many players, states, and state-dependent finite action sets; perfect public monitoring; simultaneous actions; fixed transition kernel; behavioral public-history strategies; bounded stage payoffs normalized to ([0,1]); finite-horizon average payoff criterion.
2. Each action set is nonempty, so the relevant simplices are well-defined.
3. The leakage schedule satisfies
   [
   \eta_t\ge0,\qquad \sum_{t=1}^\infty \eta_t<\infty.
   ]
4. L1: existence of the bounded compact safe-promise correspondence (W).
5. L2: nonemptiness of (W(h)) at every history.
6. L4: existence of a one-step **uncorrelated** selector, i.e. nonemptiness of (F(h,w)) for every (h) and (w\in W(h)).

## Unresolved risks

The remaining risks are concentrated and explicit.

First, **L4 is the mathematical furnace**. The route needs a product-form one-step selector at every history. Existing Martin-function outputs described in the packet appear to stop short of exactly that uncorrelated selection step. If L4 fails, the route has hit the open problem head-on rather than slipped around it.

Second, **L1 and L2 are still imports**. The packet treats them as external machinery, but does not supply definitive external citations inside the proof report itself. So even the conditional tail still depends on uncited upstream inputs.

Third, **L6 must not be oversold**. The proved statement is the literal delivery inequality only. Any stronger narrative in which the strategy publicly switches to a history-anchored punishment plan remains unproved unless the public state is enriched to remember the anchor history.

Fourth, **stale packet versions should not be treated as authoritative**. Old L7 and L8, and older notation in ((B_\delta,v^s,\beta)), should be regarded as superseded by the repaired (W/w/F) formulation with L7′ and L8′.

## Evidence trail

* The durable claim source fixes the theorem-side target as one-profile strategy-existence of uniform (\varepsilon)-equilibria for every finite stochastic game, and labels the overarching problem as open. 
* The durable proof-state anchor marks the project status as **bootstrap** and names the proof-state and claim files as the stable sources. 
* The durable route memo selects the Martin-function bootstrap route as the preferred current route, records L4 as the central unresolved selector step, and notes that the post-L4 tail is salvageable after explicit repairs. 
* The main request packet contains the breakdown, accepted amendments, prover outputs, and reviewer outputs. In particular, `prover_04` supplies the repaired proofs of L3, strengthened L5, L6, L7′, and L8′, while the reviewers uniformly classify the packet as `PATCH_BIG` rather than a complete theorem proof. 

## Bottom line

This route now has a clean conditional tail:

[
\text{safe promises} \Rightarrow \text{local feasibility} \Rightarrow \text{uncorrelated selector} \Rightarrow \text{full-tree assembly} \Rightarrow \text{telescoping} \Rightarrow \text{uniform equilibrium}.
]

But the theorem is still open because the arrow labeled **uncorrelated selector** remains unproved. The right certification is:

* **accepted conditionally:** L3, strengthened L5, literal L6, L7′, L8′;
* **not accepted as a proof of the theorem:** because L4 is unresolved and L1-L2 remain imported;
* **canonical packet conclusion:** a repaired conditional proof of the post-L4 tail, not a full proof of uniform equilibrium existence in all finite stochastic games.
