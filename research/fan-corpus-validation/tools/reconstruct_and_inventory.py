#!/usr/bin/env python3
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
EXPECTED_SIZE = 31471
EXPECTED_SHA256 = "3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a"
XLSX = OUT / "CP_Incident_Database_v1.reconstructed.xlsx"

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
    out = []
    for si in root.findall("m:si", N):
        out.append("".join((t.text or "") for t in si.iter(f"{{{NS_MAIN}}}t")))
    return out


def decode_cell(c: ET.Element, shared: list[str]) -> tuple[str, str | None, str | None]:
    ctype = c.attrib.get("t")
    style = c.attrib.get("s")
    f = c.find("m:f", N)
    formula = f.text if f is not None else None
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


def load_sheets(zf: zipfile.ZipFile) -> list[dict]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels.findall("p:Relationship", N)}
    sheets = []
    for s in wb.findall("m:sheets/m:sheet", N):
        rid = s.attrib[f"{{{NS_REL_DOC}}}id"]
        target = rel_map[rid]
        if target.startswith("/"):
            path = target.lstrip("/")
        elif target.startswith("xl/"):
            path = target
        else:
            path = "xl/" + target.lstrip("/")
        sheets.append({"name": s.attrib.get("name", ""), "sheetId": s.attrib.get("sheetId", ""), "rid": rid, "path": path})
    return sheets


def parse_sheet(zf: zipfile.ZipFile, sheet: dict, shared: list[str]) -> dict:
    root = ET.fromstring(zf.read(sheet["path"]))
    cells, formulas = [], []
    max_row = max_col = 0
    for c in root.findall(".//m:sheetData/m:row/m:c", N):
        ref = c.attrib.get("r")
        if not ref:
            continue
        row, col = parse_ref(ref)
        value, formula, style = decode_cell(c, shared)
        max_row, max_col = max(max_row, row), max(max_col, col)
        cell = {"sheet": sheet["name"], "ref": ref, "row": row, "col": col, "value": value, "formula": formula or "", "style": style or "", "type": c.attrib.get("t", "")}
        cells.append(cell)
        if formula:
            formulas.append(cell)
    merged = [x.attrib.get("ref", "") for x in root.findall("m:mergeCells/m:mergeCell", N)]
    return {**sheet, "cells": cells, "formulas": formulas, "merged": merged, "max_row": max_row, "max_col": max_col, "nonempty_cells": sum(1 for c in cells if c["value"] or c["formula"])}


def matrix(sheet_data: dict) -> list[list[str]]:
    rows = [[""] * sheet_data["max_col"] for _ in range(sheet_data["max_row"])]
    for c in sheet_data["cells"]:
        rows[c["row"] - 1][c["col"] - 1] = c["value"]
    return rows


def score_incident_header(row: list[str]) -> int:
    text = " | ".join(v.strip().upper() for v in row if v.strip())
    markers = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "INCIDENT"]
    return sum(1 for m in markers if m in text)


def choose_incident_sheet(sheets: list[dict]) -> tuple[dict, int]:
    candidates = []
    for s in sheets:
        rows = matrix(s)
        for idx, row in enumerate(rows[:15], start=1):
            candidates.append((score_incident_header(row), s["max_row"], s["max_col"], s, idx))
    candidates.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    score, _, _, sheet, row = candidates[0]
    if score < 3:
        raise RuntimeError("Could not identify incident table header reliably")
    return sheet, row


def normalized_header(v: str, idx: int) -> str:
    v = re.sub(r"\s+", " ", (v or "").strip())
    return v if v else f"UNNAMED_{idx}"


