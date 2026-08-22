# CP Corpus Schema and Codebook

## 1. Important provenance distinction

The preserved **IPP Incident Extraction Protocol v1.0** defines the extraction layer A1–A13 and the researcher-only classification layer C1–C10.

The present validation workstream adds **C0 INCIDENT CLASS** as a practical screening variable to separate intent-interpretation candidates from competence, premise, mixed, meta, and control/comparison cases. C0 is useful for validation, but it must not be falsely described as part of the original v1.0 protocol.

A second structural distinction is also important: the protocol requires A4 Possible Interpretations, but the historical v1 workbook does **not** preserve A4 as a dedicated workbook column. A4 is recoverable for the five GPT rows from their derivative extraction report; it is not assumed to be recoverable for every row.

## 2. A-fields — extraction layer

These fields belong to the forensic extraction procedure and are intended to be grounded in observable source-interaction evidence.

| Field | Meaning | Evidence role |
|---|---|---|
| A1 LOCATION | Approximate location of the incident in the conversation | Navigation/provenance aid |
| A2 TASK CONTEXT | What work was being performed | Context description |
| A3 USER WORDS (VERBATIM) | Exact user instruction or ambiguous wording | Primary IPP site; must be source-checked for C9 |
| A4 POSSIBLE INTERPRETATIONS | Reasonable alternative readings available at the decision point | Branch-space representation; missing as dedicated column in historical workbook |
| A5 INTERPRETATION CHOSEN | Reading or course of action the AI adopted | Mechanism/action evidence |
| A6 WAS THE USER ASKED? | Whether clarification was requested before proceeding | Silent-vs-surfaced resolution indicator |
| A7 ASSUMPTION CONTENT | Specific unstated assumption introduced | Content of inferred intent/premise |
| A8 FIRST VISIBLE SIGNAL OF MISMATCH | First observable correction, complaint, self-disclosure, or detection | Awareness/detection evidence; must be source-checked where applicable |
| A9 TURNS UNTIL DETECTION | Delay between interpretation and visible mismatch | Awareness-gap timing; historical values need normalization before statistics |
| A10 CONSEQUENCE TRACE | Observable rework, rollback, delay, duplicated work, blocked action, or no visible consequence | Outcome/cost trace |
| A11 RESOLUTION | How the episode ended | Recovery mechanism |
| A12 PRIOR CONTEXT LINKS | Earlier context relevant to the intended interpretation | Context-root evidence |
| A13 CONFIDENCE | Extractor confidence | Extraction reliability only; not truth/validation status |

## 3. Original researcher-only C1–C10 layer

The original protocol reserves these for researcher adjudication after evidence review.

| Field | Original role | Operational guidance |
|---|---|---|
| C1 IPP TYPE | Type of interpretation point | Original categories: Temporal, Scope, Definition, Authority, Output Form, Abstraction Level, or a justified NEW TYPE |
| C2 MATERIALITY | Material vs trivial | Material only if plausible alternative interpretations would meaningfully change output/action |
| C3 CONTEXT FACTOR | Prior-context contribution | 1.0 no prior context; 1.25 weak/stale; 1.5 conflicting, based on A12 |
| C4 EFFECTIVE ICD | Degree of interpretation authority delegated | 0–1 research estimate; requires an explicit coding rule before inferential statistics |
| C5 TRUE INTENT (GROUND TRUTH) | What the researcher/user actually meant | **Researcher-only authority**; assistant inference cannot finalize this field |
| C6 COST ESTIMATE | Time/work/rework cost | Must distinguish observed from estimated cost |
| C7 HYPOTHESIS RELEVANCE | H1 prevalence, H2 awareness gap, ICD effect, or other | Researcher decision |
| C8 BENCHMARK CANDIDATE | Suitability for benchmark conversion | YES/NO with evidence/clarity rationale |
| C9 VALIDATION FLAG | Quote/source validation | `CONFIRMED` only after sufficient primary-source check; otherwise `UNVERIFIED` |
| C10 NOTES | Research notes | Free text; should record caveats, exclusions, links, and adjudication reasoning |

