# Klear evidence archive - security and third-party exclusions

This directory is a sanitized preservation copy of the recovered `chat_inputs` evidence bundle.

Excluded from Git preservation:

1. `05_klear_source_code/_env` - contains live credential material. Only its SHA-256 is retained here: `d931c8ef19e69e2b1dcd0ce3662602eceec8e9c486cebd0abb37d15cb96145e7`.
2. `03_documents/ACM_Conference_Proceedings_Primary_Article_Template.pdf` - third-party ACM publication template; SHA-256: `4a28c98c57a8e8ce0823b89a6102954f32ec845c8e38784e18ed05303c14f885`.
3. `03_documents/ACM_Conference_Proceedings_Primary_Article_Template__1_.pdf` - duplicate/alternate third-party ACM template; SHA-256: `c921910170c3d6ff9e55612266a7b73a0ac39388eff0bef9dc6a4cc3f2a846d9`.

The credential-bearing file is deliberately not reproduced, quoted, encoded, or committed. Placeholder examples remain where they contain no live credentials.
