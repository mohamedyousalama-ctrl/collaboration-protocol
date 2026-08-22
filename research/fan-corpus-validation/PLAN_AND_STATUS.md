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
- [x] Pre-existing Base64 representation on `main` found incomplete/corrupt and preserved unchanged as evidence.
- [x] Original `files(3).zip` research bundle recovered from the user's file library.
- [x] Bundle SHA-256 `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8` verified against the repository source-bundle manifest.
- [x] Exact `CP_Incident_Database_v1.xlsx` recovered and verified at 31,471 bytes with historical SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.
- [x] Exact branch-only Base64 recovery representation stored under `research/fan-corpus-validation/recovered-source/`.
- [x] GitHub Actions independently reconstructed the binary and returned identity **PASS**: 41,964 Base64 characters, 31,471 bytes, exact expected SHA-256.
- [x] Workbook structural inventory and machine-readable 52-row audit input generated.

Verified workbook:

- `README` — A1:A16
- `Codebook` — A1:C15
- `Incidents` — A1:AD53
- `Aggregates` — A1:C13
- 52 incident records + one header row
- 30 incident columns
- all researcher-final fields `C0 FINAL` through `C10` blank across all 52 rows

Durable evidence:

- `research/fan-corpus-validation/RECOVERY_PROVENANCE_AND_FREEZE.md`
- `research/fan-corpus-validation/work/AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md`
- `research/fan-corpus-validation/work/CP_Incident_Database_v1.authoritative-v1.xlsx`
- `research/fan-corpus-validation/work/authoritative_v1_inventory.json`
- `research/fan-corpus-validation/work/incident_rows.tsv`
- `research/fan-corpus-validation/recovered-source/AUTHORITATIVE_V1_SHA256.txt`

## WP2 — Audit all 52 records

**Owner:** ChatGPT  
**Status:** COMPLETE — ALL 52 ROWS AUDITED

- [x] Confirm row count and seven-window allocation.
- [x] Check completeness of every extraction field actually stored in v1.
- [x] Complete row-by-row internal-consistency audit.
- [x] Flag competence/premise/meta records that must not automatically feed SII analysis.
- [x] Review recurrence/cross-window links.
- [x] Flag unsupported, contradictory, non-observable, or temporally ambiguous evidence.
- [x] Assign one WP2 disposition to every row.
- [x] Preserve C9 as unverified for every row pending WP3.

WP2 disposition counts:

- `PASS_TO_SOURCE_VERIFICATION` — **21**
- `NEEDS_SOURCE` — **11**
- `STRUCTURAL_DEFECT` — **2**
- `EXCLUDE_CANDIDATE` — **18**

`EXCLUDE_CANDIDATE` means exclude from the SII-analysis candidate set on present evidence, not delete from the corpus. Comparison and meta records remain preserved.

Major WP2 findings:

1. The protocol defines A1–A13, but v1 has no dedicated `A4 Possible interpretations` column.
2. The v1 aggregate `C0 FINAL=INTENT` + `A6=NO` is not a scientifically safe definition of silent inference because two `DISCLOSED-PROCEED` rows also have `A6=NO`.
3. `AUD-021` has an internal contradiction: `Resolution style=SILENT`, while A8/A11 say the deviation was self-detected and disclosed in the same reply.
4. `W39-002` lacks the required triggering quote: A3 explicitly records the original WO text as `NOT OBSERVABLE`.
5. `AUD-022` uses `ASKED/DISCLOSED`, outside the v1 Codebook's listed resolution-style vocabulary.
6. A9 is not metric-ready: integer turns are mixed with `N/O`, `N/A`, `NOT OBSERVABLE`, approximate cycles, and approximate exchanges.
7. Seven records show substantial A3/A8 textual overlap, creating a chronology risk that WP3 must resolve from primary evidence.
8. Suggested outcome has no separate researcher-final field in v1; publication outcome rates cannot rely on the suggested values without researcher validation.
9. One C0 suggestion uses non-final-codebook label `DEFINITION→INTENT` and must be normalized only as an assistant recommendation.

Durable WP2 outputs:

- `research/fan-corpus-validation/CORPUS_AUDIT_52.md`
- `research/fan-corpus-validation/corpus-audit/ROW_AUDIT_52.tsv`
- reproducible generator: `research/fan-corpus-validation/tools/wp2_audit.py`

## WP3 — Locate and verify seven source conversations

**Owner:** ChatGPT for discovery/quote checking  
**Status:** ACTIVE — NEXT WORK PACKAGE

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
- [ ] Search Git and preserved source bundles for exact source-extract/transcript artifacts for each family.
- [ ] Classify each family as `PRIMARY_TRANSCRIPT_FOUND`, `SOURCE_EXTRACT_ONLY`, `PARTIAL`, or `NOT_FOUND`.
- [ ] Map every incident to its best available source location.
- [ ] Verify A3 and A8 chronology/quotation where primary evidence exists.
- [ ] Recommend C9 evidence status only after verification.
- [ ] Produce explicit unresolved-source list; never infer a missing transcript from the workbook alone.

Deliverables:

- `SOURCE_CONVERSATION_AVAILABILITY.md`
- `QUOTE_VERIFICATION_REGISTER.md`

## WP4 — Classification recommendations

**Owner:** ChatGPT  
**Status:** WAITING FOR WP3 EVIDENCE

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
| 1 | Freeze/reconstruct v1 | **COMPLETE** |
| 2 | Audit all 52 | **COMPLETE — 52/52 audited** |
| 3 | Source conversations | **ACTIVE — NEXT** |
| 4 | Classification recommendations | WAITING FOR WP3 |
| 5 | Researcher decisions | WAITING |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | DRAFT PACKAGE CREATED |

## Update rule

Update this file after every material discovery, completed work package, evidence-status change, or blocker. GitHub Issue #3 mirrors high-level task state; this document remains the durable branch-level research handoff.