## 4. Added C0 validation helper

The present corpus audit uses C0 before SII-specific analysis:

| C0 value | Meaning |
|---|---|
| INTENT | Primary failure mechanism appears to concern what the user wanted/meant |
| COMPETENCE | Better explained by technical/factual/execution capability failure |
| PREMISE | Better explained by a wrong factual/environmental premise rather than user intent |
| MIXED | Intent interpretation and another failure mechanism are materially intertwined |
| META | Extraction/audit/process artifact rather than an ordinary task incident |
| CONTROL / NO_POSITIVE_CLASS | Counter-pattern or non-positive case intentionally retained for comparison |

C0 is an **assistant recommendation until researcher adjudication**. It is not a replacement for C1–C10.

## 5. Current construct-validity screening

The stricter assistant review currently recommends:

| Screening outcome | N | Interpretation |
|---|---:|---|
| LIKELY SII | 12 | Strong provisional fit to the SII construct; still requires researcher adjudication and source caveats |
| POSSIBLE / SOURCE-DEPENDENT | 11 | Plausible SII but source or construct ambiguity is material |
| NO / COMPARISON CLASS | 25 | Better explained by competence, premise, meta, or insufficient intent mechanism |
| CONTROL / COUNTER-PATTERN | 4 | Useful inverse/benign examples; not positive SII incidents |
| **Total** | **52** | Historical candidate set preserved intact |

These counts are **not prevalence estimates** and are not researcher-final results.

## 6. Evidence-status distinction

`A13 CONFIDENCE`, assistant construct category, and `C9 VALIDATION FLAG` answer different questions:

- **A13** — how confident was the extractor in identifying the candidate from what it saw?
- **construct category** — how well does the later auditor think the record fits SII rather than another failure class?
- **C9** — has sufficient primary interaction evidence been independently checked?

A high-confidence extraction can remain C9 UNVERIFIED. A plausible SII can remain source-dependent. A source-corroborated task instruction can still lack the later mismatch chronology.

## 7. Current source-verification vocabulary

The validation workstream preserves evidence classes rather than reducing them to one boolean:

- `SOURCE_EXTRACT_ONLY` — derivative extraction exists, primary interaction not independently complete;
- `A3 CORROBORATED — PRIMARY TASK ARTIFACT` — original work order/instruction supports A3/context, but not full incident chronology;
- `A5 PRIMARY EXECUTION BEHAVIOR CORROBORATED` — primary execution record supports action/order;
- `A8 INTERACTION-OUTPUT CORROBORATED` — preserved assistant-side output supports mismatch/disclosure;
- `UNVERIFIED — ...` — insufficient primary evidence for full C9 confirmation;
- `CONTRADICTED` — primary source materially conflicts with the candidate record;
- `CONFIRMED` — sufficient primary interaction evidence verifies the required quotation/chronology.

At the present threshold, C9 `CONFIRMED` remains **0/52**.

## 8. Rules for final researcher coding

For each row the researcher should:

1. review the compact evidence card and assistant recommendation;
2. decide `ACCEPT`, `OVERRULE`, or `DEFER FOR SOURCE`;
3. provide C5 true intent where the row is meaningfully adjudicable;
4. finalize C1–C4 and C6–C10 as appropriate;
5. explicitly exclude rows that do not satisfy the intended construct rather than forcing them into SII;
6. preserve controls and comparison classes as such; and
7. never convert missing source evidence into C9 confirmation by researcher recollection alone unless the methodology is explicitly revised to distinguish recollection from transcript verification.

## 9. Analysis rule

No statistic should use `N=52` as the denominator for “validated SII events.” Future analysis must state its denominator explicitly, for example:

- all extracted candidates;
- construct-eligible candidates;
- source-verified candidates;
- researcher-final positive SII cases;
- or a separately defined analysis subset.

This prevents candidate-generation counts from being mistaken for empirical prevalence.
