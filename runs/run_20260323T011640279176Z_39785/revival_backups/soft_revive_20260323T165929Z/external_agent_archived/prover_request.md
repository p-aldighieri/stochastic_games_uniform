# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T06:46:57.234583+00:00

## Instructions

Advance the proof by proving lemmas from the breakdown. Every step must have explicit justification (known theorem, previous lemma, or direct computation). Tag conclusions [DERIVED], new assumptions [ASSUMPTION+]/[ASSUMPTION-], and breakdown change requests [BREAKDOWN_AMEND]. Be explicit about gaps. Reference lemmas by number. Maintain a status summary of what's proved.

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
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (5941 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_01.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_02.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

