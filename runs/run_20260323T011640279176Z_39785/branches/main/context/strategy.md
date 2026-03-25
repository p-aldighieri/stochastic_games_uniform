# Searcher Output

Generated: 2026-03-23T02:57:22.328141+00:00

## Selected Route
**Hybrid modified-game + continuation-orbit construction.**

## Route Details
**Core technique:** Use a statewise auxiliary modified game to cap continuation payoffs at minmax-compatible levels, then build a compact continuation region (W) and a map (f) whose nodes are finite equilibrium blocks. The modified-game paper already supplies the auxiliary-game architecture and the stationary-equilibrium side, while the 2025 non-rectangular absorbing proof shows how each continuation vector (w) can generate a finite-horizon (\varepsilon)-equilibrium block (\sigma(w)) with positive absorption hazard, after which an approximate finite orbit of (f) is concatenated into one global strategy.
   **Key intermediate steps:** First, define partitions and cutoffs (c_i(D)) just above the uniform minmax values and prove a local block lemma in the full game: for every (w\in W), there is a block that is already an (\eta)-equilibrium of a (T(w))-stage game with terminal bonus (w), has controlled exit probability (\mu(w)>0), and yields a next continuation close to (f(w)). Second, prove an approximate finite-orbit theorem for the full continuation map, not just in the positive recursive absorbing subclass. Third, concatenate the blocks and attach public deviator-identification plus minmax punishments so the continuation vector forms an almost-supermartingale until absorption or detection. Fourth, turn that supermartingale control into finite-horizon average-payoff control, with the last partial block and all monitoring costs swallowed into the (\varepsilon) budget.
   **Likely failure point:** The hard seam is the local block lemma outside absorbing-like geometry. In the general game, punishments change transition structure, several recurrent classes may compete at once, and the continuation map may stop being tame enough to admit a finite-orbit argument. The other danger is that the route may deliver payoff-form invariance without yet yielding one uncorrelated profile that works for all large (T).
   **Complexity estimate:** Extreme, but modular. It is the most promising full-theorem route because the literature already has one engine for auxiliary payoffs and another for orbit concatenation; the missing bridge is brutal, but it is visible.
