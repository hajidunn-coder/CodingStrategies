# Claude Code workflow and skills: what to consider

Theme: `claude-code-workflow-and-skills` (32 liked videos, categories claude-code-workflow / plugins-skills / learning-resource). Verified 2026-10-10 against GitHub (star counts, push dates, licenses), code.claude.com docs (commands, ultrareview, code-review, scheduled-tasks, memory, costs, skills, remote-control), support.claude.com, and project READMEs. Companion data: `claude-code-workflow-and-skills.json` (67 rows). Note: `claude.com`, `skills.sh`, `context7.com`, `typesafe.ai`, `ai.google.dev` and `higgsfield.ai` were unreachable from the research sandbox; those items are marked with the secondary sources used.

## What the creators are collectively saying (patterns, not individual videos)

1. **"Install this skill pack" is the dominant format.** 19 of 32 videos pitch a GitHub repo of SKILL.md files or a Claude Code plugin. The stacks recur: process scaffolding (addyosmani/agent-skills, superpowers), de-bloat (ponytail, caveman, pstack's unslop, thermos), memory (claude-mem, obsidian-second-brain), design (impeccable, taste-skill, awesome-design-md, Emil Kowalski), and verification (Playwright MCP, per-feature verification skills).
2. **Token anxiety drives a whole sub-genre.** caveman (110k stars), ponytail (160k), markitdown (189k), the Codex quota hack, and /effort are all about making the 5-hour and weekly limits last. Every creator quotes the author's own benchmark as fact.
3. **Star counts are the credibility currency and, surprisingly, mostly true now.** The record flagged 216k (Karpathy skills), 161k (markitdown), 94k (superpowers) and ~100k (Addy) as implausible. Verified today: 218k, 189k, 297k and 104k. The ecosystem has simply grown faster than the captions. Only the "1.5 million skills" (find-skills) and "3.6M installs" figures could not be supported.
4. **Process over prompts.** The two highest-scored ideas in the records are not tools: Anthropic's own "thin CLAUDE.md, judgment not rules, skills on demand" guidance, and the "write a verification skill per feature so the agent tests the app" pattern. Both are free and native.
5. **Multi-model sidecars.** Several videos pair Claude (orchestrator) with Gemini (images, long video), Higgsfield (video), ElevenLabs (voice). Claude stays the brain; others are tools.
6. **Learning-resource videos are funnels.** Stanford lecture via DM, the Ryan Ahmed "free course" (email-gated Maven lightning lesson), Claude Code Club ($9/mo), Trillion waitlist, "comment PONY". The underlying free material (Karpathy's gist, 12-factor-agents, official repos) is always publicly available without the DM.
7. **Ben Gusberg alone accounts for 8 of 32 videos.** Same intro ("Stanford founder, raised $4M", unverifiable), same CTA ("let me know what you build"). No affiliate links detected, but he repeats repo-README claims verbatim and inflates numbers ("216,000 stars", "1.5M skills", "connect Claude to LinkedIn"). Treat as a discovery feed, not a reviewer.

## What holds up vs what is hype (with evidence)

**Holds up (verified, use as stated)**

- **Anthropic context-engineering guidance.** The July 24 2026 post ("We removed over 80% of Claude Code's system prompt", Thariq Shihipar) is corroborated by multiple writeups and, more importantly, is now in the official docs: target under 200 lines per CLAUDE.md, remove conflicting rules, `/doctor` trims content derivable from the codebase and keeps "pitfalls, rationale, and conventions that differ from tool defaults", `/doctor prompt-audit` (v2.1.283+) finds instructions "written for older models". The "0% worse" is Anthropic's internal eval; the operational advice stands regardless.
- **Every slash command in the "5 commands" video exists.** `/code-review ultra` (alias `/ultrareview`, 3 one-time free runs on Pro/Max then $5-25 per run in usage credits; the "May 5th" deadline was 2026 and has passed but the 3 free runs remain), `/effort` (low..xhigh, max, auto), `/simplify` (four parallel cleanup agents, no bug hunting), `/loop` (1-minute minimum, session must stay open, 7-day expiry, `loop.md`), `/mcp` (manages connections; the "/slack, /notion" claim is wrong, servers do not become slash commands). Bonus not in any video: `/skill-doctor` reports per-skill context cost and usage.
- **Karpathy LLM Wiki.** Gist is real (April 4 2026, ~5k stars): immutable `raw/`, LLM-owned wiki with `index.md` + `log.md`, schema in CLAUDE.md, ingest/query/lint, works to "~100 sources, ~hundreds of pages" then add a search tool. The creator's `outputs/` folder is his addition.
- **multica-ai/andrej-karpathy-skills.** 218k stars, a short CLAUDE.md with four rules derived from a real Karpathy post. Not affiliated with him. Prompt text only.
- **addyosmani/agent-skills.** 104k stars, MIT, pushed today, nine commands (the three unnamed are `/constraints`, `/webperf`, `/code-simplify`), 25 skills, installs as a Claude Code plugin.
- **ponytail.** 160k stars. Author benchmark says -45% tokens / -26% cost on Opus 5.5. The only independent test (JetBrains AI blog, 80 paired tasks) found -15% code, -10% cost, -11% time, no quality difference. Real but a quarter to half of the claim.
- **caveman.** 110k stars. The TikTok fact-check ("~30%, not 65%") is directionally right. The README's own numbers: `/caveman` 4,119 output tokens vs 4,334 for "Answer concisely" vs 6,983 baseline; JetBrains measured 8.5% fewer output tokens. The 65% headline is not tied to any stated method. The input-side proxy (-33% input tokens on logs/CSV/JSON) is the more interesting half.
- **linkedin-agent-skill.** 1.7k stars, MIT, substantive skills with real local scripts. But both headline claims are false per the README itself: no LinkedIn connection ("would violate its user agreement"), and the "5 AI detectors" are five local heuristics in `detect.py`, not GPTZero/Originality/etc.
- **pstack.** Real, in cursor/plugins (10.7k stars, MIT), by Lauren Tan (poteto, React core, ex-Meta/Netflix, Cursor). Not a "SpaceX engineer". It is a Cursor plugin; Claude Code use means copying SKILL.md files or trusting 0-star ports. `thermo-nuclear-code-quality-review` lives in the `thermos` plugin (moved from cursor-team-kit, matching the on-screen path).
- **claude-mem.** 99k stars, Apache-2.0, v13.35. Works, but the installer now pushes a hosted "observer" sign-in with a 30-day trial, optional cloud sync, and by default compression spends your Anthropic plan. Not the pure-local tool the videos imply.
- **Design stack.** impeccable (79k, Paul Bakaus, 24 commands + 59 deterministic lint rules), taste-skill (94k, v2 experimental, sponsor-driven README), awesome-design-md (120k, 73 brand DESIGN.md files), emilkowalski/skills (45k, appears to be the real Emil Kowalski). All real and maintained.
- **Plugins video.** Playwright MCP (38k, official Microsoft), Supabase MCP (official `supabase/mcp`, hosted with `read_only` and `project_ref` flags the video never mentions), Strix (67.7k, needs Docker + your own LLM key, "authorized use only"), SkillUI (2.4k, pure static analysis), Context7 (62.9k; free tier now capped monthly).
- **Research citation.** "Up to 39% dumber": Laban et al., "LLMs Get Lost in Multi-Turn Conversation", ICLR 2026 oral, average 39% drop across six tasks (v1 said 35%). The "designed to get dumber" spin is false.
- **12-factor-agents.** 26.6k stars, CC BY-SA 4.0 content, Apache-2.0 code, no v2, one appendix (Factor 13: pre-fetch context).
- **markitdown.** 189k stars, MIT, pushed Oct 4; `pip install markitdown-mcp` works over stdio. "Up to 70% fewer tokens" is unsourced; Claude Code already reads PDF text natively, so gains are for Office files.
- **Usage pool.** support.claude.com: "Your combined usage across both interfaces counts toward your limits" (chat + Claude Code). The Codex two-tank trick does not transfer to Claude.

**Hype or wrong**

- "Connect Claude to LinkedIn, it runs your account" (false, text generation only).
- "find-skills auto-installs whatever you need" (it asks first; "1.5M skills" unsupported; supply-chain risk is real).
- "/mcp turns Slack/Notion into /slack /notion commands" (false).
- "Code Review: enable it and run before shipping" (the GitHub product is Team/Enterprise only, $15-25 per review; on Max you get `/code-review` locally, which is good).
- "obsidian-skills connects your codebase into a second brain" (it teaches Obsidian file formats; nothing about codebases).
- "Models are designed to be lazy" (Unlazy's hook; its cited papers describe underthinking, not intent).
- "caveman cuts 65%", "ponytail cuts 50%" (independent tests: ~8-15% and ~10%).
- "Hyperframes one-prompt explainer video" (framework is real, 60k stars, HeyGen; the demo was @deedydas's own pipeline; needs ffmpeg + Chrome + a paid TTS).
- "banana-pro-director" and "cinema-world-builder" do not exist as public repos (DM funnel).
- anthropics/courses was archived on Sep 15 2026; the "five repos" video recommends a read-only repo.
- Higgsfield skill: 56 stars, no license file, Codex-first install, "discounted pricing" link in the description is a creator link.

## How we should approach this in our own apps and workflow (concrete, ordered, with tradeoffs)

**Week 1: free, native, no installs (do these first)**

1. **Run `/doctor` and `/doctor prompt-audit` in every active repo.** Accept trims; move procedures into `.claude/skills/` or `.claude/rules/` with `paths:`; delete NEVER rules that were written for old models unless they guard a real incident (then make that a PreToolUse hook). Target under 200 lines. Tradeoff: an hour across repos; watch one repo for a week before rolling out.
2. **Append the four Karpathy rules** (state assumptions, minimal code, surgical changes, verifiable success criteria + loop) to CLAUDE.md by copying 10-15 lines from the repo. Do not install a plugin for a prompt.
3. **Make the built-in review loop the default ship step:** `/simplify` then `/code-review high` (background, free) before every PR; `/code-review ultra` only for the three scariest merges (use the free runs, then $5-25 each; enable usage credits first).
4. **Start the verification-skills pattern in one app.** Install Playwright MCP (`claude mcp add playwright -- npx @playwright/mcp@latest`), write `.claude/skills/verify-signup`, `verify-payment`, `verify-core-flow` SKILL.md files, require `/verify` + screenshots on every PR, add "update verification skills" to the ship checklist. This is the single biggest time-saver for a solo founder. Tradeoff: browser runs cost tokens; scope them with `/mcp disable playwright` when not testing.
5. **Usage hygiene:** `/effort low` for grunt work, `/clear` between tasks, `/usage` weekly to see what skills/MCP/subagents eat, `/skill-doctor` after any install. Run `/insights` once and fold the friction report into user-level CLAUDE.md (under 20 lines). This replaces the Jev video's pattern for free.
6. **Writing rules:** add Minto (conclusion, three reasons, evidence) to the email/writing skill; add "red team" and "CEO" as named voices in council-gate if missing; save the Context Transfer prompt as a claude.ai skill (Claude Code already has session-handoff).
7. **Read 12-factor-agents** (one hour) and add a 12-factor check to the agent-feature spec template.

**Week 2: targeted installs, one at a time, measured**

8. **Official plugins:** `/plugin` > Discover > `typescript-lsp`, `feature-dev`, `commit-commands`, `security-guidance`, `frontend-design`. Stop at five.
9. **addyosmani/agent-skills** for `/spec` and `/plan` (and `/build auto`). Disable the review/simplify skills in it since built-ins cover them. Tradeoff: 25 skills of listing context; prune with `/skill-doctor`.
10. **One design skill, not four:** Impeccable (`/impeccable init`, `audit`, `polish`) plus a project `DESIGN.md` synthesised from two awesome-design-md references. Add `emil-design-eng` only for motion-heavy UI. Skip taste-skill (redundant, experimental v2).
11. **Token A/B:** install ponytail OR caveman on one project for a week and compare `/usage`. Expect ~10% total, not 50%. Keep only if `/ponytail-review` diffs beat `/simplify`. Do not stack ponytail + caveman + pstack + thermos; they contradict and bloat context.
12. **Supabase MCP** on Supabase apps with `read_only=true&project_ref=<ref>`; drop read_only only in dev. **Context7** with a free key for version-sensitive libraries only.
13. **markitdown** as a CLI pre-step for decks/spreadsheets (`pip install 'markitdown[all]'`); MCP only if converting inside sessions becomes frequent.
14. **Strix** once per app on a staging deploy with an API key and a budget, before the next launch. Never against production.
15. **Gemini image skill** (`gemini-images`, key from env, 16:9, outputs to `assets/`) the next time an app needs hero/OG/thumbnail images.

**Week 3+: knowledge and memory**

16. **Karpathy wiki for CodingStrategies:** paste the gist into Claude Code in a `knowledge/` folder, seed `raw/` with existing handoffs/research, let Claude write the CLAUDE.md schema, index.md and log.md; run lint weekly via a cloud Routine. Stay under ~100-200 sources before adding search. Tradeoff: ingest touches 10-15 pages per source, so batch ingests.
17. **claude-mem trial** only after checking native auto memory (`~/.claude/projects/<repo>/memory/MEMORY.md`) is populated. If trialling: choose the Anthropic-plan provider, decline cloud sync, set `CLAUDE_MEM_ONLINE_OPTIN=false`, measure per-session overhead with `/usage`. Hormozi skill: one `/hormozi-report` per product for pricing/offer sparring (read `install.sh` first; 400MB).
18. **`/remote-control`** for long builds steered from the phone; `/loop 10m` from a fresh session for CI babysitting; cloud Routines (1h minimum) for anything unattended.

**Skip:** Claude Code Review (Team/Enterprise), courses (DeepLearning.AI audit-only, Microsoft, Hugging Face, Ryan Ahmed, Stanford repost), Claude Code Club, Trillion, Higgsfield, Jev, OpenAI quota hacks, DM-gated skills, Composio's awesome list, superpowers (unless Addy's pack proves too light).

## Gaps: things they talk about that Haji has not liked yet but should look at

- **`/skill-doctor`, `/doctor prompt-audit`, `/insights`, `/verify`, `/batch`, `/goal`, `/schedule` and cloud Routines.** None appear in the 32 videos; all are in the current commands reference and directly answer the cost and automation questions the videos raise.
- **Native auto memory and `.claude/rules/` with `paths:` frontmatter.** The memory plugins are pitched as if nothing native exists; the docs now ship per-repo MEMORY.md and path-scoped rules that load on demand.
- **Claude Code GitHub Action** (open source, runs on API billing in your own CI): the Pro/Max-compatible alternative to the Team-only Code Review product.
- **Code intelligence (LSP) plugins** in the official marketplace: the docs say they cut file reads and report type errors after edits, which is a bigger token lever than terse-output skills.
- **REVIEW.md / per-repo review instructions** and `skillOverrides` to stop Claude self-invoking review; not covered by any creator.
- **Prompt-cache statistics in `/usage`** (cache hit share, misses, cold cache after 1h): explains the "usage climbs in a long session" effect that the Codex-hack and context-transfer videos gesture at.
- **MCP tool-search deferral and `/context`**: the docs recommend CLIs (gh, gcloud) over MCP for context efficiency; worth checking Haji's MCP list against this.

## Open questions

1. Does `/doctor prompt-audit` trimming change behaviour on Haji's repos with long NEVER lists (session-handoff rules, council-gate)? Needs a one-repo, one-week trial with before/after `/usage`.
2. What is the real share of output tokens in Haji's sessions? If cache reads dominate (as the docs imply), caveman/ponytail gains are smaller than any A/B on output tokens suggests. `/usage` prompt-cache line answers this.
3. Does Claude Code have a recorded-browser-session artifact equivalent to Cursor cloud agents/Devin, or is Playwright screenshots-in-PR the ceiling? Not found in docs this session.
4. Exact current free quota for Context7 and whether Supabase's hosted MCP supports OAuth scoping per project for a solo account (official pages unreachable from the sandbox).
5. Gemini video-understanding limits (duration, file size) and whether Nano Banana Pro pricing is still ~$0.134/image; verify on ai.google.dev before building the image skill.
6. Does claude-mem's "Anthropic plan" provider authenticate via Claude Code's own login and how much plan usage does the compression consume per session? README is silent.
7. Which Stanford lecture the @Dipanshu_AI tweet points to (irrelevant to action, but the record asked).
8. Whether to standardise on Addy's `/spec`/`/plan` or superpowers' brainstorm/plan/TDD flow; both are maintained and large, and running both is the one thing not to do.
