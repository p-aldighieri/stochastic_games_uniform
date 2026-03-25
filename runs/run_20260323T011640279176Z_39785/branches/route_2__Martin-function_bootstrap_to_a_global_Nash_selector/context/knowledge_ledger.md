# Knowledge Ledger

## prover_01.md
- [BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- [BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- [DERIVED] L5 is proved, conditional on the dependency/scope repairs above.
- [BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- [DERIVED] The literal L6 is proved.
- [BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- [BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- [DERIVED] L7′ is proved.
- [DERIVED] L7 is proved, and in fact sharpened.
- [BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- [DERIVED] L8 is proved.
- [BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.
- [DERIVED] L8′ is proved.
- [BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
- [DERIVED] Current lemma status:
- [DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## prover_02.md
- [BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- [BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- [DERIVED] L5 is proved, conditional on the dependency/scope repairs above.
- [BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- [DERIVED] The literal L6 is proved.
- [BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- [BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- [DERIVED] L7′ is proved.
- [DERIVED] L7 is proved, and in fact sharpened.
- [BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- [DERIVED] L8 is proved.
- [BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.
- [DERIVED] L8′ is proved.
- [BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
- [DERIVED] Current lemma status:
- [DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## prover_03.md
- [BREAKDOWN_AMEND] L5 as written needs one repair before the proof starts: to choose the root bias (\beta((s))), one needs the nonemptiness of (B_\delta((s),v^s)), which comes from L2, not from L4 alone. So either add L2 to the dependencies of L5, or strengthen L4 so that it also returns an admissible current bias when only (h) and (v) are given.
- [BREAKDOWN_AMEND] L5 should quantify over the full rooted public-history tree starting from (s), not merely “reachable” histories in an on-path sense. The later deviation analysis in L7 needs (\beta(h)) and (x(h)) on histories created by arbitrary unilateral deviations.
- [DERIVED] L5 is proved, conditional on the dependency/scope repairs above.
- [BREAKDOWN_AMEND] As written, item 2 of L6 is ambiguous if punishment mode is ever actually used. A mode variable (M_t\in{\mathrm{normal}}\cup N) remembers only the punished player, not the history at which the punishment began. If the intended meaning is “after switching at history (h), continue with the whole strategy (p^{i,h}),” then the public mode needs to remember that anchor history, or an equivalent finite/public encoding of it. The literal statement below is still provable.
- [DERIVED] The literal L6 is proved.
- [BREAKDOWN_AMEND] If L6 is intended to play a non-vacuous role in L7, it must be strengthened to specify an actual switching rule and a public state rich enough to remember the punishment anchor.
- [BREAKDOWN_AMEND] L7 should list L2 explicitly among its dependencies, because the proof uses the bias bound (C_\delta).
- [DERIVED] L7′ is proved.
- [DERIVED] L7 is proved, and in fact sharpened.
- [BREAKDOWN_AMEND] Replace the current L7 by L7′ above. After L4 and L5 are available, the deviation verification is a direct telescope; L6 is not needed for this step, and the (\pm 2\delta) slack is unnecessary.
- [DERIVED] L8 is proved.
- [BREAKDOWN_AMEND] Under L7′, the closing step can be sharpened substantially.
- [DERIVED] L8′ is proved.
- [BREAKDOWN_AMEND] The dependency spine can be shortened after the open selector step:
- [DERIVED] Current lemma status:
- [DERIVED] So the post-L4 terrain is now cleared: once a product-form one-step selector of the strength demanded by L4 exists, the rest of the route can be completed by explicit recursion and telescoping. The unresolved mass is concentrated in L1 through L4, especially L4, exactly where the packet already flags the missing-convexity hazard.

## prover_04.md
- [BREAKDOWN_AMEND] Use the corrected post-L4 backbone
- [DERIVED] **Sublemma A.** For each depth (t\ge 1), the layer (H_t) of public histories of length (t) is finite. Hence (H=\bigcup_{t\ge1}H_t) is countable.
- [DERIVED] **L3, sharpened.** For every public history (h) and every (w\in W(h)), the set (F(h,w)) is compact, possibly empty. Its graph is closed on each depth layer.
- [DERIVED] **L5, strengthened full-tree form, conditional on L4.** Assume L4. Choose one root promise (w(s)\in W(s)) for each root (s\in S), which is possible by L2. Then there exists a single family
- [DERIVED] **Explicit global assembly corollary.** If one first runs the same construction separately on each rooted subtree with initial state (s), obtaining rooted profiles (\sigma^s), then one global whole-game profile is
- [DERIVED] **L6.** Let (\sigma) be the profile from strengthened L5. Then for every initial state (s), player (i), and horizon (T\ge1),
- [BREAKDOWN_AMEND] The proof above establishes only the literal displayed statement of L6. It does **not** build a non-vacuous punishment-mode mechanism. Any stronger “switch to a punishment plan anchored at a remembered history” reading remains unproved unless the public state is enriched to remember that anchor.
- [BREAKDOWN_AMEND] Replace the old L7 by the following corrected version.
- [BREAKDOWN_AMEND] Replace L8 by the following corrected version, which explicitly cites the standing hypothesis (\eta_t\ge0).
- [DERIVED] **L8′.** Under L1, L6, and L7′, for every initial state (s), player (i), deviation (\tau_i), and horizon (T\ge1),
- [DERIVED] **Conditional close of the route.** Assume L1, L2, and L4. Fix (G) and (\varepsilon>0), and choose any summable nonnegative leakage schedule ((\eta_t)). By L2 choose root promises (w(s)\in W(s)). By strengthened L5, construct one global public-history behavioral profile (\sigma) on all of (H). By L6 and L7′ compare equilibrium and deviating path values with terminal promise corrections. By L8′ choose (T_0) so that for every (T\ge T_0),
- [BREAKDOWN_AMEND] The remaining gap is now cleanly localized. L1 and L2 remain imported. L4 remains the unresolved selector theorem. Everything after L4 is tree recursion plus telescoping bookkeeping.

## prover_05.md
- [BREAKDOWN_AMEND] I will use the typed reading
- [DERIVED] **Lemma L1.** For every public history (h), the continuation game (G_h) is again a finite stochastic game of the same class. For every player (i), horizon (T), and opponents’ profile (\sigma_{-i}) on (G_h), the value
- [DERIVED] **Lemma L3.** For fixed (h) and ((w,b)\in\mathcal C(h)), the local feasibility relation (\mathcal F(h,w,b)) is compact.
- [DERIVED] **Lemma L5.** Assuming L2 and L4, the rooted recursion statement holds as written.
- [DERIVED] **Lemma L6.** Assuming the rooted objects of L5 for every initial state, the global assembly statement holds in its literal disjoint-union form.
- [DERIVED] **Weak telescope under the current L5-L6 data.** Assume L2, L5, and L6 as currently written. Fix an initial state (s), player (i), a horizon (T), and a unilateral deviation (\tau_i). Let (H_t) denote the random public history at stage (t).
- [BREAKDOWN_AMEND] The weak telescope is the exact output of the current L3-L6 data. It does **not** imply the displayed L7' in the packet, because the right-hand sides contain the visited promise process (w_i(H_t)), not the root promise (w_i^s). Also, the expectation in (WT-ob) is taken under obedient play and the expectation in (WT-dev) under deviating play, so the promise averages do not cancel. The current local relation uses successor **biases** but never successor **promises**, so no fixed-promise invariant is propagated. Therefore the current L7' requires a genuine amendment upstream, at L3-L4, exactly where the route memo says amendments should be made first.
- [BREAKDOWN_AMEND] For each history (h) and promise vector (w\in[0,1]^N), define the bias fiber
- [DERIVED] **L3* is compact.**
- [DERIVED] **L5* follows by the same depth recursion as L5.**
- [DERIVED] **The literal assembly lemma L6 also works for the corrected L5*.**
- [DERIVED] **Corrected L7'.** Assume L2, corrected L5*, and the literal assembly lemma L6. Then for every initial state (s), every player (i), every unilateral deviation (\tau_i), and every horizon (T),
- [DERIVED] **Lemma L8'.** Assume (\eta_t\ge 0) for all (t) and (\sum_{t\ge1}\eta_t\le \varepsilon/4). Then there exists (T_0) such that for all (T\ge T_0),
- [DERIVED] **Conditional theorem for the repaired post-L4 tail.** Suppose L2 is available as imported Martin-function input, and suppose the strengthened fixed-promise selector L4* holds. Then for every finite stochastic game (G) and every (\varepsilon>0), the repaired Route B yields one global public-history behavioral profile (\sigma) and one threshold (T_0) such that for every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
- [DERIVED] **Proved in this pass.**
- [BREAKDOWN_AMEND] **Required packet repair.**
- [DERIVED] **What remains open.**

## prover_06.md
- [BREAKDOWN_AMEND] I will use the typed reading
- [DERIVED] **Lemma L1.** For every public history (h), the continuation game (G_h) is again a finite stochastic game of the same class. For every player (i), horizon (T), and opponents’ profile (\sigma_{-i}) on (G_h), the value
- [DERIVED] **Lemma L3.** For fixed (h) and ((w,b)\in\mathcal C(h)), the local feasibility relation (\mathcal F(h,w,b)) is compact.
- [DERIVED] **Lemma L5.** Assuming L2 and L4, the rooted recursion statement holds as written.
- [DERIVED] **Lemma L6.** Assuming the rooted objects of L5 for every initial state, the global assembly statement holds in its literal disjoint-union form.
- [DERIVED] **Weak telescope under the current L5-L6 data.** Assume L2, L5, and L6 as currently written. Fix an initial state (s), player (i), a horizon (T), and a unilateral deviation (\tau_i). Let (H_t) denote the random public history at stage (t).
- [BREAKDOWN_AMEND] The weak telescope is the exact output of the current L3-L6 data. It does **not** imply the displayed L7' in the packet, because the right-hand sides contain the visited promise process (w_i(H_t)), not the root promise (w_i^s). Also, the expectation in (WT-ob) is taken under obedient play and the expectation in (WT-dev) under deviating play, so the promise averages do not cancel. The current local relation uses successor **biases** but never successor **promises**, so no fixed-promise invariant is propagated. Therefore the current L7' requires a genuine amendment upstream, at L3-L4, exactly where the route memo says amendments should be made first.
- [BREAKDOWN_AMEND] For each history (h) and promise vector (w\in[0,1]^N), define the bias fiber
- [DERIVED] **L3* is compact.**
- [DERIVED] **L5* follows by the same depth recursion as L5.**
- [DERIVED] **The literal assembly lemma L6 also works for the corrected L5*.**
- [DERIVED] **Corrected L7'.** Assume L2, corrected L5*, and the literal assembly lemma L6. Then for every initial state (s), every player (i), every unilateral deviation (\tau_i), and every horizon (T),
- [DERIVED] **Lemma L8'.** Assume (\eta_t\ge 0) for all (t) and (\sum_{t\ge1}\eta_t\le \varepsilon/4). Then there exists (T_0) such that for all (T\ge T_0),
- [DERIVED] **Conditional theorem for the repaired post-L4 tail.** Suppose L2 is available as imported Martin-function input, and suppose the strengthened fixed-promise selector L4* holds. Then for every finite stochastic game (G) and every (\varepsilon>0), the repaired Route B yields one global public-history behavioral profile (\sigma) and one threshold (T_0) such that for every (T\ge T_0), every initial state (s), every player (i), and every unilateral deviation (\tau_i),
- [DERIVED] **Proved in this pass.**
- [BREAKDOWN_AMEND] **Required packet repair.**
- [DERIVED] **What remains open.**

## prover_09.md
- [DERIVED] I keep the route explicitly **open/bootstrap**, and I preserve the exact theorem-side target: one behavioral profile (\sigma), one threshold (T_0), all sufficiently large horizons, every initial state, every player, and every unilateral deviation. That is the durable project status and the adopted formal claim.
- [BREAKDOWN_AMEND] The downstream proof should use the **increment form** of the current breakdown’s local invariant and should stop citing the canceled-promise formulas from the superseded prover_07 setup. The current breakdown already has a fixed root promise (\rho^s) and a varying bias (b^s(h)):
- [ASSUMPTION+] For the closed-graph clause in L3, equip (H^s=\bigsqcup_{t\ge 1}H_t^s) with the disjoint-union topology of its finite depth layers. Equivalently, (H^s) is a countable discrete space.
- [ASSUMPTION+] (**ZU**) Every finite-state two-player zero-sum stochastic game with compact metric action sets and continuous payoff/transition data has a uniform value, and each player has uniformly (\delta)-optimal strategies.
- [DERIVED] **L1**, conditional on [ASSUMPTION+] ZU.
- [DERIVED] **L3**.
- [BREAKDOWN_AMEND] The L5 proof does **not** need a Kőnig-style compactness limit once L4 is available on the full rooted tree. Direct recursion on depth is enough. Also, L5 must cite L2 for the root bias choice. This matches the accepted amendment and the stable route-memo takeaway.
- [DERIVED] **L5**, conditional on L2 and L4.
- [BREAKDOWN_AMEND] Demote L6 to the **literal** statement that L5 defines a rooted behavioral profile. Do not cite L6 as a nonvacuous punishment-mode mechanism unless the public state is enlarged to remember punishment anchors. The route memo explicitly warns that the current stronger punishment reading is too weak / vacuous.
- [DERIVED] **Literal L6.**
- [BREAKDOWN_AMEND] Replace the current L7 by the following corrected lemma. Its proof uses only L2 and the full-tree L5 selector; L6 is not needed.
- [DERIVED] **L7′**.
- [BREAKDOWN_AMEND] Replace the current L8 by the corrected bookkeeping lemma below, with explicit use of (\eta_t\ge 0).
- [DERIVED] **L8′**.
- [BREAKDOWN_AMEND] The present L9 asks for a stronger current-state re-rooting compatibility:
- [DERIVED] **L9′**.
- [BREAKDOWN_AMEND] Replace the downstream backbone by
- [DERIVED] **Conditional L10.**
- [DERIVED] In this pass I have advanced the route as follows.

## prover_10.md
- [BREAKDOWN_AMEND] I normalize the live Route B backbone to the fixed-promise version
- [BREAKDOWN_AMEND] Replace the canceled-promise setup by the fixed-promise local increment system.
- [DERIVED] **Corrected L3(^\ast), compactness half.** For every (s\in S), every (h\in H^s), and every (b\in W^\star(h)), the set (F_s^\ast(h,b)) is compact.
- [ASSUMPTION+] **L4(^\ast), nonemptiness/selector half.** For every (s\in S), every (h\in H^s), and every current bias (b\in W^\star(h)), the set (F_s^\ast(h,b)) is nonempty. Equivalently, there exists a one-step fixed-promise selector at every node. This is the theorem-sized unresolved step in the present route.
- [DERIVED] **L5(^\ast), rooted full-tree recursion.** Assume L2 and L4(^\ast). Then for every initial state (s\in S) there exist maps
- [DERIVED] **Literal L6.** For each (s\in S), the selector from L5(^\ast) defines a rooted behavioral profile
- [DERIVED] **Corrected L7′, rooted telescoping deviation bound.** Assume L2 and L5(^\ast). Fix (s\in S), (i\in N), (T\ge1), and a unilateral behavioral deviation (\tau_i). Then
- [ASSUMPTION+] **Controlled leakage schedule.** I now add the explicit quantitative input that the selector can be chosen with a depth budget
- [DERIVED] **Corrected L8′, threshold extraction.** Under the controlled leakage schedule above, for every (s\in S), every player (i), every deviation (\tau_i), and every (T\ge1),
- [DERIVED] **L9′, disjoint-union global assembly.** There exists one whole-game behavioral profile (\sigma\in\Sigma(G)) such that for every initial state (s\in S), every history (h\in H^s), and every player (i),
- [DERIVED] **L10, conditional synthesis.** Assume imported L1, imported L2, the proved compactness half of corrected L3(^\ast), the open selector hypothesis L4(^\ast), and the controlled leakage schedule. Then for every finite stochastic game (G) and every (\varepsilon>0) there exist
- [BREAKDOWN_AMEND] Old L6 should be demoted to literal strategy construction only; it is not needed in the deviation proof. Old L7 and old L8 should be retired and replaced by corrected L7′ and L8′ above. The present packet should also record that L5(^\ast) depends on L2 for the root choice and must quantify over the full rooted tree, not just on-path histories.
- [BREAKDOWN_AMEND] The official breakdown should mark L4(^\ast), not the old variable-promise L4, as the live research bottleneck. The local fixed-promise system above is the one that actually supports the root-promise telescope.

## reviewer_01.md
- [SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

## reviewer_02.md
- [SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

## reviewer_03.md
- [SCOPE] There is no theorem-side scope drift relative to the durable target. The packet stays within the strategy-existence formulation of uniform (\varepsilon)-equilibrium for finite stochastic games with perfect public monitoring, behavioral public-history strategies, finite-horizon average payoff, and equilibrium inequalities for **every** initial state. It does not silently switch to payoff-set wording, exact equilibrium, stationary/Markov restrictions, or private monitoring.

## reviewer_05.md
- [SCOPE] The theorem-side scope is preserved. The packet still targets the adopted claim: one behavioral public-history profile (\sigma), one threshold (T_0), all sufficiently large finite horizons, and every initial state, with approximate Nash inequalities under expected finite-horizon average payoff. It does **not** silently downgrade to payoff-set existence, fixed-initial-state existence, stationary/finite-memory existence, discounted payoff, or an augmented public-randomization model. The durable claim source and the route memo both align with that scope. The fixed-promise repair is an internal lemma reformulation, not a theorem-side scope change.

## reviewer_06.md
- [SCOPE] The theorem-side scope is preserved. The packet still targets the adopted claim: one behavioral public-history profile (\sigma), one threshold (T_0), all sufficiently large finite horizons, and every initial state, with approximate Nash inequalities under expected finite-horizon average payoff. It does **not** silently downgrade to payoff-set existence, fixed-initial-state existence, stationary/finite-memory existence, discounted payoff, or an augmented public-randomization model. The durable claim source and the route memo both align with that scope. The fixed-promise repair is an internal lemma reformulation, not a theorem-side scope change.

## reviewer_07.md
- [SCOPE] The theorem-side scope is preserved. The packet still targets the exact durable claim: one behavioral strategy profile, valid for all sufficiently large horizons, for every initial state, in the strategy-existence formulation rather than a payoff-set downgrade.
- [SCOPE] The shift from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)) is a real route-level scope change, not a cosmetic proof edit. It must be recorded as a statement replacement throughout the backbone. The packet itself already flags scope changes, so this is allowed, but it must be treated explicitly.
- [SCOPE] L4* replaces L4 as the genuine open selector theorem. Any downstream text that still treats old L4 as the relevant bottleneck is stale.
- [SCOPE] L6 must remain downgraded to literal global assembly unless the public state is enriched to remember punishment anchors. Do not silently re-upgrade it later.

## reviewer_08.md
- [SCOPE] The theorem-side scope is preserved. The packet still targets the exact durable claim: one behavioral strategy profile, valid for all sufficiently large horizons, for every initial state, in the strategy-existence formulation rather than a payoff-set downgrade.
- [SCOPE] The shift from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)) is a real route-level scope change, not a cosmetic proof edit. It must be recorded as a statement replacement throughout the backbone. The packet itself already flags scope changes, so this is allowed, but it must be treated explicitly.
- [SCOPE] L4* replaces L4 as the genuine open selector theorem. Any downstream text that still treats old L4 as the relevant bottleneck is stale.
- [SCOPE] L6 must remain downgraded to literal global assembly unless the public state is enriched to remember punishment anchors. Do not silently re-upgrade it later.
