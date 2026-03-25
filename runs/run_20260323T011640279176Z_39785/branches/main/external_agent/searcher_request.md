# External Agent Request (searcher)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T02:57:22.318742+00:00

## Instructions

Propose 2-4 genuinely distinct proof strategies, each with: core technique, key intermediate steps, likely failure point, and complexity estimate. Rank by feasibility with most promising first. Number each route starting from 1. Tag scope-narrowing routes with [SCOPE].

## Context

## FILE: branches/main/context/formalizer.md

# Formalizer Output

Generated: 2026-03-23T01:56:36.300643+00:00

## Mathematical domain

Noncooperative game theory, specifically finite stochastic (Markov) games with perfect public monitoring, behavioral strategies, finite-horizon average payoff, and Nash-type equilibrium existence.  

## Claim type

Open universal existence conjecture. Logically, it is a strategy-existence statement with quantifier pattern
[
\forall G\in\mathfrak G\ \forall \varepsilon\in \mathbb R_{>0}\ \exists \sigma\in\Sigma(G)\ \exists T_0\in\mathbb N_{>0}\ \forall T\in\mathbb N_{>0}\ (T\ge T_0 \Rightarrow \forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G): \cdots ).
]
The adopted reading is the existence of uniform (\varepsilon)-equilibria for every (\varepsilon>0), not the alternative payoff-set formulation.  

## Precise formal statement

Let (\mathfrak G) be the class of all tuples
[
G=(N,S,(A_i)*{i\in N},u,P)
]
such that
[
1\le |N|<\infty,\qquad 1\le |S|<\infty,
]
for every (i\in N) and (s\in S),
[
1\le |A_i(s)|<\infty,
]
for every (s\in S) and action profile
[
a\in A(s):=\prod*{j\in N}A_j(s),
]
the stage payoff satisfies
[
u_i(s,a)\in[0,1]\quad\text{for each }i\in N,
]
and
[
P(\cdot\mid s,a)\in \Delta(S).
]

For each (t\in\mathbb N_{>0}), define the set of public histories of length (t) by
[
H_t(G):=
\left{
(s_1,a_1,s_2,a_2,\dots,s_{t-1},a_{t-1},s_t)
:
s_k\in S,\ a_k\in A(s_k)
\right}.
]

For each player (i\in N), let (\Sigma_i(G)) be the set of all behavioral strategies
[
\sigma_i:\bigcup_{t\ge 1} H_t(G)\to \bigcup_{s\in S}\Delta(A_i(s))
]
such that whenever (h_t\in H_t(G)) ends at state (s_t), one has
[
\sigma_i(h_t)\in \Delta(A_i(s_t)).
]
Let
[
\Sigma(G):=\prod_{i\in N}\Sigma_i(G).
]

For (G\in\mathfrak G), (T\in\mathbb N_{>0}), (s_1\in S), (\sigma\in\Sigma(G)), and (i\in N), define the expected (T)-stage average payoff
[
\gamma_i^T(G,s_1,\sigma)
:=
\mathbb E_{G,s_1,\sigma}!\left[\frac1T\sum_{t=1}^{T}u_i(s_t,a_t)\right].
]

Define that (\sigma\in\Sigma(G)) is a **uniform (\varepsilon)-equilibrium** iff
[
\exists T_0\in\mathbb N_{>0}\ \forall T\in\mathbb N_{>0},
\Bigl(
T\ge T_0 \Rightarrow
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G),\
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon
\Bigr).
]

Equivalently, define
[
\operatorname{HasUniformEq}(G)
:\iff
\forall \varepsilon\in\mathbb R_{>0}\ \exists \sigma\in\Sigma(G)\ \exists T_0\in\mathbb N_{>0}
]
such that
[
\forall T\in\mathbb N_{>0},
\Bigl(
T\ge T_0 \Rightarrow
\forall s_1\in S\ \forall i\in N\ \forall \tau_i\in\Sigma_i(G),\
\gamma_i^T(G,s_1,\sigma)\ge
\gamma_i^T(G,s_1,(\tau_i,\sigma_{-i}))-\varepsilon
\Bigr).
]

Then the informal claim is formalized as the open question whether
[
\forall G\in\mathfrak G,\ \operatorname{HasUniformEq}(G)
]
is true. This is the clean strategy-existence formalization selected in the request packet and the durable claim source.  

## User assumptions

The following assumptions are directly fixed by the request packet and durable claim source.  

