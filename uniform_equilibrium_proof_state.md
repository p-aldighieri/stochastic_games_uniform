# Uniform Equilibrium Proof State

- Project: Game Theory Proof
- Claim file: `uniform_equilibrium_stochastic_games_problem.md`
- Status: active bootstrap after autonomous run `run_20260323T011640279176Z_39785`
- Theorem status: still open; no proof obtained
- Durable sources intended for the ChatGPT project:
  - `uniform_equilibrium_stochastic_games_problem.md`
  - `uniform_equilibrium_proof_state.md`
  - `uniform_equilibrium_route_memo.md`

## Stable Run Summary

- The first autonomous browser-backed pass completed both the `main` route and one alternate route, then terminated with `STALL`.
- The `main` route was the hybrid modified-game plus continuation-orbit construction.
- The alternate route was the Martin-function bootstrap to a global Nash selector.
- Both routes reached three prover/reviewer cycles and ended with reviewer verdict `PATCH_BIG`.

## Certified Partial Progress

- The project should still be treated as bootstrap rather than proof-complete.
- The literature stage correctly preserved the open-problem reading and did not overclaim a proof of Neyman's problem.
- The `main` route produced some conditionally valid bookkeeping and punishment reductions, but its continuation object remains unsupported.
- The alternate selector route has the cleaner current backbone once amended:
  - L5 works after adding the missing L2 dependency and quantifying over the full rooted public-history tree.
  - L7'/L8' work after an explicit global assembly step and the assumption `eta_t >= 0`.
  - L4 remains the central unresolved theorem-sized step.

## Current Best Route

- Preferred working route: `route_2__Martin-function_bootstrap_to_a_global_Nash_selector`
- Why it is preferred:
  - it preserves the theorem-side scope correctly
  - its post-L4 telescoping/bookkeeping spine is more credible
  - its known defects are structural and explicit rather than hidden

## Main Blockers

- Main route blocker:
  - the modified-game source only supports stationary equilibrium and minmax comparison for a fixed initial state, not one equilibrium table for all states simultaneously
- Alternate route blocker:
  - L4 is still open
  - the global assembly from the family `sigma^s` to one profile on the whole game must be written explicitly
  - L6 is too weak if punishment mode remains vacuous

## Next-Run Guidance

- Do not claim the open theorem is proved.
- Prefer the alternate selector route as the main bootstrap path.
- Treat `main` as a secondary comparison route unless its continuation object is redesigned.
- If durable context is refreshed again, keep only stable route summaries and reviewer-certified blockers here; do not dump raw run artifacts into project Sources.
