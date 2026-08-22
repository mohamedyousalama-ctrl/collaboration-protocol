# Quote and Chronology Verification Register

**WP:** 3 — source discovery and primary-evidence verification  
**Rule:** C9 `CONFIRMED` requires independently available primary interaction evidence sufficient to check the incident quotation and chronology. A workbook row, derivative extraction report, original task artifact, or execution-only fragment alone cannot automatically satisfy C9.

## Evidence/status vocabulary

- `A3 CORROBORATED — PRIMARY TASK ARTIFACT`: exact triggering/source instruction is independently present in an original work order/charter/payload; A8/chronology still requires the interaction record.
- `A5 PRIMARY EXECUTION BEHAVIOR CORROBORATED`: a primary tool/session fragment independently proves the action/sequence recorded in A5, but does not contain enough A3/A8 prose to confirm the whole incident.
- `UNVERIFIED — PRIMARY BEHAVIOR FRAGMENT ONLY`: primary execution behavior/order is independently corroborated, but A3 and/or A8/full chronology are missing.
- `UNVERIFIED — SOURCE EXTRACT ONLY`: full derivative extraction record recovered, but no independently complete primary interaction.
- `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED`: preservation evidence indicates primary transcript material existed, but exact complete artifact is not yet mapped.
- `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED`: corpus names a historical extract that has not been recovered.
- `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE`: extensive current search did not locate sufficient source interaction/extract.
- `UNVERIFIED — SOURCE SEARCH PENDING`: discovery is still open.
- `CONTRADICTED`: reserved for a source check that materially disagrees with the corpus record.
- `CONFIRMED`: reserved for successful primary-interaction A3/A8/chronology verification.

## GPT — 5 records

Recovered `extract_chatgpt_w1_2026-07-30.md` maps exactly to GPT-001..005 and restores A4, but its own limitations report source-window truncation/compaction. It is derivative evidence.

| GID | Best source evidence | A3 | A8 | Chronology | C9 recommendation |
|---|---|---|---|---|---|
| GPT-001 | GPT source extract INC-001 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-002 | GPT source extract INC-002 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-003 | GPT source extract INC-003 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-004 | GPT source extract INC-004 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-005 | GPT source extract INC-005 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |

## AUD — 22 records

The exact historical KIVO-AUDITOR Claude Code session path is now known:

`/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`

The Library also contains a genuine bounded primary execution fragment extracted from that session: `PREFLIGHTKVD06REV14001_transcript.txt`, recorded as 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`, covering source-record line 1110 onward. It contains exact tool calls/results for the Revision-14 preflight but not the complete user/assistant prose of the 22-record source family.

Detailed mapping: `source-evidence/AUD_PRIMARY_FRAGMENT_MAPPING.md`.

| GID | Best current evidence | What is independently established | C9 recommendation |
|---|---|---|---|
| AUD-001 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-002 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-003 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-004 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-005 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-006 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-007 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-008 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-009 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-010 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-011 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-012 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-013 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-014 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-015 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-016 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-017 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-018 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-019 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-020 | primary preflight execution fragment | A5 behavior corroborated: existing functions/views were inspected; bounded call inventory contains no genuine PostgREST HTTP GET | `UNVERIFIED — PRIMARY BEHAVIOR FRAGMENT ONLY` |
| AUD-021 | primary preflight execution fragment | A5 sequence corroborated exactly: Statement 13 calls `auth.uid()`/`auth.role()` at 01:49:09.694Z; Statement 17 inspects their definitions at 01:50:44.339Z | `UNVERIFIED — PRIMARY BEHAVIOR FRAGMENT ONLY` |
| AUD-022 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |

### AUD-021 temporal-model clarification

The condensed v1 row stores `A6=NO` / resolution style `SILENT`, while A8 says the deviation was self-disclosed in the same reply. The primary execution record proves the interpretation was acted on before function-definition inspection. Therefore these facts can coexist temporally: silent resolution at the decision/action moment, followed by post-action disclosure in the same reply. The remaining missing primary prose is needed to verify the A3 prohibition and exact A8 self-disclosure, so C9 is still not confirmed.

## CDX — 5 records

CDX-005 names historical output `outputs/extract_codex_w1_2026-07-30.md`; that exact file has not yet been recovered despite targeted Git, Library, and materialized-archive searches.

| GID | C9 recommendation |
|---|---|
| CDX-001 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-002 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-003 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-004 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-005 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |

## W38 — 8 records

Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` were recovered from the preserved source archive. They independently corroborate the A3/source instruction for W38-001..006. They do not contain the complete assistant response/mismatch chronology.

