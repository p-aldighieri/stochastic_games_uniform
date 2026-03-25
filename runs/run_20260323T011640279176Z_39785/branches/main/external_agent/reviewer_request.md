# External Agent Request (reviewer)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T05:23:04.273580+00:00

## Instructions

Check each proof step for logical validity, completeness, and correct citations. Check scope compliance. Issue a structured verdict: VERDICT: PASS (correct and complete), VERDICT: PATCH_SMALL (minor fixable issues), VERDICT: PATCH_BIG (needs restructuring), or VERDICT: REDO (fundamentally flawed approach). Be precise about errors. Tag scope changes with [SCOPE].

## Context

## FILE: branches/main/context/breakdown.md

# Breakdown Output

Generated: 2026-03-23T05:23:04.260812+00:00

Below is the lemma stack for the selected hybrid modified-game + continuation-orbit route, with the target understood in the durable strategy-existence sense: for every finite stochastic game (G) and every (\varepsilon>0), construct one profile that is an (\varepsilon)-equilibrium for every sufficiently large finite horizon and every initial state. The theorem itself is still open, and the packet’s selected route explicitly splices Solan’s modified-game tool with the 2025 absorbing block/orbit engine.    ([Google Sites][1])

## [BREAKDOWN_AMEND] Setup

Fix a finite stochastic game (G) and (\varepsilon>0). Choose internal tolerances
[
0<\eta_{\mathrm{mm}},\eta_{\mathrm{blk}},\eta_{\mathrm{orb}},\eta_{\mathrm{mon}},\eta_{\mathrm{tail}}
\ll \varepsilon
]
to be allocated later.

For each player (i) and state (s), let (v_i(s)) be the uniform minmax value of the zero-sum stochastic game in which player (i) plays against the coalition (N\setminus{i}). For each (i), let (\mathcal D_i) be the partition of (S) into level sets of (v_i), and choose cutoffs
[
c_i(D)\in\bigl(v_i(D),,v_i(D)+\eta_{\mathrm{mm}}\bigr)
\qquad (D\in\mathcal D_i).
]
Let (\widetilde G_{\lambda,\mathcal D,c}) denote Solan’s modified game, and let
[
W\subset [0,1]^{N\times S}
]
be the continuation region produced in Lemma L3. A point (w\in W) is a statewise continuation table, so (w_i(s)) is the continuation payoff promised to player (i) if the next block starts from state (s).

**Dependency spine.**
[
\mathrm{L1}\to \mathrm{L2}\to \mathrm{L3}\to \mathrm{L4}\to \mathrm{L5}\to \mathrm{L6}\to \mathrm{L7}\to \mathrm{L8}\to \mathrm{L9}\to \mathrm{L10}\to \mathrm{L11}.
]

---

### [BREAKDOWN_AMEND] L1. Uniform minmax values and restartable punishments

**Statement.**
For every player (i) and state (s), the uniform minmax value (v_i(s)) exists. Moreover, for every (\delta>0), there is a public punishment scheme (P_i^\delta) such that after any public history ending at state (s), if players (N\setminus{i}) switch to (P_i^\delta), then for every sufficiently large horizon (T) and every continuation strategy (\tau_i),
[
\gamma_i^T\bigl(s,(\tau_i,P_i^\delta)\bigr)\le v_i(s)+\delta .
]
The punishment can be restarted after any later public history.

**Dependencies.**
None.

**Technique hint.**
Reduce to the two-side zero-sum stochastic game “player (i) versus the coalition (N\setminus{i})”, use the uniform value/minmax theorem there, and record the punishment as a public history-dependent profile.

**Difficulty estimate.**
1/5, classical/imported.

---

### [BREAKDOWN_AMEND] L2. Modified-game equilibria at minmax-safe cutoffs

**Statement.**
Fix the partitions ((\mathcal D_i)_i) and cutoffs ((c_i)*i) from the setup. For every discount factor (\lambda) sufficiently close to (1), the modified game (\widetilde G*{\lambda,\mathcal D,c}) admits a stationary equilibrium (x^\lambda). If (m^\lambda\in[0,1]^{N\times S}) is the statewise equilibrium payoff table induced by (x^\lambda), then:

1. (m_i^\lambda(s)\ge v_i(s)-\eta_{\mathrm{mm}}) for every (i,s);
2. in each partition cell (D\in\mathcal D_i), player (i)’s modified payoff contribution from time spent in (D) is capped by (c_i(D));
3. the family ((m^\lambda)_{\lambda\uparrow 1}) is precompact.

**Dependencies.**
L1.

**Technique hint.**
Import the stationary-equilibrium side of the modified-game machinery, together with the comparison between modified payoffs and uniform minmax levels.

**Difficulty estimate.**
2/5, mostly imported from the modified-game engine.

---

### [BREAKDOWN_AMEND] L3. Compact continuation region (W)

**Statement.**
Let (W) be the set of accumulation points of the tables (m^\lambda) as (\lambda\uparrow 1). Then:

1. (W\neq\varnothing);
2. (W) is compact in ([0,1]^{N\times S});
3. every (w\in W) satisfies (w_i(s)\ge v_i(s)-\eta_{\mathrm{mm}}) for all (i,s);
4. every neighborhood of every (w\in W) contains some modified-game equilibrium table (m^\lambda) for all (\lambda) close enough to (1).

**Dependencies.**
L2.

**Technique hint.**
Finite-dimensional compactness, plus the precompactness from L2.

**Difficulty estimate.**
2/5, compactness/bookkeeping.

---

### [BREAKDOWN_AMEND] L4. Local block lemma in the full stochastic game

**Statement.**
For every (w\in W), there exist:

* an integer (T(w)\ge 1),
* a public finite-memory block strategy (\sigma(w)) for the original game,
* a successor continuation table (f(w)\in W),
* a public end-of-block event (R(w)),
* and a constant (\mu(w)>0),

such that for every initial state (s\in S):

1. **Block equilibrium with terminal bonus.**
   (\sigma(w)) is an (\eta_{\mathrm{blk}})-equilibrium of the (T(w))-stage game whose terminal bonus, if the block ends at state (s'), is (w(s')).

2. **Successor payoff approximation.**
   The (T(w))-stage average-payoff vector induced by (\sigma(w)) in the original game, starting from (s), is within (\eta_{\mathrm{blk}}) (in sup norm over players) of (f(w)(s)).

3. **Positive renewal hazard.**
   [
   \mathbb P_s^{\sigma(w)}\bigl(R(w)\bigr)\ge \mu(w).
   ]

4. **Renewal/stability interface.**
   On (R(w)), either:

   * play has reached a publicly recognizable continuation regime from which the game can be restarted with continuation table (f(w)), or
   * a unilateral deviator has become publicly identifiable and the corresponding L1 punishment can be triggered.

**Dependencies.**
L1, L2, L3.

**Technique hint.**
This is the bridge lemma. Start from a modified-game equilibrium near (w), truncate it into a finite block, and graft onto it an absorbing-style renewal mechanism. The hard part is to preserve incentives after moving back from the auxiliary modified game to the original stochastic game, while keeping a strictly positive renewal hazard and a clean successor table (f(w)).

**Difficulty estimate.**
5/5, route-defining and likely brutal.

---

### [BREAKDOWN_AMEND] L5. Neighborhood robustness of the local block data

**Statement.**
For every (w\in W), there exists an open neighborhood (U(w)\subset W) such that the same block data from L4,
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr),
]
work for every terminal bonus (w'\in U(w)), with the following weaker bounds:

1. (\sigma(w)) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T(w))-stage game with terminal bonus (w');
2. the induced original-game average payoff remains (2\eta_{\mathrm{blk}})-close to (f(w));
3. (\mathbb P(R(w))\ge \mu(w)/2).

**Dependencies.**
L4.

**Technique hint.**
Continuity of finite-horizon payoffs and incentive constraints with respect to terminal bonuses, plus lower semicontinuity of the renewal probability.

**Difficulty estimate.**
4/5, technically stiff but local.

---

### [BREAKDOWN_AMEND] L6. Finite block atlas over (W)

**Statement.**
There exist finitely many representatives (w^1,\dots,w^M\in W) and open sets (U_1,\dots,U_M) covering (W), together with block data
[
(T_m,\sigma^m,f_m,R_m,\mu_m)
\qquad (m=1,\dots,M),
]
such that whenever (w\in U_m),

1. (\sigma^m) is a (3\eta_{\mathrm{blk}})-equilibrium of the (T_m)-stage game with terminal bonus (w);
2. the induced original-game average payoff is (3\eta_{\mathrm{blk}})-close to (f_m);
3. (\mathbb P(R_m)\ge \mu_m>0).

Let
[
T_{\max}:=\max_m T_m<\infty,\qquad
\mu_{\min}:=\min_m \mu_m>0.
]

**Dependencies.**
L5.

**Technique hint.**
Compactness of (W) gives a finite subcover. The finite atlas is what turns the continuation map from a mist into a graph.

**Difficulty estimate.**
3/5, compactness plus parameter uniformization.

---

### [BREAKDOWN_AMEND] L7. Approximate finite-orbit theorem for the continuation map

**Statement.**
Define a directed graph on ({1,\dots,M}) by
[
m\to m'
\quad\Longleftrightarrow\quad
U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m)\neq\varnothing .
]
Then every node has outdegree at least one. Hence there exists a directed cycle
[
m_1\to m_2\to \cdots \to m_K\to m_1
]
and representatives (w^{m_k}\in U_{m_k}) such that
[
|w^{m_{k+1}}-f_{m_k}|*\infty\le \eta*{\mathrm{orb}}
\qquad (k=1,\dots,K,\ \text{cyclically}).
]
Thus ((w^{m_1},\dots,w^{m_K})) is a finite (\eta_{\mathrm{orb}})-pseudo-orbit of the full continuation map.

