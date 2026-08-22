# Collaboration Protocol Naturalistic Incident Corpus — Methods Exchange Packet

**Prepared for:** Fan Chen-Chieh (Ah-Guang)  
**Prepared by:** Mohamed Salama  
**Purpose:** methods-first comparison with DCM 2.0 public-layer materials  
**Status:** methods-status exchange; not a final results release

## 1. Why this note exists

This note describes how the Collaboration Protocol (CP) naturalistic incident corpus was extracted, structured, audited and prepared for researcher classification. It is intended for a data-level comparison with DCM 2.0 before either side assumes that the two datasets measure the same construct or proposes a formal joint study.

The preserved historical corpus contains **52 extracted candidate records** from naturalistic AI-assisted work conversations. A later methodological audit deliberately separates those 52 extracted candidates from the smaller set that may ultimately qualify as positive Silent Intent Inference (SII) incidents.

Accordingly, the correct present description is **52 extracted candidate incidents**, not 52 fully validated SII events.

## 2. Research object and unit of analysis

The research object is a possible **Silent Intent Inference** event: a case in which an AI system may have resolved an ambiguity about what the user intended without first obtaining explicit authorization, where that interpretive choice materially affected what happened next.

The unit of analysis is an **incident within a conversation**, not the conversation as a whole and not the user as a whole.

The working SII definition is intentionally narrower than general AI error. A candidate is stronger when all four elements are present:

1. the assumption is machine-generated;
2. it concerns user intent rather than merely factual competence;
3. the interpretation is adopted without explicit authorization;
4. the interpretation materially affects the output, action or workflow.

This distinction is important because some naturalistic failures that initially look like SII are better explained by competence error, false premise, explicit-rule violation, transport failure or meta-extraction behavior.

## 3. Source material

The frozen historical workbook contains 52 candidate records across seven source-window families:

- GPT — 5
- AUD — 22
- CDX — 5
- W38 — 8
- W39 — 7
- KBD — 4
- KPF — 1

These are naturalistic work interactions rather than laboratory prompts created for the study.

The authoritative historical workbook has been recovered and byte-verified at:

- **31,471 bytes**
- SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`

The historical workbook is preserved unchanged. Validation work is additive.

## 4. Extraction procedure

The preserved **IPP Incident Extraction Protocol v1.0** instructs an LLM to act as a neutral forensic extractor rather than as the final analyst.

The extractor searches the source interaction chronologically for events matching one or more predefined triggers:

1. an ambiguous instruction where one interpretation is selected without asking the user;
2. an output later shown not to match the user's intended meaning;
3. an unstated assumption about scope, format, technology, file structure, naming, level of detail or goal;
4. the user having to restate or re-explain intent more than once before correct execution; or
5. work being discarded, rewritten, rolled back or repeated because the AI and user had diverged in interpretation.

The protocol requires transcript-observable evidence and instructs the extractor to:

- preserve exact user wording where available;
- identify reasonable competing interpretations;
- record the interpretation the AI acted upon;
- record whether clarification occurred before action;
- identify the first visible mismatch signal;
- capture observable consequence and resolution;
- retain relevant prior-context links;
- avoid making the researcher-final classification;
- avoid judging severity as scientific fact; and
- include uncertain candidates with a low-confidence flag rather than silently removing them.

## 5. Extraction-layer schema (A1–A13)

| Field | Meaning |
|---|---|
| **A1 LOCATION** | Approximate location of the incident in the source interaction |
| **A2 TASK CONTEXT** | What work was being performed |
| **A3 USER WORDS** | Verbatim or source-preserved triggering instruction |
| **A4 POSSIBLE INTERPRETATIONS** | Reasonable alternative readings |
| **A5 INTERPRETATION CHOSEN** | Reading the AI acted upon |
| **A6 WAS THE USER ASKED?** | Whether clarification was requested before proceeding |
| **A7 ASSUMPTION CONTENT** | The specific unstated assumption inserted by the AI |
| **A8 FIRST VISIBLE SIGNAL OF MISMATCH** | First observable correction, complaint or self-detection |
| **A9 TURNS UNTIL DETECTION** | Delay between interpretive action and visible mismatch |
| **A10 CONSEQUENCE TRACE** | Observable consequence such as rework, rollback, delay or no visible harm |
| **A11 RESOLUTION** | How the incident ended |
| **A12 PRIOR CONTEXT LINKS** | Earlier context relevant to the intended interpretation |
| **A13 CONFIDENCE** | Extraction confidence; not validation status |

The preserved v1 workbook compressed some of these fields rather than representing all of them as dedicated columns. The current audit treats the protocol as the intended schema and records the historical workbook's structural limitations rather than silently repairing history.

## 6. Separation between LLM extraction and researcher classification

The methodology deliberately separates two epistemic roles.

### LLM-assisted extraction

The LLM identifies candidate incidents and records transcript-observable evidence in the A-fields.

### Researcher-only classification

The researcher makes the final Part-C decisions after evidence review. The assistant may prepare recommendations, but those recommendations are not scientific ground truth.

The researcher layer is:

| Field | Meaning | Authority |
|---|---|---|
| **C0 INCIDENT CLASS** | INTENT / COMPETENCE / PREMISE / MIXED / META / control where used | Researcher |
| **C1 IPP TYPE** | Scope, Temporal, Definition/Entity, Authority, Output Form, Abstraction Level, or proposed new type | Researcher |
| **C2 MATERIALITY** | Whether alternative interpretations materially change the outcome | Researcher |
| **C3 CONTEXT FACTOR** | Effect of prior context quality, staleness or conflict | Researcher |
| **C4 EFFECTIVE ICD** | Estimated degree of interpretive authority delegated at that moment | Researcher |
| **C5 TRUE INTENT** | What the user actually meant | **Researcher/user only** |
| **C6 COST ESTIMATE** | Estimated time/work/rework cost | Researcher informed by evidence |
| **C7 HYPOTHESIS RELEVANCE** | Which hypothesis the incident may inform | Researcher |
| **C8 BENCHMARK CANDIDATE** | Whether the incident can become a benchmark item | Researcher |
| **C9 VALIDATION FLAG** | Whether the incident quotation/chronology was checked against sufficient primary interaction evidence | Evidence-gated |
| **C10 NOTES** | Free research notes | Researcher |

The most important methodological constraint is that **C5 TRUE INTENT is not retrospectively inferred by the assistant and promoted to fact**. The person who issued the original instruction is the authority for what they actually meant.

## 7. Verification procedure

An extracted candidate does not become publication-grade evidence merely because an LLM produced a record.

For a candidate to be upgraded to transcript-confirmed evidence, the validation process requires sufficient primary interaction material to check:

- A3, the triggering user wording;
- A5/A6, what the system did and whether clarification preceded action;
- A8, the first visible mismatch signal where applicable; and
- the chronology linking those elements.

Evidence categories are kept separate. An original work order may corroborate A3 without proving A8. A derivative extraction report may preserve a useful reconstruction without being a complete primary transcript. A primary execution fragment may prove tool order without containing the user-side instruction.

Current validation vocabulary includes:

- **CONFIRMED** — sufficient primary interaction evidence supports the quotation and chronology;
- **UNVERIFIED** — candidate or partial evidence exists but the primary interaction record is insufficient;
- **CONTRADICTED** — recovered primary evidence materially conflicts with the extracted record.

No missing source is silently converted into confirmation.

## 8. Two-pass audit of the 52 historical candidates

A later methodological audit reviewed all **52/52** records twice.

### Pass 1 — structural and internal-consistency audit

The audit identified issues including compressed/missing A4 representation, ambiguity between silent action and later disclosure, awareness-gap normalization problems, source-dependent records, and historical machine-suggestion fields that must not be treated as researcher-final classifications.

### Pass 2 — construct-validity audit

The second pass asked a stricter question: *does this record actually evidence Silent Intent Inference, or is another explanation stronger?*

Assistant audit recommendation at this stage:

- **12 — LIKELY SII**
- **11 — POSSIBLE / SOURCE-DEPENDENT**
- **25 — NO / better explained by a comparison class**
- **4 — CONTROL / counter-pattern**

These numbers are **not final researcher labels, not a prevalence estimate and not a claim that 23 records are already validated SII events**. They are an audit queue for final researcher adjudication.

The fact that the audit reduces the presumptive positive set is intentional: the method is designed to allow disconfirmation rather than preserve the original N=52.

## 9. Current primary-evidence status

Autonomous recovery of the currently preserved material is complete.

Current evidence state includes:

- a derivative GPT extraction mapped to all 5 GPT candidates, with its own truncation/compaction limitation disclosed;
- original task artifacts corroborating the triggering instruction/source content for 11 W38/W39/KPF records;
- the exact historical AUD Claude Code session path identified;
- a bounded primary AUD execution fragment recovered from that session, supporting specific execution-order facts for AUD-020 and AUD-021;
- the named historical CDX extraction file referenced by the corpus but not recovered in the current preservation set;
- no sufficiently complete KBD source interaction recovered in the current preservation set.

Under the strict incident-level rule, **C9 CONFIRMED currently remains 0/52** and **C9 CONTRADICTED remains 0/52**. This does not mean the 52 records are false. It means source preservation is incomplete and the current work refuses to substitute derivative material for primary transcript verification.

## 10. Sanitized examples of the audit logic

These examples are included to show how the method distinguishes positive candidates from comparison cases. They are methodological illustrations, not final published observations.

### Example A — likely SII candidate: stale-base assumption

**Structure:** the user explicitly required rebasing/checking against the latest main branch before push. The AI proceeded on the assumption that its existing base remained sufficiently current. A later check showed the stale base would have caused merged work to appear as deletions.

**Why it can qualify:** the error is not merely failure to execute Git. It involves an unstated interpretation of what counted as a sufficiently current baseline under an instruction whose meaning materially affected the outcome.

**Current status:** strong positive candidate; final researcher classification and source-verification status remain separate.

### Example B — likely authority-type candidate: content treated as command

**Structure:** SQL/catalog material was supplied in a context where execution authority had varied across work orders. The AI treated the supplied SQL content as authorization to execute read-only production queries.

**Why it can qualify:** the central issue is whether *content supplied for inspection* was silently interpreted as *permission to act*. This makes the incident potentially useful for an authority/semantic-permission taxonomy.

**Current status:** candidate only until full interaction chronology is available and researcher adjudication is complete.

### Example C — exclusion/comparison case: environment-premise failure

**Structure:** an installation attempt failed because a directory needed by the package manager was not writable.

**Why it should not automatically count as SII:** the stronger explanation is an incorrect premise about the execution environment, not an interpretation of what the user intended.

**Use:** retained as a comparison/exclusion example so the corpus does not redefine every AI failure as SII.

### Example D — counter-pattern/control

**Structure:** when a later audit instruction contained genuine ambiguity, the AI explicitly surfaced multiple readings before committing to one.

**Why it matters:** the absence of silent resolution is analytically useful. It provides a naturalistic comparison case for what the protocol is intended to encourage.

## 11. Main limitations

1. **Single-researcher/self-data context.** The corpus comes from one researcher's own AI-assisted work interactions. It can support mechanism discovery and hypothesis generation, but not population prevalence claims by itself.
2. **LLM-assisted extraction.** The LLM was used as a forensic candidate extractor, not as the final classifier.
3. **Incomplete source preservation.** Not every original source interaction is currently recoverable, so source-verification status must remain explicit.
4. **Researcher-final coding is still being completed.** Assistant recommendations exist for all 52, but final C-fields—especially C5—remain researcher-governed.
5. **Construct contamination is possible.** Competence, premise, explicit-rule and meta cases can resemble SII unless deliberately filtered.
6. **The final positive N is not forced to equal 52.** Exclusion, control and unverified outcomes are legitimate results.
7. **No causal bridge to DCM 2.0 is assumed.** Conceptual compatibility must be tested against the actual variable definitions and coding procedures.

## 12. Proposed CP ↔ DCM 2.0 data-level crosswalk

The possible bridge can be represented as a hypothesis to test rather than as a conclusion:

`interpretive choice → hidden/visible mismatch → consequence → perceived causal attribution → accepted responsibility/burden`

The CP corpus is strongest toward the **left side** of this chain: the interaction mechanics surrounding ambiguity, interpretation, awareness and consequence.

DCM 2.0 appears potentially stronger toward the **right side**: perceived causation, responsibility and burden.

The useful question is therefore not whether the two datasets are already one dataset. It is whether their variables can be mapped without changing what either study actually measured.

### Crosswalk questions

| Dimension | CP corpus | Question for DCM 2.0 |
|---|---|---|
| Unit of observation | incident within an AI interaction | participant, answer, coded episode, or another unit? |
| Primary evidence | interaction record where preserved | interview response, interviewer coding, or both? |
| Upstream event | ambiguous instruction / interpretation / assumption | is the precipitating AI event represented? |
| Awareness | A6/A8/A9 | is recognition timing represented? |
| Consequence | A10 | is practical loss/consequence separate from attribution? |
| Causal attribution | downstream candidate linkage | which variable records who caused the error? |
| Accepted responsibility/burden | not the original CP outcome | which variable records who bears the loss? |
| Ground-truth intent | C5 researcher/user authority | is there an equivalent, or only reported perception? |
| Materiality | C2 | is severity/stake/loss magnitude encoded? |
| Prior experience/context | A12/C3 | is user experience/history represented? |
| Validation | C9 source-verification gate | what coding validation/reliability procedure is used? |
| Temporal sequence | A3 → A5/A6 → A8/A9 → A10/A11 | can DCM variables be positioned in a comparable sequence? |

## 13. Specific questions for Fan

1. What is the exact observational unit in the DCM 2.0 data model?
2. Which variables distinguish perceived **AI causation** from **responsibility/loss accepted by the user**?
3. Is practical consequence represented separately from responsibility attribution?
4. Does the dataset preserve any description or coding of the precipitating AI interaction/failure mode?
5. Is there any variable indicating when the participant became aware that an AI-related failure had occurred?
6. How were qualitative answers coded, and what coder-validation/reliability procedure was used?
7. Which fields can be mapped at the public-data level without exposing participant-level restricted material?
8. Would a small schema-mapping exercise using sanitized examples be a sensible next step before proposing a joint hypothesis or new data collection?

## 14. Present exchange boundary

This note is appropriate for a **methods-first exchange now**.

It does **not** claim:

- that all 52 candidates are validated SII events;
- that 52 is the final positive N;
- that the corpus estimates prevalence;
- that CP and DCM 2.0 already measure the same causal chain; or
- that a formal collaboration design has already been established.

A later version can report researcher-final counts after final adjudication and independent quality control.

---

**Suggested citation/status language for this exchange:**  
*Salama, M. Collaboration Protocol naturalistic incident corpus: methods-status note, 52 extracted candidate records, researcher validation in progress, August 2026.*
