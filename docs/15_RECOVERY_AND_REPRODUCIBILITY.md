# 15 — Recovery and Reproducibility Guide

## 1. Purpose

This file defines how a future researcher, engineer, lawyer, or successor AI window can verify what was preserved and reconstruct the specially encoded artifacts without relying on memory of this conversation.

---

## 2. Source-identity verification

Two root manifests are authoritative preservation aids:

- `MANIFEST_SOURCE_BUNDLES_SHA256.txt` — fingerprints the major recovered source bundles represented by this archive.
- `SOURCE_ARTIFACT_SHA256.txt` — fingerprints the individual recovered staging artifacts, including many files that are also preserved directly in Git.

Verification procedure for any recovered source file:

```sh
sha256sum <file>
```

Compare the result with the exact path/hash entry in the manifest.

A matching hash proves byte identity with the preserved source used in the August 2026 archive pass. It does not prove the historical creation date printed inside the artifact.

---

## 3. Reconstructing the incident workbook

The 52-row `CP_Incident_Database_v1.xlsx` is preserved losslessly as Base64 text parts under:

`archive/research-lineage-2026-01/binary/`

Reconstruct:

```sh
cd archive/research-lineage-2026-01/binary
cat CP_Incident_Database_v1.xlsx.b64.part-* | base64 -d > CP_Incident_Database_v1.xlsx
sha256sum CP_Incident_Database_v1.xlsx
```

Expected:

```text
bytes:   31471
sha256:  3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a
```

The workbook is an empirical **candidate corpus**, not a completed ground-truth dataset. Researcher-only final classification fields were incomplete in the recovered version.

---

## 4. Reconstructing Klear `session.js`

The sanitized Klear session source is preserved as sequential parts because of repository-connector write-size constraints.

```sh
cd archive/klear/sanitized-chat-inputs/05_klear_source_code
cat session.js.part-000 session.js.part-001 session.js.part-002 session.js.part-003 > session.js
sha256sum session.js
```

Expected:

```text
bytes:   28599
sha256:  04ccb4eb0b23d55d3d55e4f94bb10af54428ad1f152b3506e61e418d694269c6
```

Do not mistake reconstruction success for frozen-CP conformance. The implementation evidence documents retry-path and reporting behavior that diverges from an ideal reference runtime.

---

## 5. Security exclusion verification

The secret-bearing historical Klear environment file is **not** reconstructible from this Git repository by design.

Its identity-only SHA-256 is recorded in:

`archive/klear/SECURITY_REDACTION_NOTICE.md`

This is an intentional preservation exception. Secret values must not be reintroduced merely for archival completeness.

---

## 6. Evidence hierarchy for future work

When two artifacts conflict, use this order of reasoning rather than choosing whichever source supports a preferred conclusion:

1. exact primary artifact / raw data;
2. version/freeze declaration governing the artifact family;
3. executable code and machine traces for implementation behavior;
4. contemporaneous provenance records and external timestamps;
5. empirical analysis derived from the raw data;
6. master summaries and handover documents;
7. later narrative descriptions.

A later summary may clarify history, but it must not silently overwrite a primary-source contradiction.

---

## 7. Frozen CP conformance protocol for future runtimes

Any future implementation claiming **CP v1.0.1 conformance** should be tested against the normalized frozen semantic record, not against historical Klear behavior.

At minimum verify:

- Context declaration/confirmation requirements;
- Intent verification and lifecycle;
- Agent allowed-list/state/type/permission controls;
- Node and Pivot distinction;
- all PC-1 through PC-4 rules;
- all PE-1 through PE-11 rules;
- all seven frozen Friction trigger types;
- all five frozen Friction resolution types;
- exactly three Guardian decisions;
- six stores and logging obligations;
- append-only reconstruction of the Responsibility Chain;
- frozen non-goals/evaluation scope.

A conformance test should fail closed when a required frozen rule is absent. Do not certify a runtime merely because its UI or terminology resembles CP.

---

## 8. Reproducing empirical work

### Klear finance

Before reporting a final comparative rate:

1. select/freeze one scenario inventory;
2. select one denominator rule;
3. link every scored row to exact response evidence;
4. recompute results from code rather than copying spreadsheet headline cells;
5. independently rate a blinded subset;
6. disclose architecture/model differences between systems;
7. preserve the exact dataset and scoring script hash.

### Naturalistic incident corpus

Before using the 52 rows as confirmed empirical evidence:

1. verify A3/A8 quotations against original transcripts;
2. complete C1–C10 researcher-only fields;
3. set C9 confirmation status;
4. exclude unverified rows from headline metrics;
5. independently code a sample; and
6. compute inter-rater reliability.

### Safety Floor / IntentHealth

Treat health results as pilot-driven research until qualified clinical reviewers validate the relevant safety assertions and scoring process.

---

## 9. Reproducing the current authority-continuity benchmark

Use the following causal separation:

```text
same model + same tools + same task fixtures
```

Compare:

1. ordinary agent;
2. final confirmation only;
3. conventional RBAC/policy/approval/audit controls;
4. prompt-only CP;
5. externally enforced CP Reference Runtime.

For the core benchmark, eliminate ambiguity at authorization time and inject only post-approval state/authority changes. Maintain stable positive controls that must execute.

Record exact state versions before approval, at Guardian evaluation, and at mutation execution.

---

## 10. Future archive additions

For every newly recovered primary artifact:

1. add it without modifying historical bytes;
2. compute SHA-256;
3. record source/provider and recovery date;
4. state what proposition the artifact supports;
5. state what it does not prove;
6. classify it as frozen/history/evidence/extension/hypothesis;
7. update `docs/11_ASSET_REGISTER.md` and the relevant lineage/contradiction records.

Do not delete superseded documents. Mark them superseded and preserve the chain.

---

## 11. Independent double-check checklist

Before using this repository for a paper, patent filing, public benchmark, or investor/partner claim, independently check:

- [ ] provenance dates against external records;
- [ ] all cited CP terms against the correct lineage;
- [ ] frozen-v1.0.1 claims against the canonical System Model/Freeze record;
- [ ] empirical denominators against row-level evidence;
- [ ] every “validated/proven” word against actual completed evidence;
- [ ] secrets and personal data before public release;
- [ ] third-party content/licensing;
- [ ] source artifact hashes;
- [ ] unresolved contradictions register;
- [ ] whether current working hypotheses have actually been tested.

A future result is stronger when the archive makes it easy to discover reasons the result might be wrong.
