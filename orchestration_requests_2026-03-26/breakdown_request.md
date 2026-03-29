You are the Breakdown role — responsible for decomposing the proof into a structured plan of lemmas and steps.

## Your Task

Given the formalized claim and the selected proof strategy, create a detailed proof blueprint that the Prover can follow. The aim is not to atomize the proof into tiny API-style micro-steps, but to choose proof-sized modules that reflect the real structure of the route.

## Instructions

1. **Decompose the proof into numbered lemmas/steps**, ordered logically (dependencies first).
2. **Each lemma should be**:
   - Self-contained: clearly stated with its own hypotheses and conclusion
   - Appropriately sized: not trivial (e.g., "by definition"), but also not split so finely that the actual proof architecture disappears
   - Tagged with its proof technique hint (induction, direct, contradiction, etc.)
3. **Show the dependency graph**: which lemmas depend on which.
4. **Identify the "critical lemma"** — the hardest step where the proof is most likely to fail.
5. **Include "glue steps"** that connect lemmas to each other and to the final conclusion.
6. **Separate the route into**:
   - provable now
   - conditional on a central blocker
   - the central blocker itself

## Output Format

Use this structure:

```
## Proof Breakdown

**Strategy:** (which route)
**Total steps:** N

### Lemma 1: (descriptive name)
**Statement:** (precise statement with hypotheses and conclusion)
**Depends on:** (nothing / Lemma X, Y)
**Technique hint:** (induction / direct / contradiction / ...)
**Known results that may help:** ...
**Difficulty:** (routine / moderate / hard)

...

### Final Assembly
**Statement:** Lemmas 1-N together imply the main claim because...
**Depends on:** All previous lemmas

## Critical Path
The hardest step is Lemma X because...
If Lemma X fails, the fallback is...

## Dependency Graph
Lemma 1 → Lemma 3 → Final
Lemma 2 → Lemma 3
```

## Key Principles

- **Granularity matters**: each lemma should be a proof-sized move, not a micro-step. Prefer a smaller number of meaningful modules over a long chain of fragile tiny claims.
- Don't skip "obvious" steps — the Prover needs explicit intermediate claims.
- If the strategy requires a result you're not sure is true, mark it clearly.
- The breakdown should be **editable** — the Prover may request amendments via `[BREAKDOWN_AMEND]` tags.
- Order matters: put independent lemmas first so they can be proven without waiting.
- If one theorem-sized blocker dominates the route, isolate it explicitly and keep the rest of the plan honest about depending on it.
- You may reorder, merge, or replace previous lemmas if that better reflects the actual proof architecture.

## Mode: semi_strict
## Branch: main
## Phase: breakdown

---

## Context

### Selected Route

**Slice reduction + 2D theorem + global additivity + k-good extension + order normalization**

This is the proof architecture for the higher-dimensional bootstrap of the simplicity conjecture, building on the already-proved two-good case (Theorem 9).

### What must be proved

**Main Theorem (Theorem 12).** For a finite product menu $Y = \prod_{i=1}^k M_i$ with $M_i = \{m_{i,1} < \cdots < m_{i,n_i}\} \subseteq [0,1]$, and $p_0$ the canonical pricing function of an IC/IR/NPT mechanism with $p_0(y) < \infty$ for all $y \in Y$:

$$\text{Simple}_{\text{nat}}(Y, p_0) \iff \exists\, p_1, \ldots, p_k \text{ s.t. } p_0(y) = \sum_{i=1}^k p_i(y_i) \quad \forall y \in Y.$$

**Order-Normalization Lemma.** If there exist SOME total orders $\preceq_i$ making the product menu simple, then the natural orders also make it simple:

$$(\exists \preceq\; \text{Simple}_\preceq(Y, p_0)) \iff \text{Simple}_{\text{nat}}(Y, p_0) \iff \text{additive separability on } Y.$$

### Established foundation (available, do NOT re-prove)

**Theorem 9 (two-good case, proved in prior run).** For $k = 2$, a finite product menu $Y = M_1 \times M_2$ with canonical price $P_{rs} = p_0(a_r, b_s)$ (convex, nondecreasing):

$$\text{simple ordered product menu} \iff P_{rs} = u_r + v_s \quad \forall r,s.$$

