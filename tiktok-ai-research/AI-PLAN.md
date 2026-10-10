# AI Coding Intel: The Plan

Built 2026-10-10 from 375 liked TikToks (119 AI-related, read in full), the last 50 posts of all 66 AI creators (1,663 scanned by title, 260 read in full: 140 added something new, 120 duplicated what you already liked), and 207 tools, repos and playbooks verified on the web the same day. Verdict rows, per-video records and the six theme guides are in the dashboard tabs.

## BLUF

1. **Most of what TikTok sells you is one of three things:** a feature Claude Code already ships (reviews, verification, routines, memory, design, cross-session messaging), a prompt dressed up as a product, or a funnel ("comment X", "DM me", "Stanford founder, raised $4M"). The content is a discovery feed, not a review. Treat it that way.
2. **The ideas that scored highest were practices, not installs:** thin CLAUDE.md with judgment instead of rules, a verification skill per feature so the agent tests the app, phased plans with a human gate between phases, a question-first prompt before building, a 21-item pre-launch security and legal checklist, and WWWHH handoffs between agents.
3. **Three free-money items have deadlines** (Max monthly API credits, Claude for Startups, the cloud-session credit). Ten minutes each. Do them today.
4. **One income play is worth a two-week test** (AI phone receptionist for local shops, Bland free tier plus a Claude Code booking backend). Everything else sold as "$10k/month" has no evidence behind it.
5. **Token-saving skills are real but small:** independent tests show roughly 10% savings, not the 50 to 65% claimed. Measure one, do not stack four.

## The operating rules (how we read this content from now on)

| Rule | Why |
|---|---|
| Native first | Before installing anything, check whether Claude Code already does it: `/doctor`, `/verify`, `/simplify`, `/code-review`, `/design`, `/context`, `/skill-doctor`, `/insights`, Routines, Projects, auto memory, `.claude/rules`. Half the "must-install" videos are covered. |
| Process over tools | The top-scored items in 229 videos were habits. A habit costs zero tokens and zero supply-chain risk. |
| One of each | One process pack, one design skill, one token tool (A/B), one review loop. Stacking contradicts and bloats context. |
| Measure claims | Any "X% fewer tokens" or "$Y/month" claim is unverified until `/usage` or a bank deposit says otherwise. |
| Stay inside the Max rules | Personal automation on native surfaces under your login is fine. Anything customers touch runs on an API key or Managed Agents. No harness that "reuses Claude Code credentials" (Hermes OAuth, OpenClaw, OmniRoute subscription mode). |
| Security and legal before user one | RLS on, secret key server-only, spend cap on, consent before analytics, policies from attorney templates. The checklist is 21 items and becomes a `/prelaunch` skill so it repeats on app number four. |
| Own a moat, not a wrapper | Jev went viral in September; OpenAI shipped the same thing as an API two weeks later. Any app we ship owns a workflow or data, never a single model call. |

## Do now (this week)