* [USER] The model class is the class of finite stochastic games with finitely many players, finitely many states, and finitely many action sets.
* [USER] The state is publicly observed at each stage.
* [USER] Actions are chosen simultaneously at each stage.
* [USER] The transition law is a fixed kernel depending only on the current state and current action profile.
* [USER] Strategies are behavioral strategies defined on public histories.
* [USER] Stage payoffs are bounded and normalized to ([0,1]).
* [USER] The payoff criterion of the target claim is expected finite-horizon average payoff.
* [USER] The equilibrium notion is approximate Nash equilibrium against unilateral deviations.
* [USER] Uniformity means one fixed strategy profile works for every sufficiently large horizon (T).
* [USER] The equilibrium inequalities are required for every initial state (s_1\in S).
* [USER] The intended formal target is existence of uniform (\varepsilon)-equilibria for every (\varepsilon>0), rather than the payoff-set wording.

## Added assumptions

* [ASSUMPTION+] (N\neq\varnothing), (S\neq\varnothing), and (A_i(s)\neq\varnothing) for all (i,s). Justification: otherwise the game may fail to be playable and the probability simplices (\Delta(A_i(s))) may be empty.
* [ASSUMPTION+] (\Delta(X)) denotes the set of probability measures on the finite set (X). Justification: this is needed to state the codomains of (P) and (\sigma_i) explicitly.
* [ASSUMPTION+] (\mathbb E_{G,s_1,\sigma}) is the expectation under the unique law on plays induced by (G), deterministic initial state (s_1), and profile (\sigma). Justification: this makes (\gamma_i^T) well-defined.
* [ASSUMPTION+] Horizons range over positive integers (\mathbb N_{>0}). Justification: the expression (1/T) excludes (T=0).

## Scope ambiguities

The following alternative readings exist in the literature; the adopted reading is the one preferred in the supplied materials.  

* [SCOPE] “Uniform equilibrium” could mean an exact equilibrium ((\varepsilon=0)) or, as adopted above, existence of a uniform (\varepsilon)-equilibrium for every (\varepsilon>0).
* [SCOPE] The claim could be phrased as existence of a uniform equilibrium payoff rather than existence of a strategy profile. The adopted target is the strategy-existence statement.
* [SCOPE] Some formulations quantify relative to a fixed initial state or an initial distribution. The adopted statement quantifies over every initial state (s_1\in S).
* [SCOPE] Some formulations restrict strategies to stationary, Markov, or finite-memory strategies. No such restriction is part of the adopted statement.
* [SCOPE] Some models allow private monitoring or signal structures. The adopted statement uses perfect public monitoring only.
* [SCOPE] Some models add an external public randomization device. The adopted statement does not augment the game with such an extra device.
* [SCOPE] Discounted payoff appears in the background discussion, but not in the target statement. The adopted claim is solely about expected finite-horizon average payoff.

The durable proof-state source is bootstrap / clean-slate, so no additional theorem-side hypotheses were imported from earlier project passes.

## FILE: claim.md

# Original Claim

# Uniform Equilibrium in Finite Stochastic Games (Open Problem, Neyman)

## 0. The canonical one-line statement (the “template”)

> **Open problem (Neyman).** Does every stochastic game with finitely many players, states, and actions have a **uniform equilibrium**?

**Where it is stated online:** the Game Theory Society (Israel chapter) lists it under “Open Problems,” suggested by Abraham Neyman.  
Reference page: https://sites.google.com/view/thegametheorysocietyilchapter/open-problems

**Baseline definitions:** the Wikipedia page on *stochastic games* gives the standard model and terminology that most authors mean by “finite stochastic game.”  
Reference page: https://en.wikipedia.org/wiki/Stochastic_game

This document rewrites the problem in a proof-oriented way: clear formalization, what counts as a solution, and concrete research directions.

---

## 1. What is the problem?

A **finite stochastic game** (also called a finite-state Markov game) is a repeated interaction in which a publicly observed **state** changes stochastically as a function of current actions. At each stage:

1. the current state is observed by all players
2. players choose actions simultaneously
3. players receive payoffs
4. the state transitions according to a fixed kernel

The question asks whether, in full generality (arbitrary finite number of players, finite state/action spaces), there always exists a strategy profile that is an approximate Nash equilibrium **uniformly for all sufficiently long horizons**, in the sense of the *long-run average payoff*.

Intuition: for large horizons, players should be able to play “almost optimally” against deviations without needing to tune their strategy to the exact horizon length. The uniformity requirement is exactly that “no tuning needed” property.

---

## 2. The formal model

### 2.1 Game data

A finite stochastic game is a tuple
\[
G = (N, S, (A_i)_{i\in N}, u, P)
\]
where:

- **Players**: \(N = \{1,\dots,n\}\) is finite.
- **States**: \(S\) is finite. The state is publicly observed each stage.
- **Actions**: for each player \(i\) and state \(s\), the action set \(A_i(s)\) is finite.
- **Stage payoffs**: for each player \(i\),
  \[
  u_i : \bigcup_{s\in S} \{s\}\times \prod_{j\in N} A_j(s) \to [0,1].
  \]
  (Bounded payoffs; the range \([0,1]\) is WLOG via affine scaling.)
