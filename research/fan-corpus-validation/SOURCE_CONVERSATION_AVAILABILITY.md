# Source Conversation Availability Register

**Workstream:** 52-record naturalistic corpus validation  
**Branch:** `research/fan-corpus-validation-2026-08-22`  
**Purpose:** establish, family by family, what source evidence exists and whether it is sufficient for primary quote/chronology verification.

## Evidence rule

A workbook row, research summary, derivative LLM extraction, or original task artifact is not automatically equivalent to a complete source conversation. C9 can be recommended as `CONFIRMED` only when A3/A8 and chronology can be checked against independently available primary interaction evidence.

Availability states used here:

- `PRIMARY_TRANSCRIPT_FOUND` — complete or sufficiently complete original interaction record located.
- `PRIMARY_TASK_ARTIFACT_FOUND` — original work order/instruction/payload located and able to corroborate A3 or context, but not the complete incident chronology.
- `SOURCE_EXTRACT_ONLY` — extraction report derived from the conversation exists, but no independently complete transcript.
- `PARTIAL` — some source evidence exists but completeness is not established.
- `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` — corpus names a historical extraction file that has not yet been recovered.
- `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` — extensive current Git/Library/archive search did not locate the relevant transcript/extract; future recovery remains possible.
- `SEARCH_PENDING` — source discovery is not yet sufficiently exhausted.

## Family matrix

| Family | Records | Current state | Evidence currently established | Next verification action |
|---|---:|---|---|---|
| GPT | 5 | `SOURCE_EXTRACT_ONLY` | Recovered `extract_chatgpt_w1_2026-07-30.md`, 12,815 bytes, SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`. It maps GPT-001..005 and restores full A4, but explicitly reports source-window truncation/compaction. | Continue search for an independently readable primary GPT transcript. C9 stays UNVERIFIED. |
| AUD | 22 | `PARTIAL` | Master Knowledge File and AUD-018 state that a raw transcript was recovered from disk for verbatim checking. Multiple auditor/source-adjacent files were searched, but the exact independently readable raw transcript has not yet been located and mapped. | Continue targeted recovery of the raw AUD transcript/extract. |
| CDX | 5 | `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` | CDX-005 states that the protocol output was saved to `outputs/extract_codex_w1_2026-07-30.md`. Current Git/Library/archive search has not recovered that exact file. | Recover the named extract and separately search for the primary Codex thread. |
| W38 | 8 | `PRIMARY_TASK_ARTIFACT_FOUND` | Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` were recovered. Exact A3 instructions are corroborated for W38-001..006. W38-007 exact A3 and W38-008 source interaction are not located. | Search for W38 conversation/extract so A8 and chronology can be verified. |
| W39 | 7 | `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL` | Original `FOUR_WINDOW_CHARTER.md`, `WO_VERIFY_FIX_RPC_SHAPES.md`, `schema_contract_extract.sql`, and `RAW_CATALOG_APPENDIX.md` corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007. W39-002 remains unmapped/structurally defective; exact sources for W39-005/006 are not located. | Search for W39 interaction/extract; prioritize W39-002 and authority chronology for W39-007. |
| KBD | 4 | `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` | Broad search across Git, July Library writing blocks/text exports, Kivo handover archives and the recovered `all.zip` source archive did not locate an exact four-record KIVO-BUILDER extract or sufficiently complete interaction containing the gh-auth/device-code/draft-PR sequence. | Carry KBD as unverified unless a new source is recovered; do not infer confirmation from the workbook. |
| KPF | 1 | `PRIMARY_TASK_ARTIFACT_FOUND` | `FOUR_WINDOW_CHARTER.md` contains the exact rebase-before-every-push A3 rule and exact no-PR/no-merge A12 governance text used by KPF-001. | Search for the KIVO-PROOF interaction/extract to verify A8 and chronology. |

## Primary task-artifact recovery

A preserved Library archive `all.zip` was inspected during WP3:

- size: **803,462 bytes**
- SHA-256: `d045661795fe195baebd53693ad94c4f1db5cf67cc31ebeee90803d305cad1ad`

It contains original Kivo task artifacts. Exact A3/source-content corroboration was established for **11 corpus rows**:

- W38: 6 rows — W38-001 through W38-006;
- W39: 4 rows — W39-001, W39-003, W39-004, W39-007;
- KPF: 1 row — KPF-001.

Detailed mapping is preserved in `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`.

**Method boundary:** these 11 are `A3 CORROBORATED`, not C9 `CONFIRMED`. The artifacts usually do not contain the assistant interpretation, A8 mismatch signal, or the full turn order.

## GPT source-extract mapping

GPT is source-extract mapped 5/5. Full provenance, recovered A4 fields and the report's own limitations are recorded in `source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`.

This improves extraction provenance but **does not improve C9 to CONFIRMED**.

## Current conclusion

We **do not have evidence that all seven complete source conversations are in Git or in the currently recovered preservation set**.

Current source-evidence progress:

- corpus rows tracked: **52/52**;
- derivative source-extract mapped: **5/52** (GPT);
- exact primary task-artifact A3/source-content corroboration: **11/52** (W38/W39/KPF);
- primary transcript/source-interaction C9 `CONFIRMED`: **0/52**;
- C9 `CONTRADICTED`: **0/52**.

AUD remains the highest-value unresolved recovery target because the preserved research record explicitly says a raw transcript existed. CDX is second because the corpus records an exact historical extraction filename. KBD has now been searched broadly enough to carry as `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` rather than pretending the transcript is available.
