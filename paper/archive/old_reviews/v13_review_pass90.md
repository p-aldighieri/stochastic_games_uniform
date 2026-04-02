# v13 Review — Pass 90

**Thinking**: 26 min 41s Extended Pro
**Verdict**: FAIL

## Per-item verdicts
- STRATEGY-INDEPENDENT BLOCK PARTITION: **MOSTLY PASS** — boundaries explicit and strategy-independent, but future node path still action-dependent
- GLOBAL REGRET COMPARISON: **FAIL** — still uses profile-dependent tau(B), not common |B|
- WITHIN-BLOCK EXIT HANDLING: **LOCAL YES, GLOBAL NO** — augmented kernel fine, but global proof treats live-segment identity as controlling whole scheduled block
- DEGENERATE TERMINAL NODES: **PASS**
- PREVIOUSLY VERIFIED COMPONENTS: **PASS**
- MATHEMATICAL COMPLETENESS: **FAIL**

## TWO FATAL ISSUES

### Issue 1: Regret subtraction uses profile-dependent tau(B)
- Realization theorem lower-bounds compliant payoff by g*E[tau_cmp]
- Bellman lemma upper-bounds deviating payoff by g*E[tau_dev]
- Subtraction leaves uncontrolled term g*(E[tau_dev] - E[tau_cmp]) which can be order |B|
- The common block interval B doesn't by itself make the subtraction legal when normalizing times differ

### Issue 2: Augmented/ordinary discrepancy is O(|B|), not O(1)
- Augmented payoff U_i(B) = live-stage payoffs + one continuation term on live segment only
- Omits the remaining |B| - tau(B) stages of the scheduled block
- If a long block exits after one live stage, the omitted part is Theta(|B|)
- One-shot continuation term cannot absorb this

## THE FIX NEEDED (reviewer's suggestion)
A full SCHEDULED-BLOCK PAYOFF IDENTITY:
- Explicitly model what the executed strategy does on the remainder [tau(B), |B|] after cemetery
- Write regret inequality on COMMON DURATION |B|, not profile-dependent tau(B)
- Both compliant and deviating payoffs must be expressed as sums over ALL |B| stages
