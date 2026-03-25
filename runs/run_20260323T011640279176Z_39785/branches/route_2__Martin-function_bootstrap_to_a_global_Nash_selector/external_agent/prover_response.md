[BREAKDOWN_AMEND] I normalize the live Route B backbone to the fixed-promise version
[
L1\to \text{imported }L2\to L3^\ast\to \text{open }L4^\ast\to L5^\ast\to \text{literal }L6\to L7'\to L8'\to L9'\to L10,
]
and I keep the theorem explicitly bootstrap/open. This matches the current request packet, the durable proof-state anchor, and the route memo: the target is still one whole-game behavioral profile, one threshold, all sufficiently large horizons, and every initial state, while the unresolved bottleneck is the selector step.   

[BREAKDOWN_AMEND] Replace the canceled-promise setup by the fixed-promise local increment system.

Fix an initial state (s\in S). By L2 choose
[
w^s\in W^\star((s)).
]
For each public history (h\in H^s), let (C(h)) be the finite set of one-step extensions (h^+=(h,a,s')). For a current bias (b\in W^\star(h)), define (F_s^\ast(h,b)) to be the set of tuples
[
(x,\beta,\eta)
]
such that

1. (x\in X(h):=\prod_{j\in N}\Delta(A_j(s(h)))),

2. (\beta(h^+)\in W^\star(h^+)) for every (h^+\in C(h)),

3. (\eta\in[0,2]),

4. for every player (i\in N),
   [
   (E_h^i)\qquad
   u_i(s(h),x)+\mathbb E_{x,P}!\left[\beta_i(H')\mid h\right]-b_i
   \ge w_i^s-\eta,
   ]

5. for every player (i\in N) and every pure one-step deviation (a_i'\in A_i(s(h))),
   [
   (D_h^{i,a_i'})\qquad
   u_i(s(h),a_i',x_{-i})+\mathbb E_{a_i',x_{-i},P}!\left[\beta_i(H'^{a_i'})\mid h\right]-b_i
   \le w_i^s+\eta.
   ]

Here (u_i(s(h),x)) denotes the expected stage payoff under the mixed action profile (x), well-defined by direct finite summation, and similarly for the conditional expectations above.

[DERIVED] **Corrected L3(^\ast), compactness half.** For every (s\in S), every (h\in H^s), and every (b\in W^\star(h)), the set (F_s^\ast(h,b)) is compact.

**Proof.**
Because the game is finite, (A_i(s(h))) is finite for every (i), hence each simplex (\Delta(A_i(s(h)))) is compact, and therefore
[
X(h)=\prod_{j\in N}\Delta(A_j(s(h)))
]
is compact. Also (C(h)) is finite because the state set and all action sets are finite. By L2, each (W^\star(h^+)) is compact. Therefore the ambient product
[
K(h):=X(h)\times \prod_{h^+\in C(h)}W^\star(h^+)\times [0,2]
]
is compact.

It remains to check closedness. The maps
[
x\mapsto u_i(s(h),x),
\qquad
(x,\beta)\mapsto \mathbb E_{x,P}[\beta_i(H')\mid h],
\qquad
(x_{-i},\beta)\mapsto \mathbb E_{a_i',x_{-i},P}[\beta_i(H'^{a_i'})\mid h]
]
are continuous, because each is a finite affine combination of coordinates of (x) and (\beta). Hence every inequality ((E_h^i)) and ((D_h^{i,a_i'})) cuts out a closed subset of (K(h)). There are only finitely many players and finitely many pure actions (a_i'), so (F_s^\ast(h,b)) is a finite intersection of closed subsets of the compact set (K(h)). Thus (F_s^\ast(h,b)) is compact.

It remains only to justify the bound (\eta\in[0,2]). Since (u_i\in[0,1]), (b_i\in[0,1]), (w_i^s\in[0,1]), and (\beta_i(h^+)\in[0,1]), both left-hand sides in ((E_h^i)) and ((D_h^{i,a_i'})) lie in ([-1,2]). Therefore any feasible tuple with (\eta>2) stays feasible after replacing (\eta) by (2). So the restriction to ([0,2]) is without loss. This proves compactness. [DERIVED]

[ASSUMPTION+] **L4(^\ast), nonemptiness/selector half.** For every (s\in S), every (h\in H^s), and every current bias (b\in W^\star(h)), the set (F_s^\ast(h,b)) is nonempty. Equivalently, there exists a one-step fixed-promise selector at every node. This is the theorem-sized unresolved step in the present route.

[DERIVED] **L5(^\ast), rooted full-tree recursion.** Assume L2 and L4(^\ast). Then for every initial state (s\in S) there exist maps
[
h\mapsto x^s(h),\qquad h\mapsto b^s(h),\qquad h\mapsto \eta^s(h)
]
defined on the full rooted public-history tree (H^s), with
[
b^s(h)\in W^\star(h),
\qquad
x^s(h)\in \prod_{j\in N}\Delta(A_j(s(h))),
\qquad
\eta^s(h)\in[0,2],
]
such that the local relations ((E_h^i)) and ((D_h^{i,a_i'})) hold at every history (h\in H^s) with (w^s) fixed.

**Proof.**
Fix (s\in S). By L2, (W^\star((s))\neq\varnothing), so choose (w^s\in W^\star((s))). Set the root bias equal to the root promise:
[
b^s((s)):=w^s.
]
This is legitimate because (w^s\in W^\star((s))).

Now recurse on depth. For depth (1), the current bias (b^s((s))\in W^\star((s))) is already chosen. By L4(^\ast), (F_s^\ast((s),b^s((s)))\neq\varnothing), so choose one tuple
[
\bigl(x^s((s)),\beta,\eta^s((s))\bigr)\in F_s^\ast((s),b^s((s))).
]
For each child (h^+\in C((s))), define
[
b^s(h^+):=\beta(h^+).
]
Then (b^s(h^+)\in W^\star(h^+)) by the definition of (F_s^\ast((s),b^s((s)))).

Inductively, suppose that for all histories of depth at most (t), the biases (b^s(h)\in W^\star(h)) have been defined, and for all histories of depth at most (t-1), the tuples (x^s(h),\eta^s(h)) and child-bias assignments have already been defined so that the local relations hold there. Let (h) be any depth-(t) history. Since (b^s(h)\in W^\star(h)), L4(^\ast) gives a nonempty (F_s^\ast(h,b^s(h))). Choose one tuple
[
\bigl(x^s(h),\beta_h,\eta^s(h)\bigr)\in F_s^\ast(h,b^s(h)),
]
and define
[
b^s(h^+):=\beta_h(h^+)
\qquad\text{for all }h^+\in C(h).
]
Because every non-root history has a unique predecessor in the rooted tree (H^s), there is no compatibility conflict in this definition.

By induction over all depths, the maps (x^s,b^s,\eta^s) are defined on the full rooted tree (H^s), not merely on-path histories. The local fixed-promise inequalities hold at every node by construction. [DERIVED]

[DERIVED] **Literal L6.** For each (s\in S), the selector from L5(^\ast) defines a rooted behavioral profile
[
\sigma_i^s(h):=x_i^s(h)
\qquad(h\in H^s).
]

**Proof.**
By L5(^\ast),
[
x_i^s(h)\in \Delta(A_i(s(h)))
]
for every player (i) and every rooted history (h\in H^s). This is exactly the defining condition for a behavioral strategy on the rooted public-history domain (H^s). Taking the product over players gives the rooted profile (\sigma^s). No punishment-mode claim is used or needed here. [DERIVED]

[DERIVED] **Corrected L7′, rooted telescoping deviation bound.** Assume L2 and L5(^\ast). Fix (s\in S), (i\in N), (T\ge1), and a unilateral behavioral deviation (\tau_i). Then
[
\gamma_i^T(G,s,\sigma^s)
\ge
w_i^s-\frac{1+\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right]}{T},
]
and
[
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)
\le
w_i^s+\frac{1+\mathbb E_{G,s,(\tau_i,\sigma^s_{-i})}!\left[\sum_{t=1}^T \eta^s(H_t)\right]}{T}.
]
Consequently,
[
\gamma_i^T(G,s,\sigma^s)
\ge
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)
------------------------------------------------

\frac{
2+
\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right]
+
\mathbb E_{G,s,(\tau_i,\sigma^s_{-i})}!\left[\sum_{t=1}^T \eta^s(H_t)\right]
}{T}.
]

**Proof.**
Let (H_t) be the realized public history at stage (t).

First consider obedient play under (\sigma^s). By definition of (\sigma^s), the mixed action prescribed at history (h) is exactly (x^s(h)). Therefore the local relation ((E_h^i)) gives
[
\mathbb E!\left[
u_i(s_t,a_t)+b_i^s(H_{t+1})-b_i^s(H_t)\mid H_t=h
\right]
\ge
w_i^s-\eta^s(h).
]
Taking expectations and summing from (t=1) to (T), the tower property yields
[
\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
+
\mathbb E_{G,s,\sigma^s}[b_i^s(H_{T+1})]
----------------------------------------

b_i^s((s))
\ge
T w_i^s
-------

\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right].
]
Rearranging and dividing by (T),
[
\gamma_i^T(G,s,\sigma^s)
\ge
w_i^s
-----

\frac{
\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right]
+
\mathbb E_{G,s,\sigma^s}[b_i^s(H_{T+1})]
----------------------------------------

b_i^s((s))
}{T}.
]
Because (b_i^s(h)\in W^\star(h)\subseteq[0,1]) for every history (h), one has
[
\mathbb E_{G,s,\sigma^s}[b_i^s(H_{T+1})]-b_i^s((s))\le 1.
]
Hence
[
\gamma_i^T(G,s,\sigma^s)
\ge
w_i^s-\frac{1+\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right]}{T}.
]

Now consider the deviating law ((\tau_i,\sigma^s_{-i})). At a given history (h), let
[
\mu_h:=\tau_i(h)\in \Delta(A_i(s(h))).
]
For each pure (a_i'\in A_i(s(h))), the local inequality ((D_h^{i,a_i'})) holds. Both the expected stage payoff and the expected next bias are affine in the deviator’s mixed action. Therefore averaging ((D_h^{i,a_i'})) against (\mu_h(a_i')) gives
[
\mathbb E!\left[
u_i(s_t,a_t)+b_i^s(H_{t+1})-b_i^s(H_t)\mid H_t=h
\right]
\le
w_i^s+\eta^s(h)
]
under the deviating law. Summing exactly as above,
[
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)
\le
w_i^s+\frac{1+\mathbb E_{G,s,(\tau_i,\sigma^s_{-i})}!\left[\sum_{t=1}^T \eta^s(H_t)\right]}{T}.
]

Subtracting the two estimates proves the final bound. [DERIVED]

[ASSUMPTION+] **Controlled leakage schedule.** I now add the explicit quantitative input that the selector can be chosen with a depth budget
[
r_t\ge0,\qquad \sum_{t\ge1} r_t\le \varepsilon/8,
]
and
[
\eta^s(h)\le r_{|h|}
\qquad\text{for every }s\in S,\ h\in H^s.
]
This is the controlled-leakage part of the fixed-promise selector package. It is not proved from the present Martin-function imports.

[DERIVED] **Corrected L8′, threshold extraction.** Under the controlled leakage schedule above, for every (s\in S), every player (i), every deviation (\tau_i), and every (T\ge1),
[
\gamma_i^T(G,s,\sigma^s)
\ge
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)
------------------------------------------------

\frac{2+\varepsilon/4}{T}.
]
Hence with
[
T_0:=\left\lceil \frac{2+\varepsilon/4}{\varepsilon}\right\rceil
]
one has, for all (T\ge T_0),
[
\gamma_i^T(G,s,\sigma^s)
\ge
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)-\varepsilon.
]

**Proof.**
At stage (t), every realized history has length (t). Therefore, pathwise,
[
\sum_{t=1}^\infty \eta^s(H_t)\le \sum_{t=1}^\infty r_t\le \varepsilon/8
]
under any play law starting from (s). In particular,
[
\mathbb E_{G,s,\sigma^s}!\left[\sum_{t=1}^T \eta^s(H_t)\right]\le \varepsilon/8,
\qquad
\mathbb E_{G,s,(\tau_i,\sigma^s_{-i})}!\left[\sum_{t=1}^T \eta^s(H_t)\right]\le \varepsilon/8.
]
Insert these two bounds into L7′:
[
\gamma_i^T(G,s,\sigma^s)
\ge
\gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)
------------------------------------------------

# \frac{2+\varepsilon/8+\varepsilon/8}{T}

## \gamma_i^T\bigl(G,s,(\tau_i,\sigma^s_{-i})\bigr)

\frac{2+\varepsilon/4}{T}.
]
If (T\ge T_0), then by direct computation
[
\frac{2+\varepsilon/4}{T}\le \varepsilon.
]
So the stated equilibrium inequality follows. [DERIVED]

[DERIVED] **L9′, disjoint-union global assembly.** There exists one whole-game behavioral profile (\sigma\in\Sigma(G)) such that for every initial state (s\in S), every history (h\in H^s), and every player (i),
[
\sigma_i(h)=\sigma_i^s(h).
]

**Proof.**
Every public history (h=(s_1,a_1,\dots,s_t)) has a unique first state (s_1). Define
[
\sigma_i(h):=\sigma_i^{s_1}(h).
]
This is well-defined because the first state is unique, so no history belongs to two different rooted trees. Since (\sigma_i^{s_1}(h)\in\Delta(A_i(s(h)))), the map (\sigma_i) is a behavioral strategy on the full public-history domain.

Now fix an initial state (s). Every history that can occur from initial state (s), under obedient play or under any unilateral deviation, belongs to the rooted tree (H^s). On that rooted tree, by construction,
[
\sigma_i(h)=\sigma_i^s(h).
]
Hence the induced law of play from initial state (s) under the global profile (\sigma) coincides with the induced law under the rooted profile (\sigma^s). Therefore all payoff inequalities proved for (\sigma^s) transfer verbatim to the global profile (\sigma). [DERIVED]

[DERIVED] **L10, conditional synthesis.** Assume imported L1, imported L2, the proved compactness half of corrected L3(^\ast), the open selector hypothesis L4(^\ast), and the controlled leakage schedule. Then for every finite stochastic game (G) and every (\varepsilon>0) there exist
[
\sigma\in\Sigma(G),\qquad T_0\in\mathbb N_{>0},
]
such that for all (T\ge T_0), all initial states (s_1\in S), all players (i\in N), and all unilateral deviations (\tau_i\in\Sigma_i(G)),
[
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T\bigl(G,s_1,(\tau_i,\sigma_{-i})\bigr)-\varepsilon.
]

**Proof.**
Fix (\varepsilon>0). For each initial state (s), L5(^\ast) and literal L6 produce a rooted profile (\sigma^s). L8′ gives one threshold (T_0) working for every rooted profile simultaneously, because the bound is state-independent. L9′ assembles the family ({\sigma^s}_{s\in S}) into one whole-game behavioral profile (\sigma), and from each initial state (s) the induced play law under (\sigma) agrees with that under (\sigma^s). Therefore the L8′ inequality transfers to (\sigma) for every initial state. This is exactly the target quantifier pattern. [DERIVED]

[BREAKDOWN_AMEND] Old L6 should be demoted to literal strategy construction only; it is not needed in the deviation proof. Old L7 and old L8 should be retired and replaced by corrected L7′ and L8′ above. The present packet should also record that L5(^\ast) depends on L2 for the root choice and must quantify over the full rooted tree, not just on-path histories.

[BREAKDOWN_AMEND] The official breakdown should mark L4(^\ast), not the old variable-promise L4, as the live research bottleneck. The local fixed-promise system above is the one that actually supports the root-promise telescope.

**Status summary**

* [DERIVED] Corrected fixed-promise local feasibility sets (F_s^\ast(h,b)) are compact.

* [DERIVED] Conditional on L4(^\ast), rooted full-tree recursion L5(^\ast) is valid.

* [DERIVED] Literal rooted strategy construction L6 is valid.

* [DERIVED] Corrected telescoping lemma L7′ is valid.

* [DERIVED] Corrected bookkeeping lemma L8′ is valid once the leakage schedule is part of the selector hypothesis.

* [DERIVED] Global assembly L9′ is valid.

* [DERIVED] Conditional synthesis L10 is valid.

* [GAP] L1 is still not fully repaired in the current branch.

* [GAP] L2 is still imported rather than source-matched/proved.

* [GAP] L4(^\ast) remains open, and it is the theorem-sized missing selector theorem.

So the proof has advanced: the post-selector tail is now coherent under the corrected fixed-promise local system, but the theorem remains conditional and bootstrap/open until L4(^\ast) and the L1/L2 grounding are actually discharged.
