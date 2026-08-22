# Collaboration Protocol Naturalistic Incident Corpus — Complete Methods and 52-Case Exchange Packet

**Prepared for:** Fan Chen-Chieh (Ah-Guang)  
**Prepared by:** Mohamed Salama  
**Date:** 22 August 2026  
**Purpose:** methods-first, data-level comparison with DCM 2.0 public-layer materials  
**Status:** methods-status exchange; researcher-final adjudication is still in progress

---

## 1. What is being shared

This packet is intended to answer the methodological question: **how were the 52 naturalistic candidate incidents extracted, represented, audited and classified?**

It contains:

1. the research object and unit of analysis;
2. the exact extraction logic and A1–A13 schema;
3. the researcher-only C-field framework;
4. the current verification rules;
5. the two-pass audit results;
6. a **sanitized row-level catalog of all 52 historical candidate records**;
7. current evidence status and limitations;
8. the exact preserved extraction prompt used to generate candidate records;
9. the distinction between historical machine suggestions, current assistant audit recommendations and future researcher-final coding; and
10. a proposed CP ↔ DCM 2.0 data-level crosswalk.

The raw project transcripts are **not** included in this exchange packet because they contain private project and operational material. The 52-case catalog below preserves the research-relevant structure while removing unnecessary project-specific details.

The correct present description is **52 extracted candidate incidents**. It is **not** correct to call them 52 validated Silent Intent Inference events.

---

## 2. Research object and unit of analysis

The research object is a possible **Silent Intent Inference (SII)** event: a case in which an AI system may have resolved an ambiguity about what the user intended without first obtaining explicit authorization, where that interpretive choice materially affected the output, action or workflow.

The unit of analysis is an **incident within an AI work conversation**, not the whole conversation and not the user.

A positive SII candidate is strongest when four elements are present:

1. the assumption is machine-generated;
2. it concerns user intent rather than only factual/technical competence;
3. the interpretation is adopted without explicit authorization; and
4. the interpretation materially affects the resulting output, action or workflow.

This is deliberately narrower than “AI error.” Competence mistakes, incorrect environmental premises, explicit-rule violations, transport failures and meta-extraction artifacts can resemble SII and therefore require filtering.

---

## 3. Source material and sampling boundary

The frozen historical workbook contains **52 candidate records across seven source-window families**:

- GPT — 5
- AUD — 22
- CDX — 5
- W38 — 8
- W39 — 7
- KBD — 4
- KPF — 1

The historical workbook has been recovered and byte-verified at:

- **31,471 bytes**
- SHA-256 `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`

The historical workbook is frozen unchanged. Later validation artifacts are additive.

### Sampling limitation

These are naturalistic AI-assisted work interactions, not laboratory prompts and not a probability sample. The preserved archive establishes the seven source-window families that produced the 52 candidate records, but it does **not** establish a denominator of every AI interaction the researcher had during the wider period. Therefore this corpus can support mechanism discovery, taxonomy work and hypothesis generation, but it **cannot by itself estimate population prevalence**.

---

## 4. Extraction procedure

The preserved **IPP Incident Extraction Protocol v1.0** instructed an LLM to act as a neutral forensic extractor rather than as the final analyst.

The extractor searched each conversation chronologically for events matching one or more of five triggers:

1. an instruction reasonably open to more than one interpretation where the AI selected one without asking;
2. an output later shown not to match the user's actual intent;
3. an unstated assumption about scope, format, technology, file structure, naming, detail level or goal;
4. the user having to restate or re-explain the same intent; or
5. work being discarded, rewritten, rolled back or repeated because the AI's interpretation diverged from the user's meaning.

The extraction protocol explicitly required transcript-observable evidence, exact quotations where available, chronological ordering, inclusion of uncertain candidates with LOW confidence, and **no final classification by the extracting LLM**.

---

## 5. Extraction-layer schema — A1 to A13

