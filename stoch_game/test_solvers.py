"""Tests for solvers: payoff computation, MDP best-response, regret, discounted."""

import numpy as np
from stoch_game.core import (
    make_2player_2state_game, make_absorbing_game, make_3player_quitting_game
)
from stoch_game.solvers import (
    StationaryStrategy, uniform_strategy,
    compute_avg_payoff_exact, compute_avg_payoff_mc,
    best_response_value, compute_regret, compute_regret_trajectory,
    check_uniform_equilibrium,
    compute_discounted_payoff, discounted_best_response_value,
    fictitious_play_discounted,
)


def test_avg_payoff_exact_vs_mc():
    """Compare exact and MC payoff for uniform strategy on 2-player game."""
    g = make_2player_2state_game()
    strat = uniform_strategy(g)
    T = 20
    for s0 in range(g.n_states):
        exact = compute_avg_payoff_exact(g, strat, T, s0)
        mc = compute_avg_payoff_mc(g, strat, T, s0, n_samples=10000, seed=42)
        diff = np.abs(exact - mc)
        assert np.all(diff < 0.05), f"MC vs exact mismatch at s0={s0}: {diff}"
    print("PASS: test_avg_payoff_exact_vs_mc")


def test_best_response_value():
    """Test MDP best-response on absorbing game."""
    g = make_absorbing_game()
    strat = uniform_strategy(g)
    T = 100

    for i in range(g.n_players):
        br_val, policy = best_response_value(g, strat, i, T, s0=0)
        avg_val = compute_avg_payoff_exact(g, strat, T, 0)[i]
        # BR value must be >= average payoff under current strategy
        assert br_val >= avg_val - 1e-6, \
            f"BR value {br_val} < avg {avg_val} for player {i}"
    print("PASS: test_best_response_value")


def test_best_response_pure_coordination():
    """In a pure coordination game with matching payoffs,
    if both players coordinate, BR value should equal the strategy payoff."""
    from stoch_game.core import FiniteStochasticGame
    # Single state, 2 players, 2 actions. Coordination: (0,0)->1,1; (1,1)->1,1; else 0,0
    g = FiniteStochasticGame(
        n_players=2, n_states=1,
        n_actions=[[2], [2]],
        payoffs={
            (0, (0, 0)): [1.0, 1.0],
            (0, (0, 1)): [0.0, 0.0],
            (0, (1, 0)): [0.0, 0.0],
            (0, (1, 1)): [1.0, 1.0],
        },
        transitions={
            (0, (0, 0)): [1.0],
            (0, (0, 1)): [1.0],
            (0, (1, 0)): [1.0],
            (0, (1, 1)): [1.0],
        }
    )
    # Strategy: both always play action 0
    sigma = [
        [np.array([1.0, 0.0])],
        [np.array([1.0, 0.0])],
    ]
    strat = StationaryStrategy(g, sigma)
    T = 50
    avg = compute_avg_payoff_exact(g, strat, T, 0)
    assert np.allclose(avg, [1.0, 1.0]), f"Expected [1,1], got {avg}"

    # BR for player 0: if player 1 plays action 0, BR is also action 0 -> value 1
    br_val, _ = best_response_value(g, strat, 0, T, 0)
    assert abs(br_val - 1.0) < 1e-6, f"BR should be 1.0, got {br_val}"
    print("PASS: test_best_response_pure_coordination")


def test_regret_computation():
    """Test regret on 2-player game."""
    g = make_2player_2state_game()
    strat = uniform_strategy(g)
    T = 50
    reg = compute_regret(g, strat, T)
    assert reg.shape == (2, 2)
    assert np.all(reg >= 0), "Regret should be non-negative"
    print(f"  Regret: {reg}")
    print("PASS: test_regret_computation")


def test_regret_trajectory():
    """Test regret trajectory over multiple horizons."""
    g = make_2player_2state_game()
    strat = uniform_strategy(g)
    T_values = [10, 20, 50, 100]
    traj = compute_regret_trajectory(g, strat, T_values, s0=0)
    assert len(traj['max_regret']) == len(T_values)
    assert all(r >= 0 for r in traj['max_regret'])
    print(f"  Max regret trajectory: {traj['max_regret']}")
    print("PASS: test_regret_trajectory")


def test_uniform_eq_check():
    """Check uniform equilibrium verification on a simple game."""
    g = make_2player_2state_game()
    strat = uniform_strategy(g)
    T_values = list(range(10, 101, 10))
    is_unif, T0, max_reg, details = check_uniform_equilibrium(g, strat, 0.5, T_values)
    print(f"  Uniform eq check: is_uniform={is_unif}, T0={T0}, max_reg={max_reg:.4f}")
    print("PASS: test_uniform_eq_check")


def test_discounted_payoff():
    """Test discounted payoff computation."""
    g = make_2player_2state_game()
    strat = uniform_strategy(g)
    delta = 0.9
    payoff = compute_discounted_payoff(g, strat, delta, 0)
    assert payoff.shape == (2,)
    assert np.all(payoff >= 0) and np.all(payoff <= 1)
    print(f"  Discounted payoff (delta=0.9): {payoff}")
    print("PASS: test_discounted_payoff")


def test_discounted_br():
    """Test discounted best-response."""
    g = make_absorbing_game()
    strat = uniform_strategy(g)
    delta = 0.95
    disc_payoff = compute_discounted_payoff(g, strat, delta, 0)
    br_val = discounted_best_response_value(g, strat, 0, delta, 0)
    # BR value >= strategy payoff
    assert br_val >= disc_payoff[0] - 1e-6
    print(f"  Discounted BR value: {br_val:.4f}, strategy payoff: {disc_payoff[0]:.4f}")
    print("PASS: test_discounted_br")


def test_fictitious_play():
    """Test fictitious play discounted equilibrium solver."""
    g = make_2player_2state_game()
    delta = 0.95
    eq_strat = fictitious_play_discounted(g, delta, n_iter=200, seed=42)
    payoff = compute_discounted_payoff(g, eq_strat, delta, 0)
    print(f"  FP equilibrium payoff (delta=0.95): {payoff}")

    # Check regret is small
    for i in range(g.n_players):
        br_val = discounted_best_response_value(g, eq_strat, i, delta, 0)
        regret = br_val - payoff[i]
        print(f"  Player {i} discounted regret: {regret:.4f}")
        assert regret < 0.15, f"Discounted regret too high: {regret}"
    print("PASS: test_fictitious_play")


if __name__ == "__main__":
    test_avg_payoff_exact_vs_mc()
    test_best_response_value()
    test_best_response_pure_coordination()
    test_regret_computation()
    test_regret_trajectory()
    test_uniform_eq_check()
    test_discounted_payoff()
    test_discounted_br()
    test_fictitious_play()
    print("\nAll solver tests passed!")
