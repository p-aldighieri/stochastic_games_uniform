# External Agent Request (reviewer)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-24T02:45:30.433999+00:00

## Instructions

Check each proof step for logical validity, completeness, and correct citations. Check scope compliance. Issue a structured verdict: VERDICT: PASS (correct and complete), VERDICT: PATCH_SMALL (minor fixable issues), VERDICT: PATCH_BIG (needs restructuring), or VERDICT: REDO (fundamentally flawed approach). Be precise about errors. Tag scope changes with [SCOPE].

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
- The downstream proof should use the **increment form** of the current breakdown’s local invariant and should stop citing the canceled-promise formulas from the superseded prover_07 setup. The current breakdown already has a fixed root promise (\rho^s) and a varying bias (b^s(h)):
- The L5 proof does **not** need a Kőnig-style compactness limit once L4 is available on the full rooted tree. Direct recursion on depth is enough. Also, L5 must cite L2 for the root bias choice. This matches the accepted amendment and the stable route-memo takeaway.
- Demote L6 to the **literal** statement that L5 defines a rooted behavioral profile. Do not cite L6 as a nonvacuous punishment-mode mechanism unless the public state is enlarged to remember punishment anchors. The route memo explicitly warns that the current stronger punishment reading is too weak / vacuous.
- Replace the current L7 by the following corrected lemma. Its proof uses only L2 and the full-tree L5 selector; L6 is not needed.
- Replace the current L8 by the corrected bookkeeping lemma below, with explicit use of (\eta_t\ge 0).
- The present L9 asks for a stronger current-state re-rooting compatibility:
- Replace the downstream backbone by

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

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_07.md

# Prover Output

Generated: 2026-03-23T23:52:03.887526+00:00

[BREAKDOWN_AMEND]
Target: Setup
Replace statement: Introduce fixed-promise bias fibers. For each public history (h) and promise vector (w\in[0,1]^N), define
[
B(h,w):={,b\in[-B,B]^N:(w,b)\in Z(h),}.
]
For a rooted construction with root state (s) and chosen root promise (w^s), the local feasibility object at a history (h) is now a bias-fiber feasibility set
[
F^*(h,w^s,b_h)
]
for (b_h\in B(h,w^s)), consisting of pairs ((x_h,\beta_h)) such that

