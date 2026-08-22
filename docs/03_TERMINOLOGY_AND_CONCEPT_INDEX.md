# 03 — Terminology and Concept Index

This index preserves the vocabulary created, used, tested, or proposed across the Collaboration Protocol research program. **Lineage is part of the definition.** A term appearing in an early CP paper does not automatically belong to frozen CP v1.0.1, and a later product term does not retroactively become protocol semantics.

## Status key

- **EARLY THEORY** — January 2026 SII/IPP/ICD/IFI research lineage.
- **FROZEN CP** — CP v1.0.1 semantic core.
- **EXTENSION** — later CP-adjacent/domain-specific mechanism.
- **APPLIED** — Ghost/Continuity/Kivo/VEIS product or architecture concept.
- **CORPUS CANDIDATE** — concept proposed from naturalistic incident extraction; not yet researcher-final validated.
- **FRONTIER** — current working research terminology, not yet frozen or proven.

---

## A. Foundational research vocabulary

| Term | Expansion / definition | Lineage | Status note |
|---|---|---|---|
| **Collaboration Protocol (CP)** | Research program for governing human–AI semantic authority and, in the frozen lineage, interaction-level accountability between signals and consequential actions. | All | The initials **CP** also appear inside the early IFI formula as “Constraint Preservation”; context must disambiguate. |
| **Silent Intent Inference (SII)** | Machine-generated assumption about user intent, without explicit human authorization, that materially affects output. | Early theory | Named central problem of the early research program. |
| **Semantic Authority** | Authority to determine what a materially underspecified human instruction will be taken to mean. | Early theory → all | Broader theoretical framing; frozen CP expresses authority through Context/Intent/Agent constraints rather than this phrase alone. |
| **Meaning Ownership** | Early-law framing that final semantic authority remains with the human. | Early theory | Normative/theoretical term, not a frozen v1.0.1 object. |
| **Intent Pivot Point (IPP)** | Point where two or more interpretations are plausible, the choice materially changes output, and the user has not specified the choice. | Early theory | Six-type original taxonomy. |
| **Intent Control Degree (ICD)** | User-selected 0.0–1.0 parameter governing how much material ambiguity the system may resolve without surfacing it. | Early theory | Not the frozen v1.0.1 Intent object. |
| **Intent Fidelity Index (IFI)** | Proposed composite `0.4(SA)+0.3(CP)+0.3(SS)`. | Early theory | Measurement proposal; not a frozen CP evaluation metric. |
| **Semantic Alignment (SA)** | Expert-rated correspondence between stated intent and output meaning. | Early theory | IFI component. |
| **Constraint Preservation (CP, IFI component)** | Proportion of user-specified constraints preserved. | Early theory | Acronym collides with Collaboration Protocol. Prefer “Constraint Preservation” in prose. |
| **Subjective Satisfaction (SS)** | User-rated match between output and intended outcome. | Early theory | IFI component; explicitly outside frozen v1.0 evaluation scope. |
| **Context Roots (CR)** | Historical anchors that locate where interpretation-relevant context originates: intra-session, cross-session, environmental, or null. | Early theory | Distinct from frozen CP `Context`. |
| **Context Factor (CF)** | Proposed multiplier for how prior context resolves or amplifies ambiguity. | Early theory | Historical values 0.50–1.50; not empirically calibrated constants. |
| **Semantic Materiality Proxy (SMP)** | Proposed composite score using semantic distance, consequence magnitude, reversibility, and Context Factor to decide whether an ambiguity is material enough to surface. | Early theory | Proposed/illustrative formula; calibration remains research work. |
| **Intent Decay** | Cumulative divergence from original intent through compounded silent assumptions. | Early theory | Explicitly theoretical; formal model deferred. |
| **IPP Log** | Audit record for intent-critical interpretation choices, including candidates, resolution, and context. | Early theory / enterprise extension | Precursor/parallel to later responsibility-chain logging. |
| **Intent Signature** | Proposed recurring user/organization intent pattern for faster alignment across tasks. | Early theory / future work | Must not be mistaken for frozen CP cross-session preference learning, which is explicitly excluded. |
| **Constitutional Onboarding** | Proposed durable user-configured intent/governance defaults established at onboarding. | Early theory / future work | Later influences Continuity/Ghost product work. |
| **Agent Intent Profile (AIP)** | Proposed machine-readable description of how an agent processes human intent. | Early future vault | Deferred until core constructs are validated. |
| **Intent-Anchored Data Analysis (IADA)** | Proposed application of intent-governed semantics to analytics/BI queries where terms such as “top” or “recent” can materially change results. | Early applied extension | Application concept. |

