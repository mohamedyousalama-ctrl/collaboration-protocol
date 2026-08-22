# Quote and Chronology Verification Register

**WP:** 3 — source discovery and primary-evidence verification  
**Autonomous recovery state:** COMPLETE FOR CURRENT PRESERVATION SCOPE — further improvement requires newly supplied/recovered primary source material.  
**Rule:** C9 `CONFIRMED` requires independently available primary interaction evidence sufficient to check the incident quotation and chronology. A workbook row, derivative extraction report, original task artifact, execution-only fragment, or preserved assistant handback alone cannot automatically satisfy C9.

## Evidence/status vocabulary

- `A3 CORROBORATED — PRIMARY TASK ARTIFACT`: exact triggering/source instruction is independently present in an original work order/charter/payload; A8/chronology still requires the interaction record.
- `A5 PRIMARY EXECUTION BEHAVIOR CORROBORATED`: a primary tool/session fragment independently proves the action/sequence recorded in A5, but does not contain enough user-side source evidence to confirm the whole incident.
- `A8 INTERACTION-OUTPUT CORROBORATED`: a preserved assistant handback independently reproduces the relevant disclosure/mismatch output, but the user-side A3 source remains missing.
- `UNVERIFIED — SOURCE EXTRACT ONLY`: full derivative extraction record recovered, but no independently complete primary interaction.
- `UNVERIFIED — A3 PRIMARY USER PROMPT NOT LOCATED`: primary behavior/output evidence exists, but the user-side source instruction required for full verification has not been recovered.
- `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED`: preservation evidence indicates source material existed, but the complete incident source is not available in the current preservation scope.
- `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED`: corpus names a historical extract that has not been recovered.
- `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE`: targeted Git/Library/archive search did not locate sufficient source interaction/extract; future recovery remains possible.
- `CONTRADICTED`: primary source materially disagrees with the corpus record.
- `CONFIRMED`: primary interaction sufficiently verifies the relevant A3/A8/chronology.

## GPT — 5 records

Recovered `extract_chatgpt_w1_2026-07-30.md` maps exactly to GPT-001..005 and restores A4, but its own limitations report source-window truncation/compaction. It is derivative evidence.

| GID | Best source evidence | A3 | A8 | Chronology | C9 recommendation |
|---|---|---|---|---|---|
| GPT-001 | GPT source extract INC-001 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-002 | GPT source extract INC-002 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-003 | GPT source extract INC-003 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-004 | GPT source extract INC-004 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-005 | GPT source extract INC-005 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |

Targeted search did not recover an independently readable primary GPT transcript in the current preservation scope.

## AUD — 22 records

Historical primary session identity:

`/root/.claude/projects/-home-user-MaitreAI/84dd6879-90b4-5ba3-b9ad-b3ed61f10a6c.jsonl`

Recovered bounded primary execution evidence: `PREFLIGHTKVD06REV14001_transcript.txt`, 32,645 bytes / 482 lines / SHA-256 `771d0f013492e1c2eb9ce63617082f69f330c3f0d14520e4b1d57a5e323c7de4`, extracted from source-record line 1110 onward. A preserved Library assistant handback also reproduces the preflight explanation/disclosure relevant to AUD-020/021. Neither source contains the missing user-side A3 work-order text.

Detailed mapping: `source-evidence/AUD_PRIMARY_FRAGMENT_MAPPING.md`.

| GID | Best current evidence | What is independently established | C9 recommendation |
|---|---|---|---|
| AUD-001 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-002 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-003 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-004 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-005 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-006 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-007 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-008 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-009 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-010 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-011 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-012 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-013 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-014 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-015 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-016 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-017 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-018 | historical path plus record that later extraction used recovered raw turns | existence of extraction workflow corroborated; exact source file unavailable | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-019 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |
| AUD-020 | primary preflight execution fragment + preserved assistant handback | A5 behavior and VP-1 BLOCKED outcome corroborated; no genuine PostgREST GET observed; user-side A3 not recovered | `UNVERIFIED — A3 PRIMARY USER PROMPT NOT LOCATED` |
| AUD-021 | primary preflight execution fragment + preserved assistant handback | A5 call-before-inspection sequence corroborated exactly; A8 self-disclosure substance corroborated; user-side A3 not recovered | `UNVERIFIED — A3 PRIMARY USER PROMPT NOT LOCATED` |
| AUD-022 | historical full-source existence/path evidence only | complete incident source not mapped | `UNVERIFIED — PRIMARY ARTIFACT NOT LOCATED` |

### AUD-021 temporal-model clarification

The condensed v1 row stores `A6=NO` / resolution style `SILENT`, while A8 says the deviation was self-disclosed in the same reply. Primary execution evidence proves the interpretation was acted on before function-definition inspection; the preserved assistant handback then discloses the sequence deviation. These can coexist temporally: silent resolution at the action moment followed by same-reply post-action disclosure. The missing primary A3 message prevents C9 confirmation.

