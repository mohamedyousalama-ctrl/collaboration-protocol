# 11 — Asset Register

**Preservation date:** 22 August 2026

This register records the substantive source families recovered during the preservation pass, their academic status, source-bundle fingerprints, and known exclusions. The normalized `docs/` record is intentionally separate from historical source artifacts.

## 1. Source families

| Family | Recovered material | Status |
|---|---|---|
| Frozen CP v1.0.1 | Freeze Declaration, System Model, Evaluation Framework, Diagram Pack, Paper Alignment, academic drafts, quick-start, runtime, implementation spec, validation template | Frozen semantics plus implementation evidence; known internal conflicts retained |
| January 2026 research lineage | SII, IPP, ICD, IFI, Context Roots, Context Factor, SMP, research packages, agenda, arXiv conversion work | Historical theory and proposed empirical program |
| Naturalistic incident program | IPP extraction protocol, 52-row incident workbook, research backlog | Empirical candidate corpus; researcher-final coding incomplete |
| Klear | implementation specification, source code, finance workbooks, diagrams/screenshots and evidence package | Applied implementation/pilot evidence; not clean frozen-v1 reference |
| IntentHealth / Safety Floor | health-domain materials, Safety Floor specification, IFI-H/SCS proposals | Domain extension / pilot-driven theory |
| Ghost / Project Continuity | constitution, strategy, decisions, continuity architecture, Kivo cross-product learning | Applied derivative research |
| Current authority-continuity research | zero-ambiguity post-approval drift, ESAI/EAF/SAC and domain benchmark notes | Working hypothesis / benchmark design |
| Publication / IP | TechRxiv record, arXiv metadata/workflow, provisional patent draft/application artifact | Publication workflow and IP drafting evidence |
| Provenance | provenance memo, technical audit, master knowledge records | Provenance/audit evidence with stated limitations |

## 2. Recovered bundle fingerprints

| Original bundle | Bytes | SHA-256 |
|---|---:|---|
| `files(3).zip` | 182,607 | `4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8` |
| `files(4).zip` | 139,240 | `ac377d0f8253002aaf8f0c8bf1ddc55b275c39019bfd6aec2bb00aaa57711552` |
| `files-31.zip` | 166,212 | `cf039f23f0d6eaec7232f690792b4d7878306c02e747f9a8b29aa0831f0bbe2d` |
| `files-29.zip` | 146,674 | `4c07ab6a60fed08973c064cf59fa428f2d23d07727fbedd6f9092bf8ce703743` |
| `files-28 2.zip` | 4,873,757 | `ba8b2e86d472da66839ad2c34e83448f04713df2137e1f692f380b787e708fe7` |
| sanitized Klear reconstruction | 13,942,209 | `abda38e6f8e6c3cc20907550eeb08ecf1ea5f83897dc16f796e43bb2b5527b1c` |

The same fingerprints are kept in `MANIFEST_SOURCE_BUNDLES_SHA256.txt`.

## 3. Key early-research artifacts recovered

- `CP_Research_Package_Complete.md`
- `CP_Research_Package_FINAL_v2.md`
- `CP_Research_Package_v3.md`
- `CP_Research_Package_FINAL_v4.md`
- `CP_Research_Package_v4.1_arXiv.md`
- `collaboration_protocol_research_agenda.md`
- `arXiv_Conversion_Plan.md`
- `Master_Prompt_arXiv_Conversion.md`
- `IPP_Extraction_Protocol.md`
- `CP_Research_Backlog.md`
- `CP_Master_Knowledge_File.md`
- `CP_Incident_Database_v1.xlsx`
- `collaboration_protocol_figures.html`

## 4. Key frozen-v1 artifacts recovered

- `cp_v1_0_1_freeze_declaration.md`
- `cp_v1_system_model_final.md`
- `cp_v1_evaluation_framework.md`
- `cp_v1_diagram_pack.md`
- `cp_v1_1_paper_alignment.md`
- `cp_v1_paper_draft.md`
- `cp_v1_paper_draft_v2.md`
- `cp_v1_quick_start_guide.md`
- `cp_v1_0_1_runtime_persistent.html`
- `CP_v1_Implementation_Complete.md`
- `v1_0_1_validation_tests.md`
- historical runtime/test/phase-report variants

## 5. Other material recovered

The broader source inventory also contains early TeX/PDF paper versions, IntentHealth JSX prototypes and market/execution documents, Safety Floor specification, Klear source/evidence workbooks, Ghost/Continuity strategy and decision documents, CP/Ghost decision packets, publication metadata, provisional-patent drafting material, and current industrial/authorization-continuity research notes.

Binary source artifacts that could not be transferred through the connected GitHub text-content interface during this preservation session remain represented by exact SHA-256 fingerprints and named source inventories. Textual source equivalents and the academic interpretation record are committed wherever recoverable.

## 6. Security / rights exclusions

A recovered Klear environment file contained live credential material. It is intentionally excluded. Its SHA-256 is:

`d931c8ef19e69e2b1dcd0ce3662602eceec8e9c486cebd0abb37d15cb96145e7`

No credential values are reproduced.

Two third-party ACM template PDFs are also excluded from the CP research payload. Their hashes are preserved in the security record:

- `4a28c98c57a8e8ce0823b89a6102954f32ec845c8e38784e18ed05303c14f885`
- `c921910170c3d6ff9e55612266a7b73a0ac39388eff0bef9dc6a4cc3f2a846d9`

## 7. Material gaps that remain evidence, not errors to hide

- official USPTO filing receipt not recovered in this preservation set;
- raw simulation generator/output behind some historical kappa/latency claims not recovered;
- 52-row incident database researcher-final classification incomplete;
- Klear workbook generations use inconsistent denominators and are not reconciled into one final dataset;
- frozen validation template is unexecuted in the recovered copy;
- historical HTML runtime omits canonical PE-3, PE-8 and PE-9 checks;
- no clean fully conformant CP v1.0.1 Reference Runtime is present in the recovered archive.

The register should be extended whenever a primary artifact is recovered; old fingerprints and gaps should never be silently deleted.
