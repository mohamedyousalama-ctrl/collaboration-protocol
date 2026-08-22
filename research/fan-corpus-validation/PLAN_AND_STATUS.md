# Fan Corpus Validation — Plan and Status

**Workstream:** Naturalistic 52-record corpus validation and Fan Chen-Chieh methods exchange  
**Started:** 22 August 2026  
**Working branch:** `research/fan-corpus-validation-2026-08-22`  
**Base:** `main`

## Governing evidence rules

1. Preserve historical `CP_Incident_Database_v1.xlsx` evidence unchanged.
2. Never mark an incident C9 `CONFIRMED` unless primary interaction evidence is independently available and sufficient to check A3/A8/chronology.
3. Original task artifacts may corroborate A3/context, but do not automatically confirm the whole incident.
4. Assistant-generated Part-C classifications are recommendations only until Mohamed Salama makes the researcher decision.
5. Ground-truth intent (`C5`) can only be finalized by Mohamed Salama.
6. Do not force the final analyzable corpus to remain 52. Exclude or retain as unverified any record that fails evidence checks.
7. Preserve all limitations, contradictions, exclusions, source-access gaps, recovery defects, comparison cases and negative controls.
8. Never describe the preserved set as “52 validated SII events” unless the completed evidence actually supports that claim.

## WP1 — Freeze and reconstruct v1

**Status:** COMPLETE — AUTHORITATIVE V1 RECOVERED AND VERIFIED

Exact v1 identity: 31,471 bytes; SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.

The incomplete historical Git Base64 representation remains untouched. The exact workbook was recovered from `files(3).zip`, whose SHA-256 `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8` exactly matches the repository source-bundle manifest. An additive exact branch representation was reconstructed and independently verified.

