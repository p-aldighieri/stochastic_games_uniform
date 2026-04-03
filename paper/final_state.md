# Final State — Neyman's Conjecture Project

**Date:** 2026-04-03
**Total Extended Pro passes:** 139
**Duration:** ~30 hours of autonomous pipeline operation

---

## The Target

**Neyman's Conjecture (N-player):** Every finite N-player stochastic game satisfying condition (a) admits a uniform ε-equilibrium.

**Condition (a) [Fudenberg-Yamamoto]:** "Irreducible despite every player i" — for each player i, there exists an opponents' profile (uniform randomization works) such that the chain on S is irreducible regardless of player i's pure stationary strategy. Existential quantifier on opponents.

---

## What We Proved

### Theorem (v28, PASS at Pass 120)
Under **classical irreducibility** (every stationary mixed profile induces an irreducible chain on S), a stationary average-reward Nash equilibrium yields a uniform ε-equilibrium with O(1/T) regret.

- **Paper:** `paper/neyman_route_d_prime_v28.tex` (793 lines)
- **Proof:** Glicksberg fixed point on average-reward meta-game + Bellman supermartingale
- **Status:** Reviewed and PASSED. Math correct, positioning honest.
- **Novelty:** Modest — the regime is classical (Rogers 1969, Sobel 1971). Our contribution is the direct O(1/T) bound and clean modern proof.

---

## What We Discovered

### 1. The correct formulation of condition (a) (Pass 130)
The paper's original "for all opponents" formulation collapses to classical irreducibility via the support-selector argument. The genuine FY condition uses an **existential** quantifier on opponents — strictly weaker.

### 2. Why the tree decomposition fails (Passes 1-116)
The tree routing creates **absorbing terminal nodes** in the expanded MDP → multichain → no single scalar benchmark. All 10+ local-to-global bridge attempts failed. The tree itself is the problem.

### 3. Why perturbation fails (Passes 134-135)
η-perturbation by uniform makes the MDP irreducible, but η·sp(h^η) = O(1), not → 0. **3-player counterexample** with η·sp = 1 for all η. Bias span blows up as O(1/η) in nearly decomposable chains.

### 4. Why unichain ≠ irreducible matters (Passes 129, 133)
The hub/anchor approach makes the augmented MDP unichain but not irreducible. The v28 proof **requires** irreducibility: transient states have positive Bellman slack, best-response convexity fails, compliant lower bound breaks.

### 5. Why purification fails (Pass 138)
Public block time-sharing between product profiles cannot approximate correlated plans for incentive purposes: publicizing the phase index enlarges the deviator's strategy set.

### 6. Why Nash gain equalization fails (Pass 139)
The Nash condition does NOT force gains to equalize across recurrent classes. A deviator may reach multiple classes but cannot control the hitting law.

### 7. The precise remaining obstacle
Under FY condition (a), the deviator's induced MDP is **multichain**. Different recurrent classes carry different gains. The deviator can shift probability between classes. **No single-number certificate bounds this.** The certificate must be class-sensitive (exit-law dual, occupation-measure, or equivalent). Condition (a) alone does not provide sufficient control over recurrent-class selection.

---

## Route Map (All Routes Tried)

| # | Route | Passes | Result | Key File |
|---|-------|--------|--------|----------|
| 1 | Tree decomposition + local Bellman | 1-116 | FAIL: multichain terminal nodes | `chronicle.md` |
| 2 | Classical irreducibility (v28) | 117-120 | **PASS** (but known regime) | `neyman_route_d_prime_v28.tex` |
| 3 | Regenerative hub memory | 126-133 | FAIL: unichain ≠ irreducible | `phase2_memory_pass126.md` |
| 4 | η-perturbation (no memory) | 134-135 | FAIL: bias span blowup | `phase2_perturbation_pass134.md` |
| 5 | Solan acceptable profiles + purification | 137-138 | FAIL: purification false | `phase3_purification_pass138.md` |
| 6 | Nash gain equalization | 139 | FAIL: hitting law not controllable | `phase3_final_pass139.md` |

