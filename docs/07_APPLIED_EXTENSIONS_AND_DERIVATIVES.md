# 07 — Applied Extensions and Derivative Research

Frozen CP v1.0.1 is intentionally interaction-level. The broader research program repeatedly asks what happens when CP is composed with domain safety, persistent context, multi-agent workflows, operational products, and real-world evidence systems. Those applications are scientifically valuable precisely because they are kept **outside** the frozen core unless a new version explicitly adopts them.

---

## 1. Safety Floor: domain safety outside ordinary intent control

### Problem discovered

Intent fidelity can conflict with domain safety or correctness. A user can explicitly choose a narrow interpretation that omits a medically prudent warning. That exposes a limit of a pure “human meaning is authoritative” rule.

### Extension response

The Safety Floor extension proposes:

- domain classification;
- a versioned, expert-approved minimum assertion set;
- injection after normal intent-constrained generation;
- non-suppressibility by ICD/user ambiguity choices;
- separate audit events; and
- a separate safety-compliance measure.

### Scientific significance

The extension is an important self-correction in the research program: it refuses to redefine fidelity as safety. It instead models two objectives separately.

### Boundary

Safety Floor is **not** frozen CP v1.0.1. Qualified domain validation is required before production claims.

---

## 2. Klear: governed financial AI implementation

Klear operationalizes a wider CP family in a functioning full-stack application. Its preserved code/evidence demonstrates practical work on:

- session articulation;
- declared context;
- IPP detection;
- ICD filtering;
- friction;
- domain selection;
- Safety Floor;
- audit/trace presentation;
- counterfactuals;
- session reports; and
- Guardian/mid-stream monitoring behavior.

The implementation is scientifically useful in two ways:

1. it provides a concrete testbed for user-facing governance mechanisms; and
2. its defects expose where a paper specification is insufficient for real enforcement.

Klear should therefore be used as a historical applied case and source of design lessons, not as the definition of frozen CP.

---

## 3. Project Continuity / Ghost

### Product thesis

Project Continuity explores a user-owned operational-context layer that carries relevant state across AI tools while preventing remembered/inferred information from silently becoming authority.

Core law:

> **Memory is not authority.**

### Architectural separation

The broader system distinguishes:

- continuity / remembered state;
- context proposals;
- confirmed operational Context;
- verified Intent;
- CP Guardian evaluation;
- external execution; and
- a Meaning Ledger / evidence record.

This architecture is designed to permit richer memory without violating frozen CP's rule that execution authority must come from explicit current state.

### Presence / “Come”

The “Presence” is a user-facing concept that can be summoned with “Come” and arrive situated in current work. The design challenge is to make the system context-aware without letting inference grant power. The source materials therefore distinguish situating, proposing, preparing, and executing.

### Ambient Context Fabric

The Ghost strategy proposes a staged pipeline:

```text
raw signal
-> derived observation
-> inferred/provisional Context (Bud)
-> confirmed Context
-> actionable authority
```

The important governance principle is that information can move toward authority only through explicit gates. Probabilistic inference may propose; it cannot authorize.

### Action grammar / minimum action floor

The strategy explores universal action primitives and several minimum-capability models (including Scribe/Desk/Hands variants in later workshop language). The aim is to make product capability truthful even when some external tools permit only preparation rather than execution.

### Continuous onboarding and calibration

The broader product explores:

- Essential Ceremony;
- Continuous Calibration;
- Just-in-Time Permission;
- user-controlled privacy/sensing boundaries; and
- no-self-amplification.

These are product governance constructs, not frozen CP semantics.

---

## 4. Kivo cross-product learning

The Ghost/Kivo learning register extracts interaction patterns from Kivo while explicitly forbidding restaurant-specific details from becoming universal product laws.

Transferable concepts include:

- one human intention coordinating many live work units;
- target-specific Context and action plans;
- explicit responsibility state (Lead / Listener / Scoped Participant);
- same-surface detailed focus without losing the wider work field;
- recovery paths and evidence per target.

Non-transferable Kivo specifics include WhatsApp timing rules, restaurant order stages, menu objects, COD assumptions, kitchen/driver roles, restaurant tenancy, and Kivo branding.

The strongest preserved cross-product principle is:

> One human intention may coordinate many live units of work, but every target must preserve its own Context, authority, plan, evidence, and recovery path.

---

## 5. Decision Packets

Applied CP/Ghost work in VEIS formalizes a **Decision Packet** with fields such as:

```text
context_hash
episode_id
current_state
requested_intent
proposed_action
evidence_assertion_ids[]
independent_families[]
benign_explanations[]
uncertainty
guardian_result
required_friction
human_authorizer
expiry
idempotency_key
execution_target
```

This is not a frozen CP object. It is an engineering pattern for compiling current state and authority into a reviewable execution artifact.

Research significance: it makes post-approval drift testable because the candidate action can be compared with the exact state/authorization packet immediately before execution.

---

## 6. Vehicle Evidence / external corroboration application

VEIS applies CP/Ghost authority ideas to vehicle-theft/asset-recovery evidence. Its governance distinctions include:

- AI can propose evidence-based risk;
- AI cannot independently confirm a legal incident;
- sensitive external queries require purpose and authorization;
- evidence source families should remain distinguishable;
- external corroboration should be minimized and auditable; and
- human confirmation remains required for incident/recovery escalation.

This application illustrates a general CP principle: the AI may organize evidence and recommend a state transition, while legal/operational authority remains separate.

---

## 7. Public benchmark / Kaggle direction

The Ghost strategy preserves a parked plan for a public benchmark program sometimes described as **IFI-Bench** or an equivalent benchmark family.

Proposed tracks include:

- core intent-fidelity scenarios;
- agentic authority/action scenarios;
- standing-instruction persistence;
- a future Kivo restaurant track;
- public notebooks/datasets;
- base-model vs CP/Ghost comparisons; and
- future community challenge formats.

The direction is strategically consistent with CP's need for falsifiable, reusable measurement. It remains parked/proposed until the dataset, scoring model, and legal/privacy sanitation are ready.

---

## 8. What derivative work teaches the frozen protocol

Derivative projects should not modify the frozen semantics, but they generate research questions that can later justify a new version:

1. How should authority expire or be invalidated over time?
2. How should a verified Intent bind to mutable transaction/version state?
3. What is the correct behavior when a Guardian itself fails?
4. How should multi-agent handoffs preserve semantic and execution authority?
5. How should idempotency/replay interact with Responsibility Chain semantics?
6. Can a durable continuity system propose context without turning memory into authority?
7. Which safety requirements must remain orthogonal to user intent?
8. Can Decision Packets provide cryptographic or formal evidence of exact authorization?

These questions belong to future CP research/versioning, not silent edits to v1.0.1.
