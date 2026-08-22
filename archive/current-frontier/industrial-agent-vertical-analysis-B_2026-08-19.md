**The strongest structural fit for Collaboration Protocol (CP) is not in generic “AI agents for industry.” It is in live, multi-variable process-control actions where a human-authorized move is still executed against a changed physical state.**

Saudi Arabia already has real deployments of exactly this class of agent. The clearest current example is the multi-agent reinforcement-learning control system (Yokogawa FKDPP agents) commissioned at Aramco’s Fadhili Gas Plant for Acid Gas Removal (AGR). Those agents directly manipulate process parameters (amine circulation rates, temperatures, etc.) inside a live DCS (CENTUM VP) while the plant’s existing safety interlocks remain active. Similar patterns exist in Aramco’s Master Gas System digital twins, emerging Ma’aden autonomous-haulage work, and desalination process-optimization digital twins.

Below is the full analysis required by the brief.

### Part 9 — 12 Candidate INDUSTRY + AGENT Combinations (scored /140)

Scores use the full 1–10 range. Totals are raw sums. No inflation.

| Rank | Candidate (Industry + Specific Agent Role) | A | B | C | D | E | F | G | H | I | J | K | L | M | N | Total |
|------|--------------------------------------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|-------|
| 1 | Gas-plant Acid Gas Removal (AGR) autonomous process-control agent (amine circulation, temperature, flow setpoints) | 10 | 9 | 9 | 10 | 9 | 10 | 9 | 8 | 9 | 10 | 9 | 9 | 9 | 9 | **129** |
| 2 | Master Gas System network real-time optimization / pressure-routing agent | 9 | 9 | 8 | 9 | 8 | 9 | 8 | 8 | 8 | 10 | 8 | 8 | 8 | 8 | **118** |
| 3 | Autonomous mining haul-truck dispatch & route-assignment agent (Ma’aden-style) | 9 | 8 | 9 | 8 | 8 | 9 | 8 | 7 | 8 | 9 | 8 | 8 | 8 | 8 | **115** |
| 4 | Seawater reverse-osmosis (SWRO) train pressure / recovery-setpoint optimization agent | 8 | 8 | 7 | 9 | 8 | 8 | 8 | 7 | 8 | 9 | 7 | 8 | 7 | 8 | **110** |
| 5 | Refinery CCR / Platformer unit APC move agent (feedstock blend or severity setpoint) | 8 | 7 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 9 | 8 | 8 | 7 | 8 | **107** |
| 6 | Upstream well choke-valve / production-setpoint change agent | 9 | 8 | 7 | 8 | 7 | 8 | 7 | 7 | 7 | 10 | 7 | 7 | 7 | 7 | **106** |
| 7 | Petrochemical reactor batch-recipe parameter adjustment agent (SABIC-style) | 8 | 6 | 8 | 8 | 7 | 7 | 7 | 7 | 7 | 8 | 6 | 7 | 6 | 7 | **99** |
| 8 | Power-grid generation dispatch instruction agent (SEC) | 9 | 8 | 8 | 7 | 7 | 8 | 6 | 6 | 7 | 9 | 6 | 6 | 6 | 6 | **99** |
| 9 | Pipeline sectional isolation / pressure-management valve agent | 9 | 6 | 7 | 9 | 8 | 8 | 7 | 6 | 7 | 9 | 5 | 6 | 7 | 6 | **100** |
| 10 | Construction tower-crane lift-sequence & exclusion-zone coordination agent (NEOM-scale) | 8 | 7 | 8 | 7 | 7 | 7 | 6 | 6 | 6 | 8 | 5 | 6 | 5 | 6 | **92** |
| 11 | Water-distribution network pressure-zone management agent | 7 | 7 | 6 | 7 | 6 | 6 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 6 | **88** |
| 12 | Airport ground-movement / fueling coordination agent | 7 | 6 | 7 | 6 | 5 | 6 | 5 | 5 | 6 | 6 | 4 | 5 | 4 | 5 | **77** |

### Part 10 — Elimination Round

All candidates below 110 were eliminated. Primary reasons:

- Petrochemical batch, power-grid dispatch, pipeline isolation, construction crane, water network, airport: either context change is slower, final-confirmation + DCS interlocks already cover most of the residual risk, or Saudi competitor density / benchmark realism is materially weaker.
- Upstream choke and refinery APC remain close but lose on the combination of multi-agent coordination + continuous multi-variable state change that AGR and Master Gas exhibit.

**Top 5 after elimination**  
1. AGR process-control agent (129)  
2. Master Gas System network agent (118)  
3. Mining haul-truck dispatch agent (115)  
4. SWRO setpoint agent (110)  
5. Refinery APC move agent (107)

