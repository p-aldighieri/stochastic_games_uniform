# v10 Review — Pass 84

**Thinking**: 26 min 24s Extended Pro
**Verdict**: FAIL

## Issue: Post-terminal horizon length

The D_eta * ||u|| / T bound controls the NUMBER of terminal hits but NOT the DURATION of post-terminal play, which can be Theta(T).

Counterexample: terminal hit at stage 1, terminal profile yields payoff 1 per stage for remaining T-1 stages. Accounting records one-shot w(b)=1 but actual contribution is (T-1)/T ≈ 1, not 1/T.

## Fix needed

The terminal continuation payoff should NOT be a one-shot w(b). Instead:
- After terminal hit at stage t, the strategy plays the terminal profile for stages t+1,...,T
- The per-stage regret from this segment = |g*_root - w_avg(b)| * (T-t)/T
- Since w_avg(b) is the known average of the terminal profile, this is INCLUDED in g*_root by the fixed-point construction
- OR: redefine terminal labels so w(b) IS the per-stage average under the terminal profile, and include the full (T-t) segment in the accounting
