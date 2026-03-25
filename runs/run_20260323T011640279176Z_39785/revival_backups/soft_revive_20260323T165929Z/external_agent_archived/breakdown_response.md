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
