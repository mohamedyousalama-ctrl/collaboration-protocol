# CP v1.0.1 Validation Tests
## Targeted Tests for Bug Fixes

**Version:** 1.0.1  
**Date:** January 27, 2025  
**Purpose:** Validate that all 5 bug fixes work correctly  
**Target File:** `cp_v1_0_1_runtime_persistent.html`

---

## Pre-Test Setup

1. Open `cp_v1_0_1_runtime_persistent.html` in browser
2. Verify title shows "CP v1.0.1 Runtime"
3. Click "Clear All Data" → Confirm both prompts
4. Verify fresh session started

---

## Fix 1: DPT-17 — "Off topic" Scope Boundary Pattern

**Issue:** "off topic" was not recognized as out-of-scope signal  
**Fix Location:** `SignalClassifier.classify()` line 264  
**Change:** Added `off topic|different subject` to scope boundary pattern

### Test 1A: "Off topic" triggers friction

**Test Steps:**
1. Click "New Context" → Enter: "Testing scope boundaries" → OK
2. When prompted for agent → Cancel (No)
3. Type: "I want to test scope detection" → Send Signal
4. Click "Confirm" to verify intent
5. Type: "off topic but what's the weather?" → Send Signal

**Expected Behavior:**
- Orange friction message appears with "⚠️ FRICTION:"
- Message says "Outside context"
- Status bar State shows "awaiting_clarification"

**Verification Checklist:**
- [ ] Friction message displayed (orange background)
- [ ] Event Log shows `friction.triggered` with type `scope_boundary`
- [ ] System state changed to `awaiting_clarification`

**Status:** ☐ PASS / ☐ FAIL

---

### Test 1B: "Different subject" triggers friction

**Test Steps:**
1. Continue from Test 1A (or set up fresh context with verified intent)
2. Type: "Noted" → Send (to clear friction from 1A)
3. Type: "different subject - can you help with cooking?" → Send Signal

**Expected Behavior:**
- Orange friction message appears
- Friction triggered for scope_boundary

**Verification Checklist:**
- [ ] Friction message displayed
- [ ] Event Log shows `friction.triggered` with type `scope_boundary`

**Status:** ☐ PASS / ☐ FAIL

---

## Fix 2: DPT-19/L2 — Revise Button Logging

**Issue:** Clicking "Revise" did not create a log entry  
**Fix Location:** `UI.revise()` lines 591-601  
**Change:** Added `LogStore.append()` for `intent.revised` event

### Test 2A: Revise creates log entry

**Test Steps:**
1. Click "Clear All Data" → Confirm both
2. Click "New Context" → Enter: "Testing revise logging" → OK → Cancel (no agent)
3. Type: "I want to explore something" → Send Signal
4. Verification prompt appears
5. Click "Revise" button

**Expected Behavior:**
- Message: "Verification cleared."
- Log entry created for the revise action

**Verification Checklist:**
- [ ] "Verification cleared." message displayed
- [ ] Event Log shows `intent.revised` entry
- [ ] Log entry details mention "User revised pending intent verification"
- [ ] System state returns to `idle`

**Status:** ☐ PASS / ☐ FAIL

---

### Test 2B: Revise logs different verification types

**Test Steps:**
1. Create context, verify intent (complete setup)
2. Type: "Lock in 'Test content' as a fact" → Send Signal
3. Node verification prompt appears
4. Click "Revise" button

**Expected Behavior:**
- Log entry shows revise for "node" verification type

**Verification Checklist:**
- [ ] Event Log shows `intent.revised` entry
- [ ] Log entry details mention "User revised pending node verification"

**Status:** ☐ PASS / ☐ FAIL

---

## Fix 3: EDGE-17 — Agent Suspension on Context Archive

**Issue:** Agent was not suspended when context archived via New Context  
**Fix Location:** `UI.newContext()` lines 512-528  
**Change:** Added agent suspension and logging before context archive

### Test 3A: Agent suspended when creating new context

**Test Steps:**
1. Click "Clear All Data" → Confirm both
2. Click "New Context" → Enter: "Context A with agent" → OK
3. When prompted for agent → OK (Yes, enable agent)
4. Verify: Agents panel shows "CP Advisory Agent" with status "active"
5. Click "New Context" → Enter: "Context B" → OK
6. When prompted for agent → Cancel (No agent for B)

**Expected Behavior:**
- Context A archived
- Agent from Context A suspended BEFORE context archived
- Two log entries: agent.state_changed (suspended), then context.state_changed (archived)

**Verification Checklist:**
- [ ] Event Log shows `agent.state_changed` with details "Agent suspended"
- [ ] Log entry reason shows "Context archived for new context"
- [ ] `agent.state_changed` appears BEFORE `context.state_changed` (archived)
- [ ] Context B created successfully

**Status:** ☐ PASS / ☐ FAIL

---

### Test 3B: Verify agent state in storage

**Test Steps:**
1. Continue from Test 3A
2. Click "Export Session"
3. Open downloaded JSON file
4. Find the agent from Context A

**Expected Behavior:**
- Agent object shows `"state": "suspended"`

**Verification Checklist:**
- [ ] Exported JSON contains agent with `state: "suspended"`
- [ ] Agent's context_id matches Context A's ID

**Status:** ☐ PASS / ☐ FAIL

---

## Fix 4: EDGE-22 — Storage Failure Notification

**Issue:** No user notification when localStorage save fails  
**Fix Location:** `Persistence.save()` lines 189-198  
**Change:** Added try/catch with `UI.addMessage()` on failure

