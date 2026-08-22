# Collaboration Protocol Research Archive — Start Here

**Researcher:** Mohamed Salama  
**Preservation edition:** 22 August 2026  
**Purpose:** Preserve the Collaboration Protocol research program without collapsing historical drafts, frozen semantics, implementation evidence, empirical materials, extensions, and current hypotheses into one undifferentiated narrative.

## What this repository preserves

This archive documents the full CP research lineage available in the preservation corpus:

1. **Early semantic-authority theory** — Silent Intent Inference (SII), Intent Pivot Points (IPP), Intent Control Degree (ICD), Intent Fidelity Index (IFI), Context Roots, Context Factor, Semantic Materiality Proxy, IPP logging, Intent Decay, Intent Signatures, and proposed validation studies.
2. **Frozen CP v1.0.1** — Context, Intent, Agent, Node, Pivot, the five-link Responsibility Chain, read-only Guardian, PC/PE rules, Friction, six stores, append-only logging, frozen non-goals, and evaluation scope.
3. **Implementation evidence** — historical runtime/specification material, technical audit, Klear source-code evidence, known conformance gaps, and fail-open paths.
4. **Empirical work** — financial Klear comparison workbooks, 52-row naturalistic incident corpus, extraction protocol, research backlog, and known data-integrity limitations.
5. **Domain extensions** — IntentHealth and Safety Floor / SCS / IFI-Health work.
6. **Derivative systems research** — Ghost / Project Continuity, Memory-is-not-Authority, Presence, Meaning Ledger, Decision Packets, Ambient Context Fabric, and cross-product learning.
7. **Current research frontier** — continuous authorization integrity after explicit approval, zero-ambiguity authority-drift benchmarks, EAF/ESAI/SAC and related metrics, finance/payment and industrial-control candidate testbeds.
8. **Publication/IP/provenance** — TechRxiv publication record, arXiv workflow artifacts, patent-drafting record, provenance conflicts, source hashes, and security exclusions.

## Read in this order

1. [`docs/00_ARCHIVE_GUIDE.md`](docs/00_ARCHIVE_GUIDE.md)
2. [`docs/01_MASTER_RESEARCH_RECORD.md`](docs/01_MASTER_RESEARCH_RECORD.md)
3. [`docs/03_TERMINOLOGY_AND_CONCEPT_INDEX.md`](docs/03_TERMINOLOGY_AND_CONCEPT_INDEX.md)
4. [`docs/05_VERSION_AND_LINEAGE_MAP.md`](docs/05_VERSION_AND_LINEAGE_MAP.md)
5. [`docs/02_CANONICAL_CP_V1_0_1_SPEC.md`](docs/02_CANONICAL_CP_V1_0_1_SPEC.md)
6. [`docs/06_IMPLEMENTATION_AND_EMPIRICAL_EVIDENCE.md`](docs/06_IMPLEMENTATION_AND_EMPIRICAL_EVIDENCE.md)
7. [`docs/10_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`](docs/10_CONTRADICTIONS_AND_OPEN_QUESTIONS.md)
8. [`docs/08_CURRENT_RESEARCH_FRONTIER_AUTHORITY_CONTINUITY.md`](docs/08_CURRENT_RESEARCH_FRONTIER_AUTHORITY_CONTINUITY.md)
9. [`docs/14_RESEARCH_DECISION_LOG.md`](docs/14_RESEARCH_DECISION_LOG.md)
10. [`docs/09_PROVENANCE_AND_PRIORITY.md`](docs/09_PROVENANCE_AND_PRIORITY.md)
11. [`docs/11_ASSET_REGISTER.md`](docs/11_ASSET_REGISTER.md)
12. [`docs/12_SECURITY_AND_DISCLOSURE_LOG.md`](docs/12_SECURITY_AND_DISCLOSURE_LOG.md)

## Evidence-status discipline

Every claim should be interpreted under one of these statuses:

- **FROZEN / CANONICAL** — frozen CP v1.0.1 semantics.
- **HISTORICAL THEORY** — earlier research lineage, not automatically frozen CP semantics.
- **IMPLEMENTATION EVIDENCE** — what code actually did, including defects.
- **EMPIRICAL MATERIAL** — collected pilot/corpus evidence, with limitations retained.
- **EXTENSION / DERIVATIVE** — later domain/product work outside frozen CP v1.0.1.
- **WORKING HYPOTHESIS** — current research direction that still requires testing.
- **CONTRADICTED / UNRESOLVED** — conflicting sources are deliberately preserved.
- **EXCLUDED FOR SECURITY/RIGHTS** — source identity is recorded but sensitive/third-party bytes are not exposed.

## Provenance warning

Some historical frozen artifacts print dates in **January 2025**. The recovered provenance record explicitly states that it found no independent support for a 2025 CP date and places the earliest supported CP activity at **25 January 2026**. The original printed dates are preserved as historical evidence, but this repository does **not** use them as verified priority claims.

## Security warning

A recovered Klear environment file contained live credential material. It is intentionally excluded; only its SHA-256 is retained in the security record. Do not restore the secret-bearing file into Git. Credentials that appeared in exported evidence should be rotated/revoked at their providers.

## Core preservation rule

> Preserve the source, preserve the contradiction, preserve the limitation, and never repair history by silently rewriting it.

That rule is more important than producing a clean story. The purpose of this archive is to make future academic, engineering, benchmark, publication, and IP work reconstructible from a truthful research record.
