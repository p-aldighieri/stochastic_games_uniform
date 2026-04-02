# v20 Review — Pass 104

**Thinking**: 24 min 51s Extended Pro
**Verdict**: FAIL

## What PASSES
- Boundary term: yes (||h|| bounded by H_eta)
- Local Bellman inside each node: yes
- Old visit-level chaining removed: yes
- All structural fixes: intact

## TWO BREAKPOINTS

### 1. Missing stock-augmented drift identity (lines 1916-1933)
The local Bellman gives a same-node next-bias term plus exit credit v_C(b).
But the paper claims a global Phi_{t+1} term from the child node.
The paper admits a "carried stock Z_t" is needed (lines 1852-1857) then suppresses it.
The +eta in line 1933 is not justified at the raw Bellman stage.

### 2. Rooted benchmark + supermartingale claim (Lemma 1958)
The deviator bound is not justified. The rooted benchmark is underdefined.

## KEY INSIGHT FROM REVIEWER
The potential Phi(t) = h_{C(t)}(X_t) is NOT continuous across node transitions.
When play exits node C to child D, h_C and h_D are different functions.
Need Psi_t = Phi_t + Z_t where Z_t tracks the accumulated stock from transitions.
