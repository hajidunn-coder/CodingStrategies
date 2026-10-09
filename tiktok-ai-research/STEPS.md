# TikTok Likes → Folders → AI Research: Every Step, Start to Finish

Goal: every liked video sorted into a saved folder, Likes tab cleaned out, and a dashboard that tells you which AI coding tools and techniques from those videos are worth using in our apps and why.

Legend: **YOU** = something you do. **ME** = I do it, you do nothing.

---

## Part 1 — Setup (YOU, one time, about 15 minutes total)

**Step 1. Request your TikTok data export (phone, 2 minutes).**
Open TikTok → Profile → ☰ (top right) → Settings and privacy → Account → Download your data → choose **JSON** (not TXT) → Request data.
*Why:* this gives me TikTok's official list of every video you ever liked and saved. It is the safety net. When we unlike hundreds of videos, this file proves nothing was lost. It takes 1 to 4 days to arrive. When it does, download it on your phone and upload the zip into this chat.

**Step 2. Unblock tiktok.com for this chat (20 seconds).**
At the top of this chat, click the environment name in the title bar → Edit → Network access. If there is a "full" or "unrestricted" option, pick it. If it only allows adding domains, add `tiktok.com`, `tiktokv.com`, `tiktokcdn.com`, `tiktokcdn-us.com`, `ttwstatic.com`, keep "Allow package managers" checked, save.
*Why:* my machine is currently blocked from TikTok. Unblocking lets me pull each video file, read every frame and every word, then delete it. This is the fast, highest quality way to know what is in a video.

**Step 3. Install and open the Claude desktop app on your Mac (3 minutes, skip if already installed).**
Download from claude.ai/download, install, sign in with the same account you use here, leave it open.
*Why:* this app is the bridge between this chat and your Mac. Without it, I cannot reach your Chrome.

**Step 4. Have TikTok open and logged in, in Chrome, with the Claude in Chrome extension installed and signed in (2 minutes).**
Chrome → TikTok.com → make sure you are logged in → open your profile → Liked tab. Check the Claude extension icon shows you signed in.
*Why:* TikTok has no official way for a program to save or unlike videos. The only way is clicking inside your own logged-in browser. The extension is what lets me click.

**Step 5. Link your Mac to this chat (10 seconds).**
In the box where you type to me, tap **+** → **Devices** → pick your Mac → send me the word "linked".
If there is no Devices option: open the Claude desktop app → new Cowork chat → paste: "Continue the TikTok project from repo hajidunn-coder/CodingStrategies, branch claude/tiktok-video-ai-research-yeiwkd. Read tiktok-ai-research/STEPS.md and start at Step 6." Then do the rest there.
*Why:* this is the moment my tools for your Chrome switch on.

---

## Part 2 — Sorting every liked video into folders

**Step 6. Inventory (ME, 10 minutes).**
I open your Liked tab and your Saved tab in Chrome, scroll to the bottom of each, and record every video link plus the names of your existing folders.
*Why:* I need the full list before I sort anything, and I need your current folder names so I keep them and add new ones beside them.

**Step 7. Quality proof on one video (ME, then YOU, 2 minutes).**
I pull one video from your Likes and show you exactly what I got: words spoken, words on screen, hashtags, creator, music, view count, and my one-line summary.
*You:* say "good" or tell me what is missing.
*Why:* you judge the quality once, before I run it on hundreds.

**Step 8. Read every liked video (ME, runs in the background, a few hours for hundreds).**
For each video: fetch the file, pull frames and audio, read every word, write a small text record, delete the file. Then I assign each video a category.
*Why:* this is how every video gets sorted on what it actually contains, not just its caption. No video files are kept. The text records live in the repo and feed the dashboard later.

**Step 9. Approve the folder list (YOU, 2 minutes).**
I show you the proposed new folders with counts, for example: AI – Coding & Agents (87), AI – Tools & Models (41), Business & Marketing (63), Faith & Personal (30), Other (19). Your existing folders stay.
*You:* approve, rename, merge, or split. One message.
*Why:* they are your folders. You should recognize the names when you open TikTok.

**Step 10. Review the unsure pile (YOU, 5 minutes, optional).**
I list the videos I could not confidently place, with a one-line summary each.
*You:* tell me where they go, or say "you decide".

---

## Part 3 — Doing the work inside TikTok (needs your Mac on, Chrome open)

**Step 11. Create the new folders (ME, 2 minutes).**
In your Chrome, I create each approved folder.

**Step 12. Batch 1, 25 videos, you watch (ME, YOU present, about 10 minutes).**
For each video: open it → Save → pick the folder → open the folder and confirm the video is there → write it to the log → Unlike. Human pace, a few seconds between clicks.
*Why you watch:* if TikTok shows a captcha or something looks wrong, we catch it on video 3, not video 300. Unlike never happens before a verified save.

**Step 13. Remaining batches (ME, 25 at a time, about 15 to 25 seconds per video).**
Same loop. I pause and ping you only if TikTok throws a captcha or blocks an action.
*Why in batches:* TikTok's rules forbid automation. Slow and steady keeps your account safe.

**Step 14. Final check (ME, then YOU, 2 minutes).**
I confirm: Likes tab empty (except any you told me to keep), every video in exactly one folder, log matches the inventory from Step 6 and the export from Step 1.
*You:* open TikTok, look at your folders, enjoy the clean Likes tab.

---

## Part 4 — Deep dive on the AI folder

**Step 15. Full extraction on every AI video (ME).**
For each AI video, a structured record: tools and products named, claims made, steps shown, links or repos on screen, prompts shown, and a score for "worth implementing in our apps".
*Why:* this turns a pile of videos into a searchable list of ideas with evidence.

**Step 16. Creator expansion (ME).**
For every creator in the AI folder, I read their last 50 posts, keep the AI-related ones, extract them the same way, and list what they cover that you did not already like.
*Why:* you asked for gaps. The creators you liked once usually have 5 more posts on the same subject.

**Step 17. Research each tool and technique (ME).**
Web research per item: what it is, is it real and maintained, cost, does it fit our stack, risks. Verdict: Use now / Watch / Skip, with reasons tied to our apps.

**Step 18. Dashboard (ME, then YOU).**
A hosted page you open in any browser: filter by folder, tool, creator, verdict, score. Click a row to see the transcript, on-screen text, and the research.
*You:* open it, tell me what to change.

**Step 19. Keep it running (optional, later).**
Weekly: new likes get read, sorted, saved, unliked, and added to the dashboard automatically. Business folder gets its own deep dive when you say go.

---

## What you end up with

1. Likes tab: empty.
2. Saved folders: your old ones untouched, new ones holding every video, sorted by what is actually in it.
3. A dashboard of every AI idea from those videos, researched, with a Use / Watch / Skip verdict.
4. A repo with the text records, so this never has to be done from scratch again.
5. No video files stored anywhere.

## Your total hands-on time

Setup ~15 min. Approvals ~10 min. Watching batch 1 ~10 min. Everything else is me.
