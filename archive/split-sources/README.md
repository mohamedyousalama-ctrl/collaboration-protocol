# Split Source Preservation Index

These files preserve byte-exact UTF-8 text for high-value CP source artifacts that exceed the practical size of the connected GitHub text-write interface. Concatenate each ordered `part-*` series with no separator to recover the original UTF-8 byte stream, then verify the SHA-256 below. Historical claims inside source files retain their original status; inclusion does not endorse them as current truth.

| Original source path | Bytes | SHA-256 | Parts | Repository parts |
|---|---:|---|---:|---|
| `archive/research-lineage-2026-01/CP_Master_Knowledge_File.md` | 23,978 | `7d8e48f683f185afc34e5df62d4df87cfdb2b850c4d00234782b503ca1afeab1` | 4 | `archive/split-sources/CP_Master_Knowledge_File.md/part-*` |
| `archive/research-lineage-2026-01/CP_Research_Package_v4.1_arXiv.md` | 69,190 | `a2e3bccee078aea05d0ac63d4f2cfbef7145c7e91f23e90ccfd2a19dce68fa90` | 9 | `archive/split-sources/CP_Research_Package_v4.1_arXiv.md/part-*` |
| `archive/research-lineage-2026-01/collaboration_protocol_research_agenda.md` | 17,423 | `13997134d77734cedbccd6fa6b9d0b3498f8ba5a780ee215a398c19400641d4c` | 3 | `archive/split-sources/collaboration_protocol_research_agenda.md/part-*` |
| `archive/research-lineage-2026-01/papers/CP_Collaboration_Protocol_FINAL_arXiv_extracted.txt` | 66,863 | `6cf8a3b96904147f2b24af7f06a8dac64309d08a77ae53ec2f50d036a5dc5d96` | 9 | `archive/split-sources/CP_Collaboration_Protocol_FINAL_arXiv_extracted.txt/part-*` |
| `archive/frozen-v1.0.1/cp_v1_0_1_runtime_persistent.html` | 65,814 | `469c440732ec615daf106b7a2bf7112c0ea7df15b2d4fce2e6a49aae21b730e9` | 9 | `archive/split-sources/cp_v1_0_1_runtime_persistent.html/part-*` |
| `archive/frozen-v1.0.1/CP_v1_Implementation_Complete.md` | 60,034 | `b25689bbb24c5d6b728d09964660bee26e56bddfccf3cc30e3e9e4bc633779eb` | 8 | `archive/split-sources/CP_v1_Implementation_Complete.md/part-*` |
| `archive/frozen-v1.0.1/cp_v1_paper_draft.md` | 37,176 | `e7d22a72141c7fce90bbff09af09f6ba1b27577e6945d088a5bf9c64cb3a1416` | 5 | `archive/split-sources/cp_v1_paper_draft.md/part-*` |
| `archive/klear/sanitized-chat-inputs/03_documents/klear_implementation_spec_v2_1.md` | 53,104 | `e1d9350bf30e3b407b5e97f3146839c389c52249ea49a4f2dfc899d3896106e5` | 7 | `archive/split-sources/klear_implementation_spec_v2_1.md/part-*` |
| `archive/applied/Ghost_Master_Strategy_Decisions_and_Backlog_2026-08-05_v2.1.md` | 51,563 | `e2c7ff97ac22324117e6affab77799e8b269622e0e0fed93aabd6754f5d7bc87` | 7 | `archive/split-sources/Ghost_Master_Strategy_Decisions_and_Backlog_2026-08-05_v2.1.md/part-*` |
| `archive/publication-and-ip/cp_provisional_patent_draft.md` | 35,147 | `b1735e87711f70c757790985f00ab3379958221bc9ca18900efa95f9c595900f` | 5 | `archive/split-sources/cp_provisional_patent_draft.md/part-*` |

Reassembly example:

```bash
cat archive/split-sources/CP_Master_Knowledge_File.md/part-* > CP_Master_Knowledge_File.md
sha256sum CP_Master_Knowledge_File.md
```

The normalized academic documents under `docs/` govern current status labels and version boundaries.
