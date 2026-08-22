# 09 — Provenance and Priority Record

## 1. Purpose

This document answers a narrow academic question:

> **What dates and authorship/provenance facts are actually supported by the recovered evidence, and which dates are merely printed inside historical artifacts?**

It does not decide legal patent priority. It preserves the evidence needed for later legal or academic review.

---

## 2. Strongest currently supported chronology

### 25 January 2026 — earliest recovered CP activity

`archive/provenance/CP_Provenance_Record.md` records provider/session-side filenames dated 25 January 2026 for:

- CP research planning;
- first full research-package synthesis;
- package v2.0 refinements;
- v3 evaluation work; and
- v4 realistic-assessment work.

It also records matching file modification dates for the January 2026 research packages.

**Preservation status:** earliest supported CP activity in the recovered provenance record.

### 26 January 2026 — publication conversion / submission workflow

The provenance memo records:

- arXiv conversion planning and master prompt;
- JAIR submission guidance; and
- a SocArXiv/OSF submission episode.

The memo identifies external provider timestamps (submission pages/emails) as stronger clocks if recovered.

### 2 February 2026 — public TechRxiv preprint

The public TechRxiv preprint is externally timestamped **2 February 2026** and is distributed as a preliminary, non-peer-reviewed report under CC BY 4.0.

Public identifier:

`https://doi.org/10.36227/techrxiv.177006153.39365379/v1`

Title:

*The Collaboration Protocol: Silent Intent Inference as an Accountability Challenge in Human-LLM Interaction*

This external posting is a strong public anchor for the early SII / ICD / IPP / IFI / Context Roots research lineage.

---

## 3. The January 2025 conflict

Recovered files include:

- `cp_v1_0_1_freeze_declaration.md` — prints **January 28, 2025**;
- `CP_v1_Implementation_Complete.md` — carries a 2025-era date/version history;
- runtime comments and audit documents with 2025 labels.

However, the dedicated provenance memo states explicitly that the project contained **no transcript, file, upload, or metadata supporting a 2025 CP date** and that the earliest evidence it could attest was 25 January 2026.

### Archive ruling

The original 2025-dated files are historically important and are preserved unchanged. Their printed date is classified as:

> **UNSUPPORTED PRIORITY DATE IN THE RECOVERED EVIDENCE**

until an independent earlier artifact is added, such as:

- a Git commit with authoritative hosting timestamp;
- a provider export with server timestamp;
- a dated email attachment;
- a notarized/time-stamped file;
- an OSF/Zenodo deposit; or
- another verifiable third-party record.

This archive therefore **does not claim 2025 priority**.

---

## 4. Recovery evidence vs creation evidence

A file's presence in the August 2026 preservation library proves only that the file had been recovered by that time. It does not automatically prove when its content was first authored.

The archive distinguishes:

- **document-internal date** — text printed in the artifact;
- **file metadata date** — modification/creation metadata from a recovered copy;
- **provider/session timestamp** — server-side record of a conversation or upload;
- **public deposit timestamp** — third-party publication/deposit clock;
- **Git commit timestamp** — repository-hosted history; and
- **legal filing receipt** — authoritative IP filing record.

These forms of evidence have different strengths and should not be conflated.

---

## 5. Provisional patent record

Recovered materials include:

- `cp_provisional_patent_draft.md`; and
- `CP_Provisional_Patent_Application.pdf`.

The recovered application PDF has blank fields for filing date and application number. It is therefore evidence of **patent drafting**, not by itself evidence of filing.

Other project documents report a U.S. provisional filing and a specific number/date. The authoritative filing receipt is not present in the recovered repository package used for this preservation pass.

### Archive ruling

- preserve the historical filing claim;
- do not erase it;
- do not treat the blank application PDF as proof;
- add the official USPTO receipt if/when recovered.

---

## 6. Publication-workflow record

Historical source documents reference:

- SocArXiv/OSF submission;
- JAIR submission workflow;
- arXiv endorsement/submission attempts;
- TechRxiv public posting.

Only the TechRxiv posting was independently observed as a public source during this preservation pass. The others remain project/provenance records pending addition of authoritative receipts where available.

---

## 7. Correspondence / external convergence

The historical Master Knowledge File records correspondence with an independent researcher, Fan Chen-Chieh, and references Zenodo DOIs and a DCM 2.0 research corpus. This material is relevant to the development of the accountability interpretation, but it is **external research, not evidence that CP itself predates the supported CP chronology**.

Any future use should preserve attribution and verify the exact DOI/version before publication.

---

## 8. Researcher authorship vs novelty

The recovered CP artifacts consistently attribute the CP research program and its named constructs to **Mohamed Salama**. This archive preserves that authorship record.

It does not automatically prove that no similar concept existed earlier under another name. Formal novelty claims require a dedicated literature/prior-art search. Accordingly, the repository uses language such as:

- “introduced/named in this research program”;
- “proposed by the CP research program”; or
- “attributed to Mohamed Salama in the recovered archive”

rather than treating global novelty as settled merely by internal documentation.

---

## 9. Future provenance additions

If additional primary evidence is recovered, add it to `archive/provenance/` and update this record with:

1. immutable filename;
2. SHA-256;
3. source/provider;
4. server/public timestamp;
5. what exact proposition it supports; and
6. what it does **not** prove.

Never backdate or rewrite existing artifacts to make the chronology cleaner.
