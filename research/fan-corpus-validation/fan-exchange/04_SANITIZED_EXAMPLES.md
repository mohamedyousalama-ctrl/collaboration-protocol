# Sanitized Coding Examples

## Read this before using the examples

These examples are included **only to demonstrate the coding logic and data shape** for the methods exchange.

They are deliberately:

- paraphrased rather than verbatim;
- stripped of repository names, people, secrets, customer data, and unnecessary project detail;
- labeled with current assistant recommendations rather than researcher-final classifications; and
- **not presented as C9-confirmed positive incidents**.

No example below should be quoted in a paper as empirical proof until the corresponding researcher decision and evidence status are finalized.

## Example 1 — scope ambiguity; provisional likely SII

**Sanitized profile:** The user identified a failure class involving messages grouped into a burst. The AI tested only an ordinary two-message case and treated that limited test as disproving the broader failure class. The user later clarified that passing the ordinary case did not withdraw the finding; additional burst shapes had to be tested.

| Field | Sanitized coding sketch |
|---|---|
| Candidate mechanism | A general failure class was silently narrowed to one representative case |
| A6 clarification before action | No |
| A8 visible mismatch | User later says the ordinary case did not resolve the broader finding |
| Consequence | New work order; additional cases tested; conclusion narrowed rather than withdrawn |
| Assistant construct recommendation | `LIKELY SII` |
| C0 recommendation | `INTENT` |
| C1 recommendation | `SCOPE` |
| Source status | Original task artifact corroborates the triggering scope; full interaction chronology remains unverified |
| Researcher status | Pending |

**Why useful for Fan:** It shows the difference between a technical test failure and the prior interpretive decision about **what the requested scope meant**.

## Example 2 — authority/content-as-command; provisional likely SII

**Sanitized profile:** A message contained a block of database inspection queries as content. The AI treated supplying the query block itself as authorization to execute the read-only queries against a live environment, although execution authority had varied across prior work orders.

| Field | Sanitized coding sketch |
|---|---|
| Candidate mechanism | Content was interpreted as action authority |
| A6 clarification before action | No |
| Consequence | Read-only catalog metadata was queried; no mutation occurred |
| Assistant construct recommendation | `LIKELY SII` |
| C0 recommendation | `INTENT` |
| C1 recommendation | `AUTHORITY` |
| Source status | The supplied query artifact is corroborated; the authorization chronology is not fully source-verified |
| Researcher status | Pending |

**Why useful for Fan:** This makes explicit that CP can represent not only *what output the user wanted*, but also *whether a supplied object was intended as data or as authorization to act*.

## Example 3 — sequence/definition ambiguity with same-reply disclosure; provisional likely but source-dependent

**Sanitized profile:** A preflight instruction prohibited calling certain functions before their definitions were inspected. During execution, the AI called two platform helper functions and only later inspected their definitions. In the same final handback it disclosed that the order had deviated from the stated sequence.

| Field | Sanitized coding sketch |
|---|---|
| Candidate mechanism | The term defining the prohibited function class was interpreted narrowly enough to allow two platform helpers |
| A6 clarification before action | No |
| A5 primary behavior | Call first → inspect definition later is independently corroborated |
| A8 | Same-reply self-disclosure is corroborated by a preserved assistant handback |
| Consequence | No harmful mutation; procedural deviation documented |
| Assistant construct recommendation | `LIKELY SII`, but source-dependent |
| C0 recommendation | `INTENT` |
| C1 recommendation | `DEFINITION` |
| C9 | `UNVERIFIED` because the primary user-side A3 work-order text is not recovered |
| Researcher status | Pending |

**Why useful for Fan:** It shows why “silent” needs a temporal definition. An interpretation can be silent at the action point even if the AI discloses the decision later in the same reply.

## Example 4 — counter-pattern: disclosure instead of silent resolution

**Sanitized profile:** A requested diff count could reasonably be read in two ways because blank lines changed one convention but not another. Instead of silently choosing, the AI reported both readings and explained which reading matched the requested total. The user accepted the convention and later reused it.

| Field | Sanitized coding sketch |
|---|---|
| Candidate mechanism | Material ambiguity was surfaced/disclosed rather than silently resolved |
| A6/A-resolution style | Disclosure before the ambiguity became consequential |
| Consequence | No rework; convention was adopted |
| Assistant construct recommendation | `CONTROL / COUNTER-PATTERN` |
| Positive SII? | No |
| Research value | Shows a plausible inverse mechanism for future experimental comparison |
| Researcher status | Pending formal control coding |

**Why useful for Fan:** The corpus does not retain only failures. Counter-patterns make it possible to formulate falsifiable comparisons such as silent resolution vs surfaced/disclosed interpretation.

## Example 5 — exclusion example: competence/premise failure rather than intent

**Sanitized profile:** A technical command failed because the execution environment lacked a needed permission/path condition. The original instruction was reasonably clear; the failure came from an incorrect environmental assumption or execution capability rather than a material choice between meanings of what the user wanted.

| Field | Sanitized coding sketch |
|---|---|
| Candidate mechanism | Environment/technical premise failure |
| Alternative user-intent interpretations | No strong material branch identified |
| Assistant construct recommendation | `NO / COMPARISON CLASS` |
| C0 recommendation | `PREMISE` or `COMPETENCE`, depending on the exact record |
| Positive SII? | No on current evidence |
| Research value | Demonstrates the filter preventing “AI made an error” from becoming synonymous with SII |

**Why useful for Fan:** A valid cross-study mapping needs this negative boundary. If DCM's precipitating events mix technical errors, factual hallucinations, and intent misinterpretations, CP categories cannot be applied without separating them first.

## Example-set design principle

The exchange examples intentionally include:

- plausible positive SII;
- a source-dependent positive candidate;
- an authority-specific interpretation case;
- a counter-pattern; and
- an excluded comparison case.

This avoids presenting only dramatic successes for the CP hypothesis and lets Fan test whether DCM's schema could distinguish the same boundaries.

## Release rule

After researcher adjudication, a later version may replace these profiles with a smaller set of researcher-approved examples. If any verbatim quotation is ever shared, it must be separately checked for source verification, confidentiality, and whether exact wording is scientifically necessary.