**Dependencies.**
L6.

**Technique hint.**
Once the finite atlas exists, this is just a directed-cycle extraction in a finite graph.

**Difficulty estimate.**
2/5, combinatorial after the atlas is built.

---

### [BREAKDOWN_AMEND] L8. Boundary regularization and unilateral deviator identification

**Statement.**
The blocks (\sigma^{m_1},\dots,\sigma^{m_K}) from L7 can be modified, by appending a uniformly bounded public reset subphase, so that:

1. block boundaries are canonical public histories;
2. any **unilateral** deviation during the reset subphase is publicly attributable to the deviating player;
3. after such an identified deviation, the relevant L1 punishment can start immediately from the current state;
4. the total distortion created by the reset phases changes payoff comparisons by at most (\eta_{\mathrm{mon}}) per block.

**Dependencies.**
L1, L7.

**Technique hint.**
Use a short pure-action reset tail. Mixed deviations inside the main body of a block are handled by L4-L6 already; the reset is only there to make the inter-block interface public and disciplined.

**Difficulty estimate.**
3/5, medium but modular.

---

### [BREAKDOWN_AMEND] L9. Concatenation lemma and almost-supermartingale control

**Statement.**
Let (\sigma^*) be the infinite public strategy profile obtained by cycling through the regularized blocks from L8 in the order
[
m_1,m_2,\dots,m_K,m_1,m_2,\dots
]
and restarting according to the actual reached state at each block boundary.

For every player (i), every initial state (s), every unilateral deviation (\tau_i), and every finite horizon (T), there exists a bounded block-boundary potential process
[
(M_k^{i,T})_{k\ge 0}
]
adapted to the public history at block boundaries, such that before entry into a stable regime or into a punishment phase:

1. (M_k^{i,T}\in[0,1]) for all (k);
2. the increment
   [
   M_k^{i,T}-M_{k+1}^{i,T}
   ]
   equals the contribution of block (k) to the (T)-stage payoff comparison, up to an error bounded by
   [
   C\bigl(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}}\bigr);
   ]
3. therefore ((M_k^{i,T})*k) is an almost-supermartingale against deviation, and the total deviation gain across any finite string of complete blocks is bounded by
   [
   C\bigl(\eta*{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}}\bigr)
   ]
   times the total normalized block weight, plus a uniformly bounded endpoint term.

**Dependencies.**
L4, L7, L8.

**Technique hint.**
At each block boundary, compare the current promised continuation (w^{m_k}) to the realized successor table, which is near (f_{m_k}), and then to the next orbit point (w^{m_{k+1}}). The pseudo-orbit gap and reset overhead create the (O(\eta)) drift, but the continuation term telescopes.

**Difficulty estimate.**
4/5, this is the main global incentive lemma.

---

### [BREAKDOWN_AMEND] L10. From complete blocks to arbitrary horizons

**Statement.**
Let (T_{\max}) be as in L6. For any horizon (T), the first (T) stages decompose into:

* some number of complete regularized blocks,
* plus at most one terminal partial block.

Hence the difference between the true (T)-stage average payoff and the average over the complete blocks before time (T) is at most
[
\frac{T_{\max}}{T}.
]
Combining this with L9 yields a constant (C) such that, for every player (i), state (s), unilateral deviation (\tau_i), and all sufficiently large (T),
[
\gamma_i^T\bigl(s,(\tau_i,\sigma^*_{-i})\bigr)
\le
\gamma_i^T(s,\sigma^*)+
C\bigl(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}}\bigr)
+\frac{T_{\max}}{T}.
]

**Dependencies.**
L9.

**Technique hint.**
Weighted Cesàro transfer from blockwise control to stagewise control, with the last partial block swallowed into a (T_{\max}/T) remainder.

**Difficulty estimate.**
3/5, once L9 exists this is routine averaging.

---

### [BREAKDOWN_AMEND] L11. Final assembly

**Statement.**
Choose the internal tolerances so that
[
C\bigl(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}}\bigr)
+\eta_{\mathrm{tail}}
<\varepsilon/2,
]
and then choose (T_0) so that
[
\frac{T_{\max}}{T}\le \varepsilon/2
\qquad\text{for all }T\ge T_0.
]
Then the single profile (\sigma^*) from L9 is a uniform (\varepsilon)-equilibrium of (G).

**Dependencies.**
L10.

**Technique hint.**
Pure error-budget closure.

**Difficulty estimate.**
1/5, bookkeeping.

---

## [BREAKDOWN_AMEND] Critical lemma

**Critical lemma: L4.**
This is the hard seam. The packet itself flags the local block lemma, outside absorbing-like geometry, as the likely failure point. That diagnosis matches the literature: the 2025 absorbing paper proves exactly the “finite block with terminal bonus, positive hazard, and successor map (f)” engine in the absorbing setting, and its discussion explicitly leaves extension to more general positive recursive games as unresolved terrain. So if L4 breaks, the whole hybrid route collapses; if L4 goes through, the rest is mostly compactness, graph selection, and horizon bookkeeping.  ([arXiv][2])

---

## [BREAKDOWN_AMEND] Glue steps from lemmas to theorem

### [BREAKDOWN_AMEND] G1. Safe continuation geometry

Use L1-L3 to manufacture a compact continuation region (W) made of statewise, minmax-safe continuation tables coming from modified-game equilibria.

### [BREAKDOWN_AMEND] G2. Turn each continuation table into a finite block

Apply L4 to every (w\in W), then L5-L6 to replace the continuum of blocks by a finite atlas of representative blocks with uniformly controlled errors and positive renewal probabilities.

### [BREAKDOWN_AMEND] G3. Collapse the continuation dynamics to a finite cycle

Use L7 to extract a finite pseudo-orbit
[
w^{m_1}\rightsquigarrow w^{m_2}\rightsquigarrow \cdots \rightsquigarrow w^{m_K}\rightsquigarrow w^{m_1}.
]
This gives the global schedule of blocks.

### [BREAKDOWN_AMEND] G4. Make the interfaces public and punitive

Use L8 to regularize block boundaries so that the global profile can be implemented by one public finite-memory automaton and unilateral boundary deviations can be punished immediately.

### [BREAKDOWN_AMEND] G5. Prove one profile works for all large horizons

Concatenate the blocks cyclically to form (\sigma^*). L9 gives almost-supermartingale control of continuation promises against deviations over complete blocks. L10 transfers that control to the actual (T)-stage average payoff for arbitrary large (T). L11 closes the (\varepsilon)-budget and finishes the uniform-equilibrium inequality.

---

## [BREAKDOWN_AMEND] Minimal dependency map in words

* **Imported backbone:** L1, L2, L3.
* **Bridge lemma:** L4.
* **Compactness cleanup:** L5, L6.
* **Orbit extraction:** L7.
* **Implementation interface:** L8.
* **Global incentive control:** L9.
* **Finite-horizon averaging:** L10.
* **Final theorem:** L11.

If I were assigning proof labor, I would treat L4 as the main theorem-sized task, L9 as the second serious task, and everything else as support beams.

[1]: https://sites.google.com/view/thegametheorysocietyilchapter/open-problems#:~:text=Problem%201%0A%0A%0A%0ADoes%20every%20stochastic%20game,meal%20in%20any%20restaurant%20worldwide "Open Problems"
[2]: https://arxiv.org/html/2512.04306v1 "Undiscounted Equilibrium in Positive Recursive Absorbing Games with Non-Rectangular Absorption Structure The authors thank János Flesch for commenting on an earlier version of the paper. Solan acknowledges the support of the Israel Science Foundation grant #211/22."

## Accepted Amendments
- In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
- L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.
- For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
- L10 and L11 need two bookkeeping repairs.
- In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
- L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.
- For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
- L10 and L11 need two bookkeeping repairs.
- In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
- L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.
- For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
- L10 and L11 need two bookkeeping repairs.

## FILE: branches/main/context/formalizer.md

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

## FILE: branches/main/context/prover_01.md

# Prover Output

Generated: 2026-03-23T04:14:37.663514+00:00

