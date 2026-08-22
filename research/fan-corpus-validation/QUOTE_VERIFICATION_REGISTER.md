# Quote and Chronology Verification Register

**WP:** 3 — source discovery and primary-evidence verification  
**Rule:** `CONFIRMED` requires independent primary conversation evidence. A workbook row or derivative extraction report cannot by itself satisfy C9.

## Status vocabulary

- `UNVERIFIED — SOURCE EXTRACT ONLY`: full extraction record recovered, but no independent primary transcript yet.
- `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED`: preservation evidence indicates primary material existed, but exact artifact is not yet mapped.
- `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED`: corpus names a historical extraction file that has not yet been recovered.
- `UNVERIFIED — SOURCE SEARCH PENDING`: no sufficient transcript/extract recovered yet.
- `CONTRADICTED`: reserved for a later source check that materially disagrees with the corpus record.
- `CONFIRMED`: reserved for successful primary-source A3/A8/chronology verification.

## GPT — 5 records

Best available evidence: recovered `extract_chatgpt_w1_2026-07-30.md`, mapped exactly to GPT-001..005. The extract includes A4 but explicitly states underlying transcript limitations/compaction. It is not independent primary evidence.

| GID | Best source evidence | A3 | A8 | Chronology | C9 recommendation |
|---|---|---|---|---|---|
| GPT-001 | GPT source extract INC-001 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-002 | GPT source extract INC-002 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-003 | GPT source extract INC-003 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-004 | GPT source extract INC-004 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |
| GPT-005 | GPT source extract INC-005 | present in extract | present in extract | derivative only | `UNVERIFIED — SOURCE EXTRACT ONLY` |

## AUD — 22 records

Best available evidence: preservation record and AUD-018 say a raw transcript was recovered from disk; exact independently readable transcript artifact has not yet been located/mapped in this WP3 pass.

| GID | C9 recommendation |
|---|---|
| AUD-001 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-002 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-003 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-004 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-005 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-006 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-007 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-008 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-009 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-010 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-011 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-012 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-013 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-014 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-015 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-016 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-017 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-018 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-019 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-020 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |
| AUD-021 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED`; structural contradiction must be resolved from source |
| AUD-022 | `UNVERIFIED — PRIMARY ARTIFACT NOT YET LOCATED` |

## CDX — 5 records

CDX-005 names historical output `outputs/extract_codex_w1_2026-07-30.md`; that exact file has not yet been recovered.

| GID | C9 recommendation |
|---|---|
| CDX-001 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-002 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-003 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-004 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |
| CDX-005 | `UNVERIFIED — EXTRACT REFERENCED NOT LOCATED` |

## W38 — 8 records

| GID | C9 recommendation |
|---|---|
| W38-001 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-002 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-003 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-004 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-005 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-006 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-007 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W38-008 | `UNVERIFIED — SOURCE SEARCH PENDING` |

## W39 — 7 records

| GID | C9 recommendation |
|---|---|
| W39-001 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-002 | `UNVERIFIED — SOURCE SEARCH PENDING`; A3 trigger is explicitly `NOT OBSERVABLE` in v1 |
| W39-003 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-004 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-005 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-006 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| W39-007 | `UNVERIFIED — SOURCE SEARCH PENDING` |

## KBD — 4 records

| GID | C9 recommendation |
|---|---|
| KBD-001 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| KBD-002 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| KBD-003 | `UNVERIFIED — SOURCE SEARCH PENDING` |
| KBD-004 | `UNVERIFIED — SOURCE SEARCH PENDING` |

## KPF — 1 record

| GID | C9 recommendation |
|---|---|
| KPF-001 | `UNVERIFIED — SOURCE SEARCH PENDING` |

## Current totals

- Corpus rows tracked: **52/52**
- Source-extract mapped: **5/52** (GPT)
- Primary-transcript C9 `CONFIRMED`: **0/52**
- C9 `CONTRADICTED`: **0/52**
- Every row remains explicitly unverified until primary evidence changes that state.

This register must be updated record-by-record when new source evidence is located. It must never infer confirmation from agreement between two copies of the same derivative extract.
