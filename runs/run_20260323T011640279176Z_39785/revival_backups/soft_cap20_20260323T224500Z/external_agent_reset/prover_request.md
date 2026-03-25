# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T22:39:55.069882+00:00

## Instructions

Advance the proof by proving lemmas from the breakdown. Every step must have explicit justification (known theorem, previous lemma, or direct computation). Tag conclusions [DERIVED], new assumptions [ASSUMPTION+]/[ASSUMPTION-], and breakdown change requests [BREAKDOWN_AMEND]. Be explicit about gaps. Reference lemmas by number. Maintain a status summary of what's proved.

## Context

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown.md

# Breakdown Output

Generated: 2026-03-23T22:39:55.058760+00:00

Bootstrap breakdown for the preferred Martin-function bootstrap to a global Nash selector. The theorem is still open in the durable project sources, and the route below preserves the exact target quantifiers: one public-history behavioral profile, one threshold (T_0), all (T\ge T_0), and every initial state.    

**Dependency order:**
(L1 \rightarrow L2 \rightarrow L3 \rightarrow L4 \rightarrow L5 \rightarrow L6 \rightarrow L7' \rightarrow L8').

Fix a finite stochastic game (G) and (\varepsilon>0). For a public history (h), write (s(h)) for its terminal state and (h[a,s']) for the successor history obtained by appending action profile (a) and next state (s'). Let (m_i(h)) denote the Martin/maxmin benchmark for player (i) in the continuation game rooted at (h). Fix a nonnegative leakage schedule ((\eta_t)_{t\ge1}).

### [BREAKDOWN_AMEND] L1. Continuation subgames and unilateral deviation values

**Statement.** For every public history (h), the continuation game (G_h) is again a finite stochastic game of the same class. For every player (i), horizon (T), and opponents’ public-history profile (\sigma_{-i}) on (G_h), the unilateral deviation problem of player (i) is a finite-horizon controlled Markov problem, so the value
[
V_i^T(h,\sigma_{-i}) := \sup_{\tau_i}\gamma_i^T(G_h,\text{root}(h),(\tau_i,\sigma_{-i}))
]
is well defined.

**Dependencies.** Formal model only.

**Technique hint.** Unwind the definition of continuation histories. Once (\sigma_{-i}) is fixed, player (i)'s problem is an MDP on a finite public-history tree.

**Difficulty estimate.** Easy.

### [BREAKDOWN_AMEND] L2. Safe promise-bias correspondence

**Statement.** There exists a constant (C<\infty) and, for every public history (h), a nonempty compact set
[
\mathcal C(h)\subseteq [0,1]^N\times[-C,C]^N
]
of admissible promise-bias pairs ((w,b)) such that every ((w,b)\in\mathcal C(h)) satisfies
[
w_i \ge m_i(h)-\eta_{|h|}\qquad\forall i\in N.
]
In particular, for every initial state (s\in S), there is at least one root pair ((w^s,b^s)\in\mathcal C(s)).

**Dependencies.** L1 plus the intended Martin-function input.

**Technique hint.** Package the Martin-function machinery into a history-indexed continuation object: (w) is the safe promise vector, (b) is the bounded bias/relative-value correction needed for telescoping average payoffs. Compactness comes from finiteness and closedness of the induced continuation constraints.

**Difficulty estimate.** Hard, but plausibly imported from existing Martin-function structure.

### [BREAKDOWN_AMEND] L3. Local feasibility relation is compact

**Statement.** Fix a history (h) and an admissible pair ((w,b)\in\mathcal C(h)). Define (\mathcal F(h,w,b)) to be the set of all data consisting of:

1. a **product** mixed action (x=\prod_{j\in N}x_j\in \prod_j \Delta(A_j(s(h)))), and
2. for every one-step successor (h[a,s']), an admissible successor pair ((w^{a,s'},b^{a,s'})\in\mathcal C(h[a,s'])),

such that for every player (i),

