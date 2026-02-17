"""Payoff computation, MDP best-response solver, regret analysis, and discounted equilibrium."""

import numpy as np
from itertools import product as iterproduct


# =================================================================
# Strategy representation
# =================================================================

class StationaryStrategy:
    """A stationary (Markov, memoryless) strategy profile.

    sigma[i][s] is a probability distribution over player i's actions in state s.
    """

    def __init__(self, game, sigma):
        """
        Parameters
        ----------
        game : FiniteStochasticGame
        sigma : list of list of np.ndarray
            sigma[i][s] = array of shape (n_actions[i][s],) summing to 1.
        """
        self.game = game
        self.sigma = sigma

    def mixed_action(self, player, state):
        return self.sigma[player][state]

    def action_profile_prob(self, state):
        """Return dict: action_profile -> probability under this strategy."""
        g = self.game
        probs = {}
        for a in g.action_profiles(state):
            p = 1.0
            for i in range(g.n_players):
                p *= self.sigma[i][state][a[i]]
            probs[a] = p
        return probs


def uniform_strategy(game):
    """Create a uniform random stationary strategy profile."""
    sigma = []
    for i in range(game.n_players):
        si = []
        for s in range(game.n_states):
            n_a = game.n_actions[i][s]
            si.append(np.ones(n_a) / n_a)
        sigma.append(si)
    return StationaryStrategy(game, sigma)


# =================================================================
# Finite-horizon average payoff (exact, for stationary strategies)
# =================================================================

def compute_avg_payoff_exact(game, strategy, T, s0):
    """Compute exact expected average payoff for stationary strategy via matrix methods.

    For stationary strategies, the induced Markov chain on states has
    transition matrix Q and expected stage payoff vector r.
    gamma_i^T(s0) = (1/T) * sum_{t=0}^{T-1} (Q^t r_i)[s0].

    Returns array of shape (n_players,).
    """
    S = game.n_states
    Q = np.zeros((S, S))
    r = np.zeros((S, game.n_players))

    for s in range(S):
        aprobs = strategy.action_profile_prob(s)
        for a, prob in aprobs.items():
            if prob < 1e-15:
                continue
            Q[s] += prob * game.get_transition(s, a)
            r[s] += prob * game.get_payoff(s, a)

    # Compute (1/T) sum_{t=0}^{T-1} Q^t r
    total_payoff = np.zeros((S, game.n_players))
    Qt = np.eye(S)  # Q^0 = I
    for t in range(T):
        total_payoff += Qt @ r
        Qt = Qt @ Q

    avg_payoff = total_payoff / T
    return avg_payoff[s0]


def compute_avg_payoff_mc(game, strategy, T, s0, n_samples=100000, seed=42):
    """Monte Carlo estimation of average payoff for stationary strategy.

    Returns array of shape (n_players,).
    """
    rng = np.random.RandomState(seed)
    total = np.zeros(game.n_players)

    for _ in range(n_samples):
        s = s0
        episode_payoff = np.zeros(game.n_players)
        for t in range(T):
            # Sample actions
            actions = []
            for i in range(game.n_players):
                mix = strategy.mixed_action(i, s)
                a_i = rng.choice(len(mix), p=mix)
                actions.append(a_i)
            a = tuple(actions)
            episode_payoff += game.get_payoff(s, a)
            # Transition
            trans = game.get_transition(s, a)
            s = rng.choice(game.n_states, p=trans)
        total += episode_payoff / T

    return total / n_samples


# =================================================================
# Best-response MDP solver (backward induction)
# =================================================================

