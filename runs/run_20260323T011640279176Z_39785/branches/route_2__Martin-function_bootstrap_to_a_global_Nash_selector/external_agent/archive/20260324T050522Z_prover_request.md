# External Agent Request (prover)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-24T02:20:49.578387+00:00

## Instructions

Advance the proof by proving lemmas from the breakdown. Every step must have explicit justification (known theorem, previous lemma, or direct computation). Tag conclusions [DERIVED], new assumptions [ASSUMPTION+]/[ASSUMPTION-], and breakdown change requests [BREAKDOWN_AMEND]. Be explicit about gaps. Reference lemmas by number. Maintain a status summary of what's proved.

## Context

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown.md

# Breakdown Output

Generated: 2026-03-24T01:39:58.214424+00:00

# Route B breakdown: Martin-function bootstrap to a global Nash selector

This is the preferred bootstrap route, and it must be treated as **open/bootstrap** rather than completed. The theorem-side quantifiers must stay exactly as in the durable claim source: one behavioral profile (\sigma), one threshold (T_0), all sufficiently large horizons (T), every initial state (s_1), every player (i), every unilateral deviation (\tau_i).   

## Setup and invariant

Fix a finite stochastic game
[
G=(N,S,(A_i)*{i\in N},u,P)
]
with (u_i\in[0,1]), and fix (\varepsilon>0). For each initial state (s\in S), let (H^s) be the rooted tree of public histories starting from (s), and let (G_h) denote the continuation game from history (h). Choose a nonnegative leakage sequence ((\eta_t)*{t\ge 1}) with
[
\sum_{t\ge 1}\eta_t \le \varepsilon/4.
]
The route tries to build, for each root (s), a target vector (\rho^s\in[0,1]^N), a bounded bias function (b^s:H^s\to\mathbb R^N), and a public-history behavioral selector (x^s(h)\in \prod_i \Delta(A_i(s(h)))) such that for every history (h\in H^s) and player (i),
[
\rho_i^s + b_i^s(h)
\le
\mathbb E_{a\sim x^s(h),,q\sim P(\cdot\mid s(h),a)}
\bigl[u_i(s(h),a)+b_i^s(h,a,q)\bigr]+\eta_{|h|}
\tag{E_h^i}
]
and
[
\rho_i^s + b_i^s(h)
\ge
\sup_{y_i\in\Delta(A_i(s(h)))}
\mathbb E_{a_i\sim y_i,\ a_{-i}\sim x^s_{-i}(h),\ q\sim P(\cdot\mid s(h),(a_i,a_{-i}))}
\bigl[u_i(s(h),(a_i,a_{-i}))+b_i^s(h,(a_i,a_{-i}),q)\bigr]-\eta_{|h|}.
\tag{D_h^i}
]
Here (b^s(h,a,q)) means the bias assigned to the child history ((h,a,q)). If this local invariant exists with uniformly bounded bias, then telescoping turns it into uniform finite-horizon incentive bounds. This is exactly the selector-and-telescoping architecture highlighted in the request packet and route memo.  

---

## Numbered lemmas in dependency order

### [BREAKDOWN_AMEND L1] Continuation maxmin floors from every public history

**Statement.**
For every public history (h) and every player (i), there exists a number (m_i(h)\in[0,1]) with the following property: for every (\delta>0), player (i) has a continuation behavioral strategy (\mu_i^{h,\delta}) in (G_h) such that for all sufficiently large horizons (T),
[
\inf_{\sigma_{-i}}\gamma_i^T(G_h,(\mu_i^{h,\delta},\sigma_{-i})) \ge m_i(h)-\delta.
]
Equivalently, each player has a uniformly (\delta)-maxmin continuation guarantee against the coalition of opponents from every continuation game (G_h).

**Dependencies.**
External zero-sum / coalition-controller uniform-value input.

**Technique hint.**
Reduce player (i) versus (N\setminus{i}) to a two-side zero-sum stochastic game with product mixed actions on the coalition side. Then cite the uniform-value / uniform-maxmin theorem for that zero-sum object.

**Difficulty.**
Moderate if cited cleanly; hard if reproved from scratch.

---

### [BREAKDOWN_AMEND L2] Nonempty bounded continuation-promise / bias correspondence

