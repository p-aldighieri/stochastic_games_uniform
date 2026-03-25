# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T18:06:44.304062+00:00

## Instructions

Advance the proof by proving lemmas from the breakdown. Every step must have explicit justification (known theorem, previous lemma, or direct computation). Tag conclusions [DERIVED], new assumptions [ASSUMPTION+]/[ASSUMPTION-], and breakdown change requests [BREAKDOWN_AMEND]. Be explicit about gaps. Reference lemmas by number. Maintain a status summary of what's proved.

## Context

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown.md

# Breakdown Output

Generated: 2026-03-23T17:34:03.268537+00:00

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

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown_amendments.md

# Breakdown Amendments

Accepted by orchestrator policy:
- L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- Under L7′, the closing step can be sharpened substantially.
- The dependency spine can be shortened after the open selector step:
- L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- Under L7′, the closing step can be sharpened substantially.
- The dependency spine can be shortened after the open selector step:
- L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- Under L7′, the closing step can be sharpened substantially.
- The dependency spine can be shortened after the open selector step:

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/formalizer.md

# Formalizer Output

Generated: 2026-03-23T01:56:36.300643+00:00

## Mathematical domain

Noncooperative game theory, specifically finite stochastic (Markov) games with perfect public monitoring, behavioral strategies, finite-horizon average payoff, and Nash-type equilibrium existence.  

## Claim type

Open universal existence conjecture. Logically, it is a strategy-existence statement with quantifier pattern
[
\forall G\in\mathfrak G\ \forall \varepsilon\in \mathbb R_{>0}\ \exists \sigma\in\Sigma(G)\ \exists T_0\in\mathbb N_{>0}\ \forall T\in\mathbb N_{>0}\ (T\ge T_0 \Rightarrow \forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G): \cdots ).
]
The adopted reading is the existence of uniform (\varepsilon)-equilibria for every (\varepsilon>0), not the alternative payoff-set formulation.  

## Precise formal statement

Let (\mathfrak G) be the class of all tuples
[
G=(N,S,(A_i)*{i\in N},u,P)
]
such that
[
1\le |N|<\infty,\qquad 1\le |S|<\infty,
]
for every (i\in N) and (s\in S),
[
1\le |A_i(s)|<\infty,
]
for every (s\in S) and action profile
[
a\in A(s):=\prod*{j\in N}A_j(s),
]
the stage payoff satisfies
[
u_i(s,a)\in[0,1]\quad\text{for each }i\in N,
]
and
[
P(\cdot\mid s,a)\in \Delta(S).
]

For each (t\in\mathbb N_{>0}), define the set of public histories of length (t) by
[
H_t(G):=
\left{
(s_1,a_1,s_2,a_2,\dots,s_{t-1},a_{t-1},s_t)
:
s_k\in S,\ a_k\in A(s_k)
\right}.
]

For each player (i\in N), let (\Sigma_i(G)) be the set of all behavioral strategies
[
\sigma_i:\bigcup_{t\ge 1} H_t(G)\to \bigcup_{s\in S}\Delta(A_i(s))
]
such that whenever (h_t\in H_t(G)) ends at state (s_t), one has
[
\sigma_i(h_t)\in \Delta(A_i(s_t)).
]
Let
[
\Sigma(G):=\prod_{i\in N}\Sigma_i(G).
]

For (G\in\mathfrak G), (T\in\mathbb N_{>0}), (s_1\in S), (\sigma\in\Sigma(G)), and (i\in N), define the expected (T)-stage average payoff
[
\gamma_i^T(G,s_1,\sigma)
:=
\mathbb E_{G,s_1,\sigma}!\left[\frac1T\sum_{t=1}^{T}u_i(s_t,a_t)\right].
]

Define that (\sigma\in\Sigma(G)) is a **uniform (\varepsilon)-equilibrium** iff
[
\exists T_0\in\mathbb N_{>0}\ \forall T\in\mathbb N_{>0},
\Bigl(
T\ge T_0 \Rightarrow
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G),\
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon
\Bigr).
]