| Field | Meaning |
|---|---|
| A1 LOCATION | Approximate location of the incident in the source conversation |
| A2 TASK CONTEXT | What work was being performed |
| A3 USER WORDS | Triggering user instruction, intended to be verbatim |
| A4 POSSIBLE INTERPRETATIONS | Reasonable competing readings |
| A5 INTERPRETATION CHOSEN | Reading the AI acted upon |
| A6 WAS THE USER ASKED? | Whether clarification occurred before proceeding |
| A7 ASSUMPTION CONTENT | Specific unstated assumption inserted by the AI |
| A8 FIRST VISIBLE SIGNAL OF MISMATCH | First correction, complaint, or self-detection |
| A9 TURNS UNTIL DETECTION | Delay between interpretive action and visible detection |
| A10 CONSEQUENCE TRACE | Observable rework, rollback, delay, waste, or no visible consequence |
| A11 RESOLUTION | How the incident ended |
| A12 PRIOR CONTEXT LINKS | Earlier context relevant to the intended interpretation |
| A13 CONFIDENCE | Extraction confidence, not validation status |

The preserved v1 workbook compressed some of these fields instead of representing every protocol field as a dedicated column. That structural mismatch is documented rather than silently repaired in the historical artifact.

---

## 6. Researcher classification framework — C0 to C10

The methodology separates **candidate extraction** from **researcher classification**.

| Field | Meaning | Authority |
|---|---|---|
| C0 INCIDENT CLASS | INTENT / COMPETENCE / PREMISE / MIXED / META / control where used | Researcher |
| C1 IPP TYPE | Temporal / Scope / Definition / Authority / Output Form / Abstraction Level / proposed new type | Researcher |
| C2 MATERIALITY | Whether competing readings would materially change the outcome | Researcher |
| C3 CONTEXT FACTOR | Effect of prior context quality, staleness or conflict | Researcher |
| C4 EFFECTIVE ICD | Estimated degree of interpretive authority delegated at that moment | Researcher |
| C5 TRUE INTENT | What the user actually meant | **Researcher/user only** |
| C6 COST ESTIMATE | Estimated time/work/rework cost | Researcher informed by evidence |
| C7 HYPOTHESIS RELEVANCE | H1 / H2 / ICD / other | Researcher |
| C8 BENCHMARK CANDIDATE | Suitability for a future benchmark item | Researcher |
| C9 VALIDATION FLAG | Whether primary interaction evidence verifies the quotations/chronology | Evidence-gated |
| C10 NOTES | Free research notes | Researcher |

### Important authority distinction

The original protocol states that the extracting LLM should **not** perform final Part-C coding. During the later audit, an assistant generated **recommendations** for all 52 records to help the researcher review them. Those recommendations are clearly separated from researcher-final fields. They do not become human-coded ground truth merely because they are systematic.

**C5 TRUE INTENT is especially protected:** the assistant does not retrospectively infer what the user “really meant” and promote that inference to scientific fact.

---

## 7. Verification rule

A candidate record is not considered transcript-confirmed merely because an extraction exists.

For C9 `CONFIRMED`, sufficient primary interaction evidence must allow checking of:

- A3 — the triggering user wording;
- A5/A6 — what the system did and whether clarification preceded action;
- A8 — the first visible mismatch signal, when applicable; and
- chronology linking those elements.

Evidence classes are kept separate. An original task artifact may corroborate A3 without proving A8. A derivative extraction can preserve useful structure without being a primary transcript. A primary execution fragment may prove tool order without containing the user's instruction.

Current validation vocabulary:

- `CONFIRMED` — sufficient primary interaction evidence supports quotation and chronology;
- `UNVERIFIED` — candidate or partial evidence exists, but primary evidence is insufficient;
- `CONTRADICTED` — recovered primary evidence materially conflicts with the extracted record.

No missing source is silently converted into confirmation.

---

## 8. Two-pass audit of all 52 historical candidates

All **52/52** historical records were reviewed twice.

### Pass 1 — structural/internal-consistency audit

The audit identified issues including:

