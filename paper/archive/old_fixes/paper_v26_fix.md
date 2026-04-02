# Paper v26 Fix — Pass 115

## Pass 114: Single-player MDP reframing CORRECT, but g_C ≠ global MDP value

The reviewer confirms: the single-player MDP reframing (v25) is correct. But the local gain g_{i,C}* is a restarted-node average, NOT the optimal gain of the global MDP. All 10+ attempts to bridge local gains to a global bound have failed. We need a fundamentally different approach to the GLOBAL STEP.

## THE FIX: Use the GLOBAL MDP value function directly — no local-to-global bridge needed

### The key realization (after 114 passes)

The paper has been overcomplicating the global step. Under v25's correct MDP reframing, the epsilon-equilibrium follows DIRECTLY from standard average-reward MDP theory, without needing to relate local gains g_C across nodes.

### The argument (3 steps)

**STEP 1: The MDP is unichain (condition (a))**

When player i considers deviating from sigma_eta, the other players continue playing sigma_{-i}^eta. Player i faces a Markov Decision Process with:
- State space: S (the game's finite state space)
- Actions: A_i (player i's finite action set)
- Transition kernel: P(s'|s, a_i) = sum_{a_{-i}} sigma_{-i}^eta(a_{-i}|s) * q(s'|s, (a_i, a_{-i}))
- Payoff: r_i(s, a_i) = sum_{a_{-i}} sigma_{-i}^eta(a_{-i}|s) * u_i(s, (a_i, a_{-i}))

Condition (a) guarantees: no player can UNILATERALLY break irreducibility. Therefore, for ANY stationary policy sigma_i, the Markov chain under (sigma_i, sigma_{-i}^eta) on the finite state space S is irreducible. This means the MDP is UNICHAIN.

**STEP 2: Standard average-reward MDP theory gives the bounds**

For a finite-state unichain MDP (Puterman 1994, Bertsekas 2007):

(a) There exists a unique optimal gain g_i* (a scalar — the maximum achievable long-run average reward).

(b) There exists a bias function h_i*: S → R satisfying the Bellman optimality equation:
  g_i* + h_i*(s) = max_{a_i} [r_i(s, a_i) + sum_{s'} P(s'|s, a_i) h_i*(s')]

(c) The span of the bias is bounded: sp(h_i*) = max_s h_i*(s) - min_s h_i*(s) ≤ D_i * max|u_i|, where D_i is the diameter of the MDP (bounded since S is finite and the chain is irreducible for all policies, by condition (a)).

(d) DEVIATOR UPPER BOUND: For ANY policy sigma_i (stationary, history-dependent, or randomized):
  (1/T) * E[sum_{t=1}^T u_i(t)] ≤ g_i* + sp(h_i*) / T

This is the optimality inequality. Proof: M_t = h_i*(s_t) - sum_{k<t}(u_i(k) - g_i*) is a supermartingale under any policy. Therefore E[M_T] ≤ M_0 = h_i*(s_0), which gives E[sum u_i(k)] ≤ g_i* T + h_i*(s_0) - E[h_i*(s_T)] ≤ g_i* T + sp(h_i*).

(e) COMPLIANT LOWER BOUND: The compliant policy sigma_i^eta is eta-optimal (by the fixed-point construction), so the gain of the chain under sigma^eta satisfies:
  g_i^{erg}(sigma^eta) ≥ g_i* - O(eta)

By the ergodic theorem (the chain is irreducible under sigma^eta by condition (a)):
  (1/T) * E[sum_{t=1}^T u_i(t; sigma^eta)] → g_i^{erg}(sigma^eta) as T → ∞

Therefore for T ≥ T_1(eta):
  (1/T) * E[sum u_i(t; sigma^eta)] ≥ g_i* - O(eta) - O(1/T)

**STEP 3: Epsilon-equilibrium**

Regret = (deviator payoff) - (compliant payoff)
       ≤ [g_i* + sp(h_i*)/T] - [g_i* - O(eta) - O(1/T)]
       = sp(h_i*)/T + O(eta) + O(1/T)

Given epsilon > 0:
- Choose eta = epsilon/4
- Construct sigma^eta via the Kakutani fixed point (existing Sections 3-5)
- sp(h_i*) is now a finite constant H_i(eta) depending on game parameters and eta
- For T ≥ T_0 = max(4H_i/epsilon, T_1), the regret ≤ epsilon

This is the UNIFORM epsilon-equilibrium: sigma^eta works for ALL T ≥ T_0.

### What changes in the paper

KEEP (Sections 1-6 approximately):
- Tree decomposition of strongly connected components
- Local Bellman certificates (g_C, h_C) at each node
- Stock Z and potential Psi — for the CONSTRUCTION of sigma^eta
- Kakutani fixed-point theorem — for existence of sigma^eta
- Proof that sigma_i^eta is eta-optimal (g_i^{erg} ≥ g_i* - O(eta))

REPLACE (the "global benchmark" / "routed comparison" / "tree telescoping" section):
- DELETE all attempts to show sum g_{C(t)} = g_root * T
- DELETE all gain-near-constancy claims
- DELETE all routed comparisons across different node sequences
- REPLACE with the 3-step argument above: unichain → global value function → regret bound

The deviator upper bound comes from the GLOBAL h_i* (which exists by standard theory), NOT from stitching together local h_C via Z. The local machinery is still essential for constructing sigma^eta, but the regret bound is a separate, cleaner argument.

### Why this fixes the "mountain pass"

The persistent failure mode (passes 100-114) was: trying to relate gains g_C at DIFFERENT nodes visited by compliant vs deviator. This is impossible because g_C is a LOCAL quantity and different policies visit different nodes.

The fix: don't compare local gains at all. The GLOBAL MDP has a SINGLE optimal gain g_i* that upper-bounds ANY policy's average reward, regardless of which nodes it visits. This is a property of the global MDP, not of individual nodes.

The local gains g_C are still useful for the fixed-point construction (they define the strategies), but they play NO role in the regret bound.

### Critical detail: sp(h_i*) boundedness

The span of h_i* is bounded because:
1. S is finite (|S| states)
2. Under condition (a), the MDP is unichain for all stationary policies
3. The diameter D_i ≤ |S|^2 / p_min where p_min > 0 is the minimum transition probability under any stationary policy (exists because condition (a) gives irreducibility with a finite action set)
4. sp(h_i*) ≤ D_i * max|u_i| ≤ |S|^2 * max|u_i| / p_min

Note: p_min depends on sigma_{-i}^eta, hence on eta. As eta → 0, p_min could shrink, making sp(h_i*) grow. But eta is fixed (depends on epsilon), so sp(h_i*) is a finite constant for fixed eta.

Output the COMPLETE v26 LaTeX source as a downloadable .tex file.
