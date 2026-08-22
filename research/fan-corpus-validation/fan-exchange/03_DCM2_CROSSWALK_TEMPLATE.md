# CP ↔ DCM 2.0 Data-Level Crosswalk Template

## Purpose
This template is for comparing the CP naturalistic incident corpus against DCM 2.0 public-layer Field & Technical Notes without assuming the datasets measure the same phenomenon.

## Crosswalk questions

| Comparison dimension | CP corpus | DCM 2.0 | Compatibility question |
|---|---|---|---|
| Unit of observation | Incident within an AI work conversation | To be filled from DCM 2.0 public materials | Can one DCM observation plausibly correspond to an interaction incident, or only to a participant-level account? |
| Primary source | Conversation transcript | To be filled | Are observations based on direct event traces, participant report, interviewer coding, or a mixture? |
| Upstream event | Ambiguous instruction / AI interpretation choice / unstated assumption | To be filled | Does DCM capture the precipitating AI/user event or only later attribution? |
| User awareness | A6/A8/A9 expose whether and when mismatch became visible | To be filled | Does DCM record when the participant recognized the AI-related error? |
| Consequence | A10 records observable rework/rollback/other consequence | To be filled | Does DCM distinguish practical consequence from responsibility attribution? |
| Responsibility / attribution | Not the original primary outcome; candidate downstream linkage | To be filled | Can DCM attribution variables be linked conceptually to CP incident mechanics? |
| Ground-truth intent | C5, researcher/user authority | To be filled | Does DCM have an equivalent ground-truth or only reported perception? |
| Ambiguity type | C1 | To be filled | Is there any compatible categorization of precipitating event types? |
| Materiality | C2 | To be filled | Does DCM encode severity, stakes, loss, or consequence magnitude? |
| Context/history | A12/C3 | To be filled | Does DCM capture prior experience, accumulated context, or experience gradient? |
| Verification | C9 requires transcript check | To be filled | What evidence/coding validation exists on the DCM side? |
| Temporal order | A3 → A5/A6 → A8/A9 → A10/A11 | To be filled | Can DCM observations be ordered along a comparable causal/temporal sequence? |

## Candidate connection to test, not assume
A possible conceptual bridge is:

`interpretation event → hidden/visible mismatch → consequence → perceived causal attribution → accepted responsibility/burden`

The CP corpus is strongest toward the left side of this chain. Fan's DCM 2.0 work may be stronger toward the right side. The exchange should test whether the variables are compatible enough to study this chain rather than claiming the connection in advance.

## Questions for Fan
1. What is the exact row/unit in the DCM 2.0 dataset: participant, event, answer, coded episode, or another object?
2. Which fields distinguish perceived AI causation from responsibility accepted by the user?
3. Is consequence/loss represented separately from causal attribution?
4. Does the dataset contain any description of the precipitating AI interaction or failure mode?
5. Are there temporal fields indicating when the participant recognized the error?
6. How are qualitative responses coded, and what validation/reliability procedure was used?
7. Which fields in the Field & Technical Notes can be shared/mapped without exposing restricted participant data?
8. Would Fan consider a small schema-mapping exercise on sanitized examples before any joint study proposal?
