#!/usr/bin/env python3
"""Generate the reproducible WP2 structural/internal-consistency audit.

This script consumes only the exact 52-row TSV emitted after authoritative-v1
identity verification. It does not write C0 FINAL-C10 and does not claim C9
verification. Row dispositions are assistant audit judgments, not researcher
classifications.
"""
from __future__ import annotations

import csv
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "research" / "fan-corpus-validation" / "work" / "incident_rows.tsv"
BASE = ROOT / "research" / "fan-corpus-validation"
OUT = BASE / "corpus-audit"
OUT.mkdir(parents=True, exist_ok=True)

PASS = set("GPT-001 GPT-002 GPT-003 GPT-004 GPT-005 AUD-014 AUD-015 AUD-017 AUD-020 W38-001 W38-003 W38-005 W38-006 W38-007 W39-001 W39-003 W39-004 W39-007 KBD-002 KBD-004 KPF-001".split())
NEEDS = set("AUD-008 AUD-009 AUD-010 AUD-011 CDX-002 CDX-003 CDX-004 W38-002 W38-004 W39-005 W39-006".split())
STRUCT = set("AUD-021 W39-002".split())
EXCLUDE = set("AUD-001 AUD-002 AUD-003 AUD-004 AUD-005 AUD-006 AUD-007 AUD-012 AUD-013 AUD-016 AUD-018 AUD-019 AUD-022 CDX-001 CDX-005 W38-008 KBD-001 KBD-003".split())
assert len(PASS | NEEDS | STRUCT | EXCLUDE) == 52
assert not ((PASS & NEEDS) | (PASS & STRUCT) | (PASS & EXCLUDE) | (NEEDS & STRUCT) | (NEEDS & EXCLUDE) | (STRUCT & EXCLUDE))

