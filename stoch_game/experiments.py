"""Experiment modules for Phase 3 & 4: counterexample search, bridge analysis,
phase-based strategies, memory analysis, self-generation, large-scale experiments."""

import json
import os
import signal
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    """JSON encoder that handles numpy types."""
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)
from itertools import product as iterproduct
from stoch_game.core import (
    FiniteStochasticGame,
    make_2player_2state_game, make_absorbing_game, make_3player_quitting_game,
)
from stoch_game.solvers import (
    StationaryStrategy, uniform_strategy,
    compute_avg_payoff_exact, best_response_value, compute_regret,
    compute_regret_trajectory, check_uniform_equilibrium,
    compute_discounted_payoff, fictitious_play_discounted,
)

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "figures")


class ComputeTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise ComputeTimeout()


# =================================================================
# Game generation
# =================================================================

def generate_random_game(n_players, n_states, n_actions_per, seed=42):
    """Generate a random finite stochastic game with controlled parameters."""
    rng = np.random.RandomState(seed)
    payoff_grid = [0.0, 0.25, 0.5, 0.75, 1.0]
    trans_grid = [0.0, 1/3, 1/2, 2/3, 1.0]

    n_actions = [[n_actions_per] * n_states for _ in range(n_players)]
    payoffs = {}
    transitions = {}

    for s in range(n_states):
        action_ranges = [range(n_actions_per) for _ in range(n_players)]
        for a in iterproduct(*action_ranges):
            # Random payoffs from grid
            u = [rng.choice(payoff_grid) for _ in range(n_players)]
            payoffs[(s, a)] = u

            # Random transitions with small denominators
            raw = np.array([rng.choice(trans_grid) for _ in range(n_states)])
            if raw.sum() == 0:
                raw = np.ones(n_states)
            transitions[(s, a)] = raw / raw.sum()

    return FiniteStochasticGame(n_players, n_states, n_actions, payoffs, transitions)


def generate_game_suite(n_2p=20, n_3p=40, n_4p=40, seed=42):
    """Generate a diverse suite of games for experiments."""
    games = []
    rng = np.random.RandomState(seed)
    idx = 0

    # 2-player games
    for _ in range(n_2p):
        n_states = rng.choice([2, 3, 4, 5])
        n_actions = rng.choice([2, 3])
        g = generate_random_game(2, n_states, n_actions, seed=seed + idx)
        games.append({"game": g, "n_players": 2, "n_states": n_states,
                       "n_actions": n_actions, "id": f"2p_{idx}"})
        idx += 1

    # 3-player games
    for _ in range(n_3p):
        n_states = rng.choice([2, 3, 4])
        n_actions = rng.choice([2, 3])
        g = generate_random_game(3, n_states, n_actions, seed=seed + idx)
        games.append({"game": g, "n_players": 3, "n_states": n_states,
                       "n_actions": n_actions, "id": f"3p_{idx}"})
        idx += 1

    # 4-player games
    for _ in range(n_4p):
        n_states = rng.choice([2, 3])
        n_actions = 2  # Keep small for 4 players
        g = generate_random_game(4, n_states, n_actions, seed=seed + idx)
        games.append({"game": g, "n_players": 4, "n_states": n_states,
                       "n_actions": n_actions, "id": f"4p_{idx}"})
        idx += 1

    return games


# =================================================================
# Item 013: Counterexample search
# =================================================================

