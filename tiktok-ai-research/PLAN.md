# TikTok AI-Video Research Pipeline — Plan v0 (awaiting Haji's answers)

Date: 2026-10-09. Branch: `claude/tiktok-video-ai-research-yeiwkd`. Status: research done, nothing executed.

## BLUF

Yes, this is doable, but in two very different halves:

| Half | Feasible? | How | Blocker today |
|---|---|---|---|
| **Read & analyze** every liked / saved / own video (transcript, on-screen text, hashtags, creator, stats) and research the AI ones | **Yes** | TikTok data export + `yt-dlp` + Whisper + Claude vision on frames | This cloud container cannot reach tiktok.com (network policy). Fixable in environment settings, or run on Haji's Mac. |
| **Write back** to TikTok (create folders, save videos, unlike) | **Yes, but only via a browser logged in as Haji** | Claude in Chrome or the desktop-app browser, human-paced | No browser linked to this session; TikTok has no API for this and its terms forbid automation. |

Fastest first move: **request the TikTok data export (JSON) today** — it takes 1–4 days to arrive and nothing downstream starts without it.

## Capability answers (what Haji asked)

| Question | Answer | Verified / Assumed |
|---|---|---|
| Can you list all my liked, saved, and own videos? | Yes. The "Download your data" export (JSON) has a Likes list and a Favorite Videos list, each entry = date + link. Own posted videos are listed too. **Collection (folder) names are NOT in the export.** Folders are read separately: `yt-dlp` has a `tiktok:collection` extractor, or we read them in the browser. | Export fields: ASSUMED (third-party guides; TikTok does not document the layout). `yt-dlp` collection extractor: VERIFIED in source. |
| Can you see the video? | Not as a live video. I download the mp4, pull frames (about 1 per second plus scene changes) and read them with Claude vision. That catches CapCut text, overlays, arrows, "look at this" flashes, UI screenshots, URLs on screen. | VERIFIED: Claude vision reads images; 100–600 images per API request; downscale to ≤2000 px per side when sending >20. |
| Can you read the words / subtitles? | Yes, two ways. (1) TikTok's own auto-captions when they exist (`yt-dlp` extracts them, free, instant). (2) Whisper transcript of the audio as fallback or cross-check. | VERIFIED: `yt-dlp` TikTok extractor pulls `auto_captions` and `cla_info` subtitles. `faster-whisper` installs and runs on CPU in this container. |
| Can you speed it up to 2x? | Not needed. I never watch in real time. A 60-second clip processes in roughly 20–60 s of CPU time for transcription plus one vision call for frames. | ASSUMED timing (faster-whisper `small` on 4 CPUs, no GPU). |
| Hashtags? | Yes, from the description text. Also creator handle, music, view/like/save counts, post date. Comments skipped as requested. | VERIFIED in `yt-dlp` source. |
| Go into the creators' accounts? | Yes. `yt-dlp` `tiktok:user` lists a creator's whole public feed with descriptions. I classify those by text first, then deep-extract only the AI-related ones. | VERIFIED extractor exists; `_WORKING` for user feed is true as of master. |
| Save AI videos to a folder, then unlike? | Only through a browser signed in as Haji. No official API (Display API = own public posts only; Zapier TikTok = ads only). Process must be: create folder → save → **verify** saved → log → only then unlike. | VERIFIED: no API path. Browser path: Claude in Chrome or desktop-app built-in browser (skills present on this account). |
| Is ChatGPT better? | For the TikTok login/write half: no, same wall. For raw video understanding: Google Gemini accepts video natively, which is the one real advantage over the frames+transcript pipeline. For 15–90 s clips the pipeline is equivalent, and keeping it in Claude keeps extraction, research, dashboard and repo in one workflow. | Honest opinion, not benchmarked. |
| Skills / plugins needed? | None to install from a catalog. Tools: `yt-dlp` (installed, v2026.08.19), `faster-whisper` (installed), `ffmpeg` (present). The browser skills (`chrome-browser`, `built-in-browser`, `computer-use`) are already on this account but only activate when a session is linked to Haji's computer. | VERIFIED in this container. |

## What I tested today

