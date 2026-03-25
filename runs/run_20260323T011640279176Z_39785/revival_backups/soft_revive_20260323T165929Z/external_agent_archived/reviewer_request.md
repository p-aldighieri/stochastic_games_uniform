# External Agent Request (reviewer)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T06:46:57.253621+00:00

## Instructions

Check each proof step for logical validity, completeness, and correct citations. Check scope compliance. Issue a structured verdict: VERDICT: PASS (correct and complete), VERDICT: PATCH_SMALL (minor fixable issues), VERDICT: PATCH_BIG (needs restructuring), or VERDICT: REDO (fundamentally flawed approach). Be precise about errors. Tag scope changes with [SCOPE].

## Context

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown.md

# Breakdown Output

Generated: 2026-03-23T06:46:57.227466+00:00

## Route-2 breakdown: Martin-function bootstrap to a global Nash selector

The adopted target is the strategy-existence form of uniform (\varepsilon)-equilibrium for every finite stochastic game with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities required for every sufficiently large horizon and every initial state. The selected route is the Martin-function bootstrap to a global Nash selector on the public-history tree. Because the theorem is still open and the current proof state is bootstrap/clean-slate, the decomposition below is a proof-route plan, not a completed proof.   

**Dependency spine.**
[
L1 \to L2 \to L3 \to L4 \to L5 \to L6 \to L7 \to L8 \to \text{Theorem}.
]

[BREAKDOWN_AMEND:promise_model]

