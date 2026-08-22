# Public-paper extraction representation note

This directory contains an ordered, searchable text extraction associated with the public Collaboration Protocol preprint.

## Important integrity limitation

This representation is **not byte-exact** to the recovered local extraction. During transfer through the connected text interface, some PDF-extraction control characters / text-encoding bytes were normalized. Part 000 matched the recovered Git blob exactly; subsequent parts did not all match the recovered local Git blob hashes.

Accordingly:

- use these parts for reading, searching, and historical comparison;
- do **not** use this representation to prove exact PDF bytes or exact extraction bytes;
- the recorded recovered-source SHA-256 (`6cf8a3b96904147f2b24af7f06a8dac64309d08a77ae53ec2f50d036a5dc5d96`) is provenance for the local recovered extraction, not a checksum claim for the concatenated GitHub text parts;
- the authoritative public publication record is the TechRxiv preprint linked from `archive/publication-and-ip/TECHRXIV_PUBLIC_RECORD.md`.

## Reconstruction for reading

```bash
cat part-* > CP_Collaboration_Protocol_FINAL_arXiv_extracted.searchable.txt
```

This produces a readable/searchable convenience copy only.
