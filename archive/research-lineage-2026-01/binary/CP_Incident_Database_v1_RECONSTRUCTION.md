# Reconstructing `CP_Incident_Database_v1.xlsx`

The original workbook is preserved losslessly as Base64 text parts because the connected GitHub writer used in this preservation session exposes UTF-8 file writes rather than direct binary upload.

Concatenate the parts in lexical order and decode:

```sh
cat CP_Incident_Database_v1.xlsx.b64.part-* | base64 -d > CP_Incident_Database_v1.xlsx
```

Expected decoded size:

```text
31,471 bytes
```

Expected SHA-256:

```text
3a5d4e82c2d65473b1117d70b68428efd89319386a89978871f38edf8ee8ed4a
```

The Base64 stream is 41,964 characters. The source workbook contains the 52-row candidate incident corpus and the researcher-only classification fields described in the academic record. Those final researcher fields remain incomplete in this preserved version; the archive does not treat the workbook as a finished ground-truth dataset.
