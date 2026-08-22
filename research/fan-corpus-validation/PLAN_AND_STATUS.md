# Fan Corpus Validation — Plan and Status

**Workstream:** Naturalistic 52-record corpus validation and Fan Chen-Chieh methods exchange  
**Started:** 22 August 2026  
**Working branch:** `research/fan-corpus-validation-2026-08-22`  
**Base:** `main`

## Governing evidence rules

1. Preserve historical `CP_Incident_Database_v1.xlsx` evidence unchanged.
2. Never mark an incident quote `CONFIRMED` unless the primary source transcript is independently available and checked.
3. Assistant-generated Part-C classifications are recommendations only until Mohamed Salama makes the researcher decision.
4. Ground-truth intent (`C5`) can only be finalized by Mohamed Salama.
5. Do not force the final analyzable corpus to remain 52. Exclude or retain as unverified any record that fails evidence checks.
6. Preserve all limitations, contradictions, exclusions, source-access gaps, and recovery defects.

## WP1 — Freeze and reconstruct v1

**Status:** COMPLETE — AUTHORITATIVE V1 RECOVERED AND VERIFIED

Exact v1 identity: 31,471 bytes; SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.

The incomplete historical Git Base64 representation remains untouched. The exact workbook was recovered from `files(3).zip`, whose SHA-256 `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8` exactly matches the repository source-bundle manifest. GitHub Actions independently reconstructed and verified the recovered branch representation.

Durable evidence:
- `RECOVERY_PROVENANCE_AND_FREEZE.md`
- `work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `work/authoritative_v1_inventory.json`
- `work/incident_rows.tsv`
- `recovered-source/AUTHORITATIVE_V1_SHA256.txt`

## WP2 — Audit all 52 records

**Status:** COMPLETE — 52/52 AUDITED

Disposition counts:
- `PASS_TO_SOURCE_VERIFICATION` — **21**
- `NEEDS_SOURCE` — **11**
- `STRUCTURAL_DEFECT` — **2**
- `EXCLUDE_CANDIDATE` — **18**

`EXCLUDE_CANDIDATE` means exclude from the SII-analysis candidate set on present evidence, not delete from the corpus.

Major findings:
1. A4 Possible interpretations is absent as a dedicated workbook column.
2. The v1 A6-only silent-inference aggregate can miscount disclosed events as silent.
3. AUD-021 has a resolution-style contradiction.
4. W39-002 lacks the required observable triggering quote in v1.
5. AUD-022 uses a resolution-style label outside the listed Codebook values.
6. A9 awareness-gap values require normalization before statistics.
7. Seven records have substantial A3/A8 overlap and require source chronology review.
8. Suggested outcome lacks a separate researcher-final field.
9. One C0 suggestion uses non-final-codebook label `DEFINITION→INTENT`.

Durable outputs:
- `CORPUS_AUDIT_52.md`
- `corpus-audit/ROW_AUDIT_52.tsv`
- `tools/wp2_audit.py`

## WP3 — Locate and verify seven source conversations

**Status:** ACTIVE — NEXT WORK PACKAGE

Families: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1.

Current state:
- AUD: `PARTIAL` because the preserved research record says its raw transcript was recovered, but the exact primary artifact still must be located and mapped.
- GPT/CDX/W38/W39/KBD/KPF: primary transcript availability not yet proven.
- The exact `files(3).zip` research bundle does not by itself prove all seven transcripts are present.

Tasks:
- [x] Create source-availability matrix.
- [ ] Search Git and preserved source bundles for exact transcript/source-extract artifacts.
- [ ] Classify each family as `PRIMARY_TRANSCRIPT_FOUND`, `SOURCE_EXTRACT_ONLY`, `PARTIAL`, or `NOT_FOUND`.
- [ ] Map every incident to its best source location.
- [ ] Verify A3/A8 chronology and quotations where primary evidence exists.
- [ ] Recommend C9 status only after primary-source checks.

Deliverables:
- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`

## WP4 — Classification recommendations

**Status:** WAITING FOR WP3 EVIDENCE

ChatGPT prepares recommendations only for C0, C1, C2, C3, C4, C6, C7, C8, C9, C10. C5 TRUE INTENT remains exclusively Mohamed's researcher decision.

## WP5 — Researcher decisions

**Owner:** Mohamed Salama  
**Status:** WAITING FOR WP4

## WP6 — Independent quality check

**Status:** DEFERRED BY FOUNDER

## WP7 — Freeze v1.1

**Status:** BLOCKED UNTIL WP5 AND LATER QC

## WP8 — Fan exchange package

**Status:** DRAFT PACKAGE CREATED; FINAL NUMBERS/EXAMPLES WAIT ON VALIDATION

Created under `fan-exchange/`:
- `00_READ_ME_FIRST.md`
- `01_METHODS_NOTE.md`
- `02_SCHEMA_AND_CODEBOOK.md`
- `03_DCM2_CROSSWALK_TEMPLATE.md`
- `04_SANITIZED_EXAMPLES.md`
- `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

## Current status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | **COMPLETE** |
| 2 | Audit all 52 | **COMPLETE — 52/52** |
| 3 | Source conversations | **ACTIVE — NEXT** |
| 4 | Classification recommendations | WAITING FOR WP3 |
| 5 | Researcher decisions | WAITING |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | DRAFT CREATED |

## Update rule

Update this file after every material discovery, completed work package, evidence-status change, or blocker. GitHub Issue #3 mirrors high-level state; this file remains the durable branch-level research handoff.
