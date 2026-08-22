# 02 — Canonical CP v1.0.1 Reference

**Status:** Normalized preservation reference for the frozen CP v1.0.1 semantics  
**Primary recovered authority:** `archive/frozen-v1.0.1/cp_v1_system_model_final.md`  
**Freeze record:** `archive/frozen-v1.0.1/cp_v1_0_1_freeze_declaration.md`

This document does not replace the recovered frozen artifacts. It makes their operative semantics easy to inspect while separately flagging implementation conflicts.

---

## 1. System position

CP v1.0.1 is an **interaction-level execution-time mediation protocol**. It sits between user signals and actions. It does not modify model weights or training data. Its accountability goal is that consequential execution be traceable to explicit human authority within valid scope.

---

## 2. Frozen object model

### Context

A bounded, user-declared semantic and operational scope within which reasoning and actions are permitted.

Key frozen properties:

- explicit rather than “all available information”;
- may be hierarchical;
- inspectable;
- has inclusions, exclusions, constraints, permitted agents, and lifecycle state;
- implicit context merging is forbidden.

**Governing constraint:** Context must be declared or confirmed before operations occur within it.

### Intent

An explicit, verified declaration of what the user wants the system to do under defined constraints before execution.

Key frozen properties:

- not inferred from text, behavior, or pattern recognition;
- binds to exactly one context;
- revocable before execution;
- has explicit lifecycle/state;
- may be typed `explore`, `decide`, `generate`, `act`, or `verify`.

**Governing constraint:** No action may execute without a verified intent. Words alone do not constitute verified intent; the frozen System Model requires explicit user confirmation.

Historical lifecycle shown in the System Model:

```text
Unsignaled -> Signaled -> Verified -> Active -> Committed -> Revised / Revoked
```

### Agent

A scoped executor or advisor operating inside a context with explicit permissions.

Frozen properties:

- cannot escape context;
- cannot self-authorize;
- cannot modify its own permissions;
- inherits context constraints;
- agent types: `advisory`, `acting`, `explanation-only`;
- lifecycle: `active`, `suspended`, `revoked`.

### Node

A user-committed structural constraint that governs future reasoning.

- binding;
- structural;
- constrains reasoning;
- requires explicit commitment;
- may participate in action;
- reversible only by explicit revision.

### Pivot

A user-declared epistemic marker of perceived importance.

- non-binding;
- annotative;
- does not constrain reasoning by itself;
- does not require commitment;
- never triggers action;
- optional and reversible.

---

## 3. Responsibility Chain

```text
User Signal -> CP Verification -> AI Suggestion -> User Commitment -> Action
```

Frozen properties:

1. every link is logged with timestamp and actor identification;
2. no link may be skipped or compressed;
3. the complete chain must be reconstructible from logs alone; and
4. user commitment is the only advancement mechanism from signal to action.

**Accountability failure condition:** if any link cannot be reconstructed, the protocol has failed its interaction-level accountability guarantee for that action.

---

## 4. Guardian

The Guardian is **read-only**. It observes and judges; it may not mutate the state it evaluates.

### Gate decisions

| Decision | Meaning | Effect |
|---|---|---|
| **Allow** | Required constraints satisfied | Proceed |
| **Clarify** | Ambiguity or boundary concern | Trigger friction / request user input |
| **Refuse** | Constraint or verification failure | Block action and log reason |

### Checkpoint 1 — Post-Classification

| Rule | Frozen condition | Decision |
|---|---|---|
| PC-1 | signal is ambiguous | Clarify |
| PC-2 | signal is out of scope | Clarify |
| PC-3 | signal requests action without context | Clarify |
| PC-4 | signal is clear and no action is requested | Allow |

### Checkpoint 2 — Pre-Execution

| Rule | Frozen condition | Decision |
|---|---|---|
| PE-1 | no intent exists | Refuse |
| PE-2 | intent is not verified or active | Refuse |
| PE-3 | intent does not match action | Refuse |
| PE-4 | context is not open | Refuse |
| PE-5 | agent is not in context allowed list | Refuse |
| PE-6 | agent is not active | Refuse |
| PE-7 | agent type prohibits action type | Refuse |
| PE-8 | action exceeds agent permissions | Refuse |
| PE-9 | action violates context constraints | Refuse |
| PE-10 | unresolved friction exists | Refuse |
| PE-11 | all checks pass | Allow |

The canonical System Model is the source of these normalized rules. The recovered Implementation Specification and HTML runtime diverge from several of them; see the contradiction register.

---

## 5. Friction

Friction is a deliberate pause that gates commitment/action but not thought or exploration.

### Frozen triggers

```text
ambiguous_signal
unverified_intent
scope_boundary
permission_violation
high_risk_action
missing_context
conflict_detected
```

### Frozen resolutions

```text
user_clarified
user_confirmed
user_revised
user_abandoned
system_blocked
```

Frozen constraint: friction cannot be silently dismissed by the system; only user action resolves friction.

---

## 6. Frozen stores

| Store | Owned state |
|---|---|
| Context Store | Context objects |
| Intent Store | Intent objects |
| Node Store | Nodes and Pivots |
| Action Store | action requests, state, outputs |
| Friction Store | friction events |
| Log Store | append-only event log |

Access principles in the System Model include ID-based access, logged writes, append-only logs, and explicit cross-store joins rather than implicit state merging.

---

## 7. Frozen non-goals

The Freeze Declaration marks the following as verbatim frozen semantics:

> CP does NOT:
> - Model long-term cognition or belief evolution
> - Infer latent, hidden, or subconscious user goals
> - Optimize outcomes, performance, or correctness
> - Learn preferences across sessions
> - Predict future intent
> - Replace institutional, legal, or organizational governance
> - Claim alignment, safety, or ethics guarantees beyond interaction accountability
>
> Interpretation rule:
> If a consideration cannot be resolved at the interaction level, CP does not attempt to solve it.

---

## 8. Completeness and composability statement

> The Collaboration Protocol is intentionally complete only at the interaction level. It does not attempt to model long-horizon system evolution or collective learning. Instead, it guarantees semantic closure, intent traceability, and accountability for each human–AI decision cycle. This local completeness allows CP to function as a standalone interaction protocol, while remaining composable with external governance, human-in-the-loop, or institutional systems that operate at larger temporal or organizational scales.

This language is preserved because it limits the scope of any CP v1.0.1 claim.

---

## 9. Frozen evaluation scope

> This evaluation framework measures whether CP fulfills its interaction-level accountability claims. It does not measure optimization, efficiency, or user satisfaction, as these are explicitly outside CP's scope.

Primary frozen evaluation claims:

- no action without verified intent;
- context boundaries enforced;
- actions traceable to user decisions;
- ambiguity surfaces as friction rather than silent failure;
- accountability reconstructible from logs;
- agents cannot self-authorize or escape scope.

---

## 10. Conformance rule for future work

A future implementation should not claim **CP v1.0.1 conformance** merely because it asks for confirmation or logs actions. At minimum it must represent and enforce the frozen object, chain, Guardian, friction, store, and logging semantics without substituting incompatible rule meanings.

The recovered HTML runtime itself is not treated as proof of full conformance because it omits several frozen PE checks. This distinction is central to the preservation record.