Using the supplied breakdown and the durable reading of the target as existence of one profile that is an (\varepsilon)-equilibrium for every sufficiently large horizon and every initial state, the clean advances in this pass are: L1 under one explicit coalition-control amendment, L2(3), L3 with a necessary correction to part (4), L5, L6, L7, and the final L10-L11 bookkeeping after two precise normalization repairs. The theorem-sized seam is still L4, and L8-L9 are still not closed.   

[BREAKDOWN_AMEND] In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
[
b_{-i}\in B_i(s):=\prod_{j\neq i}\Delta(A_j(s))
]
at each public history ending at state (s), not an arbitrary correlated distribution on (A_{-i}(s):=\prod_{j\neq i}A_j(s)). Otherwise there is a correlation-implementation gap when one tries to unfold the minimizer back into separate punishers in the original game.

[ASSUMPTION+] The classical uniform-value theorem is available for finite-state zero-sum stochastic games with compact action spaces and continuous stage payoff and transition data. This is the version needed for the product-mixed auxiliary game just described.

## L1. Uniform minmax values and restartable punishments

Fix (i\in N). Define the auxiliary two-side zero-sum stochastic game (\widehat G_i) as follows. The state space is (S). The maximizing player is player (i), with action set (A_i(s)) in state (s). The minimizing player is the coalition controller, with action set
[
B_i(s)=\prod_{j\neq i}\Delta(A_j(s)).
]
For (a_i\in A_i(s)) and (b_{-i}=(b_j)*{j\neq i}\in B_i(s)), define
[
\widehat u_i(s,a_i,b*{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),u_i(s,a_i,a_{-i}),
]
and
[
\widehat P_i(s'\mid s,a_i,b_{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),P(s'\mid s,a_i,a_{-i}).
]

The state space is finite, each (A_i(s)) is finite, each (B_i(s)) is compact, and ((\widehat u_i,\widehat P_i)) are continuous in (b_{-i}) by direct finite summation. By [ASSUMPTION+] and the zero-sum uniform-value theorem, there exists a value (v_i(s)) for every initial state (s), and for every (\delta>0) there exists a minimizing strategy (\pi_{-i}^\delta) in (\widehat G_i) such that for every (s\in S) there is (T_i^\delta(s)) with
[
\gamma_i^T\bigl(s,(\tau_i,\pi_{-i}^\delta)\bigr)\le v_i(s)+\delta
]
for every (T\ge T_i^\delta(s)) and every strategy (\tau_i) of player (i).

Because (S) is finite, the number
[
T_i^\delta:=\max_{s\in S} T_i^\delta(s)
]
is finite. Hence the same minimizing strategy works for all initial states once (T\ge T_i^\delta).

Now unfold (\pi_{-i}^\delta) into a public punishment profile (P_i^\delta) in the original game: after every public history (h_t) ending at state (s_t), each player (j\neq i) independently uses the mixed action prescribed by the (j)-th coordinate of (\pi_{-i}^\delta(h_t)). By construction of ((\widehat u_i,\widehat P_i)), the law of the state/action process under ((\tau_i,P_i^\delta)) in the original game is exactly the law of the auxiliary game under ((\tau_i,\pi_{-i}^\delta)). Therefore
[
\gamma_i^T\bigl(s,(\tau_i,P_i^\delta)\bigr)\le v_i(s)+\delta
]
for all (s\in S), all (T\ge T_i^\delta), and all (\tau_i).

Finally, restartability is immediate. After any public history ending at state (s), define the continuation punishment to be a fresh copy of the same strategy (\pi_{-i}^\delta) started from state (s). This is legitimate because strategies in the model are defined on public histories, and future play depends only on the future continuation strategy together with the current state.

[DERIVED] L1 holds under the coalition-action amendment above and [ASSUMPTION+].

## A small clean-up inside L2

The precompactness clause L2(3) does not need any modified-game theorem.

Indeed, by the statement of L2, every equilibrium payoff table satisfies
[
m^\lambda\in [0,1]^{N\times S}.
]
Since (N) and (S) are finite, the cube ([0,1]^{N\times S}) is compact in the sup norm. Any subset of a compact metric space is precompact.

[DERIVED] L2(3) is immediate from (m^\lambda\in[0,1]^{N\times S}).

I do **not** claim L2(1)-(2) here. Those remain imported from the modified-game machinery.

## L3. Compact continuation region (W)

All norms and balls below are sup norms on ([0,1]^{N\times S}).

[BREAKDOWN_AMEND] L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.

Take any sequence (\lambda_n\uparrow 1) in the domain where (m^{\lambda_n}) is defined. By L2(3), the family ((m^{\lambda_n})) is precompact, so it has a convergent subsequence, say
[
m^{\lambda_{n_k}}\to w\in [0,1]^{N\times S}.
]
By definition of (W), this limit (w) belongs to (W). Hence (W\neq\varnothing).

To prove compactness, let ((w^q)\subset W) be a convergent sequence with (w^q\to w) in ([0,1]^{N\times S}). We show (w\in W). Fix (\rho>0) and (\lambda_0<1). Choose (q) so large that
[
|w^q-w|*\infty<\rho/2.
]
Since (w^q\in W), (w^q) is an accumulation point of ((m^\lambda)), so there exists (\lambda\in(\lambda_0,1)) with
[
|m^\lambda-w^q|*\infty<\rho/2.
]
By the triangle inequality,
[
|m^\lambda-w|*\infty\le |m^\lambda-w^q|*\infty+|w^q-w|_\infty<\rho.
]
Because (\rho) and (\lambda_0) were arbitrary, (w) is also an accumulation point. Hence (W) is closed in the compact cube ([0,1]^{N\times S}), therefore compact.

For the minmax lower bound, let (w\in W). By definition, there exists a sequence (\lambda_n\uparrow 1) with
[
m^{\lambda_n}\to w.
]
By L2(1),
[
m_i^{\lambda_n}(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }n.
]
Passing to the limit coordinatewise gives
[
w_i(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }(i,s).
]

The corrected approximation property is now immediate from the definition of accumulation point:

[
\forall w\in W,\ \forall \text{ neighborhoods }U\ni w,\ \forall \lambda_0<1,\ \exists \lambda\in(\lambda_0,1)
\text{ such that } m^\lambda\in U.
]

[DERIVED] L3(1), L3(2), and L3(3) are proved from L2.
[DERIVED] The correct replacement for L3(4) is the arbitrarily-close-(\lambda) version just displayed.

This corrected L3(4) is still enough for L4, because L4 only needs one nearby modified-game equilibrium table, not a whole tail of them.

## L5. Neighborhood robustness of the local block data

[BREAKDOWN_AMEND] For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
[
\Gamma_i^{T,z}(s,\xi)
:=
\mathbb E_s^\xi!\left[\frac1T\sum_{t=1}^T u_i(s_t,a_t)+ z_i(s_{T+1})\right].
]
If a different normalization of the terminal bonus is intended, the radius chosen below must be scaled by that coefficient.

Assume L4 for some (w\in W), with data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr).
]
Set (T:=T(w)) and (\sigma:=\sigma(w)) for brevity.

Let (w'\in W). For any initial state (s), any player (i), and any profile (\xi),
[
\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)
============================================

\mathbb E_s^\xi!\left[w'*i(s*{T+1})-w_i(s_{T+1})\right].
]
Therefore
[
\bigl|\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)\bigr|
\le |w'-w|_\infty.
\tag{1}
]

