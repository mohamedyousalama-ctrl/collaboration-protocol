# CP Incident Database v1 — Git Payload Reconstruction

**Identity verdict: MISMATCH**

- Expected Base64 chars: `41964`
- Actual Base64 chars: `35408`
- Expected bytes: `31471`
- Actual bytes: `26554`
- Expected SHA-256: `3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a`
- Actual SHA-256: `f75de5b2b427c2a4c3037112085436fefc8916811914c68fb83120dc8ea12eaf`
- Valid ZIP container: `True`
- Parse error: `BadZipFile: Bad magic number for file header`

The Git payload is not promoted to authoritative v1 unless the declared byte identity matches.