- **Transitions**: for each state \(s\) and action profile \(a\in\prod_{j} A_j(s)\),
  \[
  P(\cdot\mid s,a) \in \Delta(S)
  \]
  is a probability distribution over next states.

### 2.2 Play, histories, and strategies

Let the public history at stage \(t\) be
\[
h_t = (s_1, a_1, s_2, a_2, \dots, s_t) .
\]

A **behavioral strategy** for player \(i\) is a map \(\sigma_i\) assigning, after each history \(h_t\), a distribution over \(A_i(s_t)\):
\[
\sigma_i(\cdot \mid h_t) \in \Delta(A_i(s_t)).
\]
A strategy profile is \(\sigma=(\sigma_1,\dots,\sigma_n)\).

---

## 3. Payoff criteria and equilibrium notions

There are two common payoff criteria: **finite-horizon average payoff** and **discounted payoff**. The open problem is fundamentally about the *uniform long-run average* notion, but discounted analysis is a major technical/computational tool.

### 3.1 Finite-horizon average payoff

For horizon \(T\ge 1\), define the expected average payoff of player \(i\), starting from initial state \(s_1\), under profile \(\sigma\):
\[
\gamma_i^T(s_1,\sigma)
=
\mathbb{E}_{s_1,\sigma}\left[ \frac{1}{T}\sum_{t=1}^{T} u_i(s_t,a_t) \right].
\]

### 3.2 ε-equilibrium for fixed horizon T

A strategy profile \(\sigma\) is an **\(\varepsilon\)-Nash equilibrium for horizon \(T\)** if for every player \(i\), every initial state \(s_1\), and every deviation strategy \(\tau_i\),
\[
\gamma_i^T(s_1,\sigma)
\ge
\gamma_i^T(s_1,(\tau_i,\sigma_{-i})) - \varepsilon.
\]

### 3.3 Uniform ε-equilibrium (strategy)

A strategy profile \(\sigma\) is a **uniform \(\varepsilon\)-equilibrium** if there exists some \(T_0\) such that for all \(T\ge T_0\), \(\sigma\) is an \(\varepsilon\)-equilibrium for horizon \(T\). Formally:
\[
\exists T_0\ \forall T\ge T_0:\ 
\forall i,\forall s_1,\forall \tau_i:\
\gamma_i^T(s_1,\sigma)
\ge
\gamma_i^T(s_1,(\tau_i,\sigma_{-i})) - \varepsilon.
\]

### 3.4 The open problem (existence form)

> **Uniform equilibrium existence problem (Neyman).**  
> For every finite stochastic game \(G\) and every \(\varepsilon>0\), does there exist a strategy profile \(\sigma\) that is a **uniform \(\varepsilon\)-equilibrium**?

### 3.5 “Uniform equilibrium payoff” wording (payoff-set form)

Sometimes the problem is phrased as existence of a **uniform equilibrium payoff** (a payoff vector that can be achieved by strategies that are uniformly \(\varepsilon\)-equilibria for all \(\varepsilon>0\)). This is closely related, but when you write formal statements you should pick **one precise definition** and stick to it.

A common precise version is:

- For each \(\varepsilon>0\) there exists a uniform \(\varepsilon\)-equilibrium \(\sigma^{\varepsilon}\).
- Consider the set of limit points (as \(\varepsilon\to 0\)) of the induced payoff vectors. Any such limit is a “uniform equilibrium payoff.”

If your goal is a formal proof, the **existence of uniform \(\varepsilon\)-equilibria for all \(\varepsilon>0\)** is the cleanest target.

---

## 4. What counts as a solution?

### 4.1 A full “Yes” solution

A proof of the theorem:

> For every finite stochastic game \(G\) and every \(\varepsilon>0\), there exists a strategy profile \(\sigma\) and a horizon threshold \(T_0\) such that \(\sigma\) is an \(\varepsilon\)-equilibrium of the \(T\)-stage average-payoff game for every \(T\ge T_0\).

A complete write-up should include:

- a completely explicit definition of strategies used (often finite-memory)
- explicit bounds or at least a clearly defined \(T_0(\varepsilon)\) construction
- a deviation analysis showing each unilateral deviation gains at most \(\varepsilon\) for all \(T\ge T_0\)

### 4.2 A full “No” solution (counterexample)

To refute the statement, you must produce:

- an explicit finite game \(G\) (finite players, states, actions; explicit payoffs and transitions),
- an explicit \(\varepsilon_0>0\),
- and a proof that **no** strategy profile is a uniform \(\varepsilon_0\)-equilibrium.

