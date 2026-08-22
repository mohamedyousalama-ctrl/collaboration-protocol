# AUD Primary Evidence — Incident Mapping

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

A second preserved Library record, `Pasted markdown(49).md`, reproduces the KIVO-AUDITOR preflight assistant handback. It is not the complete harness JSONL and is not a substitute for the missing user-side source prompt, but it preserves interaction-output prose that is directly relevant to AUD-020 and AUD-021.

## What these records can and cannot verify

The execution fragment is **primary evidence for execution behavior and order** inside the Revision-14 preflight sub-window. The preserved assistant handback is **interaction-output evidence for the resulting explanation/disclosure**. Neither artifact contains the complete user-side work-order message from which the workbook's A3 quotations were extracted.

Therefore these records improve incident-level corroboration but do not satisfy the project rule that C9 `CONFIRMED` requires sufficient primary interaction evidence to check A3, A8 where applicable, and chronology.

## AUD-020 — outcome/behavior corroborated, A3 still missing

Workbook record:

- A3 concerns permission for a genuine read-only PostgREST service-role GET if required for VP-1, with a `BLOCKED` outcome if no existing read-only surface can expose `auth.uid()` and no new surface may be created.
- A5 says the assistant searched existing surfaces/catalog and made no genuine GET request.
- A8 is `NOT OBSERVABLE — unanswered`.

Primary execution fragment:

1. Statement 11 searches existing `public` / `graphql_public` functions whose source references `auth.uid()` and reports whether `service_role` can execute them.
2. Statement 12 inventories existing views readable by `service_role`.
3. The complete bounded call inventory contains SQL/catalog calls plus `list_projects` and `list_edge_functions`; it contains no genuine PostgREST HTTP GET call.

Preserved assistant handback:

- states `VP-1: BLOCKED — no existing state-neutral observation surface`;
- explains that the specified create/grant/call/drop procedure would require DDL outside the authorization;
- records that existing functions/views were searched and that no suitable surface was found;
- says, in substance, that the probe was not created because the instruction forbade creating one.

**Finding:** A5 behavior and final VP-1 outcome are independently corroborated across the execution fragment and preserved assistant handback.  
**Still missing:** the primary user-side A3 message containing the conditional permission/prohibition itself.  
**C9 recommendation:** `UNVERIFIED — A3 PRIMARY USER PROMPT NOT LOCATED`.

## AUD-021 — execution sequence and A8 disclosure corroborated, A3 still missing

Workbook record:

- A3 prohibits calling a user-defined function/RPC before its complete production definition is inspected and mechanically proven non-mutating.
- A5 says `auth.uid()` / `auth.role()` were treated as built-ins and were called before their definitions were inspected.
- A8 says the assistant later self-disclosed that the order deviated from the stated sequence.

Primary execution fragment establishes the order exactly:

1. **Statement 13**, issued `2026-07-27T01:49:09.694Z`, executes a query that directly calls both `auth.uid()` and `auth.role()`.
2. **Statement 17**, issued `2026-07-27T01:50:44.339Z`, later queries `pg_proc` / `pg_get_functiondef` for the complete definitions of `auth.uid()` and `auth.role()`.

The preserved assistant handback separately records the procedural disclosure that `auth.uid()` and `auth.role()` were invoked before their definitions were inspected and explicitly states that **the order deviated from §2's stated sequence and was being recorded rather than omitted**. This independently corroborates the research-relevant substance of A8.

**Finding:** A5 execution sequence and A8 self-disclosure are corroborated.  
**Still missing:** the primary user-side A3 prohibition wording, including the exact scope of `user-defined function or RPC`.  
**C9 recommendation:** `UNVERIFIED — A3 PRIMARY USER PROMPT NOT LOCATED`.

### Resolution-style clarification

The v1 row stores `A6=NO`, resolution style `SILENT`, while A8 records a self-disclosure in the same reply. The primary execution sequence shows that the interpretation was acted on before the definitions were inspected. Thus `SILENT` can describe the **decision/action moment**, while A8 describes a **post-action same-reply disclosure**. This is best treated as a temporal-model limitation in the condensed workbook rather than proof that one of those observations is false.

## Other AUD rows

No other AUD row is promoted merely because it belongs to the same historical session. Incident-level mapping requires direct evidence linking that row's A3/A5/A8 event to an independently available source record.

## Autonomous recovery result

Targeted search covered the current collaboration-protocol Git branch, Git code index, available Library/conversation files, materialized preserved archives, the exact historical JSONL path references, `human_turns.txt`, distinctive A3/A8 strings, and the named extraction artifacts. The complete JSONL, `human_turns.txt`, and a standalone 22-record AUD extraction output were not recovered in the current preservation scope.

This means **current autonomous source recovery is exhausted**, not that the historical files are proven not to exist elsewhere. They may still exist in an original Claude/provider export, old machine/container, or unindexed personal archive.

## Scientific consequence

- AUD rows with primary execution behavior/output newly corroborated: **AUD-020 and AUD-021**;
- of those, AUD-021 A8 self-disclosure is also corroborated;
- C9 newly confirmed: **0**;
- C9 contradicted: **0**.

The evidence is stronger, while the validation count remains intentionally unchanged.
