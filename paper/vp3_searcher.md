# VP3 Searcher: Joint-Germ Compatibility (Pass 54)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the SEARCHER role. Your task is to find ALL viable strategies for proving VP3 (Joint-Germ Compatibility).

## The Problem (VP3)

**Condition (VP3)**: For every node C in a metastable tree and every feasible target (mu_C, beta_C), there exists a single convex combination of deterministic stationary joint policies that SIMULTANEOUSLY realizes:
- The target occupation measure mu_C (internal dynamics)
- The target boundary flux beta_C (exit behavior)

The issue: We know separately that
- mu_C lies in the occupation polytope P_C (proven in Section 5.1)
- beta_C lies in the flux image of the occupation polytope (proven in Section 5.2)

But we need them to come from the SAME joint policies — not from two separate decompositions.

## Mathematical Formulation

Let Theta_C^det be the set of deterministic stationary joint policies on node C.
For each theta in Theta_C^det, define:
- occ(theta) = occupation measure induced by theta
- flux(theta) = boundary flux induced by theta

VP3 asks: For every feasible (mu, beta) with mu in conv{occ(theta)} and beta in conv{flux(theta)}, does there exist a single convex combination sum_k lambda_k (occ(theta_k), flux(theta_k)) = (mu, beta)?

Equivalently: Is the image of the joint map (occ, flux): Theta_C^det -> R^d1 x R^d2 convex after taking the convex hull? I.e., does conv{(occ(theta), flux(theta)) : theta in Theta_C^det} project onto conv{occ(theta)} x conv{flux(theta)}?

This is a FIBER INTERSECTION problem in polyhedral geometry.

## What is known

- For single-state nodes (quitting games): VP3 is trivial (occ and flux collapse)
- For two-player zero-sum: saddle-point structure bypasses VP3
- For positive recursive absorbing: VP3 holds under non-rectangular absorption

## Your Task

Find at least 5 distinct strategies for proving VP3. For each, give:
1. Strategy name
2. Core idea (2-3 sentences)
3. Key mathematical tool
4. Why it might work
5. Why it might fail
6. Estimated difficulty (1-10)

Also consider:
- Can VP3 fail? Give a candidate counterexample construction or argue why it can't.
- What is the simplest non-trivial case where VP3 is not obviously true?
- Is there a connection to known results in combinatorial optimization (e.g., total unimodularity, network flows, matroid intersection)?

Be creative and thorough. This is the key to turning our conditional theorem into an unconditional one.
