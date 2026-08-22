# WP2 - Audit of All 52 Naturalistic Corpus Records

**Scope:** structural and internal-consistency audit of the exact authoritative v1 workbook recovered and frozen in WP1.

**Important boundary:** this is not quote verification and not researcher-final classification. Every C9 status remains unverified until WP3 checks primary transcripts. C5 remains exclusively Mohamed Salama's decision.

## WP2 disposition summary

| Disposition | Count | Meaning |
|---|---:|---|
| `PASS_TO_SOURCE_VERIFICATION` | 21 | Condensed row is coherent enough to advance to WP3. |
| `NEEDS_SOURCE` | 11 | Condensed row alone is insufficient to determine whether the event is analytically eligible. |
| `STRUCTURAL_DEFECT` | 2 | Required evidence/coding is internally defective and must be repaired only from primary evidence in a later version. |
| `EXCLUDE_CANDIDATE` | 18 | Retain in corpus as comparison/meta evidence, but do not feed SII analysis on current evidence. |

## Reconciliation and completeness

- Exactly **52 records** are present.
- Window allocation reconciles exactly: GPT 5, AUD 22, CDX 5, W38 8, W39 7, KBD 4, KPF 1.
- Every row populates every extraction field actually stored in v1: A1, A2, A3, A5, A6, A7, A8, A9, A10, A11, A12, A13.
- **A4 Possible interpretations is not stored as a dedicated column anywhere in v1.** This is a workbook-schema variance against the extraction protocol, not 52 separate blank cells.
- All researcher-final fields C0 FINAL through C10 are blank across all 52 rows.
- Current C0 values are explicitly suggestions only: INTENT=33, COMPETENCE=8, PREMISE=6, DEFINITION→INTENT=1, META=4.
- Suggested outcomes only: HARMFUL=31, BENIGN=20, UNRESOLVED=1.
- Confidence: HIGH=24, MEDIUM=15, LOW=13.
- A6: NO=51, N/A=1.
- Resolution style: SILENT=49, DISCLOSED-PROCEED=2, ASKED/DISCLOSED=1.

## Material scientific/method defects found

1. **A4 is absent from the workbook schema.** The protocol requires possible interpretations, while v1 stores no dedicated A4. The README says fields were condensed and full text lives in source extract files, so WP3 must attempt recovery rather than invent A4.
2. **The v1 silent-inference aggregate is methodologically unsafe.** Its formula counts `C0 FINAL=INTENT` + `A6=NO`. But AUD-017 and W38-007 both have `A6=NO` and `Resolution style=DISCLOSED-PROCEED`; disclosure is not silent. Historical v1 remains unchanged.
3. **AUD-021 has an internal coding contradiction.** Resolution style is `SILENT`, while A8/A11 explicitly say the deviation was self-detected and disclosed in the same reply.
4. **W39-002 lacks the required triggering quote.** A3 itself says the original E0 work-order text is `NOT OBSERVABLE`. It cannot become C9 CONFIRMED unless primary evidence is recovered.
5. **Resolution-style vocabulary is inconsistent.** AUD-022 uses `ASKED/DISCLOSED`, which is not one of the Codebook allowed values.
6. **A9 is not metric-ready.** Values mix integers with `N/O`, `N/A`, `NOT OBSERVABLE`, approximate cycles, and approximate exchanges. A preregistered normalization/exclusion rule is required before awareness-gap statistics.
7. **7 records show substantial A3/A8 textual overlap** under a conservative string-overlap check. This is not proof of error, but it creates a chronology risk. WP3 must reconstruct trigger -> interpretation -> mismatch order from source transcripts.
8. **Suggested outcome has no separate researcher-final column in v1.** The aggregate sheet counts suggested HARMFUL/BENIGN values. Publication outcome rates require explicit researcher validation or a v1.1 final-outcome rule/field.
9. **C0 SUGGESTED contains one non-final-codebook label (`DEFINITION->INTENT`).** It may remain a triage note, but normalization can occur only as a recommendation before researcher review.

## Analytical consequence

The v1 workbook is a useful structured candidate corpus, but it is not yet a publishable 52-event SII dataset. WP2 does **not** support saying '52 validated silent-inference events.' The defensible statement remains: **52 extracted candidate records across seven source windows, with researcher-final coding and primary-source quote verification incomplete.**

No records were deleted. `EXCLUDE_CANDIDATE` means exclude from the SII analysis candidate set on present evidence, not erase from the research corpus. Comparison classes and counter-patterns remain scientifically useful.