### Original early IPP taxonomy

1. **Scope IPP**
2. **Temporal IPP**
3. **Entity-Reference IPP**
4. **Authority IPP**
5. **Output-Form IPP**
6. **Abstraction-Level IPP**

---

## B. Frozen CP v1.0.1 vocabulary

| Term | Frozen meaning | Status |
|---|---|---|
| **Context** | Bounded, user-declared semantic and operational scope; inspectable, constrained, optionally hierarchical. | **FROZEN CP** |
| **Intent** | Explicit, verified declaration of what the user wants the system to do under defined constraints before execution. | **FROZEN CP** |
| **Agent** | Scoped executor/advisor with explicit permission and prohibition lists; cannot self-authorize. | **FROZEN CP** |
| **Node** | User-committed structural constraint governing future reasoning. | **FROZEN CP** |
| **Pivot** | User-declared epistemic marker of importance; annotative, non-binding, never itself triggers action. | **FROZEN CP** |
| **Responsibility Chain** | `User Signal -> CP Verification -> AI Suggestion -> User Commitment -> Action`, logged at every link. | **FROZEN CP** |
| **Guardian** | Read-only evaluation component issuing gate decisions at defined checkpoints. | **FROZEN CP** |
| **Gate Decision** | Exactly `Allow`, `Clarify`, or `Refuse`. | **FROZEN CP** |
| **Checkpoint 1 / Post-Classification (PC)** | Guardian evaluation after signal classification. | **FROZEN CP** |
| **Checkpoint 2 / Pre-Execution (PE)** | Guardian evaluation after candidate action construction but before execution. | **FROZEN CP** |
| **Friction** | Deliberate pause triggered by ambiguity, missing verification, scope, permission, risk, missing context, or conflict; resolved only by user action. | **FROZEN CP** |
| **Context Store** | Persists Context objects. | **FROZEN CP** |
| **Intent Store** | Persists Intent objects. | **FROZEN CP** |
| **Node Store** | Persists Nodes and Pivots. | **FROZEN CP** |
| **Action Store** | Persists action requests, state, and outputs. | **FROZEN CP** |
| **Friction Store** | Persists friction events. | **FROZEN CP** |
| **Log Store** | Append-only accountability record. | **FROZEN CP** |
| **Context collapse** | Failure in which context boundaries merge or become unclear without user consent. | **FROZEN CP** |
| **User Commitment** | The only chain mechanism that advances verified/suggested work into action. | **FROZEN CP** |

### Frozen friction triggers

`ambiguous_signal`, `unverified_intent`, `scope_boundary`, `permission_violation`, `high_risk_action`, `missing_context`, `conflict_detected`.

### Frozen friction resolutions

`user_clarified`, `user_confirmed`, `user_revised`, `user_abandoned`, `system_blocked`.

---

## C. Later CP/domain extensions

| Term | Definition | Status |
|---|---|---|
| **Safety Floor (SF)** | Domain-validated minimum safety content intended to remain present regardless of user-selected ambiguity handling. | **EXTENSION**; not frozen v1.0.1. |
| **Safety Compliance Score (SCS)** | Proposed ratio of required Safety Floor assertions present in a response. | **EXTENSION / metric proposal**. |
| **IFI-Health / IFI-H** | Health-specific extension of IFI that incorporates SCS. | **EXTENSION**. |
| **Law 8 — Domain Safety Non-Negotiability** | Proposed extension law making domain Safety Floor content non-suppressible. | **EXTENSION**. |
| **Guardian Checkpoint 1.5 / mid-generation Guardian** | Later concept allowing intervention during generation rather than only post-classification/pre-execution. | **EXTENSION**; not frozen v1.0.1. |
| **Safety Floor audit events** | `SF_ACTIVATED`, `SF_INJECTED`, `SF_VIOLATION`. | **EXTENSION**. |
| **Rule-Aware Violation** | Candidate failure in which a model articulates a governing rule and violates it in the same interaction/output. | Early/extension research learning; not frozen. |
| **IFI-adjusted / ambiguity penalty** | Proposed correction for IFI inflation when silent ambiguity resolution looks superficially successful. | Research proposal. |

---

## D. Corpus-derived candidate phenomena

These terms appear in the July 2026 research synthesis, but the recovered 52-row workbook still has incomplete researcher-final classification. Treat them as **candidate phenomena** until the classification/verification gates close.

