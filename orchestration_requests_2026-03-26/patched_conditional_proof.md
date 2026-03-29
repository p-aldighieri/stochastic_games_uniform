# External Agent Request (prover — patched conditional proof)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-26T12:00:00.000000+00:00

## Instructions

You are the prover role. Your task is to produce a CLEAN, SELF-CONTAINED, FULLY RIGOROUS conditional proof of the uniform equilibrium theorem. This incorporates 3 patches identified by the reviewer (PATCH_SMALL verdict on Prover 16):

1. **Step 1 fix**: The gain inequality must be stated as a ONE-STEP deviation inequality (not a generic "supermartingale" claim without derivation)
2. **Step 4 fix**: The constant C_i must be defined via an explicit FINITE-GAP LEMMA
3. **Step 5 fix**: Must explicitly derive that g_i(s_t) is a supermartingale under arbitrary multi-step deviations (not just one-step)

Additionally, after the conditional proof, address the UPSTREAM QUESTION:

**The Puiseux exponent question**: The reviewer found that bounded bias is NOT a general consequence of Puiseux theory — fractional exponents in (-1,0) can appear (Solan's Example 4.4). However, this example is for zero-sum VALUES, not for NASH EQUILIBRIUM branches specifically.

Investigate: Is there a structural reason why Nash equilibrium branches of multiplayer stochastic games might avoid the problematic fractional exponents? Specifically:
- Nash equilibrium conditions impose additional algebraic constraints beyond what semi-algebraic selection gives
- The equilibrium payoff is not just a value — it's a fixed point of a best-response correspondence
- Could these extra constraints force the Puiseux expansion to have integer (or at least non-negative) exponents after de-normalization?

## What to Produce

### Part 1: The Patched Conditional Proof

**Theorem (Conditional).** Let G be a finite stochastic game. Suppose there exists a sequence lambda_n -> 0 and stationary discounted Nash equilibria x_{lambda_n} such that:
(H1) x_{lambda_n}(s) -> x*(s) for every state s,
(H2) v_i^{lambda_n}(s) = g_i(s)/lambda_n + b_i(s) + r_{i,n}(s) with r_{i,n}(s) -> 0 uniformly in s, for every player i and state s.

Then for every epsilon > 0, x* is a uniform epsilon-equilibrium for all T >= T_0(epsilon).

Write the proof with:
- All notation defined
- Every inequality derived from first principles (discounted Nash condition)
- The finite-gap lemma for C_i stated and proved as a standalone lemma
- The supermartingale property for g under multi-step deviations derived explicitly
- The on-path martingale + bias equality derived explicitly
- The final regret bound computed with explicit constants

### Part 2: The Puiseux Exponent Investigation

Investigate whether Nash equilibrium branches have better Puiseux regularity than general semi-algebraic branches. This is the key to closing the full (unconditional) theorem.
