# v22 Review — Pass 108

**Thinking**: 27 min 46s Extended Pro
**Verdict**: FAIL

## PASSES: Psi telescope fully correct
- Stock Z: PASS
- Clean drift: PASS (on complete tail)
- Psi boundedness: PASS
- Previous fixes: intact

## FAILS: Gain-level routed comparison (Lemma 6.6 / Prop 8.3)
The telescope gives payoff = sum g_{C(t)} + O(boundary).
But regret needs: deviator sum g_{C(t)}^dev vs compliant sum alpha_{C(t)}^comp.
These involve DIFFERENT node sequences.
The "direct routed tail comparison" at lines 2123-2203 is not proved.
The varying gain function G is not controlled.
