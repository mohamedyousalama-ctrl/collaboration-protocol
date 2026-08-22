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
7. Preserve all limitations, contradictions, exclusions, source-access gaps, and recovery defects.

## WP1 — Freeze and reconstruct v1

**Status:** COMPLETE — AUTHORITATIVE V1 RECOVERED AND VERIFIED

Exact v1 identity: 31,471 bytes; SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.

The incomplete historical Git Base64 representation remains untouched. The exact workbook was recovered from `files(3).zip`, whose SHA-256 `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8` exactly matches the repository source-bundle manifest. GitHub Actions independently reconstructed and verified the recovered branch representation.

Durable evidence:
- `RECOVERY_PROVENANCE_AND_FREEZE.md`
- `work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `work/authoritative_v1_inventory.json`
- `work/incident_rows.tsv`
- `recovered-source/AUTHORITATIVE_V1_SHA256.txt`

## WP2 — Audit all 52 records

**Status:** COMPLETE — 52/52 AUDITED

Disposition counts:
- `PASS_TO_SOURCE_VERIFICATION` — **21**
- `NEEDS_SOURCE` — **11**
- `STRUCTURAL_DEFECT` — **2**
- `EXCLUDE_CANDIDATE` — **18**

`EXCLUDE_CANDIDATE` means exclude from the SII-analysis candidate set on present evidence, not delete from the corpus.

Major findings:
1. A4 Possible interpretations is absent as a dedicated workbook column.
2. The v1 A6-only silent-inference aggregate can miscount disclosed events as silent.
3. AUD-021 has a resolution-style contradiction.
4. W39-002 lacks the required observable triggering quote in v1.
5. AUD-022 uses a resolution-style label outside the listed Codebook values.
6. A9 awareness-gap values require normalization before statistics.
7. Seven records have substantial A3/A8 overlap and require source chronology review.
8. Suggested outcome lacks a separate researcher-final field.
9. One C0 suggestion uses non-final-codebook label `DEFINITION→INTENT`.

Durable outputs:
- `CORPUS_AUDIT_52.md`
- `corpus-audit/ROW_AUDIT_52.tsv`
- `tools/wp2_audit.py`

## WP3 — Locate and verify seven source conversations

**Status:** ACTIVE — SOURCE RECOVERY HAS ADVANCED; NO C9 CONFIRMATIONS YET

Families: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1.

### WP3 source classes now established

- **GPT — `SOURCE_EXTRACT_ONLY` / 5 of 5 mapped.** Recovered `extract_chatgpt_w1_2026-07-30.md` (12,815 bytes; SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`). It maps GPT-001..005 and restores A4, but its own limitations disclose transcript truncation/compaction. C9 remains 0/5 confirmed.
- **AUD — `PARTIAL`.** Preserved records state that a 26-human-turn raw transcript was recovered from disk for verbatim checking. Source-adjacent auditor files were searched, but the exact independently readable raw transcript is still not located/mapped.
- **CDX — `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED`.** CDX-005 names `outputs/extract_codex_w1_2026-07-30.md`; targeted Git/Library/materialized-archive searches have not recovered it.
- **W38 — `PRIMARY_TASK_ARTIFACT_FOUND`.** Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` corroborate exact A3 instructions for W38-001..006. W38-007/008 are not source-mapped. C9 remains unverified because A8/turn chronology is missing.
- **W39 — `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL`.** `FOUR_WINDOW_CHARTER.md`, `WO_VERIFY_FIX_RPC_SHAPES.md`, `schema_contract_extract.sql`, and `RAW_CATALOG_APPENDIX.md` corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007. W39-002 remains structurally unresolved; W39-005/006 are not mapped.
- **KBD — `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE`.** Broad search across Git, July Library exports, handover archives and recovered source archives did not locate an exact four-record KIVO-BUILDER extract or sufficiently complete gh-auth/device-code/draft-PR interaction.
- **KPF — `PRIMARY_TASK_ARTIFACT_FOUND`.** `FOUR_WINDOW_CHARTER.md` corroborates exact A3 rebase governance and A12 no-PR/no-merge instruction for KPF-001. A8/chronology still lacks the primary interaction.

### Primary task-artifact archive

Recovered Library archive `all.zip`:
- size **803,462 bytes**;
- SHA-256 `d045661795fe195baebd53693ad94c4f1db5cf67cc31ebeee90803d305cad1ad`.

Exact A3/source-content corroboration added for **11/52 rows**:
- W38 — 6 rows;
- W39 — 4 rows;
- KPF — 1 row.

This is recorded separately from transcript verification in `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`.

### WP3 verification totals

- corpus rows tracked: **52/52**;
- derivative source-extract mapped: **5/52**;
- exact primary task-artifact A3/source-content corroboration: **11/52**;
- primary interaction/transcript C9 `CONFIRMED`: **0/52**;
- C9 `CONTRADICTED`: **0/52**.

The 5 extract-mapped and 11 task-artifact-corroborated rows are different evidence classes and must **not** be reported as "16 verified incidents".

### Remaining WP3 priorities

1. Recover the AUD raw transcript explicitly referenced by the preserved research record.
2. Recover the named CDX extraction file and, if possible, the underlying Codex interaction.
3. Search for W38/W39/KPF interaction logs to pair A3 task artifacts with A8/chronology.
4. Carry KBD as unverified unless new preservation evidence is discovered.
5. Do not upgrade any C9 status merely because A3 matches an original work order.

Durable WP3 outputs:
- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`
- `source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`
- `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`

## WP4 — Classification recommendations

**Status:** READY TO START IN PARALLEL FOR EVIDENCE-ELIGIBLE ROWS, WHILE C9 REMAINS UNVERIFIED

WP2 is complete and WP3 has now established evidence classes. ChatGPT may prepare explicit **recommendations** for C0, C1, C2, C3, C4, C6, C7, C8, C9, C10 without pretending they are researcher decisions. Any recommendation dependent on missing primary interaction evidence must be marked provisional/unverified.

`C5 TRUE INTENT` remains exclusively Mohamed's researcher decision.

## WP5 — Researcher decisions

**Owner:** Mohamed Salama  
**Status:** WAITING FOR WP4 REVIEW CARDS

## WP6 — Independent quality check

**Status:** DEFERRED BY FOUNDER

## WP7 — Freeze v1.1

**Status:** BLOCKED UNTIL WP5 AND LATER QC

## WP8 — Fan exchange package

**Status:** DRAFT PACKAGE CREATED; FINAL NUMBERS/EXAMPLES WAIT ON VALIDATION

Created under `fan-exchange/`:
- `00_READ_ME_FIRST.md`
- `01_METHODS_NOTE.md`
- `02_SCHEMA_AND_CODEBOOK.md`
- `03_DCM2_CROSSWALK_TEMPLATE.md`
- `04_SANITIZED_EXAMPLES.md`
- `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

## Current status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | **COMPLETE** |
| 2 | Audit all 52 | **COMPLETE — 52/52** |
| 3 | Source conversations | **ACTIVE — 5 extract-mapped; 11 A3 artifact-corroborated; 0 C9 confirmed** |
| 4 | Classification recommendations | **READY TO START IN PARALLEL** |
| 5 | Researcher decisions | WAITING FOR WP4 |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | DRAFT CREATED |

## Update rule

Update this file after every material discovery, completed work package, evidence-status change, or blocker. GitHub Issue #3 mirrors high-level state; this file remains the durable branch-level research handoff.
