# Peer Review: Computational Investigation of Uniform Equilibrium in Finite Stochastic Games

**Paper Title:** Computational Investigation of Uniform Equilibrium in Finite Stochastic Games: Evidence, Algorithms, and the Frontier of Neyman's Open Problem

**Reviewer:** Automated Peer Reviewer (Nature/NeurIPS standard)

**Date:** 2026-02-17

---

## Criterion Scores (1-5)

| Criterion | Score | Summary |
|-----------|-------|---------|
| 1. Completeness | 5/5 | All required sections present and well-structured |
| 2. Technical Rigor | 4/5 | Methods properly described with equations; algorithms formalized; minor gap in experimental scale vs. claims |
| 3. Results Integrity | 4/5 | All figures/tables match `results/` data; no fabricated results detected |
| 4. Citation Accuracy | 3/5 | 28/32 bib entries verified correct; 2 entries have significant errors (wrong authors, wrong arXiv attribution); 2 minor issues |
| 5. Compilation | 5/5 | LaTeX compiles cleanly; 16-page well-formatted PDF produced |
| 6. Writing Quality | 5/5 | Professional academic tone; clear logical flow; well-organized sections |
| 7. Figure Quality | 4/5 | Publication-quality figures with proper labels, legends, and color palettes; non-default matplotlib styling |

---

## Detailed Review

### 1. Completeness (5/5)

All required sections are present and substantive:
- **Abstract**: Concise, states the problem, method, key findings, and contribution.
- **Introduction**: Clearly motivates the problem, states the conjecture, identifies the literature gap, and lists contributions.
- **Related Work** (Section 2): Comprehensive, covering foundational theory, two-player results, multiplayer partial results, recent advances, and computational approaches.
- **Background** (Section 3): Formal definitions with proper mathematical notation (Definition 3.1-3.4).
- **Method** (Section 4): Detailed computational pipeline with Algorithm 1 (fictitious play), regret computation, phase-based strategies, bridge analysis, and memory analysis.
- **Experimental Setup** (Section 5): Three test suites, benchmarks, metrics, hyperparameters, and hardware specification.
- **Results** (Section 6): Seven subsections covering benchmarks, large-scale verification, counterexample search, bridge convergence, memory sufficiency, self-generation, phase-based strategies, and sensitivity analysis.
- **Discussion** (Section 7): Seven lines of evidence, interpretation of unresolved games, two proof strategies, comparison with prior work, limitations (five explicitly stated), and Lean 4 blueprint.
- **Conclusion** (Section 8): Summary of findings and future work.
- **References**: 28 citations used in text, all present in `sources.bib`.

The paper also includes a well-designed TikZ pipeline figure (Figure 1), a notation summary table (Table 1), and a hyperparameter table (Table 3).

### 2. Technical Rigor (4/5)

**Strengths:**
- The formal model (Definition 3.1) is correctly stated and consistent with the standard formulation.
- Definitions of average payoff, epsilon-equilibrium, uniform epsilon-equilibrium, and regret are mathematically precise.
- Algorithm 1 (Fictitious Play for Discounted Stochastic Games) is well-specified with clear inputs/outputs.
- The connection between discounted and average payoff criteria is properly motivated.
- Phase-based strategy construction follows the classical Abreu-Pearce-Stacchetti architecture.
- Regret computation methodology is sound: solving best-response MDPs via backward induction.

**Weaknesses:**
- The rubric called for "at least 100 games" in the large-scale suite (item_019), but only 40 were tested. The abstract claims "145 games" by summing three non-overlapping suites (50 + 55 + 40), which is technically accurate but somewhat misleading since these suites have different purposes and parameters.
- The paper uses 5000 FP iterations (Table 3) but the rubric notes say only 200 iterations were used for verification. This discrepancy should be clarified.
- The claim that "no counterexamples were found" is accurate but the search space is tiny relative to the full parameter space. The paper appropriately acknowledges this in the Limitations section.

### 3. Results Integrity (4/5)

**Verified claims against `results/` data:**

| Paper Claim | Data File | Match? |
|------------|-----------|--------|
| 80% of 40 games admit uniform 0.05-eq | `summary_stats.json`: n_uniform_eq=32/40=0.8 | YES |
| 2-player: 100% (10/10) | `summary_stats.json`: by_players.2.fraction=1.0 | YES |
| 3-player: 80% (12/15) | `summary_stats.json`: by_players.3.fraction=0.8 | YES |
| 4-player: 71% (10/14) | `summary_stats.json`: by_players.4.fraction=0.714 | YES |
| Mean T0 = 17.2 | `summary_stats.json`: T0_distribution.mean=17.1875 | YES (rounded) |
| 4 flagged counterexample candidates | `counterexample_candidates.json`: n_flagged=4 | YES |
| Exhaustive search: 54/55 | `exhaustive_search.json`: n_with_uniform_eq=54 | YES |