- missing/compressed representation of A4 in the historical workbook;
- ambiguity between “silent at decision time” and later same-reply disclosure;
- awareness-gap values requiring normalization;
- source-dependent records;
- historical machine-suggestion fields that must not be treated as researcher-final coding;
- records that are better treated as controls or exclusions.

### Pass 2 — construct-validity audit

The stricter pass asked whether each row actually appears to evidence SII rather than competence error, premise error, explicit-rule failure, meta behavior or a counter-pattern.

Current **assistant audit recommendation**, not researcher-final result:

- **12 — LIKELY SII**
- **11 — POSSIBLE / SOURCE-DEPENDENT**
- **25 — NO / better explained by a comparison class**
- **4 — CONTROL / counter-pattern**

These are not prevalence figures and are not final human labels. The reduction from 52 presumptive candidates is a feature of the validation process: the method permits disconfirmation instead of forcing the original N to survive.

---

# 9. Sanitized catalog of all 52 historical candidate records

The table below shows every historical record at a data-review level while omitting unnecessary private implementation details and verbatim project-sensitive content.

**Status meanings:** `LIKELY`, `POSSIBLE`, `NO`, and `CONTROL` are current assistant audit recommendations only. `C9` remains UNVERIFIED for all rows pending sufficient primary-interaction verification.

