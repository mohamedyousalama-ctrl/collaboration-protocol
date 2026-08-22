# CP ↔ DCM 2.0 Data-Level Crosswalk

## 1. Purpose and evidence boundary

This document is a **comparison worksheet**, not a claim that CP and DCM 2.0 measure the same construct.

Two DCM sources are distinguished:

1. **researcher correspondence** — facts Fan and Mohamed explicitly discussed in their July/August email thread;
2. **Fan's public materials** — DCM 2.0 study DOI `10.5281/zenodo.20280700` and Field & Technical Notes DOI `10.5281/zenodo.20281517`.

The current package does not silently reconstruct fields that have not been independently mapped from Fan's technical notes. Items known only from correspondence are labeled as such and are questions for Fan to confirm against his data dictionary.

## 2. Correspondence-stated DCM facts relevant to the bridge

The July correspondence states the following study-level facts:

- field study: **328 street-intercept interviews**;
- participants: **33 nationalities**;
- location/timeframe: **Taipei, December 2025–April 2026**;
- the discussion distinguishes **Q1 causal attribution** from **Q2 who bears the loss/consequence**;
- Mohamed's July synthesis of Fan's results states Q1 as approximately **25% user / 37% shared / 31% AI**;
- the same correspondence states that **79%** assigned the primary burden/loss to themselves at Q2;
- it also states that **71% of respondents who blamed AI at Q1 still assigned the loss to themselves at Q2**;
- an experience gradient discussed in correspondence is approximately **52% among newer users vs 24% among experienced users** for the relevant responsibility pattern.

These numbers are included here only as **correspondence-stated study facts to be checked against Fan's own public technical notes/data dictionary before any publication or combined analysis**.

## 3. Crosswalk matrix

| Comparison dimension | CP naturalistic corpus | DCM 2.0 — correspondence/public-note question | Compatibility test |
|---|---|---|---|
| Unit of observation | Incident within an AI work conversation | Study is based on individual street-intercept interviews; exact machine-readable row level to confirm | Is a DCM row a participant, question-response, coded episode, or another object? Do not treat a participant as equivalent to an interaction incident. |
| Primary evidence | Conversation/task evidence, derivative extraction, and partial primary source recovery | Field interview responses plus whatever coding/recording procedure is defined in Technical Notes | Compare direct event traces vs retrospective/self-report evidence explicitly. |
| Upstream event | A3/A4/A5/A6 describe instruction ambiguity, interpretation choice, and whether clarification occurred | Unknown from correspondence whether the precipitating AI interaction itself is coded in sufficient detail | Does DCM contain an event/failure description that can classify what the AI did, or only the participant's later judgment? |
| User awareness | A8/A9 represent when mismatch becomes visible/detected | Fan linked CP's H2 Awareness Gap to his field results conceptually; exact DCM awareness variable needs confirmation | Is awareness measured directly, inferred, or absent? |
| Consequence | A10 traces rework, rollback, delay, blocked action, or no visible consequence | Q2 correspondence concerns who bears loss/consequence | Does DCM encode the kind or magnitude of loss separately from who is expected to bear it? |
| Causal attribution | Not an original primary CP outcome; could be added only in a future study | Q1 explicitly distinguishes perceived causation among user/shared/AI categories in correspondence | Keep `who caused it?` separate from `who bears it?`. |
| Responsibility / burden | Not directly measured in the historical CP corpus | Q2 is the strongest correspondence-stated DCM variable for accepted burden/loss | Can DCM Q2 be treated as responsibility, burden-bearing, loss-bearing, or another construct? Fan should specify exact wording. |
| Causation–burden divergence | Not measured directly; CP could provide candidate mechanism preceding the divergence | Correspondence states many AI-causation respondents still self-assigned loss | Is this a stable DCM pattern after examining raw/coded data, and what is the denominator? |
| Ground-truth intent | C5 belongs to the researcher/user who issued the instruction | No known direct analogue from correspondence | DCM may capture perceived intention/causation, not the historical user's actual intended meaning. Do not collapse these. |
| Ambiguity type | C1 IPP taxonomy | Unknown | Could DCM incident descriptions be coded using CP categories without forcing the taxonomy onto unrelated data? |
| Materiality | C2 and A10 | Consequence/loss may provide a related but non-equivalent concept | Does DCM record stakes/severity, or merely assignment of responsibility? |
| Context / experience | A12/C3 describe conversational prior context | Correspondence mentions an experience gradient | Is experience measured continuously, categorically, or by self-report? Could it moderate rather than mediate the proposed relationship? |
| Validation | C9 requires primary transcript/source check; final C-fields require researcher adjudication | DCM coding/reliability procedure should come from Fan's Technical Notes | Compare validation regimes; do not imply equivalent reliability metrics. |
| Temporal order | A3 → A5/A6 → A8/A9 → A10/A11 | Interview order includes at least Q1 and Q2; relationship to original AI event timing is unclear | Can a defensible temporal chain be built, or is DCM necessarily retrospective? |
| Population inference | Current CP corpus is single-researcher naturalistic candidate data, not prevalence sampling | DCM is a field-interview sample with broader participant diversity | CP cannot inherit DCM's population properties, and DCM cannot inherit CP's interaction-level mechanism evidence. |

