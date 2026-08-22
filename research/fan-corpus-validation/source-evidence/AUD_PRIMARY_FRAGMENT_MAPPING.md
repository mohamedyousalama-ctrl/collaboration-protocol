# AUD Primary Transcript Fragment — Incident Mapping

**WP:** 3 — source discovery / primary-evidence verification  
**Date:** 22 August 2026

## Source identity

A genuine primary execution fragment from the historically identified KIVO-AUDITOR Claude Code session is available in the user's preserved Library as `PREFLIGHTKVD06REV14001_transcript.txt`.

Recorded source identity:

- underlying session: `/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`
- extraction scope: source-record line 1110 onward
- transcript fragment: 32,645 bytes / 482 lines
- SHA-256: `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`
- execution window: `2026-07-27T01:47:05.509Z` through `2026-07-27T01:50:44.339Z`
- recorded calls: 17 `execute_sql` statements plus two non-SQL read-only calls

The source manifest classifies it as original transcript + contemporaneous result export. Query/result payloads are recorded from the harness-written session record, with MCP transport scaffolding stripped.

## What this fragment can and cannot verify

This fragment is **primary evidence for execution behavior and order** inside the Revision-14 preflight sub-window. It is **not** the full AUD conversation transcript. In particular, this extracted file does not contain the exact user A3 instructions or the assistant's later prose handback/self-disclosure. Therefore it cannot by itself satisfy C9 for any incident requiring A3 + A8 + full chronology.

## AUD-020 — partial primary-behavior corroboration

Workbook record:

- A3 concerns permission for a genuine read-only PostgREST service-role GET if required for VP-1, with a `BLOCKED` outcome if no existing read-only surface can expose `auth.uid()` and no new surface may be created.
- A5 says the assistant searched existing surfaces/catalog and made no genuine GET request.

Primary fragment evidence:

1. Statement 11 searches existing `public` / `graphql_public` functions whose source references `auth.uid()` and reports whether `service_role` can execute them.
2. Statement 12 inventories existing views readable by `service_role`.
3. The complete bounded call inventory contains SQL/catalog calls plus `list_projects` and `list_edge_functions`; it contains no genuine PostgREST HTTP GET call.

**Finding:** `A5 PRIMARY EXECUTION BEHAVIOR CORROBORATED` for the bounded preflight fragment.  
**Not verified:** exact A3 wording, the final VP-1 prose conclusion/A8, and full interaction chronology.  
**C9 recommendation:** `UNVERIFIED — PRIMARY BEHAVIOR FRAGMENT ONLY`.

## AUD-021 — sequence independently corroborated

Workbook record:

- A3 prohibits calling a user-defined function/RPC before its complete production definition is inspected and mechanically proven non-mutating.
- A5 says `auth.uid()` / `auth.role()` were treated as built-ins and were called before their definitions were inspected.
- A8 says the assistant later self-disclosed that the order deviated from the stated sequence.

Primary fragment evidence establishes the execution order exactly:

1. **Statement 13**, issued `2026-07-27T01:49:09.694Z`, executes a query that directly calls both `auth.uid()` and `auth.role()`.
2. **Statement 17**, issued `2026-07-27T01:50:44.339Z`, later queries `pg_proc` / `pg_get_functiondef` for the complete definitions of `auth.uid()` and `auth.role()`.

Therefore the primary execution record independently proves **call first → definition inspection later**.

**Finding:** `A5 PRIMARY EXECUTION SEQUENCE CORROBORATED`.  
**Not verified from this fragment:** exact A3 prohibition wording and the A8 self-disclosure phrase, because neither is included in the bounded execution export.  
**C9 recommendation:** `UNVERIFIED — PRIMARY BEHAVIOR FRAGMENT ONLY`.

### Resolution-style clarification

The v1 row stores `A6=NO`, resolution style `SILENT`, while A8 says the deviation was self-disclosed in the same reply. The primary execution sequence shows that the interpretation was indeed acted on before the definitions were inspected. Thus `SILENT` can describe the **decision/action moment**, while the later A8 disclosure can describe a **post-action same-reply disclosure**. This is better treated as a temporal-model limitation in the condensed workbook rather than proof that one of those two facts is false.

## Other AUD rows

No other AUD row is promoted by this fragment merely because it belongs to the same historical session. Incident-level mapping requires direct evidence that the row's A3/A5/A8 event falls inside the recovered fragment.

## Scientific consequence

This recovery improves the evidence state without inflating validation counts:

- primary execution behavior newly corroborated: **AUD-020 and AUD-021**;
- C9 newly confirmed: **0**;
- C9 contradicted: **0**.

The full AUD JSONL, `human_turns.txt`, or the extraction output used to derive all 22 AUD rows remains the key recovery target.