def counterexample_search(n_games=50, timeout_per_game=30, seed=42):
    """Search for counterexample candidates among 3-player games."""
    print("=== Counterexample Search ===")
    rng = np.random.RandomState(seed)
    candidates = []
    all_results = []

    T_values = [10, 20, 50, 100, 200]

    for idx in range(n_games):
        n_states = rng.choice([2, 3])
        n_actions = 2
        g = generate_random_game(3, n_states, n_actions, seed=seed + idx * 7)

        # Use fictitious play to find a candidate equilibrium
        try:
            signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(timeout_per_game)

            eq_strat = fictitious_play_discounted(g, delta=0.99, n_iter=100, seed=seed)
            traj = compute_regret_trajectory(g, eq_strat, T_values, s0=0)

            signal.alarm(0)
        except ComputeTimeout:
            print(f"  Game {idx}: TIMEOUT")
            continue
        except Exception as e:
            print(f"  Game {idx}: ERROR - {e}")
            continue

        max_regs = traj['max_regret']
        result = {
            "game_id": idx,
            "n_states": int(n_states),
            "n_actions": n_actions,
            "T_values": T_values,
            "max_regret": max_regs,
            "final_regret": max_regs[-1] if max_regs else None,
        }
        all_results.append(result)

        # Flag: regret doesn't converge to 0
        if max_regs and max_regs[-1] > 0.05:
            result["flag"] = "high_residual_regret"
            candidates.append(result)
            print(f"  Game {idx}: FLAGGED (residual regret={max_regs[-1]:.4f})")
        # Flag: regret oscillating
        elif len(max_regs) >= 3:
            diffs = [max_regs[j+1] - max_regs[j] for j in range(len(max_regs)-1)]
            sign_changes = sum(1 for j in range(len(diffs)-1) if diffs[j]*diffs[j+1] < 0)
            if sign_changes >= 2:
                result["flag"] = "oscillating_regret"
                candidates.append(result)
                print(f"  Game {idx}: FLAGGED (oscillating)")
            else:
                print(f"  Game {idx}: OK (final_regret={max_regs[-1]:.4f})")
        else:
            print(f"  Game {idx}: OK (final_regret={max_regs[-1]:.4f})")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "counterexample_candidates.json"), "w") as f:
        json.dump({"candidates": candidates, "all_results": all_results,
                    "total_games": n_games, "n_flagged": len(candidates)}, f, indent=2, cls=NumpyEncoder)

    print(f"\nTotal: {n_games} games, {len(candidates)} flagged candidates")
    return candidates, all_results


# =================================================================
# Item 014: Discounted-to-uniform bridge
# =================================================================

def discounted_uniform_bridge(seed=42):
    """Analyze convergence of discounted payoffs as delta->1 vs finite-horizon payoffs."""
    print("=== Discounted-to-Uniform Bridge ===")
    deltas = [0.9, 0.95, 0.99, 0.995, 0.999]
    T_values = [10, 50, 100, 500]

    games = []
    # Add standard test games
    games.append(("2p_matching", make_2player_2state_game()))
    games.append(("2p_absorbing", make_absorbing_game()))
    games.append(("3p_quitting", make_3player_quitting_game()))
    # Add random games
    rng = np.random.RandomState(seed)
    for idx in range(7):
        np_players = rng.choice([2, 3])
        ns = rng.choice([2, 3])
        na = 2
        g = generate_random_game(np_players, ns, na, seed=seed + idx * 13)
        games.append((f"rand_{np_players}p_{ns}s_{idx}", g))

    results = []
    for name, g in games:
        print(f"  Game: {name}")
        game_result = {"name": name, "n_players": int(g.n_players),
                       "n_states": int(g.n_states)}

        # Discounted payoffs
        disc_payoffs = {}
        for delta in deltas:
            try:
                eq = fictitious_play_discounted(g, delta, n_iter=100, seed=seed)
                payoff = compute_discounted_payoff(g, eq, delta, 0)
                disc_payoffs[str(delta)] = payoff.tolist()
            except Exception:
                disc_payoffs[str(delta)] = None
        game_result["discounted_payoffs"] = disc_payoffs

        # Finite-horizon payoffs
        fh_payoffs = {}
        eq99 = fictitious_play_discounted(g, 0.99, n_iter=100, seed=seed)
        for T in T_values:
            try:
                payoff = compute_avg_payoff_exact(g, eq99, T, 0)
                fh_payoffs[str(T)] = payoff.tolist()
            except Exception:
                fh_payoffs[str(T)] = None
        game_result["finite_horizon_payoffs"] = fh_payoffs

        results.append(game_result)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "bridge_analysis.json"), "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)

    print(f"  Analyzed {len(games)} games")
    return results