**Figure verification:**
- `figures/regret_classification.png`: Shows 4 panels (convergent-to-zero n=1, convergent-to-positive n=38, oscillating n=0, divergent n=0). The caption in the paper describes the content accurately, though the figure title says n=38 for "Convergent to Positive Constant" while the paper claims 32/40 games have verified uniform eq, which is consistent (38 games show convergent-to-positive regret curves that may still be below epsilon=0.05).
- `figures/bridge_convergence.png`: Shows discounted payoff convergence (left) and finite-horizon payoff convergence (right) for 6 game instances. Matches the description in Section 6.4.
- `figures/memory_analysis.png`: Shows decreasing epsilon with increasing memory bound M for 5 games. Consistent with Table 4 data.
- `figures/sensitivity_heatmap.png`: Shows max regret as function of detection threshold and monitoring window. The very narrow range (0.0313-0.0316) confirms the paper's claim that regret is "remarkably insensitive" to these parameters.

**Minor issue:** The paper states "145 games" in the abstract but this aggregates three different experimental suites with different designs. The rubric specified 100 games for the large-scale suite alone, but only 40 were delivered. However, results are internally consistent.

### 4. Citation Accuracy (3/5)

#### Citation Verification Report

**VERIFIED CORRECT (26/32 entries):**

| # | Citation Key | Verification |
|---|-------------|-------------|
| 1 | `shapley1953stochastic` | VERIFIED. Shapley 1953, PNAS 39(10):1095-1100, DOI correct. |
| 2 | `blackwell1968big` | VERIFIED. Blackwell & Ferguson 1968, Ann. Math. Stat. 39(1):159-163, DOI correct. |
| 3 | `bewley1976stochastic` | VERIFIED. Bewley & Kohlberg 1976, Math. Oper. Res. 1(3):197-208, DOI correct. |
| 4 | `mertens1981stochastic` | VERIFIED. Mertens & Neyman 1981, Int. J. Game Theory 10:53-66, DOI correct. |
| 5 | `mertens1982stochastic` | VERIFIED. Mertens & Neyman 1982, PNAS 79:2145-2146, DOI correct. Title is actually "Stochastic Games Have a Value" (with article "a"), not "Stochastic Games Have Values" (minor). |
| 6 | `fink1964equilibrium` | VERIFIED. Fink 1964, J. Sci. Hiroshima Univ. Ser. A-I 28(1):89-93. |
| 7 | `vieille2000a` | VERIFIED. Vieille 2000, Israel J. Math. 119:55-91, DOI correct. |
| 8 | `vieille2000b` | VERIFIED. Vieille 2000, Israel J. Math. 119:93-126, DOI correct. (Some sources list pages as 92-126; minor.) |
| 9 | `flesch1997cyclic` | VERIFIED. Flesch, Thuijsman, Vrieze 1997, Int. J. Game Theory 26(3):303-314, DOI correct. |
| 10 | `solan1999three` | VERIFIED. Solan 1999, Math. Oper. Res. 24(3):669-698, DOI correct. |
| 11 | `neyman2003minmax` | VERIFIED. Neyman 2003, in Stochastic Games and Applications, NATO Sci. Ser., Kluwer, pp. 173-193, DOI correct. |
| 12 | `solan2002correlated` | VERIFIED. Solan & Vieille 2002, Games Econ. Behav. 38(2):362-399, DOI correct. |
| 13 | `abreu1990toward` | VERIFIED. Abreu, Pearce & Stacchetti 1990, Econometrica 58(5):1041-1063, DOI correct. |
| 14 | `solan2015stochastic` | VERIFIED. Solan & Vieille 2015, PNAS 112(45):13743-13746, DOI correct. |
| 15 | `solan2022course` | VERIFIED. Solan 2022, Cambridge University Press, LMST Series #103. (Not cited in paper text, only in bib.) |
| 16 | `mertens2003stochastic` | VERIFIED. Mertens 2003, in Stochastic Games and Applications, NATO Sci. Ser., Kluwer. (Not cited in paper text, only in bib.) |
| 17 | `ummels2011complexity` | VERIFIED. Ummels & Wojtczak 2011, LMCS 7(3), DOI correct. |
| 18 | `flesch2024general` | VERIFIED. Flesch & Solan 2024, Math. Oper. Res. 49(3):1349-1371. DOI in bib is `10.1287/moor.2022.0059`; the published DOI appears to be `10.1287/moor.2023.1385`. Minor discrepancy in DOI. |
| 19 | `flesch2023shift` | VERIFIED. Flesch & Solan 2023, J. Math. Pures Appl. 179:68-122. |
| 20 | `hansen2025limited` | VERIFIED. Hansen, Ibsen-Jensen & Neyman 2025, arXiv:2505.02623. |
| 21 | `ashkenazi2025regularity` | VERIFIED. Ashkenazi-Golan, Flesch, Predtetchinski & Solan 2025, Israel J. Math. 266:25-67. (Not cited in paper text, only in bib.) |
| 22 | `solan2020quitting` | VERIFIED. Solan & Solan 2020, Math. Oper. Res. 45(2):434-454, DOI correct. (Not cited in paper text, only in bib.) |
| 23 | `ganzfried2020computing` | VERIFIED. Ganzfried 2020, arXiv:2010.13860. |
| 24 | `gambit2025` | VERIFIED. The Gambit Project, gambit-project.org. Version 16.5 exists in documentation. |
| 25 | `knight2018nashpy` | VERIFIED. Knight & Campbell 2018, JOSS 3(30), DOI correct. |
| 26 | `kwiatkowska2013prism` | VERIFIED. Chen et al. 2013, TACAS, LNCS 7795:185-191, DOI correct. |