Targeted search did not recover the full JSONL, `human_turns.txt`, or a standalone 22-record AUD extraction artifact in the current preservation scope.

## CDX — 5 records

CDX-005 names historical output `outputs/extract_codex_w1_2026-07-30.md`. Targeted Git code search, Library/conversation search, and preserved-archive search did not recover that file or a sufficiently complete underlying Codex interaction.

| GID | C9 recommendation |
|---|---|
| CDX-001 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-002 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-003 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-004 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-005 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |

## W38 — 8 records

Original `WO_PROOF_3_SAFETY_REPRO.md` and `WO_PROOF_4_C04_DISPUTE.md` independently corroborate A3/source instructions for W38-001..006. Targeted distinctive-string searches did not recover the missing interaction chronology.

| GID | Best source evidence | A3 status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| W38-001 | `WO_PROOF_3_SAFETY_REPRO.md` line 14 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-002 | `WO_PROOF_3_SAFETY_REPRO.md` line 33 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-003 | `WO_PROOF_3_SAFETY_REPRO.md` line 31 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-004 | `WO_PROOF_4_C04_DISPUTE.md` line 14 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-005 | `WO_PROOF_3_SAFETY_REPRO.md` line 52 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-006 | `WO_PROOF_3_SAFETY_REPRO.md` line 59 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | interaction not located | `UNVERIFIED` |
| W38-007 | workbook/derived evidence only | exact primary interaction not located | interaction not located | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| W38-008 | workbook/derived evidence only | exact primary interaction not located | competence/comparison row | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |

## W39 — 7 records

Primary task artifacts independently corroborate four A3/source-content records. Targeted searches did not recover the missing interaction chronology or the exact source for the structurally defective W39-002 row.

| GID | Best source evidence | A3/source status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| W39-001 | `FOUR_WINDOW_CHARTER.md` lines 105–109 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; governance context corroborated | interaction not located | `UNVERIFIED` |
| W39-002 | multiple E0 WOs but no exact trigger | A3 remains `NOT OBSERVABLE` | unresolved structural defect | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| W39-003 | `WO_VERIFY_FIX_RPC_SHAPES.md` lines 8 and 64 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; conflicting `verify every argument` context also corroborated | interaction not located | `UNVERIFIED` |
| W39-004 | `WO_VERIFY_FIX_RPC_SHAPES.md` line 80 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT` | transport mismatch interaction not located | `UNVERIFIED` |
| W39-005 | workbook/derived evidence only | exact bare-request source not located | interaction not located | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| W39-006 | workbook/derived evidence only | exact three-item-only source interaction not located | interaction not located | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| W39-007 | `schema_contract_extract.sql` line 1; `RAW_CATALOG_APPENDIX.md` line 32 | supplied `-- B1. Function contracts` content corroborated | execution-authority chronology not located | `UNVERIFIED` |

## KBD — 4 records

Broad and final targeted search across Git, Library writing blocks/text exports, Kivo handover archives and the recovered primary-task archive did not locate a sufficiently complete KIVO-BUILDER interaction or exact four-record extraction report.

| GID | C9 recommendation |
|---|---|
| KBD-001 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-002 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-003 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |
| KBD-004 | `UNVERIFIED — NOT FOUND IN CURRENT PRESERVATION SCOPE` |

## KPF — 1 record

`FOUR_WINDOW_CHARTER.md` corroborates the exact rebase-before-push A3 rule and no-PR/no-merge A12 governance. Distinctive-string search did not recover the KIVO-PROOF interaction containing the A8 stale-base warning.

| GID | Best source evidence | A3/A12 status | A8/chronology | C9 recommendation |
|---|---|---|---|---|
| KPF-001 | `FOUR_WINDOW_CHARTER.md` lines 105 and 109 | `A3 CORROBORATED — PRIMARY TASK ARTIFACT`; no-PR/no-merge context corroborated | primary interaction not located | `UNVERIFIED` |

## Current totals

- Corpus rows tracked: **52/52**
- Derivative source-extract mapped: **5/52** (GPT)
- Exact primary task-artifact A3/source-content corroboration: **11/52** (W38 6, W39 4, KPF 1)
- Primary AUD execution behavior/output corroboration: **2/52** (AUD-020, AUD-021)
- Of those, A8 interaction-output corroborated: **1/52** (AUD-021)
- Primary interaction C9 `CONFIRMED`: **0/52**
- C9 `CONTRADICTED`: **0/52**

These are separate evidence classes and must not be summed into a `verified N` statistic.

## Terminal autonomous-recovery rule

The current autonomous recovery pass is complete. `NOT FOUND IN CURRENT PRESERVATION SCOPE` is an evidence-access statement, not an assertion of historical nonexistence. A future C9 upgrade requires newly recovered/supplied primary provider exports, source conversation files, or equivalent primary interaction records. Until then, the affected rows remain explicitly unverified.
