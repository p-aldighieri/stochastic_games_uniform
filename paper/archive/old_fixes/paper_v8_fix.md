# Paper v8 Fix — Pass 79

## Instructions

You are the REWRITER. A 28-minute Extended Pro review of v7 found ONE remaining blocker: a restart-bias term in the renewal-reward identity.

## The blocker

When integrating Bellman equalities against the bookkeeping occupation package, an extra term appears:

g*_{i,C} = sum mu_C* u_i + sum beta_C* v_{i,C} - sum_{xi'} (R_C beta_C*)(xi') h*_{i,C}(xi')

The last term is the restart-bias: after exit, the bookkeeping kernel restarts the chain at xi' ~ rho_C(xi'|b), and the bias h* at that restart state contributes. This term vanishes ONLY under a centering condition.

## The fix (simple)

Since h_{i,C}(xi_0^C) = 0 (reference-coordinate normalization, already in the paper) and rho_C is a FREE bookkeeping choice (not part of the executed dynamics), DEFINE:

rho_C(xi | b) = delta_{xi_0^C}(xi) for all b in B_C

That is, the bookkeeping restart always returns to the reference state xi_0^C. Then:
(R_C beta_C*)(xi') = sum_b beta_C*(b) * delta_{xi_0}(xi') = beta_total * delta_{xi_0}(xi')

So the restart-bias term becomes:
sum_{xi'} (R_C beta*)(xi') h*(xi') = beta_total * h*(xi_0) = beta_total * 0 = 0

The identity is then exact: g* = sum mu* u + sum beta* v.

## What to change in the LaTeX

1. Where rho_C is defined (around lines 319-325), add the explicit choice: rho_C(xi|b) = delta_{xi_0^C}(xi) for all exit labels b. State that this is a bookkeeping convention, not a physical restart.

2. In the proof at lines 1068-1083, after the integration step, add one line: "The restart-bias term vanishes because rho_C restarts at the reference state xi_0^C where h_{i,C}*(xi_0^C) = 0 by normalization."

3. Also fix the secondary concern at lines 1585-1592: make the coefficient closeness argument explicit (this was flagged in the review as well).

## Your task

Read the attached v7 tex. Apply these fixes. Output the COMPLETE v8 LaTeX source.
