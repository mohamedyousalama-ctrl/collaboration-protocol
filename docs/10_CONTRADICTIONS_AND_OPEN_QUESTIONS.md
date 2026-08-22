# 10 — Contradictions, Gaps, and Open Questions

This register is a required part of the archive. Contradictions are evidence about the evolution of the research, not defects to be erased from history.

---

## A. Provenance contradictions

### C-01 — Freeze declaration prints 2025; recovered provenance supports 2026

- **Artifact:** `cp_v1_0_1_freeze_declaration.md`
- **Printed date:** 28 Jan 2025
- **Provenance memo:** earliest supported CP activity 25 Jan 2026; explicitly says no 2025 support found.
- **Status:** unresolved historical date conflict.
- **Archive treatment:** preserve printed date; do not claim 2025 priority.

### C-02 — Technical audit also carries a 2025 date

- **Artifact:** `cp_v1_technical_audit_report.md`
- **Issue:** audit date conflicts with the available provenance chronology.
- **Status:** report preserved; date not independently validated.

---

## B. Frozen-spec contradictions

### C-03 — PC-3 / PC-4 definitions conflict

**System Model:**

- PC-3 action without Context -> Clarify
- PC-4 clear/no action -> Allow

**Implementation Specification:**

- PC-3 clear/no action -> Allow
- PC-4 clear/action requested -> Allow

**Materiality:** high. This changes routing semantics.

**Archive ruling:** normalized frozen reference follows System Model + Freeze Declaration.

### C-04 — PE-3 meaning conflicts

**System Model:** Intent does not match action -> Refuse.  
**Implementation Specification:** action Context ID differs from Intent Context ID -> Refuse.

The latter is narrower/different and cannot substitute silently for semantic action/intent mismatch.

### C-05 — PE-8 meaning conflicts

**System Model:** action exceeds Agent permissions -> Refuse.  
**Implementation Specification:** explanation-only Agent + non-communicate action -> Refuse.

The implementation rule covers only one permission/type case.

### C-06 — PE-9 meaning conflicts

**System Model:** action violates Context constraints -> Refuse.  
**Implementation Specification:** external action -> Clarify / high-risk action.

These encode different governance policies.

### C-07 — Frozen runtime omits PE-3, PE-8, PE-9

The recovered v1.0.1 persistent HTML runtime explicitly checks PE-1/2/4/5/6/7/10/11 but lacks the canonical PE-3/8/9 checks.

**Status:** frozen runtime not fully conformant to the frozen System Model.

---

## C. Terminology/lineage contradictions

### C-08 — “Seven Protocol Laws” exist in more than one formulation

The early research package and the July Master Knowledge File use different law names/statements. Later frozen CP is defined primarily through objects, Responsibility Chain, Guardian rules, Friction, and stores rather than the early law vocabulary.

**Archive treatment:** preserve both formulations as historical theory; do not call either the exact frozen v1.0.1 rule set.

### C-09 — Pivot vs Intent Pivot Point

- frozen **Pivot** = user-declared non-binding epistemic annotation;
- early **IPP** = researcher/system-identified material semantic branch.

They are conceptually related but not the same object.

### C-10 — Context vs Context Roots

- frozen **Context** = explicit user-declared operational scope;
- early **Context Roots** = provenance/source class for ambiguity-relevant context, including cross-session/environmental context.

They must remain distinct.

### C-11 — `CP` acronym collision

Early IFI formula uses “CP” for **Constraint Preservation**, while the overall protocol is also CP. Future papers should spell out Constraint Preservation in formulas/tables or define a different symbol.

---

## D. Evaluation contradictions / gaps

### C-12 — Klear result denominators differ across workbook generations

Recovered financial workbooks contain multiple overall pass-rate and completion-count framings (including 94%, 96%, 22/23, 26/27, and 30-row baseline denominators).

**Status:** not reconciled.

**Required resolution:** freeze one row-level dataset and recompute all metrics from code.

### C-13 — Klear comparison is architecture-asymmetric

Klear is purpose-built for the governance constraint; ChatGPT/Gemini baselines are general systems with prompt-level instructions. This demonstrates architecture effects but does not isolate CP from model/product differences.

**Required resolution:** same-model CP-off vs CP-on ablation plus strong governance baselines.

### C-14 — Tester/rater blinding

Historical test guides state expected CP behavior, making tester expectation effects plausible.

**Required resolution:** blinded second rater on a meaningful sample and reliability statistics.

### C-15 — Incident database researcher-final fields incomplete

