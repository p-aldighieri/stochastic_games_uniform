You are the Consolidator. Produce a clean, self-contained write-up of the non-convex extension results for a paper appendix or companion note.

## What was established (all verified)

### Result 1: 2D theorem without convexity (PROVED)
For ANY finite 2D grid Y = M₁ × M₂ with P nondecreasing, P(0,0)=0 (NO convexity required):
Simple_nat(Y, P) ⟹ P additively separable.

Proof: Southwest-most nonzero minor argument. Pick the lexicographically first nonzero adjacent 2×2 minor Δ_{ij}. All minors below row j vanish → row j inherits slope profile from bottom boundary row (which is convex by simplicity + monotonicity). Vertical slopes inherit from left boundary column. Then Δ<0 creates a trap at (i,j), Δ>0 creates a trap at (i+1,j). Both contradict simplicity.

### Result 2: Easy direction FAILS without convexity (COUNTEREXAMPLE)
Y = {0,1,2} × {0,1}, P(i,j) = q_i with q = (0,2,3). Additive, nondecreasing, non-convex (slopes 2 then 1). For θ = (1.2, 0): u(2,0) = -0.6 not optimal, but neighbors (1,0) and (2,1) not better. So additive + nondecreasing + non-convex ≠ simple.

### Result 3: 3×3×3 counterexample under BROAD neighbors (COUNTEREXAMPLE)
P(i,j,k) = i+j+k + 1_{(1,1,1)}. Under broad neighbors (any one-coordinate jump): simple, nondecreasing, non-additive, non-convex. Under immediate adjacency: NOT simple (point (0,1,1) gets trapped).

### Result 4: NO 3×3×3 counterexample under immediate adjacency (PROVED)
On {0,1,2}³ with immediate adjacency: simple + nondecreasing → additive, even without convexity. Proof: all 2D faces are simple (boundary argument) → additive by 2D theorem → all non-center values additive → center defect t must be 0 (both signs create traps).

### Result 5: Equivalence of neighbor notions under convexity (PROVED)
When p₀ is convex: simple(broad) ⟺ simple(narrow). Proof: φ(t) = θ_i t - p₀(y|_{i→t}) is discretely concave. Distant improving move → not global max → not local max (Lemma 1) → adjacent improving move exists.

### Result 6: Partial k-dim result
Simple → additive holds without convexity when at most two coordinates have >2 levels (grids like m×n×2×...×2). Open for larger grids under immediate adjacency. The 4×4×4 case is the next frontier.

## What to produce

Write a clean narrative for Section "Beyond Convexity" of the paper, organized as:

4.1: Two neighbor notions and their equivalence under convexity (Result 5)
4.2: The two-dimensional theorem without convexity (Result 1) — full proof
4.3: Failure of the easy direction (Result 2) — counterexample
4.4: Higher dimensions without convexity
  - 3×3×3 under immediate adjacency: proved (Result 4)
  - 3×3×3 under broad neighbors: counterexample (Result 3)
  - Partial k-dim result (Result 6)
4.5: Discussion — what convexity buys, sharp boundaries

For each result, provide:
- Precise theorem/proposition statement
- Full proof or verified counterexample
- Brief discussion of significance

Keep notation consistent with our paper: p₀ for canonical price, u_θ for utility, M_i for coordinate menus, Simple_nat for natural-order simplicity.
