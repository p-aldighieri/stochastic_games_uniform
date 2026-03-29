# Section 4 — Flux Coordinate Repair (Pass 45, Prover)

**Pass**: 45
**Role**: Prover
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-28
**Thought time**: 25m 13s
**Status**: COMPLETE

## Contents

- Example 4.1 (Alternating boundary laws) — discontinuity example
- Proposition (No continuous extension of normalized exit law)
- Definition (Flux coordinates) — beta_C(e,b) = alpha_C(e) * q_C(e,b)
- Proposition (Basic identities)
- Theorem (Continuity in flux coordinates) — Cases alpha>0 and alpha=0
- Corollary (Continuity on relaxed tree space)
- Proposition (Continuity of payoff and deviation functionals)
- Closing argument: why Kakutani needs this repair

## LaTeX

```latex
\section{The Flux Coordinate Repair}\label{sec:flux-coordinate-repair}

The local witness attached to a phase-state \(\xi\) in a communicating class \(C\) carries, among other data, a projective exit-rate vector
\[
\alpha_C(\xi)=\big(\alpha_C(e;\xi)\big)_e
\]
and, for each exit coordinate \(e\), a normalized exit law
\[
q_C(e,\cdot;\xi)\in \Delta(\operatorname{Out}(C)).
\]
This normalization is convenient on the positive-exit stratum, but it is topologically wrong on the face where \(\alpha_C(e)=0\). When no mass exits through \(e\), the conditional law of that nonexistent exit is not an intrinsic datum. Thus \(q_C(e,\cdot)\) can oscillate while every genuine exit quantity converges. The cure is to replace the normalized law by the \emph{unnormalized} boundary flux.

We begin by isolating the defect.

\begin{example}[Alternating boundary laws]\label{ex:alternating-boundary-laws}
Fix a communicating class \(C\), an exit coordinate \(e\), and two distinct boundary states \(b_1,b_2\in \operatorname{Out}(C)\). For each \(n\ge 1\), let \(h_n\) be a witness whose non-exit coordinates agree with those of a fixed zero-exit witness \(h_\ast\), and such that
\[
\alpha_n:=\alpha_C(e;h_n)=\frac{1}{n},
\qquad
q_n:=q_C(e,\cdot;h_n)=
\begin{cases}
\delta_{b_1}, & n \text{ even},\\[2mm]
\delta_{b_2}, & n \text{ odd}.
\end{cases}
\]
Then \(\alpha_n\to 0\), but \(q_n\) does not converge in \(\Delta(\operatorname{Out}(C))\). Indeed,
\[
\|q_{2m}-q_{2m+1}\|_1
=
\|\delta_{b_1}-\delta_{b_2}\|_1
=
2
\qquad\text{for every }m\ge 1.
\]
So the normalized exit law keeps alternating, even though the total mass exiting through \(e\) vanishes.

Now form the actual boundary mass
\[
\beta_n(b):=\alpha_n q_n(b).
\]
Then
\[
\beta_n=
\begin{cases}
n^{-1}\delta_{b_1}, & n \text{ even},\\[2mm]
n^{-1}\delta_{b_2}, & n \text{ odd},
\end{cases}
\]
and therefore
\[
\|\beta_n\|_1=\alpha_n=\frac1n\longrightarrow 0.
\]
Thus the oscillation is an artifact of normalization: the physical exit mass converges to \(0\), while the conditional law of a nonexistent exit does not.
\end{example}

Example~\ref{ex:alternating-boundary-laws} shows that the zero-exit face cannot be parameterized continuously by the normalized law.

\begin{proposition}[No continuous extension of the normalized exit law]\label{prop:q-discontinuous}
Fix \(C\) and an exit coordinate \(e\). The coordinate
\[
q_C(e,\cdot)
\]
defined on the positive stratum \(\{\alpha_C(e)>0\}\) admits no continuous extension to the zero-exit face \(\{\alpha_C(e)=0\}\).
\end{proposition}

\begin{proof}
Suppose a continuous extension existed. Apply it to the witness sequence \(h_n\) from Example~\ref{ex:alternating-boundary-laws}. By construction, all non-\(q\) coordinates of \(h_n\) converge to the corresponding coordinates of the zero-exit witness \(h_\ast\), and \(\alpha_n\to 0\). Hence continuity would force
\[
q_n \longrightarrow q_C(e,\cdot;h_\ast).
\]

But along the even subsequence one has \(q_{2m}=\delta_{b_1}\), while along the odd subsequence one has \(q_{2m+1}=\delta_{b_2}\). These subsequences have different limits in \(\Delta(\operatorname{Out}(C))\). Therefore \(q_n\) does not converge, a contradiction.
\end{proof}

The obstruction is now clear. The old coordinate system remembers a direction after the mass in that direction has already disappeared.

\begin{definition}[Flux coordinates]\label{def:flux-coordinates}
For every phase-state \(\xi\), exit coordinate \(e\), and boundary state \(b\in \operatorname{Out}(C)\), define
\[
\beta_C(e,b;\xi):=
\alpha_C(e;\xi)\,q_C(e,b;\xi)
\]
whenever \(\alpha_C(e;\xi)>0\), and set
\[
\beta_C(e,b;\xi):=0
\]
when \(\alpha_C(e;\xi)=0\).
We call \(\beta_C(e,b;\xi)\) the \emph{boundary flux} from \(C\) through \(e\) to \(b\).
\end{definition}

The point of Definition~\ref{def:flux-coordinates} is that \(\beta_C(e,b)\) records the only exit datum that enters the recursion downstream: the actual mass that reaches boundary state \(b\).

\begin{proposition}[Basic identities]\label{prop:flux-identities}
For every phase-state \(\xi\), exit coordinate \(e\), and \(b\in \operatorname{Out}(C)\),
\[
\beta_C(e,b;\xi)\ge 0,
\qquad
\sum_{b\in \operatorname{Out}(C)} \beta_C(e,b;\xi)=\alpha_C(e;\xi),
\qquad
\|\beta_C(e,\cdot;\xi)\|_1=\alpha_C(e;\xi).
\]
Moreover, whenever \(\alpha_C(e;\xi)>0\),
\[
q_C(e,b;\xi)=\frac{\beta_C(e,b;\xi)}{\alpha_C(e;\xi)}.
\]
Hence on the positive stratum the change of coordinates \((\alpha_C,q_C)\mapsto \beta_C\) loses no information, while on the zero face it collapses the spurious oscillatory directions to a single point.
\end{proposition}

\begin{proof}
Nonnegativity is immediate from the definition. Since \(q_C(e,\cdot;\xi)\) is a probability vector whenever \(\alpha_C(e;\xi)>0\),
\[
\sum_{b\in \operatorname{Out}(C)} \beta_C(e,b;\xi)
=
\alpha_C(e;\xi)\sum_{b\in \operatorname{Out}(C)} q_C(e,b;\xi)
=
\alpha_C(e;\xi).
\]
Because the coordinates of \(\beta_C(e,\cdot;\xi)\) are nonnegative, the same identity gives
\[
\|\beta_C(e,\cdot;\xi)\|_1
=
\sum_{b\in \operatorname{Out}(C)} \beta_C(e,b;\xi)
=
\alpha_C(e;\xi).
\]
If \(\alpha_C(e;\xi)>0\), division by \(\alpha_C(e;\xi)\) recovers \(q_C(e,\cdot;\xi)\).
\end{proof}

In particular, \(\beta_C\) already contains \(\alpha_C\), since
\[
\alpha_C(e;\xi)=\sum_{b\in \operatorname{Out}(C)} \beta_C(e,b;\xi).
\]
So one may think of the flux vector as simultaneously encoding the exit rate and the boundary split, but without the singular normalization at zero.

Let \(\Xi_C\) denote the phase-state space attached to \(C\), and let \(U_C(\xi)\) collect all local witness coordinates other than the normalized exit laws. By the construction from the previous section, the coordinates in \(U_C\) are already continuous. The only defective coordinates are the \(q_C(e,\cdot)\). We therefore define the repaired local witness map by
\[
\mathcal W_C^\beta(\xi):=\big(U_C(\xi),\beta_C(\xi)\big).
\]

\begin{theorem}[Continuity in flux coordinates]\label{thm:flux-continuity}
The repaired witness map \(\mathcal W_C^\beta\) is continuous on all of \(\Xi_C\). More precisely, for each exit coordinate \(e\),
\[
\xi_n\to \xi
\quad\Longrightarrow\quad
\beta_C(e,\cdot;\xi_n)\to \beta_C(e,\cdot;\xi)
\quad\text{in }\ell^1\big(\operatorname{Out}(C)\big).
\]
\end{theorem}

\begin{proof}
Fix an exit coordinate \(e\), and let \(\xi_n\to \xi\) in \(\Xi_C\). Write
\[
\alpha_n:=\alpha_C(e;\xi_n),
\qquad
\alpha:=\alpha_C(e;\xi),
\]
and
\[
\beta_n:=\beta_C(e,\cdot;\xi_n),
\qquad
\beta:=\beta_C(e,\cdot;\xi).
\]
We prove \(\beta_n\to \beta\) in \(\ell^1\big(\operatorname{Out}(C)\big)\).

\smallskip

\noindent\emph{Case 1: \(\alpha>0\).}
Since \(\alpha_C(e;\cdot)\) is continuous, \(\alpha_n\to\alpha>0\), so \(\alpha_n>0\) for all sufficiently large \(n\). On that tail, the normalized laws \(q_C(e,\cdot;\xi_n)\) are defined and vary continuously on the positive stratum. Set
\[
q_n:=q_C(e,\cdot;\xi_n),
\qquad
q:=q_C(e,\cdot;\xi).
\]
Then \(q_n\to q\) in \(\ell^1\big(\operatorname{Out}(C)\big)\). Hence
\[
\beta_n-\beta
=
\alpha_n q_n-\alpha q
=
(\alpha_n-\alpha)q_n+\alpha(q_n-q),
\]
so
\[
\|\beta_n-\beta\|_1
\le
|\alpha_n-\alpha|\,\|q_n\|_1+\alpha\,\|q_n-q\|_1
=
|\alpha_n-\alpha|+\alpha\,\|q_n-q\|_1
\longrightarrow 0.
\]

\smallskip

\noindent\emph{Case 2: \(\alpha=0\).}
Here the normalized laws may oscillate arbitrarily, but the flux vector ignores that spurious motion. By Proposition~\ref{prop:flux-identities},
\[
\|\beta_n\|_1=\alpha_n\longrightarrow \alpha=0.
\]
Therefore \(\beta_n\to 0\) in \(\ell^1\big(\operatorname{Out}(C)\big)\). By Definition~\ref{def:flux-coordinates}, \(\beta=0\) when \(\alpha=0\). Thus \(\beta_n\to \beta\).

This proves continuity of the \(e\)-th flux vector. Since the local witness has only finitely many exit coordinates, the full vector \(\beta_C(\xi)\) depends continuously on \(\xi\). Together with the already continuous coordinates \(U_C(\xi)\), this proves continuity of \(\mathcal W_C^\beta\).
\end{proof}

The whole repair is encapsulated in the estimate
\[
\|\beta_n\|_1=\alpha_n\to 0.
\]
No matter how violently \(q_n\) oscillates near the zero-exit face, that oscillation is multiplied by vanishing mass and disappears in the flux coordinates.

The same argument passes immediately from local witnesses to the assembled tree object.

\begin{corollary}[Continuity on the relaxed tree space]\label{cor:tree-continuity}
After replacing every normalized exit-law coordinate \(q_C(e,\cdot)\) by the corresponding boundary flux \(\beta_C(e,\cdot)\), the global witness map into the relaxed tree space is continuous.
\end{corollary}

\begin{proof}
The global relaxed tree map is assembled coordinatewise from the local witness maps at its nodes. By Theorem~\ref{thm:flux-continuity}, each local repaired coordinate is continuous. Therefore the assembled map is continuous in the product topology.
\end{proof}

We now explain why this repair matters for the paper. The downstream recursion never uses \(q_C(e,\cdot)\) by itself. It uses only the actual amount of boundary mass that reaches each successor state. If \(V_i(b)\) denotes player \(i\)'s continuation value at boundary state \(b\), then the exit contribution from \(C\) has the form
\[
\sum_e \sum_{b\in \operatorname{Out}(C)} \beta_C(e,b)\,V_i(b).
\]
Similarly, the value of a unilateral deviation in \(C\) is a local payoff term plus a finite sum of continuation values weighted by the deviation fluxes.

\begin{proposition}[Continuity of payoff and deviation functionals]\label{prop:downstream-continuity}
On the repaired relaxed tree space, every payoff functional and every unilateral deviation value functional generated by the backward recursion is continuous.
\end{proposition}

\begin{proof}
We argue recursively down the tree.

At a leaf, the continuation value is part of the leaf data and is therefore continuous by definition.

Now consider an internal node \(C\). Let \(R_C^i(\xi)\) denote the local in-class contribution to player \(i\)'s value. By construction, \(R_C^i\) is continuous in the non-exit witness coordinates. The full continuation value at \(C\) is
\[
V_C^i(\xi)
=
R_C^i(\xi)
+
\sum_e\sum_{b\in \operatorname{Out}(C)} \beta_C(e,b;\xi)\,V_b^i(\xi),
\]
where \(V_b^i\) is the continuation value attached to the subtree rooted at boundary state \(b\). By the recursive hypothesis, each \(V_b^i\) is continuous. By Theorem~\ref{thm:flux-continuity}, each flux coordinate \(\beta_C(e,b;\xi)\) is continuous. Hence \(V_C^i\) is a finite sum of products of continuous functions and is therefore continuous.

The same proof applies to a unilateral deviation by player \(i\). If
\[
D_{C,i}(\xi)
=
R_{C,i}^{\mathrm{dev}}(\xi)
+
\sum_e\sum_{b\in \operatorname{Out}(C)} \beta_{C,i}^{\mathrm{dev}}(e,b;\xi)\,V_b^i(\xi),
\]
where \(R_{C,i}^{\mathrm{dev}}\) is the local deviating payoff term and \(\beta_{C,i}^{\mathrm{dev}}\) is the induced deviation flux, then the same continuity argument shows that \(D_{C,i}\) is continuous.
\end{proof}

Proposition~\ref{prop:downstream-continuity} is exactly what the fixed-point argument needs. In the raw coordinates, sequences such as Example~\ref{ex:alternating-boundary-laws} create fake boundary directions on the zero-exit faces: the asymptotic behavior stabilizes, but the witness itself fails to converge because the conditional law of a nonexistent exit keeps alternating. In the repaired coordinates, those directions collapse to the single, correct point \(\beta_C(e,\cdot)=0\). The relaxed tree space therefore carries the topology seen by the payoff formulas themselves.

This is the topological role of the repair in the paper. The Kakutani correspondence in the next section is built from feasible witness constraints together with best-response inequalities. Once the exit data are recorded by \(\beta\), the evaluation maps appearing in those constraints are continuous by Proposition~\ref{prop:downstream-continuity}. Those are the continuity inputs needed to verify closed graph and upper hemicontinuity for the fixed-point correspondence on the compact relaxed tree space. Thus the flux coordinate repair is not merely cosmetic. It removes the only artificial discontinuity coming from zero exit rate and turns the relaxed tree compactification into a legitimate domain for Kakutani.
```