def best_response_value(game, strategy, deviator, T, s0):
    """Compute best-response value for player `deviator` via backward induction.

    Given that all other players follow `strategy`, the deviator faces an MDP.
    We solve it by backward induction over the T stages.

    Returns
    -------
    br_value : float
        max_{tau_i} gamma_i^T(s0, (tau_i, sigma_{-i}))
    br_policy : list of np.ndarray
        br_policy[t][s] = optimal action for deviator at time t in state s
    """
    S = game.n_states
    i = deviator

    # Precompute: for each (s, a_i), the expected payoff and transition
    # when other players follow strategy
    # Expected over other players' mixed actions
    def deviator_mdp(s, a_i):
        """Return (expected_payoff_i, transition_dist) when deviator plays a_i."""
        exp_payoff = 0.0
        exp_trans = np.zeros(S)
        # Enumerate other players' actions weighted by strategy
        other_ranges = []
        for j in range(game.n_players):
            if j == i:
                other_ranges.append([a_i])
            else:
                other_ranges.append(range(game.n_actions[j][s]))
        for a in iterproduct(*other_ranges):
            prob = 1.0
            for j in range(game.n_players):
                if j != i:
                    prob *= strategy.mixed_action(j, s)[a[j]]
            if prob < 1e-15:
                continue
            exp_payoff += prob * game.get_payoff(s, a)[i]
            exp_trans += prob * game.get_transition(s, a)
        return exp_payoff, exp_trans

    # Backward induction: V[t][s] = max expected total payoff from stage t to T
    # starting in state s at time t (0-indexed stages t=0..T-1)
    V = np.zeros((T + 1, S))  # V[T] = 0 (no more stages)
    policy = np.zeros((T, S), dtype=int)

    for t in range(T - 1, -1, -1):
        for s in range(S):
            best_val = -np.inf
            best_a = 0
            for a_i in range(game.n_actions[i][s]):
                r, trans = deviator_mdp(s, a_i)
                val = r + trans @ V[t + 1]
                if val > best_val:
                    best_val = val
                    best_a = a_i
            V[t][s] = best_val
            policy[t][s] = best_a

    # Average payoff
    br_value = V[0][s0] / T
    return br_value, policy


# =================================================================
# Regret computation
# =================================================================

def compute_regret(game, strategy, T, s0=None):
    """Compute regret for all players and initial states.

    Regret_{i,T}(sigma, s0) = BR_value_i(T, s0) - gamma_i^T(s0, sigma).

    Returns
    -------
    regret : np.ndarray of shape (n_players, n_states)
        regret[i][s0] = max regret for player i starting from s0
    """
    S = game.n_states
    n = game.n_players
    regret = np.zeros((n, S))

    for s in range(S):
        avg = compute_avg_payoff_exact(game, strategy, T, s)
        for i in range(n):
            br_val, _ = best_response_value(game, strategy, i, T, s)
            regret[i][s] = max(0, br_val - avg[i])

    return regret


def compute_regret_trajectory(game, strategy, T_values, s0=0):
    """Compute max regret across all players for a range of horizons.

    Returns dict with 'T_values', 'max_regret', 'regret_by_player'.
    """
    max_regrets = []
    regret_by_player = {i: [] for i in range(game.n_players)}

    for T in T_values:
        reg = compute_regret(game, strategy, T)
        max_reg = reg.max()
        max_regrets.append(float(max_reg))
        for i in range(game.n_players):
            regret_by_player[i].append(float(reg[i].max()))

    return {
        'T_values': list(T_values),
        'max_regret': max_regrets,
        'regret_by_player': {str(i): v for i, v in regret_by_player.items()},
    }


def check_uniform_equilibrium(game, strategy, epsilon, T_values):
    """Check if strategy is a uniform epsilon-equilibrium over given T range.

    Returns
    -------
    is_uniform : bool
    T0 : int or None (first T where regret <= epsilon)
    max_regret : float
    details : dict
    """
    traj = compute_regret_trajectory(game, strategy, T_values)
    max_regs = traj['max_regret']

    T0 = None
    for idx, (T, mr) in enumerate(zip(T_values, max_regs)):
        if mr <= epsilon:
            if T0 is None:
                T0 = T
        else:
            T0 = None  # Reset: must be uniform from T0 onwards

    is_uniform = T0 is not None
    return is_uniform, T0, max(max_regs), traj


# =================================================================
# Discounted equilibrium solver (fictitious play for n-player)
# =================================================================