The 52 candidate incidents have model-extracted/preloaded fields, but researcher-only final classification and transcript confirmation are incomplete in the recovered workbook.

**Required resolution:** Mohamed completes researcher fields; independent coder sample follows.

### C-16 — Simulation evidence generator absent from the provenance memo

The provenance record reports that the script/raw outputs behind historical simulated kappa and latency figures were not present in that project.

**Archive treatment:** preserve the numbers as historical claims; do not treat them as independently reproducible results until code/raw output is recovered.

### C-17 — Frozen validation template not executed

The recovered `v1_0_1_validation_tests.md` is a template with blank certification/status fields.

**Status:** no completed frozen-v1.0.1 conformance certification in that artifact.

---

## E. Klear implementation contradictions / risks

### C-18 — Guardian can fail open

`guardian.js` returns `allow` on evaluation failure and parse failure.

**Risk:** a governance dependency failure can become permission to proceed.

### C-19 — Streaming monitor continues on error

`stream_monitor.js` returns continuation on monitor evaluation/parse errors.

**Risk:** mid-generation protection can disappear silently under failure.

### C-20 — Retry bypasses normal CP1 classification

`session.js` explicitly skips IPP classification, ICD filtering, and Guardian CP1 for retry.

**Risk:** alternate execution path has different governance semantics.

### C-21 — `responsibility_chain_intact` hard-coded true

Report code sets the field to true rather than deriving it from a formal reconstruction check.

**Risk:** reporting can overstate chain integrity.

### C-22 — Klear is not a clean frozen-v1 reference

Klear mixes early theory, extensions, and implementation-specific rules.

**Archive treatment:** applied evidence only.

---

## F. Safety Floor open questions

### C-23 — Fidelity and safety can conflict

This is a conceptual result, not a contradiction to erase. It means CP must not equate “user-authorized” with “clinically safe.”

### C-24 — Safety Floor content requires expert authority

The architecture can specify a non-suppressible layer, but a governance framework cannot invent clinical truth. Qualified expert review and version control are required.

### C-25 — IFI-H weighting unvalidated

Historical IFI-H weighting and SCS influence are proposals. Sensitivity and expert-validation studies are still needed.

---

## G. Current authority-continuity open questions

### C-26 — How precisely must Intent bind mutable transaction state?

Frozen Intent includes scope/constraints but does not define a universal transaction-version schema. Domain implementations must decide which fields are material and bind them explicitly.

### C-27 — What invalidates prior authorization?

Potential invalidators include payload/version, actor/permission, Context state, target, constraints, time/expiry, policy, and unresolved exceptions. A future specification must define invalidation semantics without turning every tiny change into needless reapproval.

### C-28 — Idempotency/replay are not fully frozen CP semantics

A duplicate execution can violate practical intent even if each individual call superficially passes a static authorization check. Future agentic CP work must integrate replay/idempotency without claiming the existing freeze already solved it.

### C-29 — Distributed state races

In multi-system execution, state may change between Guardian evaluation and tool commit. A future implementation may need transactional/atomic authorization checks, optimistic concurrency, locks, or version preconditions.

### C-30 — Conventional systems may already solve some cases

Modern ERP/IT platforms often bind approvals to versioned objects, permissions, policies, and workflow state. CP's incremental value must be tested rather than assumed.

---

## H. Intellectual-property / publication gaps

### C-31 — Provisional application PDF is blank in filing fields

The recovered patent application is evidence of drafting, not filing receipt evidence.

### C-32 — Historical filing number/date claim lacks receipt in this archive

Other project documents report a provisional filing. Add the authoritative USPTO receipt to close this gap.

### C-33 — Novelty not independently established

Internal use of a term first does not prove worldwide novelty. A dedicated literature/prior-art review is needed before strong novelty language.

---

## I. Open scientific questions worth prioritizing

1. Can IPPs be annotated reliably across independent coders and domains?
2. Does SII occur at a meaningful rate in representative real-world tasks?
3. Does CP enforcement add value over strong approval/RBAC/policy architectures?
4. Does external enforcement outperform prompt-only CP when the model is held constant?
5. Can authorization continuity be formalized without excessive false refusals?
6. Can Responsibility Chain reconstruction be made independently verifiable rather than self-reported?
7. How should uncertainty/classifier failure affect Guardian behavior?
8. What belongs in a future CP version versus an external composable layer?
9. Can domain safety remain orthogonal to intent while still producing a coherent user experience?
10. Can a public benchmark define stable ground truth for semantic and execution authority?

This register should be updated, not deleted, as each issue is resolved.