Fix (G\in\mathfrak G) and (\varepsilon>0). Choose parameters (\delta>0) and a summable leakage schedule ((\eta_t)*{t\ge 1}) with
[
8\delta+4\sum*{t\ge 1}\eta_t \le \varepsilon.
]
For a public history (h), write (s(h)) for its terminal state, (|h|) for its length, and (h[a,s']) for its one-step extension by action profile (a) and next state (s'). Write (G[h]) for the continuation game after (h).

For this route, package a continuation promise as a pair ((v,\beta)), where (v\in[0,1]^N) is a **fixed target average-payoff vector** carried from the root, and (\beta\in\mathbb R^N) is a bounded Martin bias vector. The same (v) must survive through successor histories; (\beta) is the telescoping term that will wash out like foam at horizon scale (1/T).

### 1. [BREAKDOWN_AMEND:L1] Public-history minmax values and punishments

**Precise statement.**
For every public history (h) and player (i), there exists a number (m_i(h)\in[0,1]) and a continuation punishment profile (p^{i,h}\in \Sigma(G[h])) such that for every (\zeta>0) there exists (T_1(h,i,\zeta)) with
[
\forall T\ge T_1(h,i,\zeta),\ \forall \tau_i\in\Sigma_i(G[h]),\qquad
\gamma_i^T(G[h],(\tau_i,p^{i,h}*{-i})) \le m_i(h)+\zeta.
]
Moreover player (i) has a continuation strategy (\hat p^{i,h}*i) securing
[
\forall T\ge T_1(h,i,\zeta),\ \forall \rho*{-i}\in\Sigma*{-i}(G[h]),\qquad
\gamma_i^T(G[h],(\hat p^{i,h}*i,\rho*{-i})) \ge m_i(h)-\zeta.
]

**Dependencies.** None.

**Technique hint.** Plug in the existing subgame (\varepsilon)-maxmin / Martin-function machinery to every continuation game (G[h]).

**Difficulty.** 5/10.

---

### 2. [BREAKDOWN_AMEND:L2] Safe-target and bounded-bias correspondence

**Precise statement.**
For every (\delta>0) and every public history (h), there exists a nonempty compact set (W_\delta(h)\subseteq [0,1]^N) and, for each (v\in W_\delta(h)), a nonempty compact bias set (B_\delta(h,v)\subseteq \mathbb R^N) such that:

1. (v_i \ge m_i(h)-\delta) for all (i).
2. There exists a constant (C_\delta<\infty), depending only on (G) and (\delta), with
   [
   |\beta|*\infty \le C*\delta \qquad \forall h,\ \forall v\in W_\delta(h),\ \forall \beta\in B_\delta(h,v).
   ]
3. The correspondence is hereditary: whenever (v\in W_\delta(h)) and (\beta\in B_\delta(h,v)), any admissible successor promise produced from ((h,v,\beta)) lies in (W_\delta(h[a,s'])) with bias in (B_\delta(h[a,s'],v)), preserving the **same** target (v).

**Dependencies.** L1.

**Technique hint.** Define the Martin safe set as the closed slice of continuation targets that remain above approximate public minmax in every continuation; obtain compactness from finiteness of states/actions and bounded payoffs.

**Difficulty.** 6/10.

---

### 3. [BREAKDOWN_AMEND:L3] Correlated one-step Martin decomposition

**Precise statement.**
For every history (h), target (v\in W_\delta(h)), and bias (\beta\in B_\delta(h,v)), there exists a finite recommendation alphabet (R_h), a distribution (\lambda_h\in \Delta(R_h)), action maps
[
a_i^h:R_h\to A_i(s(h)),
]
and successor biases
[
\beta^{r,s'} \in B_\delta(h[a^h(r),s'],v)
]
such that for every player (i) and every alternative response map (b_i:R_h\to A_i(s(h))),
[
v_i+\beta_i \ge
\sum_{r\in R_h}\lambda_h(r)\Bigl(
u_i(s(h),(b_i(r),a^h_{-i}(r)))
+
\sum_{s'}P(s'\mid s(h),(b_i(r),a^h_{-i}(r))),\beta^{r,s'}*i
\Bigr)
-\eta*{|h|},
]
and when (b_i(r)=a_i^h(r)) for all (r), the reverse inequality also holds up to (\eta_{|h|}). Thus obeying the recommendation is one-step optimal in the Martin sense while preserving the same target (v).

**Dependencies.** L1, L2.

**Technique hint.** Import the extensive-form correlated (\varepsilon)-equilibrium layer already mentioned in the route and repackage it as a one-step target-preserving decomposition.

**Difficulty.** 7/10.

---

### 4. [BREAKDOWN_AMEND:L4] **Critical lemma:** uncorrelated one-step self-generation

**Precise statement.**
For every history (h), target (v\in W_\delta(h)), and bias (\beta\in B_\delta(h,v)), there exist a **product** mixed action
[
x(h,v,\beta)=\prod_{j\in N}x_j(h,v,\beta)\in \prod_{j\in N}\Delta(A_j(s(h)))
]
and successor biases
[
\beta^{a,s'}\in B_\delta(h[a,s'],v)
]
for all action profiles (a\in A(s(h))) and next states (s'\in S), such that for every player (i),
[
v_i+\beta_i \le
\sum_{a}x(a)\Bigl(
u_i(s(h),a)+\sum_{s'}P(s'\mid s(h),a),\beta_i^{a,s'}
\Bigr)+\eta_{|h|},
]
and for every pure unilateral deviation (a_i'\in A_i(s(h))),
[
v_i+\beta_i \ge
\sum_{a_{-i}}x_{-i}(a_{-i})\Bigl(
u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'\mid s(h),(a_i',a_{-i})),\beta_i^{(a_i',a_{-i}),s'}
\Bigr)-\eta_{|h|}.
]

Equivalently: every safe target slice (W_\delta(h)) contains a **product-form Nash-preserving Martin decomposition** at every history.

**Dependencies.** L1, L2, L3.

**Technique hint.** Show that the correlated Martin-feasible set has a nonempty intersection with the product simplex after imposing all playerwise one-step obedience inequalities and successor-bias feasibility constraints. Any proof here will look like a new selector theorem on the history tree.

**Difficulty.** 10/10.

**Why this is the critical lemma.**
This is the hardest step and the one most likely to be the open problem in a new costume. The route notes already flag the missing-convexity gap: existing Martin-function tools reach individually rational profiles, correlated equilibria, or equilibrium in some subgame, but not yet a single uncorrelated profile across all histories and states. If L4 fails, the route breaks here. 

---

### 5. [BREAKDOWN_AMEND:L5] Global selector on the countable public-history tree

**Precise statement.**
Assume L4. Then for each initial state (s\in S) and each chosen root target (v^s\in W_\delta((s))), there exists a recursively defined selector assigning to every public history (h) reachable from (s) a bias
[
\beta(h)\in B_\delta(h,v^s)
]
and a product mixed action
[
x(h)\in \prod_{j\in N}\Delta(A_j(s(h)))
]
such that the L4 inequalities hold at (h) with target (v^s), and every successor history (h[a,s']) inherits the same target (v^s).

**Dependencies.** L4.

**Technique hint.** Once nonemptiness is established, this is mostly bookkeeping: the public-history tree is countable and discrete, so a recursive choice argument suffices.

**Difficulty.** 4/10.

---

### 6. [BREAKDOWN_AMEND:L6] Strategy implementation with public punishment modes

**Precise statement.**
Assume L1 and L5. Then there exists a single behavioral profile (\sigma^\varepsilon\in \Sigma(G)) and a public mode process
[
M_t \in {\mathrm{normal}}\cup N
]
such that:

1. If (M_t=\mathrm{normal}), players use the selector action (x(h_t)) from L5.
2. If (M_t=i), players use the punishment continuation (p^{i,h_t}) from L1.
3. The update rule for (M_t) depends only on the public history and the deviation-detection ingredient supplied by the Martin machinery.
4. For each initial state (s), the profile enters normal mode with root target (v^s) and thereafter preserves that same target through all successor histories in normal mode.

**Dependencies.** L1, L5.

**Technique hint.** Enlarge the public state by a mode variable carrying the current target and, when needed, the currently punished player.

**Difficulty.** 6/10.

---

### 7. [BREAKDOWN_AMEND:L7] Telescoping comparison against arbitrary unilateral deviations

**Precise statement.**
Assume L4 through L6. Let (C_\delta) be the bias bound from L2. Then for every initial state (s), every player (i), every unilateral deviation (\tau_i\in\Sigma_i(G)), and every horizon (T\ge 1),
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
v_i^s - 2\delta - \frac{2C_\delta}{T} - \frac{1}{T}\sum_{t=1}^{T}\eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
\le
v_i^s + 2\delta + \frac{2C_\delta}{T} + \frac{1}{T}\sum_{t=1}^{T}\eta_t.
]
Consequently,
[
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))
------------------------------------------------

\gamma_i^T(G,s,\sigma^\varepsilon)
\le
4\delta + \frac{4C_\delta}{T} + \frac{2}{T}\sum_{t=1}^{T}\eta_t.
]

**Dependencies.** L4, L5, L6.

**Technique hint.** Condition on the first public history where the deviation branches, apply the one-step Martin inequalities, and telescope the bias terms. The fixed target (v^s) is the keel; the bias terms are the ballast that disappears at rate (1/T).

**Difficulty.** 7/10.

---

### 8. [BREAKDOWN_AMEND:L8] Parameter closing and uniform horizon cutoff

**Precise statement.**
Choose (\delta) and ((\eta_t)) so that
[
4\delta + 2\sum_{t\ge 1}\eta_t \le \frac{\varepsilon}{2}.
]
Then choose
[
T_0 \ge \frac{8C_\delta}{\varepsilon}.
]
For every (T\ge T_0), every initial state (s\in S), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma^\varepsilon)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon.
]
Hence (\sigma^\varepsilon) is a uniform (\varepsilon)-equilibrium.