1. (x_h=\bigotimes_{i\in N}x_{h,i}\in \prod_i \Delta(A_i(s(h))));
2. for every child history (h'=(h,a,s')), (\beta_h(h')\in B(h',w^s));
3. for every player (i) and every pure one-step deviation (a_i'\in A_i(s(h))),
   [
   w_i^s+b_{h,i}\le
   \mathbb E_{x_h,P}!\left[u_i(s(h),a)+w_i^s+\beta_h(H')*i\right]+\eta(h),
   ]
   [
   \mathbb E*{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+w_i^s+\beta_h(H'^{a_i'})*i\right]
   \le w_i^s+b*{h,i}+\eta(h).
   ]
   Equivalently, after cancelling the fixed scalar (w_i^s),
   [
   b_{h,i}\le \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')*i\right]+\eta(h),
   ]
   [
   \mathbb E*{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]
   \le b*{h,i}+\eta(h).
   ]

New dependencies: L2
Technique update: Freeze the promise coordinate along each rooted public-history tree and let only the bias vary. This is the upstream repair required for any root-promise telescope.
Downstream changes: Replace L3 by L3*, L4 by L4*, L5 by L5*, rewrite G3-G5 to use the fixed-promise backbone, and interpret L7' only in that amended system.
Reason: In the current variable-promise system the visited promise process does not telescope to the root promise, so the displayed downstream L7'/L8' cannot be obtained.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L3
Replace statement: **L3*. Compactness and heredity of the fixed-promise local feasibility problem.**
Fix a history (h), a promise vector (w\in[0,1]^N), and a current bias (b_h\in B(h,w)). Then
[
F^*(h,w,b_h)
]
is a closed subset of
[
\left(\prod_{i\in N}\Delta(A_i(s(h)))\right)\times
\left(\prod_{h'\text{ child of }h} B(h',w)\right).
]
Hence (F^*(h,w,b_h)) is compact whenever it is nonempty. Moreover, if ((x_h,\beta_h)\in F^*(h,w,b_h)), then every child bias (\beta_h(h')) lies in (B(h',w)), so the same construction may be iterated at descendants with the same fixed promise (w).

New dependencies: L2, Setup
Technique update: Use compact bias fibers instead of variable promise-bias pairs.
Downstream changes: L4, L5, G3-G5, L7'
Reason: This is the correct local well-posedness statement for the fixed-promise route.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L4
Replace statement: **L4*. One-step uncorrelated fixed-promise self-generation at every history.**
For every public history (h), every promise vector (w\in[0,1]^N), and every current bias (b_h\in B(h,w)), the local feasibility set (F^*(h,w,b_h)) is nonempty.

Equivalently, every admissible fixed promise-bias label at a node admits

1. a product mixed action (x_h=\bigotimes_i x_{h,i}), and
2. a choice of child biases (\beta_h(h')\in B(h',w)) for all immediate descendants,

such that no player can gain more than (\eta(h)) from a one-step unilateral deviation.

New dependencies: L2, L3*
Technique update: This is the true selector bottleneck after the fixed-promise repair.
Downstream changes: L5, G3-G5, L7'
Reason: The old L4 is not the right upstream input for the corrected telescope.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L5
Replace statement: **L5*. Recursive assembly on the full rooted public-history tree with fixed promise.**
Assume L2 and L4*. For each initial state (s), choose one root pair
[
(w^s,b^s)\in Z(s).
]
Then there exist

1. for each initial state (s), a rooted behavioral profile (\sigma^s) defined on the full public-history tree rooted at (s), and
2. for each rooted history (h) with root (s), a bias (\beta^s(h)\in B(h,w^s)),

such that for every rooted history (h), the pair consisting of the mixed action prescribed by (\sigma^s) at (h) and the child-bias assignment at the children of (h) belongs to
[
F^*(h,w^s,\beta^s(h)).
]

Defining
[
\sigma(h):=\sigma^{s_1}(h)\qquad\text{for }h=(s_1,a_1,\dots,s_t),
]
yields one whole-game behavioral profile (\sigma) on the union of all public histories.

New dependencies: L2, L4*
Technique update: Build rooted profiles first, then glue them by initial state.
Downstream changes: G3-G5, L7', L8'
Reason: The theorem target needs one global profile, while the deviation analysis needs the full rooted tree, not only on-path histories.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G3
Replace statement: **G3. Build rooted fixed-promise trees and glue them globally.**
Assuming L4*, apply L5* to each initial state (s) using a chosen root pair ((w^s,b^s)\in Z(s)). This yields rooted profiles (\sigma^s) and rooted bias assignments (\beta^s). Then define the single whole-game profile by (\sigma(h):=\sigma^{s_1}(h)) for (h=(s_1,a_1,\dots,s_t)).

New dependencies: L2, L4*, L5*
Technique update: Use the explicit global assembly step.
Downstream changes: G4, G5
Reason: The global profile must be written down explicitly.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G4
Replace statement: **G4. Verify deviations by the corrected fixed-promise telescope.**
After G3, do not use the old variable-promise L7. Instead prove the corrected L7' from the fixed-promise objects built in L5*: the same root promise (w^s) is used all along the rooted tree, so only bias terms remain to telescope.

New dependencies: L2, L5*, corrected L7'
Technique update: Root-promise telescope, not visited-promise averaging.
Downstream changes: G5
Reason: The previous G4 invoked a downstream statement not supported by the current setup.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G5
Replace statement: **G5. Uniformize in the horizon using corrected L8'.**
Use corrected L8', with the standing hypothesis (\eta_t\ge 0), to choose (T_0) so that the endpoint bias residue is at most (\varepsilon/2) and the leakage sum is at most (\varepsilon/2).

New dependencies: corrected L8'
Technique update: Pure bookkeeping after the corrected telescope.
Downstream changes: none
Reason: The old G5 depended on an unrepaired downstream chain.
[/BREAKDOWN_AMEND]

## L1. Subgame reduction from histories to terminal states

**Claim.** For every public history (h), the continuation game after (h) is canonically identified with the original stochastic game started from the terminal state (s(h)).

**Proof.**

Fix a finite stochastic game
[
G=(N,S,(A_i)*{i\in N},u,P)
]
in the sense of the formal target. Fix a public history
[
h=(s_1,a_1,s_2,a_2,\dots,a*{t-1},s_t),
]
and write
[
s(h):=s_t.
]

Define the continuation game (G_h) as follows:

* same player set (N);
* same state set (S);
* for each player (i) and state (s), same action set (A_i(s));
* same stage payoff function (u);
* same transition kernel (P);
* initial state equal to (s(h)).

This is a direct use of the model definition: after a public history, the only state variable relevant to future play is the terminal state of that history. No past action or past state enters either the stage payoff function or the transition kernel except through the current state. [DERIVED]

Now define the shift map on future histories. A future public history after (h) has the form
[
(h,s_t,a_t,s_{t+1},a_{t+1},\dots,a_{t+k-1},s_{t+k}).
]
Delete the fixed prefix (h). This yields
[
(s_t,a_t,s_{t+1},a_{t+1},\dots,a_{t+k-1},s_{t+k}),
]
which is exactly a public history of length (k+1) in the game (G_h) started at (s(h)=s_t). Conversely, every public history in (G_h) started from (s_t) extends uniquely to a continuation history after (h) in (G) by reattaching the prefix (h). Therefore there is a bijection between continuation histories after (h) in (G) and histories in (G_h). [DERIVED]

Next compare laws of play. Let (\sigma) be any behavioral profile in (G). Its restriction to histories extending (h) determines a behavioral profile in (G_h) under the above identification. Conversely, every behavioral profile in (G_h) pulls back to a continuation profile after (h) in (G). At every future stage, the conditional distribution of the next state given the current continuation history and current action profile is
[
P(\cdot\mid s,a)
]
in both descriptions, by direct inspection of the model definition. Also the stage payoff at that stage is
[
u_i(s,a)
]
in both descriptions. Therefore the induced probability law on future plays and the induced future payoff process are identical under the history-shift identification. [DERIVED]

Hence every state-indexed object in the original game can be pulled back to histories ending in that state: if (Q(s)) is any object depending only on the continuation game from state (s), define
[
Q(h):=Q(s(h)).
]
This applies in particular to statewise maxmin values, punishment correspondences, Martin correspondences, continuation selectors, and any other continuation object defined from the subgame started at a state. [DERIVED]

So L1 is proved. [DERIVED]

---

## L3*. Compactness and heredity of the fixed-promise local feasibility problem

I will prove the amended L3* conditionally on the amended setup and imported compactness from L2.

Fix a history (h), a promise vector (w\in[0,1]^N), and a current bias (b_h\in B(h,w)).

### Step 1: the ambient domain is a finite product of compact sets

For each player (i), the action set (A_i(s(h))) is finite by the game definition. Therefore the simplex
[
\Delta(A_i(s(h)))
]
is a nonempty compact subset of a finite-dimensional Euclidean space. This is a standard theorem on simplices over finite sets. [DERIVED]

The set of children of (h) is finite, because a child is determined by a current action profile (a\in A(s(h))) and a next state (s'\in S), and both (A(s(h))) and (S) are finite. [DERIVED]

By the amended setup,
[
B(h',w)={b\in[-B,B]^N:(w,b)\in Z(h')}.
]
Under L2, each (Z(h')\subseteq [0,1]^N\times[-B,B]^N) is compact. Intersecting (Z(h')) with the closed slice ({w}\times[-B,B]^N) gives a compact set, and projecting that slice-identification to the bias coordinate yields (B(h',w)) compact whenever nonempty. [DERIVED]

Therefore the ambient set
[
X(h,w):=\left(\prod_{i\in N}\Delta(A_i(s(h)))\right)\times
\left(\prod_{h'\text{ child of }h} B(h',w)\right)
]
is compact, because it is a finite product of compact sets. [DERIVED]

### Step 2: the defining inequalities are continuous

Write a generic point of (X(h,w)) as ((x_h,\beta_h)).

For each player (i), the obedient inequality in (F^*(h,w,b_h)) is
[
b_{h,i}\le \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')_i\right]+\eta(h).
]
The right-hand side is a finite sum over current action profiles (a) and next states (s'), with coefficients equal to products of mixed-action coordinates and transition probabilities. Since mixed-action coordinates enter multilinearly and the child-bias coordinates enter linearly, this right-hand side is a continuous function of ((x_h,\beta_h)). [DERIVED]

For each player (i) and pure deviation (a_i'\in A_i(s(h))), the deviating inequality is
[
\mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]
\le b*{h,i}+\eta(h).
]
Again, the left-hand side is a finite multilinear-linear expression in the coordinates of ((x_h,\beta_h)), hence continuous. [DERIVED]

There are only finitely many such inequalities, because both (N) and all (A_i(s(h))) are finite. [DERIVED]

### Step 3: the feasible set is closed

Each obedient inequality defines a closed subset of (X(h,w)), as the preimage of ((-\infty,0]) under a continuous function. The same is true for each deviating inequality. Taking the finite intersection of these closed subsets, we conclude that
[
F^*(h,w,b_h)
]
is closed in (X(h,w)). [DERIVED]

Since (X(h,w)) is compact by Step 1, every closed subset of (X(h,w)) is compact. Therefore (F^*(h,w,b_h)) is compact whenever it is nonempty. [DERIVED]

### Step 4: heredity

If ((x_h,\beta_h)\in F^*(h,w,b_h)), then by definition of (F^*), for every child history (h') we have
[
\beta_h(h')\in B(h',w).
]
That is exactly the hereditary property needed to iterate the same fixed-promise construction at descendants. [DERIVED]

So amended L3* is proved, conditional on the amended setup and imported L2. [DERIVED]

---

## L5*. Recursive assembly on the full rooted public-history tree with fixed promise

I will prove the amended L5* conditional on L2 and amended L4*.

### Step 1: choose root labels

Fix an initial state (s\in S). By L2, (Z(s)) is nonempty. Therefore we may choose
[
(w^s,b^s)\in Z(s).
]
By definition of the bias fiber,
[
b^s\in B((s),w^s),
]
where ((s)) denotes the root history consisting only of the initial state (s). [DERIVED]

This root choice uses L2, not L4*. [DERIVED]

### Step 2: define the rooted tree

Let (H^s) denote the full rooted public-history tree starting from state (s). Its vertices are all public histories
[
h=(s,a_1,s_2,\dots,a_{t-1},s_t)
]
whose first state is (s). Every non-root history in (H^s) has a unique predecessor, obtained by deleting the final action-state pair. [DERIVED]

This uniqueness of predecessor is a direct property of history sequences. [DERIVED]

### Step 3: inductive finite-level construction

I now construct, by induction on depth, a consistent family of local witnesses on (H^s).

For depth (0), assign the root bias
[
\beta^s((s)):=b^s.
]
Since (\beta^s((s))\in B((s),w^s)), L4* applies at the root. Therefore there exists
[
(x_{(s)},\beta_{(s)}^{\mathrm{child}})\in F^*((s),w^s,b^s).
]
Define the rooted strategy at the root by
[
\sigma^s((s)):=x_{(s)},
]
and for every child (h') of the root define
[
\beta^s(h'):=\beta_{(s)}^{\mathrm{child}}(h').
]
By definition of (F^*), each such child bias lies in (B(h',w^s)). [DERIVED]

Now suppose by induction that for all histories in (H^s) of depth at most (n), we have already assigned:

1. a bias (\beta^s(h)\in B(h,w^s)), and
2. a mixed action (\sigma^s(h)) at every history of depth at most (n-1),

so that for every history (g) of depth at most (n-1), the chosen action (\sigma^s(g)) together with the chosen child-bias assignment at its children forms an element of
[
F^*(g,w^s,\beta^s(g)).
]

Take any history (h) of depth (n). By the induction hypothesis,
[
\beta^s(h)\in B(h,w^s).
]
Therefore L4* applies to ((h,w^s,\beta^s(h))), and yields some witness
[
(x_h,\beta_h^{\mathrm{child}})\in F^*(h,w^s,\beta^s(h)).
]
Define
[
\sigma^s(h):=x_h,
]
and for each child (h') of (h) define
[
\beta^s(h'):=\beta_h^{\mathrm{child}}(h').
]
Again, the definition of (F^*) guarantees
[
\beta^s(h')\in B(h',w^s).
]
This extends the construction to depth (n+1). [DERIVED]

By induction on (n\in\mathbb N), we obtain a consistent assignment on all finite depths of the rooted tree (H^s). [DERIVED]

### Step 4: consistency

There is no conflict in the construction because every non-root history (h\in H^s) has a unique predecessor. Hence the value (\beta^s(h)) is assigned exactly once, namely when the local witness at its predecessor is chosen. Likewise, (\sigma^s(h)) is assigned exactly once, namely when L4* is applied at (h). [DERIVED]

Thus the union over finite depths is well-defined. [DERIVED]

### Step 5: conclusion for one root

We have constructed:

* a behavioral profile (\sigma^s) on the full rooted tree (H^s);
* a bias assignment (\beta^s(h)\in B(h,w^s)) for every (h\in H^s);

such that for every (h\in H^s), the local data chosen at (h) belongs to
[
F^*(h,w^s,\beta^s(h)).
]
So the rooted fixed-promise version of L5 holds for the single initial state (s). [DERIVED]

### Step 6: glue all roots into one whole-game profile

Repeat Step 1 through Step 5 for every initial state (s\in S). Since (S) is finite, this yields a finite family ((\sigma^s)_{s\in S}). [DERIVED]

Now define a global behavioral profile (\sigma) on the union of all public histories by
[
\sigma(h):=\sigma^{s_1}(h)
\qquad\text{for }h=(s_1,a_1,\dots,s_t).
]
This is well-defined because the first state (s_1) of the history uniquely determines which rooted tree (H^{s_1}) contains (h). Histories with different first states lie in disjoint rooted trees. [DERIVED]

Therefore (\sigma) is one whole-game behavioral profile, not a mere family indexed by initial states. [DERIVED]

So amended L5* is proved conditional on L2 and L4*. [DERIVED]

---

## Explicit gap report

1. **L2 remains imported, not proved here.**
   The current packet treats the Martin/maxmin seed layer as external machinery. I do not upgrade it to [DERIVED]. [ASSUMPTION-]

2. **L4* remains open.**
   After the fixed-promise repair, the selector theorem that actually matters is the amended L4*, not the original variable-promise L4. I do not prove it here. This remains the theorem-sized bottleneck. [ASSUMPTION-]

3. **Current variable-promise L7' is unavailable.**
   The existing local relation propagates successor biases but not a fixed successor promise, so the visited promises do not telescope to the root promise. Hence the current downstream L7'/L8' chain is not derivable without the above amendment. [DERIVED]

4. **L6 should be retained only literally.**
   Nothing proved here supplies a non-vacuous punishment-mode mechanism with remembered punishment anchor. Any stronger reading remains unsupported. [DERIVED]

---

## Status summary

* [DERIVED] **L1**: proved explicitly.
* [DERIVED] **L3***: proved explicitly, conditional on imported L2 and the amended fixed-promise setup.
* [DERIVED] **L5***: proved explicitly, conditional on L2 and open L4*.
* [DERIVED] Current packet requires an upstream repair from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)).
* [DERIVED] The global assembly step from rooted profiles (\sigma^s) to one whole-game profile (\sigma) is explicit and correct in the amended system.
* [ASSUMPTION-] **L2** remains imported.
* [ASSUMPTION-] **L4*** remains open and is the central unresolved selector theorem.
* [DERIVED] Therefore the theorem remains **bootstrap/open**, and the correct current backbone is
  [
  L1 \to \text{imported }L2 \to L3^* \to \text{open }L4^* \to L5^* \to \text{literal }L6 \to \text{corrected }L7' \to L8'.
  ]

This advances the branch by clearing the local compactness and full-tree recursion pieces in the **corrected** fixed-promise framework, while explicitly isolating the remaining open selector step.

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_08.md

# Prover Output

Generated: 2026-03-24T01:02:45.165375+00:00

[BREAKDOWN_AMEND]
Target: Setup
Replace statement: Introduce fixed-promise bias fibers. For each public history (h) and promise vector (w\in[0,1]^N), define
[
B(h,w):={,b\in[-B,B]^N:(w,b)\in Z(h),}.
]
For a rooted construction with root state (s) and chosen root promise (w^s), the local feasibility object at a history (h) is now a bias-fiber feasibility set
[
F^*(h,w^s,b_h)
]
for (b_h\in B(h,w^s)), consisting of pairs ((x_h,\beta_h)) such that

1. (x_h=\bigotimes_{i\in N}x_{h,i}\in \prod_i \Delta(A_i(s(h))));
2. for every child history (h'=(h,a,s')), (\beta_h(h')\in B(h',w^s));
3. for every player (i) and every pure one-step deviation (a_i'\in A_i(s(h))),
   [
   w_i^s+b_{h,i}\le
   \mathbb E_{x_h,P}!\left[u_i(s(h),a)+w_i^s+\beta_h(H')*i\right]+\eta(h),
   ]
   [
   \mathbb E*{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+w_i^s+\beta_h(H'^{a_i'})*i\right]
   \le w_i^s+b*{h,i}+\eta(h).
   ]
   Equivalently, after cancelling the fixed scalar (w_i^s),
   [
   b_{h,i}\le \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')*i\right]+\eta(h),
   ]
   [
   \mathbb E*{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]
   \le b*{h,i}+\eta(h).
   ]

New dependencies: L2
Technique update: Freeze the promise coordinate along each rooted public-history tree and let only the bias vary. This is the upstream repair required for any root-promise telescope.
Downstream changes: Replace L3 by L3*, L4 by L4*, L5 by L5*, rewrite G3-G5 to use the fixed-promise backbone, and interpret L7' only in that amended system.
Reason: In the current variable-promise system the visited promise process does not telescope to the root promise, so the displayed downstream L7'/L8' cannot be obtained.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L3
Replace statement: **L3*. Compactness and heredity of the fixed-promise local feasibility problem.**
Fix a history (h), a promise vector (w\in[0,1]^N), and a current bias (b_h\in B(h,w)). Then
[
F^*(h,w,b_h)
]
is a closed subset of
[
\left(\prod_{i\in N}\Delta(A_i(s(h)))\right)\times
\left(\prod_{h'\text{ child of }h} B(h',w)\right).
]
Hence (F^*(h,w,b_h)) is compact whenever it is nonempty. Moreover, if ((x_h,\beta_h)\in F^*(h,w,b_h)), then every child bias (\beta_h(h')) lies in (B(h',w)), so the same construction may be iterated at descendants with the same fixed promise (w).

New dependencies: L2, Setup
Technique update: Use compact bias fibers instead of variable promise-bias pairs.
Downstream changes: L4, L5, G3-G5, L7'
Reason: This is the correct local well-posedness statement for the fixed-promise route.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L4
Replace statement: **L4*. One-step uncorrelated fixed-promise self-generation at every history.**
For every public history (h), every promise vector (w\in[0,1]^N), and every current bias (b_h\in B(h,w)), the local feasibility set (F^*(h,w,b_h)) is nonempty.

Equivalently, every admissible fixed promise-bias label at a node admits

1. a product mixed action (x_h=\bigotimes_i x_{h,i}), and
2. a choice of child biases (\beta_h(h')\in B(h',w)) for all immediate descendants,

such that no player can gain more than (\eta(h)) from a one-step unilateral deviation.

New dependencies: L2, L3*
Technique update: This is the true selector bottleneck after the fixed-promise repair.
Downstream changes: L5, G3-G5, L7'
Reason: The old L4 is not the right upstream input for the corrected telescope.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: L5
Replace statement: **L5*. Recursive assembly on the full rooted public-history tree with fixed promise.**
Assume L2 and L4*. For each initial state (s), choose one root pair
[
(w^s,b^s)\in Z(s).
]
Then there exist

1. for each initial state (s), a rooted behavioral profile (\sigma^s) defined on the full public-history tree rooted at (s), and
2. for each rooted history (h) with root (s), a bias (\beta^s(h)\in B(h,w^s)),

such that for every rooted history (h), the pair consisting of the mixed action prescribed by (\sigma^s) at (h) and the child-bias assignment at the children of (h) belongs to
[
F^*(h,w^s,\beta^s(h)).
]

Defining
[
\sigma(h):=\sigma^{s_1}(h)\qquad\text{for }h=(s_1,a_1,\dots,s_t),
]
yields one whole-game behavioral profile (\sigma) on the union of all public histories.

New dependencies: L2, L4*
Technique update: Build rooted profiles first, then glue them by initial state.
Downstream changes: G3-G5, L7', L8'
Reason: The theorem target needs one global profile, while the deviation analysis needs the full rooted tree, not only on-path histories.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G3
Replace statement: **G3. Build rooted fixed-promise trees and glue them globally.**
Assuming L4*, apply L5* to each initial state (s) using a chosen root pair ((w^s,b^s)\in Z(s)). This yields rooted profiles (\sigma^s) and rooted bias assignments (\beta^s). Then define the single whole-game profile by (\sigma(h):=\sigma^{s_1}(h)) for (h=(s_1,a_1,\dots,s_t)).

New dependencies: L2, L4*, L5*
Technique update: Use the explicit global assembly step.
Downstream changes: G4, G5
Reason: The global profile must be written down explicitly.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G4
Replace statement: **G4. Verify deviations by the corrected fixed-promise telescope.**
After G3, do not use the old variable-promise L7. Instead prove the corrected L7' from the fixed-promise objects built in L5*: the same root promise (w^s) is used all along the rooted tree, so only bias terms remain to telescope.

New dependencies: L2, L5*, corrected L7'
Technique update: Root-promise telescope, not visited-promise averaging.
Downstream changes: G5
Reason: The previous G4 invoked a downstream statement not supported by the current setup.
[/BREAKDOWN_AMEND]

[BREAKDOWN_AMEND]
Target: G5
Replace statement: **G5. Uniformize in the horizon using corrected L8'.**
Use corrected L8', with the standing hypothesis (\eta_t\ge 0), to choose (T_0) so that the endpoint bias residue is at most (\varepsilon/2) and the leakage sum is at most (\varepsilon/2).

New dependencies: corrected L8'
Technique update: Pure bookkeeping after the corrected telescope.
Downstream changes: none
Reason: The old G5 depended on an unrepaired downstream chain.
[/BREAKDOWN_AMEND]

## L1. Subgame reduction from histories to terminal states

**Claim.** For every public history (h), the continuation game after (h) is canonically identified with the original stochastic game started from the terminal state (s(h)).

**Proof.**

Fix a finite stochastic game
[
G=(N,S,(A_i)*{i\in N},u,P)
]
in the sense of the formal target. Fix a public history
[
h=(s_1,a_1,s_2,a_2,\dots,a*{t-1},s_t),
]
and write
[
s(h):=s_t.
]

Define the continuation game (G_h) as follows:

* same player set (N);
* same state set (S);
* for each player (i) and state (s), same action set (A_i(s));
* same stage payoff function (u);
* same transition kernel (P);
* initial state equal to (s(h)).

This is a direct use of the model definition: after a public history, the only state variable relevant to future play is the terminal state of that history. No past action or past state enters either the stage payoff function or the transition kernel except through the current state. [DERIVED]

Now define the shift map on future histories. A future public history after (h) has the form
[
(h,s_t,a_t,s_{t+1},a_{t+1},\dots,a_{t+k-1},s_{t+k}).
]
Delete the fixed prefix (h). This yields
[
(s_t,a_t,s_{t+1},a_{t+1},\dots,a_{t+k-1},s_{t+k}),
]
which is exactly a public history of length (k+1) in the game (G_h) started at (s(h)=s_t). Conversely, every public history in (G_h) started from (s_t) extends uniquely to a continuation history after (h) in (G) by reattaching the prefix (h). Therefore there is a bijection between continuation histories after (h) in (G) and histories in (G_h). [DERIVED]

Next compare laws of play. Let (\sigma) be any behavioral profile in (G). Its restriction to histories extending (h) determines a behavioral profile in (G_h) under the above identification. Conversely, every behavioral profile in (G_h) pulls back to a continuation profile after (h) in (G). At every future stage, the conditional distribution of the next state given the current continuation history and current action profile is
[
P(\cdot\mid s,a)
]
in both descriptions, by direct inspection of the model definition. Also the stage payoff at that stage is
[
u_i(s,a)
]
in both descriptions. Therefore the induced probability law on future plays and the induced future payoff process are identical under the history-shift identification. [DERIVED]

Hence every state-indexed object in the original game can be pulled back to histories ending in that state: if (Q(s)) is any object depending only on the continuation game from state (s), define
[
Q(h):=Q(s(h)).
]
This applies in particular to statewise maxmin values, punishment correspondences, Martin correspondences, continuation selectors, and any other continuation object defined from the subgame started at a state. [DERIVED]

So L1 is proved. [DERIVED]

---

## L3*. Compactness and heredity of the fixed-promise local feasibility problem

I will prove the amended L3* conditionally on the amended setup and imported compactness from L2.

Fix a history (h), a promise vector (w\in[0,1]^N), and a current bias (b_h\in B(h,w)).

### Step 1: the ambient domain is a finite product of compact sets

For each player (i), the action set (A_i(s(h))) is finite by the game definition. Therefore the simplex
[
\Delta(A_i(s(h)))
]
is a nonempty compact subset of a finite-dimensional Euclidean space. This is a standard theorem on simplices over finite sets. [DERIVED]

The set of children of (h) is finite, because a child is determined by a current action profile (a\in A(s(h))) and a next state (s'\in S), and both (A(s(h))) and (S) are finite. [DERIVED]

By the amended setup,
[
B(h',w)={b\in[-B,B]^N:(w,b)\in Z(h')}.
]
Under L2, each (Z(h')\subseteq [0,1]^N\times[-B,B]^N) is compact. Intersecting (Z(h')) with the closed slice ({w}\times[-B,B]^N) gives a compact set, and projecting that slice-identification to the bias coordinate yields (B(h',w)) compact whenever nonempty. [DERIVED]

Therefore the ambient set
[
X(h,w):=\left(\prod_{i\in N}\Delta(A_i(s(h)))\right)\times
\left(\prod_{h'\text{ child of }h} B(h',w)\right)
]
is compact, because it is a finite product of compact sets. [DERIVED]

### Step 2: the defining inequalities are continuous

Write a generic point of (X(h,w)) as ((x_h,\beta_h)).

For each player (i), the obedient inequality in (F^*(h,w,b_h)) is
[
b_{h,i}\le \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')_i\right]+\eta(h).
]
The right-hand side is a finite sum over current action profiles (a) and next states (s'), with coefficients equal to products of mixed-action coordinates and transition probabilities. Since mixed-action coordinates enter multilinearly and the child-bias coordinates enter linearly, this right-hand side is a continuous function of ((x_h,\beta_h)). [DERIVED]

For each player (i) and pure deviation (a_i'\in A_i(s(h))), the deviating inequality is
[
\mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]
\le b*{h,i}+\eta(h).
]
Again, the left-hand side is a finite multilinear-linear expression in the coordinates of ((x_h,\beta_h)), hence continuous. [DERIVED]

There are only finitely many such inequalities, because both (N) and all (A_i(s(h))) are finite. [DERIVED]

### Step 3: the feasible set is closed

Each obedient inequality defines a closed subset of (X(h,w)), as the preimage of ((-\infty,0]) under a continuous function. The same is true for each deviating inequality. Taking the finite intersection of these closed subsets, we conclude that
[
F^*(h,w,b_h)
]
is closed in (X(h,w)). [DERIVED]

Since (X(h,w)) is compact by Step 1, every closed subset of (X(h,w)) is compact. Therefore (F^*(h,w,b_h)) is compact whenever it is nonempty. [DERIVED]

### Step 4: heredity

If ((x_h,\beta_h)\in F^*(h,w,b_h)), then by definition of (F^*), for every child history (h') we have
[
\beta_h(h')\in B(h',w).
]
That is exactly the hereditary property needed to iterate the same fixed-promise construction at descendants. [DERIVED]

So amended L3* is proved, conditional on the amended setup and imported L2. [DERIVED]

---

## L5*. Recursive assembly on the full rooted public-history tree with fixed promise

I will prove the amended L5* conditional on L2 and amended L4*.

### Step 1: choose root labels

Fix an initial state (s\in S). By L2, (Z(s)) is nonempty. Therefore we may choose
[
(w^s,b^s)\in Z(s).
]
By definition of the bias fiber,
[
b^s\in B((s),w^s),
]
where ((s)) denotes the root history consisting only of the initial state (s). [DERIVED]

This root choice uses L2, not L4*. [DERIVED]

### Step 2: define the rooted tree

Let (H^s) denote the full rooted public-history tree starting from state (s). Its vertices are all public histories
[
h=(s,a_1,s_2,\dots,a_{t-1},s_t)
]
whose first state is (s). Every non-root history in (H^s) has a unique predecessor, obtained by deleting the final action-state pair. [DERIVED]

This uniqueness of predecessor is a direct property of history sequences. [DERIVED]

### Step 3: inductive finite-level construction

I now construct, by induction on depth, a consistent family of local witnesses on (H^s).

For depth (0), assign the root bias
[
\beta^s((s)):=b^s.
]
Since (\beta^s((s))\in B((s),w^s)), L4* applies at the root. Therefore there exists
[
(x_{(s)},\beta_{(s)}^{\mathrm{child}})\in F^*((s),w^s,b^s).
]
Define the rooted strategy at the root by
[
\sigma^s((s)):=x_{(s)},
]
and for every child (h') of the root define
[
\beta^s(h'):=\beta_{(s)}^{\mathrm{child}}(h').
]
By definition of (F^*), each such child bias lies in (B(h',w^s)). [DERIVED]

Now suppose by induction that for all histories in (H^s) of depth at most (n), we have already assigned:

1. a bias (\beta^s(h)\in B(h,w^s)), and
2. a mixed action (\sigma^s(h)) at every history of depth at most (n-1),

so that for every history (g) of depth at most (n-1), the chosen action (\sigma^s(g)) together with the chosen child-bias assignment at its children forms an element of
[
F^*(g,w^s,\beta^s(g)).
]

Take any history (h) of depth (n). By the induction hypothesis,
[
\beta^s(h)\in B(h,w^s).
]
Therefore L4* applies to ((h,w^s,\beta^s(h))), and yields some witness
[
(x_h,\beta_h^{\mathrm{child}})\in F^*(h,w^s,\beta^s(h)).
]
Define
[
\sigma^s(h):=x_h,
]
and for each child (h') of (h) define
[
\beta^s(h'):=\beta_h^{\mathrm{child}}(h').
]
Again, the definition of (F^*) guarantees
[
\beta^s(h')\in B(h',w^s).
]
This extends the construction to depth (n+1). [DERIVED]

By induction on (n\in\mathbb N), we obtain a consistent assignment on all finite depths of the rooted tree (H^s). [DERIVED]

### Step 4: consistency

There is no conflict in the construction because every non-root history (h\in H^s) has a unique predecessor. Hence the value (\beta^s(h)) is assigned exactly once, namely when the local witness at its predecessor is chosen. Likewise, (\sigma^s(h)) is assigned exactly once, namely when L4* is applied at (h). [DERIVED]

Thus the union over finite depths is well-defined. [DERIVED]

### Step 5: conclusion for one root

We have constructed:

* a behavioral profile (\sigma^s) on the full rooted tree (H^s);
* a bias assignment (\beta^s(h)\in B(h,w^s)) for every (h\in H^s);

such that for every (h\in H^s), the local data chosen at (h) belongs to
[
F^*(h,w^s,\beta^s(h)).
]
So the rooted fixed-promise version of L5 holds for the single initial state (s). [DERIVED]

### Step 6: glue all roots into one whole-game profile

Repeat Step 1 through Step 5 for every initial state (s\in S). Since (S) is finite, this yields a finite family ((\sigma^s)_{s\in S}). [DERIVED]

Now define a global behavioral profile (\sigma) on the union of all public histories by
[
\sigma(h):=\sigma^{s_1}(h)
\qquad\text{for }h=(s_1,a_1,\dots,s_t).
]
This is well-defined because the first state (s_1) of the history uniquely determines which rooted tree (H^{s_1}) contains (h). Histories with different first states lie in disjoint rooted trees. [DERIVED]

Therefore (\sigma) is one whole-game behavioral profile, not a mere family indexed by initial states. [DERIVED]

So amended L5* is proved conditional on L2 and L4*. [DERIVED]

---

## Explicit gap report

1. **L2 remains imported, not proved here.**
   The current packet treats the Martin/maxmin seed layer as external machinery. I do not upgrade it to [DERIVED]. [ASSUMPTION-]

2. **L4* remains open.**
   After the fixed-promise repair, the selector theorem that actually matters is the amended L4*, not the original variable-promise L4. I do not prove it here. This remains the theorem-sized bottleneck. [ASSUMPTION-]

3. **Current variable-promise L7' is unavailable.**
   The existing local relation propagates successor biases but not a fixed successor promise, so the visited promises do not telescope to the root promise. Hence the current downstream L7'/L8' chain is not derivable without the above amendment. [DERIVED]

4. **L6 should be retained only literally.**
   Nothing proved here supplies a non-vacuous punishment-mode mechanism with remembered punishment anchor. Any stronger reading remains unsupported. [DERIVED]

---

## Status summary

* [DERIVED] **L1**: proved explicitly.
* [DERIVED] **L3***: proved explicitly, conditional on imported L2 and the amended fixed-promise setup.
* [DERIVED] **L5***: proved explicitly, conditional on L2 and open L4*.
* [DERIVED] Current packet requires an upstream repair from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)).
* [DERIVED] The global assembly step from rooted profiles (\sigma^s) to one whole-game profile (\sigma) is explicit and correct in the amended system.
* [ASSUMPTION-] **L2** remains imported.
* [ASSUMPTION-] **L4*** remains open and is the central unresolved selector theorem.
* [DERIVED] Therefore the theorem remains **bootstrap/open**, and the correct current backbone is
  [
  L1 \to \text{imported }L2 \to L3^* \to \text{open }L4^* \to L5^* \to \text{literal }L6 \to \text{corrected }L7' \to L8'.
  ]

This advances the branch by clearing the local compactness and full-tree recursion pieces in the **corrected** fixed-promise framework, while explicitly isolating the remaining open selector step.

## FILE: branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/prover_09.md

# Prover Output

Generated: 2026-03-24T02:20:49.579519+00:00

[DERIVED] I keep the route explicitly **open/bootstrap**, and I preserve the exact theorem-side target: one behavioral profile (\sigma), one threshold (T_0), all sufficiently large horizons, every initial state, every player, and every unilateral deviation. That is the durable project status and the adopted formal claim.     

## Fixed-promise repair of the local invariant

[BREAKDOWN_AMEND] The downstream proof should use the **increment form** of the current breakdown’s local invariant and should stop citing the canceled-promise formulas from the superseded prover_07 setup. The current breakdown already has a fixed root promise (\rho^s) and a varying bias (b^s(h)):
[
\rho_i^s+b_i^s(h)
\le
\mathbb E!\left[u_i(s(h),a)+b_i^s(h,a,q)\right]+\eta_{|h|},
]
[
\rho_i^s+b_i^s(h)
\ge
\sup_{y_i}
\mathbb E!\left[u_i(s(h),(a_i,a_{-i}))+b_i^s(h,(a_i,a_{-i}),q)\right]-\eta_{|h|}.
]
Rearranging gives the exact fixed-promise local relations needed for telescoping:
[
\mathbb E!\left[u_i(s(h),a)+b_i^s(h,a,q)\right]-b_i^s(h)\ge \rho_i^s-\eta_{|h|},
\tag{Inc-E}
]
[
\sup_{y_i}
\mathbb E!\left[u_i(s(h),(a_i,a_{-i}))+b_i^s(h,(a_i,a_{-i}),q)\right]-b_i^s(h)\le \rho_i^s+\eta_{|h|}.
\tag{Inc-D}
]
This is algebraically equivalent to the displayed setup in the breakdown, and it is exactly the fixed-promise relation the reviewer patch set asks for.

[ASSUMPTION+] For the closed-graph clause in L3, equip (H^s=\bigsqcup_{t\ge 1}H_t^s) with the disjoint-union topology of its finite depth layers. Equivalently, (H^s) is a countable discrete space.

## L1

[ASSUMPTION+] (**ZU**) Every finite-state two-player zero-sum stochastic game with compact metric action sets and continuous payoff/transition data has a uniform value, and each player has uniformly (\delta)-optimal strategies.

[DERIVED] **L1**, conditional on [ASSUMPTION+] ZU.

Fix a public history (h) and a player (i). Let (q=s(h)) be the terminal state of (h). Define a two-player zero-sum continuation game (Z_{h,i}) as follows.

* The state space is (S), with initial state (q).
* Player Max is (i), with action set (A_i(s)) at state (s).
* Player Min is the coalition (N\setminus{i}), with action set
  [
  M_{-i}(s):=\prod_{j\ne i}\Delta(A_j(s)).
  ]
* The one-stage payoff to Max is
  [
  g_i(s,a_i,x_{-i})
  :=
  \sum_{a_{-i}}
  \Bigl(\prod_{j\ne i}x_j(a_j)\Bigr),
  u_i(s,(a_i,a_{-i})).
  ]
* The transition kernel is
  [
  Q(\cdot\mid s,a_i,x_{-i})
  :=
  \sum_{a_{-i}}
  \Bigl(\prod_{j\ne i}x_j(a_j)\Bigr),
  P(\cdot\mid s,(a_i,a_{-i})).
  ]

Justification of applicability of ZU: (S) is finite, each (A_i(s)) is finite, each (M_{-i}(s)) is a product of finite simplices and hence compact metric, and both (g_i) and (Q) are continuous and multilinear in the mixed actions.

By ZU, (Z_{h,i}) has a uniform value (m_i(h)\in[0,1]), and for every (\delta>0) player (i) has a strategy (\mu_i^{h,\delta}) in (Z_{h,i}) such that for all sufficiently large (T),
[
\inf_{\chi_{-i}}
\gamma_i^T(Z_{h,i},(\mu_i^{h,\delta},\chi_{-i}))
\ge m_i(h)-\delta.
]

Now let (\sigma_{-i}) be any opponent profile in the original continuation game (G_h). At each continuation history, (\sigma_{-i}) induces a coalition mixed action (x_{-i}\in M_{-i}(s)). Therefore the law of play in (G_h) under ((\mu_i^{h,\delta},\sigma_{-i})) is a special case of the law in (Z_{h,i}) under ((\mu_i^{h,\delta},\chi_{-i})). Hence the same lower bound holds:
[
\inf_{\sigma_{-i}}
\gamma_i^T(G_h,(\mu_i^{h,\delta},\sigma_{-i}))
\ge m_i(h)-\delta
]
for all sufficiently large (T). This is exactly L1.

## Gap on L2

L2 remains **imported/open** in this pass. I do not mark it as proved. I use only the properties explicitly stated in the breakdown: nonempty compact fibers (W^s(h)\subseteq[-B_s,B_s]^N), root nonemptiness, and the uniform bias bound. This is consistent with the route memo and the project proof-state, both of which keep the route conditional and bootstrap.

## L3

[DERIVED] **L3**.

Fix (s\in S), (h\in H^s), and (b\in W^s(h)). Let
[
X(h):=\prod_{i\in N}\Delta(A_i(s(h))).
]
Let (C(h)) be the finite set of one-step child histories (h'=(h,a,q)). Define the ambient product
[
K(h):=X(h)\times \prod_{h'\in C(h)} W^s(h').
]
By finiteness of actions and children, (X(h)) is a finite product of simplices, hence compact, and each (W^s(h')) is compact by L2. Therefore (K(h)) is compact.

For each player (i), define
[
\Phi_i(x,\beta)
:=
\mathbb E_{a\sim x,\ q\sim P(\cdot\mid s(h),a)}
\bigl[u_i(s(h),a)+\beta(h,a,q)_i\bigr].
]
This is continuous on (K(h)), because it is a finite multilinear expression in (x) and the child-bias coordinates.

Define also
[
\Psi_i(x,\beta)
:=
\sup_{y_i\in\Delta(A_i(s(h)))}
\mathbb E_{a_i\sim y_i,\ a_{-i}\sim x_{-i},\ q}
\bigl[u_i(s(h),(a_i,a_{-i}))+\beta(h,(a_i,a_{-i}),q)_i\bigr].
]
The inner expectation is affine in (y_i), so the supremum over the simplex equals the maximum over pure actions:
[
\Psi_i(x,\beta)
===============

\max_{a_i\in A_i(s(h))}
\mathbb E_{a_{-i}\sim x_{-i},\ q}
\bigl[u_i(s(h),(a_i,a_{-i}))+\beta(h,(a_i,a_{-i}),q)_i\bigr].
]
This is a finite maximum of continuous functions, hence continuous.

Therefore
[
\mathcal F^s(h,b)
=================

\Bigl{(x,\beta)\in K(h):
\rho_i^s+b_i\le \Phi_i(x,\beta)+\eta_{|h|},
\rho_i^s+b_i\ge \Psi_i(x,\beta)-\eta_{|h|}
\ \forall i
\Bigr}
]
is the intersection of finitely many closed subsets of the compact set (K(h)). Hence (\mathcal F^s(h,b)) is compact. The empty set case is harmless, since the empty set is compact.

For closed graph: let ((h_n,b_n,x_n,\beta_n)\to(h,b,x,\beta)) with ((x_n,\beta_n)\in\mathcal F^s(h_n,b_n)) for all (n). Since (H^s) is discrete, eventually (h_n=h). Since (b_n\to b) in the compact set (W^s(h)), continuity of (\Phi_i,\Psi_i) passes the defining inequalities to the limit, so ((x,\beta)\in\mathcal F^s(h,b)). Hence the graph is closed.

## L5

[BREAKDOWN_AMEND] The L5 proof does **not** need a Kőnig-style compactness limit once L4 is available on the full rooted tree. Direct recursion on depth is enough. Also, L5 must cite L2 for the root bias choice. This matches the accepted amendment and the stable route-memo takeaway.

[DERIVED] **L5**, conditional on L2 and L4.

Fix (s\in S). By L2 root nonemptiness, choose
[
b^s(s)\in W^s(s).
]
For each (n\ge 1), let (H_n^s) be the finite set of public histories of length (n) rooted at (s).

Inductively define (x^s(h)) and (b^s(h)) for all (h\in H_n^s).

* Base step (n=1): (b^s(s)) is already chosen.
* Induction step: assume (b^s(h)) is defined for every (h\in H_n^s). For each such (h), L4 gives a local package
  [
  \bigl(x_h,{c_{h'}}*{h'\text{ child of }h}\bigr)\in \mathcal F^s(h,b^s(h)).
  ]
  Set
  [
  x^s(h):=x_h,\qquad b^s(h'):=c*{h'}\ \text{for every child }h' \text{ of }h.
  ]

This is consistent because every child history (h') has a unique predecessor (h). Hence no two assignments conflict. By induction on (n), the functions
[
h\mapsto x^s(h),\qquad h\mapsto b^s(h)\in W^s(h)
]
are defined on all of (H^s), and for each (h) the chosen package lies in (\mathcal F^s(h,b^s(h))). This is exactly L5.

## L6

[BREAKDOWN_AMEND] Demote L6 to the **literal** statement that L5 defines a rooted behavioral profile. Do not cite L6 as a nonvacuous punishment-mode mechanism unless the public state is enlarged to remember punishment anchors. The route memo explicitly warns that the current stronger punishment reading is too weak / vacuous.

[DERIVED] **Literal L6.**

Given L5, define for each root (s) a behavioral profile (\widehat\sigma^s) on (H^s) by
[
\widehat\sigma_i^s(h):=x_i^s(h)\qquad(h\in H^s,\ i\in N).
]
Since (x^s(h)\in \prod_i\Delta(A_i(s(h)))), this is a well-defined public-history behavioral profile on the whole rooted tree (H^s).

No punishment-memory claim is used below.

## L7′

[BREAKDOWN_AMEND] Replace the current L7 by the following corrected lemma. Its proof uses only L2 and the full-tree L5 selector; L6 is not needed.

**Statement of L7′.** Assume L2 and L5. Then for every root (s), every player (i), every horizon (T\ge 1), and every unilateral deviation (\tau_i),
[
\mathbb E_{G,s,\widehat\sigma^s}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\ge
T\rho_i^s-2B_s-\sum_{t=1}^T\eta_t,
\tag{H_i^{T,\prime}}
]
and
[
\mathbb E_{G,s,(\tau_i,\widehat\sigma_{-i}^s)}!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
T\rho_i^s+2B_s+\sum_{t=1}^T\eta_t.
\tag{D_i^{T,\prime}}
]

[DERIVED] **L7′**.

Fix (s,i,T). Under either honest play or unilateral deviation, let (H_t) be the random public history before the stage-(t) action, so (H_1=(s)), and let (H_{t+1}=(H_t,a_t,s_{t+1})). Because L5 is defined on the **full** tree (H^s), the bias (b^s(H_t)) is defined even on histories created by a deviation.

Write
[
B_t:=b_i^s(H_t).
]
By L2, (|B_t|\le B_s) almost surely for all (t).

### Honest play

At history (H_t), the action profile is drawn from (x^s(H_t)). Therefore ((E_{H_t}^i)), equivalently (Inc-E), gives
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}\mid H_t\right]-B_t
\ge \rho_i^s-\eta_t.
]
So
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]
\ge \rho_i^s-\eta_t.
]
Take expectations and sum from (t=1) to (T):
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
+
\mathbb E[B_{T+1}-B_1]
\ge
T\rho_i^s-\sum_{t=1}^T\eta_t.
]
Since (B_{T+1}-B_1\le 2B_s),
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\ge
T\rho_i^s-2B_s-\sum_{t=1}^T\eta_t.
]

### Unilateral deviation

Now fix a deviation (\tau_i). At history (H_t), the deviator uses the mixed action
[
y_t:=\tau_i(H_t)\in\Delta(A_i(s(H_t))).
]
The opponents still use (x^s_{-i}(H_t)). Therefore ((D_{H_t}^i)), equivalently (Inc-D), applied with (y_i=y_t), gives
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}\mid H_t\right]-B_t
\le \rho_i^s+\eta_t.
]
Hence
[
\mathbb E!\left[u_i(s_t,a_t)+B_{t+1}-B_t\mid H_t\right]
\le \rho_i^s+\eta_t.
]
Taking expectations and summing,
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
+
\mathbb E[B_{T+1}-B_1]
\le
T\rho_i^s+\sum_{t=1}^T\eta_t.
]
Since (B_{T+1}-B_1\ge -2B_s),
[
\mathbb E!\left[\sum_{t=1}^T u_i(s_t,a_t)\right]
\le
T\rho_i^s+2B_s+\sum_{t=1}^T\eta_t.
]

This proves L7′.

## L8′

[BREAKDOWN_AMEND] Replace the current L8 by the corrected bookkeeping lemma below, with explicit use of (\eta_t\ge 0).

[DERIVED] **L8′**.

Assume L7′ and
[
\sum_{t\ge 1}\eta_t\le \frac{\varepsilon}{4},
\qquad
\eta_t\ge 0.
]
Divide the two inequalities of L7′ by (T):
[
\gamma_i^T(G,s,\widehat\sigma^s)
\ge
\rho_i^s-\frac{2B_s}{T}-\frac{1}{T}\sum_{t=1}^T\eta_t,
]
[
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))
\le
\rho_i^s+\frac{2B_s}{T}+\frac{1}{T}\sum_{t=1}^T\eta_t.
]
Subtracting,
[
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))
----------------------------------------------

\gamma_i^T(G,s,\widehat\sigma^s)
\le
\frac{4B_s}{T}+\frac{2}{T}\sum_{t=1}^T\eta_t.
]
Since the (\eta_t) are nonnegative,
[
\frac{2}{T}\sum_{t=1}^T\eta_t
\le
\frac{2}{T}\sum_{t\ge 1}\eta_t
\le
\frac{\varepsilon}{2T}
\le
\frac{\varepsilon}{2}.
]
Thus any
[
T_0(s)\in\mathbb N_{>0}
\quad\text{with}\quad
\frac{4B_s}{T_0(s)}\le \frac{\varepsilon}{2}
]
works. For example,
[
T_0(s):=\max!\left(1,\left\lceil \frac{8B_s}{\varepsilon}\right\rceil\right).
]
Then for all (T\ge T_0(s)),
[
\gamma_i^T(G,s,\widehat\sigma^s)
\ge
\gamma_i^T(G,s,(\tau_i,\widehat\sigma_{-i}^s))-\varepsilon.
]
This is exactly the rooted uniform (\varepsilon)-equilibrium statement.

## L9′

[BREAKDOWN_AMEND] The present L9 asks for a stronger current-state re-rooting compatibility:
the continuation from a history ending at (q) should agree with the separately constructed rooted profile for (q). That is stronger than what independent rooted constructions provide. It is also **not needed** for the formal theorem target, which quantifies over initial states only. So replace L9 by the weaker and sufficient disjoint-union assembly below. This keeps theorem-side scope unchanged.

**Statement of L9′.** Assume L8′ for every initial state (s\in S). Define a whole-game behavioral profile (\sigma) by
[
\sigma(h):=\widehat\sigma^{s_1(h)}(h),
]
where (s_1(h)) is the first state of the public history (h). Then (\sigma\in\Sigma(G)), and for every initial state (s), every horizon (T\ge T_0(s)), every player (i), and every unilateral deviation (\tau_i),
[
\gamma_i^T(G,s,\sigma)
\ge
\gamma_i^T(G,s,(\tau_i,\sigma_{-i}))-\varepsilon.
]
Because (S) is finite, one may set
[
T_0:=\max_{s\in S}T_0(s).
]

[DERIVED] **L9′**.

Every public history (h) has a unique first state (s_1(h)). Therefore the definition
[
\sigma(h):=\widehat\sigma^{s_1(h)}(h)
]
is well-defined on the full history space
[
H=\bigsqcup_{s\in S}H^s.
]
Since each (\widehat\sigma^{s}) is behavioral on (H^s), the assembled (\sigma) is behavioral on (H).

Now fix an initial state (s). Any play started from (s) only visits histories in (H^s). On that entire subset,
[
\sigma(h)=\widehat\sigma^s(h)
\qquad(h\in H^s).
]
Therefore the law of play under (\sigma) from initial state (s) is exactly the same as the law of play under (\widehat\sigma^s) from root (s). The same is true after replacing player (i)’s component by a deviation (\tau_i). Hence the rooted L8′ inequalities transfer verbatim from (\widehat\sigma^s) to (\sigma) at initial state (s). Taking (T_0=\max_s T_0(s)) is valid because (S) is finite.

## L10

[BREAKDOWN_AMEND] Replace the downstream backbone by
[
L1\to \text{imported }L2\to L3\to L4\to L5\to L7'\to L8'\to L9'\to L10,
]
with literal L6 optional and not used in the incentive proof. This is exactly the stable post-L4 route indicated by the route memo: recursion, telescoping, bookkeeping, and explicit global assembly, with L4 as the unresolved bottleneck.

[DERIVED] **Conditional L10.**

Assume L1, imported L2, and L4. Then L5 constructs, for each root state (s), a full-tree selector ((x^s,b^s)). Literal L6 turns (x^s) into a rooted behavioral profile (\widehat\sigma^s). L7′ and L8′ show that (\widehat\sigma^s) is a uniform (\varepsilon)-equilibrium from root (s). L9′ assembles the rooted family into a single whole-game behavioral profile (\sigma\in\Sigma(G)) and a common threshold
[
T_0=\max_{s\in S}T_0(s).
]
Therefore, for every (T\ge T_0), every initial state (s_1\in S), every player (i\in N), and every unilateral deviation (\tau_i\in\Sigma_i(G)),
[
\gamma_i^T(G,s_1,\sigma)
\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon.
]
This is exactly the formal theorem-side quantifier pattern.

Because L2 remains imported and L4 remains open, this is a **conditional theorem synthesis**, not a completed proof of the open problem. That is the correct project-level status.

## Status summary

[DERIVED] In this pass I have advanced the route as follows.

* **Proved conditionally from an explicit external zero-sum input:** L1.
* **Proved:** L3.
* **Proved conditionally on L2 and L4:** L5.
* **Proved in literal form only:** L6.
* **Proved and corrected:** L7′ and L8′.
* **Proved with a statement repair:** L9′, using disjoint-union whole-game assembly.
* **Proved conditionally:** L10.

Open gaps that remain explicit:

* **L2** is still imported/open and needs exact source-to-statement citation.
* **L4** is still the theorem-sized unresolved selector step.
* The stronger punishment-memory reading of **L6** is not proved.
* The stronger current-state re-rooting version of **L9** is not used.

So the coherent current proof object is:

[
\boxed{
L1\ (\text{conditional on ZU})\ \to\ \text{imported }L2\ \to\ L3\ \to\ \text{open }L4\ \to\ L5\ \to\ L7'\ \to\ L8'\ \to\ L9'\ \to\ L10
}
]

This preserves the exact theorem-side scope while honestly localizing the remaining obstruction at L2/L4, exactly as the durable proof-state and route memo require.

---
## ADDITIONAL LOADED FILES

### branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/assumption_delta.md

# Assumption Delta

- Added assumptions: 0
- Removed assumptions: 0
- Scope changes: 13
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

- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/breakdown_amendments.md` (8569 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/knowledge_ledger.md` (22488 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/literature.md` (14733 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_01.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_02.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_03.md` (4465 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_04.md` (6865 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_05.md` (7806 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_06.md` (7806 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_07.md` (6490 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/reviewer_08.md` (6490 chars)
- `branches/route_2__Martin-function_bootstrap_to_a_global_Nash_selector/context/scope_decision.md` (74 chars)