Equivalently, define
[
\operatorname{HasUniformEq}(G)
:\iff
\forall \varepsilon\in\mathbb R_{>0}\ \exists \sigma\in\Sigma(G)\ \exists T_0\in\mathbb N_{>0}
]
such that
[
\forall T\in\mathbb N_{>0},
\Bigl(
T\ge T_0 \Rightarrow
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G),\
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon
\Bigr).
]

Then the informal claim is formalized as the open question whether
[
\forall G\in\mathfrak G,\ \operatorname{HasUniformEq}(G)
]
is true. This is the clean strategy-existence formalization selected in the request packet and the durable claim source.  

## User assumptions

The following assumptions are directly fixed by the request packet and durable claim source.  

* [USER] The model class is the class of finite stochastic games with finitely many players, finitely many states, and finitely many action sets.
* [USER] The state is publicly observed at each stage.
* [USER] Actions are chosen simultaneously at each stage.
* [USER] The transition law is a fixed kernel depending only on the current state and current action profile.
* [USER] Strategies are behavioral strategies defined on public histories.
* [USER] Stage payoffs are bounded and normalized to ([0,1]).
* [USER] The payoff criterion of the target claim is expected finite-horizon average payoff.
* [USER] The equilibrium notion is approximate Nash equilibrium against unilateral deviations.
* [USER] Uniformity means one fixed strategy profile works for every sufficiently large horizon (T).
* [USER] The equilibrium inequalities are required for every initial state (s_1\in S).
* [USER] The intended formal target is existence of uniform (\varepsilon)-equilibria for every (\varepsilon>0), rather than the payoff-set wording.

## Added assumptions

* [ASSUMPTION+] (N\neq\varnothing), (S\neq\varnothing), and (A_i(s)\neq\varnothing) for all (i,s). Justification: otherwise the game may fail to be playable and the probability simplices (\Delta(A_i(s))) may be empty.
* [ASSUMPTION+] (\Delta(X)) denotes the set of probability measures on the finite set (X). Justification: this is needed to state the codomains of (P) and (\sigma_i) explicitly.
* [ASSUMPTION+] (\mathbb E_{G,s_1,\sigma}) is the expectation under the unique law on plays induced by (G), deterministic initial state (s_1), and profile (\sigma). Justification: this makes (\gamma_i^T) well-defined.
* [ASSUMPTION+] Horizons range over positive integers (\mathbb N_{>0}). Justification: the expression (1/T) excludes (T=0).

## Scope ambiguities

The following alternative readings exist in the literature; the adopted reading is the one preferred in the supplied materials.  

* [SCOPE] “Uniform equilibrium” could mean an exact equilibrium ((\varepsilon=0)) or, as adopted above, existence of a uniform (\varepsilon)-equilibrium for every (\varepsilon>0).
* [SCOPE] The claim could be phrased as existence of a uniform equilibrium payoff rather than existence of a strategy profile. The adopted target is the strategy-existence statement.
* [SCOPE] Some formulations quantify relative to a fixed initial state or an initial distribution. The adopted statement quantifies over every initial state (s_1\in S).
* [SCOPE] Some formulations restrict strategies to stationary, Markov, or finite-memory strategies. No such restriction is part of the adopted statement.
* [SCOPE] Some models allow private monitoring or signal structures. The adopted statement uses perfect public monitoring only.
* [SCOPE] Some models add an external public randomization device. The adopted statement does not augment the game with such an extra device.
* [SCOPE] Discounted payoff appears in the background discussion, but not in the target statement. The adopted claim is solely about expected finite-horizon average payoff.

The durable proof-state source is bootstrap / clean-slate, so no additional theorem-side hypotheses were imported from earlier project passes.

---
## ADDITIONAL LOADED FILES

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_01.md

# Reviewer Output

Generated: 2026-03-23T06:46:57.174989+00:00

VERDICT: PATCH_BIG

The pass gets the main meta-level judgment right: it does **not** overclaim the open theorem, and it correctly localizes the unresolved mass in L1 through L4, especially L4. That is consistent with the route packet, the durable claim source, and the durable proof-state anchor, all of which still treat the theorem as open/bootstrap rather than solved.

