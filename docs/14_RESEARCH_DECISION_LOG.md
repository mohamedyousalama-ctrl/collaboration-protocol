# 14 — Research Decision Log

**Purpose:** Preserve major research-direction decisions so later papers, benchmark designs, and successor AI work do not accidentally revert to superseded framings.

This is a living research-history document. Entries describe decisions and working conclusions at the time they were made; they do not silently convert hypotheses into established facts.

---

## RD-01 — Ambiguity is a real CP concern, but not the strongest modern differentiator

**Status:** ACTIVE RESEARCH DECISION  
**Rationale:** Contemporary AI-agent products commonly summarize tasks, authenticate users, ask for confirmation, use approval workflows, and maintain audit trails. A benchmark that merely shows “CP asks before acting” is therefore too weak to establish a distinctive systems contribution.

**Decision:** Preserve ambiguity/SII/IPP work as a foundational semantic-authority research line, but do not make clarification-before-action the sole or primary competitive thesis for modern autonomous-agent benchmarking.

---

## RD-02 — Move the primary agentic benchmark to post-approval authority drift

**Status:** ACTIVE WORKING DIRECTION

**Research question:**

> After the human has already given an explicit, unambiguous authorization, does the action eventually executed remain inside that exact authority after time, state changes, agent handoffs, permission changes, context changes, and external-system transformations?

**Reason:** A final confirmation proves what the user authorized at one moment. It does not prove that the same authorization remains valid when the action actually executes.

**Working formulation:**

> Final confirmation is a snapshot. Continuous authorization integrity is an execution-time property.

---

## RD-03 — Use zero-ambiguity scenarios to isolate the execution-governance claim

**Status:** ACTIVE BENCHMARK PRINCIPLE

All core authority-drift scenarios should make the original human instruction and approval fully explicit. The benchmark then mutates only post-approval state.

Required mutation families include:

- payload/amount drift;
- target/version drift;
- legal-entity or Context drift;
- destination drift;
- permission revocation;
- Agent substitution;
- new constraint activation;
- unresolved exception/Friction;
- context closure;
- approval expiry where modeled;
- cross-agent semantic corruption; and
- partial-workflow continuation after a material failure.

Unchanged positive controls must execute. A system that blocks every action is not successful.

---

## RD-04 — Distinguish prompt-CP from enforced CP

**Status:** REQUIRED ABLATION

A future study should not use “CP in the system prompt” as equivalent to CP enforcement.

Recommended conditions:

1. same model/tools, ordinary agent;
2. same model/tools + final confirmation;
3. same model/tools + RBAC/policy/approval/audit;
4. same model/tools + CP rules in prompt only;
5. same model/tools + externally enforced CP Reference Runtime;
6. strong domain-native enterprise baseline where an authorized sandbox is available.

This isolates the architectural claim that a governance rule enforced outside the model may behave differently from a rule the model is merely instructed to follow.

---

## RD-05 — Build a clean CP Reference Runtime before efficacy claims

**Status:** REQUIRED PRECONDITION

The recovered historical runtime is not a reliable conformance oracle because it omits canonical PE-3, PE-8, and PE-9, while the Implementation Specification also diverges from the System Model.

**Decision:** Future benchmark work requires:

- deterministic Reference Runtime built directly from the frozen semantic source;
- executable conformance tests for every PC/PE rule;
- explicit store/state invariants;
- trace-reconstruction tests; and
- separate Oracle-State and End-to-End conditions.

---

## RD-06 — Separate classification failure from governance failure

**Status:** REQUIRED RESEARCH DESIGN

Two experimental layers are required:

### Oracle-State CP

The benchmark supplies correct Context, Intent, Agent, permissions, constraints, Friction, and candidate action as structured state. This tests only the enforcement architecture.

### End-to-End CP

An LLM/classifier must infer or construct relevant structured state from natural-language/system inputs. This tests semantic interpretation plus enforcement.

A failure in End-to-End CP should not automatically be attributed to the frozen Guardian rules if the underlying classification was wrong.

---

## RD-07 — Strong conventional governance is the correct baseline

**Status:** ACTIVE METHODOLOGICAL DECISION

Raw ChatGPT/Gemini-style baselines are insufficient for the primary agentic claim. Mature enterprise systems already use permissions, approvals, policy engines, and audit records.

The scientific comparison should therefore ask:

> What incremental accountability does CP contribute beyond strong conventional controls?

If CP ties those systems, that is a meaningful negative result and should reduce the scope of the claimed contribution.

---

## RD-08 — Accounts Payable / Payments is the leading near-term benchmark vertical

**Status:** CURRENT LEADING RECOMMENDATION; NOT FROZEN

### Why this vertical ranks highly

- consequential state mutation is objectively observable: money/ledger state changes;
- authorization can be represented by exact transaction fields;
- approvals naturally age while invoices, destinations, exceptions, and permissions may change;
- the workflow spans document ingestion, ERP state, approvals, payment execution, bank interaction, and supplier communication;
- safe synthetic ERP/payment environments can be built without moving real money;
- strong Saudi and global enterprise comparators already exist.

### Candidate primary outcome

**Exact Authorized Payment Rate** or the domain-neutral **End-to-End Authorization Fidelity (EAF)**.

A valid execution should continue to match, at minimum:

- legal entity;
- supplier;
- invoice and invoice version;
- purchase-order/receipt state where relevant;
- amount;
- currency;
- destination/account;
- operation type;
- current Agent identity/state/permissions;
- Context state;
- applicable constraints/policies/exceptions; and
- reconstructible authorization provenance.

### Core falsification condition

If a well-configured conventional ERP approval/RBAC/policy architecture provides equivalent exact execution-state binding and reconstruction under the same scenario set, CP has little incremental moat in this vertical.

---

## RD-09 — Current Saudi/global comparator evidence for the finance benchmark

**Evidence status:** PUBLIC VENDOR CLAIMS / PRODUCT DOCUMENTATION, observed 22 August 2026. These sources establish advertised capabilities, not independent performance validation.

### Agent.sa — finance agent

Official page: `https://agent.sa/industries/finance-agent/`

Publicly described workflow includes:

1. invoice arrival and document extraction;
2. validation against purchase order and exception routing for approval;
3. direct posting of matching invoices to the financial system;
4. payment scheduling/execution at due date; and
5. supplier status communication.

The page also describes three cooperating roles: document reading, systems connection, and communication. This makes Agent.sa a particularly relevant Saudi multi-agent comparator for end-to-end authorization continuity.

### Oracle Fusion — Payables and Payments Agents

Saudi Oracle page: `https://www.oracle.com/sa/applications/fusion-ai/`  
Current feature matrix: `https://docs.oracle.com/en/cloud/saas/fusion-ai/aiafl/ai-erp.html`  
Payments Agent documentation: `https://docs.oracle.com/en/cloud/saas/readiness/erp/26b/fins26b/26B-fin-wn-f43659.htm`

Oracle currently documents Payables and Payments agents that ingest/normalize invoices, match them to purchase orders/receipts, perform policy/fraud/tax checks, route work for approval/payment, interact with bank/payment programs, support execution, and monitor acknowledgements/exceptions.

This is a stronger enterprise baseline than a raw LLM because the system already operates inside an ERP authority/workflow model.

### Lucidya AI Agent — governance comparator

Official page: `https://www.lucidya.com/ai-agent`

Lucidya publicly describes role-based access, configurable approval workflows, complete action audit trails, a kill switch, a policy engine, compliance controls, and human escalation outside defined parameters. It also advertises consequential actions such as refund processing, billing resolution, account changes, and subscription management.

Research implication: these capabilities reinforce RD-01. CP cannot claim differentiation merely because it has confirmation, permissions, approval, policy, or logging.

---

## RD-10 — Industrial process control remains a high-consequence second research track

**Status:** STRONG ALTERNATIVE / HIGH-SCIENCE-VALUE TRACK

The preserved industrial analyses rank live process-control/state-transition agents highly because:

- physical context changes after approval;
- DCS/interlock systems protect hard process limits but may not encode the semantic scope of the human authorization;
- the action boundary is objective (e.g., a DCS write); and
- high-fidelity simulators can inject controlled state changes safely.

The strongest industrial example in the preserved analysis is an Acid Gas Removal/process-control agent, with candidate metric **Execution-State Authorization Integrity (ESAI)**.

The principal falsification risk is also preserved: traditional DCS interlocks, process constraints, and a simple live-state recheck may already cover most failures CP would target. This must be tested, not assumed.

---

## RD-11 — Finance and industrial benchmarks test the same deeper construct

**Status:** SYNTHESIS

The domains differ, but the underlying predicate is the same:

```text
At execution time,
there exists current explicit human authority
whose exact scope covers this exact mutation,
inside a valid Context,
performed by a currently authorized Agent,
under satisfied constraints,
with no unresolved blocking Friction,
and with a reconstructible Responsibility Chain.
```

Finance turns this into money/ledger mutation integrity. Industrial control turns it into actuator/setpoint integrity. IT change turns it into approved change-set integrity.

This suggests that the publishable core may be a **domain-neutral authorization-continuity benchmark**, with multiple domain tracks.

---

## RD-12 — Do not overclaim idempotency, replay, or distributed-transaction safety as already solved by frozen CP

**Status:** ACTIVE SCOPE GUARD

Frozen CP gives strong vocabulary for Intent/action match, Context validity, Agent authority, constraints, Friction, and traceability. It does not fully define:

- idempotency semantics;
- duplicate tool-call/replay handling;
- distributed transaction atomicity;
- time-of-check/time-of-use races;
- lock/version-precondition protocols; or
- recovery/compensation semantics after partial execution.

Those are important future engineering/research extensions. They should be tested around CP, not silently attributed to v1.0.1.

---

## RD-13 — Candidate positioning sentence to earn, not claim yet

**Status:** RESEARCH TARGET

> “CP provides continuous authorization integrity for autonomous AI workflows, ensuring that the action ultimately executed is still the action the human actually authorized—even after AI reasoning, agent handoffs, system changes, and time have intervened.”

This sentence is intentionally stored as a **target claim**. It should only move into an abstract/product claim after controlled experiments support it against strong baselines.

---

## RD-14 — Negative results are part of the research asset

**Status:** PERMANENT INTEGRITY RULE

The program should preserve and publish where appropriate:

- CP conformance failures;
- baseline systems that match CP;
- false refusals;
- classifier failures;
- user-friction costs;
- logging/reconstruction failures;
- domain safety conflicts; and
- cases where ordinary deterministic controls are superior.

The goal of the repository is to protect the research record, not to manufacture a success narrative.
