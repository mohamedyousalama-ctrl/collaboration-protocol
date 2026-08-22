# Source Conversation Availability Register

**Workstream:** 52-record naturalistic corpus validation  
**Branch:** `research/fan-corpus-validation-2026-08-22`  
**Purpose:** establish, family by family, what source evidence exists and whether it is sufficient for primary quote/chronology verification.  
**Autonomous recovery state:** COMPLETE FOR CURRENT PRESERVATION SCOPE.

## Evidence rule

A workbook row, research summary, derivative LLM extraction, original task artifact, historical path reference, partial execution transcript, or preserved assistant handback is not automatically equivalent to a complete source interaction. C9 can be recommended as `CONFIRMED` only when A3/A8 and chronology can be checked against independently available primary interaction evidence.

Availability states used here:

- `PRIMARY_TRANSCRIPT_FOUND` — complete or sufficiently complete original interaction record is currently available and readable for the incident(s) being verified.
- `PRIMARY_TRANSCRIPT_FRAGMENT_FOUND` — an original interaction/export fragment is available, but it covers only a bounded sub-window and cannot stand in for the whole source family.
- `PRIMARY_TASK_ARTIFACT_FOUND` — original work order/instruction/payload located and able to corroborate A3 or context, but not the complete incident chronology.
- `INTERACTION_OUTPUT_FOUND` — preserved assistant-side output/handback exists and can corroborate A8/outcome, but the user-side source message may still be missing.
- `SOURCE_EXTRACT_ONLY` — extraction report derived from the conversation exists, but no independently complete transcript.
- `PARTIAL` — some source evidence exists but completeness is not established.
- `HISTORICAL_PRIMARY_PATH_IDENTIFIED` — a contemporaneous record gives the exact location/identity of a primary interaction file, but that complete file itself is not currently recovered in this preservation scope.
- `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` — corpus names a historical extraction file that has not been recovered.
- `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` — targeted current Git/Library/archive search did not locate the relevant transcript/extract; future recovery remains possible.

## Family matrix

