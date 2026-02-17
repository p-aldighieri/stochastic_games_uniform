#!/usr/bin/env python3
"""Run Phase 4 experiments and generate all plots."""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

from stoch_game.experiments import (
    large_scale_regret,
    sensitivity_analysis,
    plot_regret_trajectories,
    plot_bridge_analysis,
    plot_memory_analysis,
    plot_sensitivity_heatmap,
)


def main():
    start = time.time()

    print("--- Item 019: Large-Scale Regret (fast) ---")
    t0 = time.time()
    large_scale_regret(seed=42, timeout=120)
    print(f"  Time: {time.time()-t0:.1f}s")

    print("\n--- Item 023: Sensitivity Analysis ---")
    t0 = time.time()
    sensitivity_analysis(seed=42)
    print(f"  Time: {time.time()-t0:.1f}s")

    # Generate plots
    print("\n=== GENERATING FIGURES ===")

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
    print(f"\nPhase 4 complete. Total time: {total:.1f}s")


if __name__ == "__main__":
    main()