NOTES = {
    "AUD-008": "Potential intent event, but A3/A8 are both corrective-language excerpts. Primary-source chronology is needed to identify the actual triggering instruction and later mismatch.",
    "AUD-009": "Potential definition/intent event around 'additive', but the condensed record reads like a corrective turn rather than the original trigger. Source chronology required.",
    "AUD-010": "Potential scope/abstraction event, but A3 substantially overlaps A8 ('Replace the ... false two-choice framing'). Trigger-versus-detection chronology must be reconstructed.",
    "AUD-011": "Potential definition/intent event, but A3 and A8 overlap and C0 SUGGESTED uses non-codebook value DEFINITION->INTENT. Source chronology and normalized recommendation required.",
    "AUD-014": "Strong temporal-currency candidate: explicit head pin/currentness condition, silent assumption that the pin remained current, visible rework after later-head correction.",
    "AUD-015": "Benign silent-resolution candidate. No mismatch was observed, but the record documents a prior surfaced threshold ambiguity that later received a silent strict reading. Keep, but do not treat benign as researcher-validated yet.",
    "AUD-017": "Intent-resolution candidate but explicitly DISCLOSED-PROCEED, not silent. Must not enter an SII numerator merely because A6=NO.",
    "AUD-020": "Unresolved intent candidate. Keep for source verification; no outcome or correctness claim may be finalized from the condensed row.",
    "AUD-021": "Internal contradiction: Resolution style is SILENT, while A8 says the deviation was self-detected and disclosed within the same reply and A11 says self-disclosed. Repair only in v1.1 after source review.",
    "AUD-022": "Counter-pattern/meta record, not SII. Also uses ASKED/DISCLOSED, which is not one of the Codebook's listed Resolution style values.",
    "CDX-002": "Low-confidence benign candidate with no observable mismatch. Source is needed to distinguish a genuine silent interpretation from an implementation choice already implied by the WO.",
    "CDX-003": "Low-confidence benign candidate with no observable mismatch. Source needed to determine whether handling in rail only was a semantic choice or faithful implementation of existing architecture.",
    "CDX-004": "Benign candidate with no observable mismatch. Source needed to establish whether NOT MERGED left push authorization materially ambiguous in context.",
    "W38-001": "Strong standing-instruction/temporal candidate: explicit rebase-before-every-push rule, stale-base behavior, immediate visible mismatch, high material consequence avoided before merge.",
    "W38-002": "Low-confidence benign candidate with no mismatch. Source needed to establish whether keeping intentionally red tests out of default CI was a silent semantic choice or an obvious safety requirement.",
    "W38-003": "Strong scope candidate: one ordinary burst shape was silently generalized to the entire C-04 claim; later correction narrowed the tested universe.",
    "W38-004": "Low-confidence benign output-form/implementation-choice candidate with no mismatch. Source needed before treating filename choice as an IPP.",
    "W38-005": "Good scope/definition candidate: mirrors exactly was silently read as content equality without cryptographic provenance; later user required timestamp/hash.",
    "W38-006": "Strong output-form/definition candidate: marked/greppable was read as suite-level naming/footer rather than adjacent labels, causing repeated correction cycles.",
    "W38-007": "Intent-resolution candidate but explicitly DISCLOSED-PROCEED, not silent. The current aggregate A6-only rule would miscount it as SII if C0 FINAL became INTENT.",
    "W39-001": "Strong standing-instruction/temporal candidate; recurrence with W38-001/KPF-001 supports a cross-window cluster but each record must still be quote-verified independently.",
    "W39-002": "Protocol-level evidence defect: A3 literally says NOT OBSERVABLE - original E0 WO text not retained. The required triggering user words are absent; ineligible for confirmed analysis unless a primary source is recovered.",
    "W39-003": "Strong scope candidate with internally conflicting constraints (correct only six vs verify every argument). Source review is needed later for Context Factor, but the row is coherent enough to proceed.",
    "W39-004": "Plausible output-form/transport candidate: complete corrected file did not specify delivery channel and local-path delivery proved insufficient.",
    "W39-005": "Benign medium-confidence authority/scope candidate based on a nearly empty request label. Source needed to establish what contextual authorization, if any, was available.",
    "W39-006": "Benign medium-confidence scope candidate: Nothing else may apply to final packet or all task commentary. No mismatch observed; source needed.",
    "W39-007": "High-confidence authority candidate: executable SQL content was treated as authorization to execute read-only queries against production. No mutation occurred, but authorization semantics are material.",
    "KBD-002": "Strong output-form/coordination candidate: wait for Mohamed was interpreted without ensuring the device code was visible to the user; mismatch surfaced next turn.",
    "KBD-004": "Strong means-vs-outcome scope candidate: outcome request (one commit + draft PR) was silently bound to GitHub CLI authentication, creating the corpus's longest recorded awareness gap.",
    "KPF-001": "Strong standing-instruction/temporal candidate recurring independently with W38-001/W39-001.",
}

COMPARISON = {
    "COMPETENCE": "Retain as comparison-class evidence; current row describes a technical/factual belief error rather than a choice among meanings of the user's instruction.",
    "PREMISE": "Retain as comparison-class evidence; current row primarily describes a failed environment/input/transport premise rather than semantic intent resolution.",
    "META": "Retain as meta/counter-pattern evidence; do not include in the SII analysis set.",
}

with SRC.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
assert len(rows) == 52
assert {r["GID"] for r in rows} == PASS | NEEDS | STRUCT | EXCLUDE

chronology = set()
for r in rows:
    a = (r["A3 User words (verbatim, may be trimmed)"] or "").strip().lower()
    b = (r["A8 Mismatch signal"] or "").strip().lower()
    if a and b and "not observable" not in b:
        ratio = SequenceMatcher(None, a, b).ratio()
        if ratio >= 0.45 or a in b or b in a:
            chronology.add(r["GID"])

