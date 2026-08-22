# Exact Reconstructible Source — `CP_Incident_Database_v1.xlsx`

This directory preserves a new, independently recovered exact representation of the authoritative v1 incident workbook for the Fan corpus validation workstream.

## Provenance

Recovered from a prior founder-provided archive (`files(3).zip`) and verified before preservation here.

## Identity

- Expected decoded size: `31,471` bytes
- Expected SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`
- Base64 stream length: `41,964` characters
- Parts: five files, `part-00` through `part-04`
- Chunk sizes: `9000, 9000, 9000, 9000, 5964` characters

## Reconstruction

```bash
cat research/fan-corpus-validation/source-v1-exact/CP_Incident_Database_v1.xlsx.b64.part-* \
  | tr -d '[:space:]' \
  | base64 -d \
  > CP_Incident_Database_v1.xlsx

wc -c CP_Incident_Database_v1.xlsx
# 31471

sha256sum CP_Incident_Database_v1.xlsx
# 3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a
```

## Preservation rule

This exact source representation is additive. It does not overwrite or rewrite the historical Base64 artifacts under `archive/research-lineage-2026-01/binary/`, whose current concatenated payload does not match the declared v1 workbook identity.
