#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "research" / "fan-corpus-validation" / "source-v1-exact"
OUT = ROOT / "research" / "fan-corpus-validation" / "work"
OUT.mkdir(parents=True, exist_ok=True)

PARTS = [
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-00",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-01",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-02",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-03",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-04",
]
EXPECTED_CHARS = 41964
EXPECTED_BYTES = 31471
EXPECTED_SHA256 = "3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a"
XLSX = OUT / "CP_Incident_Database_v1.authoritative.xlsx"


def main() -> None:
    missing = [str(p) for p in PARTS if not p.exists()]
    if missing:
        raise SystemExit("Missing exact-source parts: " + ", ".join(missing))

    pieces = [p.read_text(encoding="utf-8").strip() for p in PARTS]
    stream = "".join(pieces)
    decoded = base64.b64decode(stream, validate=True)
    actual_sha = hashlib.sha256(decoded).hexdigest()
    ok = len(stream) == EXPECTED_CHARS and len(decoded) == EXPECTED_BYTES and actual_sha == EXPECTED_SHA256
    if not ok:
        raise SystemExit(
            f"Exact-source identity failure: chars={len(stream)} bytes={len(decoded)} sha256={actual_sha}"
        )

    XLSX.write_bytes(decoded)
    if not zipfile.is_zipfile(XLSX):
        raise SystemExit("Decoded payload is not a valid XLSX ZIP container")

    with zipfile.ZipFile(XLSX) as zf:
        wb = ET.fromstring(zf.read("xl/workbook.xml"))
        ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        sheets = [s.attrib["name"] for s in wb.findall("m:sheets/m:sheet", ns)]
        required = ["README", "Codebook", "Incidents", "Aggregates"]
        if sheets != required:
            raise SystemExit(f"Unexpected workbook sheets: {sheets}")

    result = {
        "identity_verified": True,
        "base64_chars": len(stream),
        "decoded_bytes": len(decoded),
        "sha256": actual_sha,
        "worksheets": sheets,
        "source_parts": [p.name for p in PARTS],
        "reconstructed_path": str(XLSX.relative_to(ROOT)),
    }
    (OUT / "exact_source_verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (OUT / "EXACT_SOURCE_VERIFICATION.md").write_text(
        "# CP Incident Database v1 — Exact Source Verification\n\n"
        "**VERDICT: PASS — exact byte identity independently reconstructed from the branch source parts.**\n\n"
        f"- Base64 characters: `{len(stream)}` / expected `{EXPECTED_CHARS}`\n"
        f"- Decoded bytes: `{len(decoded)}` / expected `{EXPECTED_BYTES}`\n"
        f"- SHA-256: `{actual_sha}`\n"
        f"- Worksheets: `{', '.join(sheets)}`\n"
        f"- Reconstructed working copy: `{XLSX.relative_to(ROOT)}`\n\n"
        "The historical archive representation on `main` is not rewritten by this verification.\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
