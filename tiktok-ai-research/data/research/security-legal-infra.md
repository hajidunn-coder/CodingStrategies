# Security, legal and infra for vibe-coded apps: what to consider

Theme: `security-legal-infra` (10 liked videos, plus 4 adjacent videos on Strix, Scrapling and Apify that the brief asked to cover). Facts checked on the web 2026-10-10; dates are noted inline. Companion verdict rows: `security-legal-infra.json`.

## What the creators are collectively saying (patterns, not individual videos)

1. **"Claude wrote it, nobody reviewed it" is the root problem.** Every security video (kevinfremon, bengusberg x2, ducktate) lists the same five or six holes: exposed secrets, missing permission/owner checks, unprotected Supabase tables, unvalidated input, vulnerable packages, weak login flows. They agree on the diagnosis because it is correct and matches OWASP and the Feb 2026 Moltbook leak (exposed key + no RLS).
2. **The legal exposure is real and cheap to fix, so creators package it as a checklist.** millee.md's 20 items and ducktate's 3 items overlap heavily: privacy policy, ToS, cookie notice, consent before tracking, data deletion, accessibility.
3. **"AI defaults to Supabase and Vercel; ask why."** alanonai's three videos are one message: own the infra decision, understand cost at scale and the exit path. No tooling, just a habit.
4. **Monetisation pattern.** Half the videos sell something: kevinfremon sells AppBully, bengusberg's three videos are follow-bait with a recycled "Stanford founder, raised $4M" intro and unverifiable claims (800x, 818 skills, 1.5B free tokens), ducktate funnels softly to a Mac app but the content is free and sourced. alanonai promotes an article series not located.
5. **"Paste the link into Claude" is a recurring fake how-to.** Claude cannot watch TikTok. Three bengusberg videos end with it. The real step is pasting the list as text, which this document does.

## What holds up vs what is hype (with evidence)

**Holds up**

- Supabase tables without RLS are open. Supabase's own docs: "A table in an exposed schema without RLS is readable and writable by any role with a grant on it." Two gotchas creators skip: views bypass RLS (security definer), and old `anon`/`authenticated` grants survive adding policies. From 2026-10-30 Supabase makes new tables require an explicit grant (per ducktate quoting the Supabase changelog; changelog not fetched directly). The `anon`/`service_role` keys are being replaced by `sb_publishable_`/`sb_secret_` with the old ones deprecated by end of 2026 (same source).
- The six login gaps are real for hand-rolled auth, but Supabase Auth already does four of them: bcrypt+salt hashing, OTP/reset expiry (default 3600 s, docs recommend 1 h or lower), per-IP rate limits (30 req/5 min on signup/recover/magic link), optional CAPTCHA (Turnstile/hCaptcha), email confirmation toggle. Leaked-password protection (HaveIBeenPwned) needs the Pro plan ($25/mo).
- PostHog session replay is **not** off at the SDK level. `disable_session_recording` defaults to `false`; `opt_out_capturing_by_default` defaults to `false`; inputs are masked by default but page text is not. CIPA statutory damages are $5,000 per violation (Cal. Penal Code 637.2), which matches the creator's "$5K" figure; the Ninth Circuit revived a session-replay CIPA claim (Bloomingdale's, unpublished).
- Vercel Hobby is "for personal, non-commercial use" (pricing page). Pro is $20/seat + usage, overage from $0.15/GB, "uncapped" unless you set Spend Management (default $200 on-demand budget, optional auto-pause hard limit). Attack Challenge Mode is free on all plans and blocked requests are not billed. Bill-shock stories in 2026 are about defaults (Turbo build machines, $659 community thread Apr 2026) and uncapped overage during attacks ($23k write-up, Jun 2026, secondhand).
- Strix is a real, active (PyPI 1.7.0 on 2026-10-05, commits 2026-10-08), Apache-2.0 dynamic pentest agent. It needs Docker and your own LLM key and must only be run on systems you own.
- ducktate.com/learn is free with no signup; 11 stages, 144 sourced items, per-stage Claude Code audit prompts; facts checked 2026-10-09.
- General-Legal/legal-templates (CC0, ~2.7k stars, attorney-drafted) exists and covers privacy-policy-us, privacy-policy-gdpr, terms-of-use, cookie-notice, DPAs.
- Supabase compliance: SOC 2 Type 2, ISO 27001, HIPAA via BAA (Team $599/mo add-on or Enterprise), GDPR DPA, self-hosting via Docker Compose (community-supported). So the "business requirements Supabase may not handle" worry is mostly answered.
- Legal fine figures that check out: FTC fake-review rule and CAN-SPAM up to $53,088 per violation/email; CCPA $2,663 / $7,988 per violation (2025 CPI adjustment); CA Unruh $4,000 per accessibility violation. WCAG 2.1 AA is the de facto court standard for private sites; 3,117 federal website suits in 2025 (Seyfarth figure via vendor blogs).

