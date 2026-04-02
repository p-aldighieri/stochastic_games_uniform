# VP3 Counterexample Check / Smallest Gadget (Pass 55)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the PROVER role. The VP3 Searcher (Pass 54) identified a critical insight: VP3 is equivalent to extreme-corner completion, and **VP3 in its literal product form may be FALSE.**

Your task: COMPUTE the K_{2,2} support graph for the smallest non-trivial gadget and determine whether VP3 holds or fails.

## The Gadget

Consider the simplest non-trivial case:
- A communicating class C with **2 states** {s1, s2}
- **2 exit edges** leading to distinct boundary states {b1, b2}
- **2 players**, each with 2 actions at each state
- Transition probabilities chosen to create non-trivial internal dynamics and rare exits

## What to Compute

1. **Enumerate all deterministic stationary joint policies** theta in Theta_C^det. For 2 players, 2 actions each, 2 states: there are (2*2)^2 = 16 policies.

2. **For each policy theta, compute:**
   - occ(theta): the stationary occupation measure on {s1, s2} x {actions}
   - flux(theta): the boundary flux vector (beta(b1), beta(b2))

3. **Find the extreme points** of:
   - P_C = conv{occ(theta) : theta in Theta_C^det}
   - B_C = conv{flux(theta) : theta in Theta_C^det}

4. **Check corner completion**: For each pair (x, y) with x in ext(P_C) and y in ext(B_C), does there exist a policy theta with (occ(theta), flux(theta)) = (x, y)?

5. **If VP3 fails**: Exhibit the specific missing corner. Explain why the occupation measure x forces certain action frequencies that are incompatible with the exit pattern y.

6. **If VP3 holds on this gadget**: Try a slightly larger gadget, or argue why corner completion might hold generically.

## Design the Transition Probabilities

Choose transition probabilities that create tension between internal dynamics and exit behavior. For example:
- At state s1, action pair (a1, a1): stays in C with high probability, exits through b1 with low probability
- At state s1, action pair (a2, a2): exits through b2 with moderate probability
- Different pattern at s2

The goal is to find probabilities where different policies give different occupation/flux tradeoffs, so that not all corners of ext(P) x ext(B) are achievable.

## Output

Give the explicit computation with numbers. If VP3 fails, this is a MAJOR finding — it means we need to reformulate the conditional theorem. If VP3 holds on this gadget, we need to understand why and whether it generalizes.

Be precise and computational. This is the most important pass in the entire pipeline.
