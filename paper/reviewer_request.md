You are a REVIEWER for a mathematical proof manuscript. Read the attached LaTeX file `simplicity_conjecture_v1.tex` carefully.

This is the main result paper proving: on finite product menus Y = prod M_i with convex canonical pricing p_0, simplicity (natural-order) is equivalent to additive separability of p_0.

## Your task

1. **Proof correctness**: Check every lemma and theorem for logical gaps, missing quantifiers, unstated assumptions, or errors. Pay special attention to:
   - Lemma 3' (pointwise pinning) — the key repair after Lemma 3 was shown false
   - The slice reduction argument (Lemma 4) — does the quantifier order work?
   - The order-normalization proof (Section 5) — does Step 2 correctly use global pinning?
   - The equivalence of broad/narrow simplicity under convexity (Lemma 1.3)

2. **Notation consistency**: Flag any notation that is used before being defined, or defined differently in different places.

3. **Clarity and readability**: Flag sentences that are hard to parse, arguments that skip steps, or places where a one-line remark would help the reader.

4. **Internal consistency**: The remark at lines ~144-152 says the original model's neighbor notion is covered. The discussion section should not contradict this. Check that all cross-references are consistent.

5. **Mathematical writing style**: Flag any unprofessional phrasing, redundant passages, or structural issues.

## Output format

Start with: VERDICT: PASS / PATCH_SMALL / PATCH_BIG / REDO

Then provide a numbered list of issues, each with:
- Location (section/lemma/line description)
- Severity (critical / medium / minor)
- The issue
- Suggested fix