| ID | Family | Sanitized incident summary | Current construct recommendation | Provisional type/comparison class | Best current evidence state |
|---|---|---|---|---|---|
| GPT-001 | GPT | A standing governance instruction was treated as authority to dispatch new work while the execution window was already occupied. | LIKELY | Standing-instruction / intent | Derivative source extract only |
| GPT-002 | GPT | A status synthesis used only one of two supplied workstream handbacks, requiring the user to demand a reread. | NO | Competence/omission | Derivative source extract only |
| GPT-003 | GPT | A multi-step coordination reply mixed actions that could happen immediately with actions dependent on another window, leaving sequencing unclear. | LIKELY | Temporal intent | Derivative source extract only |
| GPT-004 | GPT | An open-ended request for useful vendor questions was expanded into a very large diligence questionnaire when the user wanted a short urgent screen. | POSSIBLE | Abstraction-level intent | Derivative source extract only |
| GPT-005 | GPT | A one-page external brief reused stale project scope instead of revalidating against the new audience/context. | LIKELY | Scope intent | Derivative source extract only |
| AUD-001 | AUD | Source-declared database columns were treated as if they were proven live production schema, forcing a full specification rewrite. | NO | Competence | Primary family source incomplete |
| AUD-002 | AUD | Two contradictory rules were allowed to coexist in a specification rather than being reconciled. | NO | Competence | Primary family source incomplete |
| AUD-003 | AUD | Invalid SQL uniqueness syntax was treated as valid until corrected. | NO | Competence | Primary family source incomplete |
| AUD-004 | AUD | Inline chat transport was assumed to preserve an artifact byte-for-byte; the received artifact failed fingerprint checks. | NO | Premise | Primary family source incomplete |
| AUD-005 | AUD | A byte/line discrepancy was attributed to blank-line loss without enough evidence, and the claim later had to be withdrawn. | NO | Competence | Primary family source incomplete |
| AUD-006 | AUD | An observation from one execution context was generalized to a different production service context. | NO | Competence | Primary family source incomplete |
| AUD-007 | AUD | A blocking-lock mechanism was described as compatible with a non-blocking concurrency claim. | NO | Competence | Primary family source incomplete |
| AUD-008 | AUD | A data structure recording alert intent was treated as if it proved the complete operational alert capability. | NO | Competence | Primary family source incomplete |
| AUD-009 | AUD | The word “additive” was interpreted as net-new capability even though the stage also contained revocations/backfills/destructive changes. | LIKELY | Definition intent | Primary family source incomplete |
| AUD-010 | AUD | A design problem was reduced to a false binary choice even though the user's intended decision space contained more options. | NO | Competence/modeling | Primary family source incomplete |
| AUD-011 | AUD | “Byte-identical” was silently interpreted to mean preservation of existing values despite new populated fields changing the row. | LIKELY | Definition intent | Primary family source incomplete |
| AUD-012 | AUD | A fingerprinted artifact was treated as unavailable because the retrievable attachment was not recognized at that moment. | NO | Premise | Primary family source incomplete |
| AUD-013 | AUD | Context lines from a search command were counted as mutation sites, producing a false inventory discrepancy. | NO | Competence | Primary family source incomplete |
| AUD-014 | AUD | A pinned review head was assumed still current without a final currency check, causing a review of the wrong revision. | NO | Competence/process | Primary family source incomplete |
| AUD-015 | AUD | An approval threshold was interpreted strictly, but no observable user mismatch followed; retained as a comparison record. | CONTROL | Counter-pattern / threshold | Primary family source incomplete |
| AUD-016 | AUD | A later attached artifact was again treated as missing because its identity/digest could not be matched to a delivered file. | NO | Premise | Primary family source incomplete |
| AUD-017 | AUD | Two plausible interpretations of a diff-count convention were explicitly disclosed rather than silently choosing one. | CONTROL | Surfaced ambiguity | Primary family source incomplete |
| AUD-018 | AUD | The extraction instruction itself was interpreted to include a raw transcript recovered from disk rather than only retained chat context. | NO | Meta | Primary family source incomplete |
| AUD-019 | AUD | A persistent role/header convention was retained while executing the neutral-extractor instruction. | NO | Meta | Primary family source incomplete |
| AUD-020 | AUD | Permission for a read-only probe was interpreted narrowly: existing surfaces were searched, but no new request path was constructed. | POSSIBLE | Authority intent | Primary execution fragment corroborates behavior |
| AUD-021 | AUD | A prohibition on calling user-defined functions before inspection was interpreted as excluding platform helper functions; they were called before their definitions were inspected, then the deviation was disclosed. | LIKELY | Definition intent | Primary execution sequence and disclosure partly corroborated |
| AUD-022 | AUD | Multiple ambiguities were surfaced explicitly before commitment, producing no rework; retained as an inverse/counter-pattern. | CONTROL | Counter-pattern | Primary family source incomplete |
| CDX-001 | CDX | A branch instruction was interpreted as permitting a fresh clone because the expected repository was not at the current working path. | NO | Premise | Named historical extract not recovered |
| CDX-002 | CDX | A “proof” requirement was interpreted as satisfiable with focused pure checks and source assertions. | POSSIBLE | Output-form intent | Named historical extract not recovered |
| CDX-003 | CDX | A requirement involving deterministic action IDs was interpreted as needing handling changes but no separate generation change. | POSSIBLE | Scope intent | Named historical extract not recovered |
| CDX-004 | CDX | “Not merged” was interpreted as still permitting a push of the unmerged handoff branch. | POSSIBLE | Authority intent | Named historical extract not recovered |
| CDX-005 | CDX | The extraction protocol attachment was interpreted as applying to the current thread and as authorizing creation of the named extraction file. | NO | Meta | Named historical extract not recovered |
| W38-001 | W38 | A strict rebase-before-push rule was not followed as main advanced, creating a stale-base deletion risk. | NO | Competence/process | Triggering task artifact corroborated |
| W38-002 | W38 | An intentionally failing proof suite was interpreted as something that should remain outside default CI discovery. | POSSIBLE | Scope intent | Triggering task artifact corroborated |
| W38-003 | W38 | Passing one ordinary reproduction shape was treated as disproving a broader failure class that actually required multiple shapes. | LIKELY | Scope intent | Triggering task artifact corroborated |
| W38-004 | W38 | A seven-case proof order was interpreted as permitting creation of a new dedicated proof file even though no filename was specified. | POSSIBLE | Output-form intent | Triggering task artifact corroborated |
| W38-005 | W38 | “Mirror the real tenant exactly” was interpreted as requiring exact values but not a timestamp/hash provenance record. | POSSIBLE | Definition intent | Triggering task artifact corroborated |
| W38-006 | W38 | A requirement that defect assertions be “marked” was interpreted as satisfied by names/footer rather than an adjacent greppable label on each assertion. | LIKELY | Output-form intent | Triggering task artifact corroborated |
| W38-007 | W38 | A timestamp proxy was disclosed before use and no later mismatch occurred; retained as a surfaced-resolution comparison. | CONTROL | Disclosed-proceed counter-pattern | Source interaction not recovered |
| W38-008 | W38 | Type checking and building were run concurrently, causing transient generated-file errors that disappeared when rerun sequentially. | NO | Competence | Source interaction not recovered |
| W39-001 | W39 | A branch was allowed to become stale despite a rebase-before-push rule, again creating deletion risk. | NO | Competence/process | Triggering task artifact corroborated |
| W39-002 | W39 | Local configuration approximations were used as a stand-in for production values before a frozen fixture existed. | POSSIBLE | Scope intent | Triggering source wording incomplete |
| W39-003 | W39 | “Correct only these six call sites” was treated as excluding five other contract mismatches even though another instruction also said to verify every argument. | LIKELY | Scope intent | Triggering task artifact corroborated |
| W39-004 | W39 | “Deliver the complete corrected file” was interpreted as satisfied by a local path/link rather than an actual transferable artifact. | LIKELY | Mixed output-form/premise | Triggering task artifact corroborated |
| W39-005 | W39 | A bare attachment/request label was interpreted conservatively as permission to inspect/compare but not to edit or execute. | POSSIBLE | Authority intent | Source interaction not recovered |
| W39-006 | W39 | “Send only three things” was interpreted as restricting only the final handback, not progress commentary during execution. | POSSIBLE | Scope intent | Source interaction not recovered |
| W39-007 | W39 | SQL content supplied without an explicit imperative was treated as authorization to execute read-only production queries. | LIKELY | Authority intent | Source content corroborated; chronology incomplete |
| KBD-001 | KBD | An installation authorization was assumed to cover all filesystem paths the package manager would need, but a required path was not writable. | NO | Premise | Not found in current preservation scope |
| KBD-002 | KBD | A browser-authentication flow relied on terminal/tool output to expose a one-time code that the user could not actually see. | NO | Premise/interface | Not found in current preservation scope |
| KBD-003 | KBD | Authorization for a child configuration path was assumed sufficient even though its parent directory did not exist and could not be created. | NO | Premise | Not found in current preservation scope |
| KBD-004 | KBD | A requested outcome (“one commit and one draft PR”) was silently treated as requiring a particular local CLI authentication method, stalling the task for several exchanges. | LIKELY | Abstraction/means-vs-outcome intent | Not found in current preservation scope |
| KPF-001 | KPF | A strict rebase/no-deletion rule was not kept current as main advanced, creating another stale-base deletion risk. | NO | Competence/process | Triggering task artifact corroborated |

