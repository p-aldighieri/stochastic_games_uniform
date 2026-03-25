# External Agent Request (reviewer)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T20:14:47.831577+00:00

## Instructions

Check each proof step for logical validity, completeness, and correct citations. Check scope compliance. Issue a structured verdict: VERDICT: PASS (correct and complete), VERDICT: PATCH_SMALL (minor fixable issues), VERDICT: PATCH_BIG (needs restructuring), or VERDICT: REDO (fundamentally flawed approach). Be precise about errors. Tag scope changes with [SCOPE].

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

## Accepted Amendments
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
- Use the corrected post-L4 backbone
- The proof above establishes only the literal displayed statement of L6. It does **not** build a non-vacuous punishment-mode mechanism. Any stronger “switch to a punishment plan anchored at a remembered history” reading remains unproved unless the public state is enriched to remember that anchor.
- Replace the old L7 by the following corrected version.
- Replace L8 by the following corrected version, which explicitly cites the standing hypothesis (\eta_t\ge0).
- The remaining gap is now cleanly localized. L1 and L2 remain imported. L4 remains the unresolved selector theorem. Everything after L4 is tree recursion plus telescoping bookkeeping.

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

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_01.md

# Prover Output

Generated: 2026-03-23T06:25:36.582593+00:00

## Status summary

* [ASSUMPTION+] For the parameter-closing step I make explicit that the leakage schedule satisfies (\eta_t\ge 0) for all (t). This is needed for the monotone partial-sum bounds used in L8.
* [DERIVED] L5 is provable by explicit recursion on the rooted public-history tree, once one adds the missing root-bias nonemptiness input from L2.
* [DERIVED] L6 is literally provable as stated, via a constant normal-mode implementation. This proves the written statement, but only in a weak, vacuous-on-punishment sense.
* [DERIVED] A sharper version of L7 is provable directly from L4 and L5, together with the bias bound from L2. In that sharper form, the punishment machinery is not used in the verification step, and the (\pm 2\delta) slack disappears.
* [DERIVED] L8 is pure bookkeeping and is proved. The sharper L7 also yields a sharper L8.
* [BREAKDOWN_AMEND] The real obstruction remains L4. Everything below L4 is bookkeeping/telescoping once the selector exists. The project status remains bootstrap, and the universal theorem is still open.   

## Lemma L5, global selector on the rooted public-history tree

[BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.

[BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.

### Proof

Fix an initial state (s\in S) and a chosen root target (v^s\in W_\delta((s))).

For each (t\ge 1), let (\mathcal H_t(s)) be the set of public histories of length (t) whose first state is (s).

1. (\mathcal H_1(s)={(s)}), so (\mathcal H_1(s)) is finite.

2. Suppose (\mathcal H_t(s)) is finite. For each (h\in\mathcal H_t(s)), the terminal state is (s(h)), the action set (A(s(h))=\prod_{j\in N}A_j(s(h))) is finite because each (A_j(s(h))) is finite, and (S) is finite. Hence (h) has only finitely many one-step extensions (h[a,s']) with (a\in A(s(h))) and (s'\in S). Therefore
   [
   \mathcal H_{t+1}(s)
   ===================

   \bigcup_{h\in\mathcal H_t(s)}
   {,h[a,s'] : a\in A(s(h)),\ s'\in S,}
   ]
   is finite.

3. By induction on (t), every level (\mathcal H_t(s)) is finite. Therefore the rooted public-history tree
   [
   \mathcal H(s):=\bigcup_{t\ge 1}\mathcal H_t(s)
   ]
   is countable, being a countable union of finite sets.

4. By L2, (B_\delta((s),v^s)) is nonempty. Choose
   [
   \beta((s))\in B_\delta((s),v^s).
   ]

5. Apply L4 at the root history ((s)), with target (v^s) and bias (\beta((s))). L4 yields:

   * a product mixed action
     [
     x((s))\in \prod_{j\in N}\Delta(A_j(s)),
     ]
   * and for every action profile (a\in A(s)) and next state (s'\in S), a successor bias
     [
     \beta^{(s),a,s'}\in B_\delta((s)[a,s'],v^s).
     ]
     Define
     [
     \beta((s)[a,s']) := \beta^{(s),a,s'}.
     ]

6. Inductive step. Assume that for some (t\ge 1), (\beta(h)\in B_\delta(h,v^s)) has already been defined for every (h\in \mathcal H_t(s)). Since (\mathcal H_t(s)) is finite, we may process each such (h) one by one.

   For each (h\in\mathcal H_t(s)), apply L4 to ((h,v^s,\beta(h))). L4 yields:

   * a product mixed action
     [
     x(h)\in \prod_{j\in N}\Delta(A_j(s(h))),
     ]
   * and for every (a\in A(s(h))), (s'\in S), a successor bias
     [
     \beta^{h,a,s'}\in B_\delta(h[a,s'],v^s).
     ]
     Define
     [
     \beta(h[a,s']) := \beta^{h,a,s'}.
     ]

7. This recursive definition is consistent because every nonroot public history has a unique immediate predecessor, namely the history obtained by deleting its last action profile and final state. Hence no successor bias is assigned twice from two different parents.

8. By induction over all levels (t), (\beta(h)) and (x(h)) are defined for every (h\in\mathcal H(s)). By construction:

   * (\beta(h)\in B_\delta(h,v^s)) for every (h),
   * (x(h)\in \prod_{j\in N}\Delta(A_j(s(h)))) for every (h),
   * the L4 inequalities hold at each (h),
   * and every successor history inherits the same target (v^s), because each successor bias was chosen in (B_\delta(h[a,s'],v^s)).

[DERIVED] L5 is proved, conditional on the dependency/scope repairs above.

## Lemma L6, literal implementation

[BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.

### Proof of the literal statement

Assume L1 and the family of L5 selectors ({x^s,\beta^s}_{s\in S}), one selector for each chosen root target (v^s).

For any nonempty public history
[
h=(s_1,a_1,s_2,\dots,s_t),
]
write (\mathrm{root}(h):=s_1).

Define a behavioral profile (\sigma^\varepsilon\in\Sigma(G)) by
[
\sigma_i^\varepsilon(h):=x_i^{\mathrm{root}(h)}(h).
]
This is well-defined because every public history has a unique first state, and by L5,
[
x_i^{\mathrm{root}(h)}(h)\in \Delta(A_i(s(h))).
]
Hence (\sigma_i^\varepsilon) is a behavioral strategy for player (i).

Define the public mode process by the constant rule
[
M_t \equiv \mathrm{normal}
\quad\text{for all }t.
]

Now verify the four clauses.

1. If (M_t=\mathrm{normal}), players use the selector action from L5. This holds by construction, since (M_t) is always normal and (\sigma^\varepsilon(h_t)=x^{\mathrm{root}(h_t)}(h_t)).

2. If (M_t=i), players use the punishment continuation (p^{i,h_t}). This clause is vacuously true because (M_t=i) never occurs.

3. The update rule for (M_t) depends only on the public history and the deviation-detection ingredient. A constant rule depends on neither, so in particular it is a deterministic function of the public history alone, hence also of any larger input tuple that includes a deviation-detection signal.

4. For each initial state (s), the profile enters normal mode with root target (v^s) and preserves that same target along normal-mode successor histories. This follows because histories whose first state is (s) are governed by the L5 selector built from (v^s), and L5 preserves that target at every successor.

[DERIVED] The literal L6 is proved.

[BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.

## Sharpened Lemma L7′, telescoping without punishments

[BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).

### Statement

Assume L4 and the strengthened form of L5 proved above on the full rooted public-history tree. Fix an initial state (s), choose a root target (v^s\in W_\delta((s))), and let (x^s,\beta^s) be the selector given by L5. Let (\sigma^s) be the behavioral profile defined on histories rooted at (s) by
[
\sigma^s(h)=x^s(h).
]
Then for every player (i), every unilateral deviation (\tau_i\in\Sigma_i(G)), and every horizon (T\ge 1),
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Consequently,
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

### Proof

Fix (i), (s), (\tau_i), and (T). Let
[
h_1=(s),
\qquad
h_{t+1}=h_t[a_t,s_{t+1}]
\quad (1\le t\le T),
]
under whichever probability law is currently under discussion. Define
[
Y_t := \beta_i^s(h_t)
\quad (1\le t\le T+1).
]
Because L5 gives (\beta^s(h_t)\in B_\delta(h_t,v^s)), the uniform bias bound in L2 yields
[
|Y_t|\le C_\delta
\quad\text{almost surely for every }t.
]

### Part A, payoff of (\sigma^s)

Condition on the current public history (h_t). Under (\sigma^s), the stage-(t) action profile (a_t) is sampled from (x^s(h_t)), and the next state is sampled from (P(\cdot\mid s(h_t),a_t)). Therefore, by direct computation of conditional expectation,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
==============================================================

\sum_{a}x^s(h_t)(a)\Bigl(
u_i(s(h_t),a)
+
\sum_{s'}P(s'\mid s(h_t),a),\beta_i^s(h_t[a,s'])
\Bigr).
]
By L5, the selector at (h_t) satisfies the L4 inequality with target (v^s). Hence
[
v_i^s + Y_t
\le
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
+\eta_t.
]
Rearranging,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)\mid h_t\right]
\ge
v_i^s + Y_t - \mathbb E_{\sigma^s}[Y_{t+1}\mid h_t] - \eta_t.
]
Take full expectations:
[
\mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
v_i^s + \mathbb E_{\sigma^s}[Y_t-Y_{t+1}] - \eta_t.
]
Sum from (t=1) to (T):
[
\sum_{t=1}^T \mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
T v_i^s + \mathbb E_{\sigma^s}[Y_1-Y_{T+1}] - \sum_{t=1}^T \eta_t.
]
Since (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta),
[
\mathbb E_{\sigma^s}[Y_1-Y_{T+1}] \ge -2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t.
]

### Part B, payoff of an arbitrary unilateral deviation

Now consider the profile ((\tau_i,\sigma^s_{-i})). Conditional on (h_t), let
[
\alpha_t(\cdot\mid h_t)\in \Delta(A_i(s(h_t)))
]
be the mixed action used by the deviator at stage (t). Because the opponents still use the product distribution (x^s_{-i}(h_t)), direct computation gives
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
============================================================================

\sum_{a_i'}\alpha_t(a_i'\mid h_t)
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr).
]
For each pure action (a_i'), L4 gives
[
v_i^s + Y_t
\ge
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr)
-\eta_t.
]
The right-hand side is affine in (a_i'). Averaging with respect to (\alpha_t(\cdot\mid h_t)) preserves the inequality, so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
\le
v_i^s + Y_t + \eta_t.
]
Therefore
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_t-Y_{t+1}] + \eta_t.
]
Summing from (t=1) to (T),
[
\sum_{t=1}^T \mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
T v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] + \sum_{t=1}^T \eta_t.
]
Again (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta), so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] \le 2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]

Subtract the lower bound from the upper bound to get
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

[DERIVED] L7′ is proved.

### Corollary, the stated L7

Because (\delta>0), one has (2\delta\ge 0). Therefore the lower bound
[
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s-2\delta-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and the upper bound
[
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s+2\delta+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Hence the displayed inequalities of the original L7 follow immediately.

[DERIVED] L7 is proved, and in fact sharpened.

[BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.

## Lemma L8, original parameter closing

### Proof

Assume L7 and the explicit sign assumption (\eta_t\ge 0).

Fix (T\ge T_0), an initial state (s), a player (i), and a unilateral deviation (\tau_i). By L7,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
4\delta+\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Since (T\ge T_0) and (T_0\ge 8C_\delta/\varepsilon),
[
\frac{4C_\delta}{T}\le \frac{4C_\delta}{T_0}\le \frac{\varepsilon}{2}.
]
Because (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
2\sum_{t=1}^T\eta_t
\le
2\sum_{t\ge 1}\eta_t.
]
Hence, using the parameter condition
[
4\delta+2\sum_{t\ge 1}\eta_t\le \frac{\varepsilon}{2},
]
we obtain
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
===========================================

\varepsilon.
]
Equivalently,
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon.
]
Since this holds for every (T\ge T_0), every (s\in S), every (i\in N), and every unilateral deviation (\tau_i), (\sigma^\varepsilon) is a uniform (\varepsilon)-equilibrium.

[DERIVED] L8 is proved.

## Sharpened Lemma L8′ from L7′

[BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.

### Statement

Assume L7′ and (\eta_t\ge 0). Choose any integer (T_0) such that
[
T_0 \ge \frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{\varepsilon}.
]
Then for every (T\ge T_0),
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon
]
for all initial states (s), players (i), and unilateral deviations (\tau_i).

### Proof

By L7′,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Using (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
\frac{2}{T}\sum_{t\ge 1}\eta_t.
]
Hence
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T}
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T_0}
\le
\varepsilon.
]
So the same uniform (\varepsilon)-equilibrium conclusion follows.

