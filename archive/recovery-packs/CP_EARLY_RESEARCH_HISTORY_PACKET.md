# CP Early Research History — Exact Recovery Packet

This recovery packet preserves seven historically important pre-freeze / research-lineage artifacts as one compressed archive. The artifacts are retained as **historical theory and research-development evidence**. They do not override the later frozen CP v1.0.1 specification.

## Included sources

| Source | SHA-256 |
|---|---|
| `CP_Research_Package_Complete.md` | `cd181c8979f59be100c8afdbb474bcd7ae30ae302f588c7e8fa56981b854833f` |
| `CP_Research_Package_FINAL_v2.md` | `ecec64f114398404b9d8cfa9c3230fdcf31a8d4d91b07ea3b48b0159da1f7055` |
| `CP_Research_Package_v3.md` | `0ef44e10b51f39d621581a9907c37f935a6487a3524b49588fbda1ec157233d4` |
| `CP_Research_Package_FINAL_v4.md` | `fe420858c6798235c1b6dc065e96c2bd9403d23a68b5b293f843396f6ad15266` |
| `Master_Prompt_arXiv_Conversion.md` | `d5a50d6a41490ac326507ea805aa25f252b5d102efbc250886033aa81d0c864f` |
| `arXiv_Conversion_Plan.md` | `39898640541b708651f4390d60cc6a8df5b57de5a0bdbfa5dd368e91a6ab7484` |
| `collaboration_protocol_figures.html` | `849ea8c4321cba178ca46d08a0fd84e48dfcaa189502d351e07b62246297427f` |

## Packet identity

Original local packet:

`cp_early_research_history.tar.xz`

Expected SHA-256 after reconstruction:

`bc2958ba2bab192280b78b5e93dd6d947742fc4d183df333fc622bde9c13e2fb`

The packet is stored as six ordered Base64 parts:

`cp_early_research_history.tar.xz.b64.part-000` through `part-005`.

## Reconstruction

Because the connected UTF-8 writer may insert harmless ASCII whitespace around a text part, normalize Base64 whitespace during reconstruction:

```bash
cat archive/recovery-packs/cp_early_research_history.tar.xz.b64.part-* \
  | tr -d '[:space:]' \
  | base64 -d \
  > cp_early_research_history.tar.xz

sha256sum cp_early_research_history.tar.xz
# expected:
# bc2958ba2bab192280b78b5e93dd6d947742fc4d183df333fc622bde9c13e2fb

tar -xJf cp_early_research_history.tar.xz
```

After extraction, each source should also be checked against the per-file SHA-256 table above.

## Academic status

`HISTORICAL THEORY / VERSION LINEAGE / EXACT RECOVERY PACKET`

These files document the evolution of SII, IPP, ICD, IFI, Context Roots, materiality, proposed validation, publication conversion, and visual explanation work. Claims inside them retain their historical status. The frozen v1.0.1 documents under `archive/frozen-v1.0.1/` and the evidence-stratified interpretation under `docs/` control the current archival reading.
