# Searcher Response: Route D' — Compact Asymptotic State Space

**Source**: ChatGPT Extended Pro, "Compact Asymptotic State Space" chat
**Date**: 2026-03-27
**Role**: Searcher
**Pass**: 28 (first Route D' pass)

## Preamble

Answering the Route D' brief directly: the target is still the exact strategy-existence theorem, not merely equilibrium-payoff existence, and the durable project record already rules out three nearby roads — stationary discounted limits, public-punishment assembly without private signals, and raw fixed points on strategy space. So any viable D' object has to compactify asymptotic behavior itself: occupation, exits, continuation values, gain-bias data, and an implementability map to one public-history profile.

The literature points to three especially useful templates: absorption-path compactification for quitting games, ergodic/operator compactification for zero-sum games, and recursive reduction to absorbing subclasses for some nonzero-sum cases. From that mix, I see five genuinely distinct proof architectures. My ranking is: 1 is the most native to Route D', 2 is the strongest conceptual alternative, 5 is the best subclass-expansion bridge, and 3 plus 4 are more likely to be lemma engines or side doors than standalone closures.

## Strategy 1: Metastable Occupation-Flux Tree

**Compact object**: A finite rooted DAG of communicating classes; for each node C, store a phase-labeled occupation measure mu_C on state-action pairs inside C, a projective exit-rate vector alpha_C over outgoing macro-exits, an exit law q_C, continuation values on successor nodes, and a normalized bias vector b_C. The phase label matters because periodic transition structure can be essential, so invariant measures alone are too coarse.

**Breakdown target**: Define consistency equations for these coordinates; prove every sequence of long-block profiles has a convergent asymptotic-tree subsequence; prove payoffs and unilateral deviation values are continuous on the tree by renewal equations; apply Kakutani on the relaxed tree space; then realize fixed points by growing blocks. This is the closest honest generalization of quitting-game absorption paths, whose space is sequentially compact with continuous payoff-path map, combined with the rare-transition communicating-set hierarchy used in nonzero-sum stochastic games.

**Main obstacle**: Implementability has to stay closed when classes split, merge, or differ only at smaller rare-transition scales, and transition-tilting deviations must be readable continuously from the exit coordinates.

**Feasibility**: MEDIUM-HIGH

## Strategy 2: Ergodic Nash-Operator Graph Compactification

**Compact object**: Not a limit strategy x*, but the compactified graph of a set-valued generalized Shapley/Nash correspondence on tuples (g, b, x), where x is a statewise mixed-action table, g is the gain vector, and b is a normalized bias table satisfying a Poisson-type equation relative to x. Build A as the closure of discounted equilibrium branches (delta, g_delta, b_delta, x_delta) in projective bias space.

**Breakdown target**: Define the correspondence; prove nonemptiness for every discount; show upper hemicontinuity and compactness after bias normalization; obtain a fixed point of the graph correspondence; then feed the resulting gain-bias table into the project's telescoping/block machinery. The zero-sum template here is powerful: Mertens-Neyman gives the asymptotic value, and operator-theoretic work studies mean payoff through the ergodic equation T(u) = lambda*e + u and nonexpansive-map dynamics.

**Main obstacle**: Route B already shows that the pointwise stationary limit of discounted Nash equilibria can fail bias-level optimality, so the object must retain whole branch data, not only x*. The missing selector becomes the theorem-sized bottleneck.

**Feasibility**: MEDIUM

## Strategy 3: Puiseux-Branch Compactification of Discounted Nash Correspondences

**Compact object**: Fix a support pattern and write the discounted equilibrium conditions in variables (x, v, lambda). On each support chart these conditions are semi-algebraic; curve selection then decomposes the discounted Nash graph near lambda=0 into finitely many Puiseux-type branches. A point of A records the support pattern, leading exponents of action probabilities and value gaps, leading coefficients, and the induced gain-bias and rare-exit skeleton. This keeps the first nontrivial asymptotic jets instead of a single blurry limit.

**Breakdown target**: Prove semi-algebraicity support by support; extract finitely many branch types; show branch invariants determine payoff and deviation limits continuously; then implement a chosen branch by block lengths calibrated to the exponents. This imports the real-algebraic spirit behind Bewley-Kohlberg and the later o-minimal/definable program for zero-sum games.

**Main obstacle**: Semi-algebraicity by itself is not enough. Universality results show that Nash sets of finite games can realize essentially arbitrary compact semi-algebraic topology, and equilibrium sets generally split into many components. So one would need a stochastic-game-specific tameness theorem for the discounted Nash graph plus Markov-flow constraints, not for arbitrary Nash sets.

**Feasibility**: MEDIUM-LOW

## Strategy 4: Viability-Kernel Compactification

**Compact object**: Let K be the compact set of feasible asymptotic descriptors z = (m, f, v, b, xi), where m are occupation masses, f exit fluxes, v continuation values, b biases, and xi records deviation slack. Define a set-valued drift F(z) as the long-block moves that are locally implementable and locally incentive-compatible. Then let A be the viability kernel, or the internally chain-transitive invariant subsets, of the differential inclusion z-dot in F(z).

**Breakdown target**: Relax to mixed blocks so F has compact convex values; prove upper semicontinuity on K; apply viability/Nagumo machinery to obtain an invariant orbit; discretize that orbit into increasing blocks; show the discretization error is summable and preserves epsilon-incentives. Viability theory is built exactly for turning local admissibility constraints into global feedback trajectories, and stochastic-approximation/differential-inclusion tools, plus continuous-time best-response dynamics, already exist around stochastic-game learning in zero-sum settings.

**Main obstacle**: Purifying a viable relaxed orbit into an actual public-history strategy without importing extra correlation is delicate, and the convexity needed by the viability machinery may fail before relaxation.

**Feasibility**: LOW-MEDIUM

## Strategy 5: Recursive Collapsing to Generalized Quitting Skeletons

**Compact object**: Build a sequence of depth-k skeleton games by collapsing each long-lived communicating class into a macro "continue" node with finitely many exit modes and continuation tables. For each skeleton, use the compact object available in the nearest solved class: absorption paths for quitting layers, and continuation-orbit or equilibrium-manifold style objects for positive recursive absorbing layers. A point of A is a compatible inverse-limit family of skeleton descriptors across k.

**Breakdown target**: Define the reduction; prove that the error from collapsing microstructure below depth k is o_k(1); show each skeleton has a compact equilibrium object; prove compatibility maps are continuous; pass to the inverse limit; realize the limit by nested block lengths. This route is attractive because quitting games do admit a sequentially compact absorption-path space, positive recursive general quitting games admit sunspot epsilon-equilibria via smooth-manifold approximation, and a 2025 positive-recursive absorbing result proves plain undiscounted equilibrium payoffs under a non-rectangular absorption restriction.

**Main obstacle**: Many of the higher-player positive results at this boundary are payoff results, sunspot results, or rely on special absorption geometry, so the inverse limit may stop one rung short and yield only a payoff object unless the compatibility maps encode an actual plain strategy profile.

**Feasibility**: MEDIUM-LOW for the full theorem, MEDIUM as a route to large subclasses.

## Searcher Recommendation

If I had to choose one next proof breakdown target, I would push **Strategy 1 first**, with **Strategy 3 as its lemma engine**. Strategy 1 is the only route that natively carries all four D' coordinates the project wants — occupation, exits, continuation, and gain-bias — while matching the existing block implementation and deviation taxonomy. Strategy 2 is the highest-upside alternative if the selector obstruction can be replaced by a closed Nash-operator graph theorem. I did not find evidence in the sources I checked that the general theorem has already been closed; recent papers from 2019 and 2025 still treat the multiplayer case as open.
