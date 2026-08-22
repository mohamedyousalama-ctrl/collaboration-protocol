# Limitations and Evidence Status

## 1. Current status

The preserved historical artifact is a **52-record candidate naturalistic corpus**. The present workstream has now audited all 52 records and prepared assistant classification recommendations, but researcher-final adjudication is still pending and complete primary interaction transcripts are not available across the seven source families.

It is therefore not defensible to describe all 52 records as validated Silent Intent Inference events.

## 2. Exact current evidence counts

| Evidence/status class | Current count | Meaning |
|---|---:|---|
| Historical extracted candidates | 52 | Original candidate set; not a positive-SII count |
| Structural/construct audit completed | 52/52 | Every row reviewed in the current validation workstream |
| Assistant LIKELY SII | 12 | Provisional construct recommendation |
| Assistant POSSIBLE/source-dependent | 11 | Provisional; source/construct uncertainty material |
| Assistant NO/comparison class | 25 | Better explained by another mechanism or insufficient SII evidence |
| Assistant CONTROL/counter-pattern | 4 | Intentionally retained inverse/benign cases |
| Derivative GPT extract mapped | 5 | Extraction provenance improved; not primary verification |
| A3 corroborated by original task artifacts | 11 | W38/W39/KPF task evidence only; not full chronology |
| AUD primary behavior/output corroborated | 2 | AUD-020/021 have bounded primary execution/output evidence |
| Full C9 `CONFIRMED` | **0** | No row currently satisfies the project's complete primary-interaction verification threshold |
| C9 `CONTRADICTED` | 0 | No recovered primary source has yet materially contradicted a row |
| Researcher-final classifications in this validation pass | pending | Requires Mohamed's adjudication |

The evidence classes overlap in concept but are **not added together to create a “verified N.”**

## 3. Known limitations

### 3.1 Single-researcher/self-data context

The source material comes from one researcher's own AI-assisted work. This can be valuable for mechanism discovery, taxonomy development, and benchmark design, but it cannot by itself estimate population prevalence or user-to-user variability.

### 3.2 Non-independence of observations

The 52 records come from a small number of source windows within connected project work. Incidents can share tasks, standing instructions, model context, and correction history. Treating 52 rows as 52 independent statistical observations would be inappropriate without an explicit dependence model.

### 3.3 LLM-assisted extraction

Candidate incidents were extracted with an LLM under a fixed forensic protocol. The LLM was instructed not to perform the researcher-final classification, but candidate selection can still reflect model retrieval/segmentation biases. The current audit therefore treats extraction as a **candidate-generation stage**.

### 3.4 Historical workbook does not perfectly serialize the protocol

The protocol requires A4 Possible Interpretations, but the historical v1 workbook lacks A4 as a dedicated column. A4 was recovered for the five GPT rows from a derivative extraction report; it cannot be assumed for the remaining rows.

The workbook also contains condensed resolution-style labels whose temporal meaning can be ambiguous; AUD-021 is the clearest example.

### 3.5 Researcher-final coding incomplete

The historical researcher-only C-fields were not completed across all 52 rows. The current workstream has prepared assistant recommendations, but these cannot substitute for researcher adjudication, especially C5 TRUE INTENT.

### 3.6 Primary source availability incomplete

The autonomous recovery pass found several evidence classes but not the complete seven source interactions:

- GPT: derivative extraction report, not independently complete primary transcript;
- AUD: historical full-session path, bounded primary execution fragment, and preserved assistant handback; full source/user prompt still missing;
- CDX: exact historical extraction filename referenced but not recovered;
- W38/W39/KPF: original task artifacts corroborate some A3 content, but interaction chronology is missing;
- KBD: sufficiently complete source not found in the current preservation scope.

The search is now exhausted **within currently accessible preservation material**. This does not prove original provider exports no longer exist elsewhere.

### 3.7 Competence-versus-intent contamination

The extraction triggers were intentionally broad enough to catch plausible failure episodes. The stricter audit found many records better explained by factual/technical competence failure, environmental premise error, meta-process behavior, or a benign control pattern. This is why the final positive-SII denominator must not default to 52.

### 3.8 Selection and detection effects

The corpus comes from complex, highly governed AI-assisted project work where errors were often actively reviewed, challenged, or independently audited. Detection latency and observed consequence rates may be very different for ordinary consumer interactions in which mistakes remain unnoticed.

### 3.9 Researcher memory is not equivalent to transcript verification

Because the source interactions belong to the researcher, recollection may help establish C5 true intent, but it should not silently upgrade C9 source verification. A future methodology could add a separate `researcher recollection` evidence field if useful, but transcript confirmation and retrospective memory should remain distinct.

### 3.10 No forced N=52

Validation is allowed to reduce the final analyzable set. Exclusion, control status, source-dependent status, and unresolved evidence are legitimate outcomes.

### 3.11 No population prevalence claim

The historical CP research agenda contains prevalence hypotheses, but this naturalistic candidate corpus is not a probability sample and the current source-validation coverage is incomplete. It cannot establish a population-level SII prevalence percentage.

### 3.12 No causal bridge to DCM 2.0 is established

A conceptual relationship between upstream interpretation mechanics and downstream responsibility/burden attribution is plausible enough to investigate, but the current datasets were collected separately, at different units of observation, for different purposes.

Existing CP rows and DCM participants must **not** be treated as matched observations. A causal bridge requires a future study measuring both sides in one design.

## 4. Evidence language currently allowed

### Appropriate now

- “52 extracted candidate records”
- “52-record candidate naturalistic corpus”
- “documented LLM-assisted extraction protocol with researcher-only final coding”
- “52/52 records structurally and construct-audited in the current workstream”
- “assistant review recommends 12 likely, 11 possible/source-dependent, 25 comparison/non-SII, and 4 control/counter-pattern records”
- “primary-source recovery is incomplete; C9 confirmed is currently 0/52 at the specified evidence threshold”
- “researcher-final adjudication is pending”

### Not appropriate now

- “52 validated Silent Intent Inference events”
- “all 52 incidents are transcript-confirmed”
- “12 SII events have been scientifically proven”
- “the corpus proves SII prevalence”
- “the corpus proves CP causes better outcomes”
- “CP explains Fan's 79% result”
- “CP and DCM 2.0 form one connected dataset”
- “missing primary transcripts mean the extracted quotes are false”

## 5. Interpretation of the current 12 / 11 / 25 / 4 split

These categories are a **quality-control result**, not the study outcome.

They demonstrate that the validation process is willing to reject its own candidate extractions rather than treating every AI error as evidence for SII. That is scientifically useful because it establishes a comparison boundary and reduces confirmation bias.

The categories can change after researcher adjudication or if new source evidence is recovered.

## 6. Privacy and disclosure limitation

The original incidents arise from real project work and can contain internal repository details, tool outputs, operational information, or third-party context. The first methods exchange should therefore use schema descriptions and sanitized/paraphrased examples rather than raw full transcripts or the unredacted workbook unless there is a separate reason and review for sharing them.

## 7. Versioning rule

This methods-status package is a **pre-researcher-adjudication version**. After researcher decisions, a later package revision should update separately:

- researcher-final positive/negative/control counts;
- C5 completion status;
- final exclusions;
- source-verification status;
- any researcher-approved examples;
- and the exact analysis denominator.

The historical v1 workbook itself should remain frozen. A validated v1.1 should be created only after researcher adjudication and the separately planned independent QC.