def compute_discounted_payoff(game, strategy, delta, s0):
    """Compute discounted payoff for stationary strategy via matrix inversion.

    v_i(s) = (1-delta) * r_i(s) + delta * sum_s' Q(s,s') v_i(s')
    => (I - delta*Q) v_i = (1-delta) * r_i
    """
    S = game.n_states
    Q = np.zeros((S, S))
    r = np.zeros((S, game.n_players))

    for s in range(S):
        aprobs = strategy.action_profile_prob(s)
        for a, prob in aprobs.items():
            if prob < 1e-15:
                continue
            Q[s] += prob * game.get_transition(s, a)
            r[s] += prob * game.get_payoff(s, a)

    I = np.eye(S)
    M = I - delta * Q
    payoffs = np.zeros((S, game.n_players))
    for i in range(game.n_players):
        payoffs[:, i] = np.linalg.solve(M, (1 - delta) * r[:, i])

    return payoffs[s0]


def discounted_best_response_value(game, strategy, deviator, delta, s0):
    """Compute discounted best-response value via value iteration.

    The deviator faces a discounted MDP.
    """
    S = game.n_states
    i = deviator
    tol = 1e-10
    max_iter = 10000

    V = np.zeros(S)
    for _ in range(max_iter):
        V_new = np.zeros(S)
        for s in range(S):
            best_val = -np.inf
            for a_i in range(game.n_actions[i][s]):
                exp_r = 0.0
                exp_trans = np.zeros(S)
                other_ranges = []
                for j in range(game.n_players):
                    if j == i:
                        other_ranges.append([a_i])
                    else:
                        other_ranges.append(range(game.n_actions[j][s]))
                for a in iterproduct(*other_ranges):
                    prob = 1.0
                    for j in range(game.n_players):
                        if j != i:
                            prob *= strategy.mixed_action(j, s)[a[j]]
                    if prob < 1e-15:
                        continue
                    exp_r += prob * game.get_payoff(s, a)[i]
                    exp_trans += prob * game.get_transition(s, a)
                val = (1 - delta) * exp_r + delta * exp_trans @ V
                best_val = max(best_val, val)
            V_new[s] = best_val
        if np.max(np.abs(V_new - V)) < tol:
            break
        V = V_new

    return V[s0]


def fictitious_play_discounted(game, delta, n_iter=5000, seed=42):
    """Compute approximate discounted Nash equilibrium via fictitious play.

    Returns a StationaryStrategy that approximately minimizes regret.
    """
    from stoch_game.solvers import StationaryStrategy
    rng = np.random.RandomState(seed)
    S = game.n_states
    n = game.n_players

    # Initialize with uniform strategies
    counts = []
    for i in range(n):
        ci = []
        for s in range(S):
            n_a = game.n_actions[i][s]
            ci.append(np.ones(n_a))
        counts.append(ci)

    for iteration in range(n_iter):
        # Current mixed strategy from counts
        sigma = []
        for i in range(n):
            si = []
            for s in range(S):
                total = counts[i][s].sum()
                si.append(counts[i][s] / total)
            sigma.append(si)
        strat = StationaryStrategy(game, sigma)

        # Each player best-responds to current average
        for i in range(n):
            # Compute BR via value iteration
            V = np.zeros(S)
            for _ in range(200):
                V_new = np.zeros(S)
                br_actions = np.zeros(S, dtype=int)
                for s in range(S):
                    best_val = -np.inf
                    for a_i in range(game.n_actions[i][s]):
                        exp_r = 0.0
                        exp_trans = np.zeros(S)
                        other_ranges = []
                        for j in range(n):
                            if j == i:
                                other_ranges.append([a_i])
                            else:
                                other_ranges.append(range(game.n_actions[j][s]))
                        for a in iterproduct(*other_ranges):
                            prob = 1.0
                            for j in range(n):
                                if j != i:
                                    prob *= sigma[j][s][a[j]]
                            if prob < 1e-15:
                                continue
                            exp_r += prob * game.get_payoff(s, a)[i]
                            exp_trans += prob * game.get_transition(s, a)
                        val = (1 - delta) * exp_r + delta * exp_trans @ V
                        if val > best_val:
                            best_val = val
                            br_actions[s] = a_i
                    V_new[s] = best_val
                if np.max(np.abs(V_new - V)) < 1e-12:
                    break
                V = V_new

            # Update counts with BR action
            for s in range(S):
                counts[i][s][br_actions[s]] += 1

    # Final strategy
    sigma_final = []
    for i in range(n):
        si = []
        for s in range(S):
            total = counts[i][s].sum()
            si.append(counts[i][s] / total)
        sigma_final.append(si)

    return StationaryStrategy(game, sigma_final)
