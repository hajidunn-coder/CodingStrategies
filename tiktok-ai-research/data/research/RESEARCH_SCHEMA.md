# Research output per theme
Write TWO files to /home/user/CodingStrategies/tiktok-ai-research/data/research/:
1. <theme>.json — a list of tool/technique verdict rows:
   {"name": "...", "kind": "product|repo|skill|plugin|api|model|course|pattern|program",
    "official_url": "...", "exists": "verified|unverified|does-not-exist|renamed", "evidence": "what you checked (stars, last commit date, pricing page, docs)",
    "cost": "free|freemium|$X/mo|usage-based|unknown", "maintained": "active|stale|abandoned|n-a",
    "what_it_does": "one sentence", "claimed_in_videos": "what creators claimed", "reality_check": "where the claim holds or breaks",
    "verdict": "USE NOW|TRY THIS WEEK|WATCH|SKIP", "why": "tied to a solo founder building apps/businesses with Claude Code",
    "how_to_adopt": "concrete first step, command or URL", "risks": "lock-in, ToS, security, hype", "source_video_ids": ["..."]}
2. <theme>.md — a narrative 'what to consider' guide for Haji, structured as:
   ## What the creators are collectively saying (patterns, not individual videos)
   ## What holds up vs what is hype (with evidence)
   ## How we should approach this in our own apps and workflow (concrete, ordered, with tradeoffs)
   ## Gaps: things they talk about that Haji has not liked yet but should look at
   ## Open questions
Rules: verify on the web before calling anything "verified". Prefer official docs/GitHub over blogs. Record dates. Be blunt about affiliate/sponsored pitches. No fluff.