records = []
for r in rows:
    gid = r["GID"]
    if gid in PASS:
        disposition = "PASS_TO_SOURCE_VERIFICATION"
    elif gid in NEEDS:
        disposition = "NEEDS_SOURCE"
    elif gid in STRUCT:
        disposition = "STRUCTURAL_DEFECT"
    else:
        disposition = "EXCLUDE_CANDIDATE"

    triage = r["C0 SUGGESTED"]
    note = NOTES.get(gid)
    if note is None:
        if disposition == "EXCLUDE_CANDIDATE":
            note = COMPARISON.get(triage, "Retain outside SII analysis pending source review; current triage is not an INTENT class.")
        else:
            note = "Condensed row is internally coherent enough to proceed to primary-source quote/chronology verification; no researcher-final classification is implied."

    flags = []
    if gid in chronology:
        flags.append("A3_A8_CHRONOLOGY_OVERLAP")
    if r["Resolution style"] == "DISCLOSED-PROCEED" and r["A6 Asked?"] == "NO":
        flags.append("DISCLOSED_NOT_SILENT_DESPITE_A6_NO")
    if r["Resolution style"] == "ASKED/DISCLOSED":
        flags.append("RESOLUTION_STYLE_NOT_IN_CODEBOOK")
    if gid == "AUD-021":
        flags.append("RESOLUTION_STYLE_CONTRADICTS_A8_A11")
    if gid == "W39-002":
        flags.append("A3_TRIGGER_QUOTE_NOT_OBSERVABLE")
    if triage == "DEFINITION→INTENT":
        flags.append("C0_SUGGESTED_NOT_FINAL_CODEBOOK_VALUE")
    if r["A9 Turns to detect"] not in {"0", "1"}:
        flags.append("A9_REQUIRES_NORMALIZATION_FOR_METRICS")

    records.append({
        "GID": gid,
        "Window": r["Window"],
        "Current triage only": triage,
        "Suggested outcome only": r["Outcome (sugg.)"],
        "Confidence": r["A13 Conf."],
        "Resolution style": r["Resolution style"],
        "A6": r["A6 Asked?"],
        "WP2 disposition": disposition,
        "Audit flags": ";".join(flags) if flags else "NONE",
        "WP2 audit note": note,
        "C9 status": "UNVERIFIED - WP3 REQUIRED",
    })