**L5.** The recursion proof is logically sound **after** the stated repair. The finite-level induction, the choice of a root bias from (B_\delta((s),v^s)), the successor assignment, and the unique-predecessor consistency check are all fine. But the official L5 statement in the breakdown is **not** what is proved. The proof needs L2 for root-bias nonemptiness, and it needs the selector on the **full rooted public-history tree**, not merely on “reachable” on-path histories. [SCOPE] This is a genuine statement change, not a cosmetic edit.

**L6.** The proof is valid for the **literal text only**. The constant normal-mode construction really does satisfy the four displayed clauses, with clause 2 vacuous because (M_t=i) never occurs. So the derivation is logically valid, but the lemma is semantically much weaker than its technique hint and weaker than the punishment narrative advertised in the route packet. [SCOPE] If punishment mode is supposed to be usable rather than vacuous, the public state has to remember the punishment anchor history, or an equivalent public encoding of it.

**L7 / L7′.** The telescoping proof of **L7′** is mathematically sound. The bias process is bounded via L2, the on-path inequality gives the lower bound, the unilateral-deviation inequality gives the upper bound, mixed deviations are handled by affine averaging over pure actions, and the bias terms telescope to an (O(1/T)) remainder. But the original **L7** is not proved from its own displayed dependencies as written. The proof actually uses L2, the strengthened full-tree form of L5, and a root-specific profile (\sigma^s), whereas the breakdown lists only L4-L6 and states the lemma for (\sigma^\varepsilon). There is also a small but real notation/assembly gap in the corollary back to original L7: one must explicitly identify the global profile (\sigma^\varepsilon) with the root-assembled profile satisfying (\sigma^\varepsilon(h)=x^{\mathrm{root}(h)}(h)). That identification is available from the literal L6 construction, but it is not written into the corollary step.

**L8 / L8′.** The bookkeeping is correct once (\eta_t\ge 0) is made explicit. The proof uses nonnegativity in an essential way, so that sign condition has to be part of the formal assumptions rather than an informal aside. A second notation gap remains in **L8′**: the statement and proof are written for (\sigma^\varepsilon), but L7′ is a lemma about (\sigma^s). Again, a one-line global assembly step fixes this, but it must be stated explicitly.

[SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

The citation problem here is mainly a **logical-dependency citation** problem, not a bibliographic one. L5 must cite L2. Original L7 must cite L2 and the strengthened L5. L8 must cite the added assumption (\eta_t\ge 0). Also, the shortened post-L4 spine still needs an explicit global-assembly glue step from the family ({\sigma^s}_{s\in S}) to one profile on the whole game. So the clean corrected backbone is not quite `L1→L2→L3→L4→L5→L7′→L8′→Theorem`; it is `L1→L2→L3→L4→L5→(global assembly)→L7′→L8′→Theorem`, with L6 demoted unless punishments are restored non-vacuously. Most of these repairs are already correctly diagnosed in the packet’s own accepted-amendments section.

Bottom line: the post-L4 terrain is close to cleared, and the actual telescoping/bookkeeping arguments are good. But the official packet still has enough statement/proof mismatch that it should **not** be accepted as-is. Accept it after rewriting L5, L7, L8, the dependency spine, and the glue so they match the proofs actually given.

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_02.md

# Reviewer Output

Generated: 2026-03-23T06:46:57.216756+00:00

VERDICT: PATCH_BIG

The pass gets the main meta-level judgment right: it does **not** overclaim the open theorem, and it correctly localizes the unresolved mass in L1 through L4, especially L4. That is consistent with the route packet, the durable claim source, and the durable proof-state anchor, all of which still treat the theorem as open/bootstrap rather than solved.

**L5.** The recursion proof is logically sound **after** the stated repair. The finite-level induction, the choice of a root bias from (B_\delta((s),v^s)), the successor assignment, and the unique-predecessor consistency check are all fine. But the official L5 statement in the breakdown is **not** what is proved. The proof needs L2 for root-bias nonemptiness, and it needs the selector on the **full rooted public-history tree**, not merely on “reachable” on-path histories. [SCOPE] This is a genuine statement change, not a cosmetic edit.

**L6.** The proof is valid for the **literal text only**. The constant normal-mode construction really does satisfy the four displayed clauses, with clause 2 vacuous because (M_t=i) never occurs. So the derivation is logically valid, but the lemma is semantically much weaker than its technique hint and weaker than the punishment narrative advertised in the route packet. [SCOPE] If punishment mode is supposed to be usable rather than vacuous, the public state has to remember the punishment anchor history, or an equivalent public encoding of it.

**L7 / L7′.** The telescoping proof of **L7′** is mathematically sound. The bias process is bounded via L2, the on-path inequality gives the lower bound, the unilateral-deviation inequality gives the upper bound, mixed deviations are handled by affine averaging over pure actions, and the bias terms telescope to an (O(1/T)) remainder. But the original **L7** is not proved from its own displayed dependencies as written. The proof actually uses L2, the strengthened full-tree form of L5, and a root-specific profile (\sigma^s), whereas the breakdown lists only L4-L6 and states the lemma for (\sigma^\varepsilon). There is also a small but real notation/assembly gap in the corollary back to original L7: one must explicitly identify the global profile (\sigma^\varepsilon) with the root-assembled profile satisfying (\sigma^\varepsilon(h)=x^{\mathrm{root}(h)}(h)). That identification is available from the literal L6 construction, but it is not written into the corollary step.

**L8 / L8′.** The bookkeeping is correct once (\eta_t\ge 0) is made explicit. The proof uses nonnegativity in an essential way, so that sign condition has to be part of the formal assumptions rather than an informal aside. A second notation gap remains in **L8′**: the statement and proof are written for (\sigma^\varepsilon), but L7′ is a lemma about (\sigma^s). Again, a one-line global assembly step fixes this, but it must be stated explicitly.

[SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

The citation problem here is mainly a **logical-dependency citation** problem, not a bibliographic one. L5 must cite L2. Original L7 must cite L2 and the strengthened L5. L8 must cite the added assumption (\eta_t\ge 0). Also, the shortened post-L4 spine still needs an explicit global-assembly glue step from the family ({\sigma^s}_{s\in S}) to one profile on the whole game. So the clean corrected backbone is not quite `L1→L2→L3→L4→L5→L7′→L8′→Theorem`; it is `L1→L2→L3→L4→L5→(global assembly)→L7′→L8′→Theorem`, with L6 demoted unless punishments are restored non-vacuously. Most of these repairs are already correctly diagnosed in the packet’s own accepted-amendments section.

Bottom line: the post-L4 terrain is close to cleared, and the actual telescoping/bookkeeping arguments are good. But the official packet still has enough statement/proof mismatch that it should **not** be accepted as-is. Accept it after rewriting L5, L7, L8, the dependency spine, and the glue so they match the proofs actually given.

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_03.md

# Reviewer Output

Generated: 2026-03-23T06:46:57.253920+00:00

VERDICT: PATCH_BIG

The pass gets the main meta-level judgment right: it does **not** overclaim the open theorem, and it correctly localizes the unresolved mass in L1 through L4, especially L4. That is consistent with the route packet, the durable claim source, and the durable proof-state anchor, all of which still treat the theorem as open/bootstrap rather than solved.

**L5.** The recursion proof is logically sound **after** the stated repair. The finite-level induction, the choice of a root bias from (B_\delta((s),v^s)), the successor assignment, and the unique-predecessor consistency check are all fine. But the official L5 statement in the breakdown is **not** what is proved. The proof needs L2 for root-bias nonemptiness, and it needs the selector on the **full rooted public-history tree**, not merely on “reachable” on-path histories. [SCOPE] This is a genuine statement change, not a cosmetic edit.

**L6.** The proof is valid for the **literal text only**. The constant normal-mode construction really does satisfy the four displayed clauses, with clause 2 vacuous because (M_t=i) never occurs. So the derivation is logically valid, but the lemma is semantically much weaker than its technique hint and weaker than the punishment narrative advertised in the route packet. [SCOPE] If punishment mode is supposed to be usable rather than vacuous, the public state has to remember the punishment anchor history, or an equivalent public encoding of it.

**L7 / L7′.** The telescoping proof of **L7′** is mathematically sound. The bias process is bounded via L2, the on-path inequality gives the lower bound, the unilateral-deviation inequality gives the upper bound, mixed deviations are handled by affine averaging over pure actions, and the bias terms telescope to an (O(1/T)) remainder. But the original **L7** is not proved from its own displayed dependencies as written. The proof actually uses L2, the strengthened full-tree form of L5, and a root-specific profile (\sigma^s), whereas the breakdown lists only L4-L6 and states the lemma for (\sigma^\varepsilon). There is also a small but real notation/assembly gap in the corollary back to original L7: one must explicitly identify the global profile (\sigma^\varepsilon) with the root-assembled profile satisfying (\sigma^\varepsilon(h)=x^{\mathrm{root}(h)}(h)). That identification is available from the literal L6 construction, but it is not written into the corollary step.

**L8 / L8′.** The bookkeeping is correct once (\eta_t\ge 0) is made explicit. The proof uses nonnegativity in an essential way, so that sign condition has to be part of the formal assumptions rather than an informal aside. A second notation gap remains in **L8′**: the statement and proof are written for (\sigma^\varepsilon), but L7′ is a lemma about (\sigma^s). Again, a one-line global assembly step fixes this, but it must be stated explicitly.

[SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

The citation problem here is mainly a **logical-dependency citation** problem, not a bibliographic one. L5 must cite L2. Original L7 must cite L2 and the strengthened L5. L8 must cite the added assumption (\eta_t\ge 0). Also, the shortened post-L4 spine still needs an explicit global-assembly glue step from the family ({\sigma^s}_{s\in S}) to one profile on the whole game. So the clean corrected backbone is not quite `L1→L2→L3→L4→L5→L7′→L8′→Theorem`; it is `L1→L2→L3→L4→L5→(global assembly)→L7′→L8′→Theorem`, with L6 demoted unless punishments are restored non-vacuously. Most of these repairs are already correctly diagnosed in the packet’s own accepted-amendments section.

Bottom line: the post-L4 terrain is close to cleared, and the actual telescoping/bookkeeping arguments are good. But the official packet still has enough statement/proof mismatch that it should **not** be accepted as-is. Accept it after rewriting L5, L7, L8, the dependency spine, and the glue so they match the proofs actually given.

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/strategy.md

# Searcher Output

Generated: 2026-03-23T02:57:22.330720+00:00

## Selected Route
**Martin-function bootstrap to a global Nash selector.**

## Route Details
**Core technique:** Avoid discounted asymptotics entirely. Work directly on public histories using the Martin function to define a continuation correspondence of minmax-safe promises, then try to select at each history a mixed action and next promise that satisfy a one-step incentive inequality. Existing Martin-function machinery already gives subgame (\varepsilon)-maxmin strategies, minmax (\varepsilon)-acceptable profiles, extensive-form correlated (\varepsilon)-equilibria, and an (\varepsilon)-solvable subgame, while explicitly relying on a deviation-detection ingredient for nonstationary play.
   **Key intermediate steps:** Define a correspondence (W(h)) of continuation payoffs attainable from each public history (h) while keeping everyone above minmax. Prove a one-step self-generation property: for each (w\in W(h)), there is an uncorrelated mixed action profile (x(h)) and a continuation assignment (h'\mapsto w(h')\in W(h')) such that current promise is bounded by current payoff plus expected next promise plus a tiny leakage (\eta(h)). Then choose a measurable public-history selector and use public monitoring to identify a deviator and switch to a history-indexed punishment plan. Finally, telescope the promise inequalities over (T) stages so all leakage sums to at most (\varepsilon), uniformly in the initial state.
   **Likely failure point:** This route is allergic to missing convexity. The known Martin-function results produce individually rational profiles, correlated equilibria, or equilibrium in some subgame, but not yet a single uncorrelated profile across all histories and states. The one-step self-generation property needed here may simply be another mask worn by the open problem.
   **Complexity estimate:** Extreme to brutal. Conceptually cleaner than Route 1, but it demands a genuinely new selector theorem on the history tree.

---
## OTHER AVAILABLE FILES (not loaded; request by name if needed)

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md` (107 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (8902 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_01.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_02.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_03.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