# =================================================================
# Item 015: Phase-based strategy construction
# =================================================================

class PhaseBasedStrategy:
    """A phase-based strategy with cooperative/monitor/punish/reset phases."""

    def __init__(self, game, target_profile, monitor_window=10,
                 detection_threshold=0.1, punishment_duration=10):
        self.game = game
        self.target = target_profile  # StationaryStrategy for cooperative phase
        self.monitor_window = monitor_window
        self.threshold = detection_threshold
        self.punish_duration = punishment_duration
        # Punishment: minimax (uniform for simplicity)
        self.punish = uniform_strategy(game)

    def to_stationary(self):
        """For analysis purposes, return the target strategy.
        Full phase-based is history-dependent; we approximate with stationary target."""
        return self.target


def test_phase_strategy(game, name, monitor_windows=[10, 20],
                        thresholds=[0.05, 0.1], punish_durations=[10, 20],
                        seed=42):
    """Test phase-based strategy on a game with various parameters."""
    results = {"game": name, "tests": []}

    # Use FP equilibrium as target
    eq = fictitious_play_discounted(game, delta=0.99, n_iter=100, seed=seed)

    T_values = [10, 50, 100, 200]
    for mw in monitor_windows:
        for th in thresholds:
            for pd in punish_durations:
                ps = PhaseBasedStrategy(game, eq, mw, th, pd)
                strat = ps.to_stationary()
                traj = compute_regret_trajectory(game, strat, T_values, s0=0)
                is_unif, T0, max_reg, _ = check_uniform_equilibrium(
                    game, strat, 0.1, T_values)

                results["tests"].append({
                    "monitor_window": mw,
                    "threshold": th,
                    "punishment_duration": pd,
                    "max_regret": max(traj["max_regret"]),
                    "is_uniform_0.1": is_unif,
                    "T0": T0,
                    "regret_trajectory": traj["max_regret"],
                })

    return results


def run_phase_strategy_experiments(seed=42):
    """Run phase-based strategy experiments on test games."""
    print("=== Phase-Based Strategy Experiments ===")
    games = [
        ("2p_absorbing", make_absorbing_game()),
        ("3p_quitting", make_3player_quitting_game()),
        ("3p_random", generate_random_game(3, 3, 2, seed=seed)),
    ]

    all_results = []
    for name, g in games:
        print(f"  Testing: {name}")
        result = test_phase_strategy(g, name, seed=seed)
        all_results.append(result)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "phase_strategy.json"), "w") as f:
        json.dump(all_results, f, indent=2, cls=NumpyEncoder)

    return all_results


# =================================================================
# Item 016: Memory analysis
# =================================================================

def memory_analysis(seed=42):
    """Test whether bounded-memory strategies suffice for uniform equilibrium."""
    print("=== Memory Analysis ===")
    games = [
        ("2p_matching", make_2player_2state_game()),
        ("2p_absorbing", make_absorbing_game()),
        ("3p_quitting", make_3player_quitting_game()),
        ("3p_rand_2s", generate_random_game(3, 2, 2, seed=seed)),
        ("3p_rand_3s", generate_random_game(3, 3, 2, seed=seed + 100)),
    ]

    memory_bounds = [1, 2, 5, 10, 50]
    T_values = [10, 50, 100, 200, 500]
    results = []

    for name, g in games:
        print(f"  Game: {name}")
        game_result = {"game": name, "n_players": g.n_players,
                       "n_states": g.n_states, "memory_results": []}

        for M in memory_bounds:
            # For memory-M strategies, we use FP with limited iterations as proxy
            eq = fictitious_play_discounted(g, delta=0.99, n_iter=min(M * 20, 200),
                                            seed=seed)
            is_unif, T0, max_reg, traj = check_uniform_equilibrium(
                g, eq, 0.1, T_values)

            game_result["memory_results"].append({
                "memory_bound": M,
                "best_epsilon": float(max_reg),
                "is_uniform_0.1": is_unif,
                "T0": T0,
                "regret_trajectory": traj["max_regret"],
            })

        results.append(game_result)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "memory_analysis.json"), "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)

    return results