## 4. Candidate bridge — hypothesis, not conclusion

The scientifically interesting possibility is a chain such as:

`AI resolves material ambiguity without surfacing it`

→ `user detects the mismatch late or only after consequence`

→ `user forms a causal judgment about AI/user/shared responsibility`

→ `user nevertheless accepts the practical loss/burden`

The CP corpus is designed to observe the **interpretation and detection mechanism**. The DCM correspondence suggests variables concerning **causal attribution and burden assignment**.

The bridge becomes scientifically useful only if Fan's schema confirms that these are separable variables and if a future study measures both sides in the **same observation process**. Existing CP and DCM data should not be post-hoc joined as if they were participant-matched observations.

## 5. Candidate joint hypotheses for discussion only

These are deliberately phrased as future-test hypotheses, not findings:

- **H-Awareness:** Lower visibility of the AI's interpretation decision is associated with a larger gap between perceived AI causation and burden accepted by the user.
- **H-Disclosure:** Explicitly surfacing an interpretation point before action reduces later self-burden when the AI-selected interpretation would otherwise be wrong.
- **H-Experience:** User experience moderates the causation-to-burden relationship, potentially because experienced users identify system contribution more readily or negotiate responsibility differently.
- **H-Materiality:** The effect of interpretation visibility on responsibility judgments grows when the ambiguity is materially consequential rather than trivial.

A future design would need pre-registration, a clear unit of analysis, independent measurement of SII/visibility and responsibility/burden, and a sampling frame that supports the intended inference.

## 6. Questions for Fan to resolve from the Technical Notes/data dictionary

1. What is the exact stored unit: participant, interview, question-response, incident vignette, coded narrative, or another object?
2. What are the exact wordings and response options for Q1 and Q2?
3. Does Q2 measure moral responsibility, financial/practical loss-bearing, fault, obligation to repair, or another concept?
4. What denominator produces the 79% headline and the 71% Q1→Q2 divergence figure?
5. Is the original AI failure/event described at a level that can distinguish user-intent misinterpretation from factual/competence errors?
6. Is there a variable for when the participant noticed the AI error or how visible the AI's interpretation was?
7. How is user experience operationalized in the reported 52% vs 24% gradient?
8. Which responses are coded qualitatively, and what coder-training/reliability or adjudication procedure was used?
9. Are consequences/losses coded separately from causal attribution and burden assignment?
10. Can a small number of sanitized CP candidate profiles be mapped to DCM fields purely as a schema exercise, without treating them as matched observations?
11. Which public or shareable DCM fields can be exchanged without exposing participant-level restricted data?
12. What result would convince us that the CP↔DCM bridge is **not** empirically useful?

## 7. Minimum successful outcome of the exchange

A successful first exchange does not need a collaboration agreement. It needs a short joint mapping that marks each proposed linkage as:

- `DIRECTLY COMPATIBLE`;
- `CONCEPTUALLY RELATED BUT DIFFERENT`;
- `MISSING ON CP SIDE`;
- `MISSING ON DCM SIDE`;
- `REQUIRES NEW DATA`; or
- `NOT A VALID LINK`.

Only then should the researchers decide whether a joint study is warranted.