**Statement.**
For each initial state (s\in S), there exist:

* a target vector (\rho^s\in[0,1]^N),
* a finite constant (B_s<\infty),
* and a correspondence (W^s) assigning to every (h\in H^s) a nonempty compact set
  [
  W^s(h)\subseteq [-B_s,B_s]^N,
  ]

such that each (b\in W^s(h)) is a **continuation bias admissible at (h)** in the Martin-function sense, with the built-in properties needed later:

1. **root nonemptiness:** (W^s(s)\neq\varnothing);
2. **uniform boundedness:** every admissible bias is (B_s)-bounded;
3. **minmax safety:** admissibility at (h) includes the continuation guarantees from L1, so punishments can still be invoked from (h);
4. **forward compatibility:** admissibility is designed so that a one-step decomposition into current reward plus expected next admissible bias is meaningful.

This is the point where the route imports the Martin-function continuation object rather than inventing a new one.

**Dependencies.**
L1 plus the cited Martin-function / acceptable-profile machinery.

**Technique hint.**
Define (W^s(h)) as the compact set of bounded continuation biases associated with minmax-safe promise vectors attainable from (h). The exact coding of “bias” can be chosen to match the Martin function, but it must support one-step recursion and later telescoping.

**Difficulty.**
Hard, but mainly a statement-and-citation assembly task if the source really provides the needed continuation object.

---

### [BREAKDOWN_AMEND L3] Compact local feasibility correspondence

**Statement.**
Fix (s\in S), a history (h\in H^s), and a bias (b\in W^s(h)). Define (\mathcal F^s(h,b)) to be the set of all local continuation packages consisting of

