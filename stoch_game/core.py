"""Core data structure for finite stochastic games."""

import numpy as np
from itertools import product as iterproduct


class FiniteStochasticGame:
    """A finite stochastic game G = (N, S, (A_i), u, P).

    Parameters
    ----------
    n_players : int
        Number of players.
    n_states : int
        Number of states.
    n_actions : list of list of int
        n_actions[i][s] = number of actions for player i in state s.
        Shape: (n_players, n_states).
    payoffs : dict
        payoffs[(s, a)] = array of shape (n_players,) giving stage payoffs.
        Here a is a tuple of action indices, one per player.
    transitions : dict
        transitions[(s, a)] = array of shape (n_states,) giving P(s'|s,a).
    """

    def __init__(self, n_players, n_states, n_actions, payoffs, transitions):
        self.n_players = n_players
        self.n_states = n_states
        # n_actions[i][s] = number of actions for player i in state s
        self.n_actions = [[n_actions[i][s] for s in range(n_states)]
                          for i in range(n_players)]
        self.payoffs = {}
        self.transitions = {}

        # Validate and store
        for s in range(n_states):
            for a in self._action_profiles(s):
                key = (s, a)
                # Payoffs
                u = np.asarray(payoffs[key], dtype=np.float64)
                assert u.shape == (n_players,), f"Payoff shape mismatch at {key}"
                assert np.all(u >= -1e-9) and np.all(u <= 1.0 + 1e-9), \
                    f"Payoffs out of [0,1] at {key}: {u}"
                self.payoffs[key] = np.clip(u, 0.0, 1.0)

                # Transitions
                p = np.asarray(transitions[key], dtype=np.float64)
                assert p.shape == (n_states,), f"Transition shape mismatch at {key}"
                assert np.all(p >= -1e-9), f"Negative transition prob at {key}"
                assert abs(p.sum() - 1.0) < 1e-6, \
                    f"Transitions don't sum to 1 at {key}: sum={p.sum()}"
                self.transitions[key] = p / p.sum()  # normalize

    def _action_profiles(self, s):
        """Iterate over all action profiles at state s."""
        ranges = [range(self.n_actions[i][s]) for i in range(self.n_players)]
        return iterproduct(*ranges)

    def action_profiles(self, s):
        """Public method: list of all action profiles at state s."""
        return list(self._action_profiles(s))

    def n_action_profiles(self, s):
        """Number of action profiles at state s."""
        result = 1
        for i in range(self.n_players):
            result *= self.n_actions[i][s]
        return result

    def get_payoff(self, s, a):
        """Get payoff vector at (state, action_profile)."""
        return self.payoffs[(s, tuple(a))]

    def get_transition(self, s, a):
        """Get transition distribution at (state, action_profile)."""
        return self.transitions[(s, tuple(a))]


# =================================================================
# Example game constructors
# =================================================================

def make_2player_2state_game():
    """A simple 2-player 2-state 2-action game (matching pennies variant).

    State 0: matching pennies with transition to state 1 on (0,0)
    State 1: coordination game with self-loop
    """
    n_players, n_states = 2, 2
    n_actions = [[2, 2], [2, 2]]  # 2 actions per player per state
    payoffs = {}
    transitions = {}

    # State 0: anti-coordination
    payoffs[(0, (0, 0))] = [0.75, 0.25]
    payoffs[(0, (0, 1))] = [0.25, 0.75]
    payoffs[(0, (1, 0))] = [0.25, 0.75]
    payoffs[(0, (1, 1))] = [0.75, 0.25]

    transitions[(0, (0, 0))] = [0.5, 0.5]
    transitions[(0, (0, 1))] = [1.0, 0.0]
    transitions[(0, (1, 0))] = [1.0, 0.0]
    transitions[(0, (1, 1))] = [0.5, 0.5]

    # State 1: coordination
    payoffs[(1, (0, 0))] = [1.0, 1.0]
    payoffs[(1, (0, 1))] = [0.0, 0.0]
    payoffs[(1, (1, 0))] = [0.0, 0.0]
    payoffs[(1, (1, 1))] = [1.0, 1.0]

    transitions[(1, (0, 0))] = [0.0, 1.0]
    transitions[(1, (0, 1))] = [0.5, 0.5]
    transitions[(1, (1, 0))] = [0.5, 0.5]
    transitions[(1, (1, 1))] = [0.0, 1.0]

    return FiniteStochasticGame(n_players, n_states, n_actions, payoffs, transitions)


