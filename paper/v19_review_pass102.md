# v19 Review — Pass 102

**Thinking**: 22 min 5s Extended Pro
**Verdict**: FAIL

## THE ISSUE: U_tilde has exit credit but no entry debit

U_tilde_i(V) = U_act(V) + sum_b I_V(b)*v_C(b) has an EXIT credit only.
It does NOT include a matching ENTRY debit for the next visit.

The child visit starts with its own bias h_D(X_in), NOT with -v_C(b).
So the cross-visit cancellation is not there.

## Algebra check (C→D one-edge tree)
G - B = g_C*l_C + g_D*l_D - v_C(b)
At fixed point: v_C(b) ≈ g_D + O(eta)
So: G - B = g_C*l_C + O(eta*l_D)

This shows the cancellation only works if v_C(b) perfectly absorbs g_D*l_D,
but the proof doesn't establish this.

## Suggested fix
Either:
(a) Entry-exit corrected functional with both +exit and -entry credits
(b) Continuation data encoding entire descendant benchmark, not just g_D*
