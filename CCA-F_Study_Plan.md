# Claude Certified Architect – Foundations (CCA-F)
## Personalised Study Plan

> **Profile:** Intermediate / Advanced (already builds with Claude) | **Goal:** Team & org adoption
> **Availability:** 20.5 hrs/week — Office 1 hr/weekday (theory only) + Home 1.5 hrs/weekday + Sat 4 hrs + Sun 4 hrs
> **Constraints:** Office slot = no API access, no software installs, video/reading only
> **Exam fee status:** Already paid ($125, Anthropic receipt #1227-6121, Jul 1, 2026)
> **Generated:** Tuesday, September 22, 2026 | **Source of truth:** Official Exam Guide v0.2 (last updated June 30, 2026)

---

## 1. Exam Facts

These come from the official exam guide PDF.

| Item | Value |
|---|---|
| Credential | Claude Certified Architect – Foundations |
| Questions | 60 |
| Time limit | 120 minutes (~2 min/question) |
| Format | Multiple choice: 1 correct + 3 plausible distractors. You must answer every question before advancing. |
| Structure | 4 scenarios drawn at random from a bank of 6 |
| Domains | 5 (weights below) |
| Scoring | Scaled 100–1,000. **Pass = 720.** Result is Pass/Fail. |
| Fee | **$125 USD** (already paid) |
| Delivery | Online proctored or at a test center |
| Validity | 12 months from the award date |
| Exam rules (Exam Policy, Jun 25, 2026) | No notes, **no AI tools**, **one monitor only**, no unscheduled breaks, government-issued ID must match your registration |
| Access / registration | https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request |
| Target candidate | Solution architect with 6+ months of hands-on work with the Claude API, Agent SDK, Claude Code and MCP |

> **Corrections to earlier drafts in this workspace:** the fee is $125 (not $99), the time limit is 120 min, there are **30** task statements (not 27), and prompt caching internals and cloud-provider (AWS/GCP) configuration are **explicitly out of scope**.

---

## 2. Exam Domains

| Code | Domain | Weight | Task statements | Focus areas |
|---|---|---|---|---|
| **D1** | Agentic Architecture & Orchestration | **27%** | 1.1–1.7 | Agentic loop on `stop_reason`; hub-and-spoke coordinator; subagent isolated context; `Task` tool + `allowedTools`; programmatic prerequisites and hooks vs prompt guidance; prompt chaining vs dynamic decomposition; `--resume`, `fork_session` |
| **D2** | Tool Design & MCP Integration | **18%** | 2.1–2.5 | Tool descriptions as the selection mechanism; split/rename tools that overlap; `isError` + `errorCategory` + `isRetryable`; 4–5 tools per agent rather than 18; `tool_choice`; `.mcp.json` vs `~/.claude.json`; `${ENV}` expansion; MCP resources; Read/Write/Edit/Bash/Grep/Glob selection |
| **D3** | Claude Code Configuration & Workflows | **20%** | 3.1–3.6 | CLAUDE.md hierarchy (user/project/directory); `@import`; `.claude/rules/` with `paths:` globs; `.claude/commands/`; `.claude/skills/` SKILL.md (`context: fork`, `allowed-tools`, `argument-hint`); plan mode vs direct execution; Explore subagent; iterative refinement; CI with `-p`, `--output-format json`, `--json-schema` |
| **D4** | Prompt Engineering & Structured Output | **20%** | 4.1–4.6 | Explicit criteria instead of "be conservative"; 2–4 targeted few-shot examples; `tool_use` + JSON schema; nullable fields; `"other"` + detail and `"unclear"` enums; validation-retry with error feedback; Message Batches API; independent reviewer instance; multi-pass review |
| **D5** | Context Management & Reliability | **15%** | 5.1–5.6 | Progressive-summarization loss; lost-in-the-middle; "case facts" block; trimming tool output; escalation triggers; structured error propagation; scratchpads, `/compact`, manifests; stratified sampling and field-level confidence; claim-source provenance |

> **Priority:** D1 + D3 + D4 = 67% of the exam. D1 alone is more than a quarter.

---

## 3. Exam Scenarios (4 of these 6 appear on your exam)

| # | Scenario | Primary domains | What to expect |
|---|---|---|---|
| 1 | Customer Support Resolution Agent (Agent SDK + MCP tools `get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`) | D1, D2, D5 | Programmatic prerequisite gates (verify the customer before refund); hooks that block refunds over $500; escalation triggers; structured handoff summaries; multiple customer matches → ask for more identifiers |
| 2 | Code Generation with Claude Code | D3, D5 | Where commands, rules and skills live; plan mode vs direct execution; glob-scoped rules for test files; `/memory`, `/compact` |
| 3 | Multi-Agent Research System | D1, D2, D5 | Task decomposition that is too narrow; parallel `Task` calls; passing findings explicitly to subagents; structured error context; claim-source mappings; conflicting statistics |
| 4 | Developer Productivity with Claude (Agent SDK, built-in tools + MCP) | D2, D3, D1 | Grep vs Glob; Edit fails → Read + Write; incremental codebase exploration; MCP tool descriptions good enough to beat built-in Grep; Explore subagent |
| 5 | Claude Code for CI/CD | D3, D4 | `-p` flag; `--output-format json` + `--json-schema`; an independent reviewer instance rather than self-review; per-file passes plus an integration pass; reducing false positives |
| 6 | Structured Data Extraction | D4, D5 | Nullable schema fields; `tool_choice: "any"` vs forced; semantic vs syntax errors; when retries will not help; Batches API + `custom_id`; confidence routing; stratified sampling |

---

## 4. Course List

Hours are Skilljar estimates (only the API course's 8.1 hrs is official). The "Adj." column applies the Advanced factor of 65%.

### Must-do (4 courses)

| Course | CCA-F domains | Est. time | Adj. | Mode | Rationale |
|---|---|---|---|---|---|
| [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | D1, D2, D4, D5 (80%) | 8.1 h | 5.3 h | Video + code-along | Flagship course. Covers the agent loop, `tool_use`, structured output, `tool_choice`, batches and workflows. |
| [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | D2, D1 (45%) | 2.5 h | 1.6 h | Video + labs | MCP tools vs resources, server/client round-trip, tool descriptions |
| [Introduction to Subagents](https://anthropic.skilljar.com/introduction-to-subagents) | D1, D5 (42%) | 1.5 h | 1.0 h | Video + labs | Isolated context, delegation, Explore subagent, context-window protection |
| [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | D3, D2, D5 (53%) | 2.5 h | 1.6 h | Video + labs | CLAUDE.md, hooks, plan mode, MCP in Claude Code, headless CI |

### Recommended (3 courses)

| Course | CCA-F domains | Est. time | Adj. | Mode | Rationale |
|---|---|---|---|---|---|
| [Claude 101](https://anthropic.skilljar.com/claude-101) | Orientation | 1.0 h | 0.65 h | Video only | Beginner warm-up, but ≤1 hr (Rule 4), and useful when you onboard your team |
| [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | D3 orientation | 1.0 h | 0.65 h | Video only | ≤1 hr orientation before building skills and hooks |
| [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | D3 (task 3.2) | 1.5 h | 1.0 h | Video + labs | Tested directly (SKILL.md frontmatter, skill vs CLAUDE.md). Covers one D3 task statement in depth. |

### Optional (3 courses): do after the exam, when you start rolling this out to your team

| Course | Est. time | Rationale |
|---|---|---|
| [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | 2.5 h | Sampling, notifications and transports. Hosting/deployment of MCP servers is **out of scope**, so exam yield is low. |
| [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | 2–3 h | Beginner course over 1 hr (Rule 4). Low exam yield, but high value for your **team-adoption** goal. |
| [AI Capabilities and Limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations) | 1 h | General background. Model internals and training are out of scope. |

### Skip (7 courses)

| Course | Reason |
|---|---|
| AI Fluency for Educators | Role-specific (Rule 2) |
| AI Fluency for Students | Role-specific (Rule 2) |
| Teaching AI Fluency | Role-specific (Rule 2) |
| AI Fluency for Nonprofits | Role-specific (Rule 2) |
| Claude with Amazon Bedrock | Platform-specific. Cloud-provider configuration is **explicitly out of scope**, so no docs reading is needed either (Rule 3). |
| Claude with Google Cloud's Vertex AI | Same as above |
| Introduction to Claude Cowork | Product is not listed among the tested technologies (Claude Code, Agent SDK, API, MCP) |

### Gap-fill reading (no Skilljar course covers these)

| Topic | Where | Time | Why |
|---|---|---|---|
| Claude **Agent SDK**: agent definitions, hooks, `Task` tool, `allowedTools`, sessions/`fork_session` | docs.claude.com → Agent SDK section | 1.0 h | Appears in 3 of the 6 scenarios. The Skilljar courses teach concepts through the API and Claude Code, not the SDK itself. |
| `tool_choice`, **Message Batches API**, Claude Code **CLI reference** (`-p`, `--output-format`, `--json-schema`, `--resume`) | docs.claude.com → API and Claude Code sections | 1.0 h | Precise facts tested in D2, D3 and D4 |
| **Official exam guide**: all 30 task statements, 12 sample Qs, 4 prep exercises | Your local PDF | 1.5 h | Every exam question maps to one of these task statements |

---

## 5. Course Order Rationale

| # | Item | Why here |
|---|---|---|
| 0 | Official exam guide | Read the task statements first so you watch every course with "what gets tested" in mind. |
| 1 | Claude 101 | Foundation before application. A 40-minute orientation. |
| 2 | Building with the Claude API | Core API before tooling: Claude Code, the Agent SDK and MCP all sit on top of the Messages API and the `tool_use` round-trip. |
| 3 | Official Exercise 3 (extraction) | Hands-on interleave: lock in `tool_use` + JSON schema right after the API structured-output module. |
| 4 | Introduction to MCP | MCP comes after the core API because it formalises the tool round-trip you just built. |
| 5 | Agent SDK + CLI docs | Fills the SDK gap before the hooks/escalation exercise that depends on it. |
| 6 | Official Exercise 1 (multi-tool agent) | Applies API + MCP + SDK hooks together while all three are fresh. |
| 7 | Claude Code 101 | A 40-minute orientation so the Claude Code interface doesn't slow down the component courses. |
| 8 | Introduction to Agent Skills | Components before workflows: a single skill before the full Claude Code configuration layer. |
| 9 | Introduction to Subagents | Second component. Builds the isolated-context mental model needed for D1 and for Claude Code in Action. |
| 10 | Claude Code in Action | The full workflow layer (CLAUDE.md hierarchy, hooks, plan mode, MCP, CI) that ties the components together |
| 11 | Official Exercises 2 & 4 | Capstone labs: a team Claude Code config (D3) and a multi-agent research pipeline (D1/D5) |
| 12 | Scenario drills, then Mock 2 | Application under exam conditions once every component is known |

---

## 6. Weekly Availability & Study Split

```
Slot            | Days    | Hrs/day | Weekly | Hands-on? | Best content type
----------------|---------|---------|--------|-----------|------------------------------------------
Office          | Mon–Fri | 1.0     |  5.0   | NO        | Skilljar videos, docs, exam guide, flashcards
Home evening    | Mon–Fri | 1.5     |  7.5   | YES       | Code-along (60 min) + practice Qs / flashcards (30 min)
Saturday        | Sat     | 4.0     |  4.0   | YES       | Deep labs, TIMED MOCK EXAMS
Sunday          | Sun     | 4.0     |  4.0   | YES       | Deep labs, capstone exercises, mock review
----------------|---------|---------|--------|-----------|------------------------------------------
TOTAL                               | 20.5 hrs/week
  Theory-only (office)              |  5.0 hrs
  Hands-on capable (home + weekend) | 15.5 hrs
  Long uninterrupted blocks         |  8.0 hrs (Sat + Sun), used for mocks and capstones
```

**Home evening split (1.5 hrs):** the first 60 minutes go to the main hands-on task in the schedule. The last 30 minutes (marked **+30** in Section 8) go to retrieval practice: domain practice questions, flashcards, or finishing a lab that ran over.

**Treat the office constraint as a feature.** No API access and no installs means the office hour is used only for concepts (videos, docs, the exam guide). All coding happens at home, where Claude Code, Python and your API key are available. Never put an API key or install tooling on the office machine.

---

## 7. Total Hours Calculation

```
Content hours (Advanced: 65% of course hours)
  Must-do courses        14.6 h nominal
  Recommended courses     3.5 h nominal
                         ------
                         18.1 h x 0.65 ............... 11.8 h
  Gap-fill reading (not discounted)
    Official exam guide ............................... 1.5 h
    Agent SDK / tool_choice / Batches / CLI docs ...... 2.0 h
  Official prep exercises 1-4 (hands-on) .............. 8.0 h
                                                      -------
Content subtotal ..................................... 23.3 h
Review hours (~13% of content) ........................ 3.0 h
Mock Exam 1 (120 min + review) ........................ 3.0 h
Mock Exam 2 (120 min + review) ........................ 3.0 h
Scenario work (6 scenarios) ........................... 4.0 h
Buffer (0.5 week x 20.5 h) ........................... 10.3 h
─────────────────────────────────────────────────────────────
TOTAL HOURS NEEDED ................................... 46.6 h

Weekly capacity ...................................... 20.5 h
Weeks needed (46.6 / 20.5) ........................... 2.27 weeks  ->  2.5 calendar weeks
  (Mock 1 must fall on the Week 2 Saturday and Mock 2 on the
   final-week Saturday, so the calendar can't be shorter than 2.5 weeks)

Hours available, Tue Sep 22 -> Sun Oct 11:
  Day 0 (Sep 22 eve)                      1.5 h
  Week 1 (Wed-Fri 3 x 2.5 + Sat/Sun 8)   15.5 h
  Week 2 (full week)                     20.5 h
  Week 3 (Mon-Fri 12.5 + Sat 4 + Sun 0.5) 17.0 h
                                         ------
                                         54.5 h  (fits, ~8 h spare on top of the buffer)

Spare ~8 h is used for the "+30" practice blocks every evening
(~6.5 h of extra retrieval practice) plus a lighter Friday before Mock 2.
```

---

## 8. Day-by-Day Schedule

All dates were checked with Python `datetime`.

### Day 0: Tuesday, Sep 22, 2026 (today, home evening, ~1.5 hrs)

| Date | Day# | Theory slot | Hands-on slot (home) |
|---|---|---|---|
| Tue Sep 22 | 0 | (office slot has passed) | **Immediate Actions** (Section 13): check exam access/booking in Skilljar, get an API key, create `.env`, `pip install -r requirements.txt`, install the Claude Code CLI **on your home PC**, make a first API call. **+30:** enroll in all 7 courses. |

### Week 1: Wed Sep 23 – Sun Sep 27: Foundation, API core, MCP

| Date | Day# | Theory slot (Office, 1 hr, no API) | Hands-on slot (Home 1.5 hrs / weekend block) |
|---|---|---|---|
| Wed Sep 23 | 1 | Claude 101 (40 min) + exam guide: intro, 6 scenarios, domain list (20 min) | API course: accessing the API, first requests, multi-turn messages (code-along). **+30:** start `flashcards.md` with one card per D1 task statement. |
| Thu Sep 24 | 2 | Exam guide: **D1 + D2 task statements** (1.1–2.5); write one-line notes per statement | API course: prompt evaluation + prompt engineering modules. **+30:** add D2 flashcards; redo sample Qs 1–3 from memory. |
| Fri Sep 25 | 3 | Exam guide: **D3–D5 task statements**, all 12 sample Qs, out-of-scope list | API course: **tool use**. Build the `stop_reason` loop (`tool_use` → run tool → append `tool_result` → repeat until `end_turn`). **+30:** add `tool_choice` `auto`/`any`/forced to the loop and compare. **Check exam access; book the exam slot today if approved.** |
| **Sat Sep 26** | **4** | 4-hr block (home) | API course: structured output via tools, `tool_choice`, batches, extended thinking (skim RAG/embeddings, which are out of scope) → **Official Exercise 3, part A**: extraction tool with required/optional/nullable fields, `"other"` + detail enum, validation-retry loop |
| **Sun Sep 27** | **5** | 4-hr block (home) | API course: MCP + agents & workflows modules (**finish the API course**) → **Intro to MCP**: build a server (tools, resources, prompts), test in MCP Inspector. **Latest day to book the exam.** |

### Week 2: Mon Sep 28 – Sun Oct 4: SDK, Claude Code track, Mock 1

| Date | Day# | Theory slot (Office, 1 hr, no API) | Hands-on slot (Home 1.5 hrs / weekend block) |
|---|---|---|---|
| Mon Sep 28 | 6 | Docs: **Agent SDK**: agent definitions, `Task` tool, `allowedTools`, hooks (PostToolUse, tool-call interception), sessions, `fork_session` | Intro to MCP: finish the client, add a resource that exposes a content catalog (**MCP course done**). **+30:** 10 practice Qs on D2. |
| Tue Sep 29 | 7 | Docs: `tool_choice` (`auto` / `any` / forced), Message Batches API (50% cost, 24 h, `custom_id`, no multi-turn tools), Claude Code CLI (`-p`, `--output-format json`, `--json-schema`, `--resume`) | **Official Exercise 1, part A**: 3–4 MCP tools (two deliberately similar) with differentiated descriptions; agentic loop; structured errors (`errorCategory`, `isRetryable`). **+30:** Exercise 3, part B: submit a small Message Batch, correlate by `custom_id`. |
| Wed Sep 30 | 8 | Claude Code 101 (40 min) + Agent Skills videos (start) | **Exercise 1, part B**: interception hook that blocks refunds over $500 and escalates; structured handoff summary; multi-concern message test. **+30:** 10 practice Qs on D1. |
| Thu Oct 1 | 9 | Agent Skills videos (finish) + Subagents videos | Agent Skills hands-on: `.claude/skills/<name>/SKILL.md` with `context: fork`, `allowed-tools`, `argument-hint`; a project slash command in `.claude/commands/`. **+30:** personal variant in `~/.claude/skills/` + 10 practice Qs on D3. |
| Fri Oct 2 | 10 | Claude Code in Action videos: CLAUDE.md hierarchy, `@import`, `.claude/rules/`, plan mode, hooks, CI | Subagents hands-on: custom subagent + Explore subagent; show that the subagent does **not** inherit parent context. **+30:** flashcard pass over all domains before Mock 1. |
| **Sat Oct 3** | **11** | 4-hr block (home) | **MOCK EXAM 1**: 60 Q, **120 min timed**, no notes, one monitor (2 h) → review: tag every miss by domain and task statement (1 h) → Claude Code in Action hands-on: hooks + headless `-p` run (1 h, **Claude Code in Action done**) |
| **Sun Oct 4** | **12** | 4-hr block (home) | **Official Exercise 2** (2 h): project CLAUDE.md, `.claude/rules/` with `paths:` globs, forked skill, `.mcp.json` with `${GITHUB_TOKEN}`, personal server in `~/.claude.json`, plan mode vs direct on 3 tasks → **Exercise 4, part A** (2 h): coordinator + 2 subagents, `"Task"` in `allowedTools`, parallel `Task` calls in one response |

### Week 3: Mon Oct 5 – Sun Oct 11: Remediation, scenarios, Mock 2

| Date | Day# | Theory slot (Office, 1 hr, no API) | Hands-on slot (Home 1.5 hrs / weekend block) |
|---|---|---|---|
| Mon Oct 5 | 13 | Re-study **weakest domain #1** from Mock 1 (guide task statements + your notes) | **Exercise 4, part B**: claim-source mappings with dates; simulated subagent timeout → structured error context; conflicting-statistics handling with coverage annotations. **+30:** 10 practice Qs on weakest domain #1. |
| Tue Oct 6 | 14 | **Scenarios 1 & 3** (support agent, multi-agent research): walk through every mapped task statement; redo sample Qs 1–3, 7–9 | Practice set: **30 Q** on D1 + D5, timed at 2 min/Q (60 min); review each miss (30 min) |
| Wed Oct 7 | 15 | **Scenarios 2 & 4** (code gen, dev productivity): redo sample Qs 4–6; built-in tool selection rules | Practice set: **30 Q** on D3 + D2 (60 min); review (30 min) |
| Thu Oct 8 | 16 | **Scenarios 5 & 6** (CI, extraction): redo sample Qs 10–12; sync vs batch decisions | Practice set: **30 Q** on D4 + **weakest domain #2** (60 min); review (30 min) |
| Fri Oct 9 | 17 | Traps & anti-patterns sweep (Section 11) + out-of-scope list | Confirm the booking; run the proctoring **system check on your home PC** (not the locked-down office machine); flashcards. **Light evening, use only 1 hr of the 1.5.** Stop by 9 pm. |
| **Sat Oct 10** | **18** | 4-hr block (home) | **MOCK EXAM 2**: 60 Q, 120 min timed, exam conditions (2 h) → score by domain → apply the **decision tree** (Section 14) → targeted fix of the two weakest task statements (2 h) |
| **Sun Oct 11** | **19** | **REST DAY** | 30-min flashcard pass only. No new content. Sleep early. |
| **Mon Oct 12** | **20** | **EXAM DAY** | Take the exam at home in the morning (take PTO or work from home). Keep your ID ready and your desk clear. |

---

## 9. Exam Date

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   RECOMMENDED EXAM DATE:   Monday, October 12, 2026          │
│   BACKUP DATE:             Tuesday, October 13, 2026         │
│                                                              │
│   Mock Exam 2:             Saturday, October 10, 2026        │
│   Rest day:                Sunday, October 11, 2026          │
│                                                              │
│   RESCHEDULE TRIGGER (from Mock 2):                          │
│     overall < 72%                                            │
│     OR < 70% in D1 (27%) OR in D3/D4 (20% each)              │
│   RESCHEDULED DATE:        Monday, October 19, 2026          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Why October 12:**
- 46.6 h ÷ 20.5 h/week = 2.27 weeks of study. Mock 1 has to fall on the Week 2 Saturday (Oct 3) and Mock 2 on a later Saturday, so the earliest possible Mock 2 is Oct 10. The first weekday after that plus a rest day is Mon Oct 12.
- The extra 30 minutes per evening doesn't move the exam earlier. It adds about 8 h of retrieval practice and slack, which makes a pass at 720+ more likely.
- It is 2 days after Mock 2 (Sat Oct 10) and 1 day after the rest day (Sun Oct 11).
- A weekday lets you use home online proctoring. The office machine can't install proctoring software, so book a **morning slot and work from home or take PTO**.
- Oct 12, 2026 is the US Columbus Day / Indigenous Peoples' Day holiday. Online proctoring is normally unaffected, but if you choose a test center, check that it is open.
- Check the reschedule/cancellation window when you book. The Exam Policy PDF does not state one, so confirm it on the booking platform, and keep it in mind for the Oct 19 fallback.

---

## 10. Hands-On Labs Checklist

These follow the four official preparation exercises. The `labs/` folder is currently empty, so build each lab under `labs/`.

**Exercise 1: Multi-Tool Agent with Escalation (D1, D2, D5)**
- [ ] 3–4 MCP tools with differentiated descriptions (at least 2 deliberately similar)
- [ ] Agentic loop driven only by `stop_reason` (`tool_use` → continue, `end_turn` → stop); no text-parsing and no iteration cap as the primary stop
- [ ] Structured errors: `isError`, `errorCategory` (transient/validation/business/permission), `isRetryable`, a human-readable message
- [ ] Interception hook that blocks `process_refund` over $500 and redirects to `escalate_to_human`
- [ ] Programmatic prerequisite: `process_refund` blocked until `get_customer` returns a verified ID
- [ ] Multi-concern request is decomposed, investigated and resolved in one reply, with a structured handoff summary on escalation

**Exercise 2: Claude Code Team Workflow (D3, D2)**
- [ ] Project `CLAUDE.md` + a directory-level `CLAUDE.md` + `@import` of a standards file; verify with `/memory`
- [ ] `.claude/rules/testing.md` with `paths: ["**/*.test.*"]` that loads only when a matching file is edited
- [ ] Project slash command in `.claude/commands/` and a personal one in `~/.claude/commands/`
- [ ] Skill in `.claude/skills/` with `context: fork`, `allowed-tools`, `argument-hint`
- [ ] `.mcp.json` with `${GITHUB_TOKEN}` expansion + a personal server in `~/.claude.json`; both visible at the same time
- [ ] Plan mode vs direct execution tried on a 1-file fix, a multi-file migration, and a feature with several approaches
- [ ] Headless run: `claude -p "..." --output-format json --json-schema <schema>`

**Exercise 3: Structured Data Extraction Pipeline (D4, D5)**
- [ ] Extraction tool schema with required, optional/nullable, `"other"` + detail, and `"unclear"` values; absent fields come back `null`, not invented
- [ ] `tool_choice: "any"` vs forced `{"type":"tool","name":"extract_metadata"}` compared
- [ ] Validation-retry loop that sends the document + failed output + the specific error; log which errors retries fix and which they can't
- [ ] Few-shot examples for varied document formats
- [ ] Message Batches run with `custom_id` correlation; resubmit only the failures
- [ ] Field-level confidence scores → route low-confidence items to human review

**Exercise 4: Multi-Agent Research Pipeline (D1, D2, D5)**
- [ ] Coordinator with `"Task"` in `allowedTools`, delegating to 2 or more subagents with findings passed **explicitly** in their prompts
- [ ] Parallel `Task` calls in one coordinator response; latency compared with sequential calls
- [ ] Subagent output with claim, excerpt, source URL/doc, and publication date; attribution preserved through synthesis
- [ ] Simulated timeout → structured error context (type, query, partial results, alternatives); report annotated with coverage gaps
- [ ] Conflicting statistics from two sources are both kept, attributed, and marked as contested

---

## 11. High-Yield Facts to Memorize

**D1: Agentic architecture**
- Loop: continue while `stop_reason == "tool_use"`, stop on `"end_turn"`. Anti-patterns: parsing natural language to decide when to stop, iteration caps as the main stop, treating "has text" as done.
- Subagents **do not inherit** the coordinator's history. Pass complete findings explicitly in the prompt.
- A coordinator needs `"Task"` in `allowedTools`. For parallelism, emit **multiple `Task` calls in one response**.
- All subagent communication goes through the coordinator (hub-and-spoke).
- Coordinator prompts should state **goals and quality criteria**, not step-by-step procedures.
- Deterministic compliance (identity before refund, refund caps) needs **hooks or programmatic gates**. Prompt instructions alone have a non-zero failure rate.
- Use prompt chaining for predictable multi-aspect reviews and dynamic decomposition for open-ended investigation.
- Use `--resume <name>` when prior context is still valid. Start a new session with an injected summary when tool results are stale. Use `fork_session` for divergent approaches.

**D2: Tools & MCP**
- The tool **description** is the main thing the model uses to pick a tool. The first fix for misrouting is a better description (inputs, examples, edge cases, when to use this tool vs the similar one).
- Giving an agent 18 tools instead of 4–5 hurts selection reliability. Scope tools per role, and give a narrow cross-role tool (e.g. `verify_fact`) for high-frequency needs.
- `tool_choice`: `"auto"` means the model may reply with text; `"any"` means it must call some tool; `{"type":"tool","name":...}` forces a specific tool.
- Distinguish **access failures** from **valid empty results**. Never return failure dressed up as success.
- `.mcp.json` is project scope and shared through version control. `~/.claude.json` is user scope and personal. `${VAR}` expansion keeps secrets out of the repo. Tools from all servers are available together.
- Use MCP **resources** for content catalogs, to cut down on exploratory tool calls. Prefer community servers (e.g. Jira) over custom ones for standard integrations.
- Grep searches file **contents**; Glob matches file **paths**. If Edit can't find unique anchor text, fall back to Read + Write.

**D3: Claude Code**
- Hierarchy: `~/.claude/CLAUDE.md` is user-only and **not shared**; project `CLAUDE.md` or `.claude/CLAUDE.md`; subdirectory `CLAUDE.md`. `/memory` shows which files are loaded.
- `.claude/rules/*.md` with a `paths:` glob loads only when matching files are edited. Prefer this over directory CLAUDE.md files for conventions that span directories, such as tests.
- `.claude/commands/` = team commands; `~/.claude/commands/` = personal. There is **no** `.claude/config.json` commands array.
- Skill frontmatter: `context: fork` (isolated sub-agent), `allowed-tools`, `argument-hint`. Skills are loaded on demand; CLAUDE.md is always loaded.
- Plan mode is for architectural, multi-file work with several valid approaches. Use direct execution for clear, single-file fixes.
- CI: `-p` / `--print` (there is no `CLAUDE_HEADLESS` and no `--batch`), plus `--output-format json` and `--json-schema`. On re-review, include prior findings and report only new or unaddressed issues.
- Iterative refinement: give 2–3 input/output examples, use test-driven iteration, use the interview pattern, and send interacting issues together in one message.

**D4: Prompts & structured output**
- Explicit categorical criteria beat "be conservative" or "high-confidence only".
- 2–4 targeted few-shot examples that show the reasoning for ambiguous cases.
- `tool_use` + a strict schema removes **syntax** errors, not **semantic** ones (e.g. totals that don't sum).
- Make a field nullable when the source may lack it, so the model doesn't invent a value.
- Retries fix format and structure errors. They **cannot** recover information that isn't in the source.
- Batches API: 50% cheaper, up to 24 h, **no latency SLA**, **no multi-turn tool calling**, uses `custom_id`. Use batches for overnight jobs, never for blocking pre-merge checks.
- An independent review instance beats self-review. Split large PRs into per-file passes plus a cross-file integration pass. A bigger context window doesn't fix attention dilution.

**D5: Context & reliability**
- Keep a **case facts** block (amounts, dates, IDs, statuses) outside the summarized history. Progressive summarization loses the numbers.
- Lost in the middle: put key findings **first** and use section headers.
- Trim verbose tool output to the relevant fields before it builds up in context.
- Escalate when: the customer explicitly asks (**honor it immediately**), the policy has a gap or is ambiguous, or no progress is possible. Sentiment and self-reported confidence are **unreliable** triggers.
- Multiple customer matches → ask for more identifiers. Never pick one heuristically.
- Subagents should recover from transient errors locally and propagate only what they can't resolve, with partial results.
- Long sessions: use scratchpad files, `/compact`, Explore subagents, and state manifests for crash recovery.
- A 97% aggregate accuracy can hide weak segments. Use stratified sampling and check accuracy by document type and field before automating.
- Provenance: keep claim-source mappings, record publication dates, annotate conflicts, and render each content type in a suitable format.

**Out of scope (don't spend time here):** fine-tuning, auth/billing, MCP hosting/deployment, model internals/RLHF, embeddings/vector DBs, computer use, vision, streaming/SSE, rate limits/pricing, OAuth, AWS/GCP/Azure configuration, benchmarks, **prompt caching details**, tokenization.

---

## 12. Free Practice Resources

| Resource | What | Link | Use for |
|---|---|---|---|
| **Official exam guide** sample questions | 12 official Qs with explanations | Local PDF | Calibrating question style (redo them in Week 3) |
| **Official practice test** | The guide says its sample Qs are "drawn from the practice test". Check your Skilljar dashboard for access. | Skilljar (after access approval) | **Mock 2** if available (best fidelity) |
| haytamAroui/Claude-Certified-Architect | 120 community practice Qs + 2 × 60-Q mocks (unofficial; it lists 27 task statements, while the official guide has 30) | https://github.com/haytamAroui/Claude-Certified-Architect | **Mock 1** and daily practice sets |
| Anthropic Cookbook | Official code examples (tool use, extraction, agents) | https://github.com/anthropics/anthropic-cookbook | Starter code for Exercises 1, 3, 4 |
| ccaf-exam.guide | Community study sections by domain | https://ccaf-exam.guide | Extra review (unofficial) |
| claudearchitectcertification.com | Community domain breakdown + practice | https://claudearchitectcertification.com/exam-guide | Extra review (unofficial) |
| Anthropic docs | Agent SDK, Claude Code, API reference | https://docs.claude.com | Gap-fill reading, days 6–7 |

> Use only legitimately published practice material. The Exam Policy bans using unauthorized copies of real exam content.

---

## 13. Immediate Actions (Day 0: Tuesday, Sep 22, 2026)

1. **Confirm exam access.** The fee is already paid (Jul 1). Log in to Skilljar and check whether your CCA-F access or booking link is active. If you still need to submit the access request, do it **today**, allowing 1–3 business days for processing (i.e. by **Fri Sep 25**): https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request
2. **Book the exam for Monday, Oct 12, 2026** (morning, online proctored from home) as soon as access is confirmed. **Book by Sun Sep 27 at the latest.** Note the reschedule window when you book.
3. **Get an API key** (home PC only): https://console.anthropic.com/settings/keys
4. **Set up the workspace** on your home PC:
   ```powershell
   cd C:\repo\Anthropic
   Copy-Item .env.example .env      # then add ANTHROPIC_API_KEY
   pip install -r requirements.txt
   ```
5. **Install the Claude Code CLI** on your home PC (it's needed for Exercise 2 and the Skills, Subagents and Claude Code in Action labs).
6. **Enroll** in all 7 Must-do and Recommended courses on https://anthropic.skilljar.com/ so the office slot can go straight to videos tomorrow.
7. **Block your calendar**: Mock 1 on Sat Oct 3, Mock 2 on Sat Oct 10, rest on Sun Oct 11, and PTO or WFH on the morning of Mon Oct 12.

---

## 14. Mock Exam Decision Tree

```
MOCK EXAM 1 (Sat Oct 3): diagnostic only, no go/no-go decision
│
├─ Tag every miss by domain AND task statement
├─ Weakest domain #1 -> office slot Mon Oct 5
└─ Weakest domain #2 -> home slot Thu Oct 8

MOCK EXAM 2 (Sat Oct 10): the go/no-go decision
│
├─ >= 80% overall AND every domain >= 70%
│    └─ SIT the exam Mon Oct 12 as planned. Rest on Sunday.
│
├─ 72-79% overall AND D1, D3, D4 all >= 70%
│    └─ Fix the two weakest task statements Sat afternoon.
│       30-min flashcards Sun. SIT Mon Oct 12.
│
├─ Borderline (72-74%) and you feel unwell or unready Sunday
│    └─ Move to BACKUP: Tue Oct 13 (use Mon evening for one weak domain)
│
└─ < 72% overall  OR  < 70% in D1 (27%)  OR  < 70% in D3 / D4 (20% each)
     └─ RESCHEDULE to Mon Oct 19, 2026
        Week of Oct 12: weak-domain re-study + redo the related official exercise
        Sat Oct 17: third timed mock (re-shuffled community set)
        Sun Oct 18: rest
```

---

*Workspace:* `C:\repo\Anthropic\`
*Source of truth:* `Claude Certified Architect - Foundations - Exam Guide.pdf` (v0.2, June 30, 2026) and `Anthropic Certification Exam Policy.pdf` (June 25, 2026), in `OneDrive - Dell Technologies\Dell\Training\EdAssist\Claude Architect\`. If this plan disagrees with those PDFs, the PDFs win.
*Last updated:* Tuesday, September 22, 2026
