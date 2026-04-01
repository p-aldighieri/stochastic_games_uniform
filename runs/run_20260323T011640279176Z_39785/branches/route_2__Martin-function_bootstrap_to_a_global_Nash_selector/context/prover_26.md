# Prover Output (Embedded Communication Lemma)

Generated: 2026-03-27T11:30:00.000000+00:00

## VERDICT: Strong embedded-communication lemma FALSE

Public actions cannot simulate private signals needed for Solan-Vohra-style masked compensation.

## Key findings
- Cheap-talk implementation (Heller-Solan-Tomala) works for 4+ players in cheap-talk EXTENSIONS
- But embedding cheap talk inside original public-action game requires the game to already have a private channel
- Barany's theorem needs 4+ players AND private messages, not just public actions
- Public history generates public correlation only, not private role assignments

## What survives (conditional)
"If the game contains a bounded-length state-preserving private communication gadget, Route C + Solan-Vohra compensation becomes plausible" — a subclass theorem, not the general case.

## The razor-sharp frontier
The missing gadget: private communication embedded inside actual play, not just public branching.
