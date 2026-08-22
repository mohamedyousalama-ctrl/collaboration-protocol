# Source Conversation Availability Register

**Workstream:** 52-record naturalistic corpus validation  
**Branch:** `research/fan-corpus-validation-2026-08-22`  
**Purpose:** establish, family by family, whether primary transcript evidence exists for quote/chronology verification.

## Evidence rule

A workbook row, research summary, or prior LLM extraction is **not** itself a primary transcript. C9 can be recommended as `CONFIRMED` only when A3/A8 can be checked against independently available primary conversation evidence.

Availability states used here:

- `PRIMARY_TRANSCRIPT_FOUND` — complete or sufficiently complete original conversation record located.
- `SOURCE_EXTRACT_ONLY` — an extraction/report derived from the conversation exists, but not the original transcript.
- `PARTIAL` — some primary conversation material exists but completeness for all mapped incidents is not yet established.
- `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` — corpus evidence names a historical source-extract file, but that file has not yet been recovered.
- `NOT_FOUND` — no independently readable primary/source transcript located after the current search scope.
- `SEARCH_PENDING` — not yet fully searched.

## Family matrix

| Family | Records | Current state | Evidence currently established | Next verification action |
|---|---:|---|---|---|
| GPT | 5 | `SOURCE_EXTRACT_ONLY` | Recovered `extract_chatgpt_w1_2026-07-30.md`, 12,815 bytes, SHA-256 `22ae455d95c1776bb2dac17fd73139c6764c7dc96fd69caddd3215da31396c83`. It contains exactly 5 extraction records with full A1–A13 including the A4 fields missing from v1 and maps directly to GPT-001..005. Its own limitations state that parts of the underlying conversation were truncated/compacted, so it is derivative evidence, not an independently complete transcript. | Continue search for an independently readable primary GPT transcript. C9 stays UNVERIFIED. |
| AUD | 22 | `PARTIAL` | Master Knowledge File explicitly states the AUD raw transcript was recovered from disk for verbatim checking. AUD-018 also records retrieval of a raw transcript from disk. Multiple auditor output/source-adjacent files exist in the Library, but the exact independently readable 26-human-turn raw transcript has not yet been located and mapped. | Locate the recovered AUD transcript or exact extraction report; map turns/incidents before C9 changes. |
| CDX | 5 | `SOURCE_EXTRACT_REFERENCED_NOT_LOCATED` | CDX-005 says the protocol was applied to the current Codex thread and saved to `outputs/extract_codex_w1_2026-07-30.md`. The historical extract is therefore referenced by the corpus itself, but current Git/Library searches have not yet located that exact file. | Recover the named extract and search separately for the primary Codex thread. |
| W38 | 8 | `SEARCH_PENDING` | 8 rows present. Current searches found source-adjacent builder/proof handbacks but no exact 8-record extraction report or complete primary W38 conversation. | Search preserved July builder/proof windows and source bundles using W38 anchors/WO-PROOF-3/4 language. |
| W39 | 7 | `SEARCH_PENDING` | 7 rows present. W39-002 itself records original E0 WO text as not observable in the condensed evidence. No exact 7-record extraction report or complete primary W39 transcript yet proven. | Search W39/E0/VERIFY-FIX/FIX-2 source windows; specifically attempt recovery for W39-002. |
| KBD | 4 | `SEARCH_PENDING` | 4 rows present; no complete primary KIVO-BUILDER conversation or 4-record extraction report yet proven. | Search KIVO-BUILDER/Claude archives using gh-auth, device-code and draft-PR anchors. |
| KPF | 1 | `SEARCH_PENDING` | 1 row present; no complete primary KIVO-PROOF conversation or one-record extraction report yet proven. | Search KIVO-PROOF archives using the strict rebase/no-PR stale-base anchor. |

## GPT source-extract mapping

The GPT family is now source-extract mapped 5/5. Full provenance, recovered A4 fields and the report's own limitations are recorded in:

`source-evidence/GPT_SOURCE_EXTRACT_INDEX.md`

This improves extraction provenance but **does not improve C9 to CONFIRMED**.

## Current conclusion

We **do not have evidence that all seven complete source conversations are in Git**.

Current source-evidence progress is:

- source-extract mapped: **GPT 5/5**;
- primary-transcript quote-confirmed: **0/52**;
- AUD has a strong preservation claim that a raw transcript existed, but the exact artifact still must be recovered;
- CDX has an exact historical extract filename recorded in the corpus, but the file has not yet been recovered;
- W38/W39/KBD/KPF remain active source-discovery work.

The authoritative workbook remains the structured candidate corpus. It is not being used as a substitute for primary transcript verification.
