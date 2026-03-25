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
