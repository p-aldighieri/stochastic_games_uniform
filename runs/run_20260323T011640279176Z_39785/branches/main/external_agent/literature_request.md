# External Agent Request (literature)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-23T02:33:21.349723+00:00

## Instructions

Survey relevant known theorems, techniques, and proof approaches. Tag evidence with [LIT]. Identify applicable proof techniques and assess difficulty. Note known counterexamples to related statements. Do not claim proof validity from retrieval alone.

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

