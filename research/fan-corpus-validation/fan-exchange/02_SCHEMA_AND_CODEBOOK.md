# CP Corpus Schema and Codebook

## A-fields — extraction layer
These fields are populated from observable transcript evidence by the extraction procedure.

| Field | Meaning |
|---|---|
| A1 LOCATION | Approximate location of the incident in the conversation |
| A2 TASK CONTEXT | What work was being performed |
| A3 USER WORDS | Verbatim user instruction or ambiguous wording |
| A4 POSSIBLE INTERPRETATIONS | Reasonable alternative readings |
| A5 INTERPRETATION CHOSEN | Reading the AI acted upon |
| A6 WAS THE USER ASKED? | Whether clarification was requested before proceeding |
| A7 ASSUMPTION CONTENT | Specific unstated assumption inserted by the AI |
| A8 FIRST VISIBLE SIGNAL OF MISMATCH | First observable correction/complaint/detection |
| A9 TURNS UNTIL DETECTION | Delay between interpretation and visible mismatch |
| A10 CONSEQUENCE TRACE | Observable result such as rewrite, rollback, duplicated work, or no visible consequence |
| A11 RESOLUTION | How the incident ended |
| A12 PRIOR CONTEXT LINKS | Earlier context relevant to the intended interpretation |
| A13 CONFIDENCE | Extraction confidence, not truth status |

## C-fields — researcher layer
These fields are reserved for researcher classification after evidence review.

| Field | Meaning | Authority/status |
|---|---|---|
| C0 INCIDENT CLASS | INTENT / COMPETENCE / PREMISE / MIXED / META where used | Researcher decision |
| C1 IPP TYPE | Taxonomy category such as Scope, Temporal, Definition/Entity, Authority, Output Form, Abstraction Level, or proposed new type | Researcher decision |
| C2 MATERIALITY | Whether alternative interpretations would materially change the outcome | Researcher decision |
| C3 CONTEXT FACTOR | Effect of prior context quality/staleness/conflict | Researcher decision |
| C4 EFFECTIVE ICD | Estimated degree of interpretation authority delegated at the time | Researcher decision |
| C5 TRUE INTENT | What the user actually meant | Researcher only; cannot be established by assistant inference |
| C6 COST ESTIMATE | Estimated time/work/rework cost | Researcher decision informed by evidence |
| C7 HYPOTHESIS RELEVANCE | Which research hypothesis the incident may inform | Researcher decision |
| C8 BENCHMARK CANDIDATE | Whether the incident can be converted into a benchmark item | Researcher decision |
| C9 VALIDATION FLAG | Whether quotes were checked against the primary transcript | Requires source verification |
| C10 NOTES | Free-text research notes | Researcher decision |

## Evidence-status distinction
`A13 CONFIDENCE` and `C9 VALIDATION FLAG` are not interchangeable.

A high-confidence extraction can still be unverified if the original transcript cannot be independently checked. Conversely, a low-confidence candidate may become verifiable after returning to the primary source.

## Current validation rule
The active validation workstream will use these source-verification recommendations:

- `CONFIRMABLE` — primary transcript is available and can be checked;
- `UNVERIFIED_SOURCE_MISSING` — extracted record exists but primary transcript is not currently available;
- `CONTRADICTED` — primary transcript materially conflicts with the extracted record.

The final researcher dataset will preserve these distinctions rather than force every row into a validated category.
