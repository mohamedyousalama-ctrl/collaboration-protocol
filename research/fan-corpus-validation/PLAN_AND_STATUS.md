# Fan Corpus Validation — Plan and Status

**Workstream:** Naturalistic 52-record corpus validation and Fan Chen-Chieh methods exchange  
**Started:** 22 August 2026  
**Working branch:** `research/fan-corpus-validation-2026-08-22`  
**Base:** `main`  
**Autonomous assistant-owned work:** **COMPLETE FOR CURRENT PRESERVATION SCOPE**

## Governing evidence rules

1. Preserve historical `CP_Incident_Database_v1.xlsx` evidence unchanged.
2. Never mark an incident C9 `CONFIRMED` unless primary interaction evidence is independently available and sufficient to check A3/A8/chronology.
3. Original task artifacts may corroborate A3/context, but do not automatically confirm the whole incident.
4. Assistant-generated Part-C classifications are recommendations only until Mohamed Salama makes the researcher decision.
5. Ground-truth intent (`C5`) can only be finalized by Mohamed Salama.
6. Do not force the final analyzable corpus to remain 52. Exclude, retain as comparison/control, or retain as unverified when evidence requires it.
7. Preserve all limitations, contradictions, exclusions, source-access gaps, recovery defects, comparison cases and negative controls.
8. Never describe the preserved set as `52 validated SII events` unless completed evidence actually supports that claim.
9. `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` means current recovery is exhausted, not that a historical source is proven never to have existed.

## WP1 — Freeze and reconstruct v1

**Status: COMPLETE — AUTHORITATIVE V1 RECOVERED AND VERIFIED**

Exact v1 identity:

- bytes: **31,471**
- SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`

The historical workbook remains frozen. Validation artifacts are additive and live only on the dedicated research branch.

Key durable evidence:

- `RECOVERY_PROVENANCE_AND_FREEZE.md`
- `SOURCE_WORKBOOK_RECOVERY.md`
- `work/EXACT_SOURCE_VERIFICATION.md`
- `work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `work/authoritative_v1_inventory.json`
- `work/incident_rows.tsv`

## WP2 — Audit all 52 records

**Status: COMPLETE — TWO PASSES / 52 OF 52 REVIEWED**

### Pass 1 — structural/evidence-readiness audit

- `PASS_TO_SOURCE_VERIFICATION` — **21**
- `NEEDS_SOURCE` — **11**
- `STRUCTURAL_DEFECT` — **2**
- `EXCLUDE_CANDIDATE` — **18**

Major findings include the missing dedicated A4 workbook column, A6 silent/disclosure ambiguity, A9 normalization need, compressed chronology, source-dependent rows, and historical machine-suggestion fields that must not be treated as researcher-final coding.

### Pass 2 — stricter construct-validity audit

Assistant recommendation:

- `LIKELY SII` — **12**
- `POSSIBLE / SOURCE-DEPENDENT` — **11**
- `NO / COMPARISON CLASS` — **25**
- `CONTROL / COUNTER-PATTERN` — **4**

These are audit recommendations, not researcher-final results and not prevalence estimates.

Durable WP2 outputs:

- `CORPUS_AUDIT_52.md`
- `corpus-audit/ROW_AUDIT_52.tsv`
- `CORPUS_AUDIT_52_PASS2_SEMANTIC_REVIEW.md`
- `CORPUS_AUDIT_52_PASS2_SEMANTIC_REVIEW.tsv`
- `tools/wp2_audit.py`

## WP3 — Locate and verify seven source conversations

**Status: AUTONOMOUS RECOVERY COMPLETE FOR CURRENT PRESERVATION SCOPE — PARTIAL SOURCE EVIDENCE; C9 CONFIRMED 0/52**

Families: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1.

### Terminal source-evidence state

- **GPT — `SOURCE_EXTRACT_ONLY`, 5/5 mapped.** Recovered `extract_chatgpt_w1_2026-07-30.md`, 12,815 bytes, SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`. It restores A4 but explicitly reports truncation/compaction. No independently complete primary GPT transcript was recovered.
- **AUD — strongest partial source chain.** Historical full-session path identified: `/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`. Recovered bounded primary execution fragment `PREFLIGHTKVD06REV14001_transcript.txt`, 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`. A preserved assistant preflight handback also exists. Together they corroborate AUD-020 behavior/outcome and AUD-021 execution order; AUD-021's same-reply self-disclosure is also corroborated. The user-side A3 work-order message, full JSONL, `human_turns.txt`, and full 22-row extraction output remain unrecovered, so C9 stays UNVERIFIED.
- **CDX — `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED`.** Exact historical filename `outputs/extract_codex_w1_2026-07-30.md` is recorded but was not recovered after targeted Git/Library/archive search.
- **W38 — `PRIMARY_TASK_ARTIFACT_FOUND`.** Original work orders corroborate A3/source content for W38-001..006; full mismatch chronology was not recovered.
- **W39 — `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL`.** Original task artifacts corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007; W39-002, W39-005 and W39-006 remain source-incomplete.
- **KBD — `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE`.** No sufficiently complete four-record KIVO-BUILDER source/extract recovered.
- **KPF — `PRIMARY_TASK_ARTIFACT_FOUND`.** Rebase/no-PR governance text corroborated, but A8/full interaction chronology was not recovered.

### Evidence totals — keep categories separate

- corpus rows tracked: **52/52**
- derivative source-extract mapped: **5/52**
- exact primary task-artifact A3/source-content corroboration: **11/52**
- AUD primary execution behavior/output corroboration: **2/52**
- AUD-021 A8 interaction-output corroboration: **1/52**
- C9 `CONFIRMED`: **0/52**
- C9 `CONTRADICTED`: **0/52**