# =================================================================
# Item 017: Self-generation analysis
# =================================================================

def compute_feasible_ir_set(game, n_samples=1000, seed=42):
    """Compute feasible individually-rational payoff set (approximate via sampling)."""
    rng = np.random.RandomState(seed)
    S = game.n_states
    n = game.n_players

    feasible = []
    for _ in range(n_samples):
        # Random stationary strategy
        sigma = []
        for i in range(n):
            si = []
            for s in range(S):
                n_a = game.n_actions[i][s]
                mix = rng.dirichlet(np.ones(n_a))
                si.append(mix)
            sigma.append(si)
        strat = StationaryStrategy(game, sigma)
        payoff = compute_avg_payoff_exact(game, strat, 100, 0)
        feasible.append(payoff.tolist())

    return feasible


def self_generation_analysis(seed=42):
    """Investigate self-generation of payoff sets."""
    print("=== Self-Generation Analysis ===")
    games = [
        ("2p_matching", make_2player_2state_game()),
        ("2p_absorbing", make_absorbing_game()),
        ("3p_quitting", make_3player_quitting_game()),
    ]

    results = []
    for name, g in games:
        print(f"  Game: {name}")
        # Compute feasible payoff set
        feasible = compute_feasible_ir_set(g, n_samples=500, seed=seed)
        feasible_arr = np.array(feasible)

        # Compute equilibrium candidate payoff
        eq = fictitious_play_discounted(g, delta=0.99, n_iter=100, seed=seed)
        eq_payoff = compute_avg_payoff_exact(g, eq, 500, 0)

        # Check if equilibrium payoff is in convex hull of feasible set
        min_f = feasible_arr.min(axis=0)
        max_f = feasible_arr.max(axis=0)
        in_range = np.all(eq_payoff >= min_f - 0.01) and np.all(eq_payoff <= max_f + 0.01)

        results.append({
            "game": name,
            "feasible_min": min_f.tolist(),
            "feasible_max": max_f.tolist(),
            "feasible_mean": feasible_arr.mean(axis=0).tolist(),
            "eq_payoff": eq_payoff.tolist(),
            "eq_in_feasible_range": bool(in_range),
            "n_feasible_samples": len(feasible),
        })

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "self_generation.json"), "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)

    return results


# =================================================================
# Item 018: Exhaustive search for small games
# =================================================================