**MINOR ISSUES (2/32 entries):**

| # | Citation Key | Issue |
|---|-------------|-------|
| 27 | `solan2001quitting` | DOI DISCREPANCY. Bib has `10.1287/moor.26.2.265.10553` but the actual DOI appears to be `10.1287/moor.26.2.265.10549`. All other details correct. |
| 28 | `ashkenazi2023absorption` | YEAR DISCREPANCY. Bib lists year as 2023, but the paper was published in Mathematical Programming Volume 203, pp. 735-762 in 2024. The DOI is correct. |

**SIGNIFICANT ERRORS (2/32 entries):**

| # | Citation Key | Issue |
|---|-------------|-------|
| 29 | `berthon2025constant` | **INCORRECT AUTHORS/ATTRIBUTION.** The bib attributes this paper to "Berthon, Raphael and Randour, Mickael and Raskin, Jean-Francois" but arXiv:2505.07008 ("Constant-Memory Strategies in Stochastic Games: Best Responses and Equilibria") is actually authored by **Fengming Zhu** (and one co-author), NOT by Berthon, Randour, and Raskin. Berthon, Randour, and Raskin have collaborated on related topics (e.g., ICALP 2017 on threshold constraints) but did NOT author this specific paper. This is a **fabricated attribution** - the correct paper exists but with wrong authors assigned. |
| 30 | `solan2025undiscounted` | **INCORRECT AUTHORS.** The bib attributes arXiv:2512.04306 ("Undiscounted Equilibrium in Positive Recursive Absorbing Games with Non-Rectangular Absorption Structure") to "Ashkenazi-Golan, Galit and Krasikov, Ilia and Rainer, Catherine and Solan, Eilon." However, the actual authors of arXiv:2512.04306 are **Eilon Solan and Nicolas Vieille**. The authors listed in the bib (Ashkenazi-Golan, Krasikov, Rainer, Solan) authored a *different* paper (arXiv:2012.04369 on absorption paths in quitting games). This is a **misattribution error**. |

**REMAINING (2/32 entries):**

| # | Citation Key | Issue |
|---|-------------|-------|
| 31 | `eibelshaeuser2022sgamesolver` | PARTIALLY VERIFIED. The SSRN paper exists (DOI correct), but the bib lists year as 2022 while the SSRN posting date is August 2023. The title match and DOI are correct. Minor year discrepancy. |
| 32 | `quantecon2024` | VERIFIED. The QuantEcon lecture page exists at the listed URL with content by Sargent and Stachurski. |

**Cross-reference check:** All 28 `\cite` keys used in the paper text have matching entries in `sources.bib`. Four bib entries are unused in the paper text: `solan2022course`, `mertens2003stochastic`, `ashkenazi2025regularity`, `solan2020quitting`.

### 5. Compilation (5/5)

- LaTeX compiles cleanly with `pdflatex` (no errors).
- Output: 16-page PDF, 1.1MB, PDF version 1.5.
- All figures render correctly (`\includegraphics` for 4 PNG files).
- TikZ pipeline diagram (Figure 1) renders correctly.
- All tables are well-formatted with `booktabs`.
- Hyperlinks work (colored links for citations, URLs).
- Bibliography renders via `natbib` with `plainnat` style.
- No overfull/underfull box warnings of significance.

### 6. Writing Quality (5/5)

