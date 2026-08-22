# Locally constructed lossless preservation packets — metadata record

During the 22 August 2026 preservation pass, two lossless archive packets were constructed in the working container from recovered CP source material. Their **data chunks are not all embedded in this Git tree** because the connected GitHub writer available in this session exposes UTF-8 text writes but not a native local-binary upload action.

This directory therefore records the packet design and cryptographic identities without pretending that a hash alone preserves the bytes.

## A. Missing textual/searchable-source packet

Local packet: `cp_missing_textual_sources.tar.xz`

Purpose: consolidate 164 CP-related text/code/CSV/searchable-conversion files that were recovered in staging but were not all individually committed when the packet was constructed. The packet includes early research packages, runtime/test artifacts, Klear source and workbook CSV conversions, IntentHealth work, Ghost/Continuity source records, public-record locators, and searchable conversions of important DOCX/PDF material.

Expected packet SHA-256:

`cf0f2a401fa123a8c83e3a9fdee85973dfb344581764a54e6ff79557c279bb55`

## B. Exact small-binary research-artifact packet

Local packet: `cp_research_small_binaries.tar.xz`

Purpose: preserve exact original bytes for the CP incident workbook, Project Continuity workbook and roadmap, five Klear evidence workbooks, CP Master Knowledge DOCX, CP Compendium DOCX, and the recovered provisional-patent application PDF.

Expected packet SHA-256:

`fa448f1d2afb4c35629f48c1dbf8375a98dab9f402196220db2e508a45b28736`

## Klear image limitation

The recovered Klear screenshot/image set was not duplicated byte-for-byte in these packets. Filenames, sizes, and SHA-256 identities are intended to be retained in the image-evidence index when available. Substantive HTML diagrams are preserved in searchable form.

## Security boundary

No live credential-bearing environment file is included. The credential-bearing Klear environment file is intentionally excluded from Git; its hash is recorded in `archive/klear/SECURITY_REDACTION_NOTICE.md` and `docs/12_SECURITY_AND_DISCLOSURE_LOG.md`.

## Status

`PACKETS_CONSTRUCTED_LOCALLY / CHECKSUMMED / PAYLOADS_NOT_FULLY_GIT_EMBEDDED`

The packet checksums are provenance records. They must not be described as proof that the packet payloads are recoverable from this repository alone.