### Red-Team Review of Top 5

**AGR agent**  
Strongest counter: “CENTUM VP + ProSafe-RS already provide hard interlocks and the AI agents were trained inside a high-fidelity simulator before live deployment. Ordinary state locking + final operator confirmation already solves the problem.”  
Rebuttal that survives: the interlocks protect equipment limits; they do not re-validate the *human-authorized intent* against the live multi-variable context (feed composition, amine strength, ambient temperature, downstream capacity) that existed at the moment of approval. A stale but still “safe” move can still be wrong relative to the original authorization. Score remains 129.

**Master Gas System**  
Counter: “Central planners already run digital twins; the system is advisory.”  
Rebuttal: Aramco papers describe online rigorous optimization PDTs that advise operational changes when the network state changes. Once those advices become executable agent actions, the same intent-vs-live-state gap appears. Score held.

**Mining haul dispatch**  
Counter: “Fleet-management systems already re-plan continuously; geofencing and collision avoidance are hard.”  
Rebuttal: continuous re-planning is not the same as re-validating a *human-authorized specific assignment* (truck X to face Y under current geotechnical and traffic state). Score held at 115.

**SWRO and Refinery APC**  
Both suffer more from the “ordinary industrial control already solves most of it” critique. Scores adjusted downward slightly in the ranking order above.

### Part 11 — Deep Dive on Final Top 3

#### 1. Autonomous AGR Process-Control Agent (Fadhili-style)

**Specific agent**  
A multi-agent RL controller that continuously adjusts amine circulation rate, lean-amine temperature, and related setpoints inside an Acid Gas Removal unit to minimize chemical and energy use while meeting H₂S/CO₂ specifications.

**Industry & Saudi relevance**  
Gas processing is core to Aramco’s Master Gas System and to the Kingdom’s energy exports and domestic power/desalination feedstock. Fadhili processes ~2.5 Bscf/d. The Yokogawa FKDPP agents are already live and have delivered 10–15 % amine/steam reduction and ~5 % power reduction.

**Current competitors**  
- Verified: Yokogawa FKDPP multi-agent autonomous control agents integrated with CENTUM VP at Fadhili (live since late 2025).  
- Verified: Emerson Aspen Hybrid Models for related refining/gas planning.  
- Marketing/inference: broader Aramco “agentic AI” statements and digital-twin work.

**Live workflow (T0–T9)**  
T0 Human declares context (unit online, target product quality, max amine consumption budget).  
T1 Agent observes live state (>30 process variables).  
T2 Agent proposes specific setpoint trajectory.  
T3 Human explicitly approves the exact trajectory (or a bounded envelope).  
T4–T5 Ambient temperature shifts, inlet gas composition changes, or a downstream compressor trips.  
T6 Candidate control move reaches the DCS write boundary.  
T7 Conventional agent (or DCS) may still execute if hard interlocks are satisfied.  
T8 CP Guardian re-evaluates Intent + Context + Agent permissions + Nodes + Friction against live state.  
T9 ALLOW / REFUSE / CLARIFY.

**CP state model**  
- Context: bounded operational envelope of the AGR unit (feed quality limits, product quality limits, equipment health).  
- Intent: explicit human-authorized setpoint trajectory or optimization objective under the declared context.  
- Agent: the specific RL control agent (or agent ensemble) with declared write permissions.  
- Node/constraint: hard process limits (max amine strength, max temperature, min H₂S removal, max steam).  
- Action: the concrete DCS write (e.g., “set amine circulation to 1 240 m³/h”).  
- Friction: any unresolved change that invalidates the original context (composition shift beyond envelope, equipment status change, authority revocation).

**Killer failure (after explicit approval)**  
Human approves a higher amine circulation rate based on current lean-amine strength and inlet H₂S. Between approval and write, a sudden feed-composition change or regenerator upset degrades lean-amine quality. The approved numerical setpoint is still inside hard equipment limits, yet executing it now violates the original Intent under the new Context. Final confirmation cannot see the change; ordinary RBAC only checks role; hard interlocks only check absolute limits.

**Why normal agents / RBAC / final confirmation / rule engines fail**  
- Normal agents treat the approval as still valid.  
- RBAC authorizes the *agent*, not the continued validity of the *intent under live context*.  
- Final confirmation is a point-in-time linguistic act; it does not re-bind to live process state.  
- Ordinary rule engines or interlocks enforce absolute safety limits; they do not reconstruct human authorization provenance across a changing multi-variable state space.

