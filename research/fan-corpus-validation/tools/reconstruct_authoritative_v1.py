#!/usr/bin/env python3
"""Reconstruct the authoritative CP Incident Database v1 from recovered Base64.

The six source chunks on this research branch were regenerated from the original
`files(3).zip` research source bundle recovered from the user's file library.
That bundle's SHA-256 matches the repository source-bundle manifest. This tool
will not inventory or promote the workbook unless its exact declared identity
also matches: 41,964 Base64 characters, 31,471 decoded bytes, and SHA-256
3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a.
"""
from __future__ import annotations

import base64
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "research" / "fan-corpus-validation" / "recovered-source"
OUT = ROOT / "research" / "fan-corpus-validation" / "work"
OUT.mkdir(parents=True, exist_ok=True)

PARTS = [SRC / f"CP_Incident_Database_v1.xlsx.b64.part-{i:03d}" for i in range(6)]
EXPECTED_B64_CHARS = 41964
EXPECTED_BYTES = 31471
EXPECTED_SHA256 = "3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a"
SOURCE_BUNDLE_SHA256 = "4998d3a509114a46d54232d6e6d7f6bc0353b271bfde75fd3ba7af66956cffa8"
XLSX = OUT / "CP_Incident_Database_v1.authoritative-v1.xlsx"

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_DOC = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN, "r": REL_DOC, "p": REL_PKG}


def col_num(col: str) -> int:
    n = 0
    for ch in col:
        n = n * 26 + ord(ch.upper()) - 64
    return n


def col_name(n: int) -> str:
    out = ""
    while n:
        n, r = divmod(n - 1, 26)
        out = chr(65 + r) + out
    return out


def cell_rc(ref: str) -> tuple[int, int]:
    m = re.fullmatch(r"([A-Z]+)(\d+)", ref)
    if not m:
        raise ValueError(ref)
    return int(m.group(2)), col_num(m.group(1))


def shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return ["".join((t.text or "") for t in si.iter(f"{{{MAIN}}}t")) for si in root.findall("m:si", NS)]


def decode_cell(c: ET.Element, shared: list[str]) -> tuple[str, str, str, str]:
    ctype = c.attrib.get("t", "")
    style = c.attrib.get("s", "")
    f = c.find("m:f", NS)
    formula = "" if f is None or f.text is None else f.text
    if ctype == "inlineStr":
        node = c.find("m:is", NS)
        value = "" if node is None else "".join((t.text or "") for t in node.iter(f"{{{MAIN}}}t"))
        return value, formula, style, ctype
    v = c.find("m:v", NS)
    raw = "" if v is None or v.text is None else v.text
    if ctype == "s" and raw:
        value = shared[int(raw)]
    elif ctype == "b":
        value = "TRUE" if raw == "1" else "FALSE"
    else:
        value = raw
    return value, formula, style, ctype


def sheet_metadata(zf: zipfile.ZipFile) -> list[dict]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    relmap = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", NS)}
    result = []
    for s in wb.findall("m:sheets/m:sheet", NS):
        rid = s.attrib[f"{{{REL_DOC}}}id"]
        target = relmap[rid]
        if target.startswith("/"):
            path = target.lstrip("/")
        elif target.startswith("xl/"):
            path = target
        else:
            path = "xl/" + target.lstrip("/")
        result.append({"name": s.attrib["name"], "path": path})
    return result


def parse_sheet(zf: zipfile.ZipFile, meta: dict, shared: list[str]) -> dict:
    root = ET.fromstring(zf.read(meta["path"]))
    cells = []
    max_row = max_col = 0
    for c in root.findall(".//m:sheetData/m:row/m:c", NS):
        ref = c.attrib.get("r")
        if not ref:
            continue
        row, col = cell_rc(ref)
        value, formula, style, ctype = decode_cell(c, shared)
        max_row, max_col = max(max_row, row), max(max_col, col)
        cells.append({"sheet": meta["name"], "ref": ref, "row": row, "col": col, "value": value, "formula": formula, "style": style, "type": ctype})
    merged = [m.attrib.get("ref", "") for m in root.findall("m:mergeCells/m:mergeCell", NS)]
    return {**meta, "cells": cells, "max_row": max_row, "max_col": max_col, "merged": merged}


def matrix(sheet: dict) -> list[list[str]]:
    rows = [[""] * sheet["max_col"] for _ in range(sheet["max_row"])]
    for c in sheet["cells"]:
        rows[c["row"] - 1][c["col"] - 1] = c["value"]
    return rows


def clean_header(value: str, idx: int) -> str:
    value = re.sub(r"\s+", " ", (value or "").strip())
    return value or f"UNNAMED_{idx}"


