# External Agent Request (prover — Route C: History-Dependent Strategies)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-27T05:15:00.000000+00:00

## Instructions

You are the prover role. This is a FUNDAMENTALLY NEW approach to Neyman's open problem, building on everything learned from 16 prior Extended Pro passes.

**The key lesson**: The stationary limit of discounted Nash equilibria fails condition (H3) — concrete counterexample proves this. BUT the theorem only asks for SOME strategy profile, not a stationary one. History-dependent strategies with punishment phases can maintain incentive compatibility even when (H3) fails.

## What Has Been Established

1. **Gain-level control works automatically**: For any convergent discounted Nash branch x_lambda -> x*, the gain function g_i(s) is a supermartingale under one-step deviations. Gain-burning deviations contribute only O(1/T) to average regret. This is FREE — no punishment needed.

2. **The ONLY gap is at the bias level for gain-neutral deviations**: Actions with d_i(s,a_i) = 0 can have positive kappa_i, meaning the bias inequality fails. The counterexample shows this is genuinely possible.

3. **History-dependent strategies can close this gap**: Instead of playing the stationary x* forever, play a strategy that:
   - Normally prescribes x*(s) at each state
   - Monitors public history for deviations
   - Switches to punishment after detected deviations
   - The punishment threat deters gain-neutral deviations

## The New Proof Architecture

### Step 1: Start with the stationary profile x* from the discounted limit
- x* is gain-optimal (gain supermartingale property)
- x* satisfies the bias equality on support actions (phi_i = 0)
- x* fails (H3) on some off-support gain-neutral actions

### Step 2: Build a history-dependent strategy sigma that modifies x*
- At each stage, if no deviation has been detected, prescribe x*(s_t)
- Public deviations are detectable: in a finite stochastic game with observed actions, the entire action profile is public information
- If player i deviates at stage t (plays a_i != x_i*(s_t)), switch to a PUNISHMENT PHASE for player i

### Step 3: Design the punishment phase
- The punishment for player i uses the other players' minmax strategy against i
- Player i's minmax value v_i^min(s) is well-defined at each state (the game is finite)
- During punishment: player i's per-stage payoff is at most v_i^min(s) <= g_i(s)
- Punishment lasts for L stages, where L is chosen large enough that the deviation gain is offset

### Step 4: Regret analysis
- Gain-burning deviations: O(1/T) average regret (automatic, from gain supermartingale)
- Gain-neutral deviations WITH (H3): O(1/T) average regret (from the conditional theorem)
- Gain-neutral deviations VIOLATING (H3): The one-stage gain is at most kappa_i (bounded). The punishment phase costs the deviator at least (g_i - v_i^min) * L stages. Choose L so punishment dominates.
- On-path payoff: same as x* plus O(1/T) correction from punishment phase lengths

### Step 5: Handle the technical challenges
- **Multiplayer punishment**: When player i deviates, the other players must jointly minmax i. This requires coordination among N-1 players, which is harder than in 2-player games.
- **Mixed-action deviations**: Player i might mix between x_i*(s) and a deviating action. The deviation must be detectable from the realized action.
- **State-dependent punishment**: The punishment minmax value depends on the state. The punishment must track state transitions correctly.
- **Block structure**: Use growing blocks as in the earlier sessions. Each block has L_t stages. Punishment is scoped within blocks.

## The Key Question

Can this history-dependent construction be made rigorous for MULTIPLAYER finite stochastic games?

The 2-player case (Vieille 2000) is known. The multiplayer challenge is coordinated punishment: when player i deviates, the other N-1 players must switch to jointly minmaxing i. In a 2-player game, the other player just plays their minmax strategy. In a multiplayer game, the minmax coalition must itself be an approximate equilibrium among the N-1 punishing players.

**This is exactly the folk theorem structure.** The folk theorem literature (Fudenberg-Maskin 1986, for repeated games) handles multiplayer punishment by using a sequence of punishment phases: first punish i, then reward the punishers. The stochastic game version needs to handle state changes during punishment.

## What to Produce

1. A rigorous proof of uniform epsilon-equilibrium existence using history-dependent strategies with punishment phases, OR
2. Identification of the exact multiplayer coordination challenge and a proposed solution

Use the durable project sources for background. The conditional theorem's gain-level analysis is reusable — the new work is only at the bias level.

This is the most natural path forward. The folk theorem machinery is well-developed for repeated games. Adapting it to stochastic games with the gain-bias decomposition from our conditional theorem is the frontier.