Formally, you must show:

\[
\exists \varepsilon_0>0\ \forall \sigma\ \forall T_0\ \exists T\ge T_0\ \exists i, s_1, \tau_i:
\gamma_i^T(s_1,(\tau_i,\sigma_{-i})) > \gamma_i^T(s_1,\sigma) + \varepsilon_0.
\]

### 4.3 Partial solutions that still “count” scientifically

Even without settling the full question, any of the following are meaningful progress:

- prove existence for a large subclass (absorbing games, special transition graphs, etc.)
- prove structural lower bounds on any counterexample (minimum number of states/actions, required recurrence structure)
- prove equivalences or reductions to other open conjectures
- develop proof techniques that unify the known 2-player existence proofs with partial n-player results

---

## 5. Concrete ways to attack the problem

Below are **two complementary tracks**: a constructive proof track and a counterexample track. In practice, research often alternates between them.

### Track A: Prove existence (construct uniform strategies)

A common architecture:

1. **Decompose the state space** into transient and recurrent components under candidate behavior.
2. Construct a strategy with **phases**:
   - “play” phases meant to generate target payoffs,
   - “monitoring/test” phases detecting deviations,
   - “punishment” phases restoring incentives,
   - “reset” phases returning to the main regime.
3. Prove that for large horizons \(T\), the expected time spent in monitoring/punishment is negligible (\(o(T)\)), while still deterring deviations by making deviation detection sufficiently likely and punishment sufficiently costly.
4. Show the same strategy works for every \(T\ge T_0\).

Key proof ingredients you might need:

- concentration bounds controlling empirical averages over long horizons
- martingale or optional stopping arguments (especially for state visitation counts)
- bounds on how much a unilateral deviator can alter the state distribution
- “self-generation” arguments: a set of continuation payoffs closed under equilibrium incentives

### Track B: Find a counterexample (prove uniformity fails)

If the general theorem is false, a counterexample likely relies on a robust “tuning obstruction”:

- equilibrium behavior must depend sensitively on \(T\) (or \(\delta\)) to satisfy incentives,
- no single strategy profile can satisfy all incentive constraints uniformly.

Promising failure mechanisms to search for:

1. **Endogenous block lengths**  
   Any \(\varepsilon\)-equilibrium for horizon \(T\) forces phases of expected length proportional to \(T\) (or varying with \(T\)), so a fixed strategy cannot work for all large \(T\).

2. **Cycling incentive constraints**  
   Which player has the profitable deviation changes with \(T\), producing “regret spikes” along an infinite subsequence \(T_k\).

3. **Equilibrium selection instability**  
   For each \(T\) there are equilibria, but any selection across \(T\) fails to stabilize and thus fails uniformity.

A counterexample proof typically needs a lemma like:

> For any profile \(\sigma\), either (A) \(\sigma\) spends enough time in regime R (creating a profitable deviation), or (B) it does not (creating a different profitable deviation).  
> Therefore \(\sigma\) cannot be uniformly \(\varepsilon\)-stable.

---

## 6. Computational workflow (search-plus-verify) that can support a proof

Even if your end goal is a proof, computation can:

- discover the right “gadget”
- suggest the correct invariant to prove
- rule out small parameter spaces (supporting minimality claims)

A practical workflow:

1. **Generate candidate games** under size bounds (e.g., 3 states, 2 actions), with:
   - payoffs on a small rational grid (0, 1/4, 1/2, 3/4, 1)
   - transitions with small denominators (1/2, 1/3, 2/3, …)

2. **Solve** for:
   - finite-horizon equilibria for many horizons \(T\)
   - discounted equilibria for many \(\delta\) close to 1

3. **Compute regret** of candidate strategy profiles:
   - For a fixed profile \(\sigma\), compute best-response value to each player via dynamic programming (a unilateral deviation becomes an MDP).
   - Define regret:
     \[
     \mathrm{Regret}_{i,T}(\sigma) =
     \max_{\tau_i} \gamma^T_i(s_1,(\tau_i,\sigma_{-i})) - \gamma^T_i(s_1,\sigma).
     \]
   - Uniform \(\varepsilon\)-equilibrium means: there exists \(T_0\) with \(\mathrm{Regret}_{i,T}(\sigma)\le \varepsilon\) for all \(i\) and all \(T\ge T_0\).

4. **Look for signatures**:
   - regret does not go to 0 as \(T\to\infty\)
   - regret spikes along subsequences
   - equilibrium strategies exhibit cycling or phase lengths scaling with \(T\)

5. **Extract a proof candidate**:
   - identify a structural lemma that explains the spikes/cycling
   - prove it abstractly from the game’s transition/payoff structure

---

