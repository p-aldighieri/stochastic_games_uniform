# MathPipeProver — Paper Pipeline

## Overview

Once the theorem pipeline produces verified results (prover PASS + reviewer PASS), the **paper pipeline** takes over to produce a publishable manuscript. It operates as a separate loop with three roles:

```
THEOREM PIPELINE (Searcher → Breakdown → Prover → Reviewer)
        ↓ (results verified)
PAPER PIPELINE:
        ↓
    WRITER (produces/rewrites LaTeX manuscript)
        ↓
    EDITOR (structural/clarity/notation review)
        ↓ loops until APPROVE
    PEER REVIEWER (rigorous mathematical review)
        ↓
    PASS → done (publish)
    CONDITIONAL (minor) → WRITER (notation/typo fixes)
    FAIL (proof gap) → back to THEOREM PIPELINE
```

## Roles

### 1. WRITER
- **Prompt**: `prompts/paper_writer.md`
- **Input**: Verified proof results + fix instructions (if returning from reviewer)
- **Output**: Complete LaTeX manuscript (.tex file)
- **Responsibilities**:
  - Produce publication-quality LaTeX
  - Incorporate all verified proof components
  - Apply fix instructions from editor or reviewer
  - Maintain consistent notation throughout
  - Include abstract, introduction, main results, proofs, bibliography

### 2. EDITOR
- **Prompt**: `prompts/paper_editor.md`
- **Input**: LaTeX manuscript from writer
- **Output**: APPROVE or REVISE with specific instructions
- **Responsibilities**:
  - Structural review (logical flow, section organization)
  - Notation consistency and clarity
  - Mathematical writing quality
  - Completeness check (no missing definitions, dangling references)
  - Does NOT verify proof correctness (that's the reviewer's job)
- **Verdict**: `APPROVE` or `REVISE` (with numbered list of changes)
- **Loop**: Writer ↔ Editor until APPROVE

### 3. PEER REVIEWER
- **Prompt**: `prompts/paper_reviewer.md`
- **Input**: Editor-approved LaTeX manuscript
- **Output**: PASS / CONDITIONAL / FAIL with detailed report
- **Responsibilities**:
  - Rigorous mathematical verification of every proof step
  - Check for logical gaps, circular reasoning, undefined quantities
  - Verify the proof chain closes end-to-end
  - Check that stated theorem follows from the proofs given
  - Assess publishability and correctness
- **Verdict**:
  - `PASS` — No issues. Manuscript is correct and publishable.
  - `CONDITIONAL` — Minor fixable issues only (notation, typos, small clarifications). → Goes to WRITER for quick fixes, then back to a fresh PEER REVIEWER.
  - `FAIL` — Proof gap that could invalidate the result. → Issue goes back to the THEOREM PIPELINE (Prover/Breakdown) to fix the underlying mathematics, then the corrected results return to the WRITER.

## Routing Rules

| Reviewer Verdict | Issue Type | Next Step |
|-----------------|------------|-----------|
| PASS | — | Done. Commit, push, submit. |
| CONDITIONAL | Notation/typos/clarity | WRITER fixes → fresh PEER REVIEWER |
| FAIL | Writing-level gap (missing explanation, unclear step) | WRITER rewrites section → EDITOR → PEER REVIEWER |
| FAIL | Proof-level gap (mathematical error, missing lemma) | THEOREM PIPELINE (Prover with fix instructions) → WRITER → EDITOR → PEER REVIEWER |

## Execution Rules

1. **Always use Extended Pro** for every submission (model selector → Pro)
2. **Fresh session** for every reviewer pass (no context contamination)
3. **One role per session** — never mix writer/editor/reviewer in same chat
4. **File naming**: `neyman_route_d_prime.tex` (single file, git handles versioning)
5. **Fix instructions**: Written as `.md` files explaining exactly what to change and why
6. **All files** go to `paper/` directory in the repo, not C:\repos
