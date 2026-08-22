# WP2 Pass 2 — Semantic Construct-Validity Review of All 52 Records

**Date:** 22 August 2026  
**Source:** byte-verified authoritative v1 workbook  
**Purpose:** independently challenge whether each extracted row is actually evidence of Silent Intent Inference (SII), rather than merely accepting the historical `C0 SUGGESTED` label.

## Why a second pass was necessary

The existing WP2 audit is a useful structural/internal-consistency pass. This second pass applies a stricter construct-validity question:

> Does the row show a materially ambiguous user intent/authority/scope/definition that the assistant silently resolved, or is it better explained by competence error, false premise, explicit-rule violation, meta behavior, or a negative/control pattern?

This distinction matters scientifically. A technically harmful failure is not automatically an intent-inference event.

## Boundaries

- These are **assistant recommendations only**, not researcher-final classifications.
- No row is `C9=CONFIRMED`; primary-source verification remains WP3.
- `C5 Ground-truth intent` remains exclusively Mohamed Salama's decision.
- No historical v1 cell is edited.
- Records recommended for exclusion are retained as comparison/control evidence; they are not deleted.

## Pass-2 result

### SII-positive evidence status

- **LIKELY:** 12
- **POSSIBLE / source-dependent:** 11
- **NO — better explained by another failure class:** 25
- **CONTROL / counter-pattern:** 4

Likely rows:

`GPT-001, GPT-003, GPT-005, AUD-009, AUD-011, AUD-021, W38-003, W38-006, W39-003, W39-004, W39-007, KBD-004`

Possible/source-dependent rows:

`GPT-004, AUD-020, CDX-002, CDX-003, CDX-004, W38-002, W38-004, W38-005, W39-002, W39-005, W39-006`

Negative/control rows:

`AUD-015, AUD-017, AUD-022, W38-007`

### WP2 disposition under the stricter semantic pass

- `PASS_TO_SOURCE_VERIFICATION`: **11**
- `NEEDS_SOURCE`: **10**
- `STRUCTURAL_DEFECT`: **3**
- `EXCLUDE_CANDIDATE`: **28**

`AUD-011` is likely SII but is held as `STRUCTURAL_DEFECT` because its stored C0 suggestion (`DEFINITION→INTENT`) violates the codebook. `W39-002` is held because its A3 explicitly says the original user wording is not observable. `AUD-022` is a counter-pattern with an out-of-codebook resolution-style value.

## Recommended comparison-class distribution

Pass 2 recommends, before source verification:

- `INTENT`: 22
- `COMPETENCE`: 15
- `PREMISE`: 7
- `META`: 4
- `MIXED`: 1
- no positive incident classification recommended yet: 3 control rows

These are not final counts for the paper. They are a review queue for WP3/WP4.

## Important reclassifications versus simple triage acceptance

Several rows historically suggested as `INTENT` are more defensibly treated as non-SII unless primary evidence proves otherwise. Examples:

- `GPT-002`: the user explicitly referenced **both** windows; omitting one is an attention/completeness failure, not ambiguity.
- `AUD-008`: confusing a record structure with an operational alert capability is a conceptual/technical overclaim.
- `AUD-010`: a false two-choice solution framing is primarily a modeling/competence failure.
- `AUD-014`: the exact-head rule was explicit; not re-checking the head is procedural compliance failure.
- `W38-001`, `W39-001`, `KPF-001`: “rebase immediately before every push” was explicit. A stale-base handoff is a serious competence/compliance failure, but seriousness alone does not make it SII.
- `KBD-002`: assuming the user could see a device code is an interface-visibility premise rather than a choice among meanings of the user's intent.

Conversely, several rows remain strong intent candidates because the branch of meaning itself is visible:

- `AUD-009`: what “additive” means.
- `W38-003`: whether one ordinary burst test exhausts the entire C-04 scope.
- `W38-006`: what “marked as reproducing the defect / greppable” means operationally.
- `W39-003`: conflict between “correct only those” and “verify every argument”.
- `W39-007`: whether supplying executable SQL constitutes authority to execute against production.
- `KBD-004`: whether the requested outcome implicitly mandates a specific implementation means (`gh` CLI authentication).

## Structural findings carried forward

1. A4 (`POSSIBLE INTERPRETATIONS`) is absent from the workbook schema.
2. A3 is explicitly allowed to be trimmed and the README says A-fields were condensed.
3. All researcher-final fields C0 FINAL through C10 remain blank across all 52 rows.
4. `AUD-011` uses a non-codebook C0 suggestion.
5. `AUD-022` uses a non-codebook resolution style.
6. `W39-002` lacks transcript-observable triggering user wording in A3.
7. `DISCLOSED-PROCEED` counter-patterns must not be counted as silent merely because `A6=NO`.

## Scientific consequence

After two WP2 passes, the strongest defensible statement is still:

> **The archive contains 52 extracted candidate records across seven source-window families. It does not yet contain 52 validated SII events.**

The stricter pass indicates that a substantial portion of the candidate set may belong to comparison classes rather than the final SII-positive analysis set. That is a strength of the validation process, not a reason to force the original count.

## Machine-readable evidence

The complete row-by-row recommendations, flags, rationales and provisional C0/C1 suggestions are in:

`CORPUS_AUDIT_52_PASS2_SEMANTIC_REVIEW.tsv`

## Next gate

WP3 now becomes decisive: locate the primary source conversations/extraction outputs, reconstruct A4 where genuinely recoverable, verify A3/A8 chronology and exact quotes, and only then issue C9 recommendations and researcher review cards.
