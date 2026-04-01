# MathPipeProver — Theorem Pipeline

## Overview

The theorem pipeline develops and verifies mathematical results. It operates before and in parallel with the paper pipeline.

```
SEARCHER (find proof strategies)
    ↓
BREAKDOWN (decompose into lemma sequence)
    ↓
PROVER (prove each lemma/theorem)
    ↓
REVIEWER (verify proof correctness)
    ↓
PASS → results go to PAPER PIPELINE
PATCH_SMALL → PROVER fixes
PATCH_BIG → BREAKDOWN amends
REDO → back to SEARCHER
```

## Roles

### 1. SEARCHER
- **Prompt**: `prompts/searcher.md`
- **Task**: Find at least 5 distinct strategies for proving the target result
- **Output**: Strategy name, core idea, key tools, failure modes, difficulty estimate

### 2. BREAKDOWN
- **Prompt**: `prompts/breakdown.md`
- **Task**: Decompose chosen strategy into lemma sequence with dependencies
- **Output**: Lemma statements, dependency graph, critical path, technique hints

### 3. PROVER
- **Prompt**: `prompts/prover.md`
- **Task**: Write complete formal proofs following the breakdown
- **Output**: Full proof text with all steps justified

### 4. REVIEWER
- **Prompt**: `prompts/reviewer.md`
- **Task**: Verify proof correctness
- **Verdict**: `PASS` / `PATCH_SMALL` / `PATCH_BIG` / `REDO`

### 5. VERIFIER (Soundness Smell Test)
- **Prompt**: `prompts/verifier.md`
- **Task**: High-level architectural validation of the proof approach

## Handoff to Paper Pipeline

When the theorem pipeline produces verified results (PROVER → REVIEWER → PASS):
1. The verified proof artifacts are collected
2. They are passed to the WRITER role in the paper pipeline
3. The paper pipeline takes over (Writer → Editor → Peer Reviewer)
4. If the peer reviewer finds a PROOF-level issue, it comes back here

## Execution Rules

1. **Always use Extended Pro** for every submission
2. **Fresh session** for every reviewer pass
3. **One role per session**
4. **All files** in the repo, not C:\repos
