# Section 5.2: Boundary-Flux Witness — Full Proof (Pass 43)
**Source**: ChatGPT Extended Pro
**Date**: 2026-03-28
**Length**: 6,374 characters

Below is a LaTeX-ready proof. prover_section5_2

\begin{proof}
Fix a node $C$ with $\Out(C)\neq\varnothing$. For each boundary label $b\in\Out(C)$, adjoin a cemetery phase-state $\partial_b$ and a dummy action $\dagger_b$, and set

$$
\hat\Xi_C:=\Xi_C\sqcup\{\partial_b:b\in\Out(C)\},
\qquad
\hat\Omega_C:=\Omega_C\sqcup\{(\partial_b,\dagger_b):b\in\Out(C)\}.
$$

The augmented transition kernel $\hat P_C$ is obtained by keeping the original phase dynamics on transitions that remain inside $C$, redirecting every one-step exit through boundary $b$ to the cemetery state $\partial_b$, and making each cemetery state absorbing:

$$
\hat P_C(\partial_b\mid \partial_b,\dagger_b)=1.
$$

Thus exits are encoded as ordinary terminal coordinates of a finite controlled Markov system.

Let $B_C$ be the usual flow matrix of this augmented system, and let $r_C$ be the corresponding source/normalization vector. Define

$$
\mathcal P_C
:=
\Bigl\{
m\in\mathbb R_+^{\hat\Omega_C}
:
B_Cm=r_C,\ \langle \mathbf 1,m\rangle=1
\Bigr\}.
$$

This is the standard occupation-measure polytope on $\hat\Xi_C$. Because $\hat\Omega_C$ is finite and $m\ge 0$ with $\langle \mathbf 1,m\rangle=1$, one has $\mathcal P_C\subset[0,1]^{\hat\Omega_C}$; hence $\mathcal P_C$ is a bounded polyhedron, therefore a compact convex polytope. By the deterministic realization result from \S5.1 applied to the augmented finite system, there is a finite catalogue $\Theta_C^{\det}$ of deterministic stationary joint policies such that

$$
\operatorname{ext}(\mathcal P_C)=\{m_\theta:\theta\in\Theta_C^{\det}\},
\qquad
\mathcal P_C=\conv\{m_\theta:\theta\in\Theta_C^{\det}\}.
$$

We now verify that

$$
\mathcal L_C:m\longmapsto(\mu_C,\beta_C,J_C^{\mathrm{lin}})
$$

is affine. The $\mu_C$-component is just the fixed projection of $m$ onto the interior occupation coordinates of $C$, so it is linear. For each exit label pair $(e,b)$, let $\lambda_{e,b}(\xi,a)$ denote the fixed coefficient that records the amount of one-step mass from $(\xi,a)$ sent through the $e$-channel to the cemetery state $\partial_b$. Then

$$
\beta_C(e,b)=\sum_{(\xi,a)\in\hat\Omega_C}\lambda_{e,b}(\xi,a)\,m(\xi,a),
$$

so $m\mapsto \beta_C$ is linear. In particular,

$$
\alpha_C(e)=\sum_b \beta_C(e,b)
$$

is linear as well. This is precisely why the proof uses flux coordinates $\beta_C(e,b)=\alpha_C(e)q_C(e,b)$: the map $m\mapsto \beta_C$ extends affinely to all of $\mathcal P_C$, including faces where $\alpha_C(e)=0$. By contrast, the normalized exit share

$$
q_C(e,b)=\frac{\beta_C(e,b)}{\alpha_C(e)}
$$

would introduce a division by $\alpha_C(e)$, and would therefore fail to be affine, or even continuous, on the faces where that denominator vanishes. Finally, each coordinate of the linearized exit jet is, by definition of the fixed linearization at $C$, an affine functional of the occupation vector:

$$
J_{C,r}^{\mathrm{lin}}(m)
=
c_{C,r}
+
\sum_{(\xi,a)\in\hat\Omega_C}\kappa_{C,r}(\xi,a)\,m(\xi,a).
$$

Hence $\mathcal L_C$ has the form

$$
\mathcal L_C(m)=A_Cm+a_C,
$$

and is affine on $\mathcal P_C$.

Set

$$
V_C:=\{m_\theta:\theta\in\Theta_C^{\det}\}.
$$

Since $\mathcal P_C=\conv(V_C)$ and $\mathcal L_C$ is affine,

$$
\mathcal F_C^{\mathrm{lin}}
=
\mathcal L_C(\mathcal P_C)
=
\mathcal L_C(\conv V_C)
=
\conv\bigl(\mathcal L_C(V_C)\bigr).
$$

The identity $\mathcal L_C(\conv V_C)=\conv(\mathcal L_C(V_C))$ is simply preservation of convex combinations under affine maps: if $m=\sum_{k=1}^K h_kv_k$ with $h\in\Delta_K$ and $v_k\in V_C$, then

$$
\mathcal L_C(m)=\sum_{k=1}^K h_k\,\mathcal L_C(v_k),
$$

which gives the inclusion $\mathcal L_C(\conv V_C)\subseteq \conv(\mathcal L_C(V_C))$; the reverse inclusion follows because every convex combination on the right is the image of the same convex combination on the left. Therefore

$$
\mathcal F_C^{\mathrm{lin}}
=
\conv\{\mathcal L_C(m_\theta):\theta\in\Theta_C^{\det}\}.
$$

This proves item $2$. Since the right-hand side is the convex hull of finitely many points, $\mathcal F_C^{\mathrm{lin}}$ is itself a compact convex polytope, which proves item $1$.

For item $3$, fix any feasible target

$$
y=(\mu_C,\beta_C,J_C^{\mathrm{lin}})\in\mathcal F_C^{\mathrm{lin}},
$$

and let

$$
d:=\dim(\mathcal F_C^{\mathrm{lin}})
$$

denote the affine dimension of the feasible flux set. By the representation above,

$$
y\in
\conv\{\mathcal L_C(m_\theta):\theta\in\Theta_C^{\det}\}.
$$

Caratheodory's theorem, applied in the affine hull of $\mathcal F_C^{\mathrm{lin}}$, yields deterministic stationary policies $\theta_1,\dots,\theta_K\in\Theta_C^{\det}$ and weights $h=(h_1,\dots,h_K)\in\Delta_K$ with

$$
K\le d+1
$$

such that

$$
y=\sum_{k=1}^K h_k\,\mathcal L_C(m_{\theta_k}).
$$

Unpacking $y$ gives

$$
(\mu_C,\beta_C,J_C^{\mathrm{lin}})
=
\sum_{k=1}^K h_k\,\mathcal L_C(m_{\theta_k}),
$$

which is exactly the claimed finite witness decomposition.

Thus $\mathcal F_C^{\mathrm{lin}}$ is a compact convex polytope, it is the convex hull of the finitely many deterministic stationary boundary-flux witnesses, and every feasible target admits a witness decomposition using at most $\dim(\mathcal F_C^{\mathrm{lin}})+1$ such witnesses.
\end{proof}