---

## Key Files

### Papers
- `neyman_route_d_prime_v28.tex` — Final PASSED paper (classical irreducibility)
- `neyman_route_d_prime_v27.tex` — Pre-edit version
- `neyman_route_d_prime_v29.tex` — Hub memory attempt (FAIL)
- `neyman_route_d_prime_v30.tex` — Anchor + FY attempt (FAIL)

### Phase 2 Analysis (Passes 121-136)
- `phase2_strategy_pass121.md` — Literature survey + strategy ranking
- `phase2_breakdown_pass122.md` — Proof decomposition into 4 lemmas
- `phase2_lemmaB_pass123.md` — Local LP certificate (PROVED)
- `phase2_benchmark_pass124.md` — Benchmark selection obstacle
- `phase2_leaky_pass125.md` — Projection lemma (PROVED)
- `phase2_memory_pass126.md` — Hub memory design
- `phase2_unichain_pass127.md` — Hub unichain lemma (PROVED internally)
- `phase2_research_pass130.md` — FY condition identified
- `phase2_redesign_pass131.md` — Anchor approach
- `phase2_perturbation_pass134.md` — Perturbation lemma (PROVED) + bottleneck
- `phase2_bias_pass135.md` — Bias span counterexample (DEFINITIVE)
- `phase2_strategy_final_pass136.md` — Strategic assessment

### Phase 3 Analysis (Passes 137-139)
- `phase3_strategy_pass137.md` — Solan + occupation-measure route
- `phase3_purification_pass138.md` — Purification lemma (FALSE)
- `phase3_final_pass139.md` — Nash equalization (FALSE)

### Reviews
- `v28_review_pass120.md` — PASS (the only PASS)
- `v27_review_pass118.md` — Math correct, novelty fail
- `v29_review_pass129.md` — FAIL (condition collapse + transient gap)
- `v30_review_pass133.md` — FAIL (unichain ≠ irreducible)

### Meta
- `chronicle.md` — Complete failure history with root causes
- `proof_state.md` — Phase 2 proof state document
- `archive/` — Old versions, reviews, fixes (v2-v26, 100+ files)

---

## Verified Building Blocks (Reusable)

These lemmas are independently proved and could feed future work:

1. **v28 theorem** — classical irreducibility → O(1/T) uniform ε-equilibrium
2. **FY condition formalization** — existential quantifier, strictly weaker than classical
3. **Local LP exit certificates** — exist for any benchmark ≥ g*_C (Pass 123)
4. **Projection lemma** — condition (a) → every recurrent class projects onto all S (Pass 125)
5. **Hub unichain lemma** — regenerative hub + condition (a) → single recurrent class (Pass 127)
6. **Perturbation irreducibility** — η·uniform makes MDP irreducible under FY (Pass 134)
7. **Glicksberg on perturbed space** — fixed point exists for each η > 0 (Pass 134)

---

## What Would Solve It

The conjecture needs one of:
- A **class-sensitive exit-law dual certificate** that bounds all achievable hitting distributions
- An **occupation-measure fixed point** with built-in recurrent-class control
- A **Vieille-style reduction** extended to N players (requires new punishment mechanism)
- A **discounted-to-uniform bridge** with Nash-selection stability (not just zero-sum Tauberian)

None of these are within reach of current automated proof methods. The problem is confirmed at the genuine mathematical frontier.

---

## Repository

- **Proof repo:** `p-aldighieri/stochastic_games_uniform` (commit `7ffc02c`)
- **Pipeline repo:** `p-aldighieri/MathPipeProver`
- **Method:** MathPipeProver — markdown-first AI proof orchestration with browser-backed ChatGPT Extended Pro submissions, Claude Code as orchestrator
