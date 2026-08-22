#!/usr/bin/env python3
"""Inspect the Base64 workbook payload currently present in Git.

Important evidence rule: the preservation record declares a 31,471-byte workbook
with SHA-256 3a5d..., while the actual Git Base64 parts may or may not reconstruct
to that identity. This tool never upgrades a mismatched payload to authoritative
v1. It records the mismatch, then inventories the available payload if it is a
valid XLSX so the research team can assess recoverability without hiding the
chain-of-custody defect.
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
SRC = ROOT / "archive" / "research-lineage-2026-01" / "binary"
OUT = ROOT / "research" / "fan-corpus-validation" / "work"
OUT.mkdir(parents=True, exist_ok=True)

PARTS = [
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-000",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-001",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-002a",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-002b",
    SRC / "CP_Incident_Database_v1.xlsx.b64.part-003",
]
EXPECTED_B64_CHARS = 41964
EXPECTED_SIZE = 31471
EXPECTED_SHA256 = "3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a"
PAYLOAD = OUT / "CP_Incident_Database_v1.git_payload.xlsx"

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_REL_DOC = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
N = {"m": NS_MAIN, "r": NS_REL_DOC, "p": NS_REL_PKG}


def col_to_num(col: str) -> int:
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch.upper()) - 64)
    return n


def num_to_col(n: int) -> str:
    s = ""
    while n:
        n, rem = divmod(n - 1, 26)
        s = chr(65 + rem) + s
    return s


def parse_ref(ref: str) -> tuple[int, int]:
    m = re.fullmatch(r"([A-Z]+)(\d+)", ref)
    if not m:
        raise ValueError(ref)
    return int(m.group(2)), col_to_num(m.group(1))


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return ["".join((t.text or "") for t in si.iter(f"{{{NS_MAIN}}}t")) for si in root.findall("m:si", N)]


def decode_cell(c: ET.Element, shared: list[str]) -> tuple[str, str, str]:
    ctype = c.attrib.get("t", "")
    style = c.attrib.get("s", "")
    f = c.find("m:f", N)
    formula = "" if f is None or f.text is None else f.text
    if ctype == "inlineStr":
        is_el = c.find("m:is", N)
        value = "" if is_el is None else "".join((t.text or "") for t in is_el.iter(f"{{{NS_MAIN}}}t"))
        return value, formula, style
    v = c.find("m:v", N)
    raw = "" if v is None or v.text is None else v.text
    if ctype == "s" and raw:
        try:
            value = shared[int(raw)]
        except (ValueError, IndexError):
            value = f"[INVALID_SHARED_STRING:{raw}]"
    elif ctype == "b":
        value = "TRUE" if raw == "1" else "FALSE"
    else:
        value = raw
    return value, formula, style


def load_sheet_meta(zf: zipfile.ZipFile) -> list[dict]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels.findall("p:Relationship", N)}
    out = []
    for s in wb.findall("m:sheets/m:sheet", N):
        rid = s.attrib[f"{{{NS_REL_DOC}}}id"]
        target = rel_map[rid]
        if target.startswith("/"):
            path = target.lstrip("/")
        elif target.startswith("xl/"):
            path = target
        else:
            path = "xl/" + target.lstrip("/")
        out.append({"name": s.attrib.get("name", ""), "sheetId": s.attrib.get("sheetId", ""), "path": path})
    return out


def parse_sheet(zf: zipfile.ZipFile, meta: dict, shared: list[str]) -> dict:
    root = ET.fromstring(zf.read(meta["path"]))
    cells, formulas = [], []
    max_row = max_col = 0
    for c in root.findall(".//m:sheetData/m:row/m:c", N):
        ref = c.attrib.get("r")
        if not ref:
            continue
        row, col = parse_ref(ref)
        value, formula, style = decode_cell(c, shared)
        max_row = max(max_row, row)
        max_col = max(max_col, col)
        item = {"sheet": meta["name"], "ref": ref, "row": row, "col": col, "value": value, "formula": formula, "style": style, "type": c.attrib.get("t", "")}
        cells.append(item)
        if formula:
            formulas.append(item)
    merged = [x.attrib.get("ref", "") for x in root.findall("m:mergeCells/m:mergeCell", N)]
    return {**meta, "cells": cells, "formulas": formulas, "merged": merged, "max_row": max_row, "max_col": max_col, "nonempty_cells": sum(1 for c in cells if c["value"] or c["formula"])}


def matrix(sheet: dict) -> list[list[str]]:
    rows = [[""] * sheet["max_col"] for _ in range(sheet["max_row"])]
    for c in sheet["cells"]:
        rows[c["row"] - 1][c["col"] - 1] = c["value"]
    return rows


def header_score(row: list[str]) -> int:
    text = " | ".join((v or "").strip().upper() for v in row if (v or "").strip())
    markers = [
        "INCIDENT", "LOCATION", "TASK CONTEXT", "USER WORDS", "POSSIBLE INTERPRETATIONS",
        "INTERPRETATION CHOSEN", "WAS USER ASKED", "ASSUMPTION", "FIRST VISIBLE SIGNAL",
        "TURNS UNTIL DETECTION", "CONSEQUENCE", "RESOLUTION", "PRIOR CONTEXT", "CONFIDENCE",
        "IPP TYPE", "MATERIALITY", "CONTEXT FACTOR", "TRUE INTENT", "VALIDATION FLAG",
    ]
    return sum(1 for m in markers if m in text)


def find_incident_table(sheets: list[dict]) -> tuple[dict, int, int]:
    candidates = []
    for sheet in sheets:
        rows = matrix(sheet)
        for idx, row in enumerate(rows[:20], start=1):
            candidates.append((header_score(row), sheet["max_row"], sheet["max_col"], sheet, idx))
    candidates.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    score, _, _, sheet, row = candidates[0]
    return sheet, row, score


def clean_header(v: str, idx: int) -> str:
    v = re.sub(r"\s+", " ", (v or "").strip())
    return v or f"UNNAMED_{idx}"


def main() -> None:
    missing = [str(p) for p in PARTS if not p.exists()]
    if missing:
        raise SystemExit("Missing Base64 parts: " + ", ".join(missing))

    part_info = []
    pieces = []
    for p in PARTS:
        raw = p.read_bytes()
        text = raw.decode("utf-8").strip()
        pieces.append(text)
        part_info.append({
            "name": p.name,
            "repository_bytes": len(raw),
            "trimmed_chars": len(text),
            "sha256": hashlib.sha256(raw).hexdigest(),
        })

    stream = "".join(pieces)
    decoded = base64.b64decode(stream, validate=True)
    PAYLOAD.write_bytes(decoded)
    actual_size = len(decoded)
    actual_sha = hashlib.sha256(decoded).hexdigest()
    identity_verified = actual_size == EXPECTED_SIZE and actual_sha == EXPECTED_SHA256 and len(stream) == EXPECTED_B64_CHARS
    identity_status = "MATCH" if identity_verified else "MISMATCH"

    zip_valid = zipfile.is_zipfile(PAYLOAD)
    sheets = []
    parse_error = None
    if zip_valid:
        try:
            with zipfile.ZipFile(PAYLOAD) as zf:
                shared = read_shared_strings(zf)
                sheets = [parse_sheet(zf, meta, shared) for meta in load_sheet_meta(zf)]
        except Exception as exc:  # preserve evidence instead of hiding parser failure
            parse_error = f"{type(exc).__name__}: {exc}"

    # Always write identity report, even if workbook parsing fails.
    identity = {
        "status": identity_status,
        "identity_verified": identity_verified,
        "expected_base64_chars": EXPECTED_B64_CHARS,
        "actual_base64_chars": len(stream),
        "expected_bytes": EXPECTED_SIZE,
        "actual_bytes": actual_size,
        "expected_sha256": EXPECTED_SHA256,
        "actual_sha256": actual_sha,
        "zip_valid": zip_valid,
        "parse_error": parse_error,
        "parts": part_info,
    }
    (OUT / "git_payload_identity.json").write_text(json.dumps(identity, indent=2) + "\n", encoding="utf-8")

    if not sheets:
        report = [
            "# CP Incident Database v1 — Git Payload Reconstruction",
            "",
            f"**Identity verdict: {identity_status}**",
            "",
            f"- Expected Base64 chars: `{EXPECTED_B64_CHARS}`",
            f"- Actual Base64 chars: `{len(stream)}`",
            f"- Expected bytes: `{EXPECTED_SIZE}`",
            f"- Actual bytes: `{actual_size}`",
            f"- Expected SHA-256: `{EXPECTED_SHA256}`",
            f"- Actual SHA-256: `{actual_sha}`",
            f"- Valid ZIP container: `{zip_valid}`",
            f"- Parse error: `{parse_error}`",
            "",
            "The Git payload is not promoted to authoritative v1 unless the declared byte identity matches.",
        ]
        (OUT / "GIT_PAYLOAD_RECONSTRUCTION_AND_INVENTORY.md").write_text("\n".join(report) + "\n", encoding="utf-8")
        print(json.dumps(identity, indent=2))
        return

    with (OUT / "workbook_cells.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sheet", "ref", "row", "col", "value", "formula", "style", "type"], delimiter="\t")
        w.writeheader()
        for s in sheets:
            w.writerows(s["cells"])

    with (OUT / "formula_inventory.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sheet", "ref", "formula", "value"], delimiter="\t")
        w.writeheader()
        for s in sheets:
            for c in s["formulas"]:
                w.writerow({"sheet": s["name"], "ref": c["ref"], "formula": c["formula"], "value": c["value"]})

    incident_sheet, header_row, score = find_incident_table(sheets)
    rows = matrix(incident_sheet)
    headers = [clean_header(v, i + 1) for i, v in enumerate(rows[header_row - 1])]
    data_rows = [r for r in rows[header_row:] if any((v or "").strip() for v in r)]
    with (OUT / "incident_rows.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(headers)
        w.writerows(data_rows)

    blank_counts = Counter()
    for idx, h in enumerate(headers):
        blank_counts[h] = sum(1 for r in data_rows if idx >= len(r) or not (r[idx] or "").strip())

    summary = {
        **identity,
        "sheet_count": len(sheets),
        "incident_sheet": incident_sheet["name"],
        "incident_header_row": header_row,
        "incident_header_score": score,
        "incident_data_rows": len(data_rows),
        "incident_column_count": len(headers),
        "headers": headers,
        "blank_counts": dict(blank_counts),
        "sheets": [
            {
                "name": s["name"], "path": s["path"], "max_row": s["max_row"], "max_col": s["max_col"],
                "nonempty_cells": s["nonempty_cells"], "formula_count": len(s["formulas"]), "merged_ranges": s["merged"],
            }
            for s in sheets
        ],
    }
    (OUT / "workbook_inventory.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# CP Incident Database v1 — Git Payload Reconstruction and Inventory",
        "",
        f"**Identity verdict: {identity_status}**",
        "",
        "## Declared identity vs current Git payload",
        "",
        f"- Expected Base64 stream: `{EXPECTED_B64_CHARS}` characters",
        f"- Current Git Base64 stream: `{len(stream)}` characters",
        f"- Expected decoded size: `{EXPECTED_SIZE}` bytes",
        f"- Current Git decoded size: `{actual_size}` bytes",
        f"- Expected SHA-256: `{EXPECTED_SHA256}`",
        f"- Current Git SHA-256: `{actual_sha}`",
        f"- Valid XLSX/ZIP payload: `{zip_valid}`",
        "",
        "**Evidence interpretation:** A mismatched but parseable payload may be inspected for recovery, but it is not the cryptographically declared historical v1 workbook.",
        "",
        "## Source parts",
        "",
        "| Part | Repo bytes | Trimmed Base64 chars | SHA-256 |",
        "|---|---:|---:|---|",
    ]
    for p in part_info:
        lines.append(f"| {p['name']} | {p['repository_bytes']} | {p['trimmed_chars']} | `{p['sha256']}` |")
    lines += [
        "",
        "## Workbook structure of the current Git payload",
        "",
        f"Workbook contains **{len(sheets)} worksheets**.",
        "",
        "| Sheet | Used range | Non-empty cells | Formulas | Merged ranges |",
        "|---|---:|---:|---:|---:|",
    ]
    for s in sheets:
        used = f"A1:{num_to_col(s['max_col'])}{s['max_row']}" if s["max_row"] and s["max_col"] else "empty"
        lines.append(f"| {s['name']} | {used} | {s['nonempty_cells']} | {len(s['formulas'])} | {len(s['merged'])} |")
    lines += [
        "",
        "## Incident-table detection",
        "",
        f"- Candidate incident worksheet: **{incident_sheet['name']}**",
        f"- Candidate header row: **{header_row}**",
        f"- Header detection score: **{score}**",
        f"- Non-empty rows after header: **{len(data_rows)}**",
        f"- Columns: **{len(headers)}**",
        "",
        "### Column headers",
        "",
    ]
    lines.extend(f"{i}. `{h}`" for i, h in enumerate(headers, start=1))
    lines += ["", "## Blank cells by candidate incident column", "", "| Column | Blank rows |", "|---|---:|"]
    for h in headers:
        lines.append(f"| {h.replace('|', '\\|')} | {blank_counts[h]} |")
    lines += [
        "",
        "## Generated artifacts",
        "",
        "- `CP_Incident_Database_v1.git_payload.xlsx` — decoded current Git payload; **not authoritative v1 unless identity MATCHES**.",
        "- `git_payload_identity.json` — byte-level identity evidence.",
        "- `workbook_inventory.json` — structural inventory.",
        "- `workbook_cells.tsv` — all represented worksheet cells.",
        "- `formula_inventory.tsv` — formula inventory.",
        "- `incident_rows.tsv` — candidate incident-table export for recoverability audit.",
        "",
        "No researcher classification is changed by this tool.",
    ]
    (OUT / "GIT_PAYLOAD_RECONSTRUCTION_AND_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
