# Paper v4 Rewrite (Pass 68)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the WRITER. The proof of Theorem A is now COMPLETE (67 Extended Pro passes). Your job: rewrite the paper as a complete, publishable research article.

## What has changed since v3

The v3 draft (865 lines) was written BEFORE the following breakthroughs:

1. **VP3 Resolution (Passes 54-57)**: The joint-germ compatibility condition VP3 in PRODUCT form is FALSE (counterexample on 2-state gadget). But GRAPH-VP3 is AUTOMATIC: J_C = {(mu, L(mu)) : mu in P_C} because flux = L(occupation) is LINEAR. This eliminates VP3 as a separate condition entirely.

2. **Theorem A under condition (a) (Pass 62, 46min thinking)**: Every finite stochastic game satisfying condition (a) — no player can unilaterally break irreducibility of any node kernel — has a uniform epsilon-equilibrium.

3. **Realization Theorem (Pass 64)**: Formal assembly: Section 5.1 Caratheodory mosaic + exit-tag augmentation + superexponential block schedule + condition (a) bias span bound + Bellman certificate.

4. **Local Controller Lemma (Pass 66)**: Nodewise public realizability for exit-capable augmented nodes. The augmented feasible polytope is the graph of the linear exit map — same Caratheodory mosaic lifts via affine injection J_C(mu) = (mu, L_C mu).

## Paper structure for v4

The paper should have this structure:

1. **Introduction**: Neyman's open problem. State Theorem A clearly. Discuss condition (a) and its relationship to the full conjecture. Literature review.

2. **Model**: Finite stochastic game, strategies, payoffs, uniform epsilon-equilibrium definition.

3. **Section 3: The Metastable Tree Object**: Compact asymptotic state space A_eta. Kakutani fixed point. (Already written in v3, needs minor cleanup.)

4. **Section 4: Flux Repair and Graph-VP3**: Flux coordinates beta_C(e,b) = alpha_C(e) * q_C(e,b). KEY RESULT: Graph-VP3 is automatic because flux = L(occupation) is linear. No separate compatibility condition needed. (This replaces the old VP3 section.)

5. **Section 5: Ergodic Realization**
   - 5.1: Caratheodory mosaic controller (internal occupation)
   - 5.2: Local Controller Lemma for augmented exit-capable nodes (Pass 66)
   - 5.3: Flux witness and exit routing

6. **Section 6: Proof of Theorem A**: Assembly under condition (a). kappa_eta > 0, bias span bound, Bellman certificate, superexponential schedule, regret bound. (Incorporates Passes 62/64.)

7. **Section 7: Discussion**: Relationship to full Neyman conjecture. What condition (a) buys. Open directions.

## Key equations to include

- Regret bound: eta + C_eta*delta + 2*H_eta/M* + K_eta/T <= eps
- Bias span: sp(h) <= (|S|-1)/kappa_eta
- Augmented error: |mu_hat^aug - mu_C^aug|_1 <= (1+Lambda_C)*eta + K_C*rho_C^L <= delta
- Graph-VP3: J_C = {(mu, L(mu)) : mu in P_C} (automatic, no separate condition)

## Your task

Write the COMPLETE LaTeX source for v4. This should be a self-contained, publishable paper. Use the notation conventions from v3 (xi for phase-state, beta for flux, etc.). Target length: 30-45 pages (enough for JET/TE). Include full proofs of all key results. This is not a sketch — it should be submission-ready.

Write actual LaTeX. Every theorem should have a proof. Every claim should be justified.
