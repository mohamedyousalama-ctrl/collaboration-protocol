# Source Conversation Availability Register

**Workstream:** 52-record naturalistic corpus validation  
**Branch:** `research/fan-corpus-validation-2026-08-22`  
**Purpose:** establish, family by family, what source evidence exists and whether it is sufficient for primary quote/chronology verification.

## Evidence rule

A workbook row, research summary, derivative LLM extraction, original task artifact, historical path reference, or partial transcript is not automatically equivalent to a complete source conversation. C9 can be recommended as `CONFIRMED` only when A3/A8 and chronology can be checked against independently available primary interaction evidence.

Availability states used here:

- `PRIMARY_TRANSCRIPT_FOUND` — complete or sufficiently complete original interaction record is currently available and readable for the incident(s) being verified.
- `PRIMARY_TRANSCRIPT_FRAGMENT_FOUND` — an original interaction/export fragment is available, but it covers only a bounded sub-window and cannot stand in for the whole source family.
- `PRIMARY_TASK_ARTIFACT_FOUND` — original work order/instruction/payload located and able to corroborate A3 or context, but not the complete incident chronology.
- `SOURCE_EXTRACT_ONLY` — extraction report derived from the conversation exists, but no independently complete transcript.
- `PARTIAL` — some source evidence exists but completeness is not established.
- `HISTORICAL_PRIMARY_PATH_IDENTIFIED` — a contemporaneous record gives the exact location/identity of a primary interaction file, but that complete file itself is not currently recovered in this preservation scope.
- `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` — corpus names a historical extraction file that has not yet been recovered.
- `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` — extensive current Git/Library/archive search did not locate the relevant transcript/extract; future recovery remains possible.

## Family matrix

| Family | Records | Current state | Evidence currently established | Next verification action |
|---|---:|---|---|---|
| GPT | 5 | `SOURCE_EXTRACT_ONLY` | Recovered `extract_chatgpt_w1_2026-07-30.md`, 12,815 bytes, SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`. It maps GPT-001..005 and restores full A4, but explicitly reports source-window truncation/compaction. | Continue search for an independently readable primary GPT transcript. C9 stays UNVERIFIED. |
| AUD | 22 | `PARTIAL` + `PRIMARY_TRANSCRIPT_FRAGMENT_FOUND` + `HISTORICAL_PRIMARY_PATH_IDENTIFIED` | The exact historical Claude Code session path is known: `/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl` (recorded as 1,252 lines / 5,692,731 bytes at recovery time). The Library now contains `PREFLIGHTKVD06REV14001_transcript.txt`, classified in its own header/manifest as **original transcript + contemporaneous result export**, extracted from that JSONL from line 1110 onward; its recorded identity is 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`. A redacted audit copy and manifest are also present. This is genuine primary evidence for the bounded preflight sub-window, not the complete 26-human-turn AUD source family. | Map only AUD incidents whose A3/A8 actually fall inside this recovered preflight fragment. Continue searching for the full JSONL or the separate `human_turns.txt` / extraction output used for the 22 AUD records. |
| CDX | 5 | `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` | CDX-005 states that the protocol output was saved to `outputs/extract_codex_w1_2026-07-30.md`. Current Git/Library/archive search has not recovered that exact file. | Recover the named extract and separately search for the primary Codex thread. |
| W38 | 8 | `PRIMARY_TASK_ARTIFACT_FOUND` | Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` were recovered. Exact A3 instructions are corroborated for W38-001..006. W38-007 exact A3 and W38-008 source interaction are not located. | Search for W38 conversation/extract so A8 and chronology can be verified. |
| W39 | 7 | `PRIMARY_TASK_ARTIFACT_FOUND / PARTIAL` | Original `FOUR_WINDOW_CHARTER.md`, `WO_VERIFY_FIX_RPC_SHAPES.md`, `schema_contract_extract.sql`, and `RAW_CATALOG_APPENDIX.md` corroborate A3/source content for W39-001, W39-003, W39-004 and W39-007. W39-002 remains unmapped/structurally defective; exact sources for W39-005/006 are not located. | Search for W39 interaction/extract; prioritize W39-002 and authority chronology for W39-007. |
| KBD | 4 | `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` | Broad search across Git, July Library writing blocks/text exports, Kivo handover archives and the recovered `all.zip` source archive did not locate an exact four-record KIVO-BUILDER extract or sufficiently complete interaction containing the gh-auth/device-code/draft-PR sequence. | Carry KBD as unverified unless a new source is recovered; do not infer confirmation from the workbook. |
| KPF | 1 | `PRIMARY_TASK_ARTIFACT_FOUND` | `FOUR_WINDOW_CHARTER.md` contains the exact rebase-before-every-push A3 rule and exact no-PR/no-merge A12 governance text used by KPF-001. | Search for the KIVO-PROOF interaction/extract to verify A8 and chronology. |

## AUD primary-evidence clarification

The AUD family now has a stronger evidence chain than the earlier register showed:

1. A preservation/provenance record states that the raw transcripts behind the 52 incident records were **not** included in that Claude project; only extraction reports were supplied there. It gives the KIVO-AUDITOR JSONL path above as an example of where a raw source lived.
2. A later evidence-recovery handback independently names the same JSONL path, explains that the preflight wrote nothing to a scratch transcript at execution time, and states that the harness-written session record was used as the primary source.
3. The Library contains the resulting unredacted `PREFLIGHTKVD06REV14001_transcript.txt`, a redacted audit copy, and the evidence manifest. The manifest classifies the unredacted file as original transcript + contemporaneous result export and records that only MCP wrapper/boundary scaffolding was stripped while query/result payloads were left unaltered.

This upgrades AUD from path-only provenance to **primary transcript fragment recovered**. It does **not** justify marking all 22 AUD rows verified, because the recovered fragment begins at session-record line 1110 and covers the Revision-14 SELECT-only preflight sub-window, while the 22-record corpus spans a much larger interaction and the preserved notes refer separately to a later `human_turns.txt` extraction artifact.

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
- AUD bounded primary transcript fragment recovered: **yes**, from the known historical JSONL source;
- full AUD family transcript recovered: **no**;
- primary transcript/source-interaction C9 `CONFIRMED`: **0/52** pending incident-level A3/A8 mapping;
- C9 `CONTRADICTED`: **0/52**.

AUD remains the highest-value unresolved recovery target because the primary source identity is known and a real fragment is already recovered. The next AUD search target is specifically the full JSONL, `human_turns.txt`, or the extraction report that generated the 22 rows. CDX is second because the corpus records an exact historical extraction filename. KBD has been searched broadly enough to carry as `NOT_FOUND_IN_CURRENT_PRESERVATION_SCOPE` rather than pretending the transcript is available.
