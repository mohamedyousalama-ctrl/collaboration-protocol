# Authoritative CP Incident Database v1 — Reconstruction and Inventory

**Identity verification: PASS**

- Source bundle SHA-256: `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8`
- Base64 stream: `41964` characters (expected `41964`)
- Reconstructed workbook: `31471` bytes (expected `31471`)
- Workbook SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`
- Historical v1 was not edited; this is an exact working reconstruction.

## Workbook structure

| Sheet | Used range | Non-empty cells | Formulas |
|---|---:|---:|---:|
| README | A1:A16 | 13 | 0 |
| Codebook | A1:C15 | 45 | 0 |
| Incidents | A1:AD53 | 980 | 0 |
| Aggregates | A1:C13 | 37 | 12 |

The `Incidents` sheet contains **52 records** plus one header row and **30 columns**.

## Incident columns

1. `GID`
2. `Window`
3. `Local ID`
4. `A1 Location`
5. `A2 Task context`
6. `A3 User words (verbatim, may be trimmed)`
7. `A5 Interpretation chosen`
8. `A6 Asked?`
9. `Resolution style`
10. `A7 Assumption`
11. `A8 Mismatch signal`
12. `A9 Turns to detect`
13. `A10 Consequence`
14. `A11 Resolution`
15. `A12 Prior context`
16. `A13 Conf.`
17. `C0 SUGGESTED`
18. `Outcome (sugg.)`
19. `Recurrence link`
20. `C0 FINAL`
21. `C1 IPP type`
22. `C2 Materiality`
23. `C3 CF`
24. `C4 ICD`
25. `C5 Ground-truth intent`
26. `C6 Cost`
27. `C7 Hyp`
28. `C8 Bench`
29. `C9 Valid`
30. `C10 Notes`

## Generated audit inputs

- `CP_Incident_Database_v1.authoritative-v1.xlsx` — exact reconstructed workbook.
- `authoritative_v1_inventory.json` — structural inventory and blank counts.
- `workbook_cells.tsv` — cell-level export.
- `formula_inventory.tsv` — formula export.
- `incident_rows.tsv` — 52-row audit input.

No researcher-final classification was added or changed in this reconstruction step.
