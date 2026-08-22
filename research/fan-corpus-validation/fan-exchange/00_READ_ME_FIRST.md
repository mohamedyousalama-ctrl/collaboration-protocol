# Fan Chen-Chieh Methods Exchange — Read Me First

## Purpose
This package is prepared for a methods-first exchange between the Collaboration Protocol (CP) naturalistic incident corpus and DCM 2.0 public-layer materials.

It is intentionally narrower than a collaboration proposal. Its purpose is to make the CP corpus extraction logic, data structure, classification framework, evidence status, and limitations inspectable so that a data-level comparison can be made before any joint hypothesis or study design is proposed.

## Current corpus status
- Historical candidate corpus: 52 extracted records across seven source-window families.
- Extraction procedure: documented and preserved.
- Researcher-only classification framework: documented and preserved.
- Final researcher classification and transcript verification: incomplete and under active validation.
- Therefore the corpus must currently be described as a **52-record candidate naturalistic corpus**, not as 52 fully validated ground-truth incidents.

## Package contents
1. `01_METHODS_NOTE.md` — extraction and validation methodology.
2. `02_SCHEMA_AND_CODEBOOK.md` — A-fields and researcher-only C-fields.
3. `03_DCM2_CROSSWALK_TEMPLATE.md` — questions and mapping structure for comparing CP and DCM 2.0 at the data level.
4. `04_SANITIZED_EXAMPLES.md` — placeholder for examples that survive source verification and sanitization.
5. `05_LIMITATIONS_AND_EVIDENCE_STATUS.md` — evidence boundaries and current incompleteness.

## Exchange principle
The package separates:
- what the transcript directly shows;
- what an LLM extracted;
- what the researcher classifies;
- what remains unverified;
- and what would require a future joint interpretation.

No incomplete field is silently promoted to validated evidence.