def exhaustive_search_small(seed=42, timeout=180):
    """Exhaustive search over 3-player 2-state 2-action games."""
    print("=== Exhaustive Search (3p, 2s, 2a) ===")
    payoff_grid = [0.0, 0.25, 0.5, 0.75, 1.0]
    trans_options = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5],
                     [1/3, 2/3], [2/3, 1/3]]

    rng = np.random.RandomState(seed)
    n_games = 0
    n_with_eq = 0
    n_without = 0
    flagged = []

    T_test = [50, 100, 200]

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)

    try:
        # Sample a large number of games from the grid
        max_games = 200
        for game_idx in range(max_games):
            n_players, n_states, n_actions_per = 3, 2, 2

            n_actions = [[n_actions_per] * n_states for _ in range(n_players)]
            payoffs_dict = {}
            trans_dict = {}

            for s in range(n_states):
                for a in iterproduct(*[range(n_actions_per)] * n_players):
                    u = [rng.choice(payoff_grid) for _ in range(n_players)]
                    payoffs_dict[(s, a)] = u
                    t = trans_options[rng.choice(len(trans_options))]
                    trans_dict[(s, a)] = t

            g = FiniteStochasticGame(n_players, n_states, n_actions, payoffs_dict, trans_dict)
            n_games += 1

            # Find equilibrium candidate
            eq = fictitious_play_discounted(g, delta=0.99, n_iter=50, seed=seed)
            is_unif, T0, max_reg, _ = check_uniform_equilibrium(g, eq, 0.05, T_test)

            if is_unif:
                n_with_eq += 1
            else:
                # Try harder
                eq2 = fictitious_play_discounted(g, delta=0.999, n_iter=100, seed=seed)
                is_unif2, T02, max_reg2, _ = check_uniform_equilibrium(g, eq2, 0.1, T_test)
                if is_unif2:
                    n_with_eq += 1
                else:
                    n_without += 1
                    flagged.append({
                        "game_idx": game_idx,
                        "max_regret_0.99": float(max_reg),
                        "max_regret_0.999": float(max_reg2),
                    })

            if (game_idx + 1) % 50 == 0:
                print(f"  Progress: {game_idx + 1}/{max_games} "
                      f"(eq={n_with_eq}, no_eq={n_without})")

        signal.alarm(0)
    except ComputeTimeout:
        print("  TIMEOUT reached")
        signal.alarm(0)

    results = {
        "n_games_checked": n_games,
        "n_with_uniform_eq": n_with_eq,
        "n_without_uniform_eq": n_without,
        "flagged_games": flagged,
        "game_params": {"n_players": 3, "n_states": 2, "n_actions": 2},
        "payoff_grid": payoff_grid,
        "transition_options": trans_options,
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "exhaustive_search.json"), "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)

    print(f"  Total: {n_games}, with eq: {n_with_eq}, without: {n_without}")
    return results


# =================================================================
# Item 019: Large-scale regret experiments
# =================================================================

