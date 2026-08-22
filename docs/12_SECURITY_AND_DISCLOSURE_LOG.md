# 12 — Security and Disclosure Log

## 1. Credential-bearing source discovered

The recovered `chat_inputs` bundle contains an environment file:

`05_klear_source_code/_env`

A preservation scan found live credential material in that file. The file is therefore **not committed to Git**, even though the repository is currently private.

Its SHA-256 is retained in:

`archive/klear/SECURITY_REDACTION_NOTICE.md`

No credential values are reproduced anywhere in this archive.

### Required operational action outside this archive

Any credential that was ever present in an exported/recovered bundle should be treated as exposed and rotated/revoked at the provider. This repository records the archival exclusion but cannot itself prove provider-side rotation.

---

## 2. Placeholder references retained

Some files contain obvious placeholders such as:

```text
ANTHROPIC_API_KEY=sk-...
SUPABASE_SERVICE_KEY=eyJ...
```

or environment-variable references such as `process.env.ANTHROPIC_API_KEY`. These are not live secrets and are retained where they document setup/implementation.

---

## 3. Third-party files excluded

Two ACM conference-template PDFs were present in the recovered `chat_inputs` package. They are excluded from the sanitized Klear preservation package because they are third-party publication templates rather than original CP research output.

Their hashes are preserved in the Klear redaction notice for completeness.

---

## 4. Sanitized Klear archive

`archive/klear/parts/sanitized-chat-inputs.zip.part-*` represents a losslessly split sanitized ZIP generated from the recovered `chat_inputs` bundle with:

- the live `_env` credential file removed;
- third-party ACM template PDFs removed;
- screenshots retained;
- CP diagrams retained;
- Klear documentation retained;
- Klear evaluation workbooks retained; and
- Klear source code retained.

A browsable text/code subset is also retained under:

`archive/klear/sanitized-chat-inputs/`

---

## 5. Secret-scan policy

Before every preservation release:

1. scan text/code for provider-key prefixes and JWT-like tokens;
2. inspect `.env`, credential, config, and deployment files;
3. treat private repositories as **not** a substitute for secret hygiene;
4. never commit live keys simply to preserve historical completeness;
5. retain a hash/exclusion record so the absence itself is auditable; and
6. rotate any credential found in an exported artifact.

---

## 6. Personal and research data

The archive includes research emails/names inside historical documents and scenario workbooks. Before any future **public** release, perform a separate privacy review of:

- personal email addresses;
- Google Drive links;
- participant/tester identifiers;
- screenshots;
- conversation excerpts;
- customer/project identifiers; and
- any third-party copyrighted content.

This preservation commit is not automatically a public-release package.
