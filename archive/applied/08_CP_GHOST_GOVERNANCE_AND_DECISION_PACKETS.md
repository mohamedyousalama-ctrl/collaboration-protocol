# 08 — CP / Ghost Governance and Decision Packets

**Version:** 1.0

## Placement

### CP
CP governs consequential collaboration/action:
- confirmed Context;
- verified human Intent;
- read-only Guardian;
- friction proportional to consequence;
- Responsibility Chain;
- append-only evidence;
- no self-authorization.

### Ghost principles
Ghost contributes:
- continuity;
- Presence;
- memory/inference never grants authority;
- selected retention;
- continuous calibration;
- no silent power increase.

Runtime vehicle object = **Vehicle Evidence Episode**, not “Ghost.”

## CP adapter

### Context
Only current/confirmed facts:
- contract version;
- observations;
- evidence assertions;
- witness health;
- customer/human responses;
- official incident/report state.

### Intent
Human intent:
- observe;
- verify;
- contact;
- confirm incident;
- request external corroboration;
- initiate recovery;
- request future at-rest inhibit.

AI cannot invent the human intent.

### Guardian
Read-only checks:
- actor authority;
- evidence state/family requirements;
- legal/capability permission;
- customer-challenge policy;
- privacy purpose;
- official incident prerequisite;
- external-query authorization;
- at-rest proof for future actuator.

Guardian can block; it cannot execute.

### Friction
- WATCH: none.
- VERIFY: authorized operator.
- HIGH_RISK: explicit human review.
- official incident: human confirmation.
- government query: explicit purpose/authorization.
- future restart inhibition: dual authorization + at-rest proof + separate legal/safety approval.

### Responsibility Chain
Record:
- observer;
- derivation/model;
- proposer;
- reviewer;
- authorizer;
- executor;
- verifier.

## Decision Packet

```text
DecisionPacket
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

## External corroboration example

Intent: `REQUEST_INCIDENT_CORROBORATION`

Guardian verifies:
- state/agreement permits it;
- operator authorized;
- purpose valid;
- fields minimized;
- official incident ref if required;
- query not repeated unnecessarily.

Only then GCG executes.

## Incident confirmation

AI may propose:
> “Trajectory, integrity and external evidence are mutually consistent with serious unauthorized-use risk.”

AI may not say:
> “I confirmed theft.”

Human decides `CONFIRM_INCIDENT` or `REJECT/CONTINUE_VERIFY`.

## Explainability

Expose:
- facts;
- reason codes;
- model/rule versions;
- benign explanations;
- uncertainty;
- state change;
- what evidence would resolve uncertainty.

Do not expose hidden chain-of-thought.

## No silent authority growth

A better future model does not automatically gain:
- police access;
- immobilizer rights;
- broader phone data;
- new retention;
- higher response authority.