**Hype or wrong**

- "AppBully monitors and finds vulnerabilities" is marketing for a static pattern check plus OSV plus a wrapper over Supabase's free Security Advisor. The product is honest about this ("not a full security audit or a live attack test"). The $29 one-time beta pass is fair, but the free equivalents exist.
- "Anthropic-Cybersecurity-Skills" is not Anthropic's; the README says so. Content is SOC/forensics/Entra ID/Kubernetes, nothing named for Supabase, JWT or web OWASP in the sampled tree. Last commits (Aug 2026) are contributor-wall chores. The "install into ChatGPT" claim is meaningless (no skills folder).
- Scrapling's "800x faster" is its own HTML-parser micro-benchmark vs BeautifulSoup, not fetching. "Bypasses Cloudflare" is the maintainers' claim and is the behaviour that creates ToS/contract and CFAA exposure.
- OmniRoute's "1.5B free tokens" is a self-computed sum of 17 provider free tiers; the project itself tags 13 providers `tos: avoid`. Prompts go to whatever upstream is picked.
- "$25 per violation" for missing legal docs (ducktate): no statute found with that number; treat as unverified.
- "Cookie consent banner" as a universal must: a US-only app with only strictly necessary cookies does not need one; US state laws are opt-out (honor Global Privacy Control in CA). It becomes mandatory with EU/UK visitors plus analytics or ads.
- "Encrypt PII or you get sued": no general US statute mandates field-level encryption; the practical reason is breach-notification safe harbor for encrypted data, and it only matters for genuinely sensitive fields.
- "Abstract every DB call to stay portable": fights Supabase's main benefit (browser queries guarded by RLS) and RLS policies are plain Postgres anyway. Wrapping auth behind one module is the cheap, sensible part.
- AIOS dashboard: no code, LAN-only phone access, follow-bait.

## How we should approach this in our own apps and workflow (concrete, ordered, with tradeoffs)

Principle: Haji is one person. Prefer defaults that make the dangerous thing impossible (RLS on, secret key server-only, spend cap on) over checklists that must be remembered. Run the whole list once per app before the first real user; rerun the starred items on every significant push.

### PRE-LAUNCH CHECKLIST for a vibe-coded app (security, legal, infra)

Legend: **Why** / **With Claude Code** (prompt or command) / **Verify**. Items marked * are the ones to repeat on every push.

**A. Data and secrets (do first; a leak here hurts users immediately)**

1. **RLS on every exposed table, with per-operation policies and revoked default grants.** *
   Why: Supabase docs: tables without RLS are readable and writable by anyone with a grant; adding policies does not remove grants; views bypass RLS. Moltbook, Feb 2026.
   With Claude Code: "List every table and view in `supabase/migrations`. Write one migration that, per table: `enable row level security`, `revoke all ... from anon, authenticated`, grants only the operations the app uses, and adds separate `select/insert/update/delete` policies using `(select auth.uid()) = user_id`. For each view, recreate it with `security_invoker = true`. Then write `supabase/tests/<table>_rls.test.sql` (pgTAP) asserting allow and deny for `anon` and `authenticated`."
   Verify: `supabase test db` passes; Dashboard > Advisors > Security shows zero RLS/exposed-view warnings; a curl with the publishable key and no JWT returns `[]` on a private table.

2. **No secret/service-role key reaches the client.** *
   Why: the publishable key is only safe because of RLS; the secret key skips RLS entirely.
   With Claude Code: `npm run build && grep -rE "sb_secret_|service_role|SUPABASE_SERVICE" .next/static dist build .vercel/output 2>/dev/null` and "Any env var holding a secret must not start with `NEXT_PUBLIC_`/`VITE_`/`EXPO_PUBLIC_`; move all secret usage into one server-only module `lib/server/admin.ts` and fail the build if that module is imported from a client component."
   Verify: grep returns nothing; `git log -p | grep -c sb_secret_` is 0 (rotate the key in the dashboard if not); add `gitleaks` or GitHub secret scanning.