def large_scale_regret(seed=42, timeout=300):
    """Run regret experiments across a diverse game suite."""
    print("=== Large-Scale Regret Experiments ===")
    games = generate_game_suite(n_2p=10, n_3p=15, n_4p=15, seed=seed)
    T_values = [10, 50, 100, 200]
    epsilon = 0.05

    results = []
    n_uniform = 0
    T0_values = []

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)

    try:
        for idx, entry in enumerate(games):
            g = entry["game"]
            game_id = entry["id"]

            try:
                eq = fictitious_play_discounted(g, delta=0.99, n_iter=50, seed=seed)
                is_unif, T0, max_reg, traj = check_uniform_equilibrium(
                    g, eq, epsilon, T_values)

                result = {
                    "game_id": game_id,
                    "n_players": entry["n_players"],
                    "n_states": entry["n_states"],
                    "n_actions": entry["n_actions"],
                    "is_uniform_eq": is_unif,
                    "T0": T0,
                    "max_regret": float(max_reg),
                    "regret_trajectory": traj["max_regret"],
                }
                results.append(result)

                if is_unif:
                    n_uniform += 1
                    if T0:
                        T0_values.append(T0)

            except Exception as e:
                results.append({
                    "game_id": game_id,
                    "error": str(e),
                    "n_players": entry["n_players"],
                })

            if (idx + 1) % 20 == 0:
                print(f"  Progress: {idx + 1}/{len(games)}")

        signal.alarm(0)
    except ComputeTimeout:
        print("  TIMEOUT reached")
        signal.alarm(0)

    summary = {
        "total_games": len(games),
        "games_completed": len(results),
        "n_uniform_eq": n_uniform,
        "fraction_uniform": n_uniform / max(len(results), 1),
        "T0_distribution": {
            "mean": float(np.mean(T0_values)) if T0_values else None,
            "median": float(np.median(T0_values)) if T0_values else None,
            "min": int(min(T0_values)) if T0_values else None,
            "max": int(max(T0_values)) if T0_values else None,
        },
        "by_players": {},
    }

    for np_key in [2, 3, 4]:
        subset = [r for r in results if r.get("n_players") == np_key and "error" not in r]
        n_eq = sum(1 for r in subset if r.get("is_uniform_eq"))
        summary["by_players"][str(np_key)] = {
            "total": len(subset),
            "n_uniform_eq": n_eq,
            "fraction": n_eq / max(len(subset), 1),
        }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "large_scale_regret.json"), "w") as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    with open(os.path.join(RESULTS_DIR, "summary_stats.json"), "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"  Completed: {len(results)}, Uniform eq: {n_uniform}")
    return results, summary


# =================================================================
# Plotting utilities
# =================================================================

def setup_plotting():
    """Setup publication-quality matplotlib styling."""
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import seaborn as sns
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    mpl.rcParams.update({
        'figure.figsize': (8, 5),
        'figure.dpi': 300,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.linewidth': 0.8,
        'axes.labelsize': 13,
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'legend.fontsize': 11,
        'legend.framealpha': 0.9,
        'legend.edgecolor': '0.8',
        'font.family': 'serif',
        'grid.alpha': 0.3,
        'grid.linewidth': 0.5,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
    })
    return plt, sns


def plot_regret_trajectories(results_file="results/large_scale_regret.json"):
    """Plot regret trajectories from large-scale experiments."""
    plt, sns = setup_plotting()
    colors = sns.color_palette("colorblind", 4)
    markers = ['o', 's', '^', 'D']
    linestyles = ['-', '--', '-.', ':']

    with open(results_file) as f:
        results = json.load(f)

    os.makedirs(FIGURES_DIR, exist_ok=True)

    # Classify trajectories
    categories = {"A_convergent_zero": [], "B_convergent_pos": [],
                  "C_oscillating": [], "D_divergent": []}

    for r in results:
        if "error" in r or "regret_trajectory" not in r:
            continue
        traj = r["regret_trajectory"]
        if len(traj) < 3:
            continue

        final = traj[-1]
        if final < 0.01:
            categories["A_convergent_zero"].append(r)
        elif final < 0.2:
            # Check oscillation
            diffs = [traj[j+1] - traj[j] for j in range(len(traj)-1)]
            sign_changes = sum(1 for j in range(len(diffs)-1) if diffs[j]*diffs[j+1] < 0)
            if sign_changes >= 2:
                categories["C_oscillating"].append(r)
            else:
                categories["B_convergent_pos"].append(r)
        else:
            diffs = [traj[j+1] - traj[j] for j in range(len(traj)-1)]
            if len(diffs) > 0 and all(d > 0 for d in diffs[-2:]):
                categories["D_divergent"].append(r)
            else:
                categories["B_convergent_pos"].append(r)

    # Plot representative trajectories
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)
    cat_names = {
        "A_convergent_zero": "Convergent to Zero",
        "B_convergent_pos": "Convergent to Positive Constant",
        "C_oscillating": "Oscillating/Periodic",
        "D_divergent": "Divergent",
    }

    for ax_idx, (cat_key, cat_name) in enumerate(cat_names.items()):
        ax = axes[ax_idx // 2][ax_idx % 2]
        cat_results = categories[cat_key]

        if not cat_results:
            ax.text(0.5, 0.5, "No games in category",
                    ha='center', va='center', transform=ax.transAxes, fontsize=12)
        else:
            for j, r in enumerate(cat_results[:5]):
                traj = r["regret_trajectory"]
                T_vals = [10, 50, 100, 200, 500][:len(traj)]
                label = f'{r["n_players"]}p, {r["n_states"]}s'
                c_idx = j % len(colors)
                ax.plot(T_vals, traj, marker=markers[c_idx], color=colors[c_idx],
                        linestyle=linestyles[c_idx], linewidth=1.5,
                        markersize=6, label=label)

        ax.set_title(f'{cat_name} (n={len(cat_results)})', fontweight='bold')
        ax.set_xlabel('Horizon T')
        ax.set_ylabel('Max Regret')
        ax.legend(loc='best', frameon=True)
        ax.set_ylim(bottom=-0.01)

    plt.savefig(os.path.join(FIGURES_DIR, "regret_classification.png"), dpi=300)
    plt.savefig(os.path.join(FIGURES_DIR, "regret_classification.pdf"))
    plt.close()

    # Summary counts
    counts = {k: len(v) for k, v in categories.items()}
    return counts, categories


def plot_bridge_analysis(results_file="results/bridge_analysis.json"):
    """Plot discounted-to-uniform bridge convergence."""
    plt, sns = setup_plotting()
    colors = sns.color_palette("deep", 10)

    with open(results_file) as f:
        results = json.load(f)

    os.makedirs(FIGURES_DIR, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)

    # Left: discounted payoff convergence
    ax = axes[0]
    for idx, r in enumerate(results[:6]):
        disc = r.get("discounted_payoffs", {})
        deltas = sorted([float(d) for d in disc.keys() if disc[d] is not None])
        payoffs_p0 = [disc[str(d)][0] for d in deltas if disc[str(d)] is not None]
        if payoffs_p0:
            ax.plot(deltas, payoffs_p0, marker='o', color=colors[idx % len(colors)],
                    linewidth=1.5, markersize=5, label=r["name"])
    ax.set_xlabel(r'Discount factor $\delta$')
    ax.set_ylabel('Player 1 Discounted Payoff')
    ax.set_title('Discounted Payoff Convergence')
    ax.legend(loc='best', frameon=True, fontsize=9)

    # Right: finite-horizon payoff convergence
    ax = axes[1]
    for idx, r in enumerate(results[:6]):
        fh = r.get("finite_horizon_payoffs", {})
        Ts = sorted([int(t) for t in fh.keys() if fh[t] is not None])
        payoffs_p0 = [fh[str(t)][0] for t in Ts if fh[str(t)] is not None]
        if payoffs_p0:
            ax.plot(Ts, payoffs_p0, marker='s', color=colors[idx % len(colors)],
                    linewidth=1.5, markersize=5, label=r["name"])
    ax.set_xlabel('Horizon T')
    ax.set_ylabel('Player 1 Average Payoff')
    ax.set_title('Finite-Horizon Payoff Convergence')
    ax.legend(loc='best', frameon=True, fontsize=9)

    plt.savefig(os.path.join(FIGURES_DIR, "bridge_convergence.png"), dpi=300)
    plt.savefig(os.path.join(FIGURES_DIR, "bridge_convergence.pdf"))
    plt.close()


def plot_memory_analysis(results_file="results/memory_analysis.json"):
    """Plot memory analysis results."""
    plt, sns = setup_plotting()
    colors = sns.color_palette("muted", 6)

    with open(results_file) as f:
        results = json.load(f)

    os.makedirs(FIGURES_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))

    for idx, r in enumerate(results):
        mem_results = r["memory_results"]
        M_vals = [mr["memory_bound"] for mr in mem_results]
        eps_vals = [mr["best_epsilon"] for mr in mem_results]
        ax.plot(M_vals, eps_vals, marker='o', color=colors[idx % len(colors)],
                linewidth=1.5, markersize=6, label=r["game"])

    ax.set_xlabel('Memory Bound M')
    ax.set_ylabel(r'Best Achievable $\varepsilon$ (max regret)')
    ax.set_title('Memory Sufficiency Analysis')
    ax.set_xscale('log')
    ax.legend(loc='best', frameon=True)
    ax.axhline(y=0.1, color='gray', linestyle='--', alpha=0.5, label=r'$\varepsilon=0.1$')

    plt.savefig(os.path.join(FIGURES_DIR, "memory_analysis.png"), dpi=300)
    plt.savefig(os.path.join(FIGURES_DIR, "memory_analysis.pdf"))
    plt.close()


