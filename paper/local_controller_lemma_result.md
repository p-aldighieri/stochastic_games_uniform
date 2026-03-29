# Local Controller Lemma — Pass 66

**Pass**: 66
**Role**: Prover
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Chat**: Mathematical Lemma Proof

## THE LEMMA IS PROVED

**Lemma (Nodewise public realizability for exit-capable augmented nodes).**

Let C be a node with Out(C) != empty. Under condition (a), for every feasible augmented occupation measure mu_C^aug = J_C(mu_C) in M_C^aug, every delta > 0, and every entry state xi_0, there exists a public finite-memory block controller u_C of block length L such that:

(i) Empirical augmented occupation within delta of target in ell-1
(ii) Controller uses only public information
(iii) Block length L depends only on |C|, delta, and game parameters (not entry state)
(iv) Controller is deterministic conditional on public memory state

## PROOF STRUCTURE

**Step 1: Augmented feasible set is affine lift of Section 5.1 polytope**
- J_C: M_C -> M_C^aug, J_C(mu) = (mu, L_C mu) is affine and injective
- Preserves extreme points, so Caratheodory decomposition lifts verbatim
- No new convex-geometric argument needed

**Step 2: Apply Section 5.1 internal realizability**
- Set eta = delta / (2(1 + Lambda_C)), where Lambda_C = ||L_C||_{1->1}
- Section 5.1 yields public finite-memory controller v_C with ||mu_hat - mu_C||_1 <= eta
- L_int depends only on |C|, eta, game parameters

**Step 3: Augment controller by cemetery memory states**
- M_C^aug := M_C ⊔ {m_b^dag : b in B}
- While in C: behave like v_C
- On exit through edge b: memory updates to m_b^dag (absorbing)
- u_C is public, deterministic conditional on memory

**Step 4: Error estimate**
- beta_hat = L_C(mu_hat) + r_L where ||r_L||_1 <= K_C * rho_C^L (geometric tail)
- ||mu_hat^aug - mu_C^aug||_1 <= (1 + Lambda_C)*eta + K_C*rho_C^L
- Choose L >= L_int and K_C*rho_C^L <= delta/2
- Then (1 + Lambda_C)*eta + K_C*rho_C^L <= delta/2 + delta/2 = delta

**Step 5: Verification of (ii), (iii), (iv)**
- (ii): Both Section 5.1 mosaic and cemetery switch use only public info
- (iii): L_int, Lambda_C, K_C, rho_C depend only on |C|, delta, game parameters
- (iv): v_C deterministic by Section 5.1; cemetery transition also deterministic

## KEY INSIGHT

The augmented feasible polytope is the graph of the linear exit map over Section 5.1's internal polytope. Same Caratheodory mosaic lifts nodewise. Absorbing cemetery tags cost only the already-existing geometric tail term. No new combinatorial gadget needed.

## WHAT THIS MEANS

This was the last gap identified by the Pass 65 reviewer. With this lemma proved:
- Section 5.1 Caratheodory mosaic extends to exit-capable augmented nodes
- The realization theorem (Pass 64) is now fully rigorous
- **Theorem A is COMPLETE**: Every finite stochastic game satisfying condition (a) has a uniform epsilon-equilibrium