3. **Owner check on every mutation (authorization, not just authentication).** *
   Why: kevinfremon's "scariest" hole; AppBully's own demo finding; IDOR is what Strix finds first.
   With Claude Code: "For every API route, server action and Edge Function that reads or writes a row by id, show the line that proves the row belongs to the caller (`.eq('user_id', user.id)` or an RLS policy). Produce a table route -> check -> file:line. Fix any row that has no proof."
   Verify: run Strix (item 8) or manually hit a route with user B's session and user A's id; expect 403/404.

4. **Supabase project hardening from the official going-to-prod list.**
   Why: official checklist, five minutes of clicking.
   With Claude Code: ask it to print the dashboard path for each: SSL enforcement on, Network Restrictions on, MFA on your Supabase account and GitHub, second org owner, email confirmations on, OTP/reset expiry <= 3600 s, custom SMTP (built-in provider is 2 emails/hour), CAPTCHA on signup/OTP, leaked-password protection (Pro).
   Verify: Security Advisor clean; `supabase/config.toml` values committed where supported.

5. **Supabase MCP only against a dev project, read-only.**
   Why: Supabase's Sep 2025 post: prompt injection through stored data "remains the number one concern" even in read-only mode.
   With Claude Code: `claude mcp add supabase -- npx -y @supabase/mcp-server-supabase --read-only --project-ref <DEV_REF>`; never register the prod ref.
   Verify: `claude mcp list` shows only the dev ref.

**B. Code-level security**

6. **Dependencies: audit and pin.** *
   Why: #1 on kevinfremon's list; what AppBully sends to OSV.
   With Claude Code: `npm audit --audit-level=high` (or `pnpm audit`), enable Dependabot/Renovate; "Fix every high/critical by upgrading; if a fix needs a major bump, list the breaking changes first."
   Verify: `npm audit` exits 0 at high; Dependabot PRs appear.

7. **Input validation and injection review on the full repo.** *
   Why: unvalidated forms, raw SQL in Postgres functions, dangerouslySetInnerHTML.
   With Claude Code: run `/security-review` on the pending diff for every PR, and once before launch: "Act as `/security-review` over the entire repo, not only the diff: injection, XSS, SSRF, authZ, secrets, insecure deserialization. Report file:line, severity, fix." Add `anthropics/claude-code-security-review` as a PR Action (trusted PRs only; it is not hardened against prompt injection).
   Verify: findings list is empty or every item is marked reviewed with a reason in a `SECURITY_REVIEW.md`.

8. **Dynamic test with Strix on local/staging, never prod.**
   Why: static review cannot prove an IDOR; Strix exploits it and shows a PoC.
   With Claude Code: `curl -sSL https://strix.ai/install | bash`; `export STRIX_LLM=anthropic/<model> LLM_API_KEY=...`; seed a test user; `strix -n --target http://localhost:3000` (or `strix --target ./`). Then: "Read `strix_runs/<latest>/` and fix each validated finding; explain each fix in one line."
   Verify: rerun Strix; no critical/high remains. Budget a few dollars of tokens per run.

9. **Rate limiting beyond auth (API routes, AI endpoints, email senders).**
   Why: Supabase Auth throttles sign-in, but your own `/api/generate` or Stripe webhook does not; bots and runaway loops produce both abuse and bills.
   With Claude Code: "Add per-user and per-IP rate limiting to every public API route (Upstash Ratelimit or Vercel WAF rules), plus a hard cap on AI tokens per user per day. Return 429 with Retry-After."
   Verify: `ab -n 200 -c 20` against the route shows 429s; Vercel Firewall rule visible.

**C. Legal and consent (do before the first sign-up, not the first dollar)**

10. **Privacy policy and Terms of Service from attorney templates, filled from the real code.**
    Why: required by app stores, OAuth providers (Google/Apple sign-in), Stripe, and state privacy laws; AI-drafted text without a template invents data categories.
    With Claude Code: `git clone https://github.com/General-Legal/legal-templates ../legal-templates`; "Using `../legal-templates/templates/privacy-policy-us/template.md` and `terms-of-use/template.md`, generate `/privacy` and `/terms` pages. Fill every `<mark>` field from the code: list every table that stores personal data, every third-party SDK and its purpose, retention, and contact details. Add business name, address and contact email in the footer." Use `privacy-policy-gdpr` if EU/UK users are expected.
    Verify: pages linked in footer and in sign-up form; data categories in the policy match `supabase/migrations` and `package.json`; business details present.

