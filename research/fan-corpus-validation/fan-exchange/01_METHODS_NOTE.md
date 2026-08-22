# Methods Note — CP Naturalistic Incident Corpus

## 1. Research object
The corpus is designed to capture episodes in which an AI system may have resolved a materially ambiguous user instruction without explicit clarification, or where an interpretation mismatch later became observable.

The unit of analysis is an incident record, not a whole conversation.

## 2. Source material
The preserved candidate corpus contains 52 extracted records from seven source-window families:

- GPT — 5
- AUD — 22
- CDX — 5
- W38 — 8
- W39 — 7
- KBD — 4
- KPF — 1

These are naturalistic work conversations rather than laboratory prompts.

## 3. Extraction procedure
The preserved IPP Incident Extraction Protocol instructs an LLM to act as a neutral forensic extractor rather than an analyst. It searches the conversation chronologically for observable events matching predefined inclusion criteria, including:

1. ambiguous instructions where one interpretation was selected without asking the user;
2. outputs later shown not to match the user's intended meaning;
3. unstated assumptions about scope, format, technology, structure, naming, detail, or goal;
4. repeated restatement or re-explanation before correct execution; and
5. work discarded, rewritten, or rolled back after an interpretation mismatch.

The extractor is instructed to quote transcript evidence, avoid judging severity, avoid assigning the final incident taxonomy, and over-include uncertain candidates with a low-confidence label rather than silently omit them.

## 4. Separation of extraction and classification
The design intentionally separates two epistemic roles:

### LLM-assisted extraction
The LLM records observable transcript evidence in fields A1–A13.

### Researcher-only classification
The researcher assigns the C-fields after reviewing the evidence. These include incident type, materiality, contextual factors, delegated interpretation authority, ground-truth intent, cost, hypothesis relevance, benchmark suitability, and validation status.

Ground-truth intent cannot be inferred retrospectively by the assistant as scientific fact; it is reserved to the researcher who issued the original instruction.

## 5. Verification requirement
A candidate incident does not become verified research evidence merely because an extraction record exists.

For publication-grade use:
- quoted user wording must be checked against the original transcript;
- the first visible mismatch must be checked against the original transcript;
- the researcher-final classification must be completed;
- unresolved source-access gaps remain explicitly labeled;
- competence errors, premise errors, mixed cases, and meta-extraction artifacts must not automatically count as Silent Intent Inference.

## 6. Current validation state
The archive preserves 52 extracted candidate records and the full extraction/classification protocol. Researcher-final classification and source-verification remain incomplete in the preserved historical version.

The current workstream is therefore validating the corpus rather than retroactively claiming that all 52 were already ground truth.

## 7. Intended use in the DCM 2.0 exchange
The immediate aim is not to merge the two studies or assert that they measure the same construct.

The aim is to compare, at the data-model level:
- what event each dataset treats as the unit of observation;
- what is directly observed versus inferred;
- where responsibility, interpretation, consequence, and attribution appear in each schema;
- what temporal sequence each dataset captures;
- and whether a defensible linkage exists between upstream interpretation events and downstream responsibility/consequence observations.

Only after that mapping should a joint hypothesis or study design be proposed.
