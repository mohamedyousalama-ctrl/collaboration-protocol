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

**Owner:** ChatGPT  
**Status:** COMPLETE — AUTHORITATIVE V1 RECOVERED AND VERIFIED

- [x] Historical workbook identity established: SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`, 31,471 bytes.
- [x] Discovered that the pre-existing Base64 representation on `main` is incomplete/corrupt: 35,408 Base64 chars → 26,554 bytes → SHA-256 `f75db1ce4037adfba3d749302e7a031bc9ec1e54a84a7b25153bb7668676113a`; not a complete XLSX.
- [x] Preserved that defect; no historical `main` evidence was rewritten.
- [x] Located original `files(3).zip` research bundle in the user's file library.
- [x] Verified bundle SHA-256 `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8`, exactly matching the repository source-bundle manifest.
- [x] Recovered `CP_Incident_Database_v1.xlsx` from that bundle.
- [x] Verified exact workbook size 31,471 bytes and exact historical SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.
- [x] Stored an exact branch-only Base64 recovery representation under `research/fan-corpus-validation/recovered-source/`.
- [x] GitHub Actions reconstructed the exact binary and independently returned identity **PASS**: 41,964 Base64 chars, 31,471 bytes, declared SHA-256 match.
- [x] Workbook structural inventory generated.
- [x] Machine-readable 52-row audit export generated.

Verified workbook:

- `README` — A1:A16
- `Codebook` — A1:C15
- `Incidents` — A1:AD53
- `Aggregates` — A1:C13
- 52 incident records + header
- 30 incident columns
- all researcher-final fields `C0 FINAL` through `C10` blank across all 52 rows

Durable evidence:

- `research/fan-corpus-validation/RECOVERY_PROVENANCE_AND_FREEZE.md`
- `research/fan-corpus-validation/work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `research/fan-corpus-validation/work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `research/fan-corpus-validation/work/authoritative_v1_inventory.json`
- `research/fan-corpus-validation/work/incident_rows.tsv`
- `research/fan-corpus-validation/recovered-source/AUTHORITATIVE_V1_SHA256.txt`

### WP1 findings carried into audit

- The protocol defines A1–A13 but v1 has no dedicated `A4 Possible interpretations` column. The workbook README says extraction content was condensed and full text lives in source extract files.
- The aggregate formula `Silent (A6=NO) among INTENT` can count `DISCLOSED-PROCEED` rows as silent because two disclosed rows have `A6=NO`. Historical v1 remains unchanged; this requires a corrected analytical rule in v1.1/methods.

## WP2 — Audit all 52 records

**Owner:** ChatGPT  
**Status:** IN PROGRESS — WORKING COPY VERIFIED

For every record:

- [x] Confirm row exists and source-window allocation reconciles to 52.
- [x] Check completeness of every field actually stored in the v1 extraction section.
- [ ] Complete row-by-row internal-consistency audit.
- [ ] Flag competence/premise/meta records that must not automatically feed SII analysis.
- [ ] Flag duplicate/cross-window recurrence.
- [ ] Flag unsupported, contradictory, non-observable, or temporally ambiguous evidence.
- [ ] Assign one WP2 disposition per row: `PASS_TO_SOURCE_VERIFICATION`, `NEEDS_SOURCE`, `STRUCTURAL_DEFECT`, or `EXCLUDE_CANDIDATE`.

Already established structurally:

- window counts reconcile exactly: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1;
- all 52 rows populate every extraction field that v1 actually stores (`A1,A2,A3,A5,A6,A7,A8,A9,A10,A11,A12,A13`);
- A4 is absent at workbook-schema level rather than blank per row;
- all 52 researcher-final classifications are still blank;
- suggested triage only: 33 INTENT, 8 COMPETENCE, 6 PREMISE, 4 META, 1 `DEFINITION→INTENT`;
- suggested outcome only: 31 HARMFUL, 20 BENIGN, 1 UNRESOLVED;
- A6: 51 NO, 1 N/A;
- resolution style: 49 SILENT, 2 DISCLOSED-PROCEED, 1 `ASKED/DISCLOSED`;
- confidence: 24 HIGH, 15 MEDIUM, 13 LOW.

Planned deliverables:

- `CORPUS_AUDIT_52.md`
- `corpus-audit/ROW_AUDIT_52.tsv`

## WP3 — Locate and verify seven source conversations

**Owner:** ChatGPT for discovery/quote checking  
**Status:** DISCOVERY STARTED

Known source-window families:

- GPT — 5
- AUD — 22
- CDX — 5
- W38 — 8
- W39 — 7
- KBD — 4
- KPF — 1

Current evidence:

- the Master Knowledge File explicitly says the AUD raw transcript was recovered from disk for verbatim checking;
- the workbook README says full text lives in source extract files;
- the authoritative `files(3).zip` research bundle contains the workbook/protocol/research documents but does not by itself prove all seven complete primary transcripts are present;
- current Git search has not yet established complete independently readable primary transcripts for all seven families.

Tasks:

- [x] Create source-availability matrix.
- [ ] Locate exact primary transcript/source-extract artifact(s) for each family.
- [ ] Map every incident to source location.
- [ ] Verify A3 and A8 against primary source.
- [ ] Recommend C9 evidence status only after verification.

Deliverables:

- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`