def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in PARTS if not p.exists()]
    if missing:
        raise SystemExit("Missing recovered source chunks: " + ", ".join(missing))

    part_records = []
    pieces = []
    for p in PARTS:
        raw = p.read_bytes()
        text = raw.decode("ascii").strip()
        pieces.append(text)
        part_records.append({"name": p.name, "chars": len(text), "sha256": hashlib.sha256(text.encode("ascii")).hexdigest()})

    stream = "".join(pieces)
    decoded = base64.b64decode(stream, validate=True)
    actual_sha = hashlib.sha256(decoded).hexdigest()
    exact = len(stream) == EXPECTED_B64_CHARS and len(decoded) == EXPECTED_BYTES and actual_sha == EXPECTED_SHA256
    if not exact:
        evidence = {
            "status": "FAIL",
            "expected_base64_chars": EXPECTED_B64_CHARS,
            "actual_base64_chars": len(stream),
            "expected_bytes": EXPECTED_BYTES,
            "actual_bytes": len(decoded),
            "expected_sha256": EXPECTED_SHA256,
            "actual_sha256": actual_sha,
            "parts": part_records,
        }
        (OUT / "AUTHORITATIVE_V1_IDENTITY_FAILURE.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
        raise SystemExit("Authoritative v1 identity verification FAILED; no workbook inventory produced")

    XLSX.write_bytes(decoded)
    with zipfile.ZipFile(XLSX) as zf:
        shared = shared_strings(zf)
        sheets = [parse_sheet(zf, meta, shared) for meta in sheet_metadata(zf)]

    # Export all cells/formulas for reproducible audit.
    with (OUT / "workbook_cells.tsv").open("w", encoding="utf-8", newline="") as f:
        fields = ["sheet", "ref", "row", "col", "value", "formula", "style", "type"]
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for s in sheets:
            w.writerows(s["cells"])

    formulas = [c for s in sheets for c in s["cells"] if c["formula"]]
    with (OUT / "formula_inventory.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sheet", "ref", "formula", "value"], delimiter="\t")
        w.writeheader()
        for c in formulas:
            w.writerow({k: c[k] for k in ["sheet", "ref", "formula", "value"]})

    by_name = {s["name"]: s for s in sheets}
    if "Incidents" not in by_name:
        raise SystemExit("Verified workbook has no Incidents worksheet")
    incident = by_name["Incidents"]
    rows = matrix(incident)
    headers = [clean_header(v, i + 1) for i, v in enumerate(rows[0])]
    data_rows = [r for r in rows[1:] if any((v or "").strip() for v in r)]
    with (OUT / "incident_rows.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(headers)
        w.writerows(data_rows)

    blanks = Counter()
    for i, h in enumerate(headers):
        blanks[h] = sum(1 for r in data_rows if i >= len(r) or not (r[i] or "").strip())

    summary = {
        "status": "PASS",
        "source_bundle_sha256": SOURCE_BUNDLE_SHA256,
        "base64_chars": len(stream),
        "decoded_bytes": len(decoded),
        "sha256": actual_sha,
        "sheet_count": len(sheets),
        "sheet_names": [s["name"] for s in sheets],
        "incident_rows": len(data_rows),
        "incident_columns": len(headers),
        "incident_headers": headers,
        "blank_counts": dict(blanks),
        "parts": part_records,
        "sheets": [
            {
                "name": s["name"],
                "used_range": f"A1:{col_name(s['max_col'])}{s['max_row']}" if s["max_row"] and s["max_col"] else "empty",
                "max_row": s["max_row"],
                "max_col": s["max_col"],
                "nonempty_cells": sum(1 for c in s["cells"] if c["value"] or c["formula"]),
                "formula_count": sum(1 for c in s["cells"] if c["formula"]),
                "merged_ranges": s["merged"],
            }
            for s in sheets
        ],
    }
    (OUT / "authoritative_v1_inventory.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Authoritative CP Incident Database v1 — Reconstruction and Inventory",
        "",
        "**Identity verification: PASS**",
        "",
        f"- Source bundle SHA-256: `{SOURCE_BUNDLE_SHA256}`",
        f"- Base64 stream: `{len(stream)}` characters (expected `{EXPECTED_B64_CHARS}`)",
        f"- Reconstructed workbook: `{len(decoded)}` bytes (expected `{EXPECTED_BYTES}`)",
        f"- Workbook SHA-256: `{actual_sha}`",
        "- Historical v1 was not edited; this is an exact working reconstruction.",
        "",
        "## Workbook structure",
        "",
        "| Sheet | Used range | Non-empty cells | Formulas |",
        "|---|---:|---:|---:|",
    ]
    for s in summary["sheets"]:
        lines.append(f"| {s['name']} | {s['used_range']} | {s['nonempty_cells']} | {s['formula_count']} |")
    lines += [
        "",
        f"The `Incidents` sheet contains **{len(data_rows)} records** plus one header row and **{len(headers)} columns**.",
        "",
        "## Incident columns",
        "",
    ]
    lines.extend(f"{i}. `{h}`" for i, h in enumerate(headers, 1))
    lines += [
        "",
        "## Generated audit inputs",
        "",
        "- `CP_Incident_Database_v1.authoritative-v1.xlsx` — exact reconstructed workbook.",
        "- `authoritative_v1_inventory.json` — structural inventory and blank counts.",
        "- `workbook_cells.tsv` — cell-level export.",
        "- `formula_inventory.tsv` — formula export.",
        "- `incident_rows.tsv` — 52-row audit input.",
        "",
        "No researcher-final classification was added or changed in this reconstruction step.",
    ]
    (OUT / "AUTHORITATIVE_V1_RECONSTRUCTION_AND_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