**Guardian ranking (most important PE rules)**  
PE-9 (context constraints), PE-3 (intent–action match), PE-10 (unresolved friction), PE-4 (context open), PE-8 (permissions), then the rest.

**Strategic friction moments**  
1. Live composition or equipment state leaves the authorized envelope.  
2. Agent authority is revoked or scope reduced (e.g., emergency mode).  
3. Downstream capacity constraint appears.  
Harmful friction: interrupting a stable, still-valid optimization trajectory for noise.

**Primary benchmark**  
“Authorized Process-Setpoint Integrity” — percentage of executed DCS writes that remain consistent with the verified Intent + Context that existed at the moment of human commitment, measured against live state at the execution boundary.

**Adversarial benchmark (10 tests)**  
2 normal correct executions; 2 stale-state (composition/ambient change after approval); 2 authority/permission (agent or role revoked); 2 context/constraint (new Node violation); 1 multi-agent handoff corruption; 1 partial-execution recovery.

**Testbed**  
High-fidelity plant simulator of the type Yokogawa already used for training (digital twin of AGR unit). Inject controlled state changes after approval. No live plant risk.

**Competitor testing**  
Controlled architecture benchmark: same simulator, same scenarios, CP-governed agent vs. the existing FKDPP agents (or a re-implemented conventional agent). Black-box: observe live Fadhili-style behavior only through permitted interfaces.

**Success / falsification**  
Success: CP blocks >X % of post-approval stale or authority-violating moves that the conventional agent executes, while adding negligible friction on still-valid moves. Falsification: ordinary interlocks + final confirmation already catch essentially all of them.

**Commercial moat**  
A governance layer that sits between human intent and any industrial AI control write, independent of the underlying RL or optimization algorithm. Hard to copy without adopting the same explicit Intent–Context–Agent–Node state machine.

#### 2. Master Gas System Network Real-Time Optimization Agent

Similar structure, but the unit of action is network-level pressure or routing setpoints across the national Master Gas System. Context changes (demand, compressor status, field production) are frequent and system-wide. Consequence of mismatch is large (gas allocation, power generation, desalination feedstock). Competitors are Aramco’s own online rigorous optimization PDTs. Guardian necessity is high because authority is often central-planner authority that can be overtaken by local plant state.

#### 3. Autonomous Mining Haul-Truck Dispatch & Route Agent

Unit of action is assignment of a specific truck to a specific face/route under current geotechnical, traffic, and weather state. Ma’aden is actively evaluating autonomous haulage systems (Hexagon, CiDi MetaMine interest). Context changes rapidly (slope stability, traffic congestion, equipment health). Consequence is safety + productivity. Final confirmation of a dispatch plan does not survive a subsequent geotechnical alert or traffic lock.

### Part 12 — Final Decision

**IF I HAD TO BET THE CP PROGRAM ON ONE VERTICAL, I WOULD CHOOSE: Autonomous Acid Gas Removal (AGR) process-control agent (Fadhili-style multi-agent RL control of amine circulation, temperature and related setpoints).**

It beats every other candidate on the exact combination the brief demands:

- CP architectural fit: continuous multi-variable state, explicit human-authorized trajectories, multi-agent coordination, live constraints that are physical rather than textual.  
- Severity of authority failure: a wrong but “safe” move still wastes millions in chemicals/energy or risks product quality.  
- Dynamic context: ambient, feed composition, downstream capacity change on the order of minutes.  
- Permission complexity: different agents (observer, optimizer, executor) with sharply different write scopes; emergency mode changes authority.  
- Constraint sensitivity: PE-9 is mission-critical.  
- Guardian necessity: re-evaluation at the DCS write boundary is the only place that can catch post-approval state drift.  
- Benchmark quality: high-fidelity simulators already exist; observable is an actual process write.  
- Saudi-market importance: live at Aramco, core to national gas infrastructure, Vision 2030 industrial AI priority.  
- Defensibility against ordinary workflow/RBAC: hard interlocks and RBAC do not reconstruct human authorization provenance; final confirmation is a linguistic snapshot.  
- Scientific evidence path: controlled simulator experiments that can be published.  
- Commercial path: a governance layer that can sit in front of any future industrial AI control agent at Aramco, SABIC, SWCC, etc.

**Single biggest reason the recommendation could be wrong**  
Industrial control systems already treat the DCS write boundary as a hard safety gate with sophisticated interlocks and model-predictive constraints. If those existing mechanisms, plus a simple “re-check live state before write” policy, already eliminate essentially all of the residual authorization-integrity failures that CP targets, then CP’s additional state machine adds complexity without proportional value. The only way to know is the adversarial benchmark on a high-fidelity simulator against the real Yokogawa-style agents.
