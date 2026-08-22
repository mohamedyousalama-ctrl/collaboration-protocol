# 04 — Theory and Research Program

## 1. Research objective

The CP research program asks how human–AI systems can make interpretive and execution authority explicit, inspectable, and testable rather than leaving it embedded in model inference. Two related but distinct research lines emerge from the recovered record:

1. **Semantic-authority line** — identify and measure unauthorized resolution of ambiguity (SII / IPP / ICD / IFI / Context Roots).
2. **Execution-accountability line** — ensure consequential action is covered by verified Intent, valid Context, authorized Agent scope, Guardian approval, and a reconstructible Responsibility Chain (frozen CP v1.0.1).

The current frontier attempts to connect those lines by testing whether authorization remains valid **through execution**, not merely at the moment of clarification or approval.

---

## 2. Falsifiable propositions in the early theory lineage

Historical research packages propose hypotheses such as:

### SII prevalence / awareness

- Silent intent inference may occur frequently in complex tasks.
- Users may often be unaware of the interpretive assumptions made on their behalf.

Historical numeric thresholds (`>60%` prevalence, `>70%` unawareness) are explicitly framed in the research package as **hypotheses requiring empirical calibration**, not results.

### IPP reliability

If IPPs are a useful research construct, trained coders should be able to identify them with acceptable inter-rater reliability. The historical program uses `kappa > 0.7` as a target criterion.

### ICD effect

The early framework predicts that increasing user control over ambiguity resolution may increase intent fidelity but also increase interruption/time burden. This is a research trade-off to measure, not an established benefit.

### IPP intervention timing

The program proposes comparing:

- no pivot exposure;
- post-hoc exposure;
- real-time surfacing; and
- interactive intervention.

The ordering of expected outcomes in historical documents is a prediction, not a completed experiment.

---

## 3. Proposed early measurement system

### 3.1 Intent Fidelity Index

Historical formula:

```text
IFI = 0.4(SA) + 0.3(Constraint Preservation) + 0.3(SS)
```

Research obligations before treating IFI as a validated instrument include:

- establish inter-rater reliability for SA;
- establish how Constraint Preservation is operationalized across task types;
- examine whether subjective satisfaction creates inflation or disagreement with externally grounded outcome criteria;
- test weight sensitivity rather than treating `0.4/0.3/0.3` as universal constants; and
- distinguish fidelity to user intent from safety/correctness.

### 3.2 Semantic Materiality Proxy

Historical formula:

```text
M(a) = [alpha * D_sem + beta * C_mag + gamma * (1 - R)] * CF(a)
```

Open empirical questions:

- Can candidate interpretations be generated consistently enough for `D_sem` to be stable?
- Can consequence magnitude be scored reproducibly across domains?
- How should reversibility be defined for partially reversible operations?
- How should the Context Factor be calibrated?
- Do thresholds generalize across low-stakes and high-stakes settings?

The current archive treats SMP as a **computable research proposal**, not as a validated universal classifier.

### 3.3 IPP Log as accountability substrate

The IPP Log can be tested independently of any particular IPP detector. A system can record:

1. the original user signal;
2. the ambiguity branch;
3. candidate interpretations;
4. whether the user was asked;
5. the adopted interpretation;
6. the source/context used; and
7. the resulting output/action.

A central empirical question is whether such a record materially improves post-hoc responsibility reconstruction compared with ordinary conversation logs.

---

## 4. Frozen CP v1.0.1 hypotheses and measures

The frozen evaluation program deliberately narrows scope. Its primary questions are structural:

### H-F1 — Verified Intent Gate

**Question:** Does any action execute without a verified/active Intent?

**Pass condition:** zero unauthorized executions in tested pathways.

### H-F2 — Context Boundary Enforcement

**Question:** Does an operation cross a closed/invalid context boundary without Guardian refusal/friction?

**Pass condition:** boundary violations do not execute silently.

### H-F3 — Agent Authority Enforcement

**Question:** Can an Agent act when absent from the Context allowed list, inactive, wrong type, or insufficiently permitted?

**Pass condition:** the relevant PE checks refuse the action.

### H-F4 — Responsibility Reconstruction

**Question:** Can an evaluator reconstruct Context, Intent, verification, Guardian decision, commitment, and action from the logs?

**Pass condition:** the required chain is present and linked.

### H-F5 — Friction Persistence

**Question:** Can unresolved friction be silently bypassed or auto-resolved?

**Pass condition:** unresolved friction blocks execution until a valid user resolution exists.

These are binary/structural accountability tests rather than claims about efficiency or preference.

---

## 5. Reference-runtime requirement

The recovered artifacts reveal a research-method problem: the frozen HTML runtime and the recovered implementation specification do not perfectly implement the frozen System Model. Therefore future CP studies should first construct a **Reference Runtime** directly from the frozen semantics and pass a conformance suite before comparing outcomes.

Recommended layers:

1. **Oracle-State CP** — all classifications/state facts supplied perfectly, testing only CP enforcement logic.
2. **End-to-End CP** — an LLM/classifier infers relevant state from natural-language input, testing classification plus enforcement.
3. **Prompt-only CP** — CP rules placed in prompts without external enforcement.
4. **Enforced CP** — independent state/gate layer controls tool execution.

This separates failures in the governance protocol from failures in semantic classification.

---

## 6. Strong baseline requirement

A credible modern benchmark should not compare CP only to a raw general-purpose model. Strong baselines should include, where possible:

- frontier LLM agent with ordinary tool calling;
- final-confirmation workflow;
- RBAC + policy + approval + audit logs;
- multi-agent workflow with an approval engine;
- domain-native enterprise governance stack; and
- CP-governed execution with the same model/tools.

The relevant research question is the **incremental accountability value** CP contributes beyond existing controls.

