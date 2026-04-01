# Local Controller Lemma (Pass 66)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the PROVER. Write the FORMAL LEMMA that the reviewer (Pass 65) identified as the last missing piece.

## The Lemma

**Lemma (Nodewise Public Realizability for Exit-Capable Nodes)**:

Let C be a node in the metastable tree with Out(C) ≠ ∅ (exit-capable). Let mu_C^aug be a feasible augmented occupation measure on the exit-tag augmented system (Xi_C ∪ {∂_b : b ∈ Out(C)}), where cemetery states encode exits. Let condition (a) hold (every unilateral node kernel is irreducible on C).

Then for every delta > 0 and every entry state xi_0 ∈ Xi_C, there exists a PUBLIC FINITE-MEMORY BLOCK CONTROLLER u_C of block length L such that:

(i) The empirical augmented occupation measure is within delta of mu_C^aug in ell-1
(ii) The controller uses only public information (actions and states observed by all players)
(iii) The block length L depends only on |C|, delta, and the game parameters (not on the entry state)
(iv) The controller is deterministic conditional on the public memory state

## Why this should be true

Section 5.1 already proves this for the INTERNAL occupation measure (Caratheodory mosaic). The augmented system adds cemetery states that are absorbing. The exits are encoded as transitions to cemetery states with known probabilities (determined by the occupation measure via beta = L(mu)).

The key insight: on the augmented system, the Caratheodory mosaic construction from Section 5.1 applies DIRECTLY. The cemetery states are just additional states. The ergodic decomposition works the same way. The only subtlety is that once the process hits a cemetery state, the block terminates — but this is handled by the geometric tail bound already in Section 5.1.

## Your task

PROVE THIS LEMMA. Show that Section 5.1's construction extends to the augmented exit-tagged system. Be explicit about how exits are handled. This is the last piece — once this lemma is proved, Theorem A is complete.
