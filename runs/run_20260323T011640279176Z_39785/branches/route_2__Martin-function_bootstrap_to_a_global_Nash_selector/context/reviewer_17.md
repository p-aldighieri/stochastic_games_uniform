# Reviewer Output (Conditional Proof Review + Literature)

Generated: 2026-03-26T10:30:00.000000+00:00

## Task 1: Review of Conditional Proof
VERDICT: PATCH_SMALL

The proof skeleton is sound. Three minor patches needed:
1. Step 1 wording: one-step deviation inequality
2. Step 4: explicit finite-gap lemma for constant C_i
3. Step 5: explicit use of gain supermartingale

With patches, O(1/T) regret bound is valid.

## Task 2: Literature on Bias Boundedness
VERDICT: **NOT KNOWN, AND LIKELY FALSE IN GENERAL**

Critical finding: The Puiseux expansion can have FRACTIONAL EXPONENTS between -1 and 0.

Solan's Example 4.4: unnormalized value = 1/lambda - lambda^{-1/2} + 1 - lambda^{1/2} + ...
After subtracting g/lambda, remainder has lambda^{-1/2} -> infinity. Bias is NOT bounded.

The precise remaining gap: "Do all Puiseux exponents in (-1, 0) vanish for multiplayer discounted Nash branches?"

No existing paper (Bewley-Kohlberg, Oliu-Barton, Vigeral, Solan, Ziliotto) addresses this for multiplayer.
