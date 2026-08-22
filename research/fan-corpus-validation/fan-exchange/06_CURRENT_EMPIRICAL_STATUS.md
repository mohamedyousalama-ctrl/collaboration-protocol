# Current Empirical Status — Pre-Researcher Adjudication

**Date:** 22 August 2026  
**Purpose:** give Fan a compact, exact account of what currently exists without confusing candidate extraction, assistant audit, source verification, and researcher-final evidence.

## 1. Corpus identity

Historical candidate corpus:

- records: **52**;
- source families: **7**;
- authoritative recovered workbook: **31,471 bytes**;
- SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4`.

The historical workbook has been frozen unchanged. Validation outputs are additive artifacts on a dedicated research branch.

## 2. Two-pass audit result

### Pass 1 — structural/evidence readiness

| Disposition | N |
|---|---:|
| PASS_TO_SOURCE_VERIFICATION | 21 |
| NEEDS_SOURCE | 11 |
| STRUCTURAL_DEFECT | 2 |
| EXCLUDE_CANDIDATE | 18 |
| **Total** | **52** |

`EXCLUDE_CANDIDATE` means exclude from the positive-SII candidate set on current evidence, not delete the historical row.

### Pass 2 — construct-validity recommendation

| Recommendation | N |
|---|---:|
| LIKELY SII | 12 |
| POSSIBLE / SOURCE-DEPENDENT | 11 |
| NO / COMPARISON CLASS | 25 |
| CONTROL / COUNTER-PATTERN | 4 |
| **Total** | **52** |

This pass asks whether the candidate actually looks like an unauthorized interpretation of user intent with material effect, rather than merely “an AI error.”

## 3. Source-evidence state

The source-recovery categories are intentionally non-additive:

| Evidence class | N | Meaning |
|---|---:|---|
| GPT derivative source extract mapped | 5 | Full derivative incident records recovered, but not independently complete primary transcript |
| Original task-artifact A3/source corroboration | 11 | W38/W39/KPF triggering instruction/content independently present; later chronology incomplete |
| AUD primary execution/output corroboration | 2 | AUD-020/021 behavior/outcome supported by bounded primary/session evidence |
| AUD-021 A8 self-disclosure corroborated | 1 | Preserved assistant handback supports same-reply procedural disclosure |
| C9 CONFIRMED | **0** | No row currently has sufficient primary interaction evidence for the project's full A3/A8/chronology threshold |
| C9 CONTRADICTED | 0 | No recovered primary source materially disproves a candidate row |

The evidence classes above must not be added into a single “verified” number because they establish different parts of different incidents.

## 4. Main data-quality findings

The current validation work identified several issues that matter before quantitative analysis:

1. A4 Possible Interpretations is required by the extraction protocol but missing as a dedicated historical workbook column.
2. A6 alone cannot be treated as a clean “silent inference” indicator because some records involve disclosure before/after action rather than a simple yes/no distinction.
3. A9 detection-delay values need normalization before aggregation.
4. Some rows have A3/A8 overlap or compressed chronology that requires source-level interpretation.
5. The historical candidate set contains competence, premise, meta, and control records as well as plausible intent cases.
6. Suggested machine classifications in the workbook are not researcher-final classifications.
7. A verified source quotation and a researcher statement of true intent answer different evidentiary questions and must remain separate.

## 5. What can be analyzed now

The current materials support **methodological and descriptive audit statements**, for example:

- the corpus contains 52 historical candidate records;
- all 52 have now undergone a structured assistant audit;
- the audit does not treat every candidate as a positive SII case;
- source preservation varies materially by family;
- controls/comparison cases exist and are being retained;
- the final positive denominator is intentionally unresolved pending researcher adjudication.

## 6. What should not be analyzed yet

Do not yet calculate or publish:

- a “silent inference rate” using all 52 as the positive denominator;
- H1 prevalence from this corpus;
- a median awareness gap for “validated SII” without first defining the final eligible subset and normalizing A9;
- effect sizes involving C3/C4 before researcher coding rules are finalized;
- cost totals as though every A10/C6 value were measured rather than partly estimated;
- benchmark accuracy using assistant recommendations as ground truth;
- any causal relationship between CP variables and Fan's DCM 2.0 responsibility variables.

## 7. Researcher adjudication still required

The assistant has prepared a recommendation for every row, but the following decisions remain researcher-controlled:

- whether each candidate is accepted, overruled, or deferred for more source evidence;
- C1 IPP type;
- C2 materiality;
- C3 context factor;
- C4 effective interpretation-control delegation estimate;
- **C5 true intent**;
- C6 cost estimate/measurement status;
- C7 hypothesis relevance;
- C8 benchmark candidacy;
- C10 notes and exclusion rationale;
- final treatment of source-unverified cases.

C9 is evidence-dependent and should not be upgraded merely because the researcher remembers the event.

## 8. Current scientific claim ceiling

The strongest concise statement currently supported is:

> **We assembled 52 candidate interpretation-failure records from naturalistic AI-assisted work using a fixed LLM-assisted forensic extraction protocol. A subsequent two-pass audit found substantial construct heterogeneity: 12 records are provisionally likely SII, 11 possible/source-dependent, 25 better treated as non-SII/comparison cases, and 4 as controls/counter-patterns. Primary-source preservation is incomplete, so no incident is yet labeled fully C9-confirmed under the current transcript-verification standard; researcher-final adjudication remains pending.**

This is the recommended empirical-status description for the first Fan methods exchange.