| Term | Candidate meaning |
|---|---|
| **Standing-Instruction IPP / standing-instruction decay** | A recurring instruction that should re-fire at each applicable occurrence is silently degraded into a one-time instruction. |
| **Resolution-by-Disclosure** | System identifies multiple readings, discloses the ambiguity and chosen interpretation, then proceeds; proposed middle path between asking and silent resolution. |
| **Surfaced-IPP Decay** | A previously surfaced but unresolved ambiguity later reverts to silent resolution instead of remaining open. |
| **Post-Correction Adaptation** | Model behavior changes after explicit correction, potentially surfacing similar ambiguities proactively. |
| **Content-as-Command** | Executable/prescriptive content is treated as authorization to execute despite absence of an explicit imperative. |
| **Means-vs-Outcome Fixation** | Model silently binds an outcome-level instruction to a particular implementation means and stalls or misroutes when that means fails. |

---

## E. Klear implementation vocabulary

| Term | Meaning in Klear work | Status |
|---|---|---|
| **Klear** | CP-related governed financial AI implementation used for historical applied testing. | Implementation, not frozen reference. |
| **Friction Card** | UI mechanism surfacing a governance event and user choices. | Klear implementation. |
| **Decision Record / Trace** | User-visible/logged record of governance decisions. | Klear implementation. |
| **Session Health** | Derived status of governance/logging/session integrity. | Klear-specific. |
| **Counterfactual** | Klear mechanism for comparing/considering alternative interpretation paths. | Klear-specific / experimental. |
| **Domain Classifier** | Component selecting domain behavior such as Safety Floor. | Klear-specific. |
| **Decay** | Klear/early-lineage context decay implementation, not frozen CP Intent lifecycle. | Klear-specific. |

---

## F. Ghost / Project Continuity derivative vocabulary

The following terms belong to the broader continuity/product program and must not be imported into CP v1.0.1 without an explicit new version decision.

| Term | Applied meaning |
|---|---|
| **Memory is not authority** | Remembered or inferred information may situate work but does not itself grant execution authority. |
| **Continuity system / Continuity Plane** | Layer carrying sourced state across time/tools. |
| **Presence** | User-facing manifestation that arrives situated in relevant work/context without silently increasing authority. |
| **Come** | Invocation concept for summoning the Presence. |
| **Personal Constitution** | User-controlled enduring rules/preferences for the broader product; outside frozen CP. |
| **Context Capsule** | Proposed portable package of contextual state; must be user-confirmed before becoming frozen-CP operational Context. |
| **Meaning Ledger** | Product-level evidence ledger intended to preserve decisions, sources, authority, and execution records. |
| **Work Episode** | Bounded unit of ongoing human–AI work in the Ghost/Continuity UI model. |
| **Live Work Field** | View showing multiple live episodes with stable positions and truthful state. |
| **Intent Action** | Human goal statement in the applied product; not automatically an execution command. |
| **Contextual Action Plan** | Target-specific plan compiled from an intent/action and that target's confirmed context. |
| **Focus Studio** | Same-surface detailed view preserving wider work-field context. |
| **Lead** | Actor responsible for next outward/state-changing contribution. |
| **Listener** | Actor receiving relevant state without present execution authority. |
| **Scoped Participant** | Actor authorized for a bounded reply/stage/time/target. |
| **Responsibility Flow** | View of which actor/system must contribute next and what evidence advances work. |
| **Decision Packet** | Applied execution-evidence packet containing context hash, requested intent, proposed action, evidence, Guardian result, authorizer, expiry, idempotency key, and execution target. |
| **Bud** | Provisional inferred Context candidate in Ambient Context Fabric; does not grant authority. |
| **Ambient Context Fabric** | Proposed pipeline from raw signal to derived observation to inferred Context to confirmed Context to actionable authority. |
| **Intent Contract** | Applied authority instrument proposed in Ghost work; not frozen CP Intent. |
| **Delegation Ladder** | Product concept for graduated action authority by context/capability. |
| **Minimum Action Floor** | Product design exploration for guaranteed levels of observe/prepare/execute capability. |
| **Scribe / Desk / Hands floor** | Alternative action-capability floor formulations explored in Ghost strategy work. |
| **Essential Ceremony** | Minimal onboarding/calibration steps needed to establish safe useful state. |
| **Continuous Calibration** | Ongoing user-visible update of broader product context/preferences. |
| **Just-in-Time Permission** | Permission requested at the point a new capability is needed rather than inferred from memory. |
| **No-self-amplification** | Broader product rule that the system cannot silently expand its own authority/capability. |
| **For-You Law** | Ghost product principle that personalization should serve the user without authoring the user's goals. |