These are different evidence classes and must never be added together as a `verified N`.

### Autonomous search boundary reached

The recovery pass covered the current Git branch/code index, available Library and conversation files, preserved/materialized archives, historical path/filename references, distinctive A3/A8 phrases, `human_turns.txt`, the exact AUD JSONL reference, and the named CDX extraction file.

No additional complete source interaction was recovered. Further WP3 improvement now requires **newly supplied/recovered primary material**, such as provider exports, old-machine files, or previously unindexed source transcripts. Do not restart generic source searching without new evidence.

Durable WP3 outputs:

- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`
- `source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`
- `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`
- `source-evidence/AUD_PRIMARY_FRAGMENT_MAPPING.md`

## WP4 — Classification recommendations

**Status: COMPLETE — 52/52 ASSISTANT RECOMMENDATIONS PREPARED**

The assistant has prepared provisional recommendations for every candidate while preserving researcher authority. C5 remains researcher-only and C9 remains evidence-dependent.

Headline construct recommendation:

- LIKELY SII — **12**
- POSSIBLE/source-dependent — **11**
- NO/comparison class — **25**
- CONTROL/counter-pattern — **4**

Durable WP4 outputs:

- `CLASSIFICATION_RECOMMENDATIONS.md`
- `CLASSIFICATION_RECOMMENDATIONS_COMPACT.tsv`
- `RESEARCHER_REVIEW_CARDS_PRIORITY.md`
- `RESEARCHER_DECISION_QUEUE.md`

## WP5 — Researcher decisions

**Owner: Mohamed Salama**  
**Status: READY — THIS IS NOW THE NEXT SUBSTANTIVE STEP**

Recommended review order:

1. 12 LIKELY SII rows;
2. 11 POSSIBLE/source-dependent rows;
3. 4 CONTROL/counter-pattern rows;
4. 25 NO/comparison-class rows.

For each row Mohamed records `ACCEPT`, `OVERRULE`, or `DEFER FOR SOURCE` and supplies C5 TRUE INTENT where meaningful. Assistant language is never converted automatically into researcher ground truth.

New source evidence is optional for beginning WP5. Rows lacking sufficient source can remain `DEFER FOR SOURCE` / C9 `UNVERIFIED`.

## WP6 — Independent quality check

**Status: DEFERRED BY FOUNDER**

After WP5, independent QC should check coding consistency, source-status fidelity, exclusions/controls, denominator definitions, and version integrity.

## WP7 — Freeze v1.1

**Status: BLOCKED UNTIL WP5 + LATER INDEPENDENT QC**

Historical v1 will remain untouched. The future v1.1 must be a new validated artifact with explicit provenance, inclusion/exclusion ledger, researcher-final coding, source-status fields, and exact checksum/version records.

## WP8 — Fan exchange package

**Status: AUTONOMOUS METHODS-STATUS PACKAGE COMPLETE — READY FOR METHODS EXCHANGE NOW**

The package is intentionally pre-researcher-adjudication and does not represent the 52 candidates as validated positives.

Current files under `fan-exchange/`:

1. `00_READ_ME_FIRST.md`
2. `01_METHODS_NOTE.md`
3. `02_SCHEMA_AND_CODEBOOK.md`
4. `03_DCM2_CROSSWALK_TEMPLATE.md`
5. `04_SANITIZED_EXAMPLES.md`
6. `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`
7. `06_CURRENT_EMPIRICAL_STATUS.md`
8. `07_EXCHANGE_SEQUENCE_AND_QUESTIONS.md`

The package now contains the extraction method, corrected schema provenance, two-pass audit results, exact evidence limitations, sanitized positive/control/exclusion examples, DCM 2.0 crosswalk questions, and a recommended methods-first exchange sequence.

A later post-WP5 revision should refresh researcher-final counts/examples before any results-oriented paper or dataset release. The current package is already suitable for the limited purpose Fan requested: **compare extraction/classification methodology and data structure before defining a formal collaboration**.

## Autonomous completion handoff

`AUTONOMOUS_COMPLETION_HANDOFF.md` records the terminal state of all work that can be completed without researcher decisions.

Future windows should fresh-read, in order:

1. `PLAN_AND_STATUS.md`
2. `AUTONOMOUS_COMPLETION_HANDOFF.md`
3. `CLASSIFICATION_RECOMMENDATIONS.md`
4. `RESEARCHER_REVIEW_CARDS_PRIORITY.md`
5. `QUOTE_VERIFICATION_REGISTER.md`
6. `fan-exchange/00_READ_ME_FIRST.md`

Do not restart generic source recovery unless new primary source material becomes available.

## Current status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | **COMPLETE** |
| 2 | Audit all 52 | **COMPLETE — TWO PASSES / 52 OF 52** |
| 3 | Source conversations | **AUTONOMOUS RECOVERY COMPLETE FOR CURRENT SCOPE — PARTIAL EVIDENCE / C9 0 OF 52** |
| 4 | Classification recommendations | **COMPLETE — 52 OF 52** |
| 5 | Researcher decisions | **READY — REQUIRES MOHAMED** |
| 6 | Independent QC | **DEFERRED** |
| 7 | Freeze v1.1 | **BLOCKED ON WP5 + QC** |
| 8 | Fan methods exchange | **METHODS-STATUS PACKAGE COMPLETE / READY NOW** |

## Next action

**No further assistant-only work remains on the current evidence set. The next substantive action is WP5 researcher adjudication.**

GitHub Issue #3 mirrors this high-level state. This file remains the durable branch-level research handoff and must be updated after future researcher decisions, new source recovery, QC, or v1.1 freeze.