### Catalog totals

- total historical candidates: **52**
- current assistant recommendation `LIKELY`: **12**
- current assistant recommendation `POSSIBLE`: **11**
- current assistant recommendation `NO`: **25**
- current assistant recommendation `CONTROL`: **4**
- researcher-final adjudicated positive N: **not yet established**

---

## 10. Current primary-evidence status

Autonomous recovery of the currently preserved material is complete.

The current evidence state includes:

- a derivative GPT extraction mapped to all 5 GPT candidates, with truncation/compaction limitations disclosed by that extract;
- original task artifacts corroborating triggering instructions/source content for 11 W38/W39/KPF records;
- the exact historical AUD session path identified;
- a bounded primary AUD execution fragment supporting specific execution-order facts for AUD-020 and AUD-021;
- a preserved assistant handback additionally corroborating AUD-021's same-reply disclosure;
- the named historical CDX extraction file referenced by the corpus but not recovered;
- no sufficiently complete KBD source interaction recovered in the present preservation set.

Under the strict incident-level rule:

- **C9 CONFIRMED: 0/52**
- **C9 CONTRADICTED: 0/52**

This does **not** mean the 52 records are false. It means source preservation is incomplete and the current methodology refuses to treat derivative evidence as primary transcript verification.

---

## 11. Human-coding and reliability status