## 7. Promising directions (high-level roadmap)

1. **Clarify minimal counterexample structure**  
   Prove lower bounds: a counterexample (if it exists) must have at least \(k\) states or must contain a strongly connected nonabsorbing component of a certain type.

2. **Strengthen existence results for subclasses**  
   Try to enlarge known positive classes by relaxing assumptions one at a time (absorbing → almost absorbing → communicating under public randomization, etc.).

3. **Discounted-to-uniform bridges**  
   Prove robust links between equilibrium payoff behavior as \(\delta\to 1\) and uniform equilibria for average payoff.

4. **Finite-memory sufficiency (or insufficiency)**  
   Investigate whether uniform \(\varepsilon\)-equilibria can always be taken to have bounded memory as a function of \(\varepsilon\) and game size. A negative result here could hint at counterexamples.

---

## 8. Lean-style formalization blueprint (what you’d need to encode)

This is a **blueprint**, not a working library, but it’s the level of structure that makes the open problem precise enough to “compile as a goal.”

### 8.1 Core objects (pseudocode)

```lean
namespace StochGame

-- Finite stochastic game with perfect monitoring.
structure FinGame where
  Player : Type
  [fPlayer : Fintype Player] [dPlayer : DecidableEq Player]

  State : Type
  [fState : Fintype State] [dState : DecidableEq State]

  Action : Player → State → Type
  [fAction : ∀ i s, Fintype (Action i s)]

  -- Action profile at a state: one action per player
  ActProf : State → Type := fun s => (i : Player) → Action i s

  -- Stage payoffs (bounded)
  u : Player → (s : State) → ActProf s → ℝ
  u_bdd : ∀ i s a, 0 ≤ u i s a ∧ u i s a ≤ 1

  -- Transition kernel on a finite set of states
  P : (s : State) → ActProf s → PMF State

-- Behavioral strategies (history-dependent)
def Strat (G : FinGame) (i : G.Player) : Type :=
  ∀ (t : Nat), (Hist G t) → PMF (G.Action i (stateOf ·))

def Prof (G : FinGame) : Type := (i : G.Player) → Strat G i

-- Expected average payoff for horizon T
def avgPayoff (G : FinGame) (T : Nat) (s₁ : G.State) (σ : Prof G) (i : G.Player) : ℝ := by
  -- via induced probability measure on length-T plays
  admit

-- ε-equilibrium at horizon T
def isEpsEq_T (G : FinGame) (ε : ℝ) (T : Nat) (σ : Prof G) : Prop :=
  ∀ (s₁ : G.State) (i : G.Player) (τi : Strat G i),
    avgPayoff G T s₁ σ i ≥ avgPayoff G T s₁ (update σ i τi) i - ε

-- Uniform ε-equilibrium
def isUniformEpsEq (G : FinGame) (ε : ℝ) (σ : Prof G) : Prop :=
  ∃ T₀ : Nat, ∀ T ≥ T₀, isEpsEq_T G ε T σ

-- Existence statement (the open problem)
def HasUniformEq (G : FinGame) : Prop :=
  ∀ ε > 0, ∃ σ : Prof G, isUniformEpsEq G ε σ
```

### 8.2 The open problem as a Lean goal

```lean
theorem UniformEquilibrium_exists_for_all_finite_stochastic_games :
  ∀ (G : FinGame), HasUniformEq G := by
  -- open in general
  admit
```

### 8.3 What a conditional “compilable” proof would look like

To make real progress in Lean, you typically:

1. define a key invariant or operator (e.g., self-generation of payoff sets)
2. prove “Invariant ⇒ HasUniformEq”
3. focus mathematical work on proving the invariant

```lean
axiom selfGenerating (G : FinGame) : Prop

axiom selfGenerating_implies_uniform :
  ∀ G, selfGenerating G → HasUniformEq G

theorem UniformEquilibrium_from_selfGenerating :
  ∀ G, selfGenerating G → HasUniformEq G :=
by intro G h; exact selfGenerating_implies_uniform G h
```

This already “compiles” once you define objects, and it cleanly states what remains.

### 8.4 What a counterexample theorem would look like

```lean
def isCounterexample (G : FinGame) (ε : ℝ) : Prop :=
  ε > 0 ∧ (∀ σ : Prof G, ¬ isUniformEpsEq G ε σ)

theorem exists_counterexample :
  ∃ (G : FinGame) (ε : ℝ), isCounterexample G ε := by
  admit
```

A fully formal negative resolution would additionally provide an explicit `G`.

---

## 9. What to submit as “done”

### A finished “Yes” solution includes
- theorem statement (uniform \(\varepsilon\)-equilibria exist for all \(\varepsilon>0\))
- explicit strategy construction
- deviation bound proof uniform in \(T\)

