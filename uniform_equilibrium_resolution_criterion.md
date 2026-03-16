# Resolution Criteria for Neyman’s Uniform Equilibrium Problem (Lean Contract)

## 1. Purpose of this document

This is a **precision spec** for what it means to “solve” the open problem:

> **Does every finite stochastic game have a uniform equilibrium?** (Suggested by Abraham Neyman)

The key idea: a genuine affirmative resolution should be checkable by a **mechanical compilation criterion** in Lean. This document states:

1) the exact mathematical statement to be proved (with quantifiers made explicit),  
2) a Lean formalization target that is *strong enough to be meaningful* and *precise enough to compile*,  
3) what a finished Lean proof repository must satisfy (no `sorry`, no new axioms), and  
4) what does **not** count (common loopholes).

This document is designed to be used as a “contract”: if a Lean project satisfies the acceptance criteria below, then the problem is considered solved in the affirmative.

---

## 2. Mathematical statement (affirmative resolution criterion)

### 2.1 Model: finite stochastic game with perfect monitoring

A **finite stochastic game** consists of:

- a finite player set `N = {1, …, n}` with `n ≥ 1`,
- a finite state space `S`,
- for each player `i` and state `s`, a finite action set `A_i(s)`,
- bounded stage payoffs `u_i(s, a)` where `a ∈ Π_j A_j(s)` and `u_i(s,a) ∈ [0,1]`,
- a transition kernel `P(· | s, a)` which is a probability distribution on `S`.

At each stage `t = 0, 1, 2, …`:

1) the current state `s_t` is publicly observed,  
2) players simultaneously choose actions `a_{i,t} ∈ A_i(s_t)`,  
3) each player receives payoff `u_i(s_t, a_t)`,  
4) the next state `s_{t+1}` is drawn from `P(· | s_t, a_t)`.

Players observe all states and actions (perfect monitoring), and strategies may be fully history-dependent and randomized.

### 2.2 Histories and behavioral strategies

Let `h_t` denote the public history through time `t` (states and actions up to the current state).  
A **behavioral strategy** for player `i` maps each time `t` and history `h_t` to a distribution over `A_i(s_t)`.

### 2.3 Finite-horizon average payoff

For horizon `T ≥ 1`, the average payoff of player `i` from initial state `s_0` under strategy profile `σ` is

\[
\gamma_i^T(s_0, σ)
=
\mathbb{E}_{s_0,σ}\!\left[\frac{1}{T}\sum_{t=0}^{T-1} u_i(s_t, a_t)\right].
\]

### 2.4 ε-equilibrium at horizon T

A strategy profile `σ` is an **ε-Nash equilibrium for horizon T** (for the `T`-stage average payoff game) if

\[
\forall i,\ \forall s_0,\ \forall τ_i:\ 
\gamma_i^T(s_0, σ)\ \ge\ \gamma_i^T(s_0, (τ_i, σ_{-i})) - ε.
\]

Here `τ_i` ranges over all (possibly randomized, history-dependent) deviations.

### 2.5 Uniform ε-equilibrium

A strategy profile `σ` is a **uniform ε-equilibrium** if there exists `T₀` such that for every `T ≥ T₀`, `σ` is an ε-equilibrium for horizon `T`:

\[
\exists T₀\ \forall T\ge T₀:\ 
\forall i,\forall s_0,\forall τ_i:\ 
\gamma_i^T(s_0, σ)\ \ge\ \gamma_i^T(s_0, (τ_i, σ_{-i})) - ε.
\]

### 2.6 The open problem as a single quantified statement

An **affirmative resolution** proves the following theorem:

\[
\forall G,\ \forall ε>0,\ \exists σ,\ \exists T₀,\ 
\forall T\ge T₀,\ \forall i,\ \forall s_0,\ \forall τ_i:\ 
\gamma_i^T(s_0, σ)\ \ge\ \gamma_i^T(s_0, (τ_i, σ_{-i})) - ε.
\]

Interpretation: for every finite stochastic game and every tolerance `ε`, there exists a *single* strategy profile that is an approximate equilibrium for *all sufficiently long horizons*.

---

## 3. What does and does not count as “solving it”?

### 3.1 What counts (affirmative)

A solution counts if it provides:

1) **A fully formal Lean statement** expressing the theorem above for the standard model (finite players, states, actions; perfect monitoring; behavioral strategies; finite-horizon average payoffs).

2) **A Lean proof term** of that theorem that:
   - compiles with Lean 4 + mathlib,
   - contains **no `sorry`**,
   - contains **no new `axiom` / `constant`** declarations used to bypass the proof,
   - does not trivialize the statement by weakening definitions (see 3.2).

3) A build script or instructions so that an external verifier can run:
   - `lake build` (or `lean --make` equivalent),
   - a “no sorry” check,
   - an “axiom audit” check (see Section 6).

### 3.2 What does not count (common loopholes)

The following do **not** count as solving the problem:

- Proving existence only for:
  - stationary strategies,
  - Markov strategies,
  - pure strategies,
  - equilibria that depend on the horizon `T`,
  - equilibria that depend on `ε` but not uniformly in `T`.

- Changing the payoff criterion (for example, discounted payoffs only) unless you *also* prove it implies the uniform finite-horizon average-payoff criterion.

- Restricting deviations to a smaller class than “all behavioral strategies”.

- Using `axiom`/`constant` to assert existence of equilibrium objects or key lemmas.

- Defining “uniform equilibrium” as a vacuous predicate (for example by setting all payoffs to 0 by definition, or defining `γ` to ignore the strategy profile).

---

## 4. Lean target: the exact proposition that must be proved

This section specifies a Lean proposition `UniformEquilibriumConjecture : Prop`.  
**Solving the open problem in Lean** means constructing a theorem:

```lean
theorem uniform_equilibrium_exists :
  UniformEquilibriumConjecture := by
  -- complete proof here (no sorry)
```

### 4.1 Design choices (to avoid ambiguity)

To keep the formalization faithful and checkable:

- **Finiteness** is represented by `Fintype` instances.
- **Randomization** is represented by `ProbabilityTheory.PMF` (probability mass functions) on finite types.
- **Strategies** are behavioral: functions of time and full public history.
- **Average payoff** is defined for each finite horizon `T` via an explicit expectation over the induced finite play distribution.

This is strong enough to rule out most loopholes and is close to standard textbook definitions.

---

## 5. Lean code skeleton: definitions + conjecture (no axioms, no sorry)

Below is a *spec-level* Lean file outline that should compile once placed in a Lean 4 + mathlib project.  
It defines the objects needed to *state* the conjecture precisely.

### 5.1 File: `StochGame/UniformEq/Definitions.lean`