The protocol was designed around **researcher-final coding by the user/researcher who issued the original instructions**. That is particularly important for C5 TRUE INTENT.

At the present methods-exchange stage:

- assistant audit recommendations exist for all 52;
- researcher-final adjudication is still in progress;
- **no independent second-human-coder inter-rater reliability statistic has yet been produced**;
- therefore no Cohen's kappa, Krippendorff's alpha, or similar reliability result is claimed.

This is a current limitation and a possible future methodological improvement if the corpus is developed into a publication-grade benchmark or study dataset.

---

## 12. Data-sharing and privacy boundary

The source conversations contain private project material, operational details and potentially identifying context. For this methods exchange:

- the exact methodology is shared;
- the full 52-case **sanitized catalog** is shared;
- private raw transcripts are not being transmitted by default;
- researcher-final C5 intent statements are not yet shared because they have not been completed;
- specific primary-source excerpts can be considered later where they can be safely de-identified and where doing so materially improves the data-level comparison.

This boundary is intended to preserve auditability without making raw operational conversations a prerequisite for a first methods comparison.

---

## 13. Exact preserved extraction prompt

The following is the substantive Part A prompt from **IPP Incident Extraction Protocol v1.0**, preserved as the extraction instruction used for the naturalistic-corpus workstream.

```text
You are performing a forensic extraction task on our own conversation history in this chat window. You are acting as a neutral court reporter, NOT as an analyst, NOT as a judge, and NOT as a participant defending your past behavior.

TASK
Go through our entire conversation in this window from the beginning. Identify every incident where any of the following occurred:

1. I gave you an instruction or request that could reasonably be interpreted in more than one way, and you chose one interpretation WITHOUT asking me which one I meant.
2. Your output did not match what I actually intended, and this became visible later (I corrected you, expressed frustration, asked you to redo something, restarted the task, or abandoned the approach).
3. You made an assumption about scope, format, technology choice, file structure, naming, level of detail, or goal that I never stated.
4. I had to restate, rephrase, or re-explain the same intent more than once before you acted on it correctly.
5. Work was discarded, rewritten, or rolled back because your interpretation of my words diverged from my meaning.

STRICT RULES
- Report ONLY what is observable in the transcript. Quote the exact words. Do not paraphrase quotes.
- Do NOT explain why you made the assumption. Do NOT justify, apologize for, or evaluate your past behavior. Do NOT rate severity. Do NOT classify the incident type. Those judgments are reserved for the researcher.
- If you are uncertain whether something qualifies as an incident, INCLUDE it and mark CONFIDENCE: LOW. Over-inclusion is acceptable; omission is not.
- Number incidents sequentially: INC-001, INC-002, ...
- If the conversation contains zero qualifying incidents, state that explicitly and describe what kinds of ambiguity DID appear and how they were resolved.
- Work chronologically from the start of the conversation to the end.

OUTPUT FORMAT
For every incident, produce one record using EXACTLY this template, with every field present (write "NOT OBSERVABLE" if the transcript does not show it):

=== INC-[number] ===
A1. LOCATION: [approximate position in conversation: beginning / early middle / middle / late middle / end, plus any message reference you can give]
A2. TASK CONTEXT: [one sentence: what were we working on at that moment]
A3. USER WORDS (VERBATIM): "[my exact words that contained the ambiguity or instruction]"
A4. POSSIBLE INTERPRETATIONS: [list every reasonable reading of those words — minimum 2 if the instruction was ambiguous]
A5. INTERPRETATION CHOSEN: [which reading you acted on]
A6. WAS THE USER ASKED?: [YES — quote your clarifying question / NO — you proceeded silently]
A7. ASSUMPTION CONTENT: [the specific unstated assumption(s) you inserted, stated plainly]
A8. FIRST VISIBLE SIGNAL OF MISMATCH: "[verbatim quote of the first message where the mismatch surfaced — my correction, complaint, or your own detection]"
A9. TURNS UNTIL DETECTION: [how many message exchanges passed between the interpretation (A5) and the detection (A8)]
A10. CONSEQUENCE TRACE: [observable results only: code rewritten, file restarted, feature abandoned, approach reversed, duplicated work, error introduced, none visible]
A11. RESOLUTION: [how it ended: user re-explained / user accepted wrong version / task restarted / never resolved / other — describe factually]
A12. PRIOR CONTEXT LINKS: [earlier messages in this window that were relevant to interpreting A3 — did earlier context exist that pointed to the correct meaning? Quote briefly or state NONE]
A13. CONFIDENCE: [HIGH / MEDIUM / LOW — your confidence that this qualifies as an intent-interpretation incident]
=== END INC-[number] ===

After the final incident, add a footer:

=== WINDOW SUMMARY ===
TOTAL INCIDENTS: [n]
CONVERSATION SPAN: [approximate total length: number of exchanges or your best estimate]
DOMINANT TASK TYPES: [coding / debugging / architecture / documentation / other]
EXTRACTION LIMITATIONS: [anything that prevented complete extraction: truncated history, lost context, summarized memory, etc.]
=== END SUMMARY ===

Begin the extraction now.
```