## Row-level audit

| GID | Triage only | Outcome only | Conf. | WP2 disposition | Key audit note |
|---|---|---|---|---|---|
| GPT-001 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied. |
| GPT-002 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied. |
| GPT-003 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied. |
| GPT-004 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied. |
| GPT-005 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied. |
| AUD-001 | COMPETENCE | HARMFUL | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-002 | COMPETENCE | HARMFUL | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-003 | COMPETENCE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-004 | PREMISE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| AUD-005 | COMPETENCE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-006 | COMPETENCE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-007 | COMPETENCE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-008 | INTENT | HARMFUL | HIGH | `NEEDS_SOURCE` | Potential intent event, but A3/A8 are both corrective-language excerpts. Primary-source chronology is needed to identify the actual triggering instruction and later mismatch. |
| AUD-009 | INTENT | HARMFUL | HIGH | `NEEDS_SOURCE` | Potential definition/intent event around 'additive', but the condensed record reads like a corrective turn rather than the original trigger. Source chronology required. |
| AUD-010 | INTENT | HARMFUL | HIGH | `NEEDS_SOURCE` | Potential scope/abstraction event, but A3 substantially overlaps A8 ('Replace the ... false two-choice framing'). Trigger-versus-detection chronology must be reconstructed. |
| AUD-011 | DEFINITION→INTENT | HARMFUL | HIGH | `NEEDS_SOURCE` | Potential definition/intent event, but A3 and A8 overlap and C0 SUGGESTED uses non-codebook value DEFINITION->INTENT. Source chronology and normalized recommendation required. |
| AUD-012 | PREMISE | BENIGN | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| AUD-013 | COMPETENCE | HARMFUL | HIGH | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| AUD-014 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong temporal-currency candidate: explicit head pin/currentness condition, silent assumption that the pin remained current, visible rework after later-head correction. |
| AUD-015 | INTENT | BENIGN | MEDIUM | `PASS_TO_SOURCE_VERIFICATION` | Benign silent-resolution candidate. No mismatch was observed, but the record documents a prior surfaced threshold ambiguity that later received a silent strict reading. Keep, but do not treat benign as researcher-validated yet. |
| AUD-016 | PREMISE | BENIGN | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| AUD-017 | INTENT | BENIGN | LOW | `PASS_TO_SOURCE_VERIFICATION` | Intent-resolution candidate but explicitly DISCLOSED-PROCEED, not silent. Must not enter an SII numerator merely because A6=NO. |
| AUD-018 | META | BENIGN | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as meta/counter-pattern evidence; do not include in the SII analysis set. |
| AUD-019 | META | BENIGN | LOW | `EXCLUDE_CANDIDATE` | Retain as meta/counter-pattern evidence; do not include in the SII analysis set. |
| AUD-020 | INTENT | UNRESOLVED | MEDIUM | `PASS_TO_SOURCE_VERIFICATION` | Unresolved intent candidate. Keep for source verification; no outcome or correctness claim may be finalized from the condensed row. |
| AUD-021 | INTENT | BENIGN | MEDIUM | `STRUCTURAL_DEFECT` | Internal contradiction: Resolution style is SILENT, while A8 says the deviation was self-detected and disclosed within the same reply and A11 says self-disclosed. Repair only in v1.1 after source review. |
| AUD-022 | META | BENIGN | LOW | `EXCLUDE_CANDIDATE` | Counter-pattern/meta record, not SII. Also uses ASKED/DISCLOSED, which is not one of the Codebook's listed Resolution style values. |
| CDX-001 | PREMISE | BENIGN | LOW | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| CDX-002 | INTENT | BENIGN | LOW | `NEEDS_SOURCE` | Low-confidence benign candidate with no observable mismatch. Source is needed to distinguish a genuine silent interpretation from an implementation choice already implied by the WO. |
| CDX-003 | INTENT | BENIGN | LOW | `NEEDS_SOURCE` | Low-confidence benign candidate with no observable mismatch. Source needed to determine whether handling in rail only was a semantic choice or faithful implementation of existing architecture. |
| CDX-004 | INTENT | BENIGN | MEDIUM | `NEEDS_SOURCE` | Benign candidate with no observable mismatch. Source needed to establish whether NOT MERGED left push authorization materially ambiguous in context. |
| CDX-005 | META | BENIGN | LOW | `EXCLUDE_CANDIDATE` | Retain as meta/counter-pattern evidence; do not include in the SII analysis set. |
| W38-001 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong standing-instruction/temporal candidate: explicit rebase-before-every-push rule, stale-base behavior, immediate visible mismatch, high material consequence avoided before merge. |
| W38-002 | INTENT | BENIGN | LOW | `NEEDS_SOURCE` | Low-confidence benign candidate with no mismatch. Source needed to establish whether keeping intentionally red tests out of default CI was a silent semantic choice or an obvious safety requirement. |
| W38-003 | INTENT | HARMFUL | MEDIUM | `PASS_TO_SOURCE_VERIFICATION` | Strong scope candidate: one ordinary burst shape was silently generalized to the entire C-04 claim; later correction narrowed the tested universe. |
| W38-004 | INTENT | BENIGN | LOW | `NEEDS_SOURCE` | Low-confidence benign output-form/implementation-choice candidate with no mismatch. Source needed before treating filename choice as an IPP. |
| W38-005 | INTENT | HARMFUL | MEDIUM | `PASS_TO_SOURCE_VERIFICATION` | Good scope/definition candidate: mirrors exactly was silently read as content equality without cryptographic provenance; later user required timestamp/hash. |
| W38-006 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong output-form/definition candidate: marked/greppable was read as suite-level naming/footer rather than adjacent labels, causing repeated correction cycles. |
| W38-007 | INTENT | BENIGN | LOW | `PASS_TO_SOURCE_VERIFICATION` | Intent-resolution candidate but explicitly DISCLOSED-PROCEED, not silent. The current aggregate A6-only rule would miscount it as SII if C0 FINAL became INTENT. |
| W38-008 | COMPETENCE | BENIGN | LOW | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction. |
| W39-001 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong standing-instruction/temporal candidate; recurrence with W38-001/KPF-001 supports a cross-window cluster but each record must still be quote-verified independently. |
| W39-002 | INTENT | HARMFUL | LOW | `STRUCTURAL_DEFECT` | Protocol-level evidence defect: A3 literally says NOT OBSERVABLE - original E0 WO text not retained. The required triggering user words are absent; ineligible for confirmed analysis unless a primary source is recovered. |
| W39-003 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong scope candidate with internally conflicting constraints (correct only six vs verify every argument). Source review is needed later for Context Factor, but the row is coherent enough to proceed. |
| W39-004 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Plausible output-form/transport candidate: complete corrected file did not specify delivery channel and local-path delivery proved insufficient. |
| W39-005 | INTENT | BENIGN | MEDIUM | `NEEDS_SOURCE` | Benign medium-confidence authority/scope candidate based on a nearly empty request label. Source needed to establish what contextual authorization, if any, was available. |
| W39-006 | INTENT | BENIGN | MEDIUM | `NEEDS_SOURCE` | Benign medium-confidence scope candidate: Nothing else may apply to final packet or all task commentary. No mismatch observed; source needed. |
| W39-007 | INTENT | BENIGN | HIGH | `PASS_TO_SOURCE_VERIFICATION` | High-confidence authority candidate: executable SQL content was treated as authorization to execute read-only queries against production. No mutation occurred, but authorization semantics are material. |
| KBD-001 | PREMISE | HARMFUL | LOW | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| KBD-002 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong output-form/coordination candidate: wait for Mohamed was interpreted without ensuring the device code was visible to the user; mismatch surfaced next turn. |
| KBD-003 | PREMISE | HARMFUL | MEDIUM | `EXCLUDE_CANDIDATE` | Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution. |
| KBD-004 | INTENT | HARMFUL | HIGH | `PASS_TO_SOURCE_VERIFICATION` | Strong means-vs-outcome scope candidate: outcome request (one commit + draft PR) was silently bound to GitHub CLI authentication, creating the corpus's longest recorded awareness gap. |
| KPF-001 | INTENT | HARMFUL | MEDIUM | `PASS_TO_SOURCE_VERIFICATION` | Strong standing-instruction/temporal candidate recurring independently with W38-001/W39-001. |

## Next gate

WP3 must locate primary transcript/source-extract evidence and verify A3/A8 chronology and quotations. Only then can C9 recommendations be made. WP4 classification recommendations may be drafted from WP2 evidence, but must remain explicitly assistant recommendations / unverified until WP3 and Mohamed's researcher decisions.
