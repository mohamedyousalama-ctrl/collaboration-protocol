# Manifest Semantics and Integrity Status

This repository contains several checksum records created at different stages of the 22 August 2026 preservation operation. They do **not** all mean the same thing.

## Authoritative preservation manifest

### `MANIFEST_SHA256.txt`

This is the final preservation-planning/source-artifact manifest for the recovered staging tree used during the archive build. The SHA-256 values identify recovered source artifacts as they existed in that staging set.

A path listed in this manifest does **not by itself** assert that the original file exists as one direct GitHub blob under the same path. Depending on size, format, security, and connector limitations, a source may instead be represented by:

- a direct text file;
- ordered split text parts;
- base64 parts for a recoverable binary;
- a searchable conversion plus the recovered-source hash;
- a source-bundle/recovery record; or
- an explicit exclusion/missing-material record.

Use `docs/11_ASSET_REGISTER.md`, `docs/14_RESEARCH_PRESERVATION_STATUS.md`, `archive/split-sources/README.md`, and security/reassembly notes to determine the actual representation mode.

## Source-bundle manifest

### `MANIFEST_SOURCE_BUNDLES_SHA256.txt`

This records cryptographic identities of the recovered source bundles. Its `representation_status` column must be read literally. As of this preservation pass, several large binary bundles were recovered/staged but were **not embedded as complete binary payloads in Git** because the connected GitHub writer exposed UTF-8 text writes rather than a native local-binary upload action.

Their hashes are provenance records, not claims that the payload bytes are present in the repository.

## Superseded staging snapshot

### `SOURCE_ARTIFACT_SHA256.txt`

This file is a **superseded earlier staging snapshot**. During the final checksum audit, spot checks showed that several values do not match the final recovered staging tree represented by `MANIFEST_SHA256.txt`.

It is retained only as preservation-process history. **Do not use it as the authoritative checksum manifest.**

## Git-level verification

For split textual sources, Git blob SHA-1 values were compared against `git hash-object` values of recovered local source parts where possible. `archive/split-sources/README.md` records whether a representation is:

- `EXACT-VERIFIED`; or
- `SEARCHABLE-NORMALIZED`.

The latter is deliberately not presented as byte-identical evidence.

## Integrity principle

A checksum proves identity only when the corresponding bytes are actually available for hashing. A recorded hash alone must never be described as preservation of the underlying payload.
