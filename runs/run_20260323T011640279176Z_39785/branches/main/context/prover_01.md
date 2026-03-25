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
