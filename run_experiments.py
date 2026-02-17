#!/usr/bin/env python3
"""Run all experiments for the uniform equilibrium research project."""

import sys
import os
import time

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(__file__))

from stoch_game.experiments import (
    counterexample_search,
    discounted_uniform_bridge,
    run_phase_strategy_experiments,
    memory_analysis,
    self_generation_analysis,
    exhaustive_search_small,
    large_scale_regret,
    sensitivity_analysis,
    plot_regret_trajectories,
    plot_bridge_analysis,
    plot_memory_analysis,
    plot_sensitivity_heatmap,
)


def main():
    start = time.time()

    # Phase 3 experiments
    print("\n" + "="*60)
    print("PHASE 3: Core Research Experiments")
    print("="*60)

    print("\n--- Item 013: Counterexample Search ---")
    t0 = time.time()
    counterexample_search(n_games=50, timeout_per_game=15, seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 014: Discounted-to-Uniform Bridge ---")
    t0 = time.time()
    discounted_uniform_bridge(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 015: Phase-Based Strategy ---")
    t0 = time.time()
    run_phase_strategy_experiments(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 016: Memory Analysis ---")
    t0 = time.time()
    memory_analysis(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 017: Self-Generation ---")
    t0 = time.time()
    self_generation_analysis(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 018: Exhaustive Search ---")
    t0 = time.time()
    exhaustive_search_small(seed=42, timeout=120)
    print(f"  Time: {time.time()-t0:.1f}s")

    # Phase 4 experiments
    print("\n" + "="*60)
    print("PHASE 4: Large-Scale Experiments")
    print("="*60)

    print("\n--- Item 019: Large-Scale Regret ---")
    t0 = time.time()
    large_scale_regret(seed=42, timeout=180)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 023: Sensitivity Analysis ---")
    t0 = time.time()
    sensitivity_analysis(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    # Generate plots
    print("\n" + "="*60)
    print("GENERATING FIGURES")
    print("="*60)

    try:
        plot_regret_trajectories()
        print("  Generated: regret_classification.png/pdf")
    except Exception as e:
        print(f"  Error plotting regret: {e}")

    try:
        plot_bridge_analysis()
        print("  Generated: bridge_convergence.png/pdf")
    except Exception as e:
        print(f"  Error plotting bridge: {e}")

    try:
        plot_memory_analysis()
        print("  Generated: memory_analysis.png/pdf")
    except Exception as e:
        print(f"  Error plotting memory: {e}")

    try:
        plot_sensitivity_heatmap()
        print("  Generated: sensitivity_heatmap.png/pdf")
    except Exception as e:
        print(f"  Error plotting sensitivity: {e}")

    total = time.time() - start
    print(f"\n{'='*60}")
    print(f"ALL EXPERIMENTS COMPLETE. Total time: {total:.1f}s")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
