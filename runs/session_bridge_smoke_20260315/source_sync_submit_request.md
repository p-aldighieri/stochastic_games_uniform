# Source Sync Submit Smoke

Read the durable project sources available in this ChatGPT project and reply with exactly this JSON object shape:

```json
{
  "project": "Game Theory Proof",
  "smoke_token": "...",
  "main_problem_title": "..."
}
```

Rules:
- Set `"smoke_token"` to the exact smoke token from the durable source file `source_sync_smoke_proof_state.md`.
- Set `"main_problem_title"` to the exact H1 title from `uniform_equilibrium_stochastic_games_problem.md`.
- Return valid JSON only.