[DERIVED] L8′ is proved.

## Net effect on the route

[BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
[
L1 \to L2 \to L3 \to L4 \to L5 \to L7' \to L8' \to \text{Theorem}.
]
L6 becomes optional bookkeeping rather than a proof-critical lemma.

[DERIVED] Current lemma status:

* L1: open.
* L2: open.
* L3: open.
* L4: open, and still the critical obstruction.
* L5: proved conditionally, after the stated dependency/scope repair.
* L6: literal statement proved, but too weak to matter once L7′ is used.
* L7: proved, and sharpened to L7′.
* L8: proved, and sharpened to L8′.

[DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_02.md

# Prover Output

Generated: 2026-03-23T06:46:57.206553+00:00

## Status summary

* [ASSUMPTION+] For the parameter-closing step I make explicit that the leakage schedule satisfies (\eta_t\ge 0) for all (t). This is needed for the monotone partial-sum bounds used in L8.
* [DERIVED] L5 is provable by explicit recursion on the rooted public-history tree, once one adds the missing root-bias nonemptiness input from L2.
* [DERIVED] L6 is literally provable as stated, via a constant normal-mode implementation. This proves the written statement, but only in a weak, vacuous-on-punishment sense.
* [DERIVED] A sharper version of L7 is provable directly from L4 and L5, together with the bias bound from L2. In that sharper form, the punishment machinery is not used in the verification step, and the (\pm 2\delta) slack disappears.
* [DERIVED] L8 is pure bookkeeping and is proved. The sharper L7 also yields a sharper L8.
* [BREAKDOWN_AMEND] The real obstruction remains L4. Everything below L4 is bookkeeping/telescoping once the selector exists. The project status remains bootstrap, and the universal theorem is still open.   

## Lemma L5, global selector on the rooted public-history tree

[BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.

[BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.

### Proof

Fix an initial state (s\in S) and a chosen root target (v^s\in W_\delta((s))).

For each (t\ge 1), let (\mathcal H_t(s)) be the set of public histories of length (t) whose first state is (s).

1. (\mathcal H_1(s)={(s)}), so (\mathcal H_1(s)) is finite.

2. Suppose (\mathcal H_t(s)) is finite. For each (h\in\mathcal H_t(s)), the terminal state is (s(h)), the action set (A(s(h))=\prod_{j\in N}A_j(s(h))) is finite because each (A_j(s(h))) is finite, and (S) is finite. Hence (h) has only finitely many one-step extensions (h[a,s']) with (a\in A(s(h))) and (s'\in S). Therefore
   [
   \mathcal H_{t+1}(s)
   ===================

   \bigcup_{h\in\mathcal H_t(s)}
   {,h[a,s'] : a\in A(s(h)),\ s'\in S,}
   ]
   is finite.

3. By induction on (t), every level (\mathcal H_t(s)) is finite. Therefore the rooted public-history tree
   [
   \mathcal H(s):=\bigcup_{t\ge 1}\mathcal H_t(s)
   ]
   is countable, being a countable union of finite sets.

4. By L2, (B_\delta((s),v^s)) is nonempty. Choose
   [
   \beta((s))\in B_\delta((s),v^s).
   ]

5. Apply L4 at the root history ((s)), with target (v^s) and bias (\beta((s))). L4 yields:

   * a product mixed action
     [
     x((s))\in \prod_{j\in N}\Delta(A_j(s)),
     ]
   * and for every action profile (a\in A(s)) and next state (s'\in S), a successor bias
     [
     \beta^{(s),a,s'}\in B_\delta((s)[a,s'],v^s).
     ]
     Define
     [
     \beta((s)[a,s']) := \beta^{(s),a,s'}.
     ]

6. Inductive step. Assume that for some (t\ge 1), (\beta(h)\in B_\delta(h,v^s)) has already been defined for every (h\in \mathcal H_t(s)). Since (\mathcal H_t(s)) is finite, we may process each such (h) one by one.

   For each (h\in\mathcal H_t(s)), apply L4 to ((h,v^s,\beta(h))). L4 yields:

   * a product mixed action
     [
     x(h)\in \prod_{j\in N}\Delta(A_j(s(h))),
     ]
   * and for every (a\in A(s(h))), (s'\in S), a successor bias
     [
     \beta^{h,a,s'}\in B_\delta(h[a,s'],v^s).
     ]
     Define
     [
     \beta(h[a,s']) := \beta^{h,a,s'}.
     ]

7. This recursive definition is consistent because every nonroot public history has a unique immediate predecessor, namely the history obtained by deleting its last action profile and final state. Hence no successor bias is assigned twice from two different parents.

8. By induction over all levels (t), (\beta(h)) and (x(h)) are defined for every (h\in\mathcal H(s)). By construction:

   * (\beta(h)\in B_\delta(h,v^s)) for every (h),
   * (x(h)\in \prod_{j\in N}\Delta(A_j(s(h)))) for every (h),
   * the L4 inequalities hold at each (h),
   * and every successor history inherits the same target (v^s), because each successor bias was chosen in (B_\delta(h[a,s'],v^s)).

[DERIVED] L5 is proved, conditional on the dependency/scope repairs above.

## Lemma L6, literal implementation

[BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.

### Proof of the literal statement

Assume L1 and the family of L5 selectors ({x^s,\beta^s}_{s\in S}), one selector for each chosen root target (v^s).

For any nonempty public history
[
h=(s_1,a_1,s_2,\dots,s_t),
]
write (\mathrm{root}(h):=s_1).

Define a behavioral profile (\sigma^\varepsilon\in\Sigma(G)) by
[
\sigma_i^\varepsilon(h):=x_i^{\mathrm{root}(h)}(h).
]
This is well-defined because every public history has a unique first state, and by L5,
[
x_i^{\mathrm{root}(h)}(h)\in \Delta(A_i(s(h))).
]
Hence (\sigma_i^\varepsilon) is a behavioral strategy for player (i).

Define the public mode process by the constant rule
[
M_t \equiv \mathrm{normal}
\quad\text{for all }t.
]

Now verify the four clauses.

1. If (M_t=\mathrm{normal}), players use the selector action from L5. This holds by construction, since (M_t) is always normal and (\sigma^\varepsilon(h_t)=x^{\mathrm{root}(h_t)}(h_t)).

2. If (M_t=i), players use the punishment continuation (p^{i,h_t}). This clause is vacuously true because (M_t=i) never occurs.

3. The update rule for (M_t) depends only on the public history and the deviation-detection ingredient. A constant rule depends on neither, so in particular it is a deterministic function of the public history alone, hence also of any larger input tuple that includes a deviation-detection signal.

4. For each initial state (s), the profile enters normal mode with root target (v^s) and preserves that same target along normal-mode successor histories. This follows because histories whose first state is (s) are governed by the L5 selector built from (v^s), and L5 preserves that target at every successor.

[DERIVED] The literal L6 is proved.

[BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.

## Sharpened Lemma L7′, telescoping without punishments

[BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).

### Statement

Assume L4 and the strengthened form of L5 proved above on the full rooted public-history tree. Fix an initial state (s), choose a root target (v^s\in W_\delta((s))), and let (x^s,\beta^s) be the selector given by L5. Let (\sigma^s) be the behavioral profile defined on histories rooted at (s) by
[
\sigma^s(h)=x^s(h).
]
Then for every player (i), every unilateral deviation (\tau_i\in\Sigma_i(G)), and every horizon (T\ge 1),
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Consequently,
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

### Proof

Fix (i), (s), (\tau_i), and (T). Let
[
h_1=(s),
\qquad
h_{t+1}=h_t[a_t,s_{t+1}]
\quad (1\le t\le T),
]
under whichever probability law is currently under discussion. Define
[
Y_t := \beta_i^s(h_t)
\quad (1\le t\le T+1).
]
Because L5 gives (\beta^s(h_t)\in B_\delta(h_t,v^s)), the uniform bias bound in L2 yields
[
|Y_t|\le C_\delta
\quad\text{almost surely for every }t.
]

### Part A, payoff of (\sigma^s)

Condition on the current public history (h_t). Under (\sigma^s), the stage-(t) action profile (a_t) is sampled from (x^s(h_t)), and the next state is sampled from (P(\cdot\mid s(h_t),a_t)). Therefore, by direct computation of conditional expectation,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
==============================================================

\sum_{a}x^s(h_t)(a)\Bigl(
u_i(s(h_t),a)
+
\sum_{s'}P(s'\mid s(h_t),a),\beta_i^s(h_t[a,s'])
\Bigr).
]
By L5, the selector at (h_t) satisfies the L4 inequality with target (v^s). Hence
[
v_i^s + Y_t
\le
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
+\eta_t.
]
Rearranging,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)\mid h_t\right]
\ge
v_i^s + Y_t - \mathbb E_{\sigma^s}[Y_{t+1}\mid h_t] - \eta_t.
]
Take full expectations:
[
\mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
v_i^s + \mathbb E_{\sigma^s}[Y_t-Y_{t+1}] - \eta_t.
]
Sum from (t=1) to (T):
[
\sum_{t=1}^T \mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
T v_i^s + \mathbb E_{\sigma^s}[Y_1-Y_{T+1}] - \sum_{t=1}^T \eta_t.
]
Since (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta),
[
\mathbb E_{\sigma^s}[Y_1-Y_{T+1}] \ge -2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t.
]

### Part B, payoff of an arbitrary unilateral deviation

Now consider the profile ((\tau_i,\sigma^s_{-i})). Conditional on (h_t), let
[
\alpha_t(\cdot\mid h_t)\in \Delta(A_i(s(h_t)))
]
be the mixed action used by the deviator at stage (t). Because the opponents still use the product distribution (x^s_{-i}(h_t)), direct computation gives
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
============================================================================

\sum_{a_i'}\alpha_t(a_i'\mid h_t)
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr).
]
For each pure action (a_i'), L4 gives
[
v_i^s + Y_t
\ge
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr)
-\eta_t.
]
The right-hand side is affine in (a_i'). Averaging with respect to (\alpha_t(\cdot\mid h_t)) preserves the inequality, so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
\le
v_i^s + Y_t + \eta_t.
]
Therefore
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_t-Y_{t+1}] + \eta_t.
]
Summing from (t=1) to (T),
[
\sum_{t=1}^T \mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
T v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] + \sum_{t=1}^T \eta_t.
]
Again (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta), so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] \le 2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]

Subtract the lower bound from the upper bound to get
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

[DERIVED] L7′ is proved.

### Corollary, the stated L7

Because (\delta>0), one has (2\delta\ge 0). Therefore the lower bound
[
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s-2\delta-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and the upper bound
[
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s+2\delta+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Hence the displayed inequalities of the original L7 follow immediately.

[DERIVED] L7 is proved, and in fact sharpened.

[BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.

## Lemma L8, original parameter closing

### Proof

Assume L7 and the explicit sign assumption (\eta_t\ge 0).

Fix (T\ge T_0), an initial state (s), a player (i), and a unilateral deviation (\tau_i). By L7,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
4\delta+\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Since (T\ge T_0) and (T_0\ge 8C_\delta/\varepsilon),
[
\frac{4C_\delta}{T}\le \frac{4C_\delta}{T_0}\le \frac{\varepsilon}{2}.
]
Because (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
2\sum_{t=1}^T\eta_t
\le
2\sum_{t\ge 1}\eta_t.
]
Hence, using the parameter condition
[
4\delta+2\sum_{t\ge 1}\eta_t\le \frac{\varepsilon}{2},
]
we obtain
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
===========================================

\varepsilon.
]
Equivalently,
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon.
]
Since this holds for every (T\ge T_0), every (s\in S), every (i\in N), and every unilateral deviation (\tau_i), (\sigma^\varepsilon) is a uniform (\varepsilon)-equilibrium.

[DERIVED] L8 is proved.

## Sharpened Lemma L8′ from L7′

[BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.

### Statement

Assume L7′ and (\eta_t\ge 0). Choose any integer (T_0) such that
[
T_0 \ge \frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{\varepsilon}.
]
Then for every (T\ge T_0),
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon
]
for all initial states (s), players (i), and unilateral deviations (\tau_i).

### Proof

By L7′,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Using (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
\frac{2}{T}\sum_{t\ge 1}\eta_t.
]
Hence
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T}
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T_0}
\le
\varepsilon.
]
So the same uniform (\varepsilon)-equilibrium conclusion follows.

[DERIVED] L8′ is proved.

## Net effect on the route

[BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
[
L1 \to L2 \to L3 \to L4 \to L5 \to L7' \to L8' \to \text{Theorem}.
]
L6 becomes optional bookkeeping rather than a proof-critical lemma.

[DERIVED] Current lemma status:

* L1: open.
* L2: open.
* L3: open.
* L4: open, and still the critical obstruction.
* L5: proved conditionally, after the stated dependency/scope repair.
* L6: literal statement proved, but too weak to matter once L7′ is used.
* L7: proved, and sharpened to L7′.
* L8: proved, and sharpened to L8′.

[DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_03.md

# Prover Output

Generated: 2026-03-23T06:46:57.234847+00:00

## Status summary

* [ASSUMPTION+] For the parameter-closing step I make explicit that the leakage schedule satisfies (\eta_t\ge 0) for all (t). This is needed for the monotone partial-sum bounds used in L8.
* [DERIVED] L5 is provable by explicit recursion on the rooted public-history tree, once one adds the missing root-bias nonemptiness input from L2.
* [DERIVED] L6 is literally provable as stated, via a constant normal-mode implementation. This proves the written statement, but only in a weak, vacuous-on-punishment sense.
* [DERIVED] A sharper version of L7 is provable directly from L4 and L5, together with the bias bound from L2. In that sharper form, the punishment machinery is not used in the verification step, and the (\pm 2\delta) slack disappears.
* [DERIVED] L8 is pure bookkeeping and is proved. The sharper L7 also yields a sharper L8.
* [BREAKDOWN_AMEND] The real obstruction remains L4. Everything below L4 is bookkeeping/telescoping once the selector exists. The project status remains bootstrap, and the universal theorem is still open.   

## Lemma L5, global selector on the rooted public-history tree

[BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.

[BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.

### Proof

Fix an initial state (s\in S) and a chosen root target (v^s\in W_\delta((s))).

For each (t\ge 1), let (\mathcal H_t(s)) be the set of public histories of length (t) whose first state is (s).

1. (\mathcal H_1(s)={(s)}), so (\mathcal H_1(s)) is finite.

2. Suppose (\mathcal H_t(s)) is finite. For each (h\in\mathcal H_t(s)), the terminal state is (s(h)), the action set (A(s(h))=\prod_{j\in N}A_j(s(h))) is finite because each (A_j(s(h))) is finite, and (S) is finite. Hence (h) has only finitely many one-step extensions (h[a,s']) with (a\in A(s(h))) and (s'\in S). Therefore
   [
   \mathcal H_{t+1}(s)
   ===================

   \bigcup_{h\in\mathcal H_t(s)}
   {,h[a,s'] : a\in A(s(h)),\ s'\in S,}
   ]
   is finite.

3. By induction on (t), every level (\mathcal H_t(s)) is finite. Therefore the rooted public-history tree
   [
   \mathcal H(s):=\bigcup_{t\ge 1}\mathcal H_t(s)
   ]
   is countable, being a countable union of finite sets.

4. By L2, (B_\delta((s),v^s)) is nonempty. Choose
   [
   \beta((s))\in B_\delta((s),v^s).
   ]

5. Apply L4 at the root history ((s)), with target (v^s) and bias (\beta((s))). L4 yields:

   * a product mixed action
     [
     x((s))\in \prod_{j\in N}\Delta(A_j(s)),
     ]
   * and for every action profile (a\in A(s)) and next state (s'\in S), a successor bias
     [
     \beta^{(s),a,s'}\in B_\delta((s)[a,s'],v^s).
     ]
     Define
     [
     \beta((s)[a,s']) := \beta^{(s),a,s'}.
     ]

6. Inductive step. Assume that for some (t\ge 1), (\beta(h)\in B_\delta(h,v^s)) has already been defined for every (h\in \mathcal H_t(s)). Since (\mathcal H_t(s)) is finite, we may process each such (h) one by one.

   For each (h\in\mathcal H_t(s)), apply L4 to ((h,v^s,\beta(h))). L4 yields:

   * a product mixed action
     [
     x(h)\in \prod_{j\in N}\Delta(A_j(s(h))),
     ]
   * and for every (a\in A(s(h))), (s'\in S), a successor bias
     [
     \beta^{h,a,s'}\in B_\delta(h[a,s'],v^s).
     ]
     Define
     [
     \beta(h[a,s']) := \beta^{h,a,s'}.
     ]

7. This recursive definition is consistent because every nonroot public history has a unique immediate predecessor, namely the history obtained by deleting its last action profile and final state. Hence no successor bias is assigned twice from two different parents.

8. By induction over all levels (t), (\beta(h)) and (x(h)) are defined for every (h\in\mathcal H(s)). By construction:

   * (\beta(h)\in B_\delta(h,v^s)) for every (h),
   * (x(h)\in \prod_{j\in N}\Delta(A_j(s(h)))) for every (h),
   * the L4 inequalities hold at each (h),
   * and every successor history inherits the same target (v^s), because each successor bias was chosen in (B_\delta(h[a,s'],v^s)).

[DERIVED] L5 is proved, conditional on the dependency/scope repairs above.

## Lemma L6, literal implementation

[BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.

### Proof of the literal statement

Assume L1 and the family of L5 selectors ({x^s,\beta^s}_{s\in S}), one selector for each chosen root target (v^s).

For any nonempty public history
[
h=(s_1,a_1,s_2,\dots,s_t),
]
write (\mathrm{root}(h):=s_1).

Define a behavioral profile (\sigma^\varepsilon\in\Sigma(G)) by
[
\sigma_i^\varepsilon(h):=x_i^{\mathrm{root}(h)}(h).
]
This is well-defined because every public history has a unique first state, and by L5,
[
x_i^{\mathrm{root}(h)}(h)\in \Delta(A_i(s(h))).
]
Hence (\sigma_i^\varepsilon) is a behavioral strategy for player (i).

Define the public mode process by the constant rule
[
M_t \equiv \mathrm{normal}
\quad\text{for all }t.
]

Now verify the four clauses.

1. If (M_t=\mathrm{normal}), players use the selector action from L5. This holds by construction, since (M_t) is always normal and (\sigma^\varepsilon(h_t)=x^{\mathrm{root}(h_t)}(h_t)).

2. If (M_t=i), players use the punishment continuation (p^{i,h_t}). This clause is vacuously true because (M_t=i) never occurs.

3. The update rule for (M_t) depends only on the public history and the deviation-detection ingredient. A constant rule depends on neither, so in particular it is a deterministic function of the public history alone, hence also of any larger input tuple that includes a deviation-detection signal.

4. For each initial state (s), the profile enters normal mode with root target (v^s) and preserves that same target along normal-mode successor histories. This follows because histories whose first state is (s) are governed by the L5 selector built from (v^s), and L5 preserves that target at every successor.

[DERIVED] The literal L6 is proved.

[BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.

## Sharpened Lemma L7′, telescoping without punishments

[BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).

### Statement

Assume L4 and the strengthened form of L5 proved above on the full rooted public-history tree. Fix an initial state (s), choose a root target (v^s\in W_\delta((s))), and let (x^s,\beta^s) be the selector given by L5. Let (\sigma^s) be the behavioral profile defined on histories rooted at (s) by
[
\sigma^s(h)=x^s(h).
]
Then for every player (i), every unilateral deviation (\tau_i\in\Sigma_i(G)), and every horizon (T\ge 1),
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Consequently,
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

### Proof

Fix (i), (s), (\tau_i), and (T). Let
[
h_1=(s),
\qquad
h_{t+1}=h_t[a_t,s_{t+1}]
\quad (1\le t\le T),
]
under whichever probability law is currently under discussion. Define
[
Y_t := \beta_i^s(h_t)
\quad (1\le t\le T+1).
]
Because L5 gives (\beta^s(h_t)\in B_\delta(h_t,v^s)), the uniform bias bound in L2 yields
[
|Y_t|\le C_\delta
\quad\text{almost surely for every }t.
]

### Part A, payoff of (\sigma^s)

Condition on the current public history (h_t). Under (\sigma^s), the stage-(t) action profile (a_t) is sampled from (x^s(h_t)), and the next state is sampled from (P(\cdot\mid s(h_t),a_t)). Therefore, by direct computation of conditional expectation,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
==============================================================

\sum_{a}x^s(h_t)(a)\Bigl(
u_i(s(h_t),a)
+
\sum_{s'}P(s'\mid s(h_t),a),\beta_i^s(h_t[a,s'])
\Bigr).
]
By L5, the selector at (h_t) satisfies the L4 inequality with target (v^s). Hence
[
v_i^s + Y_t
\le
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
+\eta_t.
]
Rearranging,
[
\mathbb E_{\sigma^s}!\left[u_i(s_t,a_t)\mid h_t\right]
\ge
v_i^s + Y_t - \mathbb E_{\sigma^s}[Y_{t+1}\mid h_t] - \eta_t.
]
Take full expectations:
[
\mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
v_i^s + \mathbb E_{\sigma^s}[Y_t-Y_{t+1}] - \eta_t.
]
Sum from (t=1) to (T):
[
\sum_{t=1}^T \mathbb E_{\sigma^s}[u_i(s_t,a_t)]
\ge
T v_i^s + \mathbb E_{\sigma^s}[Y_1-Y_{T+1}] - \sum_{t=1}^T \eta_t.
]
Since (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta),
[
\mathbb E_{\sigma^s}[Y_1-Y_{T+1}] \ge -2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,\sigma^s)
\ge
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t.
]

### Part B, payoff of an arbitrary unilateral deviation

Now consider the profile ((\tau_i,\sigma^s_{-i})). Conditional on (h_t), let
[
\alpha_t(\cdot\mid h_t)\in \Delta(A_i(s(h_t)))
]
be the mixed action used by the deviator at stage (t). Because the opponents still use the product distribution (x^s_{-i}(h_t)), direct computation gives
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
============================================================================

\sum_{a_i'}\alpha_t(a_i'\mid h_t)
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr).
]
For each pure action (a_i'), L4 gives
[
v_i^s + Y_t
\ge
\sum_{a_{-i}}x^s_{-i}(h_t)(a_{-i})
\Bigl(
u_i(s(h_t),(a_i',a_{-i}))
+
\sum_{s'}P(s'\mid s(h_t),(a_i',a_{-i})),\beta_i^s(h_t[(a_i',a_{-i}),s'])
\Bigr)
-\eta_t.
]
The right-hand side is affine in (a_i'). Averaging with respect to (\alpha_t(\cdot\mid h_t)) preserves the inequality, so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}!\left[u_i(s_t,a_t)+Y_{t+1}\mid h_t\right]
\le
v_i^s + Y_t + \eta_t.
]
Therefore
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_t-Y_{t+1}] + \eta_t.
]
Summing from (t=1) to (T),
[
\sum_{t=1}^T \mathbb E_{(\tau_i,\sigma^s_{-i})}[u_i(s_t,a_t)]
\le
T v_i^s + \mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] + \sum_{t=1}^T \eta_t.
]
Again (|Y_1|\le C_\delta) and (|Y_{T+1}|\le C_\delta), so
[
\mathbb E_{(\tau_i,\sigma^s_{-i})}[Y_1-Y_{T+1}] \le 2C_\delta.
]
Divide by (T):
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
\le
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]

Subtract the lower bound from the upper bound to get
[
\gamma_i^T(G,s,(\tau_i,\sigma^s_{-i}))
--------------------------------------

\gamma_i^T(G,s,\sigma^s)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T \eta_t.
]

[DERIVED] L7′ is proved.

### Corollary, the stated L7

Because (\delta>0), one has (2\delta\ge 0). Therefore the lower bound
[
v_i^s-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s-2\delta-\frac{2C_\delta}{T}-\frac1T\sum_{t=1}^T \eta_t,
]
and the upper bound
[
v_i^s+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t
]
is stronger than
[
v_i^s+2\delta+\frac{2C_\delta}{T}+\frac1T\sum_{t=1}^T \eta_t.
]
Hence the displayed inequalities of the original L7 follow immediately.

[DERIVED] L7 is proved, and in fact sharpened.

[BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.

## Lemma L8, original parameter closing

### Proof

Assume L7 and the explicit sign assumption (\eta_t\ge 0).

Fix (T\ge T_0), an initial state (s), a player (i), and a unilateral deviation (\tau_i). By L7,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
4\delta+\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Since (T\ge T_0) and (T_0\ge 8C_\delta/\varepsilon),
[
\frac{4C_\delta}{T}\le \frac{4C_\delta}{T_0}\le \frac{\varepsilon}{2}.
]
Because (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
2\sum_{t=1}^T\eta_t
\le
2\sum_{t\ge 1}\eta_t.
]
Hence, using the parameter condition
[
4\delta+2\sum_{t\ge 1}\eta_t\le \frac{\varepsilon}{2},
]
we obtain
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
===========================================

\varepsilon.
]
Equivalently,
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon.
]
Since this holds for every (T\ge T_0), every (s\in S), every (i\in N), and every unilateral deviation (\tau_i), (\sigma^\varepsilon) is a uniform (\varepsilon)-equilibrium.

[DERIVED] L8 is proved.

## Sharpened Lemma L8′ from L7′

[BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.

### Statement

Assume L7′ and (\eta_t\ge 0). Choose any integer (T_0) such that
[
T_0 \ge \frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{\varepsilon}.
]
Then for every (T\ge T_0),
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon
]
for all initial states (s), players (i), and unilateral deviations (\tau_i).

### Proof

By L7′,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Using (\eta_t\ge 0),
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
\frac{2}{T}\sum_{t\ge 1}\eta_t.
]
Hence
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T}
\le
\frac{4C_\delta + 2\sum_{t\ge 1}\eta_t}{T_0}
\le
\varepsilon.
]
So the same uniform (\varepsilon)-equilibrium conclusion follows.

[DERIVED] L8′ is proved.

## Net effect on the route

[BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
[
L1 \to L2 \to L3 \to L4 \to L5 \to L7' \to L8' \to \text{Theorem}.
]
L6 becomes optional bookkeeping rather than a proof-critical lemma.

[DERIVED] Current lemma status:

* L1: open.
* L2: open.
* L3: open.
* L4: open, and still the critical obstruction.
* L5: proved conditionally, after the stated dependency/scope repair.
* L6: literal statement proved, but too weak to matter once L7′ is used.
* L7: proved, and sharpened to L7′.
* L8: proved, and sharpened to L8′.

[DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_04.md

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

---
## ADDITIONAL LOADED FILES

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md

# Assumption Delta

- Added assumptions: 0
- Removed assumptions: 0
- Scope changes: 3
- Mode: semi_strict

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

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown_amendments.md` (5761 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (11165 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_01.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_02.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_03.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

