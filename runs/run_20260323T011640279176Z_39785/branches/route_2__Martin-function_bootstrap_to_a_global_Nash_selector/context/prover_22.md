# Prover Output (Route C: History-Dependent Strategies)

Generated: 2026-03-27T07:30:00.000000+00:00

## VERDICT: Route C is the best live route. Real progress, not cosmetic.

## Key findings

1. Deviation taxonomy (4 species):
   - Gain-burning: handled automatically by supermartingale, O(1/T)
   - Off-support gain-neutral: immediately detectable, easy punishment target
   - Within-support gain-neutral: requires blockwise statistical testing (Vieille D1)
   - Transition-tilting: requires exit-behavior tests (Vieille D2)

2. Multiplayer punishment structure (Fudenberg-Maskin):
   - Punish deviator long enough to erase gain
   - Compensate punishers so punishment is self-enforcing
   - Post-punishment reward chosen for punisher indifference

3. THE EXACT FRONTIER:
   "Can one build a state-dependent, self-enforcing coalition punishment-and-reward correspondence that closes the bias gap and composes into one whole-game profile for all initial states?"
   This is the theorem-sized lemma.

## Blueprint
- Normal mode: play x*
- Monitoring: off-support detection + blockwise statistical tests (summable false positives)
- Punishment: coalition approximate minmax for L_i(s) stages
- Compensation/reset: continuation from W(s') to restore punisher incentives

## What's missing
The compensation/reset step for n players. In 2 players, Vieille has it. In n players, it's genuinely new work.

## Recommended next pass
"Prove or refute the statewise self-generating punishment lemma, first in the subclass where after each punishment the terminal state is absorbing or where a public correlating device is available."
