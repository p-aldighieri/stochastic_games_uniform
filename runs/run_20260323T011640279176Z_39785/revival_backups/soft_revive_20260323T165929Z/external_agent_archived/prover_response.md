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