### A finished “No” solution includes
- explicit finite game specification \((N,S,A,u,P)\)
- explicit \(\varepsilon_0>0\)
- proof that every strategy fails uniform \(\varepsilon_0\)-equilibrium requirements

---

## References
- Neyman open problem listing: https://sites.google.com/view/thegametheorysocietyilchapter/open-problems  
- Definitions and background: https://en.wikipedia.org/wiki/Stochastic_game

---
## ADDITIONAL LOADED FILES

### branches/main/context/literature.md

# Literature Output

Generated: 2026-03-23T02:33:21.350658+00:00

The request packet adopts the strong strategy-existence formulation: for every (\varepsilon>0), one behavioral profile (\sigma) must be an (\varepsilon)-equilibrium for all sufficiently large finite horizons (T), uniformly over all initial states and unilateral deviations. Much of the literature instead phrases results as existence of a “uniform/undiscounted equilibrium payoff,” so the right reading rule is: use payoff-form results as evidence and as technique guides, but do not silently identify them with the packet’s exact quantifier structure unless the paper makes that implementation explicit.  

## Status

* [LIT] The general finite-player, finite-state, finite-action, perfect-public-monitoring problem is still open as of March 2026. The Game Theory Society still lists Neyman’s problem, Solan’s 2022 text says the existence of a uniform equilibrium payoff for every stochastic game is still open, and Solan–Vieille’s December 2025 paper describes it as one of the main open problems in game theory. ([Google Sites][1])
* [LIT] In some subclasses, payoff language is close to the packet’s target. For positive recursive absorbing games, Solan–Vieille define a uniform equilibrium payoff by requiring that for every (\varepsilon>0) there is one strategy profile that is an (\varepsilon)-equilibrium in all sufficiently long finite-horizon games and yields payoff within (\varepsilon) of the target; they also note that, in that class, this coincides with the undiscounted-payoff notion. That equivalence is local to the subclass, not a general theorem for the full claim. ([arXiv][2])

## Positive results closest to the target

* [LIT] The discounted foothold is classical. Shapley proved the two-player zero-sum discounted finite-state result, and later surveys emphasize the stationary-equilibrium extension to finite discounted stochastic games. This discounted existence is the usual launchpad for long-run arguments, but it is much weaker than the packet’s uniform finite-horizon requirement. ([TAU Math][3])
* [LIT] Two-player zero-sum finite stochastic games do have the uniform value. Solan’s book states Theorem 9.13, “Every two-player zero-sum stochastic game has a uniform value,” and the proof uses the limit (v_0(s)=\lim_{\lambda\to0}v_\lambda(s)), semi-algebraic selection of stationary discounted optimal strategies, and a potential/submartingale argument based on (v_0(s_t)). ([TAU Math][4])
* [LIT] Two-player non-zero-sum finite stochastic games are also settled positively. Vieille’s 2000 program first reduces the general two-player problem to positive absorbing recursive games, then proves existence for that class. Closely related work explicitly says that rare-transition perturbation theory for Markov chains is one of the proof ingredients, and Solan shows existence when the game has at most two nonabsorbing states. ([Springer][5])
* [LIT] Beyond two players, the literature is a patchwork of positive classes rather than a general theorem: every three-player absorbing game has a uniform equilibrium payoff; every absorbing team game has an equilibrium payoff and (\varepsilon)-equilibria with cyclic structure; every multiplayer stochastic game admits an autonomous correlated equilibrium payoff; and Solan–Vieille (2025) prove uniform/undiscounted equilibrium payoff existence for positive recursive absorbing games with no rectangular nonabsorbing component, while citing a companion public-correlation result for all positive recursive stochastic games. ([TAU Math][6])
* [LIT] A weaker but structurally important theorem is “easy initial state” / “(\varepsilon)-solvable subgame”: for every (\varepsilon>0) there exists some subgame that admits an (\varepsilon)-equilibrium. Flesch–Solan recover this in great generality via the Martin-function machinery and trace the long-run-average finite-state antecedents to Thuijsman–Vrieze and Vieille. This isolates the exact gap between local solvability and the project’s global all-initial-states target. ([arXiv][7])
* [LIT] Nearby but outside the packet’s exact model, Solan notes that the continuous-time version was solved by Neyman (2017) via an adaptation of extensive-form correlated equilibrium. That is a real positive beacon, but it does not settle the discrete-time conjecture here. ([TAU Math][8])

## Proof techniques and approaches that recur in the literature