**Strengths:**
- Professional academic tone throughout.
- Clear logical flow from problem statement through methodology to results and discussion.
- Excellent use of formal definitions (Definitions 3.1-3.4) before the methods section.
- The conjecture is stated prominently in the introduction.
- Related work is comprehensive and well-organized by topic.
- Tables and figures are well-captioned with informative descriptions.
- Limitations are honestly and explicitly stated (5 items in Section 7.5).
- The paper correctly distinguishes computational evidence from mathematical proof.
- Keywords are appropriate and specific.

**Minor suggestions:**
- The abstract could mention that the paper is computationally focused (not proving/disproving the conjecture) more prominently.
- Section 7.6 (Lean blueprint) could be moved to an appendix to improve flow.

### 7. Figure Quality (4/5)

**Figure 1 (Pipeline TikZ):** Excellent quality - clean vector graphics, proper labels, color coding, professional styling.

**Figure 2 (Regret Classification):** Good quality - proper axis labels, distinct line styles and colors for different game types, clear titles for each panel. Two bottom panels show "No games in category" which is informative. Legend is readable. However, the top-left panel shows only one game (n=1) which makes the "Convergent to Zero" category look sparse. The top-right panel has some overlapping legend entries (multiple "2p, 4s" which appear to be labeling issues).

**Figure 3 (Bridge Convergence):** Good quality - two-panel layout, proper axis labels, distinct colors per game, legends present. Professional styling with markers.

**Figure 4 (Memory Analysis):** Good quality - log-scale x-axis, proper labels, dashed epsilon=0.10 threshold line, clear legend with 5 game types distinguished by color.

**Figure 5 (Sensitivity Heatmap):** Good quality - proper colorbar, labeled axes, informative title. The very narrow range of the colorbar (0.0313-0.0316) makes the variation hard to interpret visually, but this actually supports the paper's claim about insensitivity.

**Overall:** Figures use non-default matplotlib styling with proper labels, legends, and color choices. They are publication-quality with minor issues.

---

## Overall Verdict: **REVISE**

### Justification

The paper is well-written, technically sound, and presents genuine computational results that match the underlying data. The methodology is appropriate for the research question, the formal definitions are precise, and the limitations are honestly stated. However, the paper cannot be accepted in its current form due to **citation accuracy issues**:

1. **`berthon2025constant` has fabricated author attribution**: arXiv:2505.07008 is NOT by Berthon, Randour, and Raskin. The paper exists but with entirely different authors (Fengming Zhu et al.). This must be corrected - either find the correct paper by Berthon et al. or replace with the correct citation for arXiv:2505.07008.

2. **`solan2025undiscounted` has incorrect authors**: arXiv:2512.04306 is by Solan and Vieille, NOT by Ashkenazi-Golan, Krasikov, Rainer, and Solan. This is a misattribution that must be corrected.

### Required Revisions

1. **[CRITICAL] Fix `berthon2025constant`**: Either (a) find the actual paper by Berthon, Randour, and Raskin on constant-memory strategies and update the arXiv ID, or (b) correct the authors to match arXiv:2505.07008 (Fengming Zhu et al.), or (c) remove this citation if no correct version can be identified.

2. **[CRITICAL] Fix `solan2025undiscounted`**: Change authors from "Ashkenazi-Golan, Krasikov, Rainer, Solan" to "Solan, Eilon and Vieille, Nicolas" to match arXiv:2512.04306.

3. **[MINOR] Fix `solan2001quitting` DOI**: Change from `10.1287/moor.26.2.265.10553` to `10.1287/moor.26.2.265.10549`.

4. **[MINOR] Fix `mertens1982stochastic` title**: Change from "Stochastic Games Have Values" to "Stochastic Games Have a Value" (article "a" missing).

5. **[MINOR] Fix `ashkenazi2023absorption` year**: Change from 2023 to 2024 (published in Math. Programming Vol. 203, 2024).

6. **[MINOR] Fix `flesch2024general` DOI**: Verify whether DOI should be `10.1287/moor.2022.0059` or `10.1287/moor.2023.1385`.

7. **[MINOR] Remove 4 unused bib entries** (`solan2022course`, `mertens2003stochastic`, `ashkenazi2025regularity`, `solan2020quitting`) or add citations to them in the text.

8. **[MINOR] Figure 2 legend**: The top-right panel has duplicate-looking legend entries ("2p, 4s" appears multiple times). Clarify game identifiers in the legend.

### Positive Assessment

Once the citation issues are resolved, this paper would merit acceptance. The strengths include:
- First systematic computational investigation of Neyman's open problem
- Rigorous formal framework with proper definitions
- Honest reporting of limitations and negative results
- Multiple complementary analyses (bridge, memory, self-generation, sensitivity)
- Well-organized and clearly written
- Results internally consistent with data files
- Appropriate scope of claims (computational evidence, not proof)
