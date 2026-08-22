# Reassembly of split source bundles

Large recovered binary bundles are split into numbered byte chunks solely to keep Git/API preservation manageable. Reassembly is lossless where the byte chunks themselves are present in the repository.

For the early papers / IntentHealth source bundle:

```bash
cat parts/cp-early-papers-intenthealth-recovered-files28.zip.part-* > cp-early-papers-intenthealth-recovered-files28.zip
```

Verify the reconstructed file against `MANIFEST_SOURCE_BUNDLES_SHA256.txt` at the repository root.

**Preservation-status note (22 Aug 2026):** because the connected GitHub writer available during this pass accepts UTF-8 text but does not expose a native local-binary upload operation, not every recovered binary bundle could be embedded directly in this Git tree. `docs/11_ASSET_REGISTER.md` and the root manifests distinguish recovered/staged artifacts from Git-embedded artifacts and retain cryptographic hashes for the former. No missing byte payload is to be inferred from a hash alone.