Durable evidence includes:
- `RECOVERY_PROVENANCE_AND_FREEZE.md`
- `SOURCE_WORKBOOK_RECOVERY.md`
- `source-v1-exact/README.md`
- `source-v1-exact/CP_Incident_Database_v1.xlsx.b64.part-00` through `part-04`
- `work/EXACT_SOURCE_VERIFICATION.md`
- `work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `work/authoritative_v1_inventory.json`
- `work/incident_rows.tsv`

## WP2 — Audit all 52 records

**Status:** COMPLETE — TWO PASSES / 52 OF 52 REVIEWED

### Pass 1 — structural and internal-consistency audit

Disposition counts:
- `PASS_TO_SOURCE_VERIFICATION` — **21**
- `NEEDS_SOURCE` — **11**
- `STRUCTURAL_DEFECT` — **2**
- `EXCLUDE_CANDIDATE` — **18**

Major structural findings:
1. A4 Possible interpretations is absent as a dedicated workbook column.
2. The v1 A6-only silent-inference aggregate can miscount disclosed events as silent.
3. AUD-021 has a resolution-style contradiction.
4. W39-002 lacks the required observable triggering quote in v1.
5. AUD-022 uses a resolution-style label outside the listed Codebook values.
6. A9 awareness-gap values require normalization before statistics.
7. Seven records have substantial A3/A8 overlap and require source chronology review.
8. Suggested outcome lacks a separate researcher-final field.
9. AUD-011 uses non-codebook `DEFINITION→INTENT` in the historical C0 suggestion field.

### Pass 2 — stricter semantic construct-validity audit

This pass challenged whether each row actually evidences Silent Intent Inference rather than competence error, premise error, explicit-rule violation, meta behavior, or a counter-pattern.

SII evidence recommendation:
- `LIKELY` — **12**
- `POSSIBLE` / source-dependent — **11**
- `NO` — **25**
- `CONTROL` / counter-pattern — **4**

Stricter disposition counts:
- `PASS_TO_SOURCE_VERIFICATION` — **11**
- `NEEDS_SOURCE` — **10**
- `STRUCTURAL_DEFECT` — **3**
- `EXCLUDE_CANDIDATE` — **28**

`EXCLUDE_CANDIDATE` means exclude from the positive-SII analysis set on present evidence, not delete from the preserved corpus.

Durable WP2 outputs:
- `CORPUS_AUDIT_52.md`
- `corpus-audit/ROW_AUDIT_52.tsv`
- `CORPUS_AUDIT_52_PASS2_SEMANTIC_REVIEW.md`
- `CORPUS_AUDIT_52_PASS2_SEMANTIC_REVIEW.tsv`
- `tools/wp2_audit.py`

## WP3 — Locate and verify seven source conversations

**Status:** ACTIVE — REAL SOURCE RECOVERY ADVANCED; INCIDENT-LEVEL C9 CONFIRMATION STILL 0 OF 52

Families: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1.

### Current source classes

- **GPT — `SOURCE_EXTRACT_ONLY` / 5 of 5 mapped.** Recovered `extract_chatgpt_w1_2026-07-30.md` (12,815 bytes; SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`). It restores A4 and maps GPT-001..005, but its own limitations disclose transcript truncation/compaction. C9 remains 0/5 confirmed.
- **AUD — `PARTIAL + PRIMARY_TRANSCRIPT_FRAGMENT_FOUND + HISTORICAL_PRIMARY_PATH_IDENTIFIED`.** The exact historical Claude Code session path is `/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`, recorded at recovery time as 1,252 lines / 5,692,731 bytes. The Library contains `PREFLIGHTKVD06REV14001_transcript.txt`, classified by its own manifest as original transcript + contemporaneous result export from that session from line 1110 onward, with recorded identity 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`. This is genuine bounded primary evidence, not the full 22-record/26-human-turn AUD source family. The next recovery target is the full JSONL, `human_turns.txt`, or the extraction output used for the 22 AUD rows.
- **CDX — `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED`.** CDX-005 names `outputs/extract_codex_w1_2026-07-30.md`; targeted Git/Library/archive searches have not recovered it.
- **W38 — `PRIMARY_TASK_ARTIFACT_FOUND`.** Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` corroborate exact A3 instructions for W38-001..006. W38-007/008 are not source-mapped. C9 remains unverified because A8/turn chronology is missing.
- **W39 — `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL`.** `FOUR_WINDOW_CHARTER.md`, `WO_VERIFY_FIX_RPC_SHAPES.md`, `schema_contract_extract.sql`, and `RAW_CATALOG_APPENDIX.md` corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007. W39-002 remains structurally unresolved; W39-005/006 are not mapped.
- **KBD — `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE`.** Broad search across Git, July Library exports, handover archives and recovered source archives did not locate an exact four-record KIVO-BUILDER extract or sufficiently complete gh-auth/device-code/draft-PR interaction.
- **KPF — `PRIMARY_TASK_ARTIFACT_FOUND`.** `FOUR_WINDOW_CHARTER.md` corroborates exact A3 rebase governance and A12 no-PR/no-merge instruction for KPF-001. A8/chronology still lacks the primary interaction.

### Primary task-artifact archive

Recovered Library archive `all.zip`:
- size **803,462 bytes**;
- SHA-256 `d045661795fe195baebd53693ad94c4f1db5cf67cc31ebeee90803d305cad1ad`.

Exact A3/source-content corroboration established for **11/52 rows**:
- W38 — 6 rows;
- W39 — 4 rows;
- KPF — 1 row.

This is recorded separately from transcript verification in `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`.

### WP3 verification totals

- corpus rows tracked: **52/52**;
- derivative source-extract mapped: **5/52**;
- exact primary task-artifact A3/source-content corroboration: **11/52**;
- bounded AUD primary transcript fragment recovered: **YES**;
- full AUD source family recovered: **NO**;
- incident-level primary interaction/transcript C9 `CONFIRMED`: **0/52**;
- C9 `CONTRADICTED`: **0/52**.

The extract-mapped, task-artifact-corroborated and AUD-fragment evidence classes must never be collapsed into one “verified incident” count.

### Remaining WP3 priorities

1. Search specifically for the AUD full JSONL, `human_turns.txt`, or the 22-row AUD extraction output and map only incidents actually covered by recovered primary evidence.
2. Recover the named CDX extraction file and, if possible, the underlying Codex interaction.
3. Search for W38/W39/KPF interaction logs so A3 task artifacts can be paired with A8 and chronology.
4. Carry KBD as unverified unless new preservation evidence is discovered.
5. Do not upgrade any C9 status merely because A3 matches an original work order.