---

## 7. Naturalistic corpus program

### Recovered instrument

The `IPP_Extraction_Protocol.md` specifies a two-stage methodology:

- LLM-assisted extraction of candidate incidents and observable context;
- researcher-only final classification and ground-truth intent assignment.

This separation is methodologically important: the model may propose candidates, but it must not be allowed to manufacture the researcher’s final label.

### Recovered database

`CP_Incident_Database_v1.xlsx` contains 52 incident records with an explicit researcher-only classification block and aggregate formulas.

### Required completion before publication-grade analysis

1. verify quoted user language against source transcripts;
2. set researcher-final incident class;
3. set IPP type/materiality/context factor where applicable;
4. record ground-truth intent by the human researcher;
5. mark confirmation status;
6. exclude unverified rows from headline aggregates;
7. run a blinded second-coder reliability sample; and
8. document sampling bias because the corpus is drawn from the researcher's own intensive AI work.

---

## 8. Klear empirical program

The financial evaluation work is valuable because it moves from theory into an implemented governance layer and generates behavior that can be compared under repeated scenarios. It is also methodologically asymmetric: Klear was purpose-built for constraints that general-purpose baselines did not structurally enforce.

A publication-grade version therefore needs to distinguish:

- **architecture comparison** rather than “model intelligence” comparison;
- pilot evidence from generalizable findings;
- model backend effects from governance-layer effects;
- tester expectations/blinding;
- scenario completion/denominator inconsistencies;
- audit evidence from manually scored outcomes; and
- known Klear defects.

The right causal ablation is same model + same tools + same task, with CP enforcement enabled vs disabled, plus strong conventional governance baselines.

---

## 9. Safety Floor research program

The health extension introduces a critical theoretical distinction:

> **Intent fidelity and domain safety/correctness are not the same objective.**

A valid system can faithfully follow a user's selected interpretation yet still omit a domain-required safety response. Safety Floor research therefore belongs on a separate axis from frozen CP’s interaction-accountability claims.

Key research questions:

- Does Safety Floor activation improve qualified-expert safety ratings?
- Can the required assertion set be defined and versioned by qualified domain experts?
- What is the false-positive burden of domain activation?
- Does Safety Floor content remain stable under generation changes?
- Does adding safety assertions reduce user comprehension or create alert fatigue?
- Can intent fidelity and safety be reported separately instead of collapsed into a single score?

The recovered H5/IFI-H proposal is preserved, but expert clinical validation is still required.

---

## 10. Current frontier study: zero-ambiguity post-approval drift

### Research motivation

Modern agents often already summarize a task and ask for confirmation. A CP benchmark that only shows “CP asks a clarification” has weak differentiation against contemporary systems.

The stronger test removes pre-approval ambiguity entirely.

### Experimental principle

Every scenario begins with:

- explicit user identity/authority;
- explicit Context;
- exact operation;
- exact target;
- exact parameters;
- explicit confirmation/approval.

Then, **after approval and before execution**, inject one material state change.

Candidate mutations:

1. target record/version changes;
2. amount or payload changes;
3. legal entity/context changes;
4. execution destination changes;
5. permission is revoked;
6. executing Agent changes;
7. a constraint becomes active;
8. an unresolved exception/friction appears;
9. approval expires;
10. one agent mistranslates the approved operation during handoff;
11. context closes/archives;
12. policy/risk state changes.

Positive controls retain unchanged state and must still execute.

### Core question

At execution time, is there still a valid verified Intent whose exact scope covers the candidate action, a valid Context, a currently authorized Agent, satisfied constraints, no unresolved friction, and a reconstructible Responsibility Chain?

### Primary endpoint candidate

**End-to-End Authorization Fidelity (EAF)** — proportion of consequential executed actions that remain exactly covered by current human authority at the moment of execution.

Secondary endpoints can decompose failures into stale approval, context contamination, permission drift, action substitution, and reconstruction failure.

---

## 11. Research roadmap preserved by this archive

### Phase A — Conformance

- reconcile canonical frozen semantics;
- build deterministic Reference Runtime;
- build conformance suite for every PC/PE rule, store, lifecycle, friction rule, and chain property.

### Phase B — Structural efficacy

- run Oracle-State CP vs non-CP governance baselines;
- inject zero-ambiguity execution-state drift;
- measure authorization/reconstruction outcomes.

### Phase C — End-to-end semantic efficacy

- add natural-language state classification;
- measure false-positive and false-negative friction/refusal;
- separate classifier errors from protocol errors.

### Phase D — Domain benchmark

Candidate high-consequence domains preserved in the current frontier include:

- accounts payable/payment execution;
- IT change management;
- financial close/journal actions;
- AML/regulatory workflow;
- industrial process control;
- desalination dispatch; and
- other multi-system workflows with delayed execution.

### Phase E — Public benchmark

The broader program has repeatedly proposed a public intent/authority benchmark family (historically “IFI-Bench”). A defensible release should contain sanitized scenarios, formal ground truth, reproducible scoring, strong baselines, and explicit versioning.

---

## 12. Scientific discipline

The research program is strongest when it treats CP as falsifiable. A negative result is informative:

- If strong RBAC/approval systems match CP on exact authorization continuity, the incremental CP moat is smaller than hypothesized.
- If a frozen-rule Reference Runtime cannot outperform prompt-only behavior under controlled injections, the enforcement thesis needs revision.
- If IPP coders cannot reach acceptable reliability, IPP taxonomy/materiality needs refinement.
- If friction causes unacceptable false positives without measurable accountability gains, the intervention policy must change.
- If responsibility-chain reconstruction does not help independent reviewers understand authority, the logging model is insufficient.

This archive therefore preserves both the proposals and the failure modes needed to test them.
