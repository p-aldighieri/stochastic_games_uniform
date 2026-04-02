# Prover Request: Section 6 — The Conditional Theorem (Pass 49)

Provider: external_agent
Model hint: chatgpt-5.4-pro-extended
Generated: 2026-03-29

## Instructions

You are the prover role. Write the complete Section 6 of our paper: "The Conditional Theorem." The scope gatekeeper says this is 3-4 pages, ASSEMBLY standard.

## What This Section Must Contain

1. **Statement of the conditional theorem**: If for every node C in a metastable tree, the nodewise realization certificate holds (i.e., local witness packages can be implemented as actual public block controllers), then every finite stochastic game has a uniform epsilon-equilibrium.

2. **The Kakutani-Fan-Glicksberg fixed-point argument**: On the compact relaxed tree space A_eta (from Section 3), define the best-response correspondence. Show it has:
   - Nonempty convex values (from convexity of A_eta, Section 5.1 Caratheodory)
   - Closed graph (from continuity in flux coordinates, Section 4)
   - Therefore KFG gives a fixed point

3. **From fixed point to epsilon-equilibrium**: Show that a fixed point of the correspondence, when eta is small enough, gives a strategy profile where no player can gain more than epsilon by deviating. The key: the deviation value functionals are continuous (Section 4, Proposition on downstream continuity), so the best-response condition at the fixed point transfers to approximate optimality.

4. **The remaining gap (VP3)**: State clearly what the conditional theorem assumes (the nodewise realization certificate) and what remains open (VP3: joint-germ compatibility — can internal occupation germs and exit-flux witness germs be drawn from the same joint policy polytope?).

5. **Discussion**: Frame this as a conditional reduction — the open problem reduces to VP3. Mention that for special cases (quitting games, positive recursive absorbing), VP3 is known to hold.

## Notation

- A_eta — relaxed tree space (Section 3)
- beta_C — boundary flux (Section 4)
- Kakutani-Fan-Glicksberg (not Brouwer — the space is not a simplex)
- VP3 — joint-germ compatibility condition

## Output Format

LaTeX-ready mathematical prose. Numbered theorem/corollary. ~3-4 pages. This is the assembly section — it ties everything together.
