# business-with-ai: what to consider

Research date: 2026-10-10. 24 liked videos (22 with content, 2 unreadable photo posts). Every tool and play below was checked against official pages, GitHub, or primary docs; where a site could only be reached by curl, that is noted in the JSON evidence field. Companion file: `business-with-ai.json` (35 verdict rows).

## What the creators are collectively saying (patterns, not individual videos)

1. **"Build it for a local business and charge $500-$2,000."** Five of the 22 videos are the same pitch with a different tool: Readdy sites (two ambassadors), a Claude-built booking page (bengusberg), an OpenArt gym video (james_creates_), and a Bland receptionist (jasoncooperson). The common shape: prospect on Google Maps or Instagram, generate the asset in minutes, DM it, invoice. None shows a real client, a contract, or a bank deposit.
2. **"Let the agent spend money for you."** Meta ads run by Claude (mr.paidsocial), bid submissions by an agent with its own computer (xinoyaps), a cloud assistant that logs into your accounts (Hark). The videos treat credential and card hand-off as a feature; the one candid report (gov-contracting) says it burned every token in two hours and "handing over the keys" is at your own risk.
3. **"Free money from Anthropic."** Three videos in one week on the Claude for Startups program and the new monthly API credits for Max/Team. These are the only claims in the set that are fully documented by the vendor.
4. **"Give yourself a board."** Two separate creators (bengusberg in Cowork, kevinfremon in Trillion) sell the same idea: persona agents that debate and vote. One of them published a serious prompt with anti-fabrication machinery.
5. **"Score, don't write."** The angusthenontechnical trilogy (PostHog funnel, Jev hype reel, Hormozi hook loop) pushes a small classifier model (Jev) everywhere, but the hook video's actual finding is that AI-written hooks lost to his own every time and he now only uses the model to rank.
6. **Funnel mechanics are uniform.** Comment-to-DM for a "free template", Skool/community links, affiliate hashtags (#readdyambassador = a 20% x 6-month commission), a $350/yr course behind a "reaction" video. Assume every income number is marketing until proven otherwise; none were.

## What holds up vs what is hype (with evidence)

**Holds up (verified on primary sources)**
- **Monthly API credits for Max/Team** (support.claude.com article 17154008, launched 2026-10-07): Max 5x $100, Max 20x $200, Team pooled up to $500; covers API, Managed Agents, Agent SDK, Playground; not Claude Code sessions; no rollover; one Console org.
- **Claude for Startups** (claude.com/programs/startups): program is real and the videos were accurate on Oct 6-7. As of Oct 10 the page says the Team year and $1,000 credit are "over capacity" and applications are being re-reviewed; Startup Stack offers (ElevenLabs 12 months free, Granola, Hex, ClickHouse $5K, Gamma, Firecrawl) and office hours remain.
- **coreyhaines31/marketingskills**: 54k stars, MIT, 50 skills, commit on 2026-10-08. Install is one command.
- **garrytan/gstack** (gap item): ~136k stars, MIT, 23 roles incl. /office-hours and /plan-ceo-review. No marketing skills.
- **krusemediallc/arcads-claude-code**: 1.6k stars, MIT, last commit 2026-09-22. It generates creatives through Arcads (paid) and uploads ads **paused** via the Marketing API. It does not run campaigns or budgets.
- **Bland / Vapi / Retell pricing** (all pages fetched): Bland Start $0.14/min all-in, no card, free inbound number, 100 calls/day; Vapi $0.05/min + pass-through (~$0.10-0.15 all-in), $5 credit; Retell $0.07-0.31/min, $10 credit, 20 concurrent. A receptionist for a one-location shop costs Haji $50-$150/mo in minutes.
- **Readdy**: real, Starter $15/mo annual with code export, $6/mo per extra client site, 20% x 6-month affiliate program. Both videos are affiliate content.
- **OpenArt**: Director is on every paid plan from $14/mo, but **commercial use starts at Plus ($34/mo)**. The "$0 side hustle" is false on its face.
- **Remotion**: free license for individuals and companies up to 3 people, unlimited commercial use; last commit 2026-10-09.
- **canivibecodeit.com**: 1,093 apps, built by @robj3d3, MIT, verdicts are bot-drafted, monetized by sponsor slots ($2,500/30 days) and a newsletter.
- **The Board prompt** (hellotrillion.ai/p/the-board, dated 2026-07-31): exists, free, includes per-advisor dossiers, a citation gate, abstention, and a unanimity guard. Trillion itself is unreleased (5,471 on the waitlist).
- **Jev (TypeSafe)**: real model, $0.042/M input tokens, output free, launched 2026-09-15; access status is unclear (waitlist removed Sep 20-21, one report of paused signups Sep 22; console returned 403 to an anonymous probe). Speed/cost multiples are vendor claims.
- **Hark**: launched 2026-10-06, free/$20/$100 tiers. **Instinct** raised $1B at a $10B valuation (2026-09-28), not "$10B with no app".
- **SAM.gov Terms of Use**: bots, scraping, and bot-driven use of a login are prohibited; APIs and extracts are the sanctioned route.
- **VA claims law** (38 CFR 14.636; CRS 2026-07-13): only accredited reps may charge, and only after an initial decision; NJ/ME/NY criminalized unaccredited paid help in 2023; no federal criminal penalty yet; VA sends cease-and-desist letters.

**Hype or unverifiable**
- "$1,000 in one night" (Readdy), "ungodly amount of money" (Readdy), "$500 per gym video" (OpenArt), "$10K/month with Claude" (booking site): no evidence, all affiliate or comment-bait.
- "$2,019 spend -> $15,235 sales, Claude bought the ads": not findable anywhere outside the video; the reactor sells a $350/yr Skool; the repo he points at only uploads paused ads.
- "Free GitHub template" for the Bland receptionist: comment-gated, no public repo found under the creator's name.
- "grokbot": no such product found; most likely Grok running inside Nous Research's Hermes Agent (xAI integration announced 2026-05-15) or a hosted wrapper.
- "Jev is a business killer" reel: every demo is captioned "illustrative concept - synthetic data".
- "$30k listening website": the agency product is a strawman; the de-anonymization half (RB2B etc., ~20% match, US-only, $79-$199/mo) is legally exposed and useless for consumer apps.
- One static HTML file "with a booking system": impossible without an embed or backend.
- "Claude notifies us when the stock hits the price": not a native feature.

## How we should approach this in our own apps and workflow (concrete, ordered, with tradeoffs)

Ranking rule: (realistic income within 90 days) x (fit with Claude Code skills) x (hours per week it actually costs). Scores are 1-5.

### 1. AI phone receptionist for local service businesses (Bland now, Retell/Vapi later) -- income 4, fit 5, hours 3
The only play in the set with recurring revenue, a buyer who already feels the pain (missed calls), and a real Claude Code edge (custom booking backend, SMS, CRM glue that no-code resellers cannot do).
- Build: 1-2 days on Bland Start (free number, no card). Cal.com or Google Calendar via webhook. Record a 60-second Loom of a real call.
- Sell: 30 shops in one niche (auto repair, HVAC, med spa, mobile detailing) in 2 weeks. Offer $750 setup + $250/mo, 30-day cancel. Veteran-owned is a legitimate trust signal with many of these owners.
- Realistic 90 days: 2-5 clients, $500-$2,000 MRR plus $1,500-$3,500 in setup fees. First dollar in 2-6 weeks if calls start this week.
- **Blunt reality check:** the creator's $2,000 + $500/mo is top of market; vendor products sell the same thing for $30-$300/mo. Sales is 80% of the hours. Churn hits when the agent mishandles a weird call at 7pm and Haji is the support line. Confirm which Bland tier includes the SMS node and scheduling node before promising the demo's mid-call text. Check state call-recording consent and AI-disclosure rules.

### 2. Booking-page lead-in offer (Claude Code + Cal.com + Cloudflare Pages) -- income 3, fit 4, hours 3
Use bengusberg's prompt as the on-ramp to #1: a real site with a working Cal.com embed, delivered as a live preview URL, $500 one-off or bundled into the receptionist setup.
- **Reality check:** it is time-for-money, DM conversion is 1-3%, and $1,000 for a salon that can get Booksy for $0-$30/mo is fantasy. Fine as a 2-week cash test, not a business. Never use scraped photos in a public preview before they say yes.

### 3. Marketing stack for Haji's own apps (marketingskills + gstack + hook-scoring + Remotion) -- income 2 (indirect), fit 5, hours 1-2
No direct revenue, but it multiplies whatever the apps already earn and costs almost nothing.
- Today: `claude plugin marketplace add coreyhaines31/marketingskills` and run pricing, offers, launch, and aso against one existing app. Install gstack and run /office-hours on the receptionist offer before building it.
- This week: hooks.json from TikTok Studio export (60-day limit) and a `score-hooks` skill on Haiku (paid by the monthly credits). Write hooks by hand, use AI only to rank, per the creator's own A/B result.
- Later: one Remotion template for 20-second product demos (free license at his size).
- **Reality check:** none of this matters without traffic; it is 3-5 hours/week of hygiene, not a plan.

### 4. Free money: monthly API credits + Startups program -- income 0 (cost offset $1,200-$2,400/yr), fit 5, hours 0.2
- Link the Console org the apps use; route AI features through it; spend the balance monthly (it does not roll over).
- Apply to Startups with a company-domain email; expect the partner stack only (ElevenLabs year, Granola, ClickHouse) while the Team/credit tier is over capacity.
- **Reality check:** credits do not pay for Claude Code sessions and will not change the income picture; they just make the apps cheaper to run.

### 5. Veteran-owned government contracting pipeline (SAM.gov API + Claude drafting, human submission) -- income 1 in 90 days, fit 4, hours 2
Highest ceiling, slowest start. VOSB/SDVOSB set-asides are a real moat the TikTok crowd does not have.
- This month: SAM.gov registration, SBA VetCert application, capability statement. Build a Claude Code skill that pulls the SAM Opportunities API and scores fit; route 200-page solicitations to a cheap model for triage, Claude for the judgment calls.
- **Reality check:** 90-180+ days to a first award, lots of compliance paperwork, and never let an agent log into or submit on a portal (ToS violation that can cost the registration). The creator burned all his tokens in two hours doing exactly that.

**Explicitly not in the top 5 yet:** Claude-run Meta ads (no product with margin, no ad budget, affiliate-distorted numbers; revisit at >$1k MRR with proven organic content) and the C-file tool (see Gaps; legal structure first).

## Gaps: things they talk about that Haji has not liked yet but should look at

- **gstack** (not in the liked set): /office-hours and /plan-ceo-review are the missing "should I build this at all" gate; pairs with marketingskills.
- **Meta's official Ads CLI/MCP** and the Marketing API Access Tier rename (2026-05-04): Limited Access covers your own account with a system-user token in under an hour; Full Access (client accounts) needs 500 calls/15 days and business verification. Know this before any agency ad offer.
- **The C-file analysis idea.** Competitors exist for law firms (VBMS Reviewer, Page), a consumer service launched 2026-08-06 (VetsForever's The Readout), and an MCP for BVA outcomes (VetAid). The buildable, lawful version is B2B tooling for accredited attorneys/VSOs or a free self-service indexer; a paid direct-to-veteran service is claim-shark territory unless Haji gets VA accreditation. Validate with three accredited attorneys before writing code.
- **Retell's solution-partner directory** and similar reseller programs: a lead source for play #1 that none of the videos mention.
- **TikTok Studio CSV export** as the compliant replacement for Apify when scoring hooks.
- **PostHog free tier** on every landing page now, so that the behavioural-email layer has data when there is traffic.
- **Cal.com** (open source) as the booking backend for both #1 and #2 instead of pretending a static file can book.

## Open questions

1. Which Bland tier actually includes the in-call SMS node and the appointment-scheduling node? The compare table shows dashes in two of three columns; this decides whether the demo is reproducible on the free tier.
2. Will the Claude for Startups Team-year and $1,000 credit reopen, and does an existing Max subscriber count as "new to Team"? The page no longer states the condition.
3. Is Jev open for signups today (console returned 403 anonymously; reports conflict for Sep 20-22)? Is it measurably better than Haiku structured output on a 4-way classification? Needs a 50-example test.
4. What is the real retention of AI receptionist clients after month three? No operator data found; the only way to learn is to sell three and watch.
5. Does the jasoncooperson template contain anything beyond a Bland pathway JSON? Only obtainable through his comment funnel; low value either way.
6. Can Haji's veteran status be used ethically in the receptionist pitch and in SAM.gov set-asides without crossing into the claim-shark zone on any veteran-facing product? Needs a one-hour read of 38 CFR 14.629/14.636 and his state's law before any veteran-facing offer.
7. What does The Board prompt's citation gate do when an advisor has thin public writing? Test with one obscure advisor before trusting any "sourced" verdict.
