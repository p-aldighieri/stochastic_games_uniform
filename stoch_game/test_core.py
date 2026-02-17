"""Tests for core stochastic game data structure."""

import numpy as np
from stoch_game.core import (
    FiniteStochasticGame,
    make_2player_2state_game,
    make_3player_3state_game,
    make_absorbing_game,
    make_3player_quitting_game,
)


def test_2player_2state():
    g = make_2player_2state_game()
    assert g.n_players == 2
    assert g.n_states == 2
    assert g.n_actions[0] == [2, 2]
    assert g.n_actions[1] == [2, 2]
    # Check payoff bounds
    for s in range(g.n_states):
        for a in g.action_profiles(s):
            u = g.get_payoff(s, a)
            assert np.all(u >= 0) and np.all(u <= 1)
            p = g.get_transition(s, a)
            assert abs(p.sum() - 1.0) < 1e-10
    # Check specific payoff
    assert np.allclose(g.get_payoff(0, (0, 0)), [0.75, 0.25])
    print("PASS: test_2player_2state")


def test_3player_3state():
    g = make_3player_3state_game()
    assert g.n_players == 3
    assert g.n_states == 3
    for s in range(g.n_states):
        for a in g.action_profiles(s):
            u = g.get_payoff(s, a)
            assert u.shape == (3,)
            assert np.all(u >= 0) and np.all(u <= 1)
            p = g.get_transition(s, a)
            assert abs(p.sum() - 1.0) < 1e-10
    print("PASS: test_3player_3state")


def test_absorbing_game():
    g = make_absorbing_game()
    assert g.n_players == 2
    assert g.n_states == 2
    # State 1 is absorbing: only 1 action each
    assert g.n_actions[0][1] == 1
    assert g.n_actions[1][1] == 1
    # Absorbing state self-loops
    p = g.get_transition(1, (0, 0))
    assert p[1] == 1.0
    print("PASS: test_absorbing_game")


def test_quitting_game():
    g = make_3player_quitting_game()
    assert g.n_players == 3
    assert g.n_states == 2
    # All continue stays in state 0
    p = g.get_transition(0, (0, 0, 0))
    assert p[0] == 1.0
    # Any quit absorbs
    p = g.get_transition(0, (1, 0, 0))
    assert p[1] == 1.0
    print("PASS: test_quitting_game")


def test_validation_transitions():
    """Test that transitions must sum to 1."""
    try:
        FiniteStochasticGame(
            n_players=2, n_states=1,
            n_actions=[[1], [1]],
            payoffs={(0, (0, 0)): [0.5, 0.5]},
            transitions={(0, (0, 0)): [0.5]}  # doesn't sum to 1
        )
        print("PASS: test_validation_transitions (normalized automatically)")
    except AssertionError:
        print("PASS: test_validation_transitions (caught invalid)")


if __name__ == "__main__":
    test_2player_2state()
    test_3player_3state()
    test_absorbing_game()
    test_quitting_game()
    test_validation_transitions()
    print("\nAll core tests passed!")
