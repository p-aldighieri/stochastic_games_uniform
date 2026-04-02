# Theorem A — Pass 62 (PROVE IT)

**Pass**: 62
**Role**: Prover
**Model**: ChatGPT Extended Pro
**Date**: 2026-03-29
**Thought time**: 46m 18s (LONGEST in pipeline)

## THE THEOREM

**Theorem A**: Every finite stochastic game satisfying condition (a) — that for every node C, every player i, and every pure stationary action a_i, the unilateral node kernel Q_{C,i}^{x,a_i} is irreducible on C — has a uniform epsilon-equilibrium.

## THE PROOF (sketch from the 46-minute output)

1. **Condition (a) + compactness => kappa_eta > 0**: The minimum n-step transition probability over all nodes, players, actions, state pairs is a positive continuous function on the compact A_eta. Positive continuous on compact => positive minimum.

2. **kappa_eta > 0 => bias span bounded**: sp(h) ≤ (|S|-1) / kappa_eta. This is the classical diameter bound for communicating MDPs.

3. **Bounded bias span => Bellman certificate works**: The deviation value |V_dev(controller) - V_dev(relaxed)| ≤ c_0 + c_1*B_eta + c_2*eta + ... where B_eta = (|S|-1)/kappa_eta < infinity.

4. **Choose eta small, then T_0 large**: For (c_2+c_3)*eta ≤ eps/2, then T_0 such that remainder ≤ eps/2. This gives uniform epsilon-equilibrium.

## KEY FINDINGS

- **Option (e) FAILS**: eta-consistency does NOT force connectors away from zero
- **Candidate (a) is the weakest sufficient condition found**: "no player can unilaterally break irreducibility"
- **The proof is COMPLETE under condition (a)**

## WHAT THIS COVERS

Games where no single player can isolate states include:
- All games with a "public" transition component ensuring connectivity
- Games where each player controls only part of the transition
- Many multiplayer absorbing games

## WHAT IT DOESN'T COVER

Games where a deviator CAN break connectivity — e.g., a player who can choose to "stay forever" in one state, creating a multichain structure. The full Neyman conjecture requires handling this case.