## WP4 — Classification recommendations

**Owner:** ChatGPT  
**Status:** WAITING FOR WP2 ROW AUDIT; MAY PROCEED BEFORE FULL WP3 WHERE CLEARLY LABELLED UNVERIFIED

Recommendation fields only:

- C0 incident class
- C1 IPP type
- C2 materiality
- C3 Context Factor
- C4 effective ICD
- C6 cost evidence/range
- C7 hypothesis relevance
- C8 benchmark candidacy
- C9 verification recommendation from WP3 evidence
- C10 notes

`C5 TRUE INTENT` remains a question for Mohamed and will not be filled as fact by the assistant.

## WP5 — Researcher decisions

**Owner:** Mohamed Salama  
**Status:** WAITING FOR WP4

Mohamed confirms/corrects the evidence cards and supplies C5 ground-truth intent. Assistant recommendations do not become researcher ground truth merely by being written.

## WP6 — Independent quality check

**Status:** DEFERRED BY FOUNDER UNTIL AFTER RESEARCHER DECISIONS

## WP7 — Freeze v1.1

**Status:** BLOCKED UNTIL WP5 AND LATER QC

Historical v1 will remain immutable. v1.1 will contain only the later researcher-reviewed/quality-checked state plus provenance, inclusion/exclusion ledger, and corrected analytical rules.

## WP8 — Fan exchange package

**Owner:** ChatGPT  
**Status:** DRAFT PACKAGE CREATED; FINAL NUMBERS/EXAMPLES WAIT ON VALIDATION

Created under `research/fan-corpus-validation/fan-exchange/`:

- [x] `00_READ_ME_FIRST.md`
- [x] `01_METHODS_NOTE.md`
- [x] `02_SCHEMA_AND_CODEBOOK.md`
- [x] `03_DCM2_CROSSWALK_TEMPLATE.md`
- [x] `04_SANITIZED_EXAMPLES.md`
- [x] `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

The raw 52-row corpus will not be represented to Fan as fully human-validated unless WP3–WP5 establish that status.

## Current status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | **COMPLETE — exact identity verified** |
| 2 | Audit all 52 | **IN PROGRESS** |
| 3 | Source conversations | DISCOVERY STARTED |
| 4 | Classification recommendations | WAITING FOR WP2 |
| 5 | Researcher decisions | WAITING |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | DRAFT PACKAGE CREATED |

## Update rule

Update this file after every material discovery, completed work package, evidence-status change, or blocker. GitHub Issue #3 mirrors high-level task state; this document remains the durable branch-level research handoff.