### Test 4A: Verify error handling code exists

**Test Steps:**
1. Open browser Developer Tools (F12) → Sources tab
2. Find `Persistence.save` function in the code
3. Verify try/catch block exists with UI.addMessage call

**Expected Behavior:**
- Code shows:
  ```javascript
  catch(e) { 
    console.error('Storage save failed:', e);
    UI.addMessage('system', '⚠️ Storage save failed: ' + e.message + '. Data may not persist.');
  }
  ```

**Verification Checklist:**
- [ ] try/catch block present in Persistence.save()
- [ ] catch block calls UI.addMessage with warning
- [ ] Error logged to console

**Status:** ☐ PASS / ☐ FAIL

---

### Test 4B: Simulate storage failure (Advanced)

**Note:** This test requires manually triggering a storage failure, which is difficult in normal operation. This documents the expected behavior.

**Simulated Scenario:**
- If localStorage is full or unavailable
- When Persistence.save() is called

**Expected Behavior:**
- System message appears: "⚠️ Storage save failed: [error]. Data may not persist."
- Error logged to browser console
- Application continues to function (graceful degradation)

**Verification Checklist:**
- [ ] Code review confirms error handling implemented
- [ ] (Optional) If able to simulate: error message displayed to user

**Status:** ☐ PASS (Code Review) / ☐ FAIL

---

## Fix 5: L1 — Signal Received Logging

**Issue:** Individual signals were not logged as separate events  
**Fix Location:** `InteractionLoop.processSignal()` line 314  
**Change:** Added `signal.received` logging at start of function

### Test 5A: Signal received logged for normal signals

**Test Steps:**
1. Click "Clear All Data" → Confirm both
2. Click "New Context" → Enter: "Testing signal logging" → OK → Cancel (no agent)
3. Type: "Hello world" → Send Signal
4. Check Event Log

**Expected Behavior:**
- `signal.received` log entry created
- Entry appears before guardian.post_classification

**Verification Checklist:**
- [ ] Event Log shows `signal.received` entry
- [ ] Log details show "Signal: Hello world"
- [ ] Entry has correct context_id (or null if no context)
- [ ] `signal.received` appears in orange color in log

**Status:** ☐ PASS / ☐ FAIL

---

### Test 5B: Signal received logged for all signal types

**Test Steps:**
1. Continue from Test 5A
2. Type: "I want to explore testing" → Send Signal → Confirm
3. Type: "maybe" → Send Signal (triggers friction)
4. Type: "Actually I want to test logging" → Send Signal (clarification)
5. Check Event Log for all signal.received entries

**Expected Behavior:**
- Each signal creates a `signal.received` entry
- Total of 4 signal.received entries (including "Hello world" from 5A)

**Verification Checklist:**
- [ ] `signal.received` logged for intent signal
- [ ] `signal.received` logged for ambiguous signal ("maybe")
- [ ] `signal.received` logged for clarification signal
- [ ] All entries have timestamps and context references

**Status:** ☐ PASS / ☐ FAIL

---

### Test 5C: Signal truncated in log if too long

**Test Steps:**
1. Type a very long signal (>100 characters): "This is a very long signal that should be truncated in the log entry because we only store the first 100 characters of the signal text to keep logs manageable"
2. Send Signal
3. Check Event Log

**Expected Behavior:**
- Signal truncated to first 100 characters in log details

**Verification Checklist:**
- [ ] Log entry shows truncated signal (first 100 chars)
- [ ] No error from long signal

**Status:** ☐ PASS / ☐ FAIL

---

# Validation Summary

## Test Results Table

| Fix ID | Fix Description | Test ID | Status |
|--------|-----------------|---------|--------|
| Fix 1 | DPT-17: "Off topic" pattern | 1A | ☐ |
| Fix 1 | DPT-17: "Different subject" pattern | 1B | ☐ |
| Fix 2 | DPT-19/L2: Revise logging (intent) | 2A | ☐ |
| Fix 2 | DPT-19/L2: Revise logging (node) | 2B | ☐ |
| Fix 3 | EDGE-17: Agent suspension | 3A | ☐ |
| Fix 3 | EDGE-17: Agent state in export | 3B | ☐ |
| Fix 4 | EDGE-22: Storage failure notification | 4A | ☐ |
| Fix 4 | EDGE-22: Error handling (code review) | 4B | ☐ |
| Fix 5 | L1: Signal received logging | 5A | ☐ |
| Fix 5 | L1: All signal types logged | 5B | ☐ |
| Fix 5 | L1: Long signal truncation | 5C | ☐ |

## Overall Validation Status

| Fix | Tests | Passed | Failed | Status |
|-----|-------|--------|--------|--------|
| Fix 1 (DPT-17) | 2 | | | ☐ VALIDATED |
| Fix 2 (DPT-19/L2) | 2 | | | ☐ VALIDATED |
| Fix 3 (EDGE-17) | 2 | | | ☐ VALIDATED |
| Fix 4 (EDGE-22) | 2 | | | ☐ VALIDATED |
| Fix 5 (L1) | 3 | | | ☐ VALIDATED |
| **TOTAL** | **11** | | | |

---

## Validation Certification

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  CP v1.0.1 VALIDATION                                       │
│                                                             │
│  Date: _______________                                      │
│                                                             │
│  All fixes validated: ☐ YES  ☐ NO                          │
│                                                             │
│  Notes: _____________________________________________       │
│                                                             │
│         _____________________________________________       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

**End of v1.0.1 Validation Tests**