[
\sum_{a}x(a)\Bigl(u_i(s(h),a)+\sum_{s'}P(s'|s(h),a),b_i^{a,s'}\Bigr)-b_i
\ge w_i-\eta_{|h|},
\tag{Bal}
]

and for every pure unilateral deviation (a_i'\in A_i(s(h))),

[
\sum_{a_{-i}}x_{-i}(a_{-i})\Bigl(u_i(s(h),(a_i',a_{-i}))
+\sum_{s'}P(s'|s(h),(a_i',a_{-i})),b_i^{(a_i',a_{-i}),s'}\Bigr)-b_i
\le w_i+\eta_{|h|}.
\tag{Dev}
]

Then (\mathcal F(h,w,b)) is compact.

**Dependencies.** L2.

**Technique hint.** This is a closed feasibility system inside a finite-dimensional product of simplices and compact continuation sets.

**Difficulty estimate.** Medium.

### [BREAKDOWN_AMEND] L4. One-step product-selector theorem

**Statement.** For every public history (h) and every admissible pair ((w,b)\in\mathcal C(h)), the local feasibility relation is nonempty:
[
\mathcal F(h,w,b)\neq\varnothing.
]
Equivalently, every admissible promise-bias pair can be propagated one step forward by some uncorrelated mixed action and some admissible assignment of successor pairs while satisfying both (Bal) and all instances of (Dev).

**Dependencies.** L2, L3.

**Technique hint.** This is the place where the route needs a genuinely new selector theorem. The selector must output a **product** distribution, not a correlated recommendation, and it must work history-by-history while preserving all players’ one-step incentive bounds simultaneously. Any punishment logic has to be embedded here through the successor pairs; if it is postponed, later lemmas become formal shellwork.

**Difficulty estimate.** Theorem-sized. This is the hardest step.

### [BREAKDOWN_AMEND] L5. Rooted recursion on the public-history tree

**Statement.** Assume L4. For every initial state (s) and every chosen root pair ((w^s,b^s)\in\mathcal C(s)), there exists:

1. a behavioral profile (\sigma^s) on the full rooted public-history tree starting at (s), and
2. a pair assignment (h\mapsto (w(h),b(h))\in\mathcal C(h)) for every history rooted at (s),

such that ((w(s),b(s))=(w^s,b^s)) and, at every rooted history (h), the mixed action prescribed by (\sigma^s) together with the successor-pair assignment belongs to (\mathcal F(h,w(h),b(h))).

**Dependencies.** L2, L4.

**Technique hint.** Recursive construction on the countable finitely-branching history tree. No measurable-selection drama is needed here because the history tree is discrete.

**Difficulty estimate.** Medium once L4 is available.

### [BREAKDOWN_AMEND] L6. Global assembly across initial states

**Statement.** If for each initial state (s\in S) one has a rooted profile (\sigma^s) and rooted pair assignment as in L5, then these splice into a single global public-history behavioral profile (\sigma) and a single global pair assignment on all public histories by setting
[
\sigma(h):=\sigma^{s_1}(h),
]
where (s_1) is the initial state appearing in the history (h). The assembled (\sigma) preserves the L5 local feasibility property on every history.

**Dependencies.** L5.

**Technique hint.** Histories with different initial states live on disjoint rooted trees, so splicing is literal disjoint-union assembly.

**Difficulty estimate.** Easy.

### [BREAKDOWN_AMEND] L7'. Telescoping finite-horizon incentive bounds

**Statement.** Assume the global profile (\sigma) and global pair assignment satisfy L5-L6, and every admissible bias vector is bounded by (|b|*\infty\le C). Then for every initial state (s), player (i), unilateral deviation (\tau_i), and horizon (T),
[
\gamma_i^T(G,s,\sigma)\ \ge\ w_i^s-\frac{2C}{T}-\frac{1}{T}\sum*{t=1}^{T}\eta_t,
]
and
[
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))\ \le\ w_i^s+\frac{2C}{T}+\frac{1}{T}\sum_{t=1}^{T}\eta_t.
]
Therefore
[
\gamma_i^T(G,s,\sigma)\ \ge\ \gamma_i^T(G,s,(\tau_i,\sigma_{-i}))
-\frac{4C}{T}-\frac{2}{T}\sum_{t=1}^{T}\eta_t.
]

**Dependencies.** L5, L6, bounded biases from L2.

**Technique hint.** Telescope the (Bal) inequalities along the obedient play and the (Dev) inequalities along the deviating play. The only end effects are the root and terminal bias terms, hence the (2C/T) boundary loss.

**Difficulty estimate.** Medium; this is mostly algebra once the selector exists.

### [BREAKDOWN_AMEND] L8'. Bookkeeping to uniform (\varepsilon)-equilibrium

**Statement.** Choose the leakage schedule nonnegative and summable, for instance so that
[
\sum_{t\ge1}\eta_t\le \varepsilon/4.
]
Then there exists (T_0) such that for all (T\ge T_0),
[
\frac{4C}{T}+\frac{2}{T}\sum_{t=1}^{T}\eta_t \le \varepsilon.
]
Hence, by L7', for every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)\ge \gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]
So (\sigma) is a uniform (\varepsilon)-equilibrium.

**Dependencies.** L7' and (\eta_t\ge0).

**Technique hint.** Pure bookkeeping. Nonnegativity makes the leakage term monotone and summability kills it after division by (T).

**Difficulty estimate.** Easy.

## [BREAKDOWN_AMEND] Critical lemma

**Critical lemma: L4.** This is the bottleneck identified by the durable route memo. It asks for a history-wise selector that upgrades Martin-style safe continuation data into a **single uncorrelated mixed action plus successor admissible pairs** satisfying all one-step unilateral incentive inequalities. Known ingredients appear to give maxmin-safe profiles, correlated objects, or solvability on a subgame, but not this global product-selector on the full history tree. If L4 is proved, the rest of the route is mostly recursive assembly and telescoping; if L4 fails, this route does not close.  

## [BREAKDOWN_AMEND] Glue steps to the final theorem

**G1.** Fix (G\in\mathfrak G) and (\varepsilon>0). Choose a nonnegative leakage schedule ((\eta_t)) with (\sum_t \eta_t\le \varepsilon/4).

**G2.** Invoke L1-L2 to obtain the admissible promise-bias correspondence (\mathcal C(h)) and root pairs ((w^s,b^s)) for all initial states.

**G3.** Invoke L3-L4 to get one-step feasible product actions and successor admissible pairs at every history.

**G4.** Use L5 to build the rooted profiles (\sigma^s), then L6 to splice them into one global behavioral profile (\sigma) defined on all public histories.

**G5.** Apply L7' and L8' to conclude that (\sigma) is a uniform (\varepsilon)-equilibrium for every initial state simultaneously.

**G6.** Since (G) and (\varepsilon) were arbitrary, the theorem
[
\forall G\in\mathfrak G,\ \operatorname{HasUniformEq}(G)
]
would follow.

## [BREAKDOWN_AMEND] What is already downstream vs. what is still research-grade

Downstream once L4 exists: L5, L6, L7', L8'. Imported but still needing careful citation/packaging: L2. Central research obstacle: L4. This matches the durable project picture: the theorem stays open, the route is bootstrap, and the selector step is the real hinge.  

## [BREAKDOWN_AMEND] Edit rule

If a future pass changes the local inequality template, amend **L3 and L4 first**, then update only the downstream constants in L7' and L8'. The rest of the dependency graph should remain stable.

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
- Use the corrected post-L4 backbone
- The proof above establishes only the literal displayed statement of L6. It does **not** build a non-vacuous punishment-mode mechanism. Any stronger “switch to a punishment plan anchored at a remembered history” reading remains unproved unless the public state is enriched to remember that anchor.
- Replace the old L7 by the following corrected version.
- Replace L8 by the following corrected version, which explicitly cites the standing hypothesis (\eta_t\ge0).
- The remaining gap is now cleanly localized. L1 and L2 remain imported. L4 remains the unresolved selector theorem. Everything after L4 is tree recursion plus telescoping bookkeeping.
- I will use the typed reading
- The weak telescope is the exact output of the current L3-L6 data. It does **not** imply the displayed L7' in the packet, because the right-hand sides contain the visited promise process (w_i(H_t)), not the root promise (w_i^s). Also, the expectation in (WT-ob) is taken under obedient play and the expectation in (WT-dev) under deviating play, so the promise averages do not cancel. The current local relation uses successor **biases** but never successor **promises**, so no fixed-promise invariant is propagated. Therefore the current L7' requires a genuine amendment upstream, at L3-L4, exactly where the route memo says amendments should be made first.
- For each history (h) and promise vector (w\in[0,1]^N), define the bias fiber
- **Required packet repair.**

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

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_04.md

# Reviewer Output

Generated: 2026-03-23T20:14:47.833519+00:00

# VERDICT: PATCH_BIG

This is **not** a complete proof of the target theorem. The packet itself keeps the project in bootstrap/open status, preserves the exact theorem-side target as the one-profile strategy-existence statement for all sufficiently large horizons and all initial states, and explicitly leaves **L4** unresolved. That already rules out `PASS`. It is also not `REDO`, because the repaired tail in `prover_04` is mostly sound. `PATCH_BIG` is the right label because the branch still needs a packet-level rewrite: make the repaired post-L4 backbone canonical, retire stale intermediate versions, and attach real source citations for the imported L1/L2 machinery.    

## Step check

* **L1. Safe promise correspondence:** **Not proved in-packet.** It is explicitly treated as imported machinery. That is acceptable only if it is clearly labeled as an external input and given an actual source citation. In the current packet it is still an uncited import.
* **L2. Historywise nonemptiness:** **Also not proved in-packet.** Same issue: acceptable as an external assumption/import, but not as a proved lemma unless a real source is cited.
* **L3. Compact local feasibility correspondence:** The sharpened `prover_04` version is logically fine. Compactness of `X(h) × Y(h)` and continuity of the finitely many defining inequalities are enough, and the empty set is compact. The closed-graph-on-each-depth-layer argument is also acceptable once one works layerwise. Citation cleanup remains: the compactness/closed-graph proof uses **L1**, not **L2**.
* **L4. One-step uncorrelated Nash selector:** **Still unresolved.** This remains the theorem-sized bottleneck, exactly as the packet says. No theorem closure is available without it.
* **L5. Global recursive assembly:** The repaired full-tree version is logically sound **conditional on L4**, with the important correction that the root choice also needs **L2**. The explicit whole-game glue is correct: either direct recursion on all of `H`, or the equivalent `σ(h) := σ^{root(h)}(h)` construction once rooted profiles are built.
* **L6. Equilibrium-path delivery inequality:** The literal displayed inequality is proved correctly in `prover_04` by conditioning on `h_t` and telescoping the promise terms. But only that displayed inequality is proved. The stronger punishment-mode reading is **not** proved.
* **L7:** The old version should not remain as the active proof step. The corrected **L7′** in `prover_04` is the right lemma: it is a direct one-step deviation telescope on the full tree and does not need punishment machinery.
* **L8:** The corrected **L8′** is valid bookkeeping from L6 and L7′, with the explicit use of `η_t ≥ 0`. This is the clean closing step for the conditional tail. 

## Main errors and why they are big rather than small

1. **The packet is still not one coherent proof object.**
   The branch contains stale and repaired versions side by side. The old dependency spine and old L7/L8 remain in the breakdown, while `prover_04` uses the corrected backbone
   `L1 → L2 → L3 → L4 → strengthened L5 → {L6, L7′} → L8′`.
   That is more than a cosmetic fix. The branch needs restructuring so there is one authoritative statement set. 

2. **Imported inputs L1/L2 still lack actual citations.**
   Since L1/L2 are not proved here, the packet must cite the exact external source that justifies them. Without that, the conditional tail is not properly grounded. This is a serious citation/completeness defect, not a typo-level issue. 

3. **Notation is not yet consolidated.**
   Earlier prover files use the `B_δ / v^s / β` language, while the repaired backbone in `prover_04` is stated in the `W(h) / w(h) / F(h,w)` language. Those can perhaps be reconciled, but until they are unified the packet is not cleanly citable. 

4. **The theorem remains conditional, not solved.**
   The durable proof-state and route memo both still treat the route as bootstrap/open, with L4 as the central unresolved selector step. The current packet improves the post-L4 tail, but it does not convert the branch into a proof of the theorem.  

## Scope compliance

There is **no theorem-side scope drift** in the repaired tail, provided `prover_04` is taken as the authoritative version. It keeps the exact target from the durable claim source: one public-history behavioral profile, all sufficiently large finite horizons, every initial state, and strategy-existence rather than payoff-set existence. That part is aligned.   

* **[SCOPE]** L5 must quantify over the **full public-history tree**, not merely compliance-reachable histories. Otherwise the deviation paths needed in L7′ are outside the domain of the constructed objects. This repair is necessary and correct. 
* **[SCOPE]** The stronger reading of L6 as an actual punishment-mode mechanism is **not** proved. What is proved is only the displayed delivery inequality. Claiming a genuine “switch to punishment plan anchored at history `h`” would require enlarging the public state to remember that anchor, which changes the proof object. 
* **[SCOPE]** A family of rooted profiles `σ^s` is **not yet** the theorem target. The target needs one whole-game profile `σ`; the packet now has an explicit glue step, and that glue must stay in the final version.  

## Required patch set

1. Rewrite the breakdown and glue steps so the **only active backbone** is the repaired one from `prover_04`.
2. Mark `prover_01`–`prover_03` as superseded, or remove them from the proof packet.
3. Replace old **L7** by **L7′** as the main deviation lemma, and replace **L8** by **L8′** as the closing step.
4. Keep **L6** only in its literal displayed form; do not cite it as a nonvacuous punishment construction.
5. Add real citations for **L1** and **L2**, or explicitly relabel them as external assumptions for a conditional theorem.
6. Normalize dependency citations:

   * L5 must cite **L2** for root nonemptiness.
   * L7′ should cite the strengthened **L5** and whatever boundedness input is actually used.
   * L8′ must explicitly cite `η_t ≥ 0`. 

## Bottom line

The good news is real: the **post-L4 tail is now largely correct**. In particular, the full-tree assembly, the direct deviation telescope, and the final uniformization bookkeeping look sound in the repaired version. The bad news is equally real: the branch is **still conditional** on imported L1/L2 and, above all, on the unresolved selector theorem L4. So the right certification is:

* **accepted conditionally:** repaired L3, strengthened L5, literal L6, L7′, L8′;
* **not accepted as a theorem proof:** because L4 is open and L1/L2 remain uncited imports;
* **packet verdict:** `PATCH_BIG`, since the branch must be restructured around the repaired tail before it becomes a clean conditional proof record.

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_05.md

# Reviewer Output

Generated: 2026-03-23T22:39:55.036609+00:00

VERDICT: PATCH_BIG

The packet does not yet support its own displayed downstream claim. The decisive defect is that the main-route version of L7′ does **not** follow from the current variable-promise L3-L5. The packet itself later proves only a weak telescope with the visited promise process (w_i(H_t)), and then explicitly states that the root-promise bound requires an upstream replacement of L3-L5 by fixed-promise fiber versions (L3^*,L4^*,L5^*). That is a structural change to the local selector layer, not a cosmetic proof edit. The durable proof-state source still marks the project as bootstrap/open, and the durable route memo already records Route B as `PATCH_BIG`, with L4 unresolved, global assembly still needing explicit treatment, and L6 too weak to support a real punishment-mode reading.   

### Step review

1. **L1: acceptable, with minor notation cleanup.**
   The proof that a continuation game (G_h) stays in the same finite stochastic-game class, and that the unilateral (T)-horizon deviation problem has a well-defined value, is logically fine. The compactness/continuity argument over truncated behavioral deviations works. The only repair needed is notational consistency: the continuation game should start from the terminal state (s(h)) or an explicitly defined root of (G_h), not an ambiguous `root(h)` symbol. This is small. 

2. **L2: not proved, only imported.**
   This is allowed only if it is kept explicitly imported/open. The packet itself says L2 remains imported and still needs careful citation/packaging. So L2 cannot be marked as derived, and the route cannot claim more than a conditional result downstream of this input. This is a citation/completeness defect, not yet a theorem-side contradiction. 

3. **L3: valid as a compactness lemma after the typed-formula repair.**
   The compactness argument is standard once the ambient product is compact and the balance/deviation inequalities are continuous. But the packet also notes that the displayed ((Bal)) and ((Dev)) formulas are ill-typed until the comma notation is repaired into the intended scalar expression. After that repair, L3 is fine **as stated**. What it does **not** do is support the later root-promise telescope. 

4. **L4: still open, and more precisely the real downstream bottleneck is (L4^*), not current L4.**
   The packet correctly identifies L4 as the theorem-sized selector bottleneck. But once prover_05 shows that variable-promise L3-L5 do not yield the displayed L7′, the selector theorem that actually matters is the strengthened fixed-promise selector (L4^*). So the main breakdown’s “critical lemma: L4” is no longer the whole story. This is a real restructuring issue.  

5. **L5: conditionally valid as recursion, but mis-cited and insufficient for current L7′.**
   The recursion on the full rooted public-history tree is fine once L2 supplies the root pair/bias nonemptiness and L4 supplies one-step successor data. The accepted amendments already note both repairs: L5 must depend on L2, and it must quantify over the full rooted tree, not merely on-path histories. However, the variable-promise L5 does **not** propagate a fixed root promise, so it cannot be the direct upstream input for the packet’s displayed L7′. 

6. **L6: literal disjoint-union assembly is valid; punishment-mode L6 is not proved.**
   As a splice of rooted trees into one global behavioral profile, L6 is fine. But the packet’s own accepted amendments and later audit state that any stronger reading involving a remembered punishment anchor is unproved. So L6 may be cited only as literal global assembly. Using it as a substantive punishment-mode mechanism is incorrect.  

7. **Displayed L7′ in the main breakdown: not proved from current L3-L6.**
   This is the main failure. The later self-audit shows that the current local relation yields only
   [
   \gamma_i^T(\sigma)\gtrsim \frac1T\sum_t \mathbb E_\sigma[w_i(H_t)] - \cdots,\qquad
   \gamma_i^T(\tau_i,\sigma_{-i})\lesssim \frac1T\sum_t \mathbb E_{\tau_i,\sigma_{-i}}[w_i(H_t)] + \cdots,
   ]
   not bounds in terms of the single root promise (w_i^s). Since the two promise averages are taken under different laws, they do not cancel. The packet says this explicitly and correctly concludes that the displayed L7′ requires an upstream amendment at L3-L4. So the earlier “L7′ is proved” passages are superseded by the later repair note. Leaving both in the packet makes the current packet internally inconsistent. 

8. **Corrected L7′ under (L3^*,L4^*,L5^*): plausibly valid.**
   Once the promise coordinate is frozen along a rooted tree and only the bias varies, the telescope to the root promise (w^s) is the right one, and the corrected proof shape is sound. But that is a proof of a **different downstream system** than the main breakdown currently states. So it cannot rescue the present packet without rewriting the upstream lemma statements. 

9. **L8′: valid bookkeeping only after the corrected upstream rewrite.**
   Given corrected L7′ and explicit (\eta_t\ge 0), L8′ is standard averaging/bookkeeping and is fine. Under the unrepaired variable-promise route, it does not close anything. So L8′ is not the problem, but its dependency citation must be updated. 

10. **Glue steps G1-G6: not valid as currently written.**
    G3-G5 still invoke current L3-L4-L5 and the displayed L7′, but the later repair note says exactly that the local inequality template must be amended first. So the route cannot presently jump from G3 to G5 as written. The glue chain must be rewritten around (L3^*,L4^*,L5^*). 

### Scope compliance

[SCOPE] The theorem-side scope is preserved. The packet still targets the adopted claim: one behavioral public-history profile (\sigma), one threshold (T_0), all sufficiently large finite horizons, and every initial state, with approximate Nash inequalities under expected finite-horizon average payoff. It does **not** silently downgrade to payoff-set existence, fixed-initial-state existence, stationary/finite-memory existence, discounted payoff, or an augmented public-randomization model. The durable claim source and the route memo both align with that scope. The fixed-promise repair is an internal lemma reformulation, not a theorem-side scope change.   

### Citation/dependency defects

The packet still has several citation defects.

* **Internal dependency citations are wrong in places.** L5 needs L2 as well as L4; L7′ needs the bias bound from L2 and, in corrected form, the fixed-promise upstream lemmas; L8′ needs explicit (\eta_t\ge 0). The route memo specifically asks for statement repair whenever stronger dependencies are needed.  
* **External source citation for L2 is missing.** The packet repeatedly says L2 is imported from Martin-function machinery, but no precise theorem/proposition citation is given in the packet. That is incomplete.
* **Old and corrected downstream claims coexist.** Earlier derived claims for L7/L8 are later withdrawn in substance by the weak-telescope analysis. The packet should not present both as simultaneously valid.

### Required repair

The minimum coherent rewrite is:

[
L1 \to \text{imported }L2 \to L3^* \to \text{open }L4^* \to L5^* \to \text{literal }L6 \to \text{corrected }L7' \to L8'.
]

Then rewrite G3-G5 to use that backbone, keep L6 explicitly literal, and keep the whole theorem labeled bootstrap/open unless and until (L4^*) is actually proved. That matches the durable proof-state and route-memo picture.   

So the right reviewer outcome is **PATCH_BIG**: the post-selector tail is close to salvageable, but only after replacing the current variable-promise local system with the fixed-promise one and updating all downstream statements and citations accordingly.

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
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (14687 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_01.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_02.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_03.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_04.md` (15204 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_05.md` (19004 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