By L4(1), for every deviation (\tau_i),
[
\Gamma_i^{T,w}(s,\sigma)\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma_{-i})\bigr)-\eta_{\mathrm{blk}}.
\tag{2}
]
Combining (1) and (2),
[
\Gamma_i^{T,w'}(s,\sigma)
\ge
\Gamma_i^{T,w}(s,\sigma)-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w'}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-2|w'-w|*\infty.
]
Hence, if
[
|w'-w|*\infty<\eta_{\mathrm{blk}}/2,
]
then (\sigma) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T)-stage game with terminal bonus (w').

Now define
[
U(w):=W\cap B_{\eta_{\mathrm{blk}}/2}(w).
]
This is an open neighborhood of (w) in the relative topology of (W). For every (w'\in U(w)), property (1) above gives the equilibrium robustness just proved.

L4(2) and L4(3) do not involve the terminal bonus at all. The play law under the fixed strategy (\sigma(w)) in the original stochastic game is unchanged when the auxiliary terminal bonus is changed from (w) to (w'). Therefore the stronger statements
[
\text{original-game average payoff is still }\eta_{\mathrm{blk}}\text{-close to }f(w),
]
and
[
\mathbb P(R(w))\ge \mu(w)
]
continue to hold verbatim. The weaker bounds (2\eta_{\mathrm{blk}}) and (\mu(w)/2) in L5 then follow immediately.

[DERIVED] L5 follows from L4. In fact, the proof yields the sharper neighborhood (U(w)=W\cap B_{\eta_{\mathrm{blk}}/2}(w)), and L5(2)-L5(3) can be kept with the original L4 constants.

## L6. Finite block atlas over (W)

Assume L5. For each (w\in W), L5 provides an open neighborhood (U(w)\subset W) and block data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr)
]
such that for every (w'\in U(w)):

1. (\sigma(w)) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T(w))-stage game with terminal bonus (w');
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close to (f(w));
3. (\mathbb P(R(w))\ge \mu(w)/2).

By L3, (W) is compact. Therefore the open cover ({U(w):w\in W}) has a finite subcover
[
U(w^1),\dots,U(w^M).
]
For (m=1,\dots,M), set
[
U_m:=U(w^m),\quad
T_m:=T(w^m),\quad
\sigma^m:=\sigma(w^m),\quad
f_m:=f(w^m),\quad
R_m:=R(w^m),\quad
\mu_m:=\mu(w^m)/2.
]

Then, whenever (w\in U_m),

1. (\sigma^m) is a (2\eta_{\mathrm{blk}})-equilibrium, hence a fortiori a (3\eta_{\mathrm{blk}})-equilibrium, of the (T_m)-stage game with terminal bonus (w);
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close, hence (3\eta_{\mathrm{blk}})-close, to (f_m);
3. (\mathbb P(R_m)\ge \mu_m>0).

Because the family is finite,
[
T_{\max}:=\max_{1\le m\le M} T_m<\infty,
\qquad
\mu_{\min}:=\min_{1\le m\le M}\mu_m>0.
]

[DERIVED] L6 follows from L5 and compactness of (W).

## L7. Approximate finite-orbit theorem for the continuation map

Assume L6. Define the directed graph on ({1,\dots,M}) by
[
m\to m'
\quad\Longleftrightarrow\quad
U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m)\neq\varnothing.
]

Fix any node (m). By construction in L6, (f_m\in W). Since (U_1,\dots,U_M) cover (W), there exists some (m') with
[
f_m\in U_{m'}.
]
Also (f_m\in B_{\eta_{\mathrm{orb}}}(f_m)). Hence
[
f_m\in U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m),
]
so (m\to m'). Thus every node has outdegree at least one.

Now start from any node and follow one outgoing edge at each step. Because the graph is finite, some node repeats. If the first repeated node is (m_r=m_t) with (r<t), then
[
m_r\to m_{r+1}\to\cdots\to m_{t-1}\to m_t(=m_r)
]
is a directed cycle. Rename this cycle
[
m_1\to m_2\to \cdots \to m_K\to m_1.
]

For each edge (m_k\to m_{k+1}), choose
[
w^{m_{k+1}}\in U_{m_{k+1}}\cap B_{\eta_{\mathrm{orb}}}(f_{m_k}),
]
which is possible by the edge definition. Then
[
|w^{m_{k+1}}-f_{m_k}|*\infty\le \eta*{\mathrm{orb}}
\qquad (k=1,\dots,K,\text{ cyclically}).
]
Equivalently, ((w^{m_1},\dots,w^{m_K})) is a finite (\eta_{\mathrm{orb}})-pseudo-orbit for the continuation data selected by the atlas.

[DERIVED] L7 follows from L6.

## L10-L11 bookkeeping: two necessary repairs, then closure

[BREAKDOWN_AMEND] L10 and L11 need two bookkeeping repairs.

1. After L8, each block has been **regularized** by appending a reset subphase. Let (B_m) be the full length of regularized block type (m), and set
   [
   B_{\max}:=\max_m B_m.
   ]
   The remainder estimate in L10 must use (B_{\max}), not the pre-regularization (T_{\max}) from L6.

2. The endpoint term in L9 must be stated in (T)-normalized form. What L10 actually needs is a bound of the form
   [
   \bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma^**{-i})\bigr)
   \le
   \bar\gamma^{T,\mathrm{cmp}}*i(s,\sigma^*)
   +
   C(\eta*{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
   +\frac{c_0}{T},
   \tag{L9'}
   ]
   for some finite constant (c_0) independent of (T), where (\bar\gamma^{T,\mathrm{cmp}}) denotes the payoff from complete regularized blocks only, normalized by the full horizon (T). Without this (1/T) normalization of the endpoint term, L10 does not follow.

3. The symbol (\eta_{\mathrm{tail}}) in L11 is otherwise floating. Either delete it, or identify it with a chosen upper bound for (c_0/T) once (T\ge T_0). The cleaner closure is to absorb it directly into ((c_0+B_{\max})/T).

### Amended L10

Assume (L9'). Fix (T), and let (L(T)) be the total number of stages occupied by complete regularized blocks before time (T). Then the first (T) stages consist of:

* the first (L(T)) stages, which form complete regularized blocks, and
* a final tail of length (T-L(T)), with
  [
  0\le T-L(T)<B_{\max}.
  ]

For any strategy profile (\xi), define
[
\bar\gamma^{T,\mathrm{cmp}}*i(s,\xi)
:=
\frac1T,\mathbb E_s^\xi!\left[\sum*{t=1}^{L(T)} u_i(s_t,a_t)\right].
]
Since stage payoffs lie in ([0,1]),
[
0\le
\gamma_i^T(s,\xi)-\bar\gamma^{T,\mathrm{cmp}}_i(s,\xi)
======================================================

\frac1T,\mathbb E_s^\xi!\left[\sum_{t=L(T)+1}^{T}u_i(s_t,a_t)\right]
\le \frac{B_{\max}}{T}.
\tag{3}
]
Apply (3) to (\xi=(\tau_i,\sigma_{-i}^*)) and to (\xi=\sigma^*). For the deviating profile,
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma*{-i}^*)\bigr)
+\frac{B_{\max}}{T}.
]
For the baseline profile,
[
\gamma_i^T(s,\sigma^*)\ge \bar\gamma^{T,\mathrm{cmp}}_i(s,\sigma^*).
]
Subtracting and using (L9') yields
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
----------------------------------------------

\gamma_i^T(s,\sigma^*)
\le
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

[DERIVED] The corrected form of L10 is:
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)
+
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

### Amended L11

Choose the internal tolerances so that
[
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})<\varepsilon/2.
]
Because (c_0+B_{\max}<\infty), choose (T_0) so large that
[
\frac{c_0+B_{\max}}{T}\le \varepsilon/2
\qquad\text{for all }T\ge T_0.
]
Then for every player (i), state (s), deviation (\tau_i), and horizon (T\ge T_0),
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)+\varepsilon.
]
This is exactly the uniform (\varepsilon)-equilibrium inequality.

[DERIVED] The corrected form of L11 follows from the corrected L10.

## Status summary

* [DERIVED] L1, under the coalition-control amendment and the compact-action zero-sum uniform-value assumption.
* [DERIVED] L2(3).
* [DERIVED] L3(1)-(3), and corrected L3(4) with “arbitrarily close (\lambda)” replacing “all (\lambda) close enough”.
* [DERIVED] L5 from L4.
* [DERIVED] L6 from L5 and L3.
* [DERIVED] L7 from L6.
* [DERIVED] Corrected L10 from sharpened L9.
* [DERIVED] Corrected L11 from corrected L10.

Open or still imported:

* L2(1)-(2) remain imported from the modified-game theorem.
* L4 is still the main unresolved seam.
* L8 is not yet proved.
* L9 needs its normalization written precisely in the (T)-average scale used by L10.
* The original versions of L3(4), L10, and L11 should be replaced by the corrected versions above.

## FILE: branches/main/context/prover_02.md

# Prover Output

Generated: 2026-03-23T05:23:04.242821+00:00

Using the supplied breakdown and the durable reading of the target as existence of one profile that is an (\varepsilon)-equilibrium for every sufficiently large horizon and every initial state, the clean advances in this pass are: L1 under one explicit coalition-control amendment, L2(3), L3 with a necessary correction to part (4), L5, L6, L7, and the final L10-L11 bookkeeping after two precise normalization repairs. The theorem-sized seam is still L4, and L8-L9 are still not closed.   

[BREAKDOWN_AMEND] In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
[
b_{-i}\in B_i(s):=\prod_{j\neq i}\Delta(A_j(s))
]
at each public history ending at state (s), not an arbitrary correlated distribution on (A_{-i}(s):=\prod_{j\neq i}A_j(s)). Otherwise there is a correlation-implementation gap when one tries to unfold the minimizer back into separate punishers in the original game.

[ASSUMPTION+] The classical uniform-value theorem is available for finite-state zero-sum stochastic games with compact action spaces and continuous stage payoff and transition data. This is the version needed for the product-mixed auxiliary game just described.

## L1. Uniform minmax values and restartable punishments