11. **Refund/cancellation policy and subscription rules (if you charge).**
    Why: ROSCA and California ARL require clear auto-renew disclosure and easy cancellation; Stripe and app stores require a refund statement.
    With Claude Code: "Add `/refunds` stating the refund window and how to cancel; show price, renewal interval and cancel link on the checkout page and in the receipt email; add a one-click cancel in account settings (Stripe Customer Portal)."
    Verify: a test subscription can be cancelled in two clicks without emailing support.

12. **Consent before analytics/session replay; honor GPC; cookie banner only if needed.**
    Why: CIPA $5,000 per violation, hundreds of suits in 2025; PostHog replay records unless disabled; US-only + essential cookies needs no banner, EU/UK visitors + analytics do.
    With Claude Code: `posthog.init(key, { opt_out_capturing_by_default: true, disable_session_recording: true, maskAllInputs: true, maskTextSelector: '*', cookieless_mode: 'on_reject' })`; on accept `posthog.opt_in_capturing(); posthog.startSessionRecording()`. "Find every analytics/replay/pixel init in the repo and prove nothing fires before consent; treat `navigator.globalPrivacyControl === true` as opt-out; add a cookie policy page if any non-essential cookie exists."
    Verify: open DevTools Network on a fresh profile; no `/e/`, `/s/` or replay requests before clicking accept; `document.cookie` shows only essential cookies.

13. **Data deletion and export path.**
    Why: CCPA/GDPR right to delete; Apple requires in-app account deletion; cheap to build, painful to retrofit.
    With Claude Code: "Add Settings > Delete account: server action using the secret key that deletes the auth user and cascades every table with `user_id` (write `on delete cascade` FKs where missing), revokes sessions, and emails confirmation. Add a `/privacy-requests` mailto for export."
    Verify: delete a test account; `select count(*) from <every user table> where user_id = ...` returns 0.

14. **Marketing email hygiene and kids' data.**
    Why: CAN-SPAM up to $53,088 per email; unsubscribe within 10 business days; physical address required. COPPA for under-13.
    With Claude Code: "Every marketing email template must include an unsubscribe link wired to a suppression list and a postal address; transactional emails exempt. If the product is not for children, add a 13+ (or 16+ for GDPR) checkbox/age gate at sign-up and state it in the ToS."
    Verify: send a test campaign; unsubscribe works and is reflected in the DB; age gate visible.

15. **Dark patterns, fake reviews, unsupported claims, hidden fees.**
    Why: FTC fake-review rule up to $53,088 per violation; FTC warning letters in 2025-2026.
    With Claude Code: "Scan every marketing page and onboarding step. Flag: testimonials without a real source, numeric claims without a citation, pre-ticked upsells, fees shown only at checkout, confirm-shaming copy, countdown timers not backed by a real deadline. Rewrite or remove."
    Verify: a page-by-page list with 'kept with evidence' or 'removed' for each flag.

16. **Accessibility to WCAG 2.1 AA, measured.**
    Why: 3,117 federal website suits in 2025; Unruh $4,000 per violation; overlays rejected by courts.
    With Claude Code: `npx @axe-core/cli http://localhost:3000 --tags wcag2a,wcag2aa` and Lighthouse accessibility; "Fix every axe violation: alt text, contrast >= 4.5:1, visible focus, keyboard reachability for every control, form labels, skip link."
    Verify: axe reports 0 violations on the top 5 pages; tab through checkout without a mouse.

17. **Licenses for fonts, images, icons, dependencies.**
    Why: millee.md item 19; copyleft or no-license assets are a takedown risk.
    With Claude Code: `npx license-checker --summary` and "List every font/image/icon in `public/` and `app/` with its source and license; replace anything without a commercial license."
    Verify: a `LICENSES.md` in the repo.

**D. Infra and cost**