```lean
import Mathlib
import Mathlib.Probability.ProbabilityMassFunction

open scoped BigOperators
open Classical

namespace StochGame

/-- A finite stochastic game with perfect monitoring. -/
structure FinStochGame where
  Player : Type
  [fPlayer : Fintype Player]
  [dPlayer : DecidableEq Player]

  State : Type
  [fState : Fintype State]
  [dState : DecidableEq State]

  Action : Player → State → Type
  [fAction : ∀ i s, Fintype (Action i s)]
  [dAction : ∀ i s, DecidableEq (Action i s)]

  /-- Action profile at state `s`: one action per player. -/
  ActProf (s : State) : Type := (i : Player) → Action i s

  /-- Bounded stage payoff in [0,1]. -/
  u : Player → (s : State) → ActProf s → ℝ
  u_bdd : ∀ i s a, (0 ≤ u i s a) ∧ (u i s a ≤ 1)

  /-- Transition kernel as a probability mass function on the next state. -/
  P : (s : State) → ActProf s → ProbabilityTheory.PMF State

attribute [instance] FinStochGame.fPlayer FinStochGame.dPlayer
attribute [instance] FinStochGame.fState FinStochGame.dState
attribute [instance] FinStochGame.fAction FinStochGame.dAction

namespace FinStochGame

variable (G : FinStochGame)

/-- A stage record: the state at which actions were chosen, together with the action profile. -/
abbrev Stage : Type := Sigma G.ActProf  -- ⟨s, a⟩ where a : ActProf s

/-- Public history: current state plus the list of past stage records. -/
structure Hist where
  cur : G.State
  past : List G.Stage

/-- Extend a history by recording the current stage action profile and moving to `s'`. -/
def Hist.step (h : G.Hist) (a : G.ActProf h.cur) (s' : G.State) : G.Hist :=
  { cur := s', past := h.past ++ [⟨h.cur, a⟩] }

/-- Initial history at state `s0`. -/
def Hist.init (s0 : G.State) : G.Hist :=
  { cur := s0, past := [] }

/-- A behavioral strategy for player `i`. -/
def Strat (i : G.Player) : Type :=
  ∀ (t : Nat) (h : G.Hist), ProbabilityTheory.PMF (G.Action i h.cur)

/-- A strategy profile. -/
def Prof : Type := ∀ i : G.Player, G.Strat i

/-- The product distribution over action profiles induced by independent mixed actions. -/
def actProfDist (σ : G.Prof) (t : Nat) (h : G.Hist) :
    ProbabilityTheory.PMF (G.ActProf h.cur) :=
  ProbabilityTheory.PMF.pi (fun i : G.Player => σ i t h)

/-- One-step distribution over next histories induced by `σ` at time `t`. -/
def nextHistDist (σ : G.Prof) (t : Nat) (h : G.Hist) :
    ProbabilityTheory.PMF G.Hist :=
  (actProfDist (G:=G) σ t h).bind (fun a =>
    (G.P h.cur a).map (fun s' => G.Hist.step h a s')
  )

/-- Distribution of histories after `T` steps, starting from `h0`. -/
def histDist : Nat → G.Hist → G.Prof → ProbabilityTheory.PMF G.Hist
  | 0,     h0, σ => ProbabilityTheory.PMF.pure h0
  | (T+1), h0, σ => (histDist T h0 σ).bind (fun h => nextHistDist (G:=G) σ T h)

/-- Sum of realized stage payoffs for player `i` along a history's recorded past. -/
def payoffSum (i : G.Player) (h : G.Hist) : ℝ :=
  (h.past.map (fun sa => G.u i sa.1 sa.2)).sum

/-- Expected average payoff over horizon `T` (with convention `T=0` gives 0). -/
def avgPayoff (i : G.Player) (T : Nat) (s0 : G.State) (σ : G.Prof) : ℝ :=
  if hT : T = 0 then 0 else
    let dist := histDist (G:=G) T (G.Hist.init s0) σ
    dist.expect (fun h => (1 / (T : ℝ)) * payoffSum (G:=G) i h)

end FinStochGame

end StochGame
```

Remarks:

- This is purely definitional. It introduces **no axioms** and uses only mathlib structures.
- The key object is `avgPayoff`, which is a concrete expectation over a finitely-generated `PMF`.

### 5.2 File: `StochGame/UniformEq/Statement.lean`

```lean
import StochGame.UniformEq.Definitions

open scoped BigOperators
open Classical

namespace StochGame
namespace FinStochGame

variable (G : FinStochGame)

/-- Replace player `i`'s strategy inside a profile. -/
def update (σ : G.Prof) (i : G.Player) (τ : G.Strat i) : G.Prof :=
  fun j => if h : j = i then (by simpa [h] using τ) else σ j

/-- `σ` is an ε-equilibrium for the T-stage average-payoff game (all initial states). -/
def isEpsEq_T (ε : ℝ) (T : Nat) (σ : G.Prof) : Prop :=
  ∀ (i : G.Player) (s0 : G.State) (τ : G.Strat i),
    G.avgPayoff i T s0 σ ≥ G.avgPayoff i T s0 (update (G:=G) σ i τ) - ε

/-- `σ` is a uniform ε-equilibrium: ε-equilibrium for all sufficiently large horizons. -/
def isUniformEpsEq (ε : ℝ) (σ : G.Prof) : Prop :=
  ∃ T0 : Nat, ∀ T ≥ T0, isEpsEq_T (G:=G) ε T σ

/-- The conjecture for a fixed game: for every ε>0 there exists a uniform ε-equilibrium. -/
def HasUniformEq : Prop :=
  ∀ ε : ℝ, ε > 0 → ∃ σ : G.Prof, isUniformEpsEq (G:=G) ε σ

end FinStochGame

/-- The global Neyman conjecture: every finite stochastic game has a uniform equilibrium. -/
def UniformEquilibriumConjecture : Prop :=
  ∀ (G : FinStochGame), FinStochGame.HasUniformEq G

end StochGame
```

At this point, the conjecture is a precise Lean proposition with all quantifiers explicit.

---

## 6. The “it is solved” build and audit criteria (mechanical checks)

A Lean repository claims to solve the problem (affirmatively) if all of the following succeed:

### 6.1 Compilation

- `lake build` succeeds with a pinned mathlib version.
- The main theorem is provided:

```lean
import StochGame.UniformEq.Statement

open Classical

theorem uniform_equilibrium_exists :
  StochGame.UniformEquilibriumConjecture := by
  -- full proof, no sorry
```

### 6.2 No `sorry`, no new axioms

Run both checks:

- “No sorry” check (example):
  - `grep -R --line-number "sorry" ./StochGame`
- “No axioms / constants” check:
  - `grep -R --line-number -E "axiom |constant " ./StochGame`

Additionally, audit the axiom footprint of the final theorem:

- In Lean, run:

```lean
#print axioms uniform_equilibrium_exists
```

Acceptance rule: the printed axiom set contains **no new user-defined axioms**. (It may include Lean core axioms such as `Classical.choice`, `propext`, `funext`, etc., depending on the proof.)

### 6.3 Semantic audit (no weakened statement)

A reviewer should verify:

- `avgPayoff` really depends on `σ` through the induced play distribution,
- deviations `τ` are fully history-dependent behavioral strategies,
- the uniformity quantifier is `∃T0, ∀T ≥ T0`, not `∀T, ∃σ_T`.

---

## 7. Summary: the resolution criterion in one paragraph

An affirmative solution to Neyman’s problem is a Lean 4 + mathlib project that defines finite stochastic games with behavioral strategies and finite-horizon average payoffs, defines uniform ε-equilibrium exactly as “ε-equilibrium for all horizons beyond some T0,” and proves in Lean (with no `sorry` and no new axioms) that **for every finite stochastic game and every ε>0 there exists a uniform ε-equilibrium strategy profile**.

---

## References (for human readers, not part of the Lean kernel)

- Game Theory Society (Israel chapter), “Open Problems” (Problem suggested by Abraham Neyman).  
  https://sites.google.com/view/thegametheorysocietyilchapter/open-problems

- Wikipedia, “Stochastic game” (baseline definitions and context).  
  https://en.wikipedia.org/wiki/Stochastic_game
