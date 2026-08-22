# Methods Note — CP Naturalistic Incident Corpus

## 1. Research object

The naturalistic corpus is designed to identify **candidate episodes of Silent Intent Inference (SII)** in real AI-assisted work.

For this program, the working SII construct is a machine-generated assumption about what the user intends, made without explicit authorization, that materially affects the resulting action or output. The validation process must distinguish this from ordinary factual error, technical incompetence, an incorrect premise, transport/tool failure, and benign counter-patterns in which ambiguity is surfaced or disclosed appropriately.

The unit of analysis is an **incident within a conversation**, not a whole conversation and not a user.

## 2. Source material

The preserved historical workbook contains 52 extracted candidate records across seven source-window families:

| Family | Candidate records |
|---|---:|
| GPT | 5 |
| AUD | 22 |
| CDX | 5 |
| W38 | 8 |
| W39 | 7 |
| KBD | 4 |
| KPF | 1 |
| **Total** | **52** |

These were drawn from naturalistic AI-assisted project work rather than laboratory prompts. This gives the corpus ecological richness but also creates important selection, privacy, dependence, and reproducibility limitations described in `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`.

## 3. Historical extraction procedure

The preserved **IPP Incident Extraction Protocol v1.0** instructs an LLM to behave as a forensic extractor rather than as the final analyst.

The extractor scans a source conversation chronologically for observable candidate episodes meeting one or more of five triggers:

1. an ambiguous instruction is followed by one interpretation without clarification;
2. a mismatch becomes visible later;
3. an unstated assumption is introduced about scope, format, technology, file structure, naming, level of detail, or goal;
4. the user must restate or re-explain intent; or
5. work is discarded, reworked, or rolled back after interpretations diverge.

The extraction protocol requires exact transcript quotations, chronological ordering, explicit uncertainty, and all A-fields. It prohibits the extractor from treating its own judgment as researcher-final incident classification.

Long source windows may be divided into segments for extraction, but the resulting incidents are still treated as candidates requiring later source verification.

## 4. A1–A13 extraction layer

For every candidate, the protocol records:

`location → task context → user words → possible interpretations → interpretation chosen → clarification status → assumption → first mismatch → detection delay → consequence → resolution → prior context → extraction confidence`

The detailed field definitions are in `02_SCHEMA_AND_CODEBOOK.md`.

A key preservation defect was discovered during the present audit: **A4 Possible Interpretations is required by the protocol but is not represented as a dedicated column in the historical v1 workbook.** A recovered GPT extraction report preserves A4 for its five rows, but the workbook should not be represented as a perfect serialization of every protocol field.

## 5. Separation of extraction, audit, and classification

The research design now uses four distinct stages.

### Stage A — LLM-assisted candidate extraction

The LLM records the A-fields from the source interaction under the forensic protocol. This is candidate generation, not ground truth.

### Stage B — structural and construct-validity audit

A later assistant audit checks whether the candidate record is internally complete and whether the described event is actually plausible as an intent-interpretation event rather than a competence, premise, transport, or meta artifact.

The current two-pass audit produced:

- **12 LIKELY SII** candidates;
- **11 POSSIBLE / source-dependent** candidates;
- **25 NO / better explained by a comparison class** candidates;
- **4 CONTROL / counter-pattern** records.

These are assistant recommendations for researcher review, not final results.

### Stage C — primary-source verification

A candidate is not upgraded merely because the workbook contains a verbatim-looking quotation. The validation rule requires checking the relevant source interaction where it is available, especially:

- A3 user wording;
- A8 first visible mismatch/disclosure where applicable; and
- the event chronology connecting interpretation to consequence.

Different evidence classes are preserved separately. For example, an original work order can corroborate A3 while still being insufficient to prove the later mismatch. A primary execution fragment can prove an action sequence while still lacking the original user instruction.

At the end of the autonomous recovery pass, no row meets the project's full C9 `CONFIRMED` threshold. This is an evidence-access result, not a claim that the extracted quotations are false.

### Stage D — researcher adjudication

The researcher reviews the evidence and either accepts, overrides, or defers the assistant recommendation. The researcher completes the original C1–C10 fields. A validation-helper C0 incident class is also used in the current workstream to separate INTENT, COMPETENCE, PREMISE, MIXED, META, and control/comparison cases before SII-specific analysis.

Most importantly, **C5 TRUE INTENT is reserved to the researcher who issued the original instruction**. An assistant may propose what seems likely from the transcript, but that cannot become scientific ground truth without the researcher's decision.

## 6. Quote and source-verification procedure

For each incident:

1. identify the source family and best available primary/derivative evidence;
2. map the candidate A3, A5, A8 and chronology to that evidence;
3. keep task-artifact corroboration, execution-behavior corroboration, and complete interaction verification as distinct evidence classes;
4. mark C9 `CONFIRMED` only if sufficient primary interaction evidence supports the quotation and chronology;
5. mark unresolved cases explicitly `UNVERIFIED` rather than inferring confirmation;
6. preserve source contradictions if discovered; and
7. never force the final analytic sample to remain 52.

The current source-recovery register is maintained in `../QUOTE_VERIFICATION_REGISTER.md` and `../SOURCE_CONVERSATION_AVAILABILITY.md`.

## 7. Exclusion and comparison logic

The extraction protocol intentionally over-includes plausible candidates. Validation therefore needs negative cases as well as positives.

A record should not count as SII merely because the AI did something wrong. A positive SII classification should require, at minimum:

- an interpretation about **user intent** rather than a purely factual/technical proposition;
- lack of explicit authorization for that interpretation at the relevant decision moment;
- a meaningful alternative interpretation or unresolved ambiguity;
- material effect on output/action; and
- enough evidence to separate the mechanism from an ordinary competence or premise failure.

Control/counter-pattern records are retained because they show cases where ambiguity was surfaced, disclosed, or handled without the harmful silent-resolution pattern. They are useful for falsifiability and future benchmark design.

## 8. Current validation state

The correct current description is:

> **A 52-record candidate naturalistic corpus extracted with an LLM under a fixed forensic protocol, fully structurally/construct audited by the present workstream, with assistant classification recommendations prepared for all 52, but with researcher-final adjudication and full primary-source verification still incomplete.**

It is not scientifically defensible at this stage to call the set “52 validated SII events.”

## 9. Intended use in the DCM 2.0 exchange

The immediate aim is not to merge the two studies or assert that they measure the same construct.

The aim is to compare at the data-model level:

- unit of observation;
- directly observed versus inferred variables;
- precipitating event versus downstream attribution;
- awareness/detection timing;
- consequence or loss;
- causal attribution versus accepted responsibility/burden;
- experience/context variables;
- coding/verification procedures; and
- what temporal or causal linkage can and cannot be inferred.

The possible bridge is therefore a **research question**, not a finding:

`interpretation event → hidden/visible mismatch → consequence → causal attribution → accepted responsibility/burden`

CP's incident corpus is designed mainly around the left side of that chain. Fan's field study, based on the information exchanged in correspondence, appears to contain variables on the right side. `03_DCM2_CROSSWALK_TEMPLATE.md` is designed to test whether those levels can be connected without collapsing distinct constructs.

## 10. Reproducibility and disclosure language

Any academic description of this corpus should disclose that:

- candidate extraction was LLM-assisted;
- final coding is researcher-controlled;
- the data come from one researcher's naturalistic work interactions;
- source preservation is incomplete across families;
- records are not independent observations of a population;
- the extraction set deliberately contains later-excluded comparison cases; and
- all reported counts must distinguish candidate, audited, source-verified, researcher-final, and analyzable records.