**Dependencies.** L7.

**Technique hint.** Pure parameter bookkeeping.

**Difficulty.** 2/10.

---

## [BREAKDOWN_AMEND:GLUE] Glue steps from the lemmas to the final theorem

**Glue step G1. Root-target choice.**
For each initial state (s\in S), choose one root target (v^s\in W_\delta((s))). Since (S) is finite, this still defines one single profile (\sigma^\varepsilon) on the original game.

**Glue step G2. Global construction.**
Apply L5 and L6 to turn the per-history feasible tuples into one behavioral strategy profile (\sigma^\varepsilon) defined on every public history, with target (v^s) frozen at the root state (s) and punishment modes available off the normal branch.

**Glue step G3. Verification.**
Apply L7 to every (s\in S), (i\in N), (\tau_i\in\Sigma_i(G)), and (T), then apply L8 to get one threshold (T_0) such that
[
\forall T\ge T_0,\ \forall s\in S,\ \forall i\in N,\ \forall \tau_i\in\Sigma_i(G),\quad
\gamma_i^T(G,s,\sigma^\varepsilon)\ge
\gamma_i^T(G,s,(\tau_i,\sigma^\varepsilon_{-i}))-\varepsilon.
]
This is exactly the adopted definition of uniform (\varepsilon)-equilibrium. Since (\varepsilon>0) was arbitrary, this yields (\operatorname{HasUniformEq}(G)), and then (\forall G\in\mathfrak G,\operatorname{HasUniformEq}(G)).

## Short diagnosis

If this route succeeds, it will be because L4 is true in a genuinely strong sense: every safe Martin target slice admits a product-form one-step Nash decomposition with bounded successor biases. If it fails, the failure is likely not in the telescoping or bookkeeping, but in the absence of such an uncorrelated selector, exactly where the route packet says the convexity scaffolding may be missing.

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

---
## ADDITIONAL LOADED FILES

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md

# Assumption Delta

- Added assumptions: 0
- Removed assumptions: 0
- Scope changes: 2
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

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown_amendments.md` (5073 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (8396 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_01.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_02.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

