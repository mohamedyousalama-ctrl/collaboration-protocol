# 15 — Recovery and Reproducibility Guide

## 1. Purpose

This file defines how a future researcher, engineer, lawyer, or successor AI window can verify what was preserved and reconstruct specially encoded artifacts without relying on memory of the preservation conversation.

---

## 2. Checksum and representation semantics

The checksum files have different roles. Read `MANIFEST_README.md` before using them.

### Authoritative source-artifact manifest

`MANIFEST_SHA256.txt` records SHA-256 identities for the final recovered preservation staging set used to build this archive. A matching source hash establishes byte identity with the recovered source artifact that was hashed; it does not establish the historical creation date printed inside that artifact.

A path appearing in the manifest does **not by itself** prove that the original artifact bytes are present in Git under that same path. The repository may instead contain a direct text copy, ordered split parts, Base64 reconstruction, searchable conversion, source-bundle identity record, or an explicit exclusion/gap record.

### Recovered source-bundle identities

`MANIFEST_SOURCE_BUNDLES_SHA256.txt` fingerprints the major recovered bundles and now records their representation status explicitly. Several large binary source bundles were recovered and checksum-verified locally but could not be embedded as complete native binary payloads through the connected GitHub text-write interface used for this pass. Their hashes are provenance records; they are not claims that the bytes are recoverable from Git alone.

### Superseded staging snapshot

`SOURCE_ARTIFACT_SHA256.txt` is retained as preservation-process history but is **superseded**. Final audit spot checks found that several values in that earlier staging snapshot differ from the final recovered staging tree. Do not use it as the authoritative checksum manifest.

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

## 4. Reconstructing split textual sources

High-value large textual sources are stored in ordered `part-*` series under `archive/split-sources/`.

Read `archive/split-sources/README.md` before using them. It distinguishes two integrity classes:

- **EXACT-VERIFIED** — Git blob identities were checked against the corresponding recovered local source parts; ordered concatenation reconstructs the recovered byte stream.
- **SEARCHABLE-NORMALIZED** — readable/searchable content is retained, but connector/text normalization means the Git representation must not be described as byte-exact.

For an EXACT-VERIFIED source:

```sh
cat archive/split-sources/CP_Master_Knowledge_File.md/part-* > CP_Master_Knowledge_File.md
sha256sum CP_Master_Knowledge_File.md
```

Compare the result with the source SHA-256 in `archive/split-sources/README.md`.

The public-paper extraction is intentionally classed SEARCHABLE-NORMALIZED. For publication authority, use the external TechRxiv record documented in `archive/publication-and-ip/TECHRXIV_PUBLIC_RECORD.md`.

---

## 5. Reconstructing Klear `session.js`

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

Do not mistake reconstruction success for frozen-CP conformance. Klear is historical/applied evidence, and the recovered implementation diverges from a clean frozen-v1.0.1 reference implementation.

---

## 6. Security exclusion verification

The secret-bearing historical Klear environment file is **not** reconstructible from this Git repository by design.

Its identity-only SHA-256 is recorded in:

`archive/klear/SECURITY_REDACTION_NOTICE.md`

This is an intentional preservation exception. Secret values must not be reintroduced merely for archival completeness.

Third-party ACM template PDFs are likewise excluded and identified by hash in the security record.

---

## 7. Evidence hierarchy for future work

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

## 8. Frozen CP conformance protocol for future runtimes

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

## 9. Reproducing empirical work

### Klear finance

Before reporting a final comparative rate:

1. select/freeze one scenario inventory;
2. select one denominator rule;
3. link every scored row to exact response evidence;
4. recompute results from code rather than copying spreadsheet headline cells;
5. independently rate a blinded subset;
6. disclose architecture/model differences between systems;
7. preserve the exact dataset and scoring-script hash.

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

## 10. Reproducing the current authority-continuity benchmark

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

This benchmark family is a **current research direction**, not part of frozen CP v1.0.1 and not yet an empirically established result.

---

## 11. Future archive additions

For every newly recovered primary artifact:

1. add it without modifying historical bytes where technically possible;
2. compute SHA-256;
3. record source/provider and recovery date;
4. state what proposition the artifact supports;
5. state what it does not prove;
6. classify it as frozen/history/evidence/extension/hypothesis;
7. record whether its repository representation is exact, normalized, converted, or identity-only;
8. update `docs/11_ASSET_REGISTER.md` and the relevant lineage/contradiction records.

Do not delete superseded documents merely because a later account is cleaner. Mark them superseded and preserve the evidentiary chain.

---

## 12. Independent double-check checklist

Before using this repository for a paper, patent filing, public benchmark, investor/partner claim, or external research exchange, independently check:

- [ ] provenance dates against external records;
- [ ] all cited CP terms against the correct lineage;
- [ ] frozen-v1.0.1 claims against the canonical System Model/Freeze record;
- [ ] empirical denominators against row-level evidence;
- [ ] every “validated/proven” word against actual completed evidence;
- [ ] secrets and personal data before public release;
- [ ] third-party content/licensing;
- [ ] source artifact hashes and representation class;
- [ ] unresolved contradictions register;
- [ ] whether current working hypotheses have actually been tested.

A future result is stronger when the archive makes it easy to discover reasons the result might be wrong.