* [LIT] A useful taxonomy comes from Solan’s modified-game paper: successful special-case proofs have used vanishing discount, graph-theoretic tools, modified games, dynamical systems, and topological methods. That is the right map of the field. ([arXiv][9])
* [LIT] The classical absorbing-game engine is vanishing discount plus case analysis. Solan’s thesis describes the Vrieze–Thuijsman route: start from a limit of discounted equilibria, split into cases according to the limit mixed action, then add threats, perturbations, statistical tests, and punishments. Solan’s later exposition of two-player absorbing games says the constructed uniform (\varepsilon)-equilibrium has exactly three moving parts: equilibrium play, statistical tests, and punishment strategies. Applicability to the project: high if one can reduce to an absorbing or nearly-absorbing core. Difficulty: very high once there are many players and many nonabsorbing states. 
* [LIT] Rare-transition perturbation analysis is part of Vieille’s two-player toolkit. The “Small perturbations and stochastic games” paper says explicitly that it imports rare-transition Markov-chain theory and that the results are used in the proof of existence of equilibrium payoffs in two-player stochastic games. Applicability: promising for controlling occupation measures and long blocks. Difficulty: extreme in multiplayer settings, because punishers themselves are strategic. ([Springer][10])
* [LIT] Auxiliary and modified games are one of the most natural multiplayer-native routes. Solan’s thesis uses an auxiliary game that caps nonabsorbing payoffs by minmax levels; the later modified-game paper defines a general statewise modified game, proves stationary equilibria in it, and uses it to obtain uniform (\varepsilon)-equilibrium in a restricted strongly controllable class. Applicability: excellent as a proof architecture for the packet’s target. Difficulty: very high, but probably among the most plausible routes for genuine multiplayer progress. 
* [LIT] The Martin-function program is the strongest current general-purpose local-incentive technology. Flesch–Solan attach an auxiliary one-shot game to every history via a Martin function and derive subgame (\varepsilon)-maxmin strategies, minmax (\varepsilon)-acceptable profiles, extensive-form correlated (\varepsilon)-equilibria, and (\varepsilon)-solvable subgames. Applicability: excellent for history-sensitive deviation control. Limitation: it still stops short of one uncorrelated profile that is a Nash (\varepsilon)-equilibrium for all large horizons and all initial states. Difficulty: very high. ([arXiv][7])
* [LIT] The most interesting recent multiplayer existence mechanism is the 2025 self-map/orbit method. Solan–Vieille define a map (f) on continuation payoffs, prove that each node (w) yields a finite-horizon (\varepsilon)-equilibrium block (\sigma(w)) with positive absorption probability, then use a finite orbit of (f) to concatenate blocks into a global construction. Applicability: very strong conceptual candidate for the project, because it turns uniformity into an invariant-orbit problem on continuation payoffs. Difficulty: extreme outside the single-nonabsorbing-state world. ([arXiv][2])
* [LIT] Correlation and endogenous randomization are recurring escape hatches. Solan–Vieille prove autonomous correlated equilibrium payoffs in full generality; the 2025 companion result adds public correlation for positive recursive stochastic games; and jointly controlled lotteries show that in some quitting-game settings one can simulate public randomization internally. Applicability: strong, especially as a two-step route “prove correlated existence first, then internalize randomness.” Difficulty: extreme, because internalization must preserve incentives in every relevant public state. ([TAU Math][11])

## Counterexamples and obstructions to nearby statements

* [LIT] A stronger goal fails already nearby: subgame-perfect (\varepsilon)-equilibrium need not exist. Flesch–Solan emphasize that some stochastic games have no single profile inducing an (\varepsilon)-equilibrium in all subgames simultaneously. So one should not expect to prove the packet’s claim by first proving a blanket subgame-perfect theorem and then weakening it. ([arXiv][7])
* [LIT] Exact equilibrium is also too much as a generic target. The same paper states that none of its broad existence results survives at (\varepsilon=0), with counterexamples already in two-player zero-sum long-run-average games. This strongly supports the packet’s choice to ask for uniform (\varepsilon)-equilibria for every (\varepsilon>0) rather than exact uniform equilibrium. ([arXiv][7])
* [LIT] Naive discounted-limit arguments are dangerous. Solan’s book records Sorin’s example where the stationary discounted equilibrium payoff is a single point for every discount factor, yet that point is not a uniform equilibrium payoff. Renault–Ziliotto show that even in two-player observed-state stochastic games the full set of equilibrium payoffs can diverge as patience grows, robustly under perturbations and normal-form correlation. So “discounted equilibria converge, therefore uniform equilibrium exists” is not a valid theorem schema. ([TAU Math][4])
* [LIT] Restricted strategy classes fail even inside absorbing games. Solan’s thesis reports a three-player absorbing example with no stationary uniform (\varepsilon)-equilibrium profile and a four-player absorbing example with no perturbed uniform equilibrium payoff; the team-games result emphasizes cyclic (\varepsilon)-equilibria; and a four-player quitting game has a simplest equilibrium of period two. This is strong evidence that any general proof will have to tolerate richer, explicitly history-dependent, possibly periodic constructions. 
* [LIT] Several nearby generalizations are outright false. Hidden stochastic games can fail to have a uniform value, with counterexamples even in blind stochastic games, and zero-sum stochastic games with compact action sets can fail to have any asymptotic value. These are outside the packet’s scope, but they show that perfect public monitoring and finite action sets are structural, not cosmetic. ([arXiv][12])

