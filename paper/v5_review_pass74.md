# v5 Review — Pass 74

**Thinking**: 22 min 44s Pro
**Verdict**: FAIL
**Bibliography**: PASS

## Four blockers

### 1. Nonconvex Kakutani domain
Bias normalization min_xi h(xi)=0 is not convex. Two normalized biases can average to strictly positive min. Fix: normalize by FIXED reference coordinate instead.

### 2. Sub-stochastic kernel treated as Markov
Internal kernel P_C^0 has row sums < 1 when exits exist. Condition (a), kappa_eta, bias span all assume genuine stochastic kernel. Fix: rebuild on augmented stochastic kernel (including cemetery states).

### 3. Payoff target mismatch in controller
g*_i,C includes continuation terms, but theorem claims stage payoffs alone converge to g*. Fix: redefine block payoff bookkeeping to match the realized object.

### 4. Routing semantics undefined
Regenerated augmented chain can hit cemetery states multiple times per block. "Block emits single boundary state" is undefined. Fix: define block output precisely.

## What PASSES
- Augmented occupation polytope (Prop 3.1): PASS
- Graph theorem (Thm 3.2): PASS
- Coefficient map (Lemma 4.1): PASS
- Appendices: all PASS
- Bibliography: PASS

## Suggested rescue path
1. Normalize biases by fixed reference coordinate (not min h = 0)
2. Rebuild local problem and condition (a) on genuine stochastic AUGMENTED kernel
3. Redefine block payoff so g* matches realized object
4. Define block output routing precisely
