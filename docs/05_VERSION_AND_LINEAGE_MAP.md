# 05 — Version and Lineage Map

A central preservation problem is that CP has **conceptual lineage**, **document version labels**, and **provenance dates** that do not always agree. This document separates them.

---

## 1. Evidenced chronology

| Date / period | Evidence-supported event | Preservation status |
|---|---|---|
| **25 Jan 2026** | Recovered provenance record lists CP research-planning/synthesis sessions and multiple research-package versions. | Earliest supported CP activity in the recovered provenance record. |
| **26 Jan 2026** | arXiv conversion planning and JAIR submission-guidance session records in provenance. | Supported by archival session/file record; authoritative external receipts should be retained if recovered. |
| **2 Feb 2026** | Public TechRxiv preprint posted: *The Collaboration Protocol: Silent Intent Inference as an Accountability Challenge in Human-LLM Interaction*. | Public external timestamp; strongest currently observed public anchor in this preservation pass. |
| **Mar 2026** | Historical IntentHealth materials report health-domain comparator sessions and the fidelity/safety anomaly motivating Safety Floor. | Preserved as project evidence; human clinical validation remains incomplete. |
| **18–22 Apr 2026** | Klear financial-domain test workbooks record controlled comparative testing period. | Empirical pilot material; denominators/results need reconciliation. |
| **30 Jul 2026** | `IPP_Extraction_Protocol.md`, `CP_Incident_Database_v1.xlsx`, `CP_Research_Backlog.md`, and Master Knowledge File compiled/recovered with naturalistic corpus program. | Strong internal archive timestamp; researcher-final labels remain incomplete. |
| **1–5 Aug 2026** | Ghost/Continuity strategy, founder decision register, product constitution, cross-product learning, and action/authority work. | Applied/derivative research. |
| **8 Aug 2026** | VEIS / CP-Ghost Decision Packet application materials in the available library. | Applied/domain research. |
| **15–19 Aug 2026** | Frozen-CP artifacts, master document, provenance memo, audits, and current industrial/authorization-continuity research were recovered into the working research archive. | Recovery timestamp is not necessarily authorship timestamp. |
| **22 Aug 2026** | This GitHub preservation archive initialized and evidence-stratified. | Repository preservation event. |

---

## 2. Unsupported 2025 printed dates

Several recovered files print dates in January 2025, including the CP v1.0.1 Freeze Declaration (`28 Jan 2025`) and comments/headers in runtime or implementation artifacts.

The recovered `CP_Provenance_Record.md` explicitly reports that the archival project contained **no independent 2025 evidence** and that its earliest supported CP activity was 25 January 2026.

Therefore this repository applies the following rule:

- preserve the printed 2025 date exactly in the original artifact;
- do not rewrite the artifact;
- do not describe the printed date as verified priority;
- use the 2026 evidence-supported dates for provenance claims unless stronger independent evidence is later added.

This distinction protects both historical fidelity and academic credibility.

---

## 3. Conceptual lineage A — early semantic-authority theory

Recovered research packages progress through versions named `Complete`, `FINAL_v2`, `v3`, `FINAL_v4`, and `v4.1_arXiv`, with later compendium material incorporating “v6.0 Context Roots.”

Core conceptual family:

```text
Silent Intent Inference (SII)
        |
        +-- Intent Pivot Points (IPP)
        +-- Intent Control Degree (ICD)
        +-- Intent Fidelity Index (IFI)
        +-- Context Roots (CR)
        +-- Context Factor (CF)
        +-- Semantic Materiality Proxy (SMP)
        +-- IPP Log
        +-- Intent Decay / Intent Signatures / future extensions
```

This lineage is primarily a theory of **semantic authority and ambiguity governance**.

### Historical “Protocol Laws”