| # | Action | Why it matters | Cost / time |
|---|---|---|---|
| 1 | **Claim Max monthly API credits.** claude.ai > Settings > Billing > API credits > link the Console org the apps ship from. One workspace per app with a spend limit. | $100 (5x) or $200 (20x) of API capacity every month for in-app AI features and batch jobs. Expires monthly, no rollover. Link is permanent per org. | 10 min |
| 2 | **Apply to Claude for Startups** at platform.claude.com/offers/startups-application with a product-domain email. | Team year and $1k credit are "over capacity" as of Oct 10, but the partner stack (ElevenLabs 12 months, ClickHouse $5k, Firecrawl, Granola) is live. Re-check Nov 10. | 5 min |
| 3 | **Run `/claim-credit`** and look at the usage menu. | Some accounts were auto-granted the $250 cloud-session credit. Spend by Nov 4 on `claude --cloud` jobs; it does not count against the plan while it lasts. | 1 min |
| 4 | **`/doctor` and `/doctor prompt-audit` in every active repo.** Target under 200 lines. Move procedures into `.claude/skills/` and `.claude/rules/` with `paths:`. Delete NEVER rules written for old models unless they guard a real incident. | Anthropic cut 80% of Claude Code's own system prompt with no loss. Long rule lists make results worse on current models. | 1 hour across repos |
| 5 | **Add five blocks to CLAUDE.md** (about 40 lines total): the four Karpathy rules (state assumptions, minimal code, surgical changes, verifiable success criteria); the `npm view` rule (never assume a package version); the five UX rules (skeleton loaders, prefill, optimistic UI, saved state, plain-language errors with retry); the infra decision log (cost at 1k/10k/100k users and exit path before adding any vendor); the 12-factor agent line for any app with an agent loop. | These are the single highest-value lines in the whole dataset and they are free. | 20 min |
| 6 | **Make the review loop the ship step:** `/simplify` then `/code-review high` before every PR. `/code-review ultra` only for the three scariest merges (3 free runs, then $5 to $25 each). | Replaces the Team-only Code Review product the videos sell. | 0 |
| 7 | **Verification skills, one app first.** Install Playwright MCP, write `verify-signup`, `verify-payment`, `verify-core-flow` skills, require `/verify` plus screenshots on every PR. | The highest-leverage idea in the dataset for a solo founder: the agent proves the app works instead of you clicking through it. | 2 hours first app |
| 8 | **Design stack, once:** Realtime Colors palette, one DESIGN.md from awesome-design-md edited to your tokens, `npx impeccable install`, Emil Kowalski's skills, `/design <brief>` per feature that matters. CLAUDE.md line: "All UI follows DESIGN.md." | Kills the "same AI look" without four overlapping skills. Taste Skill only as an A/B, never auto-loaded alongside Impeccable. | 45 min |
| 9 | **Build the `/prelaunch` skill** from the 21-item checklist in the security guide (RLS and grants with pgTAP tests, no secret key client-side, owner check on every mutation, Supabase hardening, dependency audit, `/security-review` on full repo, rate limits, policies from General-Legal templates, consent-gated PostHog, data deletion path, CAN-SPAM, dark patterns, WCAG via axe, licenses, Vercel Pro with spend cap, backups and incident plan). | Runs once per app before the first user, starred items on every push. Output is a 21-row pass/fail table with evidence. | I build it; you run it |
| 10 | **WWWHH in every subagent.** Final report = Why ready / What next / Where (absolute paths) / Heads up / How sure (0 to 100). Orchestrator spawns a read-only verifier below 70. | The one pure engineering idea in the agent videos. Confidence triages, never approves. | 15 min |
| 11 | **Usage hygiene:** `/context` to prune unused MCP servers, skills, agents; `/effort low` for grunt work; `/clear` between tasks; `/usage` weekly; `/skill-doctor` after any install; `/insights` once, fold into user-level CLAUDE.md. | The creators' "usage limit hacks" are these commands, for free. | 30 min |
| 12 | **Three prompts to keep:** the question-first prompt (ask one question at a time until 95% confident, then two-line plan, then wait); "what decisions should I make before I start?" recorded before building; phased plans with a hard approval gate between user-testable phases. | Top-scored creator-gap findings. They stop the agent from building the wrong thing fast. | 10 min to save as skills |
| 13 | **Rotate every API key ever pasted into an AI tool** and add gitleaks or GitHub secret scanning with push protection. | Cheapest breach prevention in the set. | 30 min |

## Try next week (one at a time, measured with `/usage`)