Fix (i\in N). Define the auxiliary two-side zero-sum stochastic game (\widehat G_i) as follows. The state space is (S). The maximizing player is player (i), with action set (A_i(s)) in state (s). The minimizing player is the coalition controller, with action set
[
B_i(s)=\prod_{j\neq i}\Delta(A_j(s)).
]
For (a_i\in A_i(s)) and (b_{-i}=(b_j)*{j\neq i}\in B_i(s)), define
[
\widehat u_i(s,a_i,b*{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),u_i(s,a_i,a_{-i}),
]
and
[
\widehat P_i(s'\mid s,a_i,b_{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),P(s'\mid s,a_i,a_{-i}).
]

The state space is finite, each (A_i(s)) is finite, each (B_i(s)) is compact, and ((\widehat u_i,\widehat P_i)) are continuous in (b_{-i}) by direct finite summation. By [ASSUMPTION+] and the zero-sum uniform-value theorem, there exists a value (v_i(s)) for every initial state (s), and for every (\delta>0) there exists a minimizing strategy (\pi_{-i}^\delta) in (\widehat G_i) such that for every (s\in S) there is (T_i^\delta(s)) with
[
\gamma_i^T\bigl(s,(\tau_i,\pi_{-i}^\delta)\bigr)\le v_i(s)+\delta
]
for every (T\ge T_i^\delta(s)) and every strategy (\tau_i) of player (i).

Because (S) is finite, the number
[
T_i^\delta:=\max_{s\in S} T_i^\delta(s)
]
is finite. Hence the same minimizing strategy works for all initial states once (T\ge T_i^\delta).

Now unfold (\pi_{-i}^\delta) into a public punishment profile (P_i^\delta) in the original game: after every public history (h_t) ending at state (s_t), each player (j\neq i) independently uses the mixed action prescribed by the (j)-th coordinate of (\pi_{-i}^\delta(h_t)). By construction of ((\widehat u_i,\widehat P_i)), the law of the state/action process under ((\tau_i,P_i^\delta)) in the original game is exactly the law of the auxiliary game under ((\tau_i,\pi_{-i}^\delta)). Therefore
[
\gamma_i^T\bigl(s,(\tau_i,P_i^\delta)\bigr)\le v_i(s)+\delta
]
for all (s\in S), all (T\ge T_i^\delta), and all (\tau_i).

Finally, restartability is immediate. After any public history ending at state (s), define the continuation punishment to be a fresh copy of the same strategy (\pi_{-i}^\delta) started from state (s). This is legitimate because strategies in the model are defined on public histories, and future play depends only on the future continuation strategy together with the current state.

[DERIVED] L1 holds under the coalition-action amendment above and [ASSUMPTION+].

## A small clean-up inside L2

The precompactness clause L2(3) does not need any modified-game theorem.

Indeed, by the statement of L2, every equilibrium payoff table satisfies
[
m^\lambda\in [0,1]^{N\times S}.
]
Since (N) and (S) are finite, the cube ([0,1]^{N\times S}) is compact in the sup norm. Any subset of a compact metric space is precompact.

[DERIVED] L2(3) is immediate from (m^\lambda\in[0,1]^{N\times S}).

I do **not** claim L2(1)-(2) here. Those remain imported from the modified-game machinery.

## L3. Compact continuation region (W)

All norms and balls below are sup norms on ([0,1]^{N\times S}).

[BREAKDOWN_AMEND] L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.

Take any sequence (\lambda_n\uparrow 1) in the domain where (m^{\lambda_n}) is defined. By L2(3), the family ((m^{\lambda_n})) is precompact, so it has a convergent subsequence, say
[
m^{\lambda_{n_k}}\to w\in [0,1]^{N\times S}.
]
By definition of (W), this limit (w) belongs to (W). Hence (W\neq\varnothing).

To prove compactness, let ((w^q)\subset W) be a convergent sequence with (w^q\to w) in ([0,1]^{N\times S}). We show (w\in W). Fix (\rho>0) and (\lambda_0<1). Choose (q) so large that
[
|w^q-w|*\infty<\rho/2.
]
Since (w^q\in W), (w^q) is an accumulation point of ((m^\lambda)), so there exists (\lambda\in(\lambda_0,1)) with
[
|m^\lambda-w^q|*\infty<\rho/2.
]
By the triangle inequality,
[
|m^\lambda-w|*\infty\le |m^\lambda-w^q|*\infty+|w^q-w|_\infty<\rho.
]
Because (\rho) and (\lambda_0) were arbitrary, (w) is also an accumulation point. Hence (W) is closed in the compact cube ([0,1]^{N\times S}), therefore compact.

For the minmax lower bound, let (w\in W). By definition, there exists a sequence (\lambda_n\uparrow 1) with
[
m^{\lambda_n}\to w.
]
By L2(1),
[
m_i^{\lambda_n}(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }n.
]
Passing to the limit coordinatewise gives
[
w_i(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }(i,s).
]

The corrected approximation property is now immediate from the definition of accumulation point:

[
\forall w\in W,\ \forall \text{ neighborhoods }U\ni w,\ \forall \lambda_0<1,\ \exists \lambda\in(\lambda_0,1)
\text{ such that } m^\lambda\in U.
]

[DERIVED] L3(1), L3(2), and L3(3) are proved from L2.
[DERIVED] The correct replacement for L3(4) is the arbitrarily-close-(\lambda) version just displayed.

This corrected L3(4) is still enough for L4, because L4 only needs one nearby modified-game equilibrium table, not a whole tail of them.

## L5. Neighborhood robustness of the local block data

[BREAKDOWN_AMEND] For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
[
\Gamma_i^{T,z}(s,\xi)
:=
\mathbb E_s^\xi!\left[\frac1T\sum_{t=1}^T u_i(s_t,a_t)+ z_i(s_{T+1})\right].
]
If a different normalization of the terminal bonus is intended, the radius chosen below must be scaled by that coefficient.

Assume L4 for some (w\in W), with data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr).
]
Set (T:=T(w)) and (\sigma:=\sigma(w)) for brevity.

Let (w'\in W). For any initial state (s), any player (i), and any profile (\xi),
[
\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)
============================================

\mathbb E_s^\xi!\left[w'*i(s*{T+1})-w_i(s_{T+1})\right].
]
Therefore
[
\bigl|\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)\bigr|
\le |w'-w|_\infty.
\tag{1}
]

