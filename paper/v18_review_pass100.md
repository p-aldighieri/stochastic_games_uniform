# v18 Review — Pass 100

**Thinking**: 26 min 44s Extended Pro
**Verdict**: FAIL

## GAIN NEAR-CONSTANCY LEMMA IS FALSE
The reviewer provides a COUNTEREXAMPLE:
- Root C: u_i = 1, single boundary label b, lambda_C(b) = 1
- Degenerate terminal child T = C[b]: w_i(T) = 0
- Fixed-point: g_root* = 1, g_T* = 0
- Difference = 1, NOT O(D*eta) for small eta

The induction fails because:
- alpha_C* is an O(1) term (not O(eta))
- beta_C*(b) don't sum to 1 in a way that constrains g_C near children
- Even if all child gains are identical, parent can differ by order 1

## What still works
- Global assembly step WOULD work IF near-constancy were true
- Bellman per visit: still correct
- Actual payoff model: still [0,1]
- All previous fixes: intact

## THE REAL ISSUE
g values CAN vary by O(1) across nodes. The global assembly cannot assume they're constant.
This means the proof needs a different approach to the global step — one that accounts for the actual distribution of time across nodes with different g values.