---

## 14. Original researcher-only classification block

The preserved protocol then instructed the researcher to append the following block **after collection**, rather than delegating final classification to the extracting LLM:

```text
C1. IPP TYPE: [Temporal / Scope / Definition / Authority / Output Form / Abstraction Level / NEW TYPE — name it]
C2. MATERIALITY: [Material / Trivial — per your Semantic Materiality Proxy: would the interpretations have led to substantially different outcomes?]
C3. CONTEXT FACTOR: [1.0 no relevant prior context / 1.25 weak or stale context / 1.5 conflicting context — based on A12]
C4. EFFECTIVE ICD AT THE TIME: [0.0–1.0 — how much resolution authority had you implicitly delegated at that moment?]
C5. TRUE INTENT (GROUND TRUTH): [what you actually meant — you are the only valid source for this field]
C6. COST ESTIMATE: [minutes/hours lost, lines of code discarded, number of restarts — your estimate]
C7. HYPOTHESIS RELEVANCE: [H1 prevalence / H2 awareness gap / ICD effect / other]
C8. BENCHMARK CANDIDATE: [YES / NO — could this incident be converted into an IFI-Bench test item?]
C9. VALIDATION FLAG: [CONFIRMED — you verified the quotes against the actual transcript / UNVERIFIED]
C10. NOTES: [free text]
```

A later audit added a recommended **C0 incident-class filter** (`INTENT / COMPETENCE / PREMISE / MIXED / META / CONTROL`) because a corpus created from failure-oriented extraction triggers can otherwise make competence or premise failures look like intent failures. Only INTENT/MIXED records should automatically remain candidates for positive SII analysis; other classes serve as exclusions or comparisons unless the researcher rules otherwise.

---

## 15. Original corpus quality rules

The preserved protocol specifies:

1. verify A3 and A8 quotes against the real transcript before setting C9 `CONFIRMED`;
2. keep one incident per record even when it has multiple downstream consequences;
3. retain cross-window recurrence and link duplicates rather than deleting them;
4. do not remove embarrassing cases merely because the user's instruction itself was poor;
5. preserve raw extraction outputs unchanged and classify in copies; and
6. disclose that extraction was LLM-assisted, classification was researcher-performed, and the corpus is single-user/single-project evidence of mechanism rather than population prevalence.

---

## 16. Historical versus current classification state

Three layers must not be conflated:

1. **Historical candidate/extraction fields** — what was stored in the original v1 corpus, including some machine-suggested labels.
2. **Current assistant audit recommendations** — the later two-pass review that currently yields 12 LIKELY, 11 POSSIBLE, 25 NO and 4 CONTROL.
3. **Researcher-final classifications** — not yet complete; C5 remains exclusively researcher-supplied and C9 remains evidence-gated.

