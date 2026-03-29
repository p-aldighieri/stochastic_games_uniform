# Uniform Equilibrium Route Memo

Updated after 23 Extended Pro passes (2026-03-26 to 2026-03-27). Starting Route D'.

## Exhausted Routes

### Route B: Stationary Lexicographic — DEAD
- Conditional theorem (H1+H2+H3) is correct but H3 is provably false
- The stationary limit x* of discounted Nash equilibria fails bias-level optimality on gain-neutral off-support actions
- Concrete counterexample: 2-player absorbing game, unique analytic branch, kappa_1 = 1/4 > 0

### Route C: History-Dependent Punishment — DEAD
- Gain-level control works automatically (supermartingale)
- Bias-level punishment requires self-enforcing coalition with private signals
- Public actions/history/randomization cannot simulate private role assignments
- 4+ player absorbing Nash is the smallest open subclass
- Cheap-talk embedding in public actions insufficient (Barany needs private messages)

### Route D: Raw Strategy-Space Fixed-Point — DEAD
- Strategy space not compact in the right topology
- Payoff functionals not continuous
- Periodic orbit structure can blow up

## Active Route: D' — Compact Asymptotic State Space

### The Core Idea
Don't do topology on raw strategies. Do topology on a **compactified asymptotic object** where payoff and deviation functionals become continuous. Then apply Kakutani/viability on that space.

### What works in solved subclasses
| Subclass | Compact Object | Reference |
|----------|---------------|-----------|
| Quitting games | Absorption paths | Ashkenazi-Golan et al. |
| Positive recursive absorbing | Continuation-value orbits | Solan-Vieille 2025 |
| 2-player zero-sum | Algebraic value structure | Mertens-Neyman, Bewley-Kohlberg |

### What the general object might look like
A compact space A encoding, for each communicating set of states:
- **Occupation measures**: how long play stays in each state
- **Exit intensities**: how and when play leaves each communicating set
- **Continuation values**: what payoffs are expected after exit
- **Gain-bias structure**: the lexicographic decomposition from our conditional theorem

Plus an **implementability map** A → Σ showing each point of A can be realized by an actual strategy profile, and a **deviation map** checking that no player can improve by deviating.

### Key challenges
1. Define A precisely for general finite stochastic games
2. Prove A is compact (or can be compactified) with continuous payoff
3. Prove the self-map (best response on A) has a fixed point
4. Prove the fixed point yields a uniform epsilon-equilibrium

### What we bring from prior routes
- The gain-bias decomposition (Route B) gives the right payoff structure on A
- The deviation taxonomy (Route C) tells us which deviations the fixed point must handle
- The block structure gives the right granularity for the implementability map