| Check | Result |
|---|---|
| `curl https://www.tiktok.com` from this container | **403 — blocked by environment network policy** (also `tiktokcdn.com`) |
| Browser tools in this session | None attached (no `claude-in-chrome`, no `remote-devices`) |
| `pip install yt-dlp faster-whisper` | OK (2026.08.19; faster-whisper imports) |
| `ffmpeg` | Present. `tesseract` absent (not needed — Claude vision reads frames) |
| `ANTHROPIC_API_KEY` in container | Not set. Only matters if we run analysis as a standalone batch script; in-session I can read frames directly. |
| Zapier TikTok actions | Only Lead Generation / Conversions (ads). Useless here. |
| Connectors / skills for TikTok | None. |
| `yt-dlp` TikTok health | Challenge-solving breakage in March 2026 was fixed (issue #16199 closed via PR #16223). Expect to occasionally need `yt-dlp --update-to master`. |

## Architecture

```
TikTok export JSON ──► Phase 1 inventory (SQLite/CSV: id, url, source, date)
                              │
                              ▼
            Phase 2 metadata pass (yt-dlp --skip-download, all videos)
            description, hashtags, creator, stats, captions-available
                              │ text classifier: AI-coding / AI-tools / business / other / unsure
                              ▼
            Phase 3 deep extraction (AI + unsure only)
            mp4 ─► captions or Whisper ─► transcript
            mp4 ─► ffmpeg frames (1 fps + scene cut) ─► Claude vision ─► on-screen text, tools shown, URLs
            ─► per-video JSON: tools, claims, steps, links, "implement?" score
                              │
                              ▼
            Phase 4 creator expansion (tiktok:user feeds of AI creators) ─► same classify/extract
                              │
                              ▼
            Phase 5 research per tool/technique (web) ─► verdict: use now / watch / skip, tied to our apps
                              │
                              ▼
            Phase 6 dashboard (claude.ai artifact, data from repo JSON)
                              │
                              ▼
            Phase 7 TikTok housekeeping in Haji's browser: folder ─► save ─► verify ─► log ─► unlike
```

### Phase details

| Phase | What | Where it runs | Needs from Haji |
|---|---|---|---|
| 0 | Request export (Settings → Account → Download your data → **JSON**). Note current folder names. | Haji's phone | 2 minutes |
| 1 | Parse export → master inventory. Dedupe liked ∩ saved. Raw export stays out of git (it contains DMs and search history). | Cloud or Mac | Upload the zip |
| 2 | Metadata for every video, no download. Text-only classification. | Needs TikTok network access | Network fix or Mac |
| 3 | Deep extraction for AI + unsure videos. Transcript + frames + structured JSON. | Same | — |
| 4 | Creator feeds of every AI creator; classify; deep-extract AI ones. Gap analysis vs. what Haji liked. | Same | Cap per creator (default: last 100 posts) |
| 5 | Web research per tool/technique. | Cloud | — |
| 6 | Dashboard artifact: filter by category, tool, creator, verdict, score. | Cloud | — |
| 7 | Browser session: create collections, save, verify, unlike. Batches of ~25, slow, first batch with Haji watching. | Haji's Mac (Claude in Chrome or desktop-app browser) | Be present for batch 1 |

### Categories (first draft, to be refined after Phase 2)

AI – Coding agents & workflows · AI – Tools & models · AI – Business/automation · Business/marketing · Faith/personal · Other. Saved-folder names will mirror the categories we keep.

## Safety and data custody

- Never unlike before a verified save. Every write action logged (video id, action, timestamp, verified yes/no). Re-runnable without double-acting.
- Raw export, cookies, session files: never committed. `.gitignore` added when Phase 1 starts.
- Browser actions are human-paced (seconds between actions, batch caps). TikTok terms prohibit automation; the account-risk decision is Haji's (see Question 5).
- No sends, no deletes of videos, no posting. Unliking is reversible (we keep the full liked list).

## Rough cost / time (ASSUMED, to be measured on the first 20 videos)

| Item | Estimate |
|---|---|
| Metadata pass | ~1–2 s per video, no model cost |
| Transcript | ~0.3–0.8× real time on CPU (`small` model). 500 × 45 s clips ≈ 2–5 CPU hours |
| Vision | ~10–30 frames per video at ~1000 px → roughly 15k–40k input tokens per video |
| Browser housekeeping | ~15–25 s per video, human-paced → 500 videos ≈ 3 hours across several sessions |

## Council split (reported as required)

- **Skeptic / Ethicist:** the write-back half (Phase 7) is the only part that touches Haji's account standing. Recommend doing it last, in small supervised batches, and keeping the option to skip unliking entirely (liked list is a harmless archive; the folders are what give organization).
- **Strategist:** time-box Phases 3–5 to the AI category first, exactly as Haji asked; the business category waits.
- **Innovator:** the metadata pass alone (Phase 2) will classify most videos correctly from description + hashtags at near-zero cost; deep extraction only where text is thin. This probably cuts deep-extraction volume by more than half.
- **Pragmatist:** the export delay (1–4 days) is the critical path. Request it today. In parallel, fix network access or decide to run on the Mac.

## Open questions for Haji

See the chat message (same list, numbered 1–8).

## Sources checked

- TikTok Display API scopes (own public videos only): https://developers.tiktok.com/doc/display-api-overview/
- yt-dlp TikTok extractor source (captions, user, collection extractors): https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/tiktok.py
- yt-dlp TikTok challenge fix, closed March 2026: https://github.com/yt-dlp/yt-dlp/issues/16199
- Claude vision limits and token math: https://platform.claude.com/docs/en/build-with-claude/vision
- Closest prior art, TikTok saved-video pipeline (export → yt-dlp → faster-whisper → OCR → Claude): https://github.com/mattthomas7641/saved-video-intelligence
- Export-based liked/bookmarked downloader (Playwright-based TikTok-Api): https://github.com/samirelanduk/tiktok-save
- Export layout, third-party guides: https://www.scrolldecoded.com/blog/tiktok-data-export-guide/ · https://aitrove.app/export-tiktok-favorites/ · https://www.getphyllo.com/post/how-to-download-tiktok-data-see-everything-the-app-knows-about-you
- Claude in Chrome overview: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome.md
- Cloud environment network access: https://code.claude.com/docs/en/cloud-environments#network-access