Key tools from Theorem 9:
- Utility matrix $A^\theta_{rs} = \theta_1 a_r + \theta_2 b_s - P_{rs}$
- Adjacent secant slopes $\sigma^x_{r,s}$, $\sigma^y_{r,s}$ are nondecreasing (from convexity)
- Each row and column of $A^\theta$ is discretely concave (Lemma 2)
- Nonzero adjacent minor $\Delta_{rs} \neq 0$ creates a nonglobal orthogonal local maximum via secant-slope choice of $\theta$ (Lemma 6')
- All adjacent minors vanish $\Rightarrow$ telescoping gives $P_{rs} = u_r + v_s$ (Lemma 8)

**CRITICAL WARNING**: The original abstract localization Lemma 6 is FALSE. The replacement Lemma 6' uses the actual convex structure of $p_0$ (secant-slope monotonicity), not just unimodality. Any higher-dimensional argument must similarly use convexity, not just abstract matrix properties.

### Key model facts

- $p_0: [0,1]^k \to [0,\infty]$ is convex, coordinatewise nondecreasing, closed (lower semicontinuous)
- $p_0(0) = 0$
- $p_0$ is the Fenchel conjugate of the buyer's utility $U$
- The buyer's type space is $\mathbb{R}_+^k$
- Utility on $Y$: $u_\theta(y) = \theta \cdot y - p_0(y)$

### Proof architecture (from claim)

**Target 1: Lemma 10 — Two-coordinate slice reduction.**
Let $k \geq 2$. Assume $\text{Simple}_{\text{nat}}(Y, p_0)$. Then for all $i \neq j$, all anchors $a \in \prod_{\ell \neq i,j} M_\ell$, all $(\theta_i, \theta_j) \in \mathbb{R}_+^2$, there exists $\hat\theta_{-\{i,j\}} \in \mathbb{R}_+^{k-2}$ such that:
1. **Frozen-coordinate pinning**: for all $y \in S_{ij}(a)$ and all $\ell \notin \{i,j\}$, any adjacent move in coordinate $\ell$ is weakly non-improving.
2. **Induced simplicity**: every two-coordinate slice $S_{ij}(a)$ with restricted price and natural orders is simple.

**Technique hint**: For each frozen coordinate $\ell$, choose $\hat\theta_\ell$ to be a supporting slope of $p_0$ in coordinate $\ell$ at the anchor value $a_\ell$, so that moving in coordinate $\ell$ cannot improve utility. One-sided supporting slopes are admissible at boundary values.

The $\hat\theta_{-\{i,j\}}$ may depend on $(i, j, a, \theta_i, \theta_j)$ but must work uniformly for all $y \in S_{ij}(a)$.

**Target 2: Lemma 11 — Pairwise vanishing mixed differences imply global additivity.**
Let $k \geq 2$. Assume that for every pair $i \neq j$ and every anchor $a$, all adjacent 2×2 minors of the two-coordinate price matrix vanish:
$$P^{i,j,a}_{r+1,s+1} - P^{i,j,a}_{r+1,s} - P^{i,j,a}_{r,s+1} + P^{i,j,a}_{r,s} = 0.$$
Then $p_0$ is additively separable on $Y$: $p_0(y) = \sum_{\ell=1}^k q_\ell(y_\ell)$.

**Technique hint**: Basepoint telescoping on the product grid. Fix $y^* \in Y$. Define $p_\ell(y_\ell) = p_0(y_\ell, y^*_{-\ell}) - p_0(y^*)$. Use pairwise vanishing mixed differences to show cross-terms cancel when telescoping along any path from $y^*$ to $y$.

**Target 3: Theorem 12 — Assembly.**
Easy direction ($\Leftarrow$): If $p_0$ is additive, utility separates into $k$ one-dimensional concave terms; a nonoptimal bundle fails at least one term, giving an adjacent improving step.
Hard direction ($\Rightarrow$): Simplicity → (Lemma 10) every 2-coordinate slice is simple → (Theorem 9) pairwise vanishing of all adjacent minors → (Lemma 11) global additivity.

**Target 4: Order-normalization lemma.**
If $p_0$ is additively separable, one-step improvement depends only on 1D restrictions; each $p_i$ is convex on $M_i$; so the natural order works. Simplicity under any order → additive separability (by the main theorem for that order, using a relabeling argument) → simplicity under natural order.

### Literature assessment highlights

- **Lemma 11** is closest to known theory: essentially a modularity/valuation statement on a product grid (Bach, Geissinger). Techniques: direct telescoping with path independence, or valuation/Möbius theory on product lattice.
- **Lemma 10** is the real technical frontier. Literature supports pointwise supporting-slope pinning (Rockafellar subdifferential), but the slice-wide common pinning vector is the key challenge.
- **Order normalization**: The statement is plausible only as an existential statement (not blanket invariance across all orders). Literature counterexample shows additive + arbitrary order can fail simplicity.

### Scope restrictions (out of scope)

- Infinite/continuous menu case
- Adjacency-vs-comparability variant
- Re-proving Theorem 9 or any of its constituent lemmas