Durable WP3 outputs:
- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`
- `source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`
- `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`

## WP4 — Classification recommendations

**Status:** COMPLETE — ASSISTANT RECOMMENDATIONS FOR ALL 52 PREPARED; RESEARCHER AUTHORITY PRESERVED

Recommendations are explicitly provisional where primary evidence is missing. C9 remains `UNVERIFIED` for all 52. C5 is not supplied as fact by the assistant.

Headline recommendation state:
- LIKELY SII: **12**
- POSSIBLE: **11**
- NO / better explained by comparison class: **25**
- CONTROL: **4**
- Benchmark-candidate recommendation `YES`: **15**
- Benchmark-candidate recommendation `NO`: **37**

Provisional C0 review queue:
- INTENT — **22**
- COMPETENCE — **15**
- PREMISE — **7**
- META — **4**
- MIXED — **1**
- CONTROL / no positive class assigned — **3**

Durable WP4 outputs:
- `CLASSIFICATION_RECOMMENDATIONS.md`
- `CLASSIFICATION_RECOMMENDATIONS_COMPACT.tsv`
- `RESEARCHER_REVIEW_CARDS_PRIORITY.md`

## WP5 — Researcher decisions

**Owner:** Mohamed Salama  
**Status:** READY — PRIORITY REVIEW CARDS PREPARED

Researcher sequence:
1. 12 LIKELY SII rows;
2. 11 POSSIBLE/source-dependent rows;
3. 4 CONTROL rows;
4. 25 comparison-class rows.

For each row Mohamed records `ACCEPT`, `OVERRULE`, or `DEFER FOR SOURCE`. If accepting or correcting an intent/mixed event, Mohamed supplies C5 in his own words. Assistant wording is not ground truth merely because it appears in the review card.

WP3 may continue in parallel so missing source evidence can reduce the number of `DEFER FOR SOURCE` decisions.

## WP6 — Independent quality check

**Status:** DEFERRED BY FOUNDER

## WP7 — Freeze v1.1

**Status:** BLOCKED UNTIL WP5 AND LATER QC

Planned freeze outputs remain:
- validated/reviewed v1.1 dataset;
- inclusion/exclusion and comparison-class ledger;
- exact source/checksum record;
- method/version note;
- explicit source-verification status per retained row;
- no mutation of historical v1 evidence.

## WP8 — Fan exchange package

**Status:** DRAFT PACKAGE CREATED; METHODS CAN BE EXCHANGED, FINAL CORPUS NUMBERS/EXAMPLES REMAIN GATED

Created under `fan-exchange/`:
- `00_READ_ME_FIRST.md`
- `01_METHODS_NOTE.md`
- `02_SCHEMA_AND_CODEBOOK.md`
- `03_DCM2_CROSSWALK_TEMPLATE.md`
- `04_SANITIZED_EXAMPLES.md`
- `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

Before final exchange, update the package to reflect:
- exact v1 recovery;
- the two-pass 52-row audit;
- the distinction between 52 extracted candidates and the smaller provisional positive-SII set;
- current source-evidence classes and zero current C9 confirmations;
- researcher decisions once WP5 is completed.

## Current status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | **COMPLETE** |
| 2 | Audit all 52 | **COMPLETE — TWO PASSES / 52 OF 52** |
| 3 | Source conversations | **ACTIVE — GPT extract mapped; 11 A3 artifacts; AUD primary fragment recovered; 0 C9 confirmed** |
| 4 | Classification recommendations | **COMPLETE — 52 OF 52 ASSISTANT RECOMMENDATIONS** |
| 5 | Researcher decisions | **READY — REVIEW CARDS PREPARED** |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | DRAFT CREATED / FINAL GATED |

## Update rule

Update this file after every material discovery, completed work package, evidence-status change, or blocker. GitHub Issue #3 mirrors high-level state; this file remains the durable branch-level research handoff.
