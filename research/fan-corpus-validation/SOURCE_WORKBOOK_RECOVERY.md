# CP Incident Database v1 — Source Workbook Recovery Evidence

**Recovery date:** 22 August 2026  
**Workstream:** Fan corpus validation  
**Research branch:** `research/fan-corpus-validation-2026-08-22`

## Verdict

The original `CP_Incident_Database_v1.xlsx` has been recovered from a prior founder-provided archive and byte-verified against the historical preservation record.

- Recovered source: `files(3).zip` from the founder-provided research archive set.
- Recovered member: `CP_Incident_Database_v1.xlsx`.
- Expected byte size: `31,471`.
- Recovered byte size: `31,471`.
- Expected SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.
- Recovered SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`.
- Identity verification: **PASS — exact byte identity**.

This resolves the earlier execution-environment blocker: the authoritative workbook bytes are now available for WP1/WP2 analysis.

## Workbook structural read-back

The recovered workbook opens as a valid XLSX package and contains four worksheets:

| Sheet | Rows | Columns | Notes |
|---|---:|---:|---|
| `README` | 16 | 1 | States 52 records / 7 windows and explicitly reserves C-fields to the researcher. |
| `Codebook` | 15 | 3 | Defines C0–C10 allowed values and meanings. |
| `Incidents` | 53 | 30 | Header + exactly 52 candidate incident rows. |
| `Aggregates` | 13 | 3 | Contains 12 summary formulas over the 52-row table. |

The `Incidents` sheet contains populated extraction/triage fields and blank researcher-final fields C0 FINAL through C10 in the recovered historical version.

## Important preservation discrepancy discovered

The Base64 parts currently preserved under `archive/research-lineage-2026-01/binary/` do **not** reconstruct to the declared workbook identity when concatenated as currently stored in Git. A branch-side diagnostic produced:

- Git Base64 stream: `35,408` characters vs historical expected `41,964`.
- Decoded Git payload: `26,554` bytes vs expected `31,471`.
- Git payload SHA-256: `f75de5b2b427c2a4c3037112085436fefc8916811914c68fb83120dc8ea12eaf` vs authoritative `3a5d4e82...ed4a`.

Therefore the historical Git Base64 representation must remain preserved as an evidence artifact, but it is **not** itself an exact reconstructible copy of the workbook. The recovered byte-identical workbook is the authoritative v1 source for this validation workstream.

## Scientific handling rule

1. Do not overwrite or silently repair the historical archive representation on `main`.
2. Preserve a new exact reconstructible representation on this research branch with explicit provenance and checksum.
3. Audit the 52 rows from the byte-verified source workbook.
4. Keep all C-field output produced by ChatGPT as recommendations only until the researcher makes the final decisions.
