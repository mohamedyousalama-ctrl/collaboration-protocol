# Primary Task Artifact Evidence Index

**WP:** 3 — source discovery and verification  
**Branch:** `research/fan-corpus-validation-2026-08-22`

## Evidence class and boundary

This register records **primary task artifacts**: original work orders, window charters, SQL payloads, and other instructions that were actually supplied to the execution windows.

A primary task artifact can independently corroborate an A3 instruction or prior-context statement. It is stronger than a later summary or extraction report for that limited purpose.

It does **not**, by itself, satisfy C9 `CONFIRMED` for an incident because C9 requires the incident quotation and chronology to be checked against the source interaction. In most cases the task artifact does not contain the model's chosen interpretation, the later mismatch signal A8, or the complete turn order.

Therefore the rule for this workstream is:

- task artifact exact match -> `A3 CORROBORATED`;
- complete primary transcript/source interaction -> eligible for A3/A8/chronology verification;
- no C9 upgrade from task-artifact agreement alone.

## Recovery provenance

A preserved Library archive named `all.zip` was inspected during WP3.

- size: **803,462 bytes**
- SHA-256: `d045661795fe195baebd53693ad94c4f1db5cf67cc31ebeee90803d305cad1ad`

The archive contains original Kivo work-order/source artifacts relevant to W38, W39 and KPF, including:

- `FOUR_WINDOW_CHARTER.md`
- `WO_PROOF_3_SAFETY_REPRO.md`
- `WO_PROOF_4_C04_DISPUTE.md`
- `WO_VERIFY_FIX_RPC_SHAPES.md`
- `WO_VERIFY_FIX_2_FIVE_CORRECTIONS.md`
- `schema_contract_extract.sql`
- `RAW_CATALOG_APPENDIX.md`

The archive is used only as provenance/source evidence. It is not being treated as a replacement for the missing conversation transcripts.

## Exact A3 / context mappings

### W38

| GID | Primary artifact | Artifact location | Evidence result | C9 effect |
|---|---|---|---|---|
| W38-001 | `WO_PROOF_3_SAFETY_REPRO.md` | line 14 | Exact standing rebase/push rule and the four-stale-base prior-context sentence are present. | A3/context corroborated; C9 remains unverified. |
| W38-002 | `WO_PROOF_3_SAFETY_REPRO.md` | line 33 | Exact instruction to reproduce all three as failing tests and not fix them is present. | A3 corroborated; C9 remains unverified. |
| W38-003 | `WO_PROOF_3_SAFETY_REPRO.md` | line 31 | Exact C-04 statement about a disclosure inside a coalesced burst with `inbound_coalescing` on is present. | A3 corroborated; C9 remains unverified. |
| W38-004 | `WO_PROOF_4_C04_DISPUTE.md` | line 14 | Exact instruction that this work order tests the seven cases named by the auditor is present. | A3 corroborated; C9 remains unverified. |
| W38-005 | `WO_PROOF_3_SAFETY_REPRO.md` | line 52 | Exact shared flag-vector fixture instruction, including "mirrors the real tenant exactly", is present. | A3 corroborated; C9 remains unverified. |
| W38-006 | `WO_PROOF_3_SAFETY_REPRO.md` | line 59 | Exact defect-assertion instruction is present. | A3 corroborated; C9 remains unverified. |
| W38-007 | — | — | Exact A3 wording about the auditor requiring a capture timestamp and hash was not located in this archive pass. | No upgrade. |
| W38-008 | — | — | No exact mapping established in this archive pass; current WP2 class is competence/comparison evidence. | No upgrade. |

### W39

| GID | Primary artifact | Artifact location | Evidence result | C9 effect |
|---|---|---|---|---|
| W39-001 | `FOUR_WINDOW_CHARTER.md` | lines 105–109 | Exact rebase-immediately-before-every-push rule is present, together with zero-deletion/stop-before-push governance and the no-PR/no-merge rule. | A3/context corroborated; C9 remains unverified. |
| W39-002 | several E0 work-order files exist | — | The exact triggering E0 instruction represented by this row has not been identified. The v1 A3 remains `NOT OBSERVABLE`. | Structural defect remains unresolved. |
| W39-003 | `WO_VERIFY_FIX_RPC_SHAPES.md` | lines 8 and 64 | Exact "not a design task / six call sites / correct only those / add nothing" instruction is present; the same artifact also contains the conflicting "verify every argument" instruction. | A3 and conflicting-context evidence corroborated; C9 remains unverified. |
| W39-004 | `WO_VERIFY_FIX_RPC_SHAPES.md` | line 80 | Exact required deliverable "The complete corrected file" is present. | A3 corroborated; C9 remains unverified. |
| W39-005 | — | — | Exact `My request for Codex:` source interaction not located. | No upgrade. |
| W39-006 | — | — | Exact three-item-only PM packet instruction not located in this archive pass. | No upgrade. |
| W39-007 | `schema_contract_extract.sql`; `RAW_CATALOG_APPENDIX.md` | SQL line 1 / appendix line 32 | Exact supplied content begins `-- B1. Function contracts`. This corroborates the content that was supplied, but not whether supplying it authorized production execution. | A3 content corroborated; authority/chronology still requires transcript; C9 unverified. |

### KPF

| GID | Primary artifact | Artifact location | Evidence result | C9 effect |
|---|---|---|---|---|
| KPF-001 | `FOUR_WINDOW_CHARTER.md` | lines 105 and 109 | Exact rebase-before-every-push rule is present, and exact prior-context governance "Never open a pull request and never merge. Push your branch only." is present. | A3/A12 corroborated; C9 remains unverified. |

## Counts after this pass

- Corpus rows with exact primary-task-artifact corroboration added in this pass: **11/52**.
  - W38: **6**
  - W39: **4**
  - KPF: **1**
- GPT derivative source-extract mapped from the earlier WP3 pass: **5/52**.
- Primary conversation/transcript C9 `CONFIRMED`: **0/52**.

These categories are deliberately not added together as a "verified" count: task-artifact corroboration and derivative extraction are different evidence classes and neither automatically establishes the complete incident chronology.
