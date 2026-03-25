# Reviewer Output

Generated: 2026-03-24T00:16:24.550924+00:00

## VERDICT: PATCH_BIG

The branch is not a redo. There is real progress, and it stays inside the correct theorem-side target: one public-history behavioral profile, valid for all sufficiently large horizons and every initial state, with the theorem still treated as bootstrap/open rather than solved. That matches the durable problem statement, proof-state anchor, and route memo.    

## Step review

**Setup:** not valid for the intended downstream use. The amended Setup in prover_07 writes
[
w_i^s+b_{h,i}\le \mathbb E!\left[u_i+w_i^s+\beta_h(H')*i\right]+\eta(h),
]
and then cancels (w_i^s), leaving
[
b*{h,i}\le \mathbb E!\left[u_i+\beta_h(H')_i\right]+\eta(h),
]
with the analogous deviation inequality. After that cancellation, the fixed promise (w^s) disappears from the local relation. So this Setup cannot support a telescope centered at (w_i^s). Under this Setup, the strongest available downstream statement is the earlier weak telescope involving visited promises or bias differences, not the claimed corrected (L7'). This is the main defect. 

**L1:** valid. The continuation game after a public history is canonically the same finite stochastic game started from the terminal state, and the finite-horizon best-response value is well defined because only finitely many continuation histories up to horizon (T) matter. No scope problem here. 

**L3*:** essentially valid as a compactness and heredity lemma, conditional on imported L2 and whichever amended Setup is actually adopted. The ambient bias-fiber product is compact, the defining inequalities are continuous, and heredity is immediate from the definition of (F^*). But this only proves compactness for the local problem currently stated; it does not fix the missing (w^s)-term needed by the corrected telescope. 

**L4*:** still open, and still the theorem-sized selector step. The packet is right to keep this as the bottleneck, and the durable route memo says the same.  

**L5*:** valid conditional on L2 and L4*. The root choice correctly uses L2, the construction is over the full rooted tree rather than only on-path histories, unique predecessors prevent clashes, and the global gluing
[
\sigma(h)=\sigma^{s_1}(h)
]
is the right way to obtain one whole-game behavioral profile. This matches the durable route memo’s positive takeaway.  

**Literal L6 / G3:** acceptable only as explicit global assembly. It must not be cited as a non-vacuous punishment-mode mechanism; that stronger reading still lacks remembered anchor history. The packet correctly warns about this, and the durable memo agrees.  

**G4 / corrected (L7'):** unsupported as currently cited. Prover_07’s status summary points to a “corrected (L7')” downstream, but the only corrected (L7') proof earlier in the packet uses a different fixed-promise local relation, namely one of the form
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h\right]\ge w_i^s-\eta_t
]
and the deviation counterpart
[
\mathbb E!\left[u_i+\beta_{t+1}-\beta_t\mid h,\text{dev}\right]\le w_i^s+\eta_t,
]
not the canceled-(w^s) relation now written in the Setup amendment. So the current packet contains a dependency mismatch: the Setup of prover_07 does not justify the corrected telescope it cites. 

**G5 / corrected (L8'):** downstream bookkeeping is fine only after G4 is repaired. At present it hangs from an unsupported telescope. 

## Citation and dependency errors

1. The packet cannot cite the old variable-promise (L7') as proved. Prover_05 and prover_06 correctly diagnosed that the variable-promise data only give a weak telescope involving the visited promise process, not the root promise. 

2. Prover_07 then cites a corrected fixed-promise (L7'), but its own amended Setup is not the one that proof needs. That is the main citation error in the current branch state. 

3. L2 remains imported, not locally proved, so all compactness and fiber arguments must keep L2 explicit in the dependency list. The current packet mostly does this correctly. 

4. There are still small notation defects in several displayed formulas, but those are secondary. The decisive issue is the algebraic mismatch above, not typography. 

## [SCOPE] compliance

[SCOPE] The theorem-side scope is preserved. The packet still targets the exact durable claim: one behavioral strategy profile, valid for all sufficiently large horizons, for every initial state, in the strategy-existence formulation rather than a payoff-set downgrade.  

[SCOPE] The shift from variable-promise ((L3,L4,L5)) to fixed-promise ((L3^*,L4^*,L5^*)) is a real route-level scope change, not a cosmetic proof edit. It must be recorded as a statement replacement throughout the backbone. The packet itself already flags scope changes, so this is allowed, but it must be treated explicitly. 

[SCOPE] L4* replaces L4 as the genuine open selector theorem. Any downstream text that still treats old L4 as the relevant bottleneck is stale. 

[SCOPE] L6 must remain downgraded to literal global assembly unless the public state is enriched to remember punishment anchors. Do not silently re-upgrade it later.  

## Required patch set

1. Replace prover_07’s amended Setup by the actual fixed-promise local inequalities needed for the root-promise telescope. Concretely, the local relation must be
   [
   \mathbb E_{x_h,P}!\left[u_i(s(h),a)+\beta_h(H')*i\right]-b*{h,i}\ge w_i^s-\eta(h),
   ]
   and
   [
   \mathbb E_{x_{h,-i},P}!\left[u_i(s(h),(a_i',a_{-i}))+\beta_h(H'^{a_i'})*i\right]-b*{h,i}\le w_i^s+\eta(h).
   ]
   These are **not** equivalent to the current canceled-(w^s) formulas. 

2. Re-state L3*, L4*, L5*, G4, and G5 against that exact local relation. The current L3* compactness proof and L5* recursion proof should survive with only notational edits. 

3. Keep L6 cited only as literal assembly. 

4. Keep the theorem labeled bootstrap/open until L4* is actually proved. The durable proof-state anchor and route memo both require that discipline.  

## Bottom line

There is genuine progress here: L1 is in good shape, the full-tree recursion and gluing point is now explicit, and the branch has correctly isolated the fixed-promise selector as the research bottleneck. But the packet has **not** yet cleanly repaired the post-L4 tail, because the newest Setup amendment does not match the corrected telescope it wants to invoke. That is a restructuring issue, not a one-line fix. So the right reviewer outcome is **PATCH_BIG**.