The early packages contain a seven-law formulation including concepts such as Intent Authority, Ambiguity Surfacing, Articulation Supremacy, Meaning Ownership, Non-Assumption Default, Pivot Traceability, and Human Override. The July Master Knowledge File records a different seven-law naming formulation. Because the formulations differ, this archive does not silently designate one as a frozen v1.0.1 law set.

---

## 4. Conceptual lineage B — frozen interaction-accountability protocol

A later/restructured CP lineage defines the system using:

```text
Context
Intent
Agent
Node
Pivot
  + Responsibility Chain
  + Guardian (PC / PE gates)
  + Friction
  + six state stores
  + append-only logging
```

The Freeze Declaration labels this as CP v1.0.1 and explicitly makes those semantics immutable within v1.0.x.

This lineage is primarily a theory/architecture of **interaction-level execution accountability**.

Important: the recovered source set contains internal contradictions between the System Model, Implementation Specification, and runtime. The normalized archive treats the System Model/Freeze Declaration as the semantic reference and records the implementation deviations rather than “fixing” them in place.

---

## 5. Conceptual lineage C — domain and implementation extensions

### Safety Floor / health extension

```text
Early CP intent-fidelity theory
        + health-domain anomaly
        -> Safety Floor (SF)
        -> Safety Compliance Score (SCS)
        -> IFI-Health
        -> proposed Law 8
```

Status: later extension; not frozen CP v1.0.1.

### Klear

Klear combines multiple generations:

- ICD / IPP / IFI / Context Roots;
- Safety Floor;
- Guardian-like controls;
- friction and audit traces;
- later mid-generation monitoring concepts.

Status: applied implementation; not a clean frozen-v1.0.1 reference runtime.

### Guardian Checkpoint 1.5

A later extension adds a mid-generation intervention concept. It is not part of the two-checkpoint frozen v1.0.1 Guardian model.

---

## 6. Conceptual lineage D — naturalistic corpus and taxonomy refinement

July 2026 corpus extraction adds candidate phenomena such as:

- standing-instruction decay;
- resolution-by-disclosure;
- surfaced-IPP decay;
- content-as-command; and
- means-vs-outcome fixation.

These emerged from case extraction, but the researcher-final coding block remains incomplete in the recovered database. Their status is therefore **candidate refinement**, not frozen taxonomy.

---

## 7. Conceptual lineage E — Ghost / Continuity

The Ghost/Continuity product-research program treats CP as one layer inside a larger architecture:

```text
Continuity / memory / sensed state
            |
            | proposes / situates
            v
      confirmed Context
      verified Intent
            |
       CP Guardian
            |
         execution
            |
      Meaning Ledger
```

Core separation:

```text
Memory != authority
Inference != authority
Personalization != permission
```

This lineage explores cross-session and cross-tool continuity that frozen CP explicitly does not model. It is therefore a **composable system around CP**, not an expansion of CP v1.0.1 by implication.

---

## 8. Conceptual lineage F — authorization continuity frontier

The newest research direction moves from pre-action ambiguity to post-approval state drift:

```text
Explicit human authorization at t0
        |
        v
reasoning / planning / handoffs / time
        |
state, permission, context or payload changes
        |
        v
candidate action at tN
        |
question: is the authorization STILL valid and exact?
```

This yields current working concepts such as ESAI, EAF, SAC, stale-approval reuse, and responsibility reconstruction.

This frontier is conceptually close to frozen PE-3 through PE-10 because those rules evaluate current action, context, agent, permissions, constraints, and friction immediately before execution. However, the frontier metrics and benchmark vocabulary are **new research proposals**, not frozen v1.0.1 semantics.

---

## 9. Version-governance rule for future repository work

When new research is added, every artifact should declare one of:

- `frozen-cp-v1.0.1`
- `historical-theory`
- `extension`
- `implementation`
- `empirical-material`
- `applied-derivative`
- `working-hypothesis`

A new construct that changes what CP means or does must never be backported into `frozen-cp-v1.0.1` merely because it is useful.
