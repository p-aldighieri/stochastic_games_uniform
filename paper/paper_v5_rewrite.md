# Paper v5 Rewrite — Fix Fundamental Definitions (Pass 73)

Provider: external_agent
Model hint: chatgpt-5.4-pro
Generated: 2026-03-30

## Instructions

You are the REWRITER. A 33-minute Pro review found that the v4 paper has fundamental DEFINITION errors that make the proof appear broken, even though the underlying mathematics is correct. The attached `neyman_route_d_prime_v4_final.tex` is the current paper.

Your job: FIX ALL SIX ISSUES below and output the COMPLETE corrected LaTeX source.

## Issue 1 (CRITICAL): Node occupation polytope forces zero exit mass

The balance equations (lines ~380-406) use raw stationarity:
  pi_mu(xi') = sum mu(xi,a) P_C^0(xi'|xi,a)
with mu in Delta(Omega_C). Summing over xi' gives total internal mass = 1, forcing L_C mu = 0. This makes exit-capable nodes have empty feasible sets.

**FIX**: Redefine using the AUGMENTED system with cemetery states. For exit-capable node C with Out(C) = B:
- Augmented state space: Xi_C^aug = Xi_C ⊔ {partial_b : b in B}
- Cemetery states partial_b are absorbing
- Occupation measure mu^aug = (mu, beta) where beta = L_C(mu) is the exit mass
- The AUGMENTED stationarity equations allow total internal mass < 1, with the deficit being exit mass
- Formally: sum_xi' P_C^aug(xi'|xi,a) mu(xi,a) = pi^aug(xi') where the sum includes cemetery states
- This gives: internal mass + exit mass = 1 (correct!)

The key point from the proof (Pass 66): M_C^aug = J_C(M_C) where J_C(mu) = (mu, L_C mu) is the affine lift. The internal polytope M_C should be defined as the set of SUB-probability measures satisfying the flow-balance equations with deficit equal to exit mass.

## Issue 2: Local Nash existence needs multi-player theorem

Appendix A only proves one-player LP duality. But N_C(x) requires a package where ALL players simultaneously have Bellman certificates.

**FIX**: Add a proper local equilibrium existence proposition. At each node C with fixed environment x:
- Each player i faces an average-reward MDP (given others play according to the occupation measure)
- A local Nash equilibrium exists by standard finite-game Nash theorem applied to the "average game"
- The Bellman certificates (g_i, h_i) exist for each player at the equilibrium occupation
- Reference: this is a standard result for finite stochastic games restricted to a single ergodic class

## Issue 3: Kakutani global assembly — continuation self-consistency

The current proof claims nodewise Nash selections assemble globally, but doesn't address continuation value self-consistency.

**FIX**: Make explicit that BR_eta(x) = {y in A_eta : y_C in N_C(x) for all C}. The key insight:
- y is assembled from local packages y_C, each optimal against x's continuation values
- y need NOT have the same continuation values as x — that's the WHOLE POINT of the fixed-point
- At the fixed point x* = BR_eta(x*), self-consistency is automatic
- For nonemptiness of BR_eta(x) for arbitrary x: the local packages are chosen against FIXED continuation values from x, so there's no circular dependency. The inter-node flow constraints are linear and compatible with any choice of local occupations (graph-VP3 handles this)

## Issue 4: Local Controller Lemma quantitative mismatch

Theorem 5.8 gives high-probability empirical bounds but Theorem 5.9 imports exponential expected-error K*rho^L.

**FIX**: Either:
(a) Strengthen Theorem 5.8 to give the exponential bound (standard for Markov chains with geometric mixing), OR
(b) Weaken Theorem 5.9 to use polynomial bounds O(1/sqrt(L)) which suffice for the final epsilon-equilibrium (just need L large enough)

Option (b) is cleaner: the local controller lemma only needs ||mu_hat^aug - mu^aug||_1 <= delta for SOME L depending on delta and game parameters. The specific rate doesn't matter.

## Issue 5: Deviation/Bellman coefficient-level perturbation

The deviation-value Lipschitz lemma needs a DEFINED map from occupation to MDP coefficients.

**FIX**: Explicitly define the map nu -> (r_nu, Q_nu):
- Given a node occupation measure nu for the compliant players, the deviator i faces an MDP with:
  - State space Xi_C
  - Action sets A_i(xi) for each state xi
  - Transition: Q_nu(xi'|xi, a_i) = sum_{a_{-i}} sigma_{-i}(a_{-i}|xi) P(xi'|xi, (a_i, a_{-i})) where sigma_{-i} is the mixed strategy profile induced by nu
  - Reward: r_nu(xi, a_i) = sum_{a_{-i}} sigma_{-i}(a_{-i}|xi) u_i(xi, (a_i, a_{-i}))
- This map is AFFINE in nu (since sigma_{-i} depends affinely on nu)
- Therefore ||r_{nu'} - r_nu||_inf <= C ||nu' - nu||_1 and ||Q_{nu'} - Q_nu||_TV <= C ||nu' - nu||_1
- These are the COEFFICIENT-LEVEL bounds needed for Bellman transfer

## Issue 6: Condition (a) operationally checkable

**FIX**: State condition (a) in terms of PRIMITIVE game data:
- Condition (a): For every node C in the metastable tree, every player i, and every action a_i of player i, the transition kernel P(·|xi, (a_i, a_{-i})) summed/mixed over any response a_{-i} of the other players keeps Xi_C irreducible.
- Equivalently: no single player can, by choosing their action, create a non-communicating class within a metastable node
- Give an EXAMPLE: any stochastic game where transitions depend only on the current state and the action profile (not on individual actions separately) satisfies condition (a) trivially if each node's internal transitions form an irreducible chain under every action profile

## Additional fixes needed

- Add missing references: Neyman 2003, Flesch-Thuijsman-Vrieze 1997, Nowak 2003, Solan-Vieille 2002, Kakutani FPT reference, standard MDP textbook
- Fix the deviation-value Lipschitz constant to 1 + sp(h), not just sp(h)
- Make P_C (the feasible occupation set) explicitly defined and distinguished from M_C

## Your task

Read the attached v4 tex file. Apply ALL fixes. Output the COMPLETE fixed LaTeX source. This should be a compilable, mathematically rigorous paper. Every definition must be precise. Every theorem must have a complete proof. Target the same ~30 page length.
