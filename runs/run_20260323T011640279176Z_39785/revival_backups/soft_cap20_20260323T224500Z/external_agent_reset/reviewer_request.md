# External Agent Request (reviewer)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T22:39:55.081127+00:00

## Instructions

Check each proof step for logical validity, completeness, and correct citations. Check scope compliance. Issue a structured verdict: VERDICT: PASS (correct and complete), VERDICT: PATCH_SMALL (minor fixable issues), VERDICT: PATCH_BIG (needs restructuring), or VERDICT: REDO (fundamentally flawed approach). Be precise about errors. Tag scope changes with [SCOPE].

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
- I will use the typed reading
- The weak telescope is the exact output of the current L3-L6 data. It does **not** imply the displayed L7' in the packet, because the right-hand sides contain the visited promise process (w_i(H_t)), not the root promise (w_i^s). Also, the expectation in (WT-ob) is taken under obedient play and the expectation in (WT-dev) under deviating play, so the promise averages do not cancel. The current local relation uses successor **biases** but never successor **promises**, so no fixed-promise invariant is propagated. Therefore the current L7' requires a genuine amendment upstream, at L3-L4, exactly where the route memo says amendments should be made first.
- For each history (h) and promise vector (w\in[0,1]^N), define the bias fiber
- **Required packet repair.**
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

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_05.md

# Prover Output

Generated: 2026-03-23T22:19:04.446035+00:00

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

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_06.md

# Prover Output

Generated: 2026-03-23T22:39:55.070320+00:00

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

---
## ADDITIONAL LOADED FILES

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md

# Assumption Delta

- Added assumptions: 0
- Removed assumptions: 0
- Scope changes: 4
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

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown_amendments.md` (7359 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (17528 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_01.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_02.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_03.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_04.md` (6865 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_05.md` (7806 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (52 chars)