| Family | Records | Current state | Evidence currently established | Autonomous conclusion |
|---|---:|---|---|---|
| GPT | 5 | `SOURCE_EXTRACT_ONLY` | Recovered `extract_chatgpt_w1_2026-07-30.md`, 12,815 bytes, SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`. It maps GPT-001..005 and restores A4, but explicitly reports source-window truncation/compaction. | No independently readable primary GPT transcript recovered. C9 stays UNVERIFIED. |
| AUD | 22 | `PARTIAL` + `PRIMARY_TRANSCRIPT_FRAGMENT_FOUND` + `INTERACTION_OUTPUT_FOUND` + `HISTORICAL_PRIMARY_PATH_IDENTIFIED` | Historical session path: `/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`, recorded as 1,252 lines / 5,692,731 bytes. Recovered `PREFLIGHTKVD06REV14001_transcript.txt`: 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`, extracted from line 1110 onward. A preserved assistant preflight handback additionally corroborates AUD-020 outcome and AUD-021 self-disclosure. | AUD-020/021 have stronger behavior/output evidence, but the user-side A3 preflight prompt, full JSONL, `human_turns.txt`, and full 22-record extraction output remain unrecovered. C9 stays UNVERIFIED. |
| CDX | 5 | `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` | CDX-005 states that the protocol output was saved to `outputs/extract_codex_w1_2026-07-30.md`. Exact Git code search plus Library/conversation/archive searches did not recover it. | Named extract and primary Codex interaction remain unavailable in current preservation scope. |
| W38 | 8 | `PRIMARY_TASK_ARTIFACT_FOUND` | Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` corroborate exact A3 instructions for W38-001..006. | No interaction/extract recovered for A8/chronology; W38-007/008 source interaction remains not found. |
| W39 | 7 | `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL` | `FOUR_WINDOW_CHARTER.md`, `WO_VERIFY_FIX_RPC_SHAPES.md`, `schema_contract_extract.sql`, and `RAW_CATALOG_APPENDIX.md` corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007. | Interaction chronology remains unavailable; W39-002 exact trigger and W39-005/006 source interactions remain not found. |
| KBD | 4 | `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` | Broad plus final distinctive-string search across Git, Library writing blocks/text exports, Kivo handover archives and recovered source archives did not locate an exact four-record KIVO-BUILDER extract or sufficiently complete gh-auth/device-code/draft-PR interaction. | Carry all four as unverified unless new source material is supplied/recovered. |
| KPF | 1 | `PRIMARY_TASK_ARTIFACT_FOUND` | `FOUR_WINDOW_CHARTER.md` contains the exact rebase-before-every-push A3 rule and no-PR/no-merge A12 governance text used by KPF-001. | No KIVO-PROOF interaction/extract recovered for A8/chronology. |

## AUD evidence clarification

The AUD family has the strongest recovered primary-evidence chain, but it is still incomplete:

1. A preservation/provenance record states that raw transcripts behind the 52 incident records were not included in that later research project and gives the KIVO-AUDITOR JSONL path as an example of where a raw source lived.
2. A later evidence-recovery handback names the same JSONL path and states that a harness-written session record was used as the primary source.
3. The Library contains the unredacted `PREFLIGHTKVD06REV14001_transcript.txt`, a redacted audit copy, and a manifest identifying the unredacted file as original transcript + contemporaneous result export.
4. A separate preserved assistant preflight handback records `VP-1: BLOCKED` reasoning and the procedural disclosure that `auth.uid()` / `auth.role()` were called before their definitions were inspected. This strengthens AUD-020 and AUD-021 at A5/outcome/A8, but still does not recover the user-side A3 message.

Detailed incident mapping is in `source-evidence/AUD_PRIMARY_FRAGMENT_MAPPING.md`.

## Primary task-artifact recovery

A preserved Library archive `all.zip` was inspected during WP3:

- size: **803,462 bytes**
- SHA-256: `d045661795fe195baebd53693ad94c4f1db5cf67cc31ebeee90803d305cad1ad`

Exact A3/source-content corroboration was established for **11 corpus rows**:

- W38: 6 rows — W38-001 through W38-006;
- W39: 4 rows — W39-001, W39-003, W39-004, W39-007;
- KPF: 1 row — KPF-001.

Detailed mapping is preserved in `source-evidence/PRIMARY_TASK_ARTIFACT_INDEX.md`.

**Method boundary:** these 11 are `A3 CORROBORATED`, not C9 `CONFIRMED`. The artifacts generally do not contain the assistant interpretation, A8 mismatch signal, or full turn order.

## GPT source-extract mapping

GPT is derivative-source-extract mapped 5/5. Full provenance, recovered A4 fields and the report's own limitations are recorded in `source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`. This improves extraction provenance but does not upgrade C9.

## Search scope completed

The autonomous recovery pass covered:

- the collaboration-protocol Git branch and Git code index;
- available Library and conversation files;
- exact phrase searches using distinctive A3/A8 text;
- preserved ZIP/source archives materialized during WP3;
- historical source-path and filename references;
- targeted searches for `human_turns.txt` and `outputs/extract_codex_w1_2026-07-30.md`;
- final targeted searches for W38/W39/KBD/KPF mismatch phrases.

No additional complete source interaction was found.

`NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` means only that autonomous recovery from the currently accessible evidence is exhausted. It does not prove that an original provider export, old machine, destroyed container, or unindexed personal archive cannot contain the historical source.

## Current conclusion

We **do not have all seven complete source conversations in Git or in the currently recovered preservation set**.

Current evidence progress:

- corpus rows tracked: **52/52**;
- derivative source-extract mapped: **5/52** (GPT);
- exact primary task-artifact A3/source-content corroboration: **11/52** (W38/W39/KPF);
- primary AUD behavior/output corroboration: **2/52** (AUD-020/AUD-021);
- AUD-021 A8 disclosure corroborated: **yes**;
- primary interaction C9 `CONFIRMED`: **0/52**;
- C9 `CONTRADICTED`: **0/52**.

These evidence categories are deliberately separate and must not be combined into a fake `verified N`.

Further WP3 improvement now depends on **new source material**, not more autonomous searching of the current preservation set. Rows without sufficient source evidence remain unverified rather than being guessed into confirmation.
