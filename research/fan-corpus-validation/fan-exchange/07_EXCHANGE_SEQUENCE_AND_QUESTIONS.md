# Recommended Exchange Sequence — CP ↔ DCM 2.0

## Purpose

Fan's latest request is methods-first: understand how the 52 candidate records were extracted and classified, then compare that structure with his DCM 2.0 Field & Technical Notes before naming a formal collaboration.

The scientifically safest exchange is therefore a **schema-comparison exercise**, not a proposal to combine datasets immediately.

## Step 1 — Fan reviews the CP method, not the result claim

Recommended first-read order:

1. `00_READ_ME_FIRST.md`
2. `01_METHODS_NOTE.md`
3. `02_SCHEMA_AND_CODEBOOK.md`
4. `06_CURRENT_EMPIRICAL_STATUS.md`
5. `03_DCM2_CROSSWALK_TEMPLATE.md`
6. `04_SANITIZED_EXAMPLES.md`
7. `05_LIMITATIONS_AND_EVIDENCE_STATUS.md`

The key question for Fan is whether he can identify meaningful DCM counterparts for the CP variables without forcing equivalence.

## Step 2 — Fan marks the crosswalk

For each row in `03_DCM2_CROSSWALK_TEMPLATE.md`, Fan can mark one of:

- `DIRECTLY COMPATIBLE`
- `CONCEPTUALLY RELATED BUT DIFFERENT`
- `MISSING ON CP SIDE`
- `MISSING ON DCM SIDE`
- `REQUIRES NEW DATA`
- `NOT A VALID LINK`

This creates a concrete technical artifact from the exchange instead of a broad conceptual discussion.

## Step 3 — resolve four construct definitions before any hypothesis

The two researchers should agree on the exact meaning of:

### A. AI causation

Does “AI caused the error” mean factual causation, perceived blame, contribution, or primary fault?

### B. user responsibility / burden

Does DCM Q2 mean moral responsibility, practical obligation, financial loss-bearing, duty to correct, or something else?

### C. interpretation visibility

What counts as a surfaced interpretation: a clarifying question, explicit alternatives, a disclosure before acting, a disclosure after acting, or all of these with different codes?

### D. materiality

What minimum consequence makes an interpretation decision relevant to the accountability question?

If these definitions cannot be aligned, the collaboration can still be valuable as a comparison of distinct constructs, but the causal bridge should not be claimed.

## Step 4 — map a small number of sanitized profiles

Use the five profiles in `04_SANITIZED_EXAMPLES.md` only as schema probes.

For each profile, Fan can answer:

- Which DCM fields could represent this event?
- Which facts would DCM not capture?
- Would the participant's Q1/Q2 answers be interpretable without seeing the precipitating interaction?
- Would CP need a new downstream responsibility field to make the event comparable?
- Does this case reveal that the proposed bridge is invalid or incomplete?

The exercise should include the counter-pattern and exclusion example, not only likely-SII cases.

## Step 5 — decide whether existing data support only a conceptual paper or a new empirical study

Possible outcomes:

### Outcome A — methods note only

The schemas illuminate different layers of the same accountability problem, but existing data are not joinable. The researchers write a short conceptual/methodological note and propose a future design.

### Outcome B — secondary comparative coding

Fan's DCM narratives contain enough precipitating-event detail that a blinded subset can be coded for CP-style event categories. This would require a separate coding protocol, privacy review, coder-independence plan, and reliability procedure. CP categories must not be imposed retroactively without testing their fit.

### Outcome C — new joint study

The existing datasets reveal a testable bridge but cannot answer it. A new study measures both:

1. interpretation visibility / SII mechanism; and
2. causal attribution plus accepted burden/responsibility.

This is the cleanest design for causal or mediation claims.

### Outcome D — no empirical bridge

The data operate at incompatible levels and no defensible mapping exists. Recording that result would still be scientifically useful and should be treated as a valid outcome.

## Step 6 — only then formulate a formal hypothesis

If the mapping survives, a future pre-registered design might test whether interpretation visibility changes the gap between perceived AI causation and user-accepted burden.

The current datasets alone should not be used to assert that relationship causally.

## Questions Mohamed should send with the package

1. Does the CP A1–A13 schema capture a layer that your DCM 2.0 data currently lack, or is the same layer already present under different fields?
2. What exactly is the unit of observation in your shareable/public data structure?
3. Can you provide the exact Q1 and Q2 wording and coding categories used for causation versus burden/responsibility?
4. Does your data retain any description of the original AI failure sufficiently detailed to distinguish intent misinterpretation from factual or competence errors?
5. Is there a measure of when or whether the participant noticed the AI's interpretation/error?
6. How is experience defined for the 52% vs 24% gradient discussed in our correspondence?
7. What coding/adjudication or inter-rater reliability procedure applies to qualitative responses?
8. Which DCM fields would you map to CP A8/A9 (awareness), A10 (consequence), C2 (materiality), and C3 (context/experience), if any?
9. Would you be willing to mark the crosswalk as compatible / related-but-different / missing / new-data-required / invalid-link before we discuss a joint hypothesis?
10. What evidence would make you reject the proposed CP↔DCM bridge?

## What Mohamed should not ask Fan to do yet

Do not ask Fan yet to:

- endorse the 52 records as validated SII incidents;
- merge participant-level DCM data with CP incident rows;
- accept CP's taxonomy as the correct coding system for his data;
- commit to a co-authored paper;
- commit to new data collection;
- or interpret the 79% result as being caused by silent intent inference.

Those are downstream questions. The present exchange should remain technical, falsifiable, and low-commitment.

## Suggested endpoint of the first exchange

A one- or two-page joint schema map answering:

> **Where do CP's interaction-level interpretation variables and DCM 2.0's attribution/responsibility variables genuinely connect, where are they merely conceptually adjacent, and what new measurement would be required to test the proposed bridge?**

If the two researchers can answer that clearly, a collaboration design becomes much easier and much more defensible.
