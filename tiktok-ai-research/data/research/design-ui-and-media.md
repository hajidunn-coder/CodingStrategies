# Design, UI and media: what to consider

Theme: design-ui-and-media. 10 liked videos, 7 creators. Research date: 2026-10-10. Every "verified" item below was checked against the official site, GitHub metadata (via the GitHub API) or Anthropic's own pages on that date; third-party numbers are marked as such.

## What the creators are collectively saying (patterns, not individual videos)

1. **Design slop is the known weakness of vibe-coded products, and the fix is a text file.** Four of the ten videos push the same mechanism: give the agent a written design brief (a `DESIGN.md` from getdesign.md, a `SKILL.md` like Impeccable or Taste Skill, an "Apple design language" skill) so it stops reaching for the default layout. Nobody argues for Figma anymore; the argument is about which markdown file to install.
2. **Reference, then remix.** The most substantive video (chase_ai_, 16 min) and the shortest ones agree: start from a real site you admire (Land Book, Twitter, a competitor), extract or clone its structure, then re-skin with your brand. The clone is scaffolding, not the deliverable.
3. **Media generation is being bolted onto the coding agent.** Higgsfield's MCP/CLI shows up in four videos as the way Claude Code gets hero images and video (Seedream for a still, Seedance for motion, Nano Banana as an alternative). The claim is "Claude builds the whole site including media".
4. **Free copy-paste component sites are the "hidden gems" filler.** Componentry, Motion Primitives, 21st.dev, Haikei, Realtime Colors: all real, all cheap, all presented as 30-second tips between sponsored segments.
5. **"One prompt, $10k website" is a funnel, not a method.** Two near-identical videos (nateherkai, forcceee_) recycle the same example sites and gate the "prompt pack" behind a comment or DM. A third (lucca.the.develop) is a silent showcase with "DM for workflow". None demonstrates a build.
6. **Sponsored no-code pitches ride along.** Both kaithevibecoder videos carry `#manuspartner`; Manus is positioned as "hands down the best" builder. That is paid placement.
7. **One video is pure product-polish craft** (JPLoft's five UX features) and it is the most directly applicable content in the batch for someone shipping apps rather than landing pages.
8. **Anthropic's own design surface is real and moving fast.** "Claude Design" in the videos is a real product; since then it has been folded into Claude and Claude Code got a `/design` skill.

## What holds up vs what is hype (with evidence)

**Holds up**

- **Impeccable** (pbakaus/impeccable): 79,261 stars, Apache-2.0, pushed 2026-10-09, free. Real tooling for Claude Code: hooks, a slop detector, ~25 focused commands, PRODUCT.md/DESIGN.md context. The best-maintained design skill that exists.
- **Taste Skill** (Leonxlnx/taste-skill): 94,317 stars, MIT, pushed 2026-10-09, free. 13 skills; v2 is marked experimental. Real, but it overlaps Impeccable almost completely. The "do they conflict?" question is not settled by anyone's data; mechanically they are two rulebooks, so pick one as default.
- **DESIGN.md catalogs**: VoltAgent/awesome-design-md has 120,134 stars, MIT, pushed 2026-10-05; getdesign.md lists 550+ files and follows Google's DESIGN.md spec (originated by Google Stitch). The "Awesome Claude Design" repo Mariah refers to is VoltAgent/awesome-claude-design (4,028 stars, 68 files, last commit 2026-06-20, stale). The files are fan analyses of public sites, not licensed brand tokens.
- **Emil Kowalski's skills** (emilkowalski/skills): 44,954 stars, MIT, pushed 2026-10-02. Includes `apple-design` ("Apple's principles for interface design and fluid motion, distilled from WWDC talks, translated for the web"), which matches the unnamed "Apple design language skill" video almost word for word and is the credible option among several small Apple-HIG repos (s1gmamale1: 26 stars; ykswang: 1 star).
- **Component sites**: Componentry (584 stars, MIT, Vercel OSS program, shadcn CLI), Motion Primitives (6,512 stars, MIT, Motion + Tailwind), 21st.dev (12,000+ components, free browse + 2 copies/day, Builder $6/mo yearly), Haikei (free, unlimited SVG, commercial OK, no updates since ~2022), Realtime Colors (free forever, CSS/SCSS export). All as described.
- **clone-site / remix-site** (cth9191/site-clone): 141 stars, MIT, created and last pushed 2026-08-21. README matches the video exactly. Playwright pixel-diff QA is real (0.00% on the Plinth example). Tweak panel is dev-only (backtick key), so it does not ship. The chase_ai_ walkthrough is the only honest demonstration in the set and it shows 30+ minutes of work, not one prompt.
- **Higgsfield MCP/CLI/skills**: official (higgsfield.ai/mcp; higgsfield-ai/skills 1,251 stars, MIT, pushed 2026-09-26). Exposes Seedance 2.5/2.0, Seedream 5.0, Nano Banana Pro, GPT Image 2, Kling 3, Veo 3.1. Higgsfield's own blog (2026-08-06): Seedance 2.5 needs the $49 plan; an 8-second 720p clip costs 52 credits (~$2.55), ~19 clips a month. Higgsfield tells Claude Code users to use the CLI + skills rather than the MCP connector.
- **Claude Design**: launched by Anthropic Labs 2026-04-17 (Opus 4.7, Pro/Max/Team/Enterprise). Now lives inside Claude as artifacts on Free/Pro/Max/Team/Enterprise; the standalone claude.ai/design closes 2026-12-14. Claude Code's `/design` skill (research preview, v2.1.234+, August 17-21 2026) publishes editable artboards and implements the one you pick. Not creator shorthand.
- **Claude Motion**: real, beta, **Team and Enterprise only** (support article updated 2026-10-09). Code-based animations to MP4, no video model. Not available to a Pro/Max user.
- **Models**: Seedance 2.0 (Feb 2026, global rollout paused March 2026 after studio complaints) and Seedance 2.5 (~2026-07-31, 30s clips) are real. Nano Banana 2 = Gemini 3.1 Flash Image (2026-02-26; 2.1 update 2026-10-06). Seedream 5.0 Lite/Pro live on Higgsfield.
- **JPLoft's five UX rules**: standard patterns, compatible with TanStack Query-style optimistic mutations. Nothing to debunk.

**Hype or broken**

- **"$10k website from one prompt"**: no demonstration anywhere; identical scripts and example sites across two creators; comment-gated. The working version of this idea (reference URL + design skill + iteration + one generated hero) is in chase_ai_'s video and costs time, tokens and Higgsfield credits.
- **"CDANCE 2.0"**: does not exist. It is the caption engine's rendering of "Seedance 2.0".
- **"Free templates from React Video Editor"**: the Pro Remotion templates sit behind a $149 (non-commercial Hobby) or $499 (Startup, commercial) one-time licence; only a stale MIT "lite" editor (last push 2024-12) is free. Mariah's "free" framing does not hold for commercial use.
- **Manus "hands down the best"**: sponsored (`#manuspartner`). Real product (Free: 300 daily credits on 2.0 Lite; Pro from $20/mo for 4,000 credits), but it hosts the app for you and credit cost per task is unpredictable. It competes with Claude Code rather than complementing it.
- **Antigravity in the burger-site stack**: real, free for individuals, but adds nothing over Claude Code for the task shown; it is a second agent IDE.
- **"Clone any website" in Claude Design**: Claude Design has a web-capture tool for grabbing elements and can imitate a style; it is not a pixel clone. The real pixel clone is the site-clone skill, and that one copies the target's CSS, which is a copyright problem until you remix it.
- **"Stanford founder, raised $4M, repo URL never shown"**: lead-gen; use Emil's skill instead.
- **Opal** (Google): shutting down as a Labs product 2026-11-17; workflows stop running. Do not build on it.

## How we should approach this in our own apps and workflow (concrete, ordered, with tradeoffs)

The goal is a minimal, free, repo-local "anti-slop" stack that every new Claude Code project inherits. Order matters: constraints first, assets second, media last.

### Step 0: house style once (30 min)
1. Pick a palette at https://www.realtimecolors.com (background, text, primary, secondary, accent; check the contrast lights), Export > CSS.
2. Clone `https://github.com/VoltAgent/awesome-design-md`, pick one DESIGN.md whose *structure* fits (Linear/Vercel for dashboards, Framer/Lovable for marketing), copy it to the repo root as `DESIGN.md`, replace its tokens with your Realtime Colors values and your fonts (check font licences; SF Pro is Apple-platform only).
3. Add to `CLAUDE.md`: "All UI follows DESIGN.md. Do not introduce colors, radii or type sizes not defined there."
Tradeoff: a borrowed DESIGN.md looks like its source until you edit it; spend the 20 minutes editing.

### Step 1: install the three skills (10 min, per machine)
```
npx impeccable install              # choose Claude Code; adds hooks + detector + /impeccable commands
npx skills@latest add emilkowalski/skills   # animate, review-animations, apple-design, pick-ui-library
```
Then inside Claude Code in each project: `/impeccable init` (writes PRODUCT.md: audience, goals), and run `/impeccable audit` on the current UI once to see what the detector flags.
Install Taste Skill too, but only for an A/B: `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend`. Build the same page both ways, keep one as the default auto-loaded skill and invoke the other by name only. Do not let both auto-load.
Tradeoff: every design skill adds context on UI turns; Impeccable's hooks only fire on web files, which is the right scope.

### Step 2: UX standards block in CLAUDE.md (5 min)
Paste the JPLoft five as rules Claude must follow on every screen: skeleton loaders that mirror layout; prefill any field the app already knows; optimistic mutations with rollback (TanStack Query `onMutate`/`onError`); persist drafts, filters and carts (URL or localStorage, never secrets); every network failure shows a plain-language message with a retry and preserves user input. This is the highest ROI item in the whole batch for product apps.

### Step 3: design before building (per feature)
Use Claude Code's `/design <brief>` (v2.1.234+) to get artboards, pick one, then "implement option N following DESIGN.md". For marketing pages, give a reference URL as "visual inspiration" in the same prompt. Iterate 3-5 times; that is the realistic version of the "one prompt" videos.
Tradeoff: artifacts usage counts against the plan; use it for screens that matter (onboarding, pricing, dashboard home), not every modal.

### Step 4: components and motion from vetted sources
- Base on shadcn/ui. Pull a signature piece from Motion Primitives or Componentry via the shadcn CLI (`npx shadcn@latest add @componentry/<name>`), then ask Claude to restyle to DESIGN.md tokens.
- Browse 21st.dev free; pay $6/mo only if copying weekly.
- Run `/review-animations` (Emil) after adding motion; rule of thumb from the skill: UI animations under 300 ms, ease-out on enter.
- Haikei for a background SVG when a screen is empty; commit the SVG.
Tradeoff: showy components hurt product UIs; keep them to marketing pages and one accent per screen.

### Step 5: reference sites, remix, never ship a clone (marketing only)
Install cth9191/site-clone (`cp -r skills/* ~/.claude/skills/`, needs Playwright). Keep a taste vault file of URLs/screenshots. Run `/clone-site <url>` with `--analyze-only` first (a couple of minutes, gives you TEARDOWN.md and tokens), and only do the full clone + `/remix-site` when a page is worth 30-45 minutes. Ship only the remixed direction.
Tradeoff: the clone copies the target's CSS and downloads its fonts; the remix phase replaces logos, people, product shots and licensed fonts, and that is the legal line. Repo has had no commits since 2026-08-21, so expect to maintain it yourself.

### Step 6: generated media, only when a page needs it
- Stills: a 20-line Gemini API script (Nano Banana 2/Pro) from https://aistudio.google.com is cheaper than a Higgsfield plan.
- Video hero: Higgsfield CLI + skills (`higgsfield auth login`, `npx skills add higgsfield-ai/skills`), lowest plan that includes the model (Seedance 2.5 requires the $49 tier; ~$2.55 per 8-second 720p clip). Generate the still first with dead space for copy, animate once, serve the still on mobile.
- Product/launch videos: HyperFrames (`npx skills add heygen-com/hyperframes`, 60k stars, Apache-2.0) renders HTML to MP4 locally. Skip React Video Editor's paid templates; Claude Motion is Team/Enterprise only.
Tradeoff: credits and model availability change monthly; keep generated assets in the repo so a vendor change does not break the site.

### Explicitly skip
Manus (sponsored, hosted lock-in), Antigravity (second IDE, no design gain), Opal (shutting down), React Video Editor licence (not needed), comment-gated "prompt packs".

## Gaps: things they talk about that Haji has not liked yet but should look at

- **Claude Code `/design` skill** (research preview since 2026-08-17): the creators show the standalone Claude Design app; the in-terminal version is the one that fits Haji's workflow and none of the liked videos cover it.
- **Emil Kowalski's skills** (44.9k stars): the Apple video is almost certainly selling this repo without naming it; the animation review/audit skills are the missing motion half of anti-slop.
- **HyperFrames** (heygen-com/hyperframes, 60k stars, daily commits): agent-native product videos; replaces the RVE-template trick and sidesteps Claude Motion's Team-only gate.
- **SkillUI** (amaancoderx/skillui, 251 stars, stale since 2026-04-14): `npx skillui <url>` to extract DESIGN.md/ANIMATIONS.md/LAYOUT.md from Haji's own existing apps; Impeccable's `/impeccable extract` and `document` do the same inside Claude Code, so it is optional.
- **open-slide** (9.1k stars, MIT, active): decks as React in the repo with `/create-slide`; relevant for investor/client decks under version control.
- **Google Stitch**: free Labs tool that invented the DESIGN.md spec; useful to bootstrap a DESIGN.md for a brand-new product when there is no reference.
- **Taste Skill's `stitch-skill` and style variants** (soft/minimalist/brutalist): quick way to give a client a mood option without a designer.
- **Performance and conversion of 3D-scroll heroes**: none of the creators mention Lighthouse, CLS or mobile data; a scroll-scrubbed frame sequence (the burger site) is dozens of MB. Any marketing page Haji ships should serve a still on mobile and be measured.
- **Licensing hygiene**: fonts named in DESIGN.md files, component licences on 21st.dev (per author), and cloned CSS all need a 2-minute check before a public launch.

## Open questions

1. Impeccable vs Taste Skill when both are installed: no public benchmark; needs a one-afternoon A/B on one of Haji's real pages (same prompt, same DESIGN.md).
2. Token cost of Claude Code `/design` and of max-effort multi-page builds on Haji's plan: not measured by any creator; worth logging on the first two uses.
3. Higgsfield's current plan prices: the pricing page is JS-rendered; the $49 Seedance-tier figure is from Higgsfield's own August 2026 blog, third parties list $19/$47/$99 tiers. Confirm at checkout before subscribing.
4. Whether cth9191/site-clone will be maintained (single-day history) or whether a more active alternative (ogabrielalonso/website-cloner, faisalg22/ai-site-cloner) should be the pick; neither was evaluated here.
5. Legal line for DESIGN.md "inspirations": following layout principles is fine; shipping a recognisable Apple/Stripe/Spotify look for a product invites trade-dress complaints. No creator addresses this.
6. When Claude Motion reaches Pro/Max (or if Haji moves to Team): it would replace HyperFrames for simple explainers.
7. Whether the burger site (lucca.the.develop) was AI-generated end to end: unknowable from the video; treat it as a showcase, not a method.