fields = list(records[0])
with (OUT / "ROW_AUDIT_52.tsv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
    w.writeheader()
    w.writerows(records)

counts = Counter(r["WP2 disposition"] for r in records)
classes = Counter(r["C0 SUGGESTED"] for r in rows)
outcomes = Counter(r["Outcome (sugg.)"] for r in rows)
confidence = Counter(r["A13 Conf."] for r in rows)
styles = Counter(r["Resolution style"] for r in rows)
a6 = Counter(r["A6 Asked?"] for r in rows)
windows = Counter(r["Window"] for r in rows)

md = [
    "# WP2 - Audit of All 52 Naturalistic Corpus Records", "",
    "**Scope:** structural and internal-consistency audit of the exact authoritative v1 workbook recovered and frozen in WP1.", "",
    "**Important boundary:** this is not quote verification and not researcher-final classification. Every C9 status remains unverified until WP3 checks primary transcripts. C5 remains exclusively Mohamed Salama's decision.", "",
    "## WP2 disposition summary", "",
    "| Disposition | Count | Meaning |", "|---|---:|---|",
    f"| `PASS_TO_SOURCE_VERIFICATION` | {counts['PASS_TO_SOURCE_VERIFICATION']} | Condensed row is coherent enough to advance to WP3. |",
    f"| `NEEDS_SOURCE` | {counts['NEEDS_SOURCE']} | Condensed row alone is insufficient to determine whether the event is analytically eligible. |",
    f"| `STRUCTURAL_DEFECT` | {counts['STRUCTURAL_DEFECT']} | Required evidence/coding is internally defective and must be repaired only from primary evidence in a later version. |",
    f"| `EXCLUDE_CANDIDATE` | {counts['EXCLUDE_CANDIDATE']} | Retain in corpus as comparison/meta evidence, but do not feed SII analysis on current evidence. |", "",
    "## Reconciliation and completeness", "",
    f"- Exactly **{len(rows)} records** are present.",
    "- Window allocation reconciles exactly: " + ", ".join(f"{k} {windows[k]}" for k in ["GPT", "AUD", "CDX", "W38", "W39", "KBD", "KPF"]) + ".",
    "- Every row populates every extraction field actually stored in v1: A1, A2, A3, A5, A6, A7, A8, A9, A10, A11, A12, A13.",
    "- **A4 Possible interpretations is not stored as a dedicated column anywhere in v1.** This is a workbook-schema variance against the extraction protocol, not 52 separate blank cells.",
    "- All researcher-final fields C0 FINAL through C10 are blank across all 52 rows.",
    "- Current C0 values are explicitly suggestions only: " + ", ".join(f"{k}={v}" for k, v in classes.items()) + ".",
    "- Suggested outcomes only: " + ", ".join(f"{k}={v}" for k, v in outcomes.items()) + ".",
    "- Confidence: " + ", ".join(f"{k}={v}" for k, v in confidence.items()) + ".",
    "- A6: " + ", ".join(f"{k}={v}" for k, v in a6.items()) + ".",
    "- Resolution style: " + ", ".join(f"{k}={v}" for k, v in styles.items()) + ".", "",
    "## Material scientific/method defects found", "",
    "1. **A4 is absent from the workbook schema.** The protocol requires possible interpretations, while v1 stores no dedicated A4. The README says fields were condensed and full text lives in source extract files, so WP3 must attempt recovery rather than invent A4.",
    "2. **The v1 silent-inference aggregate is methodologically unsafe.** Its formula counts `C0 FINAL=INTENT` + `A6=NO`. But AUD-017 and W38-007 both have `A6=NO` and `Resolution style=DISCLOSED-PROCEED`; disclosure is not silent. Historical v1 remains unchanged.",
    "3. **AUD-021 has an internal coding contradiction.** Resolution style is `SILENT`, while A8/A11 explicitly say the deviation was self-detected and disclosed in the same reply.",
    "4. **W39-002 lacks the required triggering quote.** A3 itself says the original E0 work-order text is `NOT OBSERVABLE`. It cannot become C9 CONFIRMED unless primary evidence is recovered.",
    "5. **Resolution-style vocabulary is inconsistent.** AUD-022 uses `ASKED/DISCLOSED`, which is not one of the Codebook allowed values.",
    "6. **A9 is not metric-ready.** Values mix integers with `N/O`, `N/A`, `NOT OBSERVABLE`, approximate cycles, and approximate exchanges. A preregistered normalization/exclusion rule is required before awareness-gap statistics.",
    f"7. **{len(chronology)} records show substantial A3/A8 textual overlap** under a conservative string-overlap check. This is not proof of error, but it creates a chronology risk. WP3 must reconstruct trigger -> interpretation -> mismatch order from source transcripts.",
    "8. **Suggested outcome has no separate researcher-final column in v1.** The aggregate sheet counts suggested HARMFUL/BENIGN values. Publication outcome rates require explicit researcher validation or a v1.1 final-outcome rule/field.",
    "9. **C0 SUGGESTED contains one non-final-codebook label (`DEFINITION->INTENT`).** It may remain a triage note, but normalization can occur only as a recommendation before researcher review.", "",
    "## Analytical consequence", "",
    "The v1 workbook is a useful structured candidate corpus, but it is not yet a publishable 52-event SII dataset. WP2 does **not** support saying '52 validated silent-inference events.' The defensible statement remains: **52 extracted candidate records across seven source windows, with researcher-final coding and primary-source quote verification incomplete.**", "",
    "No records were deleted. `EXCLUDE_CANDIDATE` means exclude from the SII analysis candidate set on present evidence, not erase from the research corpus. Comparison classes and counter-patterns remain scientifically useful.", "",
    "## Row-level audit", "",
    "| GID | Triage only | Outcome only | Conf. | WP2 disposition | Key audit note |", "|---|---|---|---|---|---|",
]
for rec in records:
    note = rec["WP2 audit note"].replace("|", "\\|").replace("\n", " ")
    md.append(f"| {rec['GID']} | {rec['Current triage only']} | {rec['Suggested outcome only']} | {rec['Confidence']} | `{rec['WP2 disposition']}` | {note} |")
md += [
    "", "## Next gate", "",
    "WP3 must locate primary transcript/source-extract evidence and verify A3/A8 chronology and quotations. Only then can C9 recommendations be made. WP4 classification recommendations may be drafted from WP2 evidence, but must remain explicitly assistant recommendations / unverified until WP3 and Mohamed's researcher decisions.", "",
]
(BASE / "CORPUS_AUDIT_52.md").write_text("\n".join(md), encoding="utf-8")
print(dict(counts))