def main() -> None:
    missing = [str(p) for p in PARTS if not p.exists()]
    if missing:
        raise SystemExit("Missing Base64 parts: " + ", ".join(missing))

    stream = "".join(p.read_text(encoding="utf-8").strip() for p in PARTS)
    decoded = base64.b64decode(stream, validate=True)
    XLSX.write_bytes(decoded)
    size = len(decoded)
    sha = hashlib.sha256(decoded).hexdigest()
    if size != EXPECTED_SIZE or sha != EXPECTED_SHA256:
        raise SystemExit(f"Verification failed: size={size} sha={sha}; expected size={EXPECTED_SIZE} sha={EXPECTED_SHA256}")

    with zipfile.ZipFile(XLSX) as zf:
        shared = read_shared_strings(zf)
        sheet_meta = load_sheets(zf)
        sheets = [parse_sheet(zf, s, shared) for s in sheet_meta]

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

    incident_sheet, header_row = choose_incident_sheet(sheets)
    rows = matrix(incident_sheet)
    headers = [normalized_header(v, i + 1) for i, v in enumerate(rows[header_row - 1])]
    data_rows = [r for r in rows[header_row:] if any((v or "").strip() for v in r)]

    with (OUT / "incident_rows.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(headers)
        w.writerows(data_rows)

    blank_counts = Counter()
    for idx, h in enumerate(headers):
        blank_counts[h] = sum(1 for r in data_rows if idx >= len(r) or not (r[idx] or "").strip())

    summary = {
        "expected_sha256": EXPECTED_SHA256,
        "actual_sha256": sha,
        "expected_bytes": EXPECTED_SIZE,
        "actual_bytes": size,
        "base64_chars": len(stream),
        "sheet_count": len(sheets),
        "incident_sheet": incident_sheet["name"],
        "incident_header_row": header_row,
        "incident_data_rows": len(data_rows),
        "incident_column_count": len(headers),
        "headers": headers,
        "blank_counts": dict(blank_counts),
        "sheets": [{"name": s["name"], "path": s["path"], "max_row": s["max_row"], "max_col": s["max_col"], "nonempty_cells": s["nonempty_cells"], "formula_count": len(s["formulas"]), "merged_ranges": s["merged"]} for s in sheets],
    }
    (OUT / "workbook_inventory.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# CP Incident Database v1 — Reconstruction and Workbook Inventory", "",
        "## Byte-level verification", "",
        f"- Reconstructed file: `{XLSX.relative_to(ROOT)}`",
        f"- Expected bytes: `{EXPECTED_SIZE}`",
        f"- Actual bytes: `{size}`",
        f"- Expected SHA-256: `{EXPECTED_SHA256}`",
        f"- Actual SHA-256: `{sha}`",
        "- Verification: **PASS**", f"- Concatenated Base64 stream length: `{len(stream)}` characters", "",
        "The historical Base64 source parts were read-only inputs. They were not edited.", "",
        "## Workbook structure", "", f"Workbook contains **{len(sheets)} worksheets**.", "",
        "| Sheet | Used range | Non-empty cells | Formulas | Merged ranges |", "|---|---:|---:|---:|---:|",
    ]
    for s in sheets:
        used = f"A1:{num_to_col(s['max_col'])}{s['max_row']}" if s["max_row"] and s["max_col"] else "empty"
        lines.append(f"| {s['name']} | {used} | {s['nonempty_cells']} | {len(s['formulas'])} | {len(s['merged'])} |")
    lines += ["", "## Incident table detection", "", f"- Incident worksheet: **{incident_sheet['name']}**", f"- Header row: **{header_row}**", f"- Non-empty data rows after header: **{len(data_rows)}**", f"- Columns: **{len(headers)}**", "", "### Column headers", ""]
    lines.extend(f"{i}. `{h}`" for i, h in enumerate(headers, start=1))
    lines += ["", "## Blank cells by incident-table column", "", "| Column | Blank rows |", "|---|---:|"]
    for h in headers:
        lines.append(f"| {h.replace('|', '\\|')} | {blank_counts[h]} |")
    lines += ["", "## Generated machine-readable artifacts", "", "- `workbook_inventory.json` — exact structural summary.", "- `workbook_cells.tsv` — all represented worksheet cells with formulas and styles.", "- `formula_inventory.tsv` — every formula cell and cached value.", "- `incident_rows.tsv` — incident-table export used for WP2 audit.", "", "No scientific classification has been changed by this reconstruction step."]
    (OUT / "WORKBOOK_RECONSTRUCTION_AND_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
