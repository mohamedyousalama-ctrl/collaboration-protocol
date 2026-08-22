# Fan Corpus Validation — Plan and Status

**Workstream:** Naturalistic 52-record corpus validation and Fan Chen-Chieh methods exchange
**Started:** 22 August 2026
**Working branch:** `research/fan-corpus-validation-2026-08-22`
**Base:** `main`

## Governing evidence rules

1. Preserve the historical `CP_Incident_Database_v1.xlsx` representation unchanged.
2. Never mark an incident quote `CONFIRMED` unless the source transcript is independently available and checked.
3. Assistant-generated Part-C classifications are recommendations only until Mohamed Salama makes the researcher decision.
4. Ground-truth intent (`C5`) can only be finalized by Mohamed Salama.
5. Do not force the final analyzable corpus to remain 52. Exclude or retain as unverified any record that fails evidence checks.
6. Preserve all limitations, contradictions, exclusions, and source-access gaps.

## Work packages

### WP1 — Freeze and reconstruct v1
**Owner:** ChatGPT
**Status:** IN PROGRESS

- [x] Confirm authoritative source-workbook SHA-256 in preservation record: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.
- [x] Confirm reconstructible Base64 representation is present on `main` as five ordered parts plus reconstruction instructions.
- [ ] Reconstruct workbook into a working copy without altering the historical Base64 source.
- [ ] Verify decoded byte size and SHA-256 against the preservation record.
- [ ] Record workbook sheet inventory, row count, field inventory, formula inventory, and blank researcher fields.
- [ ] Produce a machine-readable audit export for the 52 incident rows.

### WP2 — Audit all 52 records
**Owner:** ChatGPT
**Status:** NOT STARTED

For every record:
- [ ] Check A1–A13 completeness.
- [ ] Check internal consistency between A3/A4/A5/A6/A7/A8/A9/A10/A11/A12/A13.
- [ ] Flag likely competence/premise/meta cases that should not automatically count as SII.
- [ ] Flag duplicate or cross-window recurring incidents.
- [ ] Flag unsupported or internally contradictory claims.
- [ ] Assign an audit disposition: `PASS_TO_SOURCE_VERIFICATION`, `NEEDS_SOURCE`, `STRUCTURAL_DEFECT`, or `EXCLUDE_CANDIDATE`.

Deliverable: `CORPUS_AUDIT_52.md` plus row-level audit table.

### WP3 — Locate and verify seven source conversations
**Owner:** ChatGPT for source discovery and quote checking
**Status:** PARTIALLY AVAILABLE / DISCOVERY REQUIRED

Known source-window families from the preserved research record:
- GPT — 5 records
- AUD — 22 records
- CDX — 5 records
- W38 — 8 records
- W39 — 7 records
- KBD — 4 records
- KPF — 1 record

Current repository evidence:
- The preserved Master Knowledge File explicitly states that the **AUD raw transcript was recovered from disk for verbatim checking**.
- The repository preserves the 52-row workbook and extraction protocol.
- A current tree/code search has **not yet established that all seven complete original source conversations are present as independently readable transcript artifacts in Git**.

Therefore no claim will be made that all seven are available until each source family is individually located and mapped.

Tasks:
- [ ] Build a source-availability matrix for GPT/AUD/CDX/W38/W39/KBD/KPF.
- [ ] Locate the exact primary transcript artifact(s) for each family, if present.
- [ ] Map every incident to source location.
- [ ] Verify A3 and A8 verbatim quotes against source.
- [ ] Set evidence recommendation: `CONFIRMABLE`, `UNVERIFIED_SOURCE_MISSING`, or `CONTRADICTED`.

Deliverable: `SOURCE_CONVERSATION_AVAILABILITY.md` and `QUOTE_VERIFICATION_REGISTER.md`.

### WP4 — Classification recommendations
**Owner:** ChatGPT
**Status:** NOT STARTED

For each record that survives WP2, prepare recommendation only for:
- C0 incident class where applicable (INTENT / COMPETENCE / PREMISE / MIXED / META)
- C1 IPP type
- C2 materiality
- C3 Context Factor
- C4 effective ICD
- C6 cost estimate/range based only on evidence
- C7 hypothesis relevance
- C8 benchmark candidacy
- C9 verification recommendation based on WP3
- C10 notes

`C5 TRUE INTENT` will be presented as a question for Mohamed, not filled as fact by the assistant.

Deliverable: `CLASSIFICATION_RECOMMENDATIONS.md` and researcher review cards.

### WP5 — Researcher decisions
**Owner:** Mohamed Salama
**Status:** WAITING FOR WP4

Mohamed reviews the compact evidence cards and confirms/corrects:
- final incident class;
- final IPP classification;
- materiality;
- ground-truth intent (C5);
- any disputed recommendation.

No assistant recommendation becomes researcher ground truth merely by being written into this branch.

### WP6 — Independent quality check
**Owner:** Later independent review
**Status:** DEFERRED BY FOUNDER

Will occur after researcher decisions are complete.

### WP7 — Freeze v1.1
**Owner:** ChatGPT after WP5/WP6 authorization
**Status:** BLOCKED

Planned outputs:
- frozen v1.1 validated dataset;
- method/version note;
- inclusion/exclusion ledger;
- source and checksum record;
- no mutation of historical v1 evidence.

### WP8 — Fan exchange package
**Owner:** ChatGPT
**Status:** PREPARE IN PARALLEL; FINALIZE AFTER WP2/WP3 STATUS IS KNOWN

Package should explain, without overclaiming:
1. research question and corpus origin;
2. seven source-window families and sampling nature;
3. LLM-assisted neutral extraction procedure;
4. A1–A13 extraction schema;
5. researcher-only classification framework;
6. competence-vs-intent filtering rule;
7. transcript/quote verification procedure;
8. current corpus status and limitations;
9. sanitized example records;
10. data-level crosswalk questions for comparison with DCM 2.0 Field & Technical Notes.

Planned files under `research/fan-corpus-validation/fan-exchange/`:
- `00_READ_ME_FIRST.md`
- `01_METHODS_NOTE.md`
- `02_SCHEMA_AND_CODEBOOK.md`
- `03_DCM2_CROSSWALK_TEMPLATE.md`
- `04_SANITIZED_EXAMPLES.md`
- `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

The raw 52-row corpus will not be represented to Fan as fully human-validated unless WP3–WP5 actually establish that status.

## Status summary

| WP | Work | Status |
|---|---|---|
| 1 | Freeze/reconstruct v1 | IN PROGRESS |
| 2 | Audit 52 | NOT STARTED |
| 3 | Source conversations | PARTIAL / DISCOVERY REQUIRED |
| 4 | Classification recommendations | NOT STARTED |
| 5 | Researcher decisions | WAITING |
| 6 | Independent QC | DEFERRED |
| 7 | Freeze v1.1 | BLOCKED |
| 8 | Fan methods exchange | PREPARE IN PARALLEL |

## Update rule

This file is the branch-level workstream status record. Update it after every material discovery, completed work package, evidence-status change, or blocker. GitHub issues may mirror task state, but this document remains the durable research-state handoff inside the repository.
