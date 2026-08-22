# IPP Incident Extraction Protocol v1.0
### For mining LLM chat histories for Silent Intent Inference events
**Author: Mohamed Salama — The Collaboration Protocol research program**

---

## How to use this document

1. Open each LLM chat window you worked with during your coding project.
2. Paste **Part A (Extraction Prompt)** exactly as written into the window.
3. The LLM will return incident records in the fixed format defined in **Part B**.
4. Save each window's output as a separate file named: `extract_[tool]_[window#]_[date].md` (example: `extract_claude_w3_2026-07-30.md`).
5. Do NOT let the LLM classify or judge incidents. Classification fields (Section C of each record) are completed by YOU only, later, against your IPP taxonomy.
6. If a window's history is too long, run the prompt in segments: "Apply the extraction protocol to the first third of our conversation," then the second, then the third. Keep incident numbering continuous.

---

## PART A — EXTRACTION PROMPT (paste this into each LLM window)

```
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

## PART B — FIELD DEFINITIONS (for your reference)

| Field | What it captures | Maps to your construct |
|---|---|---|
| A3 | The ambiguous instruction, verbatim | The IPP site itself |
| A4 | The branch space | IPP — "meaning may branch" |
| A5 + A6 | Silent resolution vs. surfaced | **Silent Intent Inference** (A6=NO is your core phenomenon) |
| A7 | The inserted assumption | Non-Assumption Principle (Law 5) violation content |
| A8 + A9 | Detection lag | **Awareness Gap (H2)** — how long inference stayed invisible |
| A10 | Cost | Cost-of-misalignment quantification (restarts, waste) |
| A11 | Recovery path | Override/Reversibility behavior (Laws 6–7) in the wild |
| A12 | Available context | **Context Roots / Context Factor** — was correct meaning recoverable from history? |
| A13 | Extraction reliability | Data quality flag for your analysis |

---

## PART C — RESEARCHER-ONLY CLASSIFICATION BLOCK
**(You complete this per incident. Never delegate to the LLM.)**

Append to each incident record after collection:

```
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

---

## PART D — QUALITY RULES FOR THE CORPUS

1. **Verify quotes.** LLMs reconstruct imperfectly. Before an incident enters your dataset, check A3 and A8 against the real transcript and set C9=CONFIRMED. Unverified incidents may be reported only as such.
2. **One incident, one record.** If a single instruction caused multiple downstream failures, keep one record and list all consequences in A10.
3. **Cross-window duplicates.** If the same intent failure recurred in different windows, keep both records and link them in C10 (this itself is data: signature-less re-alignment cost).
4. **Do not clean the data of embarrassment.** Incidents where YOUR instruction was genuinely poor are still valid data — the framework predicts ambiguity is a joint property, not a fault.
5. **Preserve raw outputs.** Keep the LLM's original extraction files unedited; do classification in copies. Chain of custody matters if this becomes a published corpus.
6. **Disclose method.** In any paper: extraction was LLM-assisted, classification was researcher-performed, corpus is single-user and single-project — evidence of existence and mechanism, not population prevalence.

---

*Protocol version 1.0 — July 2026. Prepared for the Collaboration Protocol empirical program (Studies: Silent Inference Prevalence, IPP Taxonomy Validation, IFI-Bench seeding).*