def make_3player_3state_game():
    """A 3-player 3-state game with 2 actions each."""
    n_players, n_states = 3, 3
    n_actions = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    payoffs = {}
    transitions = {}

    rng = np.random.RandomState(42)
    for s in range(n_states):
        for a in iterproduct(range(2), range(2), range(2)):
            payoffs[(s, a)] = rng.choice([0.0, 0.25, 0.5, 0.75, 1.0], size=3)
            raw = rng.dirichlet(np.ones(n_states))
            transitions[(s, a)] = raw

    return FiniteStochasticGame(n_players, n_states, n_actions, payoffs, transitions)


def make_absorbing_game():
    """A 2-player absorbing game: state 0 is non-absorbing, state 1 is absorbing.

    This is a simplified 'Big Match' variant.
    """
    n_players, n_states = 2, 2
    n_actions = [[2, 1], [2, 1]]  # In absorbing state 1, only 1 action each
    payoffs = {}
    transitions = {}

    # State 0 (non-absorbing): 2x2 actions
    payoffs[(0, (0, 0))] = [0.5, 0.5]
    payoffs[(0, (0, 1))] = [0.0, 1.0]
    payoffs[(0, (1, 0))] = [1.0, 0.0]
    payoffs[(0, (1, 1))] = [0.5, 0.5]

    # (0,0) and (1,1) stay in state 0; (0,1) and (1,0) absorb to state 1
    transitions[(0, (0, 0))] = [1.0, 0.0]
    transitions[(0, (0, 1))] = [0.0, 1.0]
    transitions[(0, (1, 0))] = [0.0, 1.0]
    transitions[(0, (1, 1))] = [1.0, 0.0]

    # State 1 (absorbing): only one action profile, self-loop
    payoffs[(1, (0, 0))] = [0.5, 0.5]
    transitions[(1, (0, 0))] = [0.0, 1.0]

    return FiniteStochasticGame(n_players, n_states, n_actions, payoffs, transitions)


def make_3player_quitting_game():
    """A 3-player quitting game (single non-absorbing state + absorbing state).

    Each player has 2 actions: Continue (0) or Quit (1).
    If any player quits, the game absorbs.
    Payoffs depend on which players quit.
    """
    n_players, n_states = 3, 2
    # State 0: 2 actions each; State 1 (absorbing): 1 action each
    n_actions = [[2, 1], [2, 1], [2, 1]]
    payoffs = {}
    transitions = {}

    # State 0
    # All continue -> stay in state 0, payoff (1/3, 1/3, 1/3)
    payoffs[(0, (0, 0, 0))] = [1/3, 1/3, 1/3]
    transitions[(0, (0, 0, 0))] = [1.0, 0.0]

    # One quits -> absorb with payoffs favoring quitter
    payoffs[(0, (1, 0, 0))] = [0.75, 0.25, 0.25]
    transitions[(0, (1, 0, 0))] = [0.0, 1.0]

    payoffs[(0, (0, 1, 0))] = [0.25, 0.75, 0.25]
    transitions[(0, (0, 1, 0))] = [0.0, 1.0]

    payoffs[(0, (0, 0, 1))] = [0.25, 0.25, 0.75]
    transitions[(0, (0, 0, 1))] = [0.0, 1.0]

    # Two quit
    payoffs[(0, (1, 1, 0))] = [0.5, 0.5, 0.0]
    transitions[(0, (1, 1, 0))] = [0.0, 1.0]

    payoffs[(0, (1, 0, 1))] = [0.5, 0.0, 0.5]
    transitions[(0, (1, 0, 1))] = [0.0, 1.0]

    payoffs[(0, (0, 1, 1))] = [0.0, 0.5, 0.5]
    transitions[(0, (0, 1, 1))] = [0.0, 1.0]

    # All quit
    payoffs[(0, (1, 1, 1))] = [0.25, 0.25, 0.25]
    transitions[(0, (1, 1, 1))] = [0.0, 1.0]

    # State 1 (absorbing)
    payoffs[(1, (0, 0, 0))] = [0.5, 0.5, 0.5]
    transitions[(1, (0, 0, 0))] = [0.0, 1.0]

    return FiniteStochasticGame(n_players, n_states, n_actions, payoffs, transitions)