The source archive additionally preserves exploratory interface metaphors such as **Living Atlas, Thread Loom, Decision Constellation, Capability Halo, Presence Relay,** and **Temporal Evidence Lens**. These are product exploration terms, not protocol constructs.

---

## G. Applied CP decision architecture (VEIS / other domains)

| Term | Applied meaning | Status |
|---|---|---|
| **Decision Packet** | Evidence-and-authority envelope checked before consequential action. | Applied CP/Ghost architecture. |
| **Evidence Assertion** | Typed claim grounded in an observation/source and used in a governed decision. | Applied. |
| **Independent Evidence Family** | Source-family concept used to avoid treating correlated observations as independent proof. | Applied. |
| **Government Corroboration Gateway (GCG)** | VEIS concept for privacy-preserving official corroboration without bulk access to sensitive systems. | Domain-specific applied architecture. |
| **Vehicle Evidence Episode** | VEIS runtime object for a bounded evidence/recovery episode. | Domain-specific. |

---

## H. Current authorization-continuity frontier

| Term | Working definition | Status |
|---|---|---|
| **Authorization Integrity / Continuous Authorization Integrity** | Whether the action executed at time `tN` remains exactly inside the authority the human granted at `t0`, after intervening changes. | **FRONTIER**. |
| **Authority Continuity** | Persistence of valid human authority across time, agents, systems, state transitions, and handoffs. | **FRONTIER**. |
| **Execution-State Authorization Integrity (ESAI)** | Proposed benchmark measuring whether execution is allowed only while current state still satisfies the authorization conditions. | **FRONTIER metric**. |
| **End-to-End Authorization Fidelity (EAF)** | Proposed measure of whether each consequential mutation remains covered by a current, exact human authorization chain. | **FRONTIER metric**. |
| **Semantic Authority Continuity (SAC)** | Proposed concept emphasizing semantic preservation of what was authorized across multi-agent/system transformations. | **FRONTIER**. |
| **Unauthorized Financial State Mutation Rate (UFSMR)** | Proposed rate of money/ledger mutations outside current exact authority. | **FRONTIER metric**. |
| **Stale Approval Reuse Rate** | Proposed rate of actions executed using approval invalidated by later state. | **FRONTIER metric**. |
| **Cross-Context Contamination Rate (CCR)** | Proposed rate of actions using data/authority from the wrong legal entity, case, project, or context. | **FRONTIER metric**. |
| **Responsibility Reconstruction Rate (RRR)** | Proposed proportion of consequential actions whose exact authorization chain an independent validator can reconstruct. | **FRONTIER metric**. |
| **Zero-Ambiguity Authority-Drift Benchmark** | Benchmark design in which all human instructions are explicit and failures are injected only after approval. | **FRONTIER design principle**. |
| **Dynamic Constraint Adherence Rate (DCAR)** | Proposed industrial-agent metric for respecting changing human constraints at execution time. | **FRONTIER metric**. |
| **Context-Aware Execution Yield** | Proposed industrial metric balancing correct execution of valid actions with refusal after context invalidation. | **FRONTIER metric**. |
| **Approved Change-Set Integrity** | Proposed IT-change metric: whether executed system change equals the exact authorized change set. | **FRONTIER metric**. |
| **Exact Authorized Payment Rate** | Proposed finance metric: whether actual payment exactly matches currently authorized entity, invoice/version, amount, currency, destination, operation and constraints. | **FRONTIER metric**. |

---

## I. Terminology collisions that must not be silently collapsed

1. **CP** = Collaboration Protocol, but the early IFI formula also uses `CP` for **Constraint Preservation**.
2. **Context Roots (CR)** from early theory are not the same object as frozen CP **Context**.
3. **Pivot** in frozen CP is a user-declared non-binding epistemic marker; **Intent Pivot Point (IPP)** in early theory is a system/research classification of a material semantic branch. They are not synonyms.
4. **ICD / IPP / IFI** are prominent in early theory and Klear but are not frozen CP v1.0.1 core objects.
5. **Safety Floor** and **Guardian 1.5** are later extensions and cannot be described as frozen v1.0.1.
6. **Memory / Presence / Constitution / Continuity** belong to derivative product work; frozen CP explicitly excludes cross-session preference learning and long-horizon cognition.
7. **Intent Contract** in Ghost product work is not the same definition as frozen CP `Intent` unless a mapping is explicitly specified.
8. Historical “Protocol Laws” exist in more than one formulation. The frozen v1.0.1 system model instead fixes concrete object/gate semantics. See the lineage and contradiction registers.
