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
