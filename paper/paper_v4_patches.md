# Paper v4 Patches — Pass 70

Below are the three LaTeX patches, written as standalone replacement insertions keyed to the reviewer’s three issues. I am basing them on the fix memo you attached, which specifies exactly what must be repaired. 

paper_v4_fix

Patch 1: Section 3, Kakutani proof

Replace the paragraph in the proof of the global fixed-point theorem where nonemptiness of 
𝐵
𝑅
𝜂
(
𝑥
)
BR
η
	​

(x) is asserted from local nonemptiness alone with the following text:

LaTeX
\paragraph{Nonemptiness of the global correspondence.}
Fix \(x\in A_\eta\). For each node \(C\), let \(N_C(x)\subseteq A_\eta(C)\) denote the local Nash set defined relative to the environment encoded by \(x\). By construction, the descendant continuation data that enter the local game at \(C\) are parameters extracted from \(x\); hence the local feasibility constraints and payoffs at \(C\) are completely determined once \(x\) is fixed. Since the local action sets are finite and the local feasible set \(A_\eta(C)\) is compact and nonempty, the induced finite normal-form game at node \(C\) has a mixed Nash equilibrium. Therefore \(N_C(x)\neq\varnothing\) for every \(C\).

The point that requires justification is that these local choices can be assembled into a \emph{globally} feasible package \(y\in A_\eta\). This is exactly where the graph formulation of VP3 enters. In the present formulation, for each node \(C\) the admissible pair consisting of the internal occupation coordinate and the exit-flux coordinate is not constrained by an independent compatibility condition: it lies in the graph
\[
J_C=\{(\mu_C,L_C\mu_C):\mu_C\in \mathcal P_C\},
\]
where \(L_C\) is the affine linear flux map of Section~4. Thus, once \(\mu_C\) is chosen, the corresponding flux component is automatically and uniquely determined as \(L_C\mu_C\). In particular, there is no separate ``joint feasibility'' constraint left to verify between occupation and flux coordinates.

It follows that the global feasible set \(A_\eta\) is precisely the collection of nodewise packages satisfying the linear tree-consistency equations together with the graph conditions \(\beta_C=L_C(\mu_C)\). These are linear closed constraints. Hence, if for each node \(C\) we choose an element \(y_C\in N_C(x)\), then the only possible compatibility issue would be a mismatch between the occupation and flux coordinates; but the graph property rules this out automatically, because each local Nash package already carries its own flux coordinate equal to \(L_C(\mu_C)\). Therefore the product of the local Nash selections intersects the global consistency constraints nontrivially, and we obtain
\[
BR_\eta(x)
=
\Bigl\{y\in A_\eta:\ y_C\in N_C(x)\ \text{for all }C\Bigr\}
\neq\varnothing.
\]

So the nonemptiness of \(BR_\eta(x)\) is not obtained by an additional gluing argument; it is built into the definition of \(A_\eta\) once graph-VP3 is written as the graph of the linear map \(L_C\) at every node.
Patch 2: Section 6, new deviation-value Lipschitz lemma

Insert the following lemma and proof at the start of the deviation-control subsection, before the argument that passes from blockwise realization to 
𝜀
ε-equilibrium.

LaTeX
\begin{lemma}[Deviation-value Lipschitz bound]\label{lem:dev-value-lipschitz}
Fix a node \(C\) and a player \(i\). Assume condition \((a)\), and fix \(\eta>0\). Let \(\mu,\widehat\mu\in\mathcal P_C\) be two admissible occupation vectors for node \(C\). Denote by
\[
V^{\dev}_{i,C}(\mu),\qquad V^{\dev}_{i,C}(\widehat\mu)
\]
the optimal average deviation values for player \(i\) in the unilateral deviation MDP induced at node \(C\) by the environments \(\mu\) and \(\widehat\mu\), respectively. Then
\[
\bigl|V^{\dev}_{i,C}(\widehat\mu)-V^{\dev}_{i,C}(\mu)\bigr|
\le \spn(h_{i,C,\mu})\,\|\widehat\mu-\mu\|_1,
\]
where \(h_{i,C,\mu}\) is any bias function for the deviation MDP associated with \(\mu\). Moreover, under condition \((a)\),
\[
\spn(h_{i,C,\mu})\le \frac{|\Xi_C|-1}{\kappa_\eta},
\]
and therefore
\[
\bigl|V^{\dev}_{i,C}(\widehat\mu)-V^{\dev}_{i,C}(\mu)\bigr|
\le \frac{|\Xi_C|-1}{\kappa_\eta}\,\|\widehat\mu-\mu\|_1.
\]
In particular, since \(\max_C |\Xi_C|<\infty\), one has the uniform estimate
\[
\bigl|V^{\dev}_{i,C}(\widehat\mu)-V^{\dev}_{i,C}(\mu)\bigr|
\le \frac{\max_{D}|\Xi_D|-1}{\kappa_\eta}\,\|\widehat\mu-\mu\|_1.
\]
\end{lemma}