18. **Vercel Pro (not Hobby) for anything commercial, spend cap on day one.**
    Why: Hobby is non-commercial by ToS; overage is uncapped without Spend Management; Turbo build machines default on Pro.
    With Claude Code: ask it to print the steps: Settings > Billing > Spend Management: alert at ~1.5x expected bill, hard limit (pause projects) at ~3x; Settings > Build: Standard machine; Firewall: enable Attack Challenge Mode when under attack. Add `output: 'standalone'` and a Dockerfile so the exit path is tested.
    Verify: Spend Management shows a hard limit; `docker build . && docker run -p 3000:3000` serves the app locally.

19. **Infra decision log in CLAUDE.md.**
    Why: alanonai's habit, made automatic: cost at 1k/10k/100k users and the exit path for every vendor.
    With Claude Code: add to CLAUDE.md: "Before proposing or adding infra (Supabase, Vercel, Stripe, PostHog, any API), state: monthly cost at 1k/10k/100k users, what is proprietary vs portable, and the migration path. Keep schema as plain SQL migrations. All auth calls go through `lib/auth.ts`. Only `lib/server/admin.ts` may use the secret key. Prefer Postgres functions over Edge Functions."
    Verify: `grep -n "1k/10k/100k" CLAUDE.md`.

20. **Backups, point-in-time recovery, breach clock.**
    Why: ducktate stage 1: breach-notice clocks start at discovery (72 h under GDPR); Supabase Pro has daily backups, PITR is an add-on.
    With Claude Code: "Write `INCIDENT.md`: how to rotate the secret key, revoke all sessions (`auth.admin.signOut` for all), restore from backup, and whom to notify within 72 h. Add a weekly `pg_dump` GitHub Action to private storage."
    Verify: a restore drill on the dev project succeeds once.

21. **Make it stick: `/prelaunch` skill.**
    Why: the only way a solo founder repeats this on app #4.
    With Claude Code: create `.claude/skills/prelaunch/SKILL.md` containing items 1-20 as a checklist that outputs a table of item / evidence (file:line or dashboard screenshot name) / pass-fail, and run it from the ducktate Stage 11 rules block.
    Verify: the skill is in the project, output table has 21 rows, no 'unknown'.

Tradeoffs to accept: masking all replay text reduces its value (keep replay for logged-in flows only); a hard Vercel limit can pause the site under a legitimate traffic spike (set it generously and watch alerts); Strix costs tokens and time; a lawyer pass on policies is still required for health, kids or finance verticals.

## Gaps: things they talk about that Haji has not liked yet but should look at

- **ducktate's Launch Readiness stages 7-10** (AI-feature disclosure under the EU AI Act and California's companion-chatbot law, DMCA agent and TAKE IT DOWN Act if users upload content, ROSCA/click-to-cancel, TCPA for SMS). None of the liked videos cover these and every Haji app with an AI feature or user content hits at least one.
- **Supabase's 2026-10-30 grant change and key migration** (`sb_publishable_`/`sb_secret_`, anon key deprecated end of 2026). Any app scaffolded before then will throw permission errors on new tables; the lazy fix Claude will suggest (`grant all to anon`) is the wrong one.
- **Claude Code's built-in `/security-review` and the PR Action.** The creators sell scanners around a feature Haji already has.
- **Vercel Spend Management and Attack Challenge Mode.** The lock-in videos never mention that the actual bill risk has a switch.
- **Secret scanning in CI** (gitleaks / GitHub secret scanning + push protection) and key rotation; the videos stop at "don't expose keys".
- **Global Privacy Control**: a browser signal California treats as a legal opt-out; cheaper to honor than to litigate.

## Open questions

- Supabase changelog for the 2026-10-30 explicit-grant change and the new key format was reported via ducktate (checked 2026-10-09), not fetched from supabase.com; confirm on the changelog before relying on dates.
- Next.js Adapter API "stable in 16.2 (March 2026)" comes from third-party blogs; verify in Next.js release notes before counting on it for the exit path.
- Strix per-run token cost on a typical Next.js + Supabase app is unmeasured; the $3.37/challenge figure is from a third-party benchmark write-up.
- AppBully's false-positive rate and what its "Database" check adds over the Supabase Security Advisor is unknown without connecting a real project.
- Which repo ducktate meant by "open-source legal templates" is unconfirmed; General-Legal/legal-templates is the strongest candidate.
- CCPA applicability thresholds (revenue/consumer counts) were not re-verified this pass; treat the CCPA items as "if it applies" until checked.
- Search budget ran out before confirming PostHog's dedicated GDPR/consent guide text and the Apify Claude connector's exact MCP install string; both are referenced in their docs but were not read directly.