By L4(1), for every deviation (\tau_i),
[
\Gamma_i^{T,w}(s,\sigma)\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma_{-i})\bigr)-\eta_{\mathrm{blk}}.
\tag{2}
]
Combining (1) and (2),
[
\Gamma_i^{T,w'}(s,\sigma)
\ge
\Gamma_i^{T,w}(s,\sigma)-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w'}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-2|w'-w|*\infty.
]
Hence, if
[
|w'-w|*\infty<\eta_{\mathrm{blk}}/2,
]
then (\sigma) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T)-stage game with terminal bonus (w').

Now define
[
U(w):=W\cap B_{\eta_{\mathrm{blk}}/2}(w).
]
This is an open neighborhood of (w) in the relative topology of (W). For every (w'\in U(w)), property (1) above gives the equilibrium robustness just proved.

L4(2) and L4(3) do not involve the terminal bonus at all. The play law under the fixed strategy (\sigma(w)) in the original stochastic game is unchanged when the auxiliary terminal bonus is changed from (w) to (w'). Therefore the stronger statements
[
\text{original-game average payoff is still }\eta_{\mathrm{blk}}\text{-close to }f(w),
]
and
[
\mathbb P(R(w))\ge \mu(w)
]
continue to hold verbatim. The weaker bounds (2\eta_{\mathrm{blk}}) and (\mu(w)/2) in L5 then follow immediately.

[DERIVED] L5 follows from L4. In fact, the proof yields the sharper neighborhood (U(w)=W\cap B_{\eta_{\mathrm{blk}}/2}(w)), and L5(2)-L5(3) can be kept with the original L4 constants.

## L6. Finite block atlas over (W)

Assume L5. For each (w\in W), L5 provides an open neighborhood (U(w)\subset W) and block data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr)
]
such that for every (w'\in U(w)):

1. (\sigma(w)) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T(w))-stage game with terminal bonus (w');
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close to (f(w));
3. (\mathbb P(R(w))\ge \mu(w)/2).

By L3, (W) is compact. Therefore the open cover ({U(w):w\in W}) has a finite subcover
[
U(w^1),\dots,U(w^M).
]
For (m=1,\dots,M), set
[
U_m:=U(w^m),\quad
T_m:=T(w^m),\quad
\sigma^m:=\sigma(w^m),\quad
f_m:=f(w^m),\quad
R_m:=R(w^m),\quad
\mu_m:=\mu(w^m)/2.
]

Then, whenever (w\in U_m),

1. (\sigma^m) is a (2\eta_{\mathrm{blk}})-equilibrium, hence a fortiori a (3\eta_{\mathrm{blk}})-equilibrium, of the (T_m)-stage game with terminal bonus (w);
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close, hence (3\eta_{\mathrm{blk}})-close, to (f_m);
3. (\mathbb P(R_m)\ge \mu_m>0).

Because the family is finite,
[
T_{\max}:=\max_{1\le m\le M} T_m<\infty,
\qquad
\mu_{\min}:=\min_{1\le m\le M}\mu_m>0.
]

[DERIVED] L6 follows from L5 and compactness of (W).

## L7. Approximate finite-orbit theorem for the continuation map

Assume L6. Define the directed graph on ({1,\dots,M}) by
[
m\to m'
\quad\Longleftrightarrow\quad
U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m)\neq\varnothing.
]

Fix any node (m). By construction in L6, (f_m\in W). Since (U_1,\dots,U_M) cover (W), there exists some (m') with
[
f_m\in U_{m'}.
]
Also (f_m\in B_{\eta_{\mathrm{orb}}}(f_m)). Hence
[
f_m\in U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m),
]
so (m\to m'). Thus every node has outdegree at least one.

Now start from any node and follow one outgoing edge at each step. Because the graph is finite, some node repeats. If the first repeated node is (m_r=m_t) with (r<t), then
[
m_r\to m_{r+1}\to\cdots\to m_{t-1}\to m_t(=m_r)
]
is a directed cycle. Rename this cycle
[
m_1\to m_2\to \cdots \to m_K\to m_1.
]

For each edge (m_k\to m_{k+1}), choose
[
w^{m_{k+1}}\in U_{m_{k+1}}\cap B_{\eta_{\mathrm{orb}}}(f_{m_k}),
]
which is possible by the edge definition. Then
[
|w^{m_{k+1}}-f_{m_k}|*\infty\le \eta*{\mathrm{orb}}
\qquad (k=1,\dots,K,\text{ cyclically}).
]
Equivalently, ((w^{m_1},\dots,w^{m_K})) is a finite (\eta_{\mathrm{orb}})-pseudo-orbit for the continuation data selected by the atlas.

[DERIVED] L7 follows from L6.

## L10-L11 bookkeeping: two necessary repairs, then closure

[BREAKDOWN_AMEND] L10 and L11 need two bookkeeping repairs.

1. After L8, each block has been **regularized** by appending a reset subphase. Let (B_m) be the full length of regularized block type (m), and set
   [
   B_{\max}:=\max_m B_m.
   ]
   The remainder estimate in L10 must use (B_{\max}), not the pre-regularization (T_{\max}) from L6.

2. The endpoint term in L9 must be stated in (T)-normalized form. What L10 actually needs is a bound of the form
   [
   \bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma^**{-i})\bigr)
   \le
   \bar\gamma^{T,\mathrm{cmp}}*i(s,\sigma^*)
   +
   C(\eta*{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
   +\frac{c_0}{T},
   \tag{L9'}
   ]
   for some finite constant (c_0) independent of (T), where (\bar\gamma^{T,\mathrm{cmp}}) denotes the payoff from complete regularized blocks only, normalized by the full horizon (T). Without this (1/T) normalization of the endpoint term, L10 does not follow.

3. The symbol (\eta_{\mathrm{tail}}) in L11 is otherwise floating. Either delete it, or identify it with a chosen upper bound for (c_0/T) once (T\ge T_0). The cleaner closure is to absorb it directly into ((c_0+B_{\max})/T).

### Amended L10

Assume (L9'). Fix (T), and let (L(T)) be the total number of stages occupied by complete regularized blocks before time (T). Then the first (T) stages consist of:

* the first (L(T)) stages, which form complete regularized blocks, and
* a final tail of length (T-L(T)), with
  [
  0\le T-L(T)<B_{\max}.
  ]

For any strategy profile (\xi), define
[
\bar\gamma^{T,\mathrm{cmp}}*i(s,\xi)
:=
\frac1T,\mathbb E_s^\xi!\left[\sum*{t=1}^{L(T)} u_i(s_t,a_t)\right].
]
Since stage payoffs lie in ([0,1]),
[
0\le
\gamma_i^T(s,\xi)-\bar\gamma^{T,\mathrm{cmp}}_i(s,\xi)
======================================================

\frac1T,\mathbb E_s^\xi!\left[\sum_{t=L(T)+1}^{T}u_i(s_t,a_t)\right]
\le \frac{B_{\max}}{T}.
\tag{3}
]
Apply (3) to (\xi=(\tau_i,\sigma_{-i}^*)) and to (\xi=\sigma^*). For the deviating profile,
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma*{-i}^*)\bigr)
+\frac{B_{\max}}{T}.
]
For the baseline profile,
[
\gamma_i^T(s,\sigma^*)\ge \bar\gamma^{T,\mathrm{cmp}}_i(s,\sigma^*).
]
Subtracting and using (L9') yields
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
----------------------------------------------

\gamma_i^T(s,\sigma^*)
\le
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

[DERIVED] The corrected form of L10 is:
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)
+
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

### Amended L11

Choose the internal tolerances so that
[
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})<\varepsilon/2.
]
Because (c_0+B_{\max}<\infty), choose (T_0) so large that
[
\frac{c_0+B_{\max}}{T}\le \varepsilon/2
\qquad\text{for all }T\ge T_0.
]
Then for every player (i), state (s), deviation (\tau_i), and horizon (T\ge T_0),
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)+\varepsilon.
]
This is exactly the uniform (\varepsilon)-equilibrium inequality.

[DERIVED] The corrected form of L11 follows from the corrected L10.

## Status summary

* [DERIVED] L1, under the coalition-control amendment and the compact-action zero-sum uniform-value assumption.
* [DERIVED] L2(3).
* [DERIVED] L3(1)-(3), and corrected L3(4) with “arbitrarily close (\lambda)” replacing “all (\lambda) close enough”.
* [DERIVED] L5 from L4.
* [DERIVED] L6 from L5 and L3.
* [DERIVED] L7 from L6.
* [DERIVED] Corrected L10 from sharpened L9.
* [DERIVED] Corrected L11 from corrected L10.

Open or still imported:

* L2(1)-(2) remain imported from the modified-game theorem.
* L4 is still the main unresolved seam.
* L8 is not yet proved.
* L9 needs its normalization written precisely in the (T)-average scale used by L10.
* The original versions of L3(4), L10, and L11 should be replaced by the corrected versions above.

## FILE: branches/main/context/prover_03.md

# Prover Output

Generated: 2026-03-23T05:23:04.267057+00:00

Using the supplied breakdown and the durable reading of the target as existence of one profile that is an (\varepsilon)-equilibrium for every sufficiently large horizon and every initial state, the clean advances in this pass are: L1 under one explicit coalition-control amendment, L2(3), L3 with a necessary correction to part (4), L5, L6, L7, and the final L10-L11 bookkeeping after two precise normalization repairs. The theorem-sized seam is still L4, and L8-L9 are still not closed.   

[BREAKDOWN_AMEND] In Setup and L1, the object (v_i(s)) must be defined in a way that can be implemented by an actual punishment profile of players (N\setminus{i}) in the original game. The safe formulation is this: in the auxiliary zero-sum game for player (i), the minimizing side chooses a **product mixed action**
[
b_{-i}\in B_i(s):=\prod_{j\neq i}\Delta(A_j(s))
]
at each public history ending at state (s), not an arbitrary correlated distribution on (A_{-i}(s):=\prod_{j\neq i}A_j(s)). Otherwise there is a correlation-implementation gap when one tries to unfold the minimizer back into separate punishers in the original game.

[ASSUMPTION+] The classical uniform-value theorem is available for finite-state zero-sum stochastic games with compact action spaces and continuous stage payoff and transition data. This is the version needed for the product-mixed auxiliary game just described.

## L1. Uniform minmax values and restartable punishments

