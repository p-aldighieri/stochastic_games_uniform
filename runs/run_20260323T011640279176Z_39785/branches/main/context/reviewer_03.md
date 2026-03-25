# Reviewer Output

Generated: 2026-03-23T05:23:04.273915+00:00

VERDICT: PATCH_BIG

The packet has several sound conditional repairs, but it is still not certifiable in its present form. The already-acknowledged gaps at L4, L8, and L9 remain theorem-sized, and there is also an earlier defect in L2-L3: the modified-game source gives stationary equilibria and minmax comparison for a **fixed initial state** (s_0), whereas L2 upgrades that to one stationary equilibrium (x^\lambda) producing a minmax-safe payoff table (m^\lambda(s)) for **every** state simultaneously. The modified-game paper explicitly notes that even the stationary optimal strategy may depend on the initial state, so this upgrade is not currently justified.    

### Validated pieces

* **L1** is logically fine **under the stated amendment and imported theorem**: using a coalition controller whose action at each history is a product mixed action closes the implementation gap, and restartability after any public history is legitimate in the public-history stochastic-game model. This is a correct imported reduction, not a new theorem. 
* **L2(3)** is fine once a legitimate family (m^\lambda\subset[0,1]^{N\times S}) has been defined. Compactness of the cube makes precompactness immediate. 
* **L3** is correctly repaired at part (4): “arbitrarily large (\lambda)” is the right conclusion for accumulation points; “all (\lambda) sufficiently close to 1” was too strong. Given a valid family (m^\lambda), the proofs of L3(1)-(3) and the corrected L3(4) are fine. 
* **L5-L7** are correct as conditional lemmas. Once L4 supplies block data and the terminal-bonus convention is fixed exactly as in the amendment, the neighborhood robustness, finite subcover, and finite-cycle extraction arguments go through. 
* **Amended L10-L11** are also correct **conditional on the sharpened L9′**. Replacing (T_{\max}) by the regularized-block bound (B_{\max}), and forcing the endpoint term into (c_0/T) scale, repairs the bookkeeping cleanly. 

### Precise errors and gaps

1. **[SCOPE] L2/L3 overreach the modified-game source from “fixed initial state” to “all states simultaneously.”**
   The modified game is defined with a fixed initial state (s_0), and Theorem 4.1 proves stationary equilibrium existence for each such (s_0). Corollary 7.4 then gives only a fixed-state lower bound
   [
   \liminf_{\lambda\to1}\hat\gamma_i^\lambda(s_0,x^\lambda)\ge v_i(s_0)
   ]
   for that same initial state. The paper also gives an explicit example showing that the stationary optimal strategy in the modified game can depend on the initial state. So the current L2 statement, namely that there exists one stationary equilibrium (x^\lambda) whose induced table (m^\lambda(s)) is minmax-safe for every state (s), is not supported by the cited machinery. 

   This is the main new blocker. If you repair it by choosing separate equilibria (x^{\lambda,s}) for each state and then defining a coordinatewise table, you lose the claim that (m^\lambda) is “induced by one equilibrium (x^\lambda).” Then L3(4) and the current L4 heuristic “start from a modified-game equilibrium near (w)” no longer mean what they need to mean. That is why this is **PATCH_BIG**, not a typo-sized repair. 

2. **L2(2) needs exact wording and exact citation.**
   The cap is essentially definitional, but the current phrasing is ambiguous. The precise modified contribution from a partition cell (D) is
   [
   \min{U_i^\lambda(s_0,\sigma;D),\ t_\lambda(s_0,\sigma;D)c_i(D)},
   ]
   or equivalently the **normalized** payoff within (D) is capped by (c_i(D)). Saying simply that the “contribution is capped by (c_i(D))” blurs raw versus normalized quantities. The correct citation is Definition 3.1 / equation (3) of the modified-game paper, not a generic appeal to “the modified-game machinery.” 

3. **L4 remains the theorem-sized unresolved seam.**
   The packet is right about where the real dragon lives. The 2025 absorbing paper does give an analogous block map in a special class of positive recursive absorbing games, and the introduction summarizes exactly the kind of finite block with terminal payoff, positive hazard, and successor map that the packet wants. It also explicitly says that extension to positive recursive games with more than one nonabsorbing state is still an open direction. So the citation is correct, but it confirms that L4 is still open rather than supporting it. ([arXiv][1])

4. **L8 and L9 are still not proofs.**
   The packet correctly marks them as open or incomplete. That is acceptable proof-state bookkeeping, but it means the theorem is not closed. In particular, L10-L11 only become usable after an actual L9 proof with the endpoint term normalized as (c_0/T). Right now L10-L11 are repaired conditionals, not forward progress on the main existence theorem. 

### Citation audit

* The open-problem citation is correct: the Game Theory Society page states, as Problem 1, “Does every stochastic game with finitely many players, states, and actions have a uniform equilibrium?” and attributes it to Abraham Neyman. ([Google Sites][2])
* The arXiv citation is also correct for the absorbing-game result and for the paper’s own block-map summary; the same source explicitly describes the positive-recursive, multi-nonabsorbing-state extension as future work and mentions that a broader companion result uses a **public correlation device**. ([arXiv][1])
* The missing citations are in **L2**. That step should cite, at minimum, the modified-game definition/cap formula, the stationary-equilibrium theorem, and the fixed-state minmax comparison theorem/corollary, all at theorem level. As written, “modified-game machinery” is too foggy for certification. 

### Scope notes

* **[SCOPE]** Do not import the companion public-correlation result into this route without a separate derandomization theorem. The durable target does **not** add an external public randomization device.  ([arXiv][1])
* **[SCOPE]** Do not silently upgrade fixed-initial-state modified-game theorems to simultaneous all-state continuation tables. That is exactly the inflation currently happening in L2/L3.  

### What to patch next

1. Rebuild **L2/L3** around a continuation object that is actually supported by the modified-game paper. Either prove a new simultaneous-all-states theorem for a single stationary equilibrium family (x^\lambda), or rewrite the continuation region so L4 no longer needs “a nearby equilibrium table induced by one profile.” The latter is a genuine redesign, not a local edit. 
2. Keep the current repairs to **L3(4)** and **L10-L11**. Those are good and should stay. 
3. Treat **L4** and **L9** as the two real theorem-sized tasks. The packet’s own labor allocation on that point is correct. 

This route still looks alive, but the continuation geometry is not yet sitting on a proven foundation.

[1]: https://arxiv.org/html/2512.04306v1 "Undiscounted Equilibrium in Positive Recursive Absorbing Games with Non-Rectangular Absorption Structure The authors thank János Flesch for commenting on an earlier version of the paper. Solan acknowledges the support of the Israel Science Foundation grant #211/22."
[2]: https://sites.google.com/view/thegametheorysocietyilchapter/open-problems?utm_source=chatgpt.com "Open Problems"
