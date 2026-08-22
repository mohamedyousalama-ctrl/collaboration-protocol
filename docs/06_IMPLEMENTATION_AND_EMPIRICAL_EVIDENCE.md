# 06 — Implementation and Empirical Evidence Audit

This document separates **specification truth**, **implementation truth**, and **empirical-material truth**. The recovered archive contains useful evidence, but it also contains contradictions that make a simple “CP is validated” statement academically indefensible.

---

## 1. Frozen source set and conformance problem

The Freeze Declaration names eight canonical artifacts. The recovered preservation bundles collectively contain those artifacts, but they are not perfectly mutually consistent.

### 1.1 System Model vs Implementation Specification

The canonical System Model defines:

- PC-3 = action requested without Context -> Clarify;
- PC-4 = clear, no action requested -> Allow;
- PE-3 = Intent does not match action -> Refuse;
- PE-8 = action exceeds Agent permissions -> Refuse; and
- PE-9 = action violates Context constraints -> Refuse.

The recovered `CP_v1_Implementation_Complete.md` instead contains materially different rules, including:

- PC-3 = clear + no action -> Allow;
- PC-4 = clear + action requested -> Allow;
- PE-3 = action Context ID differs from Intent Context ID;
- PE-8 = explanation-only agent + non-communicate action;
- PE-9 = external action -> Clarify / high-risk action.

These are not cosmetic differences. They change what CP means and does. The preservation archive therefore treats the **System Model + Freeze Declaration** as the normalized semantic source and the Implementation Specification as an implementation-lineage artifact with known divergence.

### 1.2 Frozen runtime omissions

The recovered `cp_v1_0_1_runtime_persistent.html` implements explicit checks for:

- PE-1
- PE-2
- PE-4
- PE-5
- PE-6
- PE-7
- PE-10
- PE-11

It does **not** implement the canonical PE-3, PE-8, or PE-9 checks from the System Model.

Therefore the historical runtime cannot be used as evidence that all frozen pre-execution semantics were implemented.

### 1.3 Validation template status

`v1_0_1_validation_tests.md` is preserved as a validation template. In the recovered artifact, the certification/status fields are not completed. It is therefore not evidence of an executed conformance certification.

---

## 2. Technical audit report

The recovered `cp_v1_technical_audit_report.md` reports a governance score of approximately 82/100 and describes ten adversarial simulations, with partial failures around context collapse and silent drift.

Two preservation cautions apply:

1. The document prints a January 2025 date that is not supported by the recovered provenance record.
2. The archive does not contain a separate raw execution log proving every reported simulation independently of the report itself.

The report is therefore preserved as **historical technical assessment evidence**, not elevated into an independently replicated result.

Its useful findings include production-readiness gaps such as client-side state, unsigned logs, authentication limitations, and brittle regex classification.

---

## 3. Klear source-code audit

The sanitized Klear source code is preserved under `archive/klear/`.

### 3.1 Positive evidence

The code contains concrete governance mechanisms rather than only prose:

- session-start articulation and context handling;
- IPP classification/filtering;
- friction records;
- Safety Floor logic;
- domain classification;
- Guardian-like checks;
- action/session logging;
- counterfactual and trace surfaces;
- streaming monitor/mid-generation concepts; and
- database schemas for governance events.

This is important applied evidence that the research program progressed beyond a paper-only concept.

### 3.2 Material conformance gaps

#### Fail-open Guardian behavior

The recovered `guardian.js` contains exception and parse-error fallbacks that return `decision: 'allow'`. That is inconsistent with a strict external enforcement layer if Guardian failure should block uncertain execution.

#### Mid-stream monitor continues on error

The recovered `stream_monitor.js` explicitly returns a continuation result on evaluation/parse errors. The comments call this “fail safe to CONTINUE,” but from an enforcement perspective it is a fail-open path for the monitoring function.

#### Retry path bypasses nominal checkpoint flow

`session.js` contains a retry branch documented in code as:

```text
Skip IPP classification, ICD filter, and Guardian CP1
```

It then logs an allow-style post-classification event for the retry path. This is a different control path from a complete frozen CP chain.

#### Responsibility-chain health is hard-coded

The recovered report-generation code sets:

```text
responsibility_chain_intact: true
```

rather than proving chain integrity from the underlying linked events at report time.

#### CP2 can be represented as skipped

Trace-generation code can report an allow-like result with `cp2_skipped: true`. This is implementation-specific behavior and not equivalent to a frozen universal pre-execution gate.

### 3.3 Conclusion on Klear conformance

Klear is best classified as:

> **CP-inspired / CP-related applied governance implementation with substantial real mechanisms, but not a clean frozen CP v1.0.1 reference runtime.**

This status is academically stronger than either dismissing Klear or overclaiming conformance.

---

## 4. Klear financial evaluation dataset

### 4.1 Recovered evidence

The sanitized evidence archive contains multiple generations of:

- scenario banks;
- session logs;
- observation notes;
- aggregate analysis;
- research-paper-data sheets;
- screenshot organizers; and
- a separate earlier general evaluation sheet.

The financial test design spans categories for research, boundary pressure, credentials/authority, long-conversation drift, stress/personalization pressure, and audit traceability.

### 4.2 Result-generation inconsistency

The workbooks do not present one stable denominator across all versions.

Examples found in the recovered workbook generations include:

- an earlier aggregate showing roughly **94% vs 27% vs 27%**;
- a later generation showing **96%** for Klear with a `22/23` or related completion framing;
- an updated-final analysis sheet describing **26/27** Klear Pass with 1 Partial while comparing ChatGPT/Gemini against 30-row denominators;
- completed-scenario counts that do not always match the prose note in the same workbook.

Because denominator choice is material, this archive does **not** select one headline rate as the final empirical truth.

### 4.3 Stable qualitative findings present across workbook generations

The workbooks repeatedly record:

- strong Klear boundary enforcement in tested finance scenarios;
- zero recorded silent-advice events in the Klear B/C/D/E subset used by later analysis;
- credential challenges in Klear where baselines did not challenge;
- named friction and audit/decision-record behavior; and
- known Klear defects, including false-positive scope warnings and a borderline post-scope-expansion response.

These are **pilot observations**, not yet population-level conclusions.

### 4.4 Publication-grade remediation

Before using the Klear dataset for a final paper:

1. freeze one scenario inventory;
2. define one denominator policy per metric;
3. ensure every scored row has underlying response evidence;
4. remove or complete pending rows;
5. blind at least a second rater on a meaningful subset;
6. compute inter-rater reliability;
7. explicitly disclose the architectural asymmetry between Klear and general-purpose baselines;
8. separate model backend and governance-layer causal effects; and
9. archive the exact raw response/evidence set with hashes.

---

## 5. Naturalistic incident database audit

`CP_Incident_Database_v1.xlsx` contains:

- 52 incident rows plus header;
- seven source windows according to the workbook README;
- preloaded extraction fields;
- a codebook;
- aggregate formulas; and
- researcher-only final classification fields.

The workbook explicitly says rows cannot enter paper analysis until quote verification and researcher-final classification are complete.

In the recovered workbook, those final fields are not completed. Consequently:

> **The 52-row file is a structured candidate corpus, not a finished ground-truth dataset.**

This matters because the historical Master Knowledge File uses the corpus to propose new phenomena. Those candidate phenomena remain preserved, but they should be re-tested after final coding.

---

## 6. IntentHealth / Safety Floor evidence audit

The recovered Safety Floor specification reports an IntentHealth anomaly in which a CP-guided response received higher intent-fidelity scoring while an external model-based clinical evaluation preferred a more cautious cardiac-first answer.

Research value:

- exposes a genuine conceptual separation between intent fidelity and domain safety;
- motivates an orthogonal safety mechanism;
- produces falsifiable hypotheses.

Limitations:

- the clinical evaluator was an AI model rather than a qualified physician panel;
- only a small pilot is represented;
- SCS values and IFI-H weighting require calibration;
- the Safety Floor's clinical content is not itself validated by the specification.

Therefore Safety Floor is preserved as a **strong theoretical extension motivated by pilot evidence**, not as clinically validated production safety infrastructure.

---

## 7. What future CP evidence should look like

A research-grade evidence hierarchy should be:

1. **Frozen semantics** — versioned specification.
2. **Conformance tests** — machine-executable coverage of every frozen rule.
3. **Reference Runtime** — implementation proven to pass conformance.
4. **Raw scenario inputs and expected state** — deterministic benchmark fixtures.
5. **Raw outputs/tool traces** — immutable exact evidence.
6. **Scoring code** — reproducible metrics, no spreadsheet-only hidden logic.
7. **Independent rating where subjective judgment remains**.
8. **Ablations** — CP-off, prompt-CP, conventional governance, enforced CP.
9. **Failure injection** — including post-approval state changes.
10. **Reconstruction tests** — verify that independent reviewers can establish who authorized what.

This structure turns CP from a collection of promising ideas into a falsifiable, reproducible systems-research program.
