# 00 — Archive Guide and Evidence Discipline

**Preservation date:** 22 August 2026  
**Archive owner / research author:** Mohamed Salama  
**Purpose:** Preserve the complete recoverable Collaboration Protocol research record without silently merging incompatible versions, overstating evidence, or publishing secrets.

## 1. Why this archive exists

The Collaboration Protocol research program exists across multiple generations of documents, experiments, source-code bundles, research workbooks, product applications, and later theory. Several of those generations reuse terminology differently. Some files are frozen specifications; some are exploratory papers; some are implementation attempts; some contain empirical observations; some contain proposed experiments; and some contain claims that the recovered evidence does not yet verify.

A preservation archive that simply puts every file in one folder would lose the most important information: **which artifact meant what, when, and with what evidentiary status**. This repository therefore preserves both the original artifacts and a normalized academic index.

## 2. Evidence-status labels

| Label | Meaning |
|---|---|
| **FROZEN / CANONICAL** | Declared semantic authority for CP v1.0.1. A later file may contradict it; the contradiction is recorded rather than silently harmonized. |
| **HISTORICAL THEORY** | Earlier CP research lineage. Important to intellectual development, but not automatically part of frozen CP v1.0.1. |
| **EXTENSION / DERIVATIVE** | Later construct, domain extension, product application, or applied architecture that builds on CP without redefining the frozen core. |
| **IMPLEMENTATION EVIDENCE** | Code, runtime, test artifact, or technical report showing what an implementation actually did. |
| **EMPIRICAL MATERIAL** | Scenario banks, ratings, transcripts/extracts, workbooks, observed incidents, or evaluation outputs. |
| **PROPOSED STUDY** | A research design or hypothesis that has not yet been executed to the stated standard. |
| **UNVERIFIED CLAIM** | A statement present in a historical artifact for which the recovered archive does not contain sufficient primary evidence. |
| **CONTRADICTED / INCONSISTENT** | Two or more recovered artifacts conflict materially. Both are retained, and the conflict is surfaced. |
| **WORKING HYPOTHESIS** | Current research direction; not frozen semantics and not established empirical finding. |
| **EXCLUDED FOR SECURITY / RIGHTS** | Known artifact intentionally not committed because it contains live credentials or is third-party material outside the original research corpus. A hash or inventory record is retained where appropriate. |

## 3. Source hierarchy used by this preservation pass

For frozen CP v1.0.1 semantics, the normalized record gives highest authority to the recovered **System Model** and **Freeze Declaration**, then cross-checks the Evaluation Framework and Paper Alignment Guide. The recovered `CP_v1_Implementation_Complete.md` and HTML runtime are preserved as implementation artifacts but are **not allowed to silently override the System Model**, because they contain rule differences documented in `10_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`.

For early CP theory (SII / IPP / ICD / IFI / Context Roots / SMP / CF), the archive treats the January 2026 research-package lineage and the public preprint as historical/theoretical sources. These constructs remain important intellectual contributions of the research program but are not automatically the same thing as the later frozen v1.0.1 object model.

For empirical claims, raw workbooks and incident records outrank prose summaries. Where prose and spreadsheets disagree, the disagreement is preserved and the claim is not promoted as settled.

## 4. Preservation principles

1. **Preserve originals.** Recovered source bundles are kept byte-for-byte where safe.
2. **Never repair history invisibly.** Incorrect dates, stale claims, and superseded terminology stay in the historical artifacts.
3. **Normalize separately.** Corrected interpretation belongs in `docs/`, not by rewriting the source artifact.
4. **No fabricated completion.** Blank researcher-final fields, unexecuted validation templates, and missing raw outputs remain explicitly incomplete.
5. **No false priority.** A printed date is not treated as provenance merely because it appears in a document.
6. **No secret publication.** Live credentials are excluded even if they appeared in a recovered source package.
7. **No novelty overclaim.** This archive records what the research program names and proposes; it does not substitute for a formal prior-art or patentability search.
8. **No empirical overclaim.** Pilot findings and historical comparative results are preserved with their design limitations and denominator inconsistencies.
9. **Frozen means frozen.** Later useful concepts do not retroactively become CP v1.0.1.
10. **Derivative work is still preserved.** Ghost/Continuity, Safety Floor, Klear, VEIS decision packets, and current authority-continuity research are archived because they document how CP ideas developed in practice.

## 5. Directory map

```text
archive/
  source-bundles/           recovered historical bundles
  frozen-v1.0.1/           frozen-spec sources and implementation-adjacent artifacts
  research-lineage-2026-01/ early SII/IPP/ICD/IFI/CR research program
  klear/                    sanitized Klear code/evidence package
  applied/                  Ghost/Continuity/domain applications and source records
  current-frontier/         August 2026 authority-continuity / industrial-agent research
  provenance/               provenance and audit records
  publication-and-ip/       publication metadata and patent-drafting artifacts

docs/                       normalized academic record
MANIFEST_SHA256.txt          repository-preservation hashes
```

## 6. What “complete” means here

“Complete” means **all recoverable, substantively CP-related material located in the available source bundles and research library was either committed, represented by a preserved source bundle, or explicitly listed as excluded/missing**. It does not mean that every historical claim has been validated or that every referenced external artifact was recovered.

The asset register identifies remaining gaps and exclusions.
