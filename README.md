# The Collaboration Protocol (CP)

**Academic preservation archive of the Collaboration Protocol research program by Mohamed Salama.**

This repository preserves the theory, terminology, specifications, research designs, source artifacts, implementation experiments, empirical materials, applied extensions, provenance records, contradictions, and current research frontier associated with the Collaboration Protocol (CP).

The repository is intentionally **evidence-stratified**. It does not treat every historical file as equally authoritative. In particular, it distinguishes:

- **FROZEN / CANONICAL** — the semantics declared frozen for CP v1.0.1.
- **HISTORICAL THEORY** — earlier CP research lineages such as SII / IPP / ICD / IFI / Context Roots.
- **EXTENSION / DERIVATIVE** — later domain or product work such as Safety Floor, Klear, Ghost/Continuity, and applied decision packets.
- **EMPIRICAL MATERIAL** — scenario banks, workbooks, incident extraction, logs, and evaluation artifacts.
- **UNVERIFIED / INCOMPLETE** — claims or measurements for which the recovered archive does not contain sufficient primary evidence.
- **WORKING HYPOTHESIS** — current research directions that are not part of frozen CP and are not yet experimentally established.

## Start here

1. `docs/00_ARCHIVE_GUIDE.md` — how to read the archive and its evidence labels.
2. `docs/01_MASTER_RESEARCH_RECORD.md` — consolidated academic record of the research program.
3. `docs/02_CANONICAL_CP_V1_0_1_SPEC.md` — normalized reference for frozen CP v1.0.1 semantics.
4. `docs/03_TERMINOLOGY_AND_CONCEPT_INDEX.md` — terminology, definitions, lineage, and acronym collisions.
5. `docs/05_VERSION_AND_LINEAGE_MAP.md` — chronology and conceptual lineages.
6. `docs/09_PROVENANCE_AND_PRIORITY.md` — what the recovered evidence supports about dates and priority.
7. `docs/10_CONTRADICTIONS_AND_OPEN_QUESTIONS.md` — contradictions and unresolved research issues that must not be silently erased.
8. `docs/11_ASSET_REGISTER.md` — preserved asset inventory and hashes.

## Core frozen CP v1.0.1

The frozen interaction-level model is built around five named objects — **Context, Intent, Agent, Node, Pivot** — plus a five-link **Responsibility Chain**, a read-only **Guardian**, explicit **Friction**, six state stores, and append-only logging. The core execution rule is that consequential action must remain traceable to a verified human intent operating inside a valid context and authorized agent boundary.

The frozen Responsibility Chain is:

```text
User Signal -> CP Verification -> AI Suggestion -> User Commitment -> Action
```

## Important provenance caution

Some recovered frozen artifacts print dates in **January 2025**. The recovered provenance record does **not** support a 2025 CP priority date. The earliest supported CP activity in the recovered research record is **25 January 2026**. The original dated files are preserved as historical artifacts in the source register; this archive does not silently rewrite them and does not treat the printed 2025 dates as verified priority evidence.

## Security preservation rule

A recovered Klear source bundle contained live credential material in an environment file. That file is **not committed**. Its SHA-256 is preserved in the security record so the exclusion itself is auditable. Third-party ACM template PDFs are also excluded from the preservation payload because they are not original CP research artifacts.

## What this repository does not claim

This archive preserves authorship records and research artifacts; it does **not** independently establish legal novelty, patent validity, priority before the supported evidence date, peer-reviewed validation, or empirical superiority of CP. Historical documents that make stronger claims are retained as historical evidence and are explicitly status-labeled in the academic index.

## Researcher

**Mohamed Salama** — independent researcher and originator of the Collaboration Protocol research program represented in this archive.
