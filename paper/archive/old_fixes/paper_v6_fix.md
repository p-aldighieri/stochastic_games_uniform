# Paper v6 Fix — Pass 75

Provider: external_agent
Model hint: chatgpt-5.4-pro
Generated: 2026-03-30

## Instructions

You are the REWRITER. A 22-minute Pro review found 4 blockers in v5. Fix ALL FOUR and output the COMPLETE corrected v6 LaTeX source.

## Blocker 1: Nonconvex Kakutani domain (bias normalization)

The bias coordinate h_{i,C} is normalized by min_xi h(xi) = 0. This set is NOT convex — two normalized biases can average to strictly positive minimum.

**FIX**: Replace min h = 0 normalization with a FIXED reference coordinate: h_{i,C}(xi_0) = 0 for a fixed reference state xi_0. This makes the bias space an affine subspace (convex!). Alternatively, normalize by sum h = 0. Either works — the key is that the normalization must be a LINEAR constraint, not a pointwise min.

## Blocker 2: Sub-stochastic kernel treated as Markov

The internal kernel P_C^0 has row sums < 1 when exits exist. But condition (a), kappa_eta, and the bias-span proof all assume a genuine stochastic kernel (irreducibility, hitting times, powers).

**FIX**: All of these must be stated for the AUGMENTED kernel, not the internal kernel. The augmented kernel P_C^aug on Xi_C^aug = Xi_C ⊔ {cemetery states} IS a genuine stochastic kernel (cemetery states are absorbing, so rows sum to 1). Under condition (a), the augmented kernel restricted to Xi_C (the transient states before absorption) is irreducible. The relevant MDP for the deviator also operates on the augmented state space. Rewrite condition (a) as: "for every player i and every action a_i, the augmented transition kernel remains irreducible on Xi_C (i.e., the process can reach any internal state from any other before being absorbed)."

## Blocker 3: Payoff target mismatch

g*_{i,C} = sum mu_C sigma* u_i + sum_b beta_C sigma*(b) v_{i,C}^x*(b) includes continuation terms from exits. But the theorem claims the average of STAGE PAYOFFS alone converges to g*. This is wrong — stage payoffs don't include continuation values.

**FIX**: Define the "augmented stage payoff" that includes the continuation value at the moment of exit. Specifically:
- While in Xi_C: stage payoff is u_i(xi, a) as usual
- When hitting cemetery state partial_b: the "payoff" at that step is the continuation value v_{i,C}(b)
- The augmented average payoff over a block = (1/L) * [sum of stage payoffs in Xi_C + continuation value at exit]
- This matches g*_{i,C} exactly

Alternatively: define g*_{i,C} as the average stage payoff ONLY (without continuation), and handle the continuation contribution separately in the regret bound. Either approach works, but be consistent.

## Blocker 4: Routing semantics

The regenerated augmented chain can visit cemetery states multiple times per block (because it regenerates). "Block emits single boundary state" is undefined.

**FIX**: Define block termination precisely:
- A block at node C starts when the global process enters C
- The block runs the local augmented controller
- The block TERMINATES at the FIRST visit to any cemetery state partial_b
- After termination, the process transitions to the child node determined by b
- The remaining block time (if any) is wasted/padded (contributes zero to payoff)
- This gives exactly ONE boundary emission per block (or none if the block ends without exit)

The regeneration in the Caratheodory mosaic happens WITHIN the internal states only — it never regenerates through cemetery states.

## Additional fixes from reviewer
- Add a uniqueness-of-normalized-bias citation for communicating MDPs
- Make sure all lemmas that use "irreducibility" are stated for the augmented kernel

## Your task

Read the attached v5 tex. Apply ALL 4 fixes. Output the COMPLETE v6 LaTeX source. Every theorem must have a complete, correct proof.
