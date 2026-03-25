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
