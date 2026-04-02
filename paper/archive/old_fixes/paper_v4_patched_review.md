# Patched v4 Review — Pass 71

Non-EP review (1m 38s)

Verdict: FAIL

I do not think Theorem A has a complete proof yet in the patched v4 manuscript neyman_route_d_prime_v4_patched.tex.

The three requested fixes do improve real weaknesses:

the 
∣
𝑆
∣
∣S∣ to 
max
⁡
𝐷
∣
Ξ
𝐷
∣
max
D
	​

∣Ξ
D
	​

∣ repair is the right correction,

the new graph-VP3 discussion clarifies the occupation/flux issue,

the new deviation-value Lipschitz lemma is the right kind of ingredient.

But two load-bearing gaps remain.

First, the Kakutani nonemptiness step is still not fully proved. The argument now says that graph-VP3 makes global feasibility automatic once one picks local Nash packages nodewise. That only resolves the occupation/flux compatibility 
𝛽
𝐶
=
𝐿
𝐶
𝜇
𝐶
β
C
	​

=L
C
	​

μ
C
	​

. It does not resolve the inter-node continuation consistency built into 
𝐴
𝜂
A
η
	​

, namely the parent-child constraints relating 
𝑣
𝐶
(
𝑏
)
v
C
	​

(b) to 
𝑔
𝐷
g
D
	​

. In the definition of 
𝑁
~
𝐶
(
𝑥
)
N
C
	​

(x), the continuation values at node 
𝐶
C are pinned to the environment encoded by 
𝑥
x, while membership in 
BR
⁡
𝜂
(
𝑥
)
BR
η
	​

(x) requires a single 
𝑦
∈
𝐴
𝜂
y∈A
η
	​

 whose child gains are those of 
𝑦
y. So the proof still jumps from “each node has a local Nash package relative to 
𝑥
x” to “there exists a globally consistent 
𝑦
y” without proving that the chosen local packages fit together across parent-child links. Graph-VP3 fixes the old internal/exit mismatch, but it does not by itself solve this global assembly problem.

Second, the new blockwise Bellman certificate still contains an unjustified inference. The Lipschitz lemma bounds only the scalar deviation value

∣
𝑉
d
e
v
(
𝜇
^
)
−
𝑉
d
e
v
(
𝜇
)
∣
≤
𝐻
𝜂
∥
𝜇
^
−
𝜇
∥
1
.
∣V
dev
(
μ
	​

)−V
dev
(μ)∣≤H
η
	​

∥
μ
	​

−μ∥
1
	​

.

But in the proof of the blockwise Bellman lemma, this is used to conclude, in effect, that the actual deviating block’s reward and transition coefficients are each within 
𝑂
(
𝛿
)
O(δ) of the target coefficients, and therefore the one-step Bellman inequality with 
ℎ
𝑖
,
𝐶
∗
h
i,C
∗
	​

 holds up to 
𝐶
𝜂
𝛿
C
η
	​

δ. That inference does not follow from value closeness alone. A small perturbation in optimal value does not automatically imply pointwise closeness of the Bellman operator, or closeness of the realized deviating kernel 
𝑄
Q and reward vector 
𝑟
r, or validity of the same certificate 
ℎ
𝑖
,
𝐶
∗
h
i,C
∗
	​

 for the perturbed block. What is still needed is a direct lemma of one of these forms:

continuity of the Bellman operator 
𝑇
𝜇
T
μ
	​

 in 
𝜇
μ strong enough to transfer the certificate,

or a direct perturbation bound on 
(
𝑟
𝜇
,
𝑄
𝜇
)
(r
μ
	​

,Q
μ
	​

),

or a direct blockwise comparison argument that bypasses coefficientwise control.

Without that bridge, the telescoping estimate that drives the final regret bound is not established.

So the paper is closer, but not closed. The right verdict is FAIL, not CONDITIONAL, because the remaining issues are not cosmetic or local bookkeeping. They sit exactly at the two structural hinges of the proof:

existence of a global relaxed fixed point,

transfer from realized block occupations to deviation control.

The shortest diagnosis is: graph-VP3 solved the old occupation/flux compatibility problem, but not the global parent-child consistency problem; and the new deviation-value Lipschitz lemma solved value continuity, but not Bellman-certificate transport.