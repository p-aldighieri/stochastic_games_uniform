# Prover Output

Generated: 2026-03-26T01:55:00.000000+00:00

I do not have a proof of Strong L4* under the present hypotheses. What I can give is a sharp obstruction: the current one-step formulation is false for a legitimate exposed-face choice W*. I will stay entirely at L4*, as requested, and leave the already-verified tail untouched.

[DERIVED] **Singleton-face obstruction.**
Fix a history h. Suppose there is a vector w such that

b(h) = w^s = w and W*(h+) = {w} for every child h+ in C(h).

Then every feasible triple (x, beta, eta) in F_s*(h, w) satisfies beta(h+) = w for all children, so the continuation term is constant and cancels the current bias:

E[beta_i(H') | h] - b_i = w_i - w_i = 0.

Hence the local constraints reduce to

u_i(x) >= w_i - eta,   u_i(a_i', x_{-i}) <= w_i + eta   (for all i, for all a_i').

Therefore

max_{a_i'} u_i(a_i', x_{-i}) - u_i(x) <= 2*eta,

so x is a 2*eta-approximate mixed Nash equilibrium of the one-shot stage game at s(h), and its payoff vector lies within eta of w.

Consequently, if w is not a mixed Nash payoff of that stage game, then

inf{eta : exists (x, beta) with (x, beta, eta) in F_s*(h, w)} > 0.

**Proof.** If there were eta_n -> 0 with feasible x_n, compactness of the product simplex gives a convergent subsequence x_n -> x*. Passing to the limit in the inequalities yields that x* is a mixed Nash equilibrium and u(x*) = w, contradiction.

So the architecture has a very specific failure mode: if the exposed face W*(h+) is too thin, the selector loses all punitive continuation freedom and collapses to an approximate Nash problem in the raw stage game.

[ASSUMPTION+] **Concrete counterexample.**
Take the one-state, deterministic self-loop, two-player repeated Prisoner's Dilemma with actions C, D and stage payoffs

|     | C         | D       |
|-----|-----------|---------|
| C   | (3/4,3/4) | (0,1)   |
| D   | (1,0)     | (1/4,1/4)|

at the unique state s.

Let W(h) be the imported set of uniformly achievable individually rational payoffs from history h. Because the state never changes, W(h) = W for all h. The payoff

w := (3/4, 3/4)

belongs to W since "play C forever" achieves it exactly. Also every achievable payoff v in W satisfies

v_1 + v_2 <= 3/2,

because every stage payoff sum is at most 3/2, with equality only at (C,C). Hence the sum-maximizing face is the singleton {w}.

So if the deterministic tie-break used in L2 exposes the sum-maximizing face, then

W*(h) = {w} for every history h.

This is a legitimate exposed-face choice under the current setup.

[DERIVED] **Exact leakage floor in that game.**
At every node h, the current bias is forced to be b(h) = w, and every child continuation is forced to be beta(h+) = w. Write

p := x_1(C),  q := x_2(C).

Then the local feasibility conditions become

u_1(x) >= 3/4 - eta,  u_2(x) >= 3/4 - eta,
u_1(D, x_2) <= 3/4 + eta,  u_2(x_1, D) <= 3/4 + eta.

A direct computation gives

u_1(x) = 1/4 + 3q/4 - p/4,  u_2(x) = 1/4 + 3p/4 - q/4,
u_1(D, x_2) = 1/4 + 3q/4,  u_2(x_1, D) = 1/4 + 3p/4.

So feasibility implies

3q - p >= 2 - 4*eta,  3p - q >= 2 - 4*eta,
q <= 2/3 + 4*eta/3,  p <= 2/3 + 4*eta/3.

Summing the first two inequalities yields

p + q >= 2 - 4*eta,

while summing the last two yields

p + q <= 4/3 + 8*eta/3.

Therefore

2 - 4*eta <= 4/3 + 8*eta/3,

hence

**eta >= 1/10.**

This bound is sharp: p = q = 4/5 attains eta = 1/10.

So in this explicit finite stochastic game, every local selector at every history has leakage at least 1/10.

[GAP] **Conclusion.**
The present Strong L4* is false under the currently stated hypotheses. In the counterexample above, every nonroot depth t has the same local problem and the same lower bound

r_t >= 1/10.

Hence

sum_{t>=1} r_t = infinity,

so no depth-summable leakage budget exists.

This does not refute the main theorem target of uniform epsilon-equilibrium existence in finite stochastic games. It refutes the current one-step fixed-promise selector with continuations restricted to W*(h+). The bottleneck is real, exactly where the route memo says it is, but the obstruction is more precise than "uncorrelatedness is hard": the exposed face can contain the promise point while excluding the punitive continuation points needed to finance incentive control.

[SCOPE] **Most promising workaround.**
If you want to preserve the W*-endpoint architecture, the right repair is not another one-step selector. It is a **block selector**.

A concrete replacement is:

For each depth t, choose a block length L_t and an error r_t with sum_t r_t <= epsilon/8. At each node h, choose an L_t-stage public-history block policy pi_h and terminal continuation values beta_h(z) in W*(z) for each block-end child z, such that

(1/L_t)(E_{pi_h}[sum_{l=0}^{L_t - 1} u_i(H_l, A_l) | h] + E[beta_{h,i}(Z) | h] - b_i(h)) >= w_i^s - r_t,

and for every unilateral deviation tau_i inside the block,

(1/L_t)(E_{(tau_i, pi_{h,-i})}[sum_{l=0}^{L_t - 1} u_i(H_l, A_l) | h] + E[beta_{h,i}(Z) | h] - b_i(h)) <= w_i^s + r_t.

**Why this is the right repair:** in the Prisoner's Dilemma obstruction above, keep the terminal continuation fixed at beta_h = w, but inside an L-stage block play "C unless a deviation is observed, then D for the rest of the block." On path, the block payoff is exactly w. A deviation at stage k gains at most 1/4 once and then loses 1/2 per remaining stage, so the maximal average gain is attained at the last stage and equals

1/(4L).

Thus the same example that kills one-step Strong L4* satisfies the block version with

r_t = 1/(4*L_t),

and geometric L_t makes sum_t r_t < infinity.

So my verdict is:

[GAP] Strong L4* in its current one-step, W*-restricted form is not salvageable.

[SCOPE] The most promising replacement is a **block version of L4***.

A lighter syntactic repair also exists: let beta(h+) range over full W(h+) rather than W*(h+). In the same PD example, that already restores an exact one-step selector. But if the route wants to keep exposed-face endpoints, blockification is the clean repair.