## Difficulty assessment and best routes

* [LIT] Difficulty: extreme. Existing positive proofs beyond two players are heavily class-specific, the literature repeatedly remarks that uniform (\varepsilon)-equilibria are usually quite complex, and the known obstruction results eliminate many tempting simplifications at once: stationary, perturbed, subgame-perfect, or blindly discounted-limit constructions are all too crude in general. ([TAU Math][13])
* [LIT] The most promising positive route is a hybrid of modified-game and self-generating-orbit ideas: use a statewise auxiliary game to enforce minmax-compatible continuation values, then seek a finite or periodic invariant structure of continuation payoffs that can be concatenated into one horizon-robust profile. This is an inference from the pattern of successful proofs, not a published theorem. ([arXiv][14])
* [LIT] The most promising technical ingredient for deviation control is the Martin-function/identification-of-the-deviator machinery, because the hardest part of the packet’s target is not merely generating good payoffs but making one profile deviation-resistant uniformly across long horizons and histories. This, too, is an inference from the present toolkit rather than a settled reduction theorem. ([arXiv][7])
* [LIT] The sharpest counterexample template suggested by the literature is a (\ge 4)-player absorbing/quitting gadget with a tuning obstruction: any fixed monitoring or punishment intensity is either too weak to deter some deviation or too costly to sustain the intended payoff. The periodic and non-perturbed examples make this route look plausible, but no published result currently upgrades that heuristic into a full counterexample to the general conjecture. ([TAU Math][15])
* [LIT] Bottom line: the literature gives sturdy anchors in two-player games, a growing list of multiplayer subclasses, and several real proof machines. But the missing step is exactly the hard one: turning local, correlated, or subclass existence into one uncorrelated behavioral profile that works for all sufficiently large finite horizons and all initial states. The sources above strongly support treating the conjecture as genuinely open and technically formidable, and they do not by themselves certify a proof of the packet’s full statement. ([Google Sites][1])

[1]: https://sites.google.com/view/thegametheorysocietyilchapter/open-problems?utm_source=chatgpt.com "Open Problems"
[2]: https://arxiv.org/pdf/2512.04306?utm_source=chatgpt.com "Undiscounted Equilibrium in Positive Recursive Absorbing Games with Non-Rectangular Absorption Structure"
[3]: https://www.math.tau.ac.il/~eilons/discount.pdf?utm_source=chatgpt.com "Discounted Stochastic Games"
[4]: https://www.math.tau.ac.il/~eilons/book.pdf?utm_source=chatgpt.com "https://www.math.tau.ac.il/~eilons/book.pdf"
[5]: https://link.springer.com/content/pdf/10.1007/BF02810663.pdf?utm_source=chatgpt.com "Two-player stochastic games I: A reduction"
[6]: https://www.math.tau.ac.il/~eilons/threeA.htm?utm_source=chatgpt.com "Discounted Stochastic Games"
[7]: https://arxiv.org/pdf/2208.12096?utm_source=chatgpt.com "https://arxiv.org/pdf/2208.12096"
[8]: https://www.math.tau.ac.il/~eilons/book.pdf "https://www.math.tau.ac.il/~eilons/book.pdf"
[9]: https://arxiv.org/pdf/1703.04026?utm_source=chatgpt.com "https://arxiv.org/pdf/1703.04026"
[10]: https://link.springer.com/article/10.1007/bf02810665?utm_source=chatgpt.com "Small perturbations and stochastic games - Springer Nature"
[11]: https://www.math.tau.ac.il/~eilons/correlA.htm?utm_source=chatgpt.com "Discounted Stochastic Games"
[12]: https://arxiv.org/pdf/2602.06480?utm_source=chatgpt.com "Approximating the Uniform Value in Hidden Stochastic ..."
[13]: https://www.math.tau.ac.il/~eilons/acceptable_published.pdf "https://www.math.tau.ac.il/~eilons/acceptable_published.pdf"
[14]: https://arxiv.org/pdf/1703.04026 "https://arxiv.org/pdf/1703.04026"
[15]: https://www.math.tau.ac.il/~eilons/thesis.pdf?utm_source=chatgpt.com "https://www.math.tau.ac.il/~eilons/thesis.pdf"