Fix (i\in N). Define the auxiliary two-side zero-sum stochastic game (\widehat G_i) as follows. The state space is (S). The maximizing player is player (i), with action set (A_i(s)) in state (s). The minimizing player is the coalition controller, with action set
[
B_i(s)=\prod_{j\neq i}\Delta(A_j(s)).
]
For (a_i\in A_i(s)) and (b_{-i}=(b_j)*{j\neq i}\in B_i(s)), define
[
\widehat u_i(s,a_i,b*{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),u_i(s,a_i,a_{-i}),
]
and
[
\widehat P_i(s'\mid s,a_i,b_{-i})
:=
\sum_{a_{-i}\in A_{-i}(s)}
\Bigl(\prod_{j\neq i} b_j(a_j)\Bigr),P(s'\mid s,a_i,a_{-i}).
]

The state space is finite, each (A_i(s)) is finite, each (B_i(s)) is compact, and ((\widehat u_i,\widehat P_i)) are continuous in (b_{-i}) by direct finite summation. By [ASSUMPTION+] and the zero-sum uniform-value theorem, there exists a value (v_i(s)) for every initial state (s), and for every (\delta>0) there exists a minimizing strategy (\pi_{-i}^\delta) in (\widehat G_i) such that for every (s\in S) there is (T_i^\delta(s)) with
[
\gamma_i^T\bigl(s,(\tau_i,\pi_{-i}^\delta)\bigr)\le v_i(s)+\delta
]
for every (T\ge T_i^\delta(s)) and every strategy (\tau_i) of player (i).

Because (S) is finite, the number
[
T_i^\delta:=\max_{s\in S} T_i^\delta(s)
]
is finite. Hence the same minimizing strategy works for all initial states once (T\ge T_i^\delta).

Now unfold (\pi_{-i}^\delta) into a public punishment profile (P_i^\delta) in the original game: after every public history (h_t) ending at state (s_t), each player (j\neq i) independently uses the mixed action prescribed by the (j)-th coordinate of (\pi_{-i}^\delta(h_t)). By construction of ((\widehat u_i,\widehat P_i)), the law of the state/action process under ((\tau_i,P_i^\delta)) in the original game is exactly the law of the auxiliary game under ((\tau_i,\pi_{-i}^\delta)). Therefore
[
\gamma_i^T\bigl(s,(\tau_i,P_i^\delta)\bigr)\le v_i(s)+\delta
]
for all (s\in S), all (T\ge T_i^\delta), and all (\tau_i).

Finally, restartability is immediate. After any public history ending at state (s), define the continuation punishment to be a fresh copy of the same strategy (\pi_{-i}^\delta) started from state (s). This is legitimate because strategies in the model are defined on public histories, and future play depends only on the future continuation strategy together with the current state.

[DERIVED] L1 holds under the coalition-action amendment above and [ASSUMPTION+].

## A small clean-up inside L2

The precompactness clause L2(3) does not need any modified-game theorem.

Indeed, by the statement of L2, every equilibrium payoff table satisfies
[
m^\lambda\in [0,1]^{N\times S}.
]
Since (N) and (S) are finite, the cube ([0,1]^{N\times S}) is compact in the sup norm. Any subset of a compact metric space is precompact.

[DERIVED] L2(3) is immediate from (m^\lambda\in[0,1]^{N\times S}).

I do **not** claim L2(1)-(2) here. Those remain imported from the modified-game machinery.

## L3. Compact continuation region (W)

All norms and balls below are sup norms on ([0,1]^{N\times S}).

[BREAKDOWN_AMEND] L3(4) is too strong as written. If (W) is defined as the set of accumulation points of one selected family ((m^\lambda)_{\lambda\uparrow 1}), then one can conclude only that every neighborhood of (w\in W) contains some (m^\lambda) for arbitrarily large (\lambda), not for **all** (\lambda) sufficiently close to (1). The stronger statement would require an additional lower-hemicontinuity theorem for the equilibrium correspondence, which is not presently in the stack.

Take any sequence (\lambda_n\uparrow 1) in the domain where (m^{\lambda_n}) is defined. By L2(3), the family ((m^{\lambda_n})) is precompact, so it has a convergent subsequence, say
[
m^{\lambda_{n_k}}\to w\in [0,1]^{N\times S}.
]
By definition of (W), this limit (w) belongs to (W). Hence (W\neq\varnothing).

To prove compactness, let ((w^q)\subset W) be a convergent sequence with (w^q\to w) in ([0,1]^{N\times S}). We show (w\in W). Fix (\rho>0) and (\lambda_0<1). Choose (q) so large that
[
|w^q-w|*\infty<\rho/2.
]
Since (w^q\in W), (w^q) is an accumulation point of ((m^\lambda)), so there exists (\lambda\in(\lambda_0,1)) with
[
|m^\lambda-w^q|*\infty<\rho/2.
]
By the triangle inequality,
[
|m^\lambda-w|*\infty\le |m^\lambda-w^q|*\infty+|w^q-w|_\infty<\rho.
]
Because (\rho) and (\lambda_0) were arbitrary, (w) is also an accumulation point. Hence (W) is closed in the compact cube ([0,1]^{N\times S}), therefore compact.

For the minmax lower bound, let (w\in W). By definition, there exists a sequence (\lambda_n\uparrow 1) with
[
m^{\lambda_n}\to w.
]
By L2(1),
[
m_i^{\lambda_n}(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }n.
]
Passing to the limit coordinatewise gives
[
w_i(s)\ge v_i(s)-\eta_{\mathrm{mm}}
\qquad\text{for all }(i,s).
]

The corrected approximation property is now immediate from the definition of accumulation point:

[
\forall w\in W,\ \forall \text{ neighborhoods }U\ni w,\ \forall \lambda_0<1,\ \exists \lambda\in(\lambda_0,1)
\text{ such that } m^\lambda\in U.
]

[DERIVED] L3(1), L3(2), and L3(3) are proved from L2.
[DERIVED] The correct replacement for L3(4) is the arbitrarily-close-(\lambda) version just displayed.

This corrected L3(4) is still enough for L4, because L4 only needs one nearby modified-game equilibrium table, not a whole tail of them.

## L5. Neighborhood robustness of the local block data

[BREAKDOWN_AMEND] For L4-L6, fix the meaning of “(T)-stage game with terminal bonus (z)” as
[
\Gamma_i^{T,z}(s,\xi)
:=
\mathbb E_s^\xi!\left[\frac1T\sum_{t=1}^T u_i(s_t,a_t)+ z_i(s_{T+1})\right].
]
If a different normalization of the terminal bonus is intended, the radius chosen below must be scaled by that coefficient.

Assume L4 for some (w\in W), with data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr).
]
Set (T:=T(w)) and (\sigma:=\sigma(w)) for brevity.

Let (w'\in W). For any initial state (s), any player (i), and any profile (\xi),
[
\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)
============================================

\mathbb E_s^\xi!\left[w'*i(s*{T+1})-w_i(s_{T+1})\right].
]
Therefore
[
\bigl|\Gamma_i^{T,w'}(s,\xi)-\Gamma_i^{T,w}(s,\xi)\bigr|
\le |w'-w|_\infty.
\tag{1}
]

By L4(1), for every deviation (\tau_i),
[
\Gamma_i^{T,w}(s,\sigma)\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma_{-i})\bigr)-\eta_{\mathrm{blk}}.
\tag{2}
]
Combining (1) and (2),
[
\Gamma_i^{T,w'}(s,\sigma)
\ge
\Gamma_i^{T,w}(s,\sigma)-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-|w'-w|*\infty
]
[
\ge
\Gamma_i^{T,w'}\bigl(s,(\tau_i,\sigma*{-i})\bigr)-\eta_{\mathrm{blk}}-2|w'-w|*\infty.
]
Hence, if
[
|w'-w|*\infty<\eta_{\mathrm{blk}}/2,
]
then (\sigma) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T)-stage game with terminal bonus (w').

Now define
[
U(w):=W\cap B_{\eta_{\mathrm{blk}}/2}(w).
]
This is an open neighborhood of (w) in the relative topology of (W). For every (w'\in U(w)), property (1) above gives the equilibrium robustness just proved.

L4(2) and L4(3) do not involve the terminal bonus at all. The play law under the fixed strategy (\sigma(w)) in the original stochastic game is unchanged when the auxiliary terminal bonus is changed from (w) to (w'). Therefore the stronger statements
[
\text{original-game average payoff is still }\eta_{\mathrm{blk}}\text{-close to }f(w),
]
and
[
\mathbb P(R(w))\ge \mu(w)
]
continue to hold verbatim. The weaker bounds (2\eta_{\mathrm{blk}}) and (\mu(w)/2) in L5 then follow immediately.

[DERIVED] L5 follows from L4. In fact, the proof yields the sharper neighborhood (U(w)=W\cap B_{\eta_{\mathrm{blk}}/2}(w)), and L5(2)-L5(3) can be kept with the original L4 constants.

## L6. Finite block atlas over (W)

Assume L5. For each (w\in W), L5 provides an open neighborhood (U(w)\subset W) and block data
[
\bigl(T(w),\sigma(w),f(w),R(w),\mu(w)\bigr)
]
such that for every (w'\in U(w)):

1. (\sigma(w)) is a (2\eta_{\mathrm{blk}})-equilibrium of the (T(w))-stage game with terminal bonus (w');
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close to (f(w));
3. (\mathbb P(R(w))\ge \mu(w)/2).

By L3, (W) is compact. Therefore the open cover ({U(w):w\in W}) has a finite subcover
[
U(w^1),\dots,U(w^M).
]
For (m=1,\dots,M), set
[
U_m:=U(w^m),\quad
T_m:=T(w^m),\quad
\sigma^m:=\sigma(w^m),\quad
f_m:=f(w^m),\quad
R_m:=R(w^m),\quad
\mu_m:=\mu(w^m)/2.
]

Then, whenever (w\in U_m),

1. (\sigma^m) is a (2\eta_{\mathrm{blk}})-equilibrium, hence a fortiori a (3\eta_{\mathrm{blk}})-equilibrium, of the (T_m)-stage game with terminal bonus (w);
2. the induced original-game average payoff is (2\eta_{\mathrm{blk}})-close, hence (3\eta_{\mathrm{blk}})-close, to (f_m);
3. (\mathbb P(R_m)\ge \mu_m>0).

Because the family is finite,
[
T_{\max}:=\max_{1\le m\le M} T_m<\infty,
\qquad
\mu_{\min}:=\min_{1\le m\le M}\mu_m>0.
]

[DERIVED] L6 follows from L5 and compactness of (W).

## L7. Approximate finite-orbit theorem for the continuation map

Assume L6. Define the directed graph on ({1,\dots,M}) by
[
m\to m'
\quad\Longleftrightarrow\quad
U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m)\neq\varnothing.
]

Fix any node (m). By construction in L6, (f_m\in W). Since (U_1,\dots,U_M) cover (W), there exists some (m') with
[
f_m\in U_{m'}.
]
Also (f_m\in B_{\eta_{\mathrm{orb}}}(f_m)). Hence
[
f_m\in U_{m'}\cap B_{\eta_{\mathrm{orb}}}(f_m),
]
so (m\to m'). Thus every node has outdegree at least one.

Now start from any node and follow one outgoing edge at each step. Because the graph is finite, some node repeats. If the first repeated node is (m_r=m_t) with (r<t), then
[
m_r\to m_{r+1}\to\cdots\to m_{t-1}\to m_t(=m_r)
]
is a directed cycle. Rename this cycle
[
m_1\to m_2\to \cdots \to m_K\to m_1.
]

For each edge (m_k\to m_{k+1}), choose
[
w^{m_{k+1}}\in U_{m_{k+1}}\cap B_{\eta_{\mathrm{orb}}}(f_{m_k}),
]
which is possible by the edge definition. Then
[
|w^{m_{k+1}}-f_{m_k}|*\infty\le \eta*{\mathrm{orb}}
\qquad (k=1,\dots,K,\text{ cyclically}).
]
Equivalently, ((w^{m_1},\dots,w^{m_K})) is a finite (\eta_{\mathrm{orb}})-pseudo-orbit for the continuation data selected by the atlas.

[DERIVED] L7 follows from L6.

## L10-L11 bookkeeping: two necessary repairs, then closure

[BREAKDOWN_AMEND] L10 and L11 need two bookkeeping repairs.

1. After L8, each block has been **regularized** by appending a reset subphase. Let (B_m) be the full length of regularized block type (m), and set
   [
   B_{\max}:=\max_m B_m.
   ]
   The remainder estimate in L10 must use (B_{\max}), not the pre-regularization (T_{\max}) from L6.

2. The endpoint term in L9 must be stated in (T)-normalized form. What L10 actually needs is a bound of the form
   [
   \bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma^**{-i})\bigr)
   \le
   \bar\gamma^{T,\mathrm{cmp}}*i(s,\sigma^*)
   +
   C(\eta*{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
   +\frac{c_0}{T},
   \tag{L9'}
   ]
   for some finite constant (c_0) independent of (T), where (\bar\gamma^{T,\mathrm{cmp}}) denotes the payoff from complete regularized blocks only, normalized by the full horizon (T). Without this (1/T) normalization of the endpoint term, L10 does not follow.

3. The symbol (\eta_{\mathrm{tail}}) in L11 is otherwise floating. Either delete it, or identify it with a chosen upper bound for (c_0/T) once (T\ge T_0). The cleaner closure is to absorb it directly into ((c_0+B_{\max})/T).

### Amended L10

Assume (L9'). Fix (T), and let (L(T)) be the total number of stages occupied by complete regularized blocks before time (T). Then the first (T) stages consist of:

* the first (L(T)) stages, which form complete regularized blocks, and
* a final tail of length (T-L(T)), with
  [
  0\le T-L(T)<B_{\max}.
  ]

For any strategy profile (\xi), define
[
\bar\gamma^{T,\mathrm{cmp}}*i(s,\xi)
:=
\frac1T,\mathbb E_s^\xi!\left[\sum*{t=1}^{L(T)} u_i(s_t,a_t)\right].
]
Since stage payoffs lie in ([0,1]),
[
0\le
\gamma_i^T(s,\xi)-\bar\gamma^{T,\mathrm{cmp}}_i(s,\xi)
======================================================

\frac1T,\mathbb E_s^\xi!\left[\sum_{t=L(T)+1}^{T}u_i(s_t,a_t)\right]
\le \frac{B_{\max}}{T}.
\tag{3}
]
Apply (3) to (\xi=(\tau_i,\sigma_{-i}^*)) and to (\xi=\sigma^*). For the deviating profile,
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\bar\gamma^{T,\mathrm{cmp}}*i\bigl(s,(\tau_i,\sigma*{-i}^*)\bigr)
+\frac{B_{\max}}{T}.
]
For the baseline profile,
[
\gamma_i^T(s,\sigma^*)\ge \bar\gamma^{T,\mathrm{cmp}}_i(s,\sigma^*).
]
Subtracting and using (L9') yields
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
----------------------------------------------

\gamma_i^T(s,\sigma^*)
\le
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

[DERIVED] The corrected form of L10 is:
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)
+
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})
+\frac{c_0+B_{\max}}{T}.
]

### Amended L11

Choose the internal tolerances so that
[
C(\eta_{\mathrm{blk}}+\eta_{\mathrm{orb}}+\eta_{\mathrm{mon}})<\varepsilon/2.
]
Because (c_0+B_{\max}<\infty), choose (T_0) so large that
[
\frac{c_0+B_{\max}}{T}\le \varepsilon/2
\qquad\text{for all }T\ge T_0.
]
Then for every player (i), state (s), deviation (\tau_i), and horizon (T\ge T_0),
[
\gamma_i^T\bigl(s,(\tau_i,\sigma_{-i}^*)\bigr)
\le
\gamma_i^T(s,\sigma^*)+\varepsilon.
]
This is exactly the uniform (\varepsilon)-equilibrium inequality.

[DERIVED] The corrected form of L11 follows from the corrected L10.

## Status summary

* [DERIVED] L1, under the coalition-control amendment and the compact-action zero-sum uniform-value assumption.
* [DERIVED] L2(3).
* [DERIVED] L3(1)-(3), and corrected L3(4) with “arbitrarily close (\lambda)” replacing “all (\lambda) close enough”.
* [DERIVED] L5 from L4.
* [DERIVED] L6 from L5 and L3.
* [DERIVED] L7 from L6.
* [DERIVED] Corrected L10 from sharpened L9.
* [DERIVED] Corrected L11 from corrected L10.

Open or still imported:

* L2(1)-(2) remain imported from the modified-game theorem.
* L4 is still the main unresolved seam.
* L8 is not yet proved.
* L9 needs its normalization written precisely in the (T)-average scale used by L10.
* The original versions of L3(4), L10, and L11 should be replaced by the corrected versions above.

---
## ADDITIONAL LOADED FILES

### branches/main/context/assumption_delta.md

# Assumption Delta

- Added assumptions: 2
- Removed assumptions: 0
- Scope changes: 0
- Mode: semi_strict

### branches/main/context/strategy.md

# Searcher Output

Generated: 2026-03-23T02:57:22.328141+00:00

## Selected Route
**Hybrid modified-game + continuation-orbit construction.**

## Route Details
**Core technique:** Use a statewise auxiliary modified game to cap continuation payoffs at minmax-compatible levels, then build a compact continuation region (W) and a map (f) whose nodes are finite equilibrium blocks. The modified-game paper already supplies the auxiliary-game architecture and the stationary-equilibrium side, while the 2025 non-rectangular absorbing proof shows how each continuation vector (w) can generate a finite-horizon (\varepsilon)-equilibrium block (\sigma(w)) with positive absorption hazard, after which an approximate finite orbit of (f) is concatenated into one global strategy.
   **Key intermediate steps:** First, define partitions and cutoffs (c_i(D)) just above the uniform minmax values and prove a local block lemma in the full game: for every (w\in W), there is a block that is already an (\eta)-equilibrium of a (T(w))-stage game with terminal bonus (w), has controlled exit probability (\mu(w)>0), and yields a next continuation close to (f(w)). Second, prove an approximate finite-orbit theorem for the full continuation map, not just in the positive recursive absorbing subclass. Third, concatenate the blocks and attach public deviator-identification plus minmax punishments so the continuation vector forms an almost-supermartingale until absorption or detection. Fourth, turn that supermartingale control into finite-horizon average-payoff control, with the last partial block and all monitoring costs swallowed into the (\varepsilon) budget.
   **Likely failure point:** The hard seam is the local block lemma outside absorbing-like geometry. In the general game, punishments change transition structure, several recurrent classes may compete at once, and the continuation map may stop being tame enough to admit a finite-orbit argument. The other danger is that the route may deliver payoff-form invariance without yet yielding one uncorrelated profile that works for all large (T).
   **Complexity estimate:** Extreme, but modular. It is the most promising full-theorem route because the literature already has one engine for auxiliary payoffs and another for orbit concatenation; the missing bridge is brutal, but it is visible.

---
## OTHER AVAILABLE FILES (not loaded; request by name if needed)

- `branches/main/context/breakdown_amendments.md` (2736 chars)
- `branches/main/context/knowledge_ledger.md` (5851 chars)
- `branches/main/context/literature.md` (14733 chars)
- `branches/main/context/reviewer_01.md` (7305 chars)
- `branches/main/context/reviewer_02.md` (7305 chars)
- `branches/main/context/scope_decision.md` (52 chars)