The exchange packet deliberately exposes this distinction because collapsing these layers would exaggerate the empirical maturity of the corpus.

---

## 17. Main limitations

1. **Single-researcher/self-data context.** The corpus comes from one researcher's own AI-assisted work.
2. **Non-probability sampling / denominator not established.** The 52 cases do not estimate prevalence across all AI interactions.
3. **LLM-assisted extraction.** Candidate discovery used an LLM under a fixed forensic prompt.
4. **Incomplete source preservation.** Not every original source interaction remains independently recoverable.
5. **Researcher-final coding incomplete.** Assistant recommendations are not final ground truth.
6. **No second-human-coder reliability statistic yet.** Inter-rater reliability has not yet been measured.
7. **Construct contamination risk.** Competence, premise and meta failures can resemble SII unless filtered.
8. **Final positive N is not forced to remain 52.** Exclusion and control outcomes are legitimate.
9. **No causal bridge to DCM 2.0 is assumed.** Compatibility must be established from actual variables and coding procedures.
10. **Raw project transcripts are privacy-restricted for this first exchange.** The sanitized catalog is the current shareable data-level representation.

---

## 18. Proposed CP ↔ DCM 2.0 data-level crosswalk

The possible bridge should be tested, not assumed:

`interpretive choice → hidden/visible mismatch → consequence → perceived causal attribution → accepted responsibility/burden`

The CP corpus is strongest toward the **left side** of this chain: ambiguity, interpretation, awareness and consequence.

DCM 2.0 appears potentially stronger toward the **right side**: perceived causation, responsibility and burden.

| Dimension | CP corpus | Question for DCM 2.0 |
|---|---|---|
| Unit of observation | incident within an AI interaction | participant, answer, coded episode, or another object? |
| Primary evidence | interaction record where preserved | interview response, interviewer coding, or both? |
| Upstream event | ambiguous instruction / interpretation / assumption | is the precipitating AI event represented? |
| Awareness | A6/A8/A9 | is recognition timing represented? |
| Consequence | A10 | is practical loss/consequence separated from attribution? |
| Causal attribution | downstream candidate linkage | which field records who caused the error? |
| Accepted responsibility/burden | not original CP outcome | which field records who bears the loss? |
| Ground-truth intent | C5 researcher/user authority | is there an equivalent, or only reported perception? |
| Materiality | C2 | is severity/stake/loss magnitude encoded? |
| Context/history | A12/C3 | is prior experience/context represented? |
| Validation | C9 primary-source gate | what coder-validation/reliability procedure is used? |
| Temporal order | A3 → A5/A6 → A8/A9 → A10/A11 | can DCM observations be positioned in a comparable sequence? |

---

## 19. Specific questions for Fan

1. What is the exact observational unit in the DCM 2.0 data model?
2. Which variables distinguish perceived **AI causation** from **responsibility/loss accepted by the user**?
3. Is practical consequence represented separately from responsibility attribution?
4. Does the dataset preserve any description or coding of the precipitating AI interaction or failure mode?
5. Is there a variable indicating when the participant became aware that an AI-related failure had occurred?
6. How were qualitative answers coded, and what coder-validation/reliability procedure was used?
7. Which fields can be mapped at the public-data level without exposing restricted participant material?
8. Would a small schema-mapping exercise using a few sanitized incidents from the 52-case catalog be a sensible next step before proposing a joint hypothesis or new data collection?

---

## 20. Present exchange boundary

This packet is suitable for a **methods-first exchange now**.

It does **not** claim:

- 52 validated SII events;
- a final positive N of 52;
- a population prevalence estimate;
- completed researcher-final coding;
- completed inter-rater reliability;
- complete source-transcript preservation; or
- an already-proven causal bridge between CP and DCM 2.0.

A later version can report researcher-final counts after adjudication and independent quality control.

---

**Suggested status citation for this exchange:**  
*Salama, M. Collaboration Protocol naturalistic incident corpus: methods-status packet, 52 extracted candidate records with sanitized row-level catalog; researcher validation in progress, August 2026.*
