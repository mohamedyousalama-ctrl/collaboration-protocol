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
- `NOT_FOUND` — no independently readable primary/source transcript located after the current search scope.
- `SEARCH_PENDING` — not yet fully searched.

## Family matrix

| Family | Records | Current state | Evidence currently established | Next verification action |
|---|---:|---|---|---|
| GPT | 5 | `SEARCH_PENDING` | 5 rows present in authoritative workbook; no complete primary GPT conversation artifact yet proven in Git/recovered research bundle. | Search preserved chat/source bundles and prior conversation exports for GPT-001..005 anchors. |
| AUD | 22 | `PARTIAL` | Master Knowledge File explicitly states the AUD raw transcript was recovered from disk for verbatim checking. Authoritative workbook contains 22 AUD rows. Exact independently readable transcript artifact still must be located/mapped in preserved sources before C9 confirmation. | Locate recovered AUD transcript/source extract and map turns/incidents. |
| CDX | 5 | `SEARCH_PENDING` | 5 rows present; workbook/research record references Codex extraction activity, but complete primary Codex conversation not yet proven available. | Search source bundles for `extract_codex_w1_2026-07-30.md`, Codex transcript, and CDX anchors. |
| W38 | 8 | `SEARCH_PENDING` | 8 rows present; no complete primary W38 conversation artifact yet proven. | Search archived chat inputs/source bundles for W38/WO-PROOF anchors. |
| W39 | 7 | `SEARCH_PENDING` | 7 rows present; W39-002 itself records original E0 WO text as not observable in the condensed evidence. No complete primary W39 transcript yet proven. | Search source bundles for W39/E0/VERIFY-FIX/FIX-2 anchors; specifically attempt recovery for W39-002. |
| KBD | 4 | `SEARCH_PENDING` | 4 rows present; no complete primary KIVO-BUILDER conversation artifact yet proven. | Search preserved KIVO-BUILDER/Claude chat bundles and exact KBD anchors. |
| KPF | 1 | `SEARCH_PENDING` | 1 row present; no complete primary KIVO-PROOF conversation artifact yet proven. | Search preserved KIVO-PROOF source bundles and stale-base anchor. |

## Current conclusion

We **do not yet have evidence to say all seven complete source conversations are in Git**.

What is established:

1. the authoritative 52-row workbook is now recovered and exact;
2. the workbook README says its A-fields were condensed from extraction reports and that full text lives in source extract files;
3. the preserved Master Knowledge File states that the AUD raw transcript was recovered from disk;
4. the `files(3).zip` research source bundle contains the corpus/protocol/research documents but does not, by itself, establish complete primary transcripts for all seven families.

WP3 now searches broader preserved source bundles and library archives rather than treating workbook text as a substitute for primary evidence.