* a product mixed action (x\in \prod_i \Delta(A_i(s(h)))),
* and, for each one-step successor (h'=(h,a,q)), a child bias (b(h')\in W^s(h')),

such that the local equilibrium inequalities ((E_h^i)) and ((D_h^i)) hold for every player (i) at (h).

Then (\mathcal F^s(h,b)) is a compact set, and the map ((h,b)\mapsto \mathcal F^s(h,b)) has closed graph.

**Dependencies.**
L2 and finiteness of states/actions.

**Technique hint.**
The action simplex is compact, successor sets are finite, expected payoff and transition expressions are multilinear and continuous, and (W^s(h')) is compact. So the feasible-set graph is cut out by finitely many closed inequalities inside a compact ambient product.

**Difficulty.**
Moderate.

---

### [BREAKDOWN_AMEND L4] One-step uncorrelated self-generation / Nash selector lemma  **(critical lemma)**

**Statement.**
For every (s\in S), every history (h\in H^s), and every admissible bias (b\in W^s(h)), the local feasibility set is nonempty:
[
\mathcal F^s(h,b)\neq\varnothing.
]
Equivalently, for every admissible current bias there exists a **product** mixed action profile (x^s(h)) and an assignment of admissible child biases (b^s(h')\in W^s(h')) to one-step successor histories (h') such that all players simultaneously satisfy the one-step honest-play inequalities ((E_h^i)) and deviation inequalities ((D_h^i)).

This is the exact step that turns a continuation correspondence into an actual public-history Nash selector.

**Dependencies.**
L2 and L3, plus whatever new selector theorem is needed to pass from Martin-function objects, acceptable profiles, or correlated objects to a single uncorrelated local profile.

**Technique hint.**
This is where the route either succeeds or cracks. A proof would likely need one of the following:

* a new fixed-point / self-generation theorem on the history tree,
* an uncoupling theorem upgrading correlated one-step implementability to product implementability while preserving minmax safety,
* or a sharper Martin-function statement that already encodes an uncorrelated local selector.

**Difficulty.**
Extreme. This is the theorem-sized bottleneck and the hardest step in the entire route. The durable memo explicitly identifies L4 as the central unresolved blocker. 

---

### [BREAKDOWN_AMEND L5] Recursive construction on the rooted public-history tree

**Statement.**
Assume L4. Fix (s\in S) and choose a root bias (b_\emptyset^s\in W^s(s)). Then there exist functions
[
h\mapsto x^s(h),\qquad h\mapsto b^s(h)\in W^s(h)
]
defined for all (h\in H^s), such that for every history (h), the pair consisting of the chosen local mixed action (x^s(h)) and the chosen child biases ({b^s(h')}_{h' \text{ child of } h}) belongs to (\mathcal F^s(h,b^s(h))).

So once the one-step feasibility lemma exists, the entire infinite rooted selector is obtained consistently on the full public-history tree.

**Dependencies.**
L2, L3, L4.

**Technique hint.**
Build consistent selectors on finite-depth truncations, use compactness / Kőnig-style consistency to pass to the infinite rooted tree, then read off the full behavioral selector.

**Difficulty.**
Moderate once L4 is available. The route memo marks this recursion step as one of the stable downstream pieces. 

---

### [BREAKDOWN_AMEND L6] Strengthened public-history punishment lemma  **(statement repair needed)**

**Statement.**
Assume L5. Then the rooted selector ((x^s,b^s)) can be augmented to a public-history behavioral profile (\widehat\sigma^s) together with continuation punishment modes so that, for every player (i) and every unilateral deviation strategy (\tau_i), the deviator’s continuation payoff is controlled by the local deviation inequalities ((D_h^i)) along the realized deviating path, up to the tail leakage budget.

A usable form is:

for every (T\ge 1),
[
\mathbb E_{G,s,(\tau_i,\widehat\sigma^s_{-i})}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
T\rho_i^s + 2B_s + \sum_{t=1}^T \eta_t.
\tag{P_i^T}
]

**Dependencies.**
L1 and L5, plus an explicit deviation-detection / punishment ingredient compatible with public monitoring and product mixing.

**Technique hint.**
This lemma must say more than “punishments exist.” It must explain why the public history determines a branch on which a deviator can be charged and punished, despite simultaneous mixed play. A proof could use a cited deviation-detection block construction, or bake test phases into the selector itself.

**Difficulty.**
Hard. The current route memo says the existing weak version is logically valid but too weak if punishment is meant to do real work. So this is the place where a statement repair is mandatory rather than cosmetic. 

---

### [BREAKDOWN_AMEND L7] Telescoping lemma for equilibrium and deviation sums

**Statement.**
Assume L5 and the strengthened L6. Then for every initial state (s), every player (i), every horizon (T\ge 1), and every unilateral deviation (\tau_i),

1. along the honest profile,
   [
   \mathbb E_{G,s,\widehat\sigma^s}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
   \ge
   T\rho_i^s - 2B_s - \sum_{t=1}^T \eta_t;
   \tag{H_i^T}
   ]
2. along any unilateral deviation,
   [
   \mathbb E_{G,s,(\tau_i,\widehat\sigma^s_{-i})}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
   \le
   T\rho_i^s + 2B_s + \sum_{t=1}^T \eta_t.
   \tag{D_i^T}
   ]

**Dependencies.**
L5, L6, and the boundedness (|b^s(h)|\le B_s).

**Technique hint.**
Sum the one-step inequalities ((E_h^i)) and ((D_h^i)) along the realized history. The bias terms telescope, leaving only the initial and terminal biases, hence the (2B_s) endpoint cost. This is one of the durable stable steps of the route. 

**Difficulty.**
Moderate.

---

### [BREAKDOWN_AMEND L8] Horizon bookkeeping from telescoping to (\varepsilon)-incentives

**Statement.**
Assume L7 and choose the leakage sequence so that (\sum_{t\ge 1}\eta_t\le \varepsilon/4). Then for each initial state (s) there exists
[
T_0(s)\in \mathbb N
]
such that for all (T\ge T_0(s)), all players (i), and all unilateral deviations (\tau_i),
[
\gamma_i^T(G,s,\widehat\sigma^s)
\ge
\gamma_i^T(G,s,(\tau_i,\widehat\sigma^s_{-i}))-\varepsilon.
]
For example, any (T_0(s)) satisfying
[
\frac{4B_s}{T_0(s)}\le \frac{\varepsilon}{2}
]
is enough after dividing the L7 sum inequalities by (T).

**Dependencies.**
L7 and the explicit nonnegativity / summability of ((\eta_t)).

**Technique hint.**
Divide the L7 inequalities by (T). The terminal-bias cost is (O(B_s/T)), and the leakage contributes at most ((1/T)\sum_{t=1}^T\eta_t), which is uniformly small once the total leakage budget is fixed. This is exactly the bookkeeping step the route memo marks as stable once (\eta_t\ge 0) is stated explicitly. 

**Difficulty.**
Easy to moderate.

---

### [BREAKDOWN_AMEND L9] Global assembly from rooted families (\widehat\sigma^s) to one whole-game profile

**Statement.**
Assume L8 for every root state (s\in S). Then there exists a **single** behavioral strategy profile
[
\sigma\in\Sigma(G)
]
such that for every public history (h) ending at state (q=s(h)), the continuation of (\sigma) from (h) agrees with the re-rooted continuation profile built for (q). In particular, if each rooted profile (\widehat\sigma^s) is a uniform (\varepsilon)-equilibrium from root (s), then the assembled profile (\sigma) satisfies the same equilibrium inequalities from **every** initial state of the original game.

Moreover, because (S) is finite, one can set
[
T_0 := \max_{s\in S} T_0(s).
]

**Dependencies.**
L5 through L8.

**Technique hint.**
This step must be written explicitly, because the route memo flags it as missing in the earlier run. The clean version is: define the whole-game strategy by public-history recursion, not by keeping separate root-indexed objects forever. At each history, look only at the current state and local continuation data already assigned on the appropriate rooted tree.

**Difficulty.**
Moderate. It is not the hard math, but it is logically indispensable. 

---

### [BREAKDOWN_AMEND L10] Final theorem synthesis

**Statement.**
Assume L1 through L9. Then for every finite stochastic game (G) and every (\varepsilon>0), there exist a behavioral profile (\sigma\in\Sigma(G)) and a threshold (T_0\in\mathbb N_{>0}) such that for every horizon (T\ge T_0), every initial state (s_1\in S), every player (i\in N), and every unilateral deviation (\tau_i\in\Sigma_i(G)),
[
\gamma_i^T(G,s_1,\sigma)
\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Hence (G) has a uniform (\varepsilon)-equilibrium.

**Dependencies.**
L8 and L9.

**Technique hint.**
Take the global profile from L9 and the common horizon threshold (T_0=\max_s T_0(s)). Then the exact theorem-side quantifiers from the claim file are satisfied.

**Difficulty.**
Easy once the previous lemmas are genuinely in place.

---

## Critical lemma

### [BREAKDOWN_AMEND C1] Central bottleneck

The critical lemma is **L4**.

Everything after L4 is mostly downstream engineering:

* L5 is rooted-tree recursion once a local selector exists.
* L7 is telescoping once bounded biases exist.
* L8 is bookkeeping once leakage is summable.
* L9 is a required but conceptually routine assembly step.

By contrast, L4 asks for the missing theorem-sized upgrade from Martin-function continuation data, acceptable profiles, or correlated / solvable-subgame outputs to a **single uncorrelated one-step selector** at every history. The durable route memo explicitly warns that this may just be the open problem in disguise. 

---

## Glue steps from lemmas to theorem

### [BREAKDOWN_AMEND G1] Local invariant package

Use L1 and L2 to define the admissible continuation object (W^s(h)), then L3 to formalize the local feasible-set map (\mathcal F^s(h,b)). L4 closes the local invariant by proving nonemptiness of every such feasible set.

### [BREAKDOWN_AMEND G2] Rooted strategy construction

Apply L5 to choose a full rooted public-history selector ((x^s,b^s)) on each tree (H^s). Then repair L6 so deviations are actually controlled on realized public histories.

### [BREAKDOWN_AMEND G3] Finite-horizon incentive bounds

Use L7 to telescope the one-step inequalities into horizon-(T) payoff bounds with only endpoint-bias and leakage errors. Apply L8 to convert those bounds into uniform (\varepsilon)-equilibrium inequalities from each root (s).

### [BREAKDOWN_AMEND G4] Quantifier-correct whole-game conclusion

Use L9 to assemble the root-indexed family into one global behavioral profile (\sigma), and use L10 to obtain the exact theorem statement:
one (\sigma), one (T_0), all (T\ge T_0), every initial state, every player, every unilateral deviation. This preserves the theorem-side scope required by the durable claim source.  

---

## Minimal dependency DAG

[
L1 \to L2 \to L3 \to L4 \to L5 \to L6 \to L7 \to L8 \to L9 \to L10.
]

Two annotations matter:

1. **L4 is the research bottleneck.**
2. **L6 needs statement repair** before the downstream telescoping argument can honestly bear the full incentive load.

---

## Practical edit points for the next pass

### [BREAKDOWN_AMEND P1]

Do not let any later bookkeeping lemma masquerade as progress on the open theorem unless L4 is actually solved or replaced by a theorem of equal strength.

### [BREAKDOWN_AMEND P2]

When proving L2 or L6, demand explicit source-to-statement matching. If the cited Martin-function source gives only correlated objects, acceptable profiles, or a solvable subgame, record that mismatch immediately rather than silently upgrading it.

### [BREAKDOWN_AMEND P3]

Keep L9 explicit. The theorem requires one whole-game behavioral profile, not merely a family ({\widehat\sigma^s}_{s\in S}) indexed by initial state. The route memo identifies this assembly step as necessary. 

### [BREAKDOWN_AMEND P4]

Keep the theorem labeled **open/bootstrap** throughout unless L4 and the repaired L6 are genuinely discharged. That is the durable project status.

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

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_06.md

# Reviewer Output

Generated: 2026-03-23T22:39:55.081408+00:00

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

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_07.md

# Reviewer Output

Generated: 2026-03-24T00:16:24.550924+00:00

## VERDICT: PATCH_BIG

The branch is not a redo. There is real progress, and it stays inside the correct theorem-side target: one public-history behavioral profile, valid for all sufficiently large horizons and every initial state, with the theorem still treated as bootstrap/open rather than solved. That matches the durable problem statement, proof-state anchor, and route memo.    

## Step review

**Setup:** not valid for the intended downstream use. The amended Setup in prover_07 writes
[
w_i^s+b_{h,i}\le \mathbb E!\left[u_i+w_i^s+\beta_h(H')*i\right]+\eta(h),
]
and then cancels (w_i^s), leaving
[
b*{h,i}\le \mathbb E!\left[u_i+\beta_h(H')_i\right]+\eta(h),
]
with the analogous deviation inequality. After that cancellation, the fixed promise (w^s) disappears from the local relation. So this Setup cannot support a telescope centered at (w_i^s). Under this Setup, the strongest available downstream statement is the earlier weak telescope involving visited promises or bias differences, not the claimed corrected (L7'). This is the main defect. 

**L1:** valid. The continuation game after a public history is canonically the same finite stochastic game started from the terminal state, and the finite-horizon best-response value is well defined because only finitely many continuation histories up to horizon (T) matter. No scope problem here. 

**L3*:** essentially valid as a compactness and heredity lemma, conditional on imported L2 and whichever amended Setup is actually adopted. The ambient bias-fiber product is compact, the defining inequalities are continuous, and heredity is immediate from the definition of (F^*). But this only proves compactness for the local problem currently stated; it does not fix the missing (w^s)-term needed by the corrected telescope. 

**L4*:** still open, and still the theorem-sized selector step. The packet is right to keep this as the bottleneck, and the durable route memo says the same.  

**L5*:** valid conditional on L2 and L4*. The root choice correctly uses L2, the construction is over the full rooted tree rather than only on-path histories, unique predecessors prevent clashes, and the global gluing
[
\sigma(h)=\sigma^{s_1}(h)
]
is the right way to obtain one whole-game behavioral profile. This matches the durable route memo’s positive takeaway.  

**Literal L6 / G3:** acceptable only as explicit global assembly. It must not be cited as a non-vacuous punishment-mode mechanism; that stronger reading still lacks remembered anchor history. The packet correctly warns about this, and the durable memo agrees.  

**G4 / corrected (L7'):** unsupported as currently cited. Prover_07’s status summary points to a “corrected (L7')” downstream, but the only corrected (L7') proof earlier in the packet uses a different fixed-promise local relation, namely one of the form
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h\right]\ge w_i^s-\eta_t
]
and the deviation counterpart
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h,\text{dev}\right]\le w_i^s+\eta_t,
]
not the canceled-(w^s) relation now written in the Setup amendment. So the current packet contains a dependency mismatch: the Setup of prover_07 does not justify the corrected telescope it cites. 

**G5 / corrected (L8'):** downstream bookkeeping is fine only after G4 is repaired. At present it hangs from an unsupported telescope. 

## Citation and dependency errors

1. The packet cannot cite the old variable-promise (L7') as proved. Prover_05 and prover_06 correctly diagnosed that the variable-promise data only give a weak telescope involving the visited promise process, not the root promise. 

2. Prover_07 then cites a corrected fixed-promise (L7'), but its own amended Setup is not the one that proof needs. That is the main citation error in the current branch state. 

3. L2 remains imported, not locally proved, so all compactness and fiber arguments must keep L2 explicit in the dependency list. The current packet mostly does this correctly. 

4. There are still small notation defects in several displayed formulas, but those are secondary. The decisive issue is the algebraic mismatch above, not typography. 

## [SCOPE] compliance

[SCOPE] The theorem-side scope is preserved. The packet still targets the exact durable claim: one behavioral strategy profile, valid for all sufficiently large horizons, for every initial state, in the strategy-existence formulation rather than a payoff-set downgrade.  

[SCOPE] The shift from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)) is a real route-level scope change, not a cosmetic proof edit. It must be recorded as a statement replacement throughout the backbone. The packet itself already flags scope changes, so this is allowed, but it must be treated explicitly. 

[SCOPE] L4* replaces L4 as the genuine open selector theorem. Any downstream text that still treats old L4 as the relevant bottleneck is stale. 

[SCOPE] L6 must remain downgraded to literal global assembly unless the public state is enriched to remember punishment anchors. Do not silently re-upgrade it later.  

## Required patch set

1. Replace prover_07’s amended Setup by the actual fixed-promise local inequalities needed for the root-promise telescope. Concretely, the local relation must be
   [
   \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')*i\right]-b*{h,i}\ge w_i^s-\eta(h),
   ]
   and
   [
   \mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]-b*{h,i}\le w_i^s+\eta(h).
   ]
   These are **not** equivalent to the current canceled-(w^s) formulas. 

2. Re-state L3*, L4*, L5*, G4, and G5 against that exact local relation. The current L3* compactness proof and L5* recursion proof should survive with only notational edits. 

3. Keep L6 cited only as literal assembly. 

4. Keep the theorem labeled bootstrap/open until L4* is actually proved. The durable proof-state anchor and route memo both require that discipline.  

## Bottom line

There is genuine progress here: L1 is in good shape, the full-tree recursion and gluing point is now explicit, and the branch has correctly isolated the fixed-promise selector as the research bottleneck. But the packet has **not** yet cleanly repaired the post-L4 tail, because the newest Setup amendment does not match the corrected telescope it wants to invoke. That is a restructuring issue, not a one-line fix. So the right reviewer outcome is **PATCH_BIG**.

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_08.md

# Reviewer Output

Generated: 2026-03-24T01:02:45.180804+00:00

## VERDICT: PATCH_BIG

The branch is not a redo. There is real progress, and it stays inside the correct theorem-side target: one public-history behavioral profile, valid for all sufficiently large horizons and every initial state, with the theorem still treated as bootstrap/open rather than solved. That matches the durable problem statement, proof-state anchor, and route memo.    

## Step review

**Setup:** not valid for the intended downstream use. The amended Setup in prover_07 writes
[
w_i^s+b_{h,i}\le \mathbb E!\left[u_i+w_i^s+\beta_h(H')*i\right]+\eta(h),
]
and then cancels (w_i^s), leaving
[
b*{h,i}\le \mathbb E!\left[u_i+\beta_h(H')_i\right]+\eta(h),
]
with the analogous deviation inequality. After that cancellation, the fixed promise (w^s) disappears from the local relation. So this Setup cannot support a telescope centered at (w_i^s). Under this Setup, the strongest available downstream statement is the earlier weak telescope involving visited promises or bias differences, not the claimed corrected (L7'). This is the main defect. 

**L1:** valid. The continuation game after a public history is canonically the same finite stochastic game started from the terminal state, and the finite-horizon best-response value is well defined because only finitely many continuation histories up to horizon (T) matter. No scope problem here. 

**L3*:** essentially valid as a compactness and heredity lemma, conditional on imported L2 and whichever amended Setup is actually adopted. The ambient bias-fiber product is compact, the defining inequalities are continuous, and heredity is immediate from the definition of (F^*). But this only proves compactness for the local problem currently stated; it does not fix the missing (w^s)-term needed by the corrected telescope. 

**L4*:** still open, and still the theorem-sized selector step. The packet is right to keep this as the bottleneck, and the durable route memo says the same.  

**L5*:** valid conditional on L2 and L4*. The root choice correctly uses L2, the construction is over the full rooted tree rather than only on-path histories, unique predecessors prevent clashes, and the global gluing
[
\sigma(h)=\sigma^{s_1}(h)
]
is the right way to obtain one whole-game behavioral profile. This matches the durable route memo’s positive takeaway.  

**Literal L6 / G3:** acceptable only as explicit global assembly. It must not be cited as a non-vacuous punishment-mode mechanism; that stronger reading still lacks remembered anchor history. The packet correctly warns about this, and the durable memo agrees.  

**G4 / corrected (L7'):** unsupported as currently cited. Prover_07’s status summary points to a “corrected (L7')” downstream, but the only corrected (L7') proof earlier in the packet uses a different fixed-promise local relation, namely one of the form
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h\right]\ge w_i^s-\eta_t
]
and the deviation counterpart
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h,\text{dev}\right]\le w_i^s+\eta_t,
]
not the canceled-(w^s) relation now written in the Setup amendment. So the current packet contains a dependency mismatch: the Setup of prover_07 does not justify the corrected telescope it cites. 

**G5 / corrected (L8'):** downstream bookkeeping is fine only after G4 is repaired. At present it hangs from an unsupported telescope. 

## Citation and dependency errors

1. The packet cannot cite the old variable-promise (L7') as proved. Prover_05 and prover_06 correctly diagnosed that the variable-promise data only give a weak telescope involving the visited promise process, not the root promise. 

2. Prover_07 then cites a corrected fixed-promise (L7'), but its own amended Setup is not the one that proof needs. That is the main citation error in the current branch state. 

3. L2 remains imported, not locally proved, so all compactness and fiber arguments must keep L2 explicit in the dependency list. The current packet mostly does this correctly. 

4. There are still small notation defects in several displayed formulas, but those are secondary. The decisive issue is the algebraic mismatch above, not typography. 

## [SCOPE] compliance

[SCOPE] The theorem-side scope is preserved. The packet still targets the exact durable claim: one behavioral strategy profile, valid for all sufficiently large horizons, for every initial state, in the strategy-existence formulation rather than a payoff-set downgrade.  

[SCOPE] The shift from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)) is a real route-level scope change, not a cosmetic proof edit. It must be recorded as a statement replacement throughout the backbone. The packet itself already flags scope changes, so this is allowed, but it must be treated explicitly. 

[SCOPE] L4* replaces L4 as the genuine open selector theorem. Any downstream text that still treats old L4 as the relevant bottleneck is stale. 

[SCOPE] L6 must remain downgraded to literal global assembly unless the public state is enriched to remember punishment anchors. Do not silently re-upgrade it later.  

## Required patch set

1. Replace prover_07’s amended Setup by the actual fixed-promise local inequalities needed for the root-promise telescope. Concretely, the local relation must be
   [
   \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')*i\right]-b*{h,i}\ge w_i^s-\eta(h),
   ]
   and
   [
   \mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]-b*{h,i}\le w_i^s+\eta(h).
   ]
   These are **not** equivalent to the current canceled-(w^s) formulas. 

2. Re-state L3*, L4*, L5*, G4, and G5 against that exact local relation. The current L3* compactness proof and L5* recursion proof should survive with only notational edits. 

3. Keep L6 cited only as literal assembly. 

4. Keep the theorem labeled bootstrap/open until L4* is actually proved. The durable proof-state anchor and route memo both require that discipline.  

## Bottom line

There is genuine progress here: L1 is in good shape, the full-tree recursion and gluing point is now explicit, and the branch has correctly isolated the fixed-promise selector as the research bottleneck. But the packet has **not** yet cleanly repaired the post-L4 tail, because the newest Setup amendment does not match the corrected telescope it wants to invoke. That is a restructuring issue, not a one-line fix. So the right reviewer outcome is **PATCH_BIG**.

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

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md` (108 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (20075 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_01.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_02.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_03.md` (15695 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_04.md` (15204 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_05.md` (19004 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_06.md` (19004 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_07.md` (18403 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_08.md` (18403 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (74 chars)

