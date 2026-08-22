# Reconstructing `session.js`

The original sanitized Klear `session.js` is preserved losslessly as four sequential UTF-8 parts because the connected repository writer has practical per-call size limits.

Concatenate, in lexical order:

```sh
cat session.js.part-000 session.js.part-001 session.js.part-002 session.js.part-003 > session.js
```

Expected size:

```text
28,599 bytes
```

Expected SHA-256:

```text
04ccb4eb0b23d55d3d55e4f94bb10af54428ad1f152b3506e61e418d694269c6
```

This source is historically important because it contains the explicit retry path that skips IPP classification, ICD filtering, and Guardian CP1, and the report path that sets `responsibility_chain_intact: true`.