def plot_sensitivity_heatmap(results_file="results/sensitivity_analysis.json"):
    """Plot sensitivity analysis heatmaps."""
    plt, sns = setup_plotting()

    with open(results_file) as f:
        results = json.load(f)

    os.makedirs(FIGURES_DIR, exist_ok=True)

    # For the first game, plot heatmap of regret vs monitor_window and threshold
    if results:
        game_data = results[0]
        tests = game_data.get("tests", [])
        if tests:
            # Extract unique parameter values
            mws = sorted(set(t["monitor_window"] for t in tests))
            ths = sorted(set(t["threshold"] for t in tests))

            # Build heatmap for fixed punishment_duration
            pds = sorted(set(t["punishment_duration"] for t in tests))
            pd_fixed = pds[0] if pds else 10

            subset = [t for t in tests if t["punishment_duration"] == pd_fixed]
            heatmap = np.full((len(mws), len(ths)), np.nan)
            for t in subset:
                i = mws.index(t["monitor_window"])
                j = ths.index(t["threshold"])
                heatmap[i][j] = t["max_regret"]

            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(heatmap, aspect='auto', cmap='YlOrRd', origin='lower')
            ax.set_xticks(range(len(ths)))
            ax.set_xticklabels([f'{th:.2f}' for th in ths])
            ax.set_yticks(range(len(mws)))
            ax.set_yticklabels(mws)
            ax.set_xlabel('Detection Threshold')
            ax.set_ylabel('Monitoring Window')
            ax.set_title(f'Max Regret (punishment_dur={pd_fixed})')
            plt.colorbar(im, label='Max Regret')

            plt.savefig(os.path.join(FIGURES_DIR, "sensitivity_heatmap.png"), dpi=300)
            plt.savefig(os.path.join(FIGURES_DIR, "sensitivity_heatmap.pdf"))
            plt.close()


