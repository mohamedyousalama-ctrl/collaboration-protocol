# Recovery Provenance and v1 Freeze Record

**Workstream:** Fan corpus validation
**Branch:** `research/fan-corpus-validation-2026-08-22`
**Date:** 2026-08-22

## Verdict

**WP1 authoritative reconstruction: PASS.**

The exact historical `CP_Incident_Database_v1.xlsx` has been recovered, reconstructed on the research branch, and verified byte-for-byte against the identity already declared by the preservation archive.

## 1. Historical identity declared by the archive

The preservation record declares:

- workbook name: `CP_Incident_Database_v1.xlsx`
- decoded size: **31,471 bytes**
- SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`
- expected Base64 stream length: **41,964 characters**

## 2. Defect discovered in the pre-existing Git Base64 representation

The pre-existing Base64 pieces under `archive/research-lineage-2026-01/binary/` did **not** reconstruct to the declared workbook identity.

Observed from those historical Git pieces:

- concatenated Base64 length: **35,408 characters**
- decoded size: **26,554 bytes**
- decoded SHA-256: `f75db1ce4037adfba3d749302e7a031bc9ec1e54a84a7b25153bb7668676113a`
- decoded payload was not a valid complete XLSX ZIP

This defect is preserved as evidence. The historical archive files on `main` were **not edited or silently repaired**.

## 3. Recovery source

The original research source bundle `files(3).zip` was located in the user's ChatGPT file library and materialized for recovery.

The bundle identity is:

- size: **182,607 bytes**
- SHA-256: `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8`

That SHA-256 exactly matches the existing repository source-bundle manifest entry for the recovered CP research package (`files(3).zip`). This creates an independent provenance link between the external recovered bundle and the Git preservation record.

Inside that bundle, the workbook was recovered as:

- `CP_Incident_Database_v1.xlsx`
- size: **31,471 bytes**
- SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`

The inner workbook therefore exactly matches the historical workbook identity declared by the archive.

## 4. Research-branch representation

Because the GitHub connector writes UTF-8 text rather than arbitrary binary through the contents API, the exact recovered workbook was Base64-encoded and split under:

`research/fan-corpus-validation/recovered-source/`

The six ordered chunks total exactly **41,964 Base64 characters**. A branch-only GitHub Actions verifier reconstructs the binary and refuses to inventory it unless all three identity conditions match:

1. Base64 length = 41,964 characters;
2. decoded size = 31,471 bytes;
3. SHA-256 = `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.

The verifier returned **PASS** and committed the exact working reconstruction at:

`research/fan-corpus-validation/work/CP_Incident_Database_v1.authoritative-v1.xlsx`

## 5. Verified workbook structure

The reconstructed workbook contains four worksheets:

- `README` — A1:A16
- `Codebook` — A1:C15
- `Incidents` — A1:AD53
- `Aggregates` — A1:C13

The `Incidents` sheet contains **52 incident rows plus one header row and 30 columns**.

All researcher-final fields `C0 FINAL` through `C10` are blank across all 52 rows. This confirms the historical v1 corpus is an extracted/triaged candidate corpus, not a completed researcher-validated dataset.

## 6. Freeze rule

The recovered v1 workbook is evidence, not an editable working dataset.

- Do not overwrite historical v1.
- Do not fill researcher-final cells in v1.
- WP2/WP4 analysis is recorded in separate audit/recommendation artifacts.
- Researcher decisions will later be applied only to a new v1.1 candidate after the required decision and QC stages.

## 7. Known schema observations carried into WP2

Two observations require explicit audit rather than silent normalization:

1. The protocol defines A1–A13, but the workbook has no dedicated `A4 Possible interpretations` column. The workbook README says A-fields were condensed from extraction reports and full text lives in source extract files.
2. The v1 aggregate formula `Silent (A6=NO) among INTENT` is not sufficient to distinguish silent resolution from `DISCLOSED-PROCEED`: two rows have `A6=NO` while their resolution style is explicitly `DISCLOSED-PROCEED`. v1 must remain untouched; any corrected metric belongs in v1.1/methods analysis.

These are audit findings, not retroactive edits to v1.
