# TikTok Likes → Folders → AI Research: Every Step, Start to Finish

Goal: every liked video sorted into a saved folder, Likes tab cleaned out, and a dashboard that tells you which AI coding tools and techniques from those videos are worth using in our apps and why.

Legend: **YOU** = something you do. **ME** = I do it, you do nothing.

---

## Part 1 — Setup (YOU, one time)

**Step 1. Unblock tiktok.com for this chat. DONE and verified 2026-10-09.**

**Step 2. Install the Claude in Chrome extension (3 minutes, skip if you already have it).**
Open Google Chrome → go to the Chrome Web Store → search "Claude in Chrome" → Add to Chrome → sign in with your Claude account → click the puzzle-piece icon in Chrome's toolbar → click the pin next to Claude.
*Why:* TikTok has no official way for a program to save or unlike videos. The only way is clicking inside your own logged-in Chrome. This extension is what lets me click.

**Step 3. Turn the extension on inside the Claude desktop app (1 minute).**
Open the Claude desktop app on your Mac (update it first if it asks) → click your initials in the lower-left corner → Settings → Connectors → find "Claude in Chrome" → Configure → switch it on.
*Why:* this tells the desktop app it is allowed to use your Chrome.

**Step 4. Start the browser session in the desktop app (1 minute).**
In the Claude desktop app: start a new conversation. If the message box shows "Chat" and "Cowork", pick Cowork. If it does not show those, just start the conversation. Open the "+" (or Connectors) menu in the message box and turn on Claude in Chrome for this conversation (it is off by default every time). Make sure TikTok is open and logged in, in Chrome. Then paste this:

> You are working in my real Chrome through Claude in Chrome. TikTok is open and I am logged in. Go to my profile and open the Liked tab. Scroll all the way to the bottom until no more videos load. Collect every video link on that tab. Then open the Saved tab, note the names of every folder (collection) I have, and collect every video link in each folder with its folder name. Save everything as a plain text file on my Desktop called tiktok_links.txt, one line per video in the form: liked|<link>  or  saved|<folder name>|<link>. Do not like, unlike, save, or change anything. Tell me when the file is ready and how many links you found.

*Why:* the Liked tab is private to you, so only a browser logged in as you can see it. This gives me the full list.

**Step 5. Drop the file into THIS chat (10 seconds).**
When the desktop session says the file is ready, drag `tiktok_links.txt` from your Desktop into this chat and send it.
*Why:* this chat is where the reading, sorting and research happens. That file is the hand-off.

**Step 1b (optional, any time). Request your TikTok data export.** Phone → TikTok → Profile → ☰ → Settings and privacy → Account → Download your data → JSON → Request. Not needed to start. It arrives in a few days and is only the backup copy of your liked list.

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

**Step 11. Hand the sorting file to the desktop session (YOU, 10 seconds).**
I give you a file called `tiktok_sort.txt` (video link → folder). Drag it into the desktop app conversation from Step 4 and send: "Create any folders in this file that do not exist yet, then for each line: open the video, Save it to that folder, confirm it appears in the folder, write the result to tiktok_log.txt on my Desktop, then Unlike it. Do 25, then stop and show me the log." 
*Why:* the clicking can only happen in your Chrome, and the desktop app is the only thing connected to it.

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
