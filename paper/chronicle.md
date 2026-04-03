# Chronicle: 136 Passes Attacking Neyman's Conjecture

## The Target
**Neyman's Conjecture (N-player):** Every finite N-player stochastic game satisfying condition (a) admits a uniform ε-equilibrium.

**Condition (a) [Fudenberg-Yamamoto "irreducible despite every player i"]:** For each player i, there exists a mixed stationary opponents' profile x_{-i} (uniform randomization works) such that for ALL pure stationary f_i, the chain under (f_i, x_{-i}) is irreducible on S. Opponents' quantifier is EXISTENTIAL, not universal.

## What Does NOT Work (and WHY)

### Route 1: Tree Decomposition + Local Bellman (Passes 1-116)
**Idea:** Decompose game into SCCs, build local Bellman certificates (g_C, h_C) at each node, stitch together with stock Z and potential Ψ = h + Z.
**What works:** All local machinery verified 10+ times (Bellman, Z, Ψ, Kakutani on tree packages, realization theorem).
**What fails:** The local-to-global bridge. EVERY attempt to convert local per-node bounds into a global T-horizon bound failed:
- Gain near-constancy: DISPROVED (counterexample, g varies O(1))
- Tree telescoping: wrong currency (stationary rates vs actual)
- Visit-level chaining: exit/entry mismatch
- Common g_root scalar: appears false
- g_C as MDP value: g_C is restarted-node average, not global value
**Root cause (Pass 116):** The tree routing creates ABSORBING TERMINAL NODES in the expanded MDP → multichain → no single scalar benchmark. The tree itself IS the problem.

### Route 2: Direct Stationary on S — Classical Irreducibility (Passes 117-120)
**Idea:** Drop the tree. Use stationary strategies on S. Glicksberg + Bellman supermartingale.
**What works:** The proof is CORRECT under classical irreducibility (v28, PASS at Pass 120).
**What fails:** Classical irreducibility (all mixed profiles irreducible) is NOT Neyman's condition. It's the already-known regime (Rogers 1969, Sobel 1971). Not new.

### Route 3: Regenerative Hub Memory (Passes 126-129)
**Idea:** Add rich working memory + rare resets to a sticky hub state. Hub makes augmented MDP unichain.
**What works:** Hub unichain lemma correct internally (Pass 127).
**What fails:** Unichain ≠ irreducible. Working-memory states are TRANSIENT, causing:
- Bellman slack d(ω) > 0 at transient states
- Compliant lower bound fails from transient initial states
- Best-response convexity fails (gain-optimal set not convex under unichain)
**Root cause (Passes 129, 133):** The v28 proof requires IRREDUCIBILITY, not just unichain. The hub makes the MDP unichain but leaves working-memory states transient.

### Route 4: η-Perturbation (No Memory) (Passes 134-135)
**Idea:** Play (1-η)·Nash + η·uniform. Under FY condition (a), the η·uniform provides the guardian → chain irreducible → v28 applies.
**What works:** Makes MDP irreducible. Glicksberg gives fixed point. Regret = η·sp(h^η) + O(1/T).
**What fails:** η·sp(h^η) does NOT → 0. In nearly decomposable chains, sp(h^η) = O(1/η), so the product stays O(1).
**Concrete counterexample (Pass 135):** 3-player game satisfying FY condition with η·sp(h^η) = 1 for all η.
**Root cause:** The bias span blows up as the perturbation vanishes, exactly compensating the perturbation cost.

### Route 5: Vieille-Style Reduction (Pass 136 analysis)
**What Vieille does (2-player):** Separates states into "high payoff" (turned into absorbing states) and "future opportunity" (turned into recursive game). Solves recursive piece in second step.
**Why it doesn't extend to N players:**
- Missing brick 1: Multiplayer controlled-set alternative (2-player uses zero-sum structure)
- Missing brick 2: Coalition-stable punishment mechanism (2-player uses minmax)
- Condition (a) does not supply either of these

## The Precise Mathematical Obstacle

Under FY condition (a), when player i deviates while others play the compliant profile:
1. Player i's induced MDP on the augmented state space is MULTICHAIN
2. Different recurrent classes carry different gains g_1, g_2, ..., g_k
3. The deviator can shift probability between classes: payoff = Σ p_j(τ_i) g_j
4. The compliant achieves Σ p_j(σ_i) g_j
5. Regret depends on how much the deviator can shift probability toward high-gain classes

**No single-number Bellman certificate can bound this.** The certificate must be class-sensitive.

## What IS Available (Verified Building Blocks)

1. v28 proof under classical irreducibility (PASS)
2. FY condition correctly formalized (existential quantifier)
3. Local LP certificates for communicating sets (Pass 123)
4. Projection lemma: condition (a) → every recurrent class projects onto all S (Pass 125)
5. Hub unichain lemma (Pass 127, correct but insufficient alone)
6. Perturbation irreducibility lemma (Pass 134)
7. The Solan-Vieille communicating-set dichotomy framework
8. The Kakutani/Glicksberg fixed-point machinery on compact convex spaces

## What the Literature Says Works

- **2-player:** Vieille's reduction (controlled sets + recursive games + punishment)
- **N-player correlated:** Solan-Vieille 2002 (correlation device enables punishment)
- **Discounted:** Stationary equilibria always exist; payoff sets converge (Renault-Ziliotto)
- **Zero-sum:** Mertens-Neyman value exists via Bewley-Kohlberg algebraic structure

## The Unexplored Directions

1. **Discounted-to-uniform bridge with structure:** Not bare Tauberian, but using the algebraic structure of discounted equilibria (Bewley-Kohlberg Laurent expansions) to extract uniform strategies.

2. **Solan's acceptable profiles (2018):** Uses communicating-set exit laws, state-action frequencies, and a stay-or-exit dichotomy. Closest existing framework to what we need.

3. **Condition (a) as punishment substitute:** In 2-player, punishment = minmax. Under condition (a), "no player can break irreducibility" might provide a STRUCTURAL punishment: if a player deviates too much, the other players' guardian profile forces mixing across recurrent classes, diluting the deviator's gain advantage.

4. **Occupation-measure fixed point:** Work directly with long-run state-action frequencies. The feasible frequency set is a polytope. Condition (a) constrains which vertices are reachable. A dual certificate on this polytope might bound regret without needing bias spans.

5. **The "threat of uniform play" as deterrent:** Under condition (a), if player i deviates, the others can switch to uniform randomization (the guardian), which makes the chain irreducible and destroys any recurrent-class advantage. This is a PUNISHMENT mechanism built into condition (a) itself. The key question: can this threat be made credible in a Nash (not correlated) equilibrium?
