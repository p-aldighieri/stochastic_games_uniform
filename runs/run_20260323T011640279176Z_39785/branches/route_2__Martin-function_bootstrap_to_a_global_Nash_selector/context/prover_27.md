# Prover Output (Route D: Direct Topological/Fixed-Point)

Generated: 2026-03-27T12:00:00.000000+00:00

## VERDICT: Raw strategy-space fixed-point REFUTED. Correct idea, wrong space.

Direct Brouwer/Kakutani on ordinary history-dependent strategies fails because:
- Strategy space is not compact in the right topology
- Payoff functionals are not continuous in the product topology
- Periodic orbit structure can blow up

## What the literature shows
- Quitting games (Ashkenazi-Golan): succeed by using ABSORPTION PATHS as the compact space
- Positive recursive absorbing (Solan-Vieille 2025): use continuation-value orbits, not raw strategies
- Both work on COMPACTIFIED ASYMPTOTIC OBJECTS, not the original strategy space

## Route D' (the real theorem)
"Construct a compact asymptotic state space A of public-play summaries, with continuous payoff and deviation functionals, plus an implementability map A → Σ, and apply Kakutani on A."

For general stochastic games, A would encode occupation measures + exit intensities + continuation values together. This is a research program — each solved subclass found its own compactification.

## Status
The problem is genuinely open. Three architectures comprehensively mapped:
- Route B: stationary limits fail (H3 false)
- Route C: punishment needs private signals
- Route D: raw fixed-point fails, correct compactification unknown
