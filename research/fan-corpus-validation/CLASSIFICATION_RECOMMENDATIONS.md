# WP4 — Classification Recommendations for the 52-Record Corpus

**Status:** ASSISTANT RECOMMENDATIONS COMPLETE — RESEARCHER DECISIONS NOT YET MADE

## Scientific authority boundary

This file does **not** convert assistant judgments into researcher ground truth. It operationalizes the preserved codebook so Mohamed Salama can review the 52 records efficiently. `C5 Ground-truth intent` is intentionally left as a question, never filled as fact. `C9` remains `UNVERIFIED` for every row until incident-level primary-source A3/A8/chronology checking is complete.

Rows recommended as comparison/control cases remain preserved; no record is deleted merely because it is not a positive SII event.

## Recommendation rubric

- **C0:** from the stricter WP2 construct-validity pass, not the historical triage label.
- **C1:** only where an intent/mixed interpretation type is applicable.
- **C2:** asks whether alternative readings could materially change the outcome; it is not the same as whether harm actually occurred.
- **C3:** protocol values only: `1.0` no relevant prior context, `1.25` weak/stale/relevant prior context, `1.5` conflicting prior context.
- **C4:** transparent recommendation for implicitly delegated interpretive discretion on a 0–1 scale; it is not an empirical measurement and requires researcher acceptance.
- **C5:** researcher question only.
- **C6:** observable consequence/detection wording only; no invented hours or lines of code.
- **C7:** one primary codebook value; secondary relevance may be noted in C10.
- **C8:** candidate for a future IFI-Bench item; `YES` does not mean source-verified.
- **C9:** all `UNVERIFIED` at this stage.

## Headline recommendations

- SII status: LIKELY **12**, POSSIBLE **11**, NO **25**, CONTROL **4**.
- Benchmark recommendation: YES **15**, NO **37**.
- Final analyzable positive-SII count: **not yet determined**.

### Provisional C0 queue

| Recommended class | Records |
|---|---:|
| INTENT | 22 |
| COMPETENCE | 15 |
| PREMISE | 7 |
| MIXED | 1 |
| META | 4 |
| CONTROL/NO_POSITIVE_CLASS | 3 |

## Priority order for researcher review

1. **12 LIKELY SII rows** — resolve C5 and accept/overrule C0–C4 first.
2. **11 POSSIBLE rows** — these are most sensitive to missing source context and delegated-discretion interpretation.
3. **4 CONTROL rows** — confirm they really are disclosed/uncorrected counter-patterns rather than positive events.
4. **25 NO rows** — accept/overrule the competence/premise/meta recommendation; do not spend time writing C5 unless you believe an intent branch actually existed.

## Source-verification boundary

The current source register has a GPT derivative extract, 11 primary task-artifact A3 corroborations, and a bounded AUD primary transcript fragment from the historically identified Claude Code JSONL session. That is not enough to mark any corpus row `C9=CONFIRMED` without row-level A3/A8/chronology mapping.

## Machine-readable recommendations

`CLASSIFICATION_RECOMMENDATIONS.tsv` contains all 52 rows and columns for C0–C10 recommendations/questions, SII status, evidence note, original A13 confidence, and historical triage class.

## Researcher decision rule

For each row, Mohamed should record: **ACCEPT**, **OVERRULE**, or **DEFER FOR SOURCE**. If overruling, state the corrected C0/C1/C2/C3/C4 and write C5 in his own words. No assistant-generated wording should be copied into C5 unless Mohamed independently confirms it expresses what he actually meant.
