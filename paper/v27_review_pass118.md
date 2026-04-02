# v27 Review — Pass 118

**Thinking**: Extended Pro
**Verdict**: FAIL (novelty/positioning) — but MATH IS CORRECT

## CRITICAL FINDING: First mathematically correct proof in 118 passes

### Mathematics: ALL PASS
1. Condition (a) → unichain: **PASS** — "this step is fine"
2. MDP theory: **PASS** — "standard and used correctly"
3. Supermartingale: **PASS** — "the strongest part of the paper, and I think it works"
4. Glicksberg fixed point: **PASS** — "I do not see a failure here either"
5. Main theorem / uniformity: **PASS** — "The proof chain closes"
6. Completeness: **No major hidden gap**

### FAIL reason: Not Neyman's conjecture + prior art

**The paper does NOT solve Neyman's open problem.** It proves a theorem under a STRONG
global irreducibility assumption (Condition A). The reviewer notes:

- Condition A is EQUIVALENT to classical irreducibility of all stationary profiles
- Rogers (1969) and Sobel (1971) already proved existence of stationary equilibria
  under this same assumption
- The hard part of Neyman's conjecture is the MULTICHAIN case, which the paper assumes away
- "the novelty burden is unmet"

### Reviewer's suggested repositioning

If rewritten as: "A direct proof that in irreducible finite stochastic games, a stationary
average-reward equilibrium yields a uniform ε-equilibrium with O(1/T) regret" — then
salvageable after adding classical references and honest positioning.

### Minor presentation fixes needed
- Filtration prose is hand-wavy — define pre-action filtration cleanly
- Bias uniqueness: either cite precisely or soften to "there exists a normalized bias"
- Add references: Rogers (1969), Sobel (1971), Federgruen (1978)

### Key quote
"Mathematical correctness of the conditional theorem: probably yes.
Claim to solve Neyman's conjecture: no.
Current-form publication recommendation: reject or drastically reposition."

## Implications

The game-level condition (a) is TOO STRONG — it's the classical irreducibility regime.
Neyman's actual condition is WEAKER. The paper's earlier versions used a nodewise
condition (weaker), but that required a tree decomposition which creates multichain MDPs.

The open problem lives in the GAP between:
- Classical irreducibility (proven, not new)
- Nodewise irreducibility (tree approach failed — multichain)

This is a DECISION POINT for the project direction.
