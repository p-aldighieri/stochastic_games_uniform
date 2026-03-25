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
