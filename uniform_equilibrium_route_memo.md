# Uniform Equilibrium Route Memo

This memo compresses the stable conclusions from autonomous run
`run_20260323T011640279176Z_39785` into durable context that is safe to
promote into the ChatGPT project. It is intentionally shorter and more stable
than the raw run artifacts.

## Global Status

- The target theorem remains open.
- The run did not produce a certifiable proof.
- The useful output is structural: it identified one cleaner bootstrap route and
  one route whose continuation object appears fundamentally mismatched to the
  cited source.

## Route A: Hybrid Modified-Game Plus Continuation-Orbit Construction

### Status

- Not preferred.
- Reviewer verdict after three cycles: `PATCH_BIG`.

### What survived review

- L1 is acceptable after the coalition-controller repair using product mixed
  actions and a zero-sum uniform-value assumption.
- L3 compactness work is acceptable once a legitimate continuation family exists.
- L5-L7 are conditionally fine once L4 actually supplies the required block map.
- L10-L11 bookkeeping is acceptable only after the endpoint normalization repair.

### Main blocker

- The route tries to upgrade modified-game facts from a fixed initial state to a
  single equilibrium table that works for all states simultaneously.
- The cited modified-game source does not justify that upgrade.
- That means the continuation object feeding L4 is not currently supported.

## Route B: Martin-Function Bootstrap To A Global Nash Selector

### Status

- Preferred current bootstrap route.
- Reviewer verdict after three cycles: `PATCH_BIG`, but with a cleaner repair
  path than Route A.

### Stable positive takeaways

- L5 can be proved by recursion on the full rooted public-history tree once the
  root-bias nonemptiness input from L2 is cited explicitly.
- L7' can be proved by telescoping once the selector exists and the bias bounds
  are available.
- L8' is bookkeeping once `eta_t >= 0` is made explicit.
- The route keeps the theorem-side scope aligned with the durable claim source:
  one public-history behavioral profile, all sufficiently large finite horizons,
  every initial state, no silent downgrade to payoff-set existence.

### Remaining blockers

- L4 is still the theorem-sized unresolved step.
- The route needs an explicit global assembly step from the family `sigma^s`
  into a single whole-game profile.
- L6 as currently written is logically valid but too weak if punishment mode is
  meant to do real work rather than remain vacuous.

## Prompting Guidance For The Next Run

- Keep the theorem labeled as open/bootstrap throughout.
- Ask the model to preserve the exact theorem-side quantifiers and not switch to
  payoff-set wording.
- Push the next run to work with the alternate selector route first.
- Ask for explicit statement repair whenever a lemma proof needs stronger
  dependencies than the current breakdown claims.
- Treat L4 as the central research bottleneck and avoid pretending that later
  bookkeeping closes the theorem without it.
