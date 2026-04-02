# Prover Request: Section 4 — Flux Coordinate Repair (Pass 45)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-28T23:30:00.000000+00:00

## Instructions

You are the prover role. Write the complete Section 4 of our paper: "The Flux Coordinate Repair." The scope gatekeeper says this is 3-4 pages, FULL PROOF standard.

## What This Section Must Contain

1. **The discontinuity example**: A concrete example showing that normalized exit laws q_C(e,.) are discontinuous at zero exit rate. Use the alternating-boundary-law example: witnesses h_n with alpha_n -> 0 and q_n alternating between delta_{b_1} and delta_{b_2}.

2. **The flux coordinate definition**: Define beta_C(e,b) = alpha_C(e) * q_C(e,b) as unnormalized boundary flux.

3. **The continuity theorem**: Prove that in beta-coordinates, the witness map is continuous. The key: ||beta_n||_1 = alpha_n -> 0 regardless of how q_n oscillates.

4. **Why this matters for the paper**: The flux coordinates make the downstream functionals (payoff, deviation values) continuous on the relaxed tree space, which is needed for Kakutani.

## Notation (from v2 draft)

- xi for phase-states (not x)
- beta_C(e,b) = alpha_C(e) * q_C(e,b) — unnormalized flux
- alpha_C — projective exit-rate vector
- q_C(e,.) — normalized exit law (the BAD coordinate)
- Out(C) — exit set

## Output Format

LaTeX-ready mathematical prose. Numbered propositions/examples. ~3-4 pages. Concise and clean — this is a repair section, not the main theorem.
