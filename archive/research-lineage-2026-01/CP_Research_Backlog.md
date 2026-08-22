# CP Empirical Research Program — Master Backlog
**Owner: Mohamed Salama | Created: July 2026 | Status: Active**

**Objective:** Become the person who defines how intent fidelity is measured and governed. Vehicle: one empirical paper combining (1) first evidence of Silent Intent Inference, (2) IPP taxonomy grounded in real failures, (4) validated IPP detection algorithm — now upgraded with Klear comparative data and IntentHealth cross-domain pilots.

**Paper working title:** "Measuring Silent Intent Inference: Evidence from Naturalistic Corpora and a CP-Governed System"

---

## EPIC 0 — Publication pipeline (in flight)
- [ ] **0.1** Secure arXiv endorsement for cs.HC (LinkedIn outreach ongoing; use ready message)
- [ ] **0.2** Publish CP theory paper on arXiv once endorsed → this makes the Safety Floor addendum citation valid
- [ ] **0.3** Track JAIR review; prepare response strategy — the empirical program is the answer to the inevitable "no data" critique
- [ ] **0.4** Reply to Fan Chen-Chieh with Q1/Q2 nuance; keep collaboration door open (his field data = attribution consequences layer)

## EPIC 1 — Corpus: chat-log incident extraction (Study A — naturalistic evidence)
- [ ] **1.1** Run IPP Extraction Protocol v1.0 across all LLM windows (in progress — reports incoming)
- [ ] **1.2** Verify every incident quote against real transcripts → set C9=CONFIRMED (no unverified incident enters analysis)
- [ ] **1.3** Complete researcher-only classification (Part C) per incident: IPP type, materiality, Context Factor, effective ICD, ground-truth intent, cost
- [ ] **1.4** Build the incident database (one spreadsheet, one row per incident, all A+C fields)
- [ ] **1.5** Compute headline metrics: silent inference rate (A6=NO %), awareness gap (median A9 turns), cost totals (C6), distribution by IPP type
- [ ] **1.6** Identify NEW IPP types not in the original taxonomy → taxonomy v2
- [ ] **1.7** Flag benchmark candidates (C8=YES) → feed EPIC 5

## EPIC 2 — Klear comparative evaluation (Study B — controlled system evidence)
- [ ] **2.1** ⚠ FIX DATA INTEGRITY: FIN-R-04 ChatGPT/Gemini marked PENDING but scored Pass — run the tests or blank the rows. Audit the full log for any other pre-filled cells. **Blocker for any publication use.**
- [ ] **2.2** Add blind second-rater pass: export all responses as anonymized transcripts (system identity stripped), have an independent rater score Boundary Compliance / Scope Hold / Silent Advice; compute inter-rater agreement (target κ > 0.7) — this converts the pilot into defensible data
- [ ] **2.3** Reframe comparison correctly in all writing: "governed architecture vs prompt-level instruction," never "Klear beats GPT"
- [ ] **2.4** Document Klear's architecture formally (which CP constructs are implemented, how IPP detection works in production, audit log schema) — this is the systems-paper section
- [ ] **2.5** Fix and document known Klear gaps (false-positive scope warnings on FIN-R-01/02) — report them; honesty about your own system's errors is credibility
- [ ] **2.6** Preserve evidence chain: mirror all Google Drive session folders to a permanent archive with hashes
- [ ] **2.7** Decide: expand N (more testers, more scenarios) now, or publish as labeled pilot — recommendation: publish as pilot, expand in follow-up

## EPIC 3 — IntentHealth + Safety Floor (Study C — cross-domain + self-correction)
- [ ] **3.1** Write up Sessions 1–2 formally (methods, transcripts, GPT-4o-as-clinical-rater disclosed as a limitation — a model rating a model needs human clinical validation eventually)
- [ ] **3.2** Define SF profile assertion checklists so SCS becomes measurable (currently post-hoc estimates)
- [ ] **3.3** Sensitivity analysis on the 0.15 SCS weight in IFI-H (vary 0.10–0.25, show ranking stability)
- [ ] **3.4** Position the anomaly (high IFI ≠ clinical safety) as a headline finding — frameworks that discover their own limits are publishable
- [ ] **3.5** H5 validation study design: park until Studies A+B are written (avoid scope explosion)

## EPIC 4 — Algorithm validation (the "option 4" core)
- [ ] **4.1** Freeze IPP detection algorithm version (the one in paper lines 287–312 + Klear production variant; document divergence)
- [ ] **4.2** Run algorithm on the verified incident corpus (EPIC 1 output) → precision/recall against your manual labels
- [ ] **4.3** Run algorithm on Klear session transcripts → does it flag the same IPPs Klear fired in production?
- [ ] **4.4** Error analysis: where algorithm misses vs over-fires; connect to Semantic Materiality Proxy thresholds
- [ ] **4.5** Report computational cost on real data (replaces simulated 22–489ms latency claim)

## EPIC 5 — IFI-Bench seed (parallel, low effort now)
- [ ] **5.1** Convert C8=YES incidents into benchmark item drafts (prompt, context, interpretation set, materiality label, correct behavior per ICD, scoring rubric)
- [ ] **5.2** Add Klear scenario bank items (FIN-B, FIN-C, FIN-D categories are ready-made benchmark items)
- [ ] **5.3** Target: 50–100 items for IFI-Bench v0.1 — release as companion artifact to the empirical paper, GitHub + HuggingFace

## EPIC 6 — The empirical paper itself
- [ ] **6.1** Skeleton: Intro (SII problem, recap theory paper) → Study A (corpus) → Study B (Klear) → Study C (health pilots + SF anomaly) → Algorithm validation → Taxonomy v2 → Limitations → IFI-Bench announcement
- [ ] **6.2** Limitations section written FIRST (single-user corpus; non-blind pilot tester; asymmetric comparison; model-as-rater; single dates) — pre-empting is stronger than defending
- [ ] **6.3** Venue decision: CHI/CSCW (HCI systems+studies) vs IUI vs FAccT (accountability angle) — decide after data volume is known
- [ ] **6.4** Ethics/consent check: Usama's data (get written consent to publish), chat-log corpus is self-data (fine), health sessions are self-generated (fine)

---

## SEQUENCE (critical path)
1. **Now:** 0.1 endorsement outreach ∥ 1.1 extraction runs ∥ 2.1 data-integrity fix
2. **Next:** 1.2–1.5 corpus build → 4.2 algorithm vs corpus
3. **Then:** 2.2 blind re-rating → 6.1 paper skeleton
4. **Later:** 3.x write-ups, 5.x bench seed, 6.3 venue choice

## STANDING RULES
- No unverified quote enters the dataset. No pre-filled result survives audit.
- Every claim gets a limitation tag at the moment it's written, not at the end.
- LLMs extract; Mohamed classifies. Ground truth intent has exactly one source: you.
- Nothing cites "Salama 2026, arXiv" until the arXiv page exists.
