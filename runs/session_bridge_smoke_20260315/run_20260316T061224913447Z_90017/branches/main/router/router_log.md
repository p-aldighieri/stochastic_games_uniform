# Router Decision

- Phase: formalizer
- Allowed: SEARCHER
- Selected: SEARCHER
- Fallback: yes (router disabled)

# Router Decision

- Phase: searcher
- Allowed: BREAKDOWN
- Selected: BREAKDOWN
- Fallback: yes (router disabled)

# Router Decision

- Phase: breakdown
- Allowed: PROVER, STOP_STALL
- Selected: PROVER
- Fallback: yes (router disabled)

# Router Decision

- Phase: prover
- Allowed: REVIEWER
- Selected: REVIEWER
- Fallback: yes (router disabled)

# Router Decision

- Phase: reviewer
- Allowed: CONSOLIDATOR, PROVER
- Selected: CONSOLIDATOR
- Fallback: yes (router disabled)

# Router Decision

- Phase: consolidator
- Allowed: STOP_PASS
- Selected: STOP_PASS
- Fallback: yes (router disabled)