| Item | What to do | Keep if |
|---|---|---|
| Official plugins | `/plugin` > typescript-lsp, feature-dev, commit-commands, security-guidance, frontend-design. Stop at five. | Context cost under control in `/skill-doctor` |
| Process pack | addyosmani/agent-skills for `/spec` `/plan` `/build`, OR gstack (`/office-hours`, `/plan-ceo-review`, `/qa`, `/ship`). Pick one. | It beats council-gate plus code-review on one real feature |
| Token A/B | ponytail OR caveman on one project for a week. Expect about 10%. | `/usage` shows it and output quality holds |
| Supabase MCP | Read-only, dev project ref only. Never prod. | Fewer round trips on schema work |
| Context7 | Free key, version-sensitive libraries only. | Fewer wrong-API hallucinations |
| MarkItDown | `pipx install 'markitdown[all]'` for XLSX, PPTX, DOCX before reading. | Office files show up in sessions |
| Strix | Once per app on staging with a budget. | It finds an IDOR the static review missed |
| Marketing stack | coreyhaines31/marketingskills (pricing, offers, launch) and alexsmedile/hormozi-skills (`/audit-offer`, `/pricing-strategy`) on one existing app. | A pricing or offer change you actually ship |
| Hook scoring | TikTok Studio CSV export, `score-hooks` skill on Haiku paid by the credits. Write hooks by hand, rank with AI (the creator's own A/B result). | Only matters once there is content volume |
| On-call loop | PostHog error webhook > Routine API trigger > failing test first > draft PR with RISK line > second routine runs code-review. Auto-merge only after about 20 clean PRs. | The native version of every "AI engineer while you sleep" pitch |
| Haiku router | 200 labelled examples, tool-use enum plus confidence, measure accuracy and latency. | Answers Jev and the Decisions API without a new vendor |
| Second-model reviewer | openai/codex-plugin-cc inside Claude Code with a CLAUDE.md collaboration block: Claude builds, Codex reviews. One reviewer, not a council. | Catches something `/code-review` missed |
| Cloudflare security-audit-skill | Verify it is Cloudflare-official and the star count, then run on one app. | Findings beyond Strix |
| Zapier SDK | Loop in code, call the model only for judgment. Covers 9,000 apps with one login. | A real integration need appears |
| Mods | A goal meter and a cache-cost HUD inside Claude Code. I can build these with the plugin-authoring skill. | You want to see cost and progress at a glance |
| `/analyze-content` | The pipeline that built this dashboard already does this (frames, transcript, on-screen text). Turn it into a skill for any video URL. | Research on demand |

## Watch (not now)

Jev and the OpenAI Decisions API (uncalibrated confidence, Haiku does it), Managed Agents (the home for a customer-facing agent with a budget, $0.08 per session-hour plus tokens), Claude Code Projects (rollout; threads plus PRs replace every "AI company" dashboard), Claude Dashboards (Pro/Max, launched Oct 8, no video covered it), Claude Motion (Team and Enterprise only), Meta's official Ads MCP (own account is easy, client accounts need business verification), agent teams (experimental, 3 to 10x tokens), Trillion (waitlist, no code), Instinct, Muse, Cue, Hark, Fo (inbox-holding agents; read the retention complaints first).

## Skip (and why)

| Skip | Reason |
|---|---|
| Paperclip, Automaton, Cowork "four-agent dev team" | Org-chart theatre. Anthropic's own post: role splits are "often counterproductive" and cost 3 to 10x tokens. Automaton holds a wallet and self-modifies; that is your liability. Projects plus Routines give the useful 20%. |
| Hermes on a VPS, any "Jarvis" course | Second harness, 47k open issues, two 2026 injection CVEs, borrowed-OAuth billing cut off since April. The architecture is Claude Code's own. |
| OmniRoute, GonkaRouter, Dahl, MixRoute, NVIDIA "never pay for API keys" | Free tiers summed into a headline; 13 providers self-tagged ToS-avoid; routing your Max subscription through a proxy risks the account; prompts may train models. Throwaway evals only. |
| Readdy and OpenArt side hustles, "$10k website in one prompt", four-prompt "$10k/month" | Affiliate scripts (20% commission), paid tiers hidden ("$0" needs a $34 plan), no client or deposit shown anywhere. |
| Manus | Sponsored (#manuspartner), hosted lock-in, agents with wallets, undisclosed future pricing. |
| AppBully paid pass, "Anthropic-Cybersecurity-Skills" | Static check plus Supabase's free Security Advisor; the skills repo is not Anthropic's and has nothing for Supabase, JWT or web OWASP. |
| Scrapling for Cloudflare bypass, de-anonymization funnels (RB2B etc.) | The "800x" is a parser micro-benchmark; bypassing bot protection is the exact behavior that creates CFAA and ToS exposure. |
| Courses and clubs (Claude Code Club, Chase AI+, CoWork OS, DM-gated prompt packs, "Stanford course") | Public material behind a funnel. anthropics/courses is archived. |
| React Video Editor templates, Antigravity, Google Opal | $149 to $499 licence; a second IDE; shutting down Nov 17. HyperFrames is the free answer. |
| Claude Code Review (GitHub product) | Team/Enterprise, $15 to $25 per review. `/code-review` locally is the equivalent on Max. |

## Income plays, ranked (realistic 90 days x fit x hours)

| Rank | Play | Realistic 90 days | Reality check |
|---|---|---|---|
| 1 | **AI phone receptionist for local service businesses.** Bland Start ($0.14/min, free number, no card) plus Claude Code booking backend (Cal.com), SMS and CRM glue. $750 setup + $250/mo, 30-day cancel. 30 shops in one niche in two weeks. | 2 to 5 clients, $500 to $2,000 MRR plus $1.5k to $3.5k setup. First dollar in 2 to 6 weeks. | Sales is 80% of the hours. Vendors sell the same at $30 to $300/mo. You are the 7pm support line. Check call-recording consent and AI-disclosure rules in your state. |
| 2 | **Booking-page lead-in** (Claude Code + Cal.com + Cloudflare Pages), $500 one-off or bundled into #1. | A few sales as a two-week cash test. | DM conversion is 1 to 3%. Never use scraped photos in a preview before they say yes. Not a business. |
| 3 | **Marketing stack for our own apps** (marketingskills, hormozi-skills, hook scoring, Remotion free tier). | Indirect; multiplies what the apps already earn. | Nothing without traffic. 3 to 5 hours a week of hygiene. |
| 4 | **Free money** (credits, Startups program). | $1,200 to $2,400 a year of cost offset. | Does not pay for Claude Code sessions. Makes apps cheaper to run, not income. |
| 5 | **Veteran-owned government contracting** (SAM.gov Opportunities API plus Claude drafting, human submits). VOSB/SDVOSB set-asides are a moat the TikTok crowd does not have. | 90 to 180+ days to a first award. | SAM.gov ToS bans bots and bot logins; the creator who automated submissions burned every token in two hours. Start with SAM registration, SBA VetCert, a capability statement. |
| Not yet | Claude-run Meta ads; C-file analysis tool for veterans. | | No product with margin or ad budget; the arcads repo uploads ads paused and the 7.5x case is unverifiable. C-file: 38 CFR 14.636 means only accredited reps can charge; NJ/ME/NY criminalized unaccredited paid help. Lawful shape is B2B for accredited attorneys or a free indexer. Validate with three accredited attorneys before code. |

## How we build from here (the approach our apps follow)

1. **Spec, then plan in user-testable phases with a human gate between phases.** Question-first prompt before the spec. Record decisions before building.
2. **Build with constraints in files, not in your head:** CLAUDE.md under 200 lines, DESIGN.md for UI, `.claude/rules` with paths, skills on demand.
3. **Verify with skills, not eyes:** a verification skill per feature, Playwright screenshots on every PR.
4. **Clean, then review:** `/simplify`, `/code-review high`, a second model only as a single reviewer. Ultra review for scary merges.
5. **Pre-launch gate:** `/prelaunch` 21 rows, all pass, before user one. Starred rows every push.
6. **Security by default:** RLS and revoked grants, secret key in one server module, Supabase MCP read-only on dev, spend cap on Vercel Pro, secret scanning in CI, keys rotated.
7. **Consent by default:** nothing fires before accept, Global Privacy Control honored, policies from attorney templates filled from the real schema.
8. **Cost by design:** Haiku 5.5 for volume and routing, Batches API at half price, monthly credits spent on purpose, `/effort` matched to the task.
9. **Agents only where there is a check:** WWWHH handoffs, confidence gates, humans contacted through tool calls (12-factor), draft PRs before auto-merge, Routines with stripped connectors, Managed Agents with budgets for anything customer-facing.
10. **Own a workflow or data, never a wrapper.** Every feature answers "what dies if the next keynote ships this as an API?"

## Gaps: what the creators cover that you had not liked yet (46 new items scored 4 or 5, grouped)

**Claude Code itself (none of your liked videos covered these):** `/design` inside the CLI (artboards, stack with Impeccable), Mods (TypeScript plugins that intercept events and add panes; a cost and goal HUD is a two-hour build), cross-session messaging (one session plans, another builds), `/context` pruning to stop hitting limits, Routines' API and GitHub triggers, Projects, Auto Mode by default since Aug 14 (verify the 97% figure), effort data (max effort costs about 15x extra-high for about 1% accuracy; use extra-high), the openai/codex-plugin-cc plugin for a second-model reviewer, a "PR creator with docs" skill that updates per-feature CLAUDE.md before every PR.

**Prompts and habits worth saving as skills:** the question-first prompt, "what decisions before I start", phased plans with approval gates, the `npm view` package-version rule, the Google developer-docs style skill to cure "Claudish" prose, `/visualplanner` (plan as an HTML page with per-section thumbs), the i-have-adhd output skill (numbered steps, no preamble, exact next command), "cc the agent into the email thread" delegation.

**Security (the biggest gap cluster, 14 items):** Cloudflare's security-audit-skill (one creator ran it: about 130 agents, 9.2M tokens, 10% of a weekly 20x limit, found low and medium issues; verify the repo is Cloudflare-official), NVIDIA SkillSpector (scan a skill before installing it; verify it exists), Gitleaks after every AI change set, rotate every key ever pasted into an AI tool, the Vercel breach lesson (non-sensitive env vars are readable; flag sensitive, audit logs), email OTP is not real MFA, Stripe webhook idempotency and outage behavior, agent spend controls (own wallet with a cap, ask-first for send or spend, kill switch outside the chat), and three overlapping 10 to 20 item checklists with verbatim Claude prompts that fold straight into the `/prelaunch` skill.

**Design:** the 20 Laws of UX as one markdown file, Impeccable 4.0 Worlds and Live, Anthropic's own frontend-design skill, a DESIGN.md generated from a folder of inspiration screenshots, Mobbin MCP for 600k real UI references before building a screen, the 20-item pre-launch website checklist (meta, OG, sitemap, contrast, 404, forms).

**Business:** hormozi-skills plugin (orchestrator plus 17 skills: offer audit, pricing, landing copy), a "Claude SEO" GEO skill (verify repo), `/analyze-content` (this project's own pipeline as a skill), Zapier SDK for agents, Meta Ads Library ad-spy scoring, a Gmail triage Routine at 4am with drafts only, the subscription-price-decay retention hack, pre-launch demand tests with concept emails.

**Models and programs:** Haiku 5.5 pricing and benchmarks (agentic coding 39%, computer use 72%, $0.10/$0.50, 5x price above 100k context), Claude Dashboards, the Startup Stack partners beyond the headline, Anthropic's cheap tiers that every "cheap model" video ignored, ducktate's launch-readiness stages 7 to 10 (AI-feature disclosure, DMCA agent, click-to-cancel, TCPA).

## Where the Council split

- **Skeptic vs Pragmatist on the receptionist play.** Skeptic: churn and support load will eat a solo founder; the creator's prices are top of market. Pragmatist: it is the only play with recurring revenue and a real Claude Code edge, and the test costs two weeks and $0. Resolution: two-week test, one niche, three clients max, then decide.
- **Innovator vs Ethicist on the C-file tool.** Innovator: real demand, veteran credibility, competitors just launched. Ethicist: claim-shark law is criminal in three states and the VA sends cease-and-desists. Resolution: no direct-to-veteran paid service without accreditation; B2B for accredited reps or free only, after three attorney conversations.
- **Domain Expert vs User-Advocate on the number of installs.** Expert wants the full stack. User-Advocate: Haji is one person with ADHD and a weekly limit; every install is context cost and a decision. Resolution: the "one of each" rule above.
- **Analyst note:** every star count the creators quoted was true or already low; every revenue number was unverifiable; every token-saving percentage was 3 to 6x the independent measurement.

## Open questions I could not close

1. Whether your account is in the Claude Code Projects rollout (if not, Routines plus Desktop scheduled tasks cover the same ground).
2. Exact behavior change after `/doctor prompt-audit` trims your long NEVER lists (session-handoff, council-gate). Needs a one-repo, one-week trial.
3. Supabase's Oct 30 explicit-grant change and new key format: confirm on the changelog before relying on dates.
4. Which Bland tier includes the in-call SMS and scheduling nodes (decides whether the receptionist demo works on the free tier).
5. Whether Claude for Startups reinstates the Team year and $1k credit, and whether an existing Max subscriber counts as "new to Team" (re-check Nov 10).
6. Token cost of gstack's full role chain and of `/design` on your plan: log the first two uses.

## Decisions needed from Haji

1. **Which Console org gets the monthly API credits.** The link is permanent per org.
2. **If Startups approves a Team plan: Team (unlocks Motion, pooled $500) or stay on Max 20x ($200 credits plus 20x Claude Code limits).**
3. **Green-light the two-week receptionist test** (one niche, three clients max, Bland free tier), yes or no.
4. **Process pack: addyosmani/agent-skills or gstack.** One, not both.
5. **Build the Mods HUD (goal meter and cost gauge inside Claude Code)**, yes or no. About two hours of my time.

## What runs without you

I can build and hand you: the `/prelaunch` skill, the five CLAUDE.md blocks, three verification-skill templates, a starter DESIGN.md and Impeccable setup instructions, the question-first and phased-plan skills, the hook-scoring skill on Haiku, the Haiku router test harness, a Routines config for the on-call loop, the `/analyze-content` skill from this project's own pipeline, and a weekly refresh of this dashboard as new likes come in.