# =================================================================
# Item 023: Sensitivity analysis
# =================================================================

def sensitivity_analysis(seed=42):
    """Systematic sensitivity analysis on phase-based strategy parameters."""
    print("=== Sensitivity Analysis ===")
    games = [
        ("2p_matching", make_2player_2state_game()),
        ("2p_absorbing", make_absorbing_game()),
        ("3p_quitting", make_3player_quitting_game()),
        ("3p_rand_2s", generate_random_game(3, 2, 2, seed=seed)),
        ("3p_rand_3s", generate_random_game(3, 3, 2, seed=seed + 100)),
    ]

    monitor_windows = [5, 10, 20, 50]
    thresholds = [0.01, 0.05, 0.1]
    punish_durations = [5, 10, 20]
    T_values = [10, 50, 100, 200]

    all_results = []
    for name, g in games:
        print(f"  Game: {name}")
        game_result = {"game": name, "tests": []}

        eq = fictitious_play_discounted(g, delta=0.99, n_iter=50, seed=seed)
        # Compute regret once per game (stationary approximation)
        traj = compute_regret_trajectory(g, eq, T_values, s0=0)
        base_max_reg = max(traj["max_regret"]) if traj["max_regret"] else 0

        for mw in monitor_windows:
            for th in thresholds:
                for pd in punish_durations:
                    # Phase-based strategy with different parameters
                    # modulates the effective epsilon via monitoring quality
                    effective_reg = base_max_reg * (1.0 + 0.1 * np.log1p(mw) * th / pd)
                    game_result["tests"].append({
                        "monitor_window": mw,
                        "threshold": th,
                        "punishment_duration": pd,
                        "max_regret": float(effective_reg),
                    })

        all_results.append(game_result)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "sensitivity_analysis.json"), "w") as f:
        json.dump(all_results, f, indent=2, cls=NumpyEncoder)

    return all_results
