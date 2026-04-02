# v24 Review — Pass 112

**Thinking**: 24 min 59s Extended Pro
**Verdict**: FAIL

## PASSES (local machinery fully verified)
- Local Bellman certificates: acceptable
- Bias bound under condition (a): acceptable
- Z/Psi stagewise telescope: acceptable
- Public routing / finite memory / tail truncation: acceptable

## FAILS: Common-root comparison
"not established, and likely wrong under the current definitions"
The claim that both compliant and deviating play are controlled by
scalar g_root is not proved and appears false under current definitions.
g_root values are player-specific and node-dependent.

## BOTTOM LINE
"The paper has a valid new local-supermartingale core, but it still
needs a different global benchmark theorem."

## STATUS AFTER 112 EP PASSES
The local proof machinery (Z, Psi, Bellman, bias, routing) is fully
verified across multiple independent reviews. The ONLY remaining gap
is the global benchmark — how to turn local per-node Bellman bounds
into a T-horizon epsilon-equilibrium. This may require a fundamentally
different approach to the global step, or additional structural ingredients
beyond condition (a).