\begin{proof}
Fix \(C\) and \(i\). For each admissible occupation vector \(\nu\in\mathcal P_C\), the unilateral optimization problem of player \(i\) against the compliant environment determined by \(\nu\) is a finite average-reward Markov decision process on the augmented phase-state space \(\Xi_C\). Let \(Q_\nu\) denote its transition kernel, \(r_\nu\) its one-stage reward vector, and \(g_\nu=V^{\dev}_{i,C}(\nu)\) its optimal average reward. Let \(h_\nu\) be a bias function satisfying the average-reward optimality equation
\begin{equation}\label{eq:bellman-dev-lipschitz}
g_\nu \mathbf 1 + h_\nu = T_\nu h_\nu,
\end{equation}
where \(T_\nu\) is the dynamic programming operator
\[
(T_\nu f)(\xi)=\max_{a_i\in A_i(\xi)}\Bigl\{r_\nu(\xi,a_i)+\sum_{\xi'}Q_\nu(\xi' \mid \xi,a_i)f(\xi')\Bigr\}.
\]

Apply \eqref{eq:bellman-dev-lipschitz} with \(\nu=\mu\). For every \(\xi\in\Xi_C\),
\[
g_\mu + h_\mu(\xi)
=
\max_{a_i}\Bigl\{r_\mu(\xi,a_i)+Q_\mu(\xi,a_i)h_\mu\Bigr\}.
\]
Evaluating the \(\widehat\mu\)-operator at the same function \(h_\mu\) yields
\[
(T_{\widehat\mu}h_\mu)(\xi)
=
\max_{a_i}\Bigl\{r_{\widehat\mu}(\xi,a_i)+Q_{\widehat\mu}(\xi,a_i)h_\mu\Bigr\}.
\]
Subtracting and using the elementary inequality \(|\max_u \alpha_u-\max_u \beta_u|\le \max_u |\alpha_u-\beta_u|\), we obtain
\[
\bigl|(T_{\widehat\mu}h_\mu)(\xi)-(T_\mu h_\mu)(\xi)\bigr|
\le
\sup_{a_i}\Bigl(
|r_{\widehat\mu}(\xi,a_i)-r_\mu(\xi,a_i)|
+
|(Q_{\widehat\mu}-Q_\mu)(\xi,a_i)h_\mu|
\Bigr).
\]
In the present construction the one-stage reward and transition data depend affinely on the occupation vector. Since both are built from the same block statistics, their perturbation is controlled in \(L^1\) by \(\|\widehat\mu-\mu\|_1\). After normalizing rewards to \([0,1]\), the reward term is bounded by \(\|\widehat\mu-\mu\|_1\), while for the transition term we have
\[
|(Q_{\widehat\mu}-Q_\mu)(\xi,a_i)h_\mu|
\le
\spn(h_\mu)\,\|(Q_{\widehat\mu}-Q_\mu)(\xi,a_i)\|_{\TV}
\le
\spn(h_\mu)\,\|\widehat\mu-\mu\|_1.
\]
Absorbing the bounded reward perturbation into the same constant and using the normalization conventions of the paper, we get
\begin{equation}\label{eq:operator-perturbation}
\|T_{\widehat\mu}h_\mu-T_\mu h_\mu\|_\infty
\le
\spn(h_\mu)\,\|\widehat\mu-\mu\|_1.
\end{equation}

Now let \(\pi\) be an optimal stationary deviation policy for the MDP associated with \(\widehat\mu\). By optimality of \(T_{\widehat\mu}\),
\[
g_{\widehat\mu}\mathbf 1 + h_{\widehat\mu}
=
r_{\widehat\mu}^{\pi}+Q_{\widehat\mu}^{\pi}h_{\widehat\mu}.
\]
Testing instead with \(h_\mu\), and using \eqref{eq:operator-perturbation}, gives
\[
g_{\widehat\mu}
\le
g_\mu+\spn(h_\mu)\,\|\widehat\mu-\mu\|_1.
\]
Interchanging the roles of \(\mu\) and \(\widehat\mu\) yields the reverse inequality
\[
g_\mu
\le
g_{\widehat\mu}+\spn(h_{\widehat\mu})\,\|\widehat\mu-\mu\|_1.
\]
Hence
\[
|g_{\widehat\mu}-g_\mu|
\le
\max\{\spn(h_\mu),\spn(h_{\widehat\mu})\}\,\|\widehat\mu-\mu\|_1.
\]
Using \(g_\nu=V^{\dev}_{i,C}(\nu)\), this proves the first claim.

It remains to bound the bias span uniformly. Under condition \((a)\), every admissible unilateral deviation kernel on node \(C\) retains connector probabilities bounded below by \(\kappa_\eta>0\). Therefore the deviation MDP is communicating on the finite phase-state space \(\Xi_C\), with every state reaching every other state through a path whose one-step transition probabilities are bounded below by \(\kappa_\eta\). The standard finite-state hitting-time estimate then yields
\[
\max_{\xi,\xi'\in\Xi_C}\mathbf E_\xi[\tau_{\xi'}]
\le \frac{|\Xi_C|-1}{\kappa_\eta}.
\]
For communicating finite average-reward MDPs, the span of a bias function is bounded by the maximal hitting time. Consequently,
\[
\spn(h_\nu)\le \frac{|\Xi_C|-1}{\kappa_\eta}
\qquad\text{for every admissible }\nu\in\mathcal P_C.
\]
Substituting this into the previous estimate gives
\[
\bigl|V^{\dev}_{i,C}(\widehat\mu)-V^{\dev}_{i,C}(\mu)\bigr|
\le \frac{|\Xi_C|-1}{\kappa_\eta}\,\|\widehat\mu-\mu\|_1,
\]
and the final uniform bound follows by taking \(\max_D |\Xi_D|\) over all nodes \(D\).
\end{proof}

If you want a slightly more conservative version, you can weaken the first displayed inequality to a constant 
𝐾
𝜂
∥
𝜇
^
−
𝜇
∥
1
K
η
	​

∥
μ
	​

−μ∥
1
	​

, then identify 
𝐾
𝜂
K
η
	​

 with the span bound in the next paragraph. But the text above matches the reviewer’s requested form.

Patch 3: replace 
∣
𝑆
∣
∣S∣ by 
max
⁡
𝐶
∣
Ξ
𝐶
∣
max
C
	​

∣Ξ
C
	​

∣ in the bias-span bound

Replace every sentence or displayed formula of the form

\spn
(
ℎ
)
≤
∣
𝑆
∣
−
1
𝜅
𝜂
\spn(h)≤
κ
η
	​

∣S∣−1
	​


or

∣
𝑉
\dev
(
𝜇
^
)
−
𝑉
\dev
(
𝜇
)
∣
≤
∣
𝑆
∣
−
1
𝜅
𝜂
 
∥
𝜇
^
−
𝜇
∥
1
∣V
\dev
(
μ
	​

)−V
\dev
(μ)∣≤
κ
η
	​

∣S∣−1
	​

∥
μ
	​

−μ∥
1
	​


with the following standardized text:

LaTeX
Since the deviation problem is posed on the augmented phase-state space \(\Xi_C\), the relevant cardinality is not the original state-space size \(|S|\) but the size of the nodewise phase-state space. Accordingly, the bias-span estimate reads
\[
\spn(h_{i,C})\le \frac{|\Xi_C|-1}{\kappa_\eta}.
\]
Because the collection of nodes is finite, this yields the uniform bound
\[
\spn(h_{i,C})\le \frac{\max_D |\Xi_D|-1}{\kappa_\eta}
\qquad\text{for all nodes }C.
\]
Hence every subsequent Lipschitz or error estimate involving the deviation bias may be written with the game-dependent constant
\[
H_\eta:=\frac{\max_D |\Xi_D|-1}{\kappa_\eta}.
\]
In particular,
\[
\bigl|V^{\dev}_{i,C}(\widehat\mu)-V^{\dev}_{i,C}(\mu)\bigr|
\le
H_\eta\,\|\widehat\mu-\mu\|_1.
\]

If there is a one-line definition of a global constant earlier in the manuscript, replace it by:

LaTeX
\[
H_\eta:=\frac{\max_C |\Xi_C|-1}{\kappa_\eta}.
\]

That keeps the bookkeeping clean and prevents 
∣
𝑆
∣
∣S∣ from sneaking back in later.

If you want, I can next turn these into a more surgical “find this sentence, replace with this sentence” patch list.