| GID | Best source evidence | A3 status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| W38-001 | `WO_PROOF_3_SAFETY_REPRO.md` line 14 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-002 | `WO_PROOF_3_SAFETY_REPRO.md` line 33 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-003 | `WO_PROOF_3_SAFETY_REPRO.md` line 31 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-004 | `WO_PROOF_4_C04_DISPUTE.md` line 14 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-005 | `WO_PROOF_3_SAFETY_REPRO.md` line 52 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-006 | `WO_PROOF_3_SAFETY_REPRO.md` line 59 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-007 | no exact A3 source located in this pass | not corroborated | interaction not located | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-008 | no exact interaction/source mapping established | not corroborated | competence/comparison row | `UNVERIFIED — SOURCE SEARCH PENDING` |

## W39 — 7 records

Primary task artifacts independently corroborate four A3/source-content records. They do not establish the full incident chronology.

| GID | Best source evidence | A3/source status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| W39-001 | `FOUR_WINDOW_CHARTER.md` lines 105–109 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; governance context corroborated | interaction not located | `UNVERIFIED` |
| W39-002 | multiple E0 WOs exist but exact trigger not identified | A3 remains `NOT OBSERVABLE` | unresolved structural defect | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-003 | `WO_VERIFY_FIX_RPC_SHAPES.md` lines 8 and 64 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; conflicting "verify every argument" context also corroborated | interaction not located | `UNVERIFIED` |
| W39-004 | `WO_VERIFY_FIX_RPC_SHAPES.md` line 80 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | transport mismatch interaction not located | `UNVERIFIED` |
| W39-005 | exact bare-request source interaction not located | not corroborated | interaction not located | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-006 | exact three-item-only packet instruction not located | not corroborated | interaction not located | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-007 | `schema_contract_extract.sql` line 1; `RAW_CATALOG_APPENDIX.md` line 32 | supplied `-- B1. Function contracts` content corroborated | execution-authority chronology not located | `UNVERIFIED` |

## KBD — 4 records

Broad search across Git, July Library exports/writing blocks, Kivo handover archives and the recovered primary-task archive did not locate a sufficiently complete KIVO-BUILDER interaction or exact four-record extraction report.

| GID | C9 recommendation |
|---|---|
| KBD-001 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-002 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-003 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-004 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |

## KPF — 1 record

| GID | Best source evidence | A3/A12 status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| KPF-001 | `FOUR_WINDOW_CHARTER.md` lines 105 and 109 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; exact no-PR/no-merge A12 context corroborated | KIVO-PROOF interaction not located | `UNVERIFIED` |

## Current totals

- Corpus rows tracked: **52/52**
- Derivative source-extract mapped: **5/52** (GPT)
- Exact primary task-artifact A3/source-content corroboration: **11/52** (W38 6, W39 4, KPF 1)
- Primary execution behavior corroborated from bounded AUD transcript fragment: **2/52** (AUD-020, AUD-021)
- Primary interaction/transcript C9 `CONFIRMED`: **0/52**
- C9 `CONTRADICTED`: **0/52**

These are separate evidence categories and must not be summed into a "verified N" statistic.

Next source priority: recover the complete AUD session / `human_turns.txt` / 22-record extraction output; then recover the named CDX extraction file. If those remain unavailable after targeted recovery, preserve the limitation rather than infer confirmation.